from frameworks.wulf import ViewModel

class UserMissionsSlideModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(UserMissionsSlideModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getWeight(self):
        return self._getNumber(1)

    def setWeight(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(UserMissionsSlideModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'weight', 0)
        return
