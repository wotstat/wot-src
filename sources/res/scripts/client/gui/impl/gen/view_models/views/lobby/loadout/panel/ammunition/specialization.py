from frameworks.wulf import ViewModel

class Specialization(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(Specialization, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getEditable(self):
        return self._getBool(1)

    def setEditable(self, value):
        self._setBool(1, value)
        return

    def getActive(self):
        return self._getBool(2)

    def setActive(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(Specialization, self)._initialize()
        self._addStringProperty(b'type', b'none')
        self._addBoolProperty(b'editable', False)
        self._addBoolProperty(b'active', False)
        return
