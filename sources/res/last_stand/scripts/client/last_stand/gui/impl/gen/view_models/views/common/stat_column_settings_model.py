from enum import Enum
from frameworks.wulf import Array, ViewModel

class ColumnEnum(Enum):
    KILLS = b'kills'
    DAMAGE = b'damage'
    ASSIST = b'assist'
    BLOCKED = b'blocked'
    PLACE = b'place'
    KEYS = b'keys'


class StatColumnSettingsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(StatColumnSettingsModel, self).__init__(properties=properties, commands=commands)
        return

    def getVisibleColumns(self):
        return self._getArray(0)

    def setVisibleColumns(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getVisibleColumnsType():
        return ColumnEnum

    def _initialize(self):
        super(StatColumnSettingsModel, self)._initialize()
        self._addArrayProperty(b'visibleColumns', Array())
        return
