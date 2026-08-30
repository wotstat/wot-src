from frameworks.wulf import ViewModel

class BaseOverlayViewModel(ViewModel):
    __slots__ = (b'onCloseClicked', b'onEscapePressed')

    def __init__(self, properties=2, commands=2):
        super(BaseOverlayViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCloseVisible(self):
        return self._getBool(0)

    def setIsCloseVisible(self, value):
        self._setBool(0, value)
        return

    def getIsHidden(self):
        return self._getBool(1)

    def setIsHidden(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(BaseOverlayViewModel, self)._initialize()
        self._addBoolProperty(b'isCloseVisible', True)
        self._addBoolProperty(b'isHidden', False)
        self.onCloseClicked = self._addCommand(b'onCloseClicked')
        self.onEscapePressed = self._addCommand(b'onEscapePressed')
        return
