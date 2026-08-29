from frameworks.wulf import ViewModel

class ClanShortInfoContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ClanShortInfoContentModel, self).__init__(properties=properties, commands=commands)
        return

    def getEmblem(self):
        return self._getString(0)

    def setEmblem(self, value):
        self._setString(0, value)
        return

    def getFullName(self):
        return self._getString(1)

    def setFullName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(ClanShortInfoContentModel, self)._initialize()
        self._addStringProperty(b'emblem', b'')
        self._addStringProperty(b'fullName', b'')
        return
