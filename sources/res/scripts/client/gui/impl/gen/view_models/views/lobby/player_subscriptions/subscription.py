from frameworks.wulf import ViewModel

class Subscription(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(Subscription, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getImageUriSmall(self):
        return self._getString(3)

    def setImageUriSmall(self, value):
        self._setString(3, value)
        return

    def getHas3rdPartyRewardsToClaim(self):
        return self._getBool(4)

    def setHas3rdPartyRewardsToClaim(self, value):
        self._setBool(4, value)
        return

    def getHasDepotRewardsToClaim(self):
        return self._getBool(5)

    def setHasDepotRewardsToClaim(self, value):
        self._setBool(5, value)
        return

    def getImageUriMedium(self):
        return self._getString(6)

    def setImageUriMedium(self, value):
        self._setString(6, value)
        return

    def getImageUriLarge(self):
        return self._getString(7)

    def setImageUriLarge(self, value):
        self._setString(7, value)
        return

    def getRefreshTime(self):
        return self._getNumber(8)

    def setRefreshTime(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(Subscription, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'imageUriSmall', b'')
        self._addBoolProperty(b'has3rdPartyRewardsToClaim', True)
        self._addBoolProperty(b'hasDepotRewardsToClaim', True)
        self._addStringProperty(b'imageUriMedium', b'')
        self._addStringProperty(b'imageUriLarge', b'')
        self._addNumberProperty(b'refreshTime', 0)
        return
