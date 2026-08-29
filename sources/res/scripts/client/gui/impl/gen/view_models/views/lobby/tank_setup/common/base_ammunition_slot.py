from gui.impl.gen import R
from frameworks.wulf import ViewModel

class BaseAmmunitionSlot(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(BaseAmmunitionSlot, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getIntCD(self):
        return self._getNumber(1)

    def setIntCD(self, value):
        self._setNumber(1, value)
        return

    def getKeyName(self):
        return self._getString(2)

    def setKeyName(self, value):
        self._setString(2, value)
        return

    def getImageSource(self):
        return self._getResource(3)

    def setImageSource(self, value):
        self._setResource(3, value)
        return

    def getWithAttention(self):
        return self._getBool(4)

    def setWithAttention(self, value):
        self._setBool(4, value)
        return

    def getIsInstalled(self):
        return self._getBool(5)

    def setIsInstalled(self, value):
        self._setBool(5, value)
        return

    def getIsMountedMoreThanOne(self):
        return self._getBool(6)

    def setIsMountedMoreThanOne(self, value):
        self._setBool(6, value)
        return

    def getItemInstalledSetupIdx(self):
        return self._getNumber(7)

    def setItemInstalledSetupIdx(self, value):
        self._setNumber(7, value)
        return

    def getOverlayType(self):
        return self._getString(8)

    def setOverlayType(self, value):
        self._setString(8, value)
        return

    def getHighlightType(self):
        return self._getString(9)

    def setHighlightType(self, value):
        self._setString(9, value)
        return

    def getCategoryImgSource(self):
        return self._getResource(10)

    def setCategoryImgSource(self, value):
        self._setResource(10, value)
        return

    def _initialize(self):
        super(BaseAmmunitionSlot, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'keyName', b'')
        self._addResourceProperty(b'imageSource', R.invalid())
        self._addBoolProperty(b'withAttention', False)
        self._addBoolProperty(b'isInstalled', True)
        self._addBoolProperty(b'isMountedMoreThanOne', False)
        self._addNumberProperty(b'itemInstalledSetupIdx', -1)
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'highlightType', b'')
        self._addResourceProperty(b'categoryImgSource', R.invalid())
        return
