from frameworks.wulf import Array, ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_equipment_model import BattleRoyaleEquipmentModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_respawn_ability_model import BattleRoyaleRespawnAbilityModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_shell_model import BattleRoyaleShellModel

class LoadoutViewModel(ViewModel):
    __slots__ = (b'showUpgrades',)

    def __init__(self, properties=3, commands=1):
        super(LoadoutViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def respawnAbility(self):
        return self._getViewModel(0)

    @staticmethod
    def getRespawnAbilityType():
        return BattleRoyaleRespawnAbilityModel

    def getShells(self):
        return self._getArray(1)

    def setShells(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getShellsType():
        return BattleRoyaleShellModel

    def getEquipment(self):
        return self._getArray(2)

    def setEquipment(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getEquipmentType():
        return BattleRoyaleEquipmentModel

    def _initialize(self):
        super(LoadoutViewModel, self)._initialize()
        self._addViewModelProperty(b'respawnAbility', BattleRoyaleRespawnAbilityModel())
        self._addArrayProperty(b'shells', Array())
        self._addArrayProperty(b'equipment', Array())
        self.showUpgrades = self._addCommand(b'showUpgrades')
        return
