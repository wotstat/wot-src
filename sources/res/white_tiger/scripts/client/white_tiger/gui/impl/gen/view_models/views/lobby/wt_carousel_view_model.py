from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_carousel_tank_model import WtCarouselTankModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_carousel_tank_status_model import WtCarouselTankStatusModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_equipment_group_model import WtEquipmentGroupModel

class WtCarouselViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(WtCarouselViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def status(self):
        return self._getViewModel(0)

    @staticmethod
    def getStatusType():
        return WtCarouselTankStatusModel

    def getIsDisableAll(self):
        return self._getBool(1)

    def setIsDisableAll(self, value):
        self._setBool(1, value)
        return

    def getTanks(self):
        return self._getArray(2)

    def setTanks(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getTanksType():
        return WtCarouselTankModel

    def getEquipmentGroups(self):
        return self._getArray(3)

    def setEquipmentGroups(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getEquipmentGroupsType():
        return WtEquipmentGroupModel

    def _initialize(self):
        super(WtCarouselViewModel, self)._initialize()
        self._addViewModelProperty(b'status', WtCarouselTankStatusModel())
        self._addBoolProperty(b'isDisableAll', False)
        self._addArrayProperty(b'tanks', Array())
        self._addArrayProperty(b'equipmentGroups', Array())
        self.onClick = self._addCommand(b'onClick')
        return
