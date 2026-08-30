from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.wrappers.user_list_model import UserListModel
from white_tiger.gui.impl.gen.view_models.views.lobby.widgets.equipment_group_model import EquipmentGroupModel

class TankTypeEnum(Enum):
    HUNTER = b'wt_hunter'
    BOSS = b'wt_boss'
    SPECIALBOSS = b'wt_special_boss'


class HangarConsumablesPanelViewModel(ViewModel):
    __slots__ = (b'onOpenTasks', b'onBuyTicket')

    def __init__(self, properties=5, commands=2):
        super(HangarConsumablesPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def equipments(self):
        return self._getViewModel(0)

    @staticmethod
    def getEquipmentsType():
        return EquipmentGroupModel

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getResource(2)

    def setIcon(self, value):
        self._setResource(2, value)
        return

    def getQuantity(self):
        return self._getNumber(3)

    def setQuantity(self, value):
        self._setNumber(3, value)
        return

    def getTankType(self):
        return TankTypeEnum(self._getString(4))

    def setTankType(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(HangarConsumablesPanelViewModel, self)._initialize()
        self._addViewModelProperty(b'equipments', UserListModel())
        self._addStringProperty(b'title', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'quantity', -1)
        self._addStringProperty(b'tankType')
        self.onOpenTasks = self._addCommand(b'onOpenTasks')
        self.onBuyTicket = self._addCommand(b'onBuyTicket')
        return
