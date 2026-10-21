from frameworks.wulf import ViewModel

class AbilitiesTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(AbilitiesTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getDuration(self):
        return self._getNumber(1)

    def setDuration(self, value):
        self._setNumber(1, value)
        return

    def getReload(self):
        return self._getNumber(2)

    def setReload(self, value):
        self._setNumber(2, value)
        return

    def getLevel(self):
        return self._getNumber(3)

    def setLevel(self, value):
        self._setNumber(3, value)
        return

    def getLearned(self):
        return self._getBool(4)

    def setLearned(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(AbilitiesTooltipModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'duration', 0)
        self._addNumberProperty(b'reload', 0)
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'learned', False)
        return
