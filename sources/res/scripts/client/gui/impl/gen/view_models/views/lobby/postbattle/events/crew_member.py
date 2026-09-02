from gui.impl.gen import R
from frameworks.wulf import ViewModel

class CrewMember(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CrewMember, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getRole(self):
        return self._getString(2)

    def setRole(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def getBattlesLeft(self):
        return self._getNumber(4)

    def setBattlesLeft(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(CrewMember, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'role', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'battlesLeft', 0)
        return
