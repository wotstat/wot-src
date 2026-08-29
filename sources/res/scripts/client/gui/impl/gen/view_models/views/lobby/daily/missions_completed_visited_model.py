from frameworks.wulf import ViewModel

class MissionsCompletedVisitedModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MissionsCompletedVisitedModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getValue(self):
        return self._getBool(1)

    def setValue(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(MissionsCompletedVisitedModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addBoolProperty(b'value', False)
        return
