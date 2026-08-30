from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MissionHubIntroViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=4, commands=1):
        super(MissionHubIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getHeader(self):
        return self._getResource(0)

    def setHeader(self, value):
        self._setResource(0, value)
        return

    def getDescription(self):
        return self._getResource(1)

    def setDescription(self, value):
        self._setResource(1, value)
        return

    def getButtonText(self):
        return self._getResource(2)

    def setButtonText(self, value):
        self._setResource(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def _initialize(self):
        super(MissionHubIntroViewModel, self)._initialize()
        self._addResourceProperty(b'header', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addResourceProperty(b'buttonText', R.invalid())
        self._addResourceProperty(b'icon', R.invalid())
        self.onClose = self._addCommand(b'onClose')
        return
