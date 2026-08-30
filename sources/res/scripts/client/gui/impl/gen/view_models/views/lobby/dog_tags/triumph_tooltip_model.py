from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R

class TriumphTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TriumphTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentGrade(self):
        return self._getNumber(0)

    def setCurrentGrade(self, value):
        self._setNumber(0, value)
        return

    def getGradeValues(self):
        return self._getArray(1)

    def setGradeValues(self, value):
        self._setArray(1, value)
        return

    def getComponentTitle(self):
        return self._getResource(2)

    def setComponentTitle(self, value):
        self._setResource(2, value)
        return

    def getProgressNumberType(self):
        return self._getString(3)

    def setProgressNumberType(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(TriumphTooltipModel, self)._initialize()
        self._addNumberProperty(b'currentGrade', 0)
        self._addArrayProperty(b'gradeValues', Array())
        self._addResourceProperty(b'componentTitle', R.invalid())
        self._addStringProperty(b'progressNumberType', b'')
        return
