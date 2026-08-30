from frameworks.wulf import ViewModel

class CommonPlayerDataModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CommonPlayerDataModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getClanTag(self):
        return self._getString(1)

    def setClanTag(self, value):
        self._setString(1, value)
        return

    def getBadgeID(self):
        return self._getString(2)

    def setBadgeID(self, value):
        self._setString(2, value)
        return

    def getRating(self):
        return self._getString(3)

    def setRating(self, value):
        self._setString(3, value)
        return

    def getColor(self):
        return self._getString(4)

    def setColor(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(CommonPlayerDataModel, self)._initialize()
        self._addStringProperty(b'name', b'rookie')
        self._addStringProperty(b'clanTag', b'')
        self._addStringProperty(b'badgeID', b'')
        self._addStringProperty(b'rating', b'')
        self._addStringProperty(b'color', b'')
        return
