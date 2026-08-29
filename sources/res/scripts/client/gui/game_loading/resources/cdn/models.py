from datetime import datetime
import typing
from typing import Optional, Union
import ResMgr
from dict2model.models import Model as BaseConfigModel
from gui.game_loading import loggers
from gui.game_loading.resources.cdn.consts import MIN_SLIDES_COUNT_TO_VIEW, SequenceCohorts
from gui.game_loading.resources.consts import ImageVfxs
from gui.game_loading.resources.models import LocalImageModel
from helpers import getClientLanguage, time_utils
from web.cache.web_cache import generateKey
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.cdn.consts import SequenceOrders
    from gui.game_loading.resources.cdn.cache import GameLoadingCdnCache
_logger = loggers.getCdnConfigLogger()

class LocalSlideModel(LocalImageModel):
    __slots__ = (b'additionalImage', b'sound', b'_historyKey')

    def __init__(self, imageRelativePath, vfx=None, localizationText=None, descriptionText=None, minShowTimeSec=0, transition=0, additionalImage=None, sound=None):
        super(LocalSlideModel, self).__init__(imageRelativePath=imageRelativePath, vfx=vfx, localizationText=localizationText, descriptionText=descriptionText, minShowTimeSec=minShowTimeSec, transition=transition)
        self.additionalImage = additionalImage
        self.sound = sound
        self._historyKey = generateKey(self.imageRelativePath)
        return

    @property
    def historyKey(self):
        return self._historyKey

    @staticmethod
    def isDownloaded(*args):
        return True


class LocalSequenceModel(object):
    __slots__ = (b'name', b'order', b'slides')

    def __init__(self, name, order, slides):
        self.name = name
        self.order = order
        self.slides = list(slides)
        return

    @property
    def minSlidesCountToView(self):
        return max(len(self.slides), 1)

    def __repr__(self):
        return (b'<LocalSequenceModel(name={}, slides={})>').format(self.name, len(self.slides))


class AdditionalImageModel(BaseConfigModel):
    __slots__ = (b'image', b'width', b'height', b'margins', b'paddings', b'position', b'pathInCache')

    def __init__(self, *args, **kwargs):
        super(AdditionalImageModel, self).__init__(*args, **kwargs)
        self.image = kwargs.get(b'image', b'')
        self.width = kwargs.get(b'width', 0)
        self.height = kwargs.get(b'height', 0)
        self.margins = kwargs.get(b'margins', (0, 0, 0, 0))
        self.paddings = kwargs.get(b'paddings', (0, 0, 0, 0))
        self.position = kwargs.get(b'position', (0, 0))
        self.pathInCache = None
        return


class ConfigSlideModel(BaseConfigModel):
    __slots__ = (b'image', b'vfx', b'localization', b'additionalImage', b'sound', b'_imageCacheKey', b'_localizationCacheKey', b'_cacheKeysToUrls', b'_langCode')

    def __init__(self, image, vfx, localization, additionalImage, sound):
        super(ConfigSlideModel, self).__init__()
        self.image = image
        self.vfx = vfx
        self.localization = localization
        self.additionalImage = additionalImage
        self.sound = sound
        self._imageCacheKey = generateKey(self.image)
        self._cacheKeysToUrls = {(self._imageCacheKey): (self.image)}
        if self.additionalImage:
            additionalImageUrl = self.additionalImage.image
            self._cacheKeysToUrls[generateKey(additionalImageUrl)] = additionalImageUrl
        if self.localization:
            self._localizationCacheKey = generateKey(self.localization)
            self._cacheKeysToUrls[self._localizationCacheKey] = self.localization
        else:
            self._localizationCacheKey = None
        self._langCode = getClientLanguage()
        return

    @property
    def historyKey(self):
        return self._imageCacheKey

    @property
    def urls(self):
        return list(self._cacheKeysToUrls.values())

    def isDownloaded(self, fileCache):
        currentCacheKeys = set(fileCache.getLoaded())
        return currentCacheKeys.issuperset(set(self._cacheKeysToUrls))

    def convertToLocal(self, fileCache, minShowTimeSec=0, transition=0):
        if not fileCache:
            _logger.warning(b'File cache object missing.')
            return
        else:
            localImagePath = fileCache.getRelativePath(self.image)
            if not localImagePath:
                _logger.warning(b'Image file for url [%s] is missing.', self.image)
                return
            if self.additionalImage:
                self.additionalImage.pathInCache = fileCache.getRelativePath(self.additionalImage.image)
            localizationText = None
            descriptionText = None
            if self.localization:
                localLocalizationPath = fileCache.get(self.localization)
                if not localLocalizationPath:
                    _logger.warning(b'Localization file for url [%s] is missing.', self.localization)
                    return
                localizations = ResMgr.openSection(localLocalizationPath)
                if localizations:
                    titleSection = localizations[b'title']
                    if titleSection:
                        localizationText = titleSection.readString(self._langCode, default=None)
                    descriptionSection = localizations[b'description']
                    if descriptionSection:
                        descriptionText = descriptionSection.readString(self._langCode, default=None)
                    _logger.debug(b'Localization for lang [%s] is [%s] [%s].', self._langCode, localizationText, descriptionText)
            return LocalSlideModel(imageRelativePath=localImagePath, vfx=self.vfx, localizationText=localizationText or None, descriptionText=descriptionText or None, minShowTimeSec=minShowTimeSec, transition=transition, additionalImage=self.additionalImage, sound=self.sound)

    def __repr__(self):
        return (b'<ConfigSlideModel(image={}, vfx={}, localization={})>').format(self.image, self.vfx, self.localization)


