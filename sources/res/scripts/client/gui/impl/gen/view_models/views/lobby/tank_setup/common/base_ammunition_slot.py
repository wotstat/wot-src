from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BaseAmmunitionSlot(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
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

    def getImageName(self):
        return self._getString(4)

    def setImageName(self, value):
        self._setString(4, value)
        return

    def getIconName(self):
        return self._getString(5)

    def setIconName(self, value):
        self._setString(5, value)
        return

    def getWithAttention(self):
        return self._getBool(6)

    def setWithAttention(self, value):
        self._setBool(6, value)
        return

    def getIsInstalled(self):
        return self._getBool(7)

    def setIsInstalled(self, value):
        self._setBool(7, value)
        return

    def getIsMountedMoreThanOne(self):
        return self._getBool(8)

    def setIsMountedMoreThanOne(self, value):
        self._setBool(8, value)
        return

    def getItemInstalledSetupIdx(self):
        return self._getNumber(9)

    def setItemInstalledSetupIdx(self, value):
        self._setNumber(9, value)
        return

    def getOverlayType(self):
        return self._getString(10)

    def setOverlayType(self, value):
        self._setString(10, value)
        return

    def getHighlightType(self):
        return self._getString(11)

    def setHighlightType(self, value):
        self._setString(11, value)
        return

    def getCategoryImgSource(self):
        return self._getResource(12)

    def setCategoryImgSource(self, value):
        self._setResource(12, value)
        return

    def _initialize(self):
        super(BaseAmmunitionSlot, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'intCD', 0)
        self._addStringProperty(b'keyName', b'')
        self._addResourceProperty(b'imageSource', R.invalid())
        self._addStringProperty(b'imageName', b'')
        self._addStringProperty(b'iconName', b'')
        self._addBoolProperty(b'withAttention', False)
        self._addBoolProperty(b'isInstalled', True)
        self._addBoolProperty(b'isMountedMoreThanOne', False)
        self._addNumberProperty(b'itemInstalledSetupIdx', -1)
        self._addStringProperty(b'overlayType', b'')
        self._addStringProperty(b'highlightType', b'')
        self._addResourceProperty(b'categoryImgSource', R.invalid())
        return
