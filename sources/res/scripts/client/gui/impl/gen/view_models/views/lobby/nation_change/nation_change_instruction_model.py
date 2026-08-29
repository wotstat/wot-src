from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NationChangeInstructionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(NationChangeInstructionModel, self).__init__(properties=properties, commands=commands)
        return

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)
        return

    def getIsInstalled(self):
        return self._getBool(1)

    def setIsInstalled(self, value):
        self._setBool(1, value)
        return

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)
        return

    def getIsPerkReplace(self):
        return self._getBool(3)

    def setIsPerkReplace(self, value):
        self._setBool(3, value)
        return

    def getIntCD(self):
        return self._getNumber(4)

    def setIntCD(self, value):
        self._setNumber(4, value)
        return

    def getLayoutIDx(self):
        return self._getNumber(5)

    def setLayoutIDx(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(NationChangeInstructionModel, self)._initialize()
        self._addResourceProperty(b'image', R.invalid())
        self._addBoolProperty(b'isInstalled', False)
        self._addBoolProperty(b'isActive', False)
        self._addBoolProperty(b'isPerkReplace', False)
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'layoutIDx', 0)
        return
