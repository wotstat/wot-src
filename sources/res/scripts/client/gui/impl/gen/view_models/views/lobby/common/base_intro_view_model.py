from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.intro_slide_model import IntroSlideModel

class BaseIntroViewModel(ViewModel):
    __slots__ = (b'onClose', b'onVideo', b'onViewLoaded')

    def __init__(self, properties=5, commands=3):
        super(BaseIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVideoExist(self):
        return self._getBool(0)

    def setIsVideoExist(self, value):
        self._setBool(0, value)
        return

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def getAbout(self):
        return self._getResource(2)

    def setAbout(self, value):
        self._setResource(2, value)
        return

    def getButtonLabel(self):
        return self._getResource(3)

    def setButtonLabel(self, value):
        self._setResource(3, value)
        return

    def getSlides(self):
        return self._getArray(4)

    def setSlides(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getSlidesType():
        return IntroSlideModel

    def _initialize(self):
        super(BaseIntroViewModel, self)._initialize()
        self._addBoolProperty(b'isVideoExist', True)
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'about', R.invalid())
        self._addResourceProperty(b'buttonLabel', R.invalid())
        self._addArrayProperty(b'slides', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onVideo = self._addCommand(b'onVideo')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        return
