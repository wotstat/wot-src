import typing
from gui.game_loading import loggers
from gui.game_loading.resources.cdn.consts import SequenceOrders
from gui.game_loading.resources.cdn.models import LocalSlideModel, LocalSequenceModel, CdnCacheDefaultsModel
from gui.game_loading.resources.consts import ImageVfxs, MilestonesTypes, LoadingTypes, Milestones, InfoStyles
from gui.game_loading.resources.models import StatusTextModel, LogoModel
from gui.game_loading.state_machine.models import ImageViewSettingsModel
from gui.game_loading.state_machine.const import DEFAULT_SLIDE_DURATION, DEFAULT_LOGIN_NEXT_SLIDE_DURATION, DEFAULT_LOGIN_STATUS_MIN_SHOW_TIME_SEC, DEFAULT_SLIDE_TRANSITION_DURATION, ContentState
from gui.game_loading.state_machine.models import LoadingMilestoneModel, ProgressSettingsModel
from helpers import getClientLanguage
from helpers.i18n import makeString
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from ResMgr import DataSection
_logger = loggers.getLoaderSettingsLogger()
DEFAULT_TAG = b'default'

class GameLoadingSettings(object):
    __slots__ = (b'_settings', b'_ageRatingPath', b'_lang')

    def __init__(self, settings):
        self._settings = settings
        self._ageRatingPath = None
        self._lang = getClientLanguage()
        return

    def getLogos(self):
        logoListSection = self._settings[b'logoList']
        if logoListSection is None:
            return []
        else:
            logos = []
            infoStyleValues = InfoStyles.values()
            for logoData in logoListSection.values():
                info = b''
                style = InfoStyles.DEFAULT
                infoDatas = logoData[b'info']
                if infoDatas is not None:
                    infoData = None
                    if infoDatas.has_key(self._lang):
                        infoData = infoDatas[self._lang]
                    elif infoDatas.has_key(DEFAULT_TAG):
                        infoData = infoDatas[DEFAULT_TAG]
                    if infoData is not None:
                        info = infoData.readString(b'text')
                        styleValue = infoData.readString(b'style')
                        if styleValue:
                            if styleValue not in infoStyleValues:
                                _logger.warning(b'Not supported info style: %s not in %s.', styleValue, infoStyleValues)
                            else:
                                style = InfoStyles(styleValue)
                logos.append(LogoModel(logoType=logoData.readInt(b'type', 0), minShowTimeSec=logoData.readFloat(b'duration', 0), showCopyright=logoData.readBool(b'showCopyright', False), showVersion=logoData.readBool(b'showVersion', False), transition=int(logoData.readFloat(b'transitionDuration', 0) * 1000), info=makeString(info) or b'', infoStyle=style))

            return logos

    def getLoginNextSlideDuration(self):
        return self._settings.readFloat(b'loginNextSlideDuration', DEFAULT_LOGIN_NEXT_SLIDE_DURATION)

    def getCdnCacheDefaults(self):
        slideDuration = self._settings.readFloat(b'slideDuration', DEFAULT_SLIDE_DURATION)
        slideTransitionDuration = int(self._settings.readFloat(b'slideTransitionDuration', DEFAULT_SLIDE_TRANSITION_DURATION) * 1000)
        defaultSlideListSection = self._settings[b'defaultSlideList']
        defaultSlideList = [] if defaultSlideListSection is None else defaultSlideListSection.values()
        slides, vfxValues = [], ImageVfxs.values()
        for slideSection in defaultSlideList:
            image = slideSection.readString(b'image')
            if not image:
                _logger.error(b'Empty image section, slide will be skipped.')
                continue
            vfx = None
            vfxValue = slideSection.readString(b'vfx') or None
            if vfxValue is not None:
                if vfxValue not in vfxValues:
                    _logger.warning(b'Not supported vfx value: %s not in %s.', vfxValue, vfxValues)
                    vfx = None
                else:
                    vfx = ImageVfxs(vfxValue)
            slide = LocalSlideModel(imageRelativePath=image, localizationText=makeString(slideSection.readString(b'title') or b''), descriptionText=makeString(slideSection.readString(b'description') or b''), vfx=vfx, minShowTimeSec=slideDuration, transition=slideTransitionDuration)
            slides.append(slide)

        if not slides:
            _logger.error(b'Default sequence id empty.')
        sequence = LocalSequenceModel(name=b'__static__', order=SequenceOrders.RANDOM, slides=slides)
        return CdnCacheDefaultsModel(sequence=sequence, minShowTimeSec=slideDuration, transition=slideTransitionDuration)

    def getStatusTexts(self):
        statusTextDuration = self._settings.readFloat(b'statusTextDuration', DEFAULT_SLIDE_DURATION)
        statusTextListSection = self._settings[b'statusTextList']
        if statusTextListSection is None:
            return []
        else:
            return [StatusTextModel(text=makeString(text.asString), minShowTimeSec=statusTextDuration) for text in statusTextListSection.values()]

    def getProgressSettingsByType(self, loadingType):
        loadingTypeSection = self._getLoadingTypeSection(loadingType)
        if loadingTypeSection is None:
            raise SoftException(b'Wrong progress settings.')
        settingsSection = loadingTypeSection[b'settings']
        if settingsSection is None:
            raise SoftException(b'No "settings" section for progress.')
        return ProgressSettingsModel(startPercent=settingsSection.readInt(b'startPercent', 0), limitPercent=settingsSection.readInt(b'limitPercent', 100), ticksInProgress=settingsSection.readInt(b'ticksInProgress', 1000), minTickTimeSec=settingsSection.readFloat(b'minTickTimeSec', 0))

    def getProgressMilestones(self, loadingType):
        loadingTypeSection = self._getLoadingTypeSection(loadingType)
        if loadingTypeSection is None:
            raise SoftException(b'Wrong progress settings.')
        milestoneSection = loadingTypeSection[b'milestones']
        if milestoneSection is None:
            return {}
        else:
            milestonesForTypes = {}
            for rawMilestonesType, rawMilestones in milestoneSection.items():
                milestonesType = rawMilestonesType
                milestonesTypes = MilestonesTypes.values()
                if milestonesType not in milestonesTypes:
                    _logger.error(b'Unknown milestonesType: %s, Available: %s', milestonesType, milestonesTypes)
                    continue
                milestonesForType = milestonesForTypes.setdefault(MilestonesTypes(milestonesType), {})
                for milestoneSection in rawMilestones.values():
                    milestoneName = milestoneSection.readString(b'name')
                    milestones = Milestones.values()
                    if milestoneName not in milestones:
                        _logger.error(b'Unknown milestone: %s, Available: %s', milestoneName, milestones)
                        continue
                    status = StatusTextModel(text=makeString(milestoneSection.readString(b'text')), minShowTimeSec=DEFAULT_LOGIN_STATUS_MIN_SHOW_TIME_SEC)
                    milestoneName = Milestones(milestoneName)
                    milestonesForType[milestoneName] = LoadingMilestoneModel(name=milestoneName, percent=milestoneSection.readInt(b'percent'), forceApply=milestoneSection.readBool(b'forceApply'), status=status)

            defaultMilestones = milestonesForTypes.get(MilestonesTypes.CONNECTION)
            if defaultMilestones is None:
                raise SoftException(b'Default milestones type should be in settings.')
            if not defaultMilestones:
                raise SoftException(b'At list one milestone should be in settings.')
            return milestonesForTypes

    def getClientLoadingStateViewSettings(self):
        return self._getStateViewSettings(b'clientLoading')

    def getLoginStateViewSettings(self):
        return self._getStateViewSettings(b'login')

    def getPlayerLoadingStateViewSettings(self):
        return self._getStateViewSettings(b'playerLoading')

    def _getStateViewSettings(self, state):
        statesSection = self._settings[b'states']
        if statesSection is None:
            _logger.warning(b'No states section can be found')
            return ImageViewSettingsModel()
        else:
            stateSection = statesSection[state]
            showVfx = False
            contentState = ContentState.INVISIBLE
            ageRatingPath = self._getAgeRatingPath()
            info = b''
            hasVignette = True
            if stateSection is not None:
                showVfx = stateSection.readBool(b'showVfx', False)
                contentStateValue = stateSection.readInt(b'contentState', ContentState.INVISIBLE.value)
                info = makeString(stateSection.readString(b'info') or b'')
                hasVignette = stateSection.readBool(b'hasVignette', hasVignette)
                if contentStateValue not in ContentState.values():
                    _logger.warning(b'Not supported contentState value for %s state: %s not in %s.', state, contentStateValue, ContentState.values())
                else:
                    contentState = ContentState(contentStateValue)
            else:
                _logger.warning(b'No section can be found for %s view state', state)
            return ImageViewSettingsModel(showVfx=showVfx, contentState=contentState, ageRatingPath=ageRatingPath, info=info, hasVignette=hasVignette)

    def _getAgeRatingPath(self):
        if self._ageRatingPath is None:
            self._ageRatingPath = b''
            ageRatingPathData = self._settings[b'ageRatingPath']
            if ageRatingPathData is not None:
                if ageRatingPathData.has_key(self._lang):
                    self._ageRatingPath = ageRatingPathData.readString(self._lang)
                elif ageRatingPathData.has_key(DEFAULT_TAG):
                    self._ageRatingPath = ageRatingPathData.readString(DEFAULT_TAG)
        return self._ageRatingPath

    def _getLoadingTypeSection(self, loadingType):
        progressSettingsSection = self._settings[b'progressSettings']
        if progressSettingsSection is None:
            _logger.error(b'No progressSettings section.')
            return
        else:
            if loadingType not in LoadingTypes.values():
                _logger.error(b'Wrong loading type %s', loadingType)
                return
            loadingTypeSection = progressSettingsSection[loadingType]
            if loadingTypeSection is None:
                _logger.error(b'No loading type %s section.', loadingTypeSection)
                return
            return loadingTypeSection
