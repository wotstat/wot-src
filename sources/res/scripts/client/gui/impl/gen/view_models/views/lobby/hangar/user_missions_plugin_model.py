from frameworks.wulf import Array, ViewModel

class UserMissionsPluginModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(UserMissionsPluginModel, self).__init__(properties=properties, commands=commands)
        return

    def getUrl(self):
        return self._getString(0)

    def setUrl(self, value):
        self._setString(0, value)
        return

    def getDependencies(self):
        return self._getArray(1)

    def setDependencies(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getDependenciesType():
        return unicode

    def _initialize(self):
        super(UserMissionsPluginModel, self)._initialize()
        self._addStringProperty(b'url', b'')
        self._addArrayProperty(b'dependencies', Array())
        return
