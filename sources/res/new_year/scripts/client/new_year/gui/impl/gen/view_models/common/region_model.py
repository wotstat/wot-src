from frameworks.wulf import ViewModel

class RegionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(RegionModel, self).__init__(properties=properties, commands=commands)
        return

    def getRealm(self):
        return self._getString(0)

    def setRealm(self, value):
        self._setString(0, value)
        return

    def getLanguage(self):
        return self._getString(1)

    def setLanguage(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(RegionModel, self)._initialize()
        self._addStringProperty(b'realm', b'')
        self._addStringProperty(b'language', b'')
        return
