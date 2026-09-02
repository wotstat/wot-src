from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.postbattle.stats_base_item import StatsBaseItem

class StatsTwoValuesItem(StatsBaseItem):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(StatsTwoValuesItem, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return self._getArray(4)

    def setValue(self, value):
        self._setArray(4, value)
        return

    def _initialize(self):
        super(StatsTwoValuesItem, self)._initialize()
        self._addArrayProperty(b'value', Array())
        return