class ConfigSequenceModel(BaseConfigModel):
    __slots__ = (b'name', b'start', b'finish', b'priority', b'order', b'views', b'enabled', b'cohorts', b'slides')

    def __init__(self, name, order, slides, start, finish, priority, views, enabled, cohorts):
        super(ConfigSequenceModel, self).__init__()
        self.name = name
        self.order = order
        self.slides = list(slides)
        self.start = start
        self.finish = finish
        self.priority = priority
        self.views = views
        self.enabled = enabled
        self.cohorts = list(cohorts or SequenceCohorts.getDefaults())
        return

    @property
    def isActive(self):
        utcnow = datetime.utcfromtimestamp(time_utils.getServerUTCTime())
        return (self.enabled) and (self.start) <= utcnow < self.finish

    @property
    def minSlidesCountToView(self):
        return min(max(len(self.slides), 1), MIN_SLIDES_COUNT_TO_VIEW)

    def __repr__(self):
        return (b'<ConfigSequenceModel(name={}, active={}, priority={}, slides={})>').format(self.name, self.isActive, self.priority, len(self.slides))


class ConfigModel(BaseConfigModel):
    __slots__ = (b'enabled', b'sequences')

    def __init__(self, enabled, sequences):
        super(ConfigModel, self).__init__()
        self.sequences = sequences
        self.enabled = enabled
        return

    def __repr__(self):
        return (b'<ConfigModel(enabled={}, sequences={})>').format(self.enabled, len(self.sequences))


class CdnCacheDefaultsModel(object):
    __slots__ = (b'sequence', b'minShowTimeSec', b'transition')

    def __init__(self, sequence, minShowTimeSec=0, transition=0):
        self.sequence = sequence
        self.minShowTimeSec = minShowTimeSec
        self.transition = transition
        return

    def __repr__(self):
        return (b'<CdnCacheDefaultsModel(slides={}, minShowTimeSec={}, transition={})>').format(len(self.sequence.slides), self.minShowTimeSec, self.transition)


class CdnCacheParams(object):
    __slots__ = (b'configUrl', b'cohort')

    def __init__(self):
        self.configUrl = None
        self.cohort = None
        return

    @property
    def isItemsCacheParamsReady(self):
        return bool(self.cohort)

    @property
    def isServerSettingsParamsReady(self):
        return bool(self.configUrl)

    @property
    def isReady(self):
        return self.isItemsCacheParamsReady and self.isServerSettingsParamsReady

    def reset(self):
        self.configUrl = None
        self.cohort = None
        return

    def __repr__(self):
        return (b'<CdnCacheParamsModel(configUrl={}, cohort={})>').format(self.configUrl, self.cohort)
