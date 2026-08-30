from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.shells_preset_slot_model import ShellsPresetSlotModel

class ShellsPresetType(Enum):
    STANDARD = b'standard'
    ADVANCED = b'advanced'


class ShellsPresetModel(PresetModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ShellsPresetModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return ShellsPresetType(self._getString(5))

    def setType(self, value):
        self._setString(5, value.value)
        return

    def getItems(self):
        return self._getArray(6)

    def setItems(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getItemsType():
        return ShellsPresetSlotModel

    def _initialize(self):
        super(ShellsPresetModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addArrayProperty(b'items', Array())
        return
