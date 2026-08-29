from frameworks.wulf import ViewModel

class UserModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(UserModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIsCurrentUser(self):
        return self._getBool(1)

    def setIsCurrentUser(self, value):
        self._setBool(1, value)
        return

    def getIsReady(self):
        return self._getBool(2)

    def setIsReady(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(UserModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isCurrentUser', False)
        self._addBoolProperty(b'isReady', False)
        return
