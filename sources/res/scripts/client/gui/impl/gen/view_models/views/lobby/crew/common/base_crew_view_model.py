from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BaseCrewViewModel(ViewModel):
    __slots__ = (b'onAbout', b'onClose', b'onBack', b'onHangar')

    def __init__(self, properties=2, commands=4):
        super(BaseCrewViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackButtonLabel(self):
        return self._getResource(0)

    def setBackButtonLabel(self, value):
        self._setResource(0, value)
        return

    def getIsButtonBarVisible(self):
        return self._getBool(1)

    def setIsButtonBarVisible(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(BaseCrewViewModel, self)._initialize()
        self._addResourceProperty(b'backButtonLabel', R.invalid())
        self._addBoolProperty(b'isButtonBarVisible', True)
        self.onAbout = self._addCommand(b'onAbout')
        self.onClose = self._addCommand(b'onClose')
        self.onBack = self._addCommand(b'onBack')
        self.onHangar = self._addCommand(b'onHangar')
        return
