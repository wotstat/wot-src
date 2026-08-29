from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class ModeSelectorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ModeSelectorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getBattleTypes(self):
        return self._getArray(0)

    def setBattleTypes(self, value):
        self._setArray(0, value)
        return

    def _initialize(self):
        super(ModeSelectorTooltipModel, self)._initialize()
        self._addArrayProperty(b'battleTypes', Array())
        return
