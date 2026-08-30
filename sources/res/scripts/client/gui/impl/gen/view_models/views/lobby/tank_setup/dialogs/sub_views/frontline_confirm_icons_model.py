from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class FrontlineConfirmIconsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(FrontlineConfirmIconsModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcons(self):
        return self._getArray(0)

    def setIcons(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getIconsType():
        return unicode

    def getIsExtendedHeight(self):
        return self._getBool(1)

    def setIsExtendedHeight(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(FrontlineConfirmIconsModel, self)._initialize()
        self._addArrayProperty(b'icons', Array())
        self._addBoolProperty(b'isExtendedHeight', False)
        return
