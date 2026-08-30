from frameworks.wulf import ViewModel

class NarrationViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSlide', b'onVoiceoverToggle')

    def __init__(self, properties=4, commands=3):
        super(NarrationViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSlideNumber(self):
        return self._getNumber(0)

    def setSlideNumber(self, value):
        self._setNumber(0, value)
        return

    def getIsNextDisabled(self):
        return self._getBool(1)

    def setIsNextDisabled(self, value):
        self._setBool(1, value)
        return

    def getIsPrevDisabled(self):
        return self._getBool(2)

    def setIsPrevDisabled(self, value):
        self._setBool(2, value)
        return

    def getIsVoiceoverActive(self):
        return self._getBool(3)

    def setIsVoiceoverActive(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(NarrationViewModel, self)._initialize()
        self._addNumberProperty(b'slideNumber', 0)
        self._addBoolProperty(b'isNextDisabled', False)
        self._addBoolProperty(b'isPrevDisabled', False)
        self._addBoolProperty(b'isVoiceoverActive', False)
        self.onClose = self._addCommand(b'onClose')
        self.onSlide = self._addCommand(b'onSlide')
        self.onVoiceoverToggle = self._addCommand(b'onVoiceoverToggle')
        return
