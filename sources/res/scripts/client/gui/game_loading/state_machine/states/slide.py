import time, typing, game_loading_bindings
from frameworks.state_machine import StateFlags
from gui.game_loading import loggers
from gui.game_loading.common import normalizeGfImagePath
from gui.game_loading.resources.consts import InfoStyles
from gui.game_loading.state_machine.models import ImageViewSettingsModel
from gui.game_loading.state_machine.states.base import BaseState, BaseViewResourcesTickingState
from gui.game_loading.resources.cdn.models import LocalSlideModel
from gui.game_loading.loading_sounds import handleLoadingSoundChangeEvent, DEFAULT_LOADING_SOUND
if typing.TYPE_CHECKING:
    from frameworks.state_machine import StateEvent
    from gui.game_loading.resources.models import LocalImageModel
    from gui.game_loading.resources.base import BaseResources
_logger = loggers.getStatesLogger()

def _showImage(image, settings):
    imagePath = normalizeGfImagePath(image.imageRelativePath)
    if not imagePath:
        _logger.warning(b'Broken image path: %s.', imagePath)
        return
    if not game_loading_bindings.isViewOpened():
        _logger.debug(b'Opening GF view.')
        game_loading_bindings.createLoadingView()
    data = {b'backgroundPath': imagePath, 
       b'text': (image.localizationText or b''), 
       b'description': (image.descriptionText or b''), 
       b'contentState': (settings.contentState), 
       b'transitionTime': (image.transition), 
       b'ageRatingPath': (settings.ageRatingPath), 
       b'info': (settings.info), 
       b'infoStyle': (InfoStyles.DEFAULT.value), 
       b'hasVignette': (settings.hasVignette)}
    if isinstance(image, LocalSlideModel) and image.additionalImage:
        handleLoadingSoundChangeEvent(image.sound)
        additionalImage = image.additionalImage
        data.update({b'additionalImage': {b'image': (normalizeGfImagePath(additionalImage.pathInCache)), 
                                b'width': (additionalImage.width), 
                                b'height': (additionalImage.height), 
                                b'margins': (additionalImage.margins), 
                                b'paddings': (additionalImage.paddings), 
                                b'position': (additionalImage.position)}})
    else:
        handleLoadingSoundChangeEvent(DEFAULT_LOADING_SOUND)
    game_loading_bindings.setViewData(data)
    _logger.debug(b'Image [%s] shown.', image)
    return


class StaticSlideState(BaseState):
    __slots__ = (b'_images', b'_image', b'_imageViewSettings')

    def __init__(self, stateID, images, imageViewSettings, flags=StateFlags.UNDEFINED):
        super(StaticSlideState, self).__init__(stateID=stateID, flags=flags)
        self._images = images
        self._image = None
        self._imageViewSettings = imageViewSettings
        return

    @property
    def lastShownImage(self):
        return self._image

    def setImage(self, image):
        self._image = image
        _logger.debug(b'[%s] image [%s] set.', self, image)
        return

    def _onEntered(self):
        super(StaticSlideState, self)._onEntered()
        self._image = self._image or self._images.get()
        _showImage(self._image, self._imageViewSettings)
        return

    def _onExited(self):
        self._images.reset()
        super(StaticSlideState, self)._onExited()
        return


class SlideState(BaseViewResourcesTickingState):
    __slots__ = (b'_image', b'_imageViewSettings', b'_isImageOverridden')

    def __init__(self, stateID, images, imageViewSettings, flags=StateFlags.UNDEFINED, isSelfTicking=False, onCompleteEvent=None):
        super(SlideState, self).__init__(stateID=stateID, resources=images, flags=flags, isSelfTicking=isSelfTicking, onCompleteEvent=onCompleteEvent)
        self._image = None
        self._imageViewSettings = imageViewSettings
        self._isImageOverridden = False
        return

    @property
    def lastShownImage(self):
        return self._image

    @property
    def timeLeft(self):
        return max(self._nextTickTime - time.time(), 0)

    def setImage(self, image):
        self._image = image
        self._nextTickTime = time.time() + image.minShowTimeSec
        self._isImageOverridden = True
        _logger.debug(b'[%s] image [%s] set.', self, image)
        return

    def _onEntered(self):
        super(SlideState, self)._onEntered()
        if self._isImageOverridden and self._image:
            self._isImageOverridden = False
            self._view(self._image)
        return

    def _view(self, image):
        self._image = image
        _showImage(image, self._imageViewSettings)
        return
