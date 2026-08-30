from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.loadout.base_loadout_model import BaseLoadoutModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.battle_booster_slot_model import BattleBoosterSlotModel

class InstructionsModel(BaseLoadoutModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=1):
        super(InstructionsModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasChanges(self):
        return self._getBool(1)

    def setHasChanges(self, value):
        self._setBool(1, value)
        return

    def getAutoloadEnabled(self):
        return self._getBool(2)

    def setAutoloadEnabled(self, value):
        self._setBool(2, value)
        return

    def getCrewInstructions(self):
        return self._getArray(3)

    def setCrewInstructions(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getCrewInstructionsType():
        return BattleBoosterSlotModel

    def getEquipmentInstructions(self):
        return self._getArray(4)

    def setEquipmentInstructions(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getEquipmentInstructionsType():
        return BattleBoosterSlotModel

    def _initialize(self):
        super(InstructionsModel, self)._initialize()
        self._addBoolProperty(b'hasChanges', False)
        self._addBoolProperty(b'autoloadEnabled', False)
        self._addArrayProperty(b'crewInstructions', Array())
        self._addArrayProperty(b'equipmentInstructions', Array())
        return
