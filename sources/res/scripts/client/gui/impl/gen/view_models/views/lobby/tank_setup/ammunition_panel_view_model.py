from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_panel_model import AmmunitionPanelModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.role_skill_slot_model import RoleSkillSlotModel
from gui.impl.gen.view_models.views.lobby.tank_setup.tank_setup_action_model import TankSetupActionModel

class AmmunitionPanelViewModel(ViewModel):
    __slots__ = (b'onEscKeyDown',)

    def __init__(self, properties=7, commands=1):
        super(AmmunitionPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def ammunitionPanel(self):
        return self._getViewModel(0)

    @staticmethod
    def getAmmunitionPanelType():
        return AmmunitionPanelModel

    @property
    def lastSlotAction(self):
        return self._getViewModel(1)

    @staticmethod
    def getLastSlotActionType():
        return TankSetupActionModel

    @property
    def roleSkillSlot(self):
        return self._getViewModel(2)

    @staticmethod
    def getRoleSkillSlotType():
        return RoleSkillSlotModel

    def getVehicleCD(self):
        return self._getNumber(3)

    def setVehicleCD(self, value):
        self._setNumber(3, value)
        return

    def getIsMaintenanceEnabled(self):
        return self._getBool(4)

    def setIsMaintenanceEnabled(self, value):
        self._setBool(4, value)
        return

    def getIsDisabled(self):
        return self._getBool(5)

    def setIsDisabled(self, value):
        self._setBool(5, value)
        return

    def getIsReady(self):
        return self._getBool(6)

    def setIsReady(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(AmmunitionPanelViewModel, self)._initialize()
        self._addViewModelProperty(b'ammunitionPanel', AmmunitionPanelModel())
        self._addViewModelProperty(b'lastSlotAction', TankSetupActionModel())
        self._addViewModelProperty(b'roleSkillSlot', RoleSkillSlotModel())
        self._addNumberProperty(b'vehicleCD', -1)
        self._addBoolProperty(b'isMaintenanceEnabled', True)
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isReady', False)
        self.onEscKeyDown = self._addCommand(b'onEscKeyDown')
        return
