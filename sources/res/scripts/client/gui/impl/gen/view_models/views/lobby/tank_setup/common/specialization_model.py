from frameworks.wulf import ViewModel

class SpecializationModel(ViewModel):
    __slots__ = ()
    EMPTY = b'empty'

    def __init__(self, properties=3, commands=0):
        super(SpecializationModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getIsCorrect(self):
        return self._getBool(1)

    def setIsCorrect(self, value):
        self._setBool(1, value)
        return

    def getIsClickable(self):
        return self._getBool(2)

    def setIsClickable(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(SpecializationModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isCorrect', False)
        self._addBoolProperty(b'isClickable', False)
        return
