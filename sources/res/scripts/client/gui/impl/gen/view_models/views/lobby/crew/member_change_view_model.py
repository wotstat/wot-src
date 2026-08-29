from frameworks.wulf import Array
from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel
from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class MemberChangeViewModel(BaseCrewViewModel):
    __slots__ = (b'onResetFilters', b'onTankmanSelected', b'onRecruitSelected', b'onRecruitNewTankman', b'onTankmanRestore', b'onPlayRecruitVoiceover', b'onLoadCards')

    def __init__(self, properties=13, commands=11):
        super(MemberChangeViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleInfo(self):
        return self._getViewModel(2)

    @staticmethod
    def getVehicleInfoType():
        return VehicleInfoModel

    def getHasCrew(self):
        return self._getBool(3)

    def setHasCrew(self, value):
        self._setBool(3, value)
        return

    def getHasFilters(self):
        return self._getBool(4)

    def setHasFilters(self, value):
        self._setBool(4, value)
        return

    def getRoleChangeDiscountPercent(self):
        return self._getNumber(5)

    def setRoleChangeDiscountPercent(self, value):
        self._setNumber(5, value)
        return

    def getVehicle(self):
        return self._getString(6)

    def setVehicle(self, value):
        self._setString(6, value)
        return

    def getNation(self):
        return self._getString(7)

    def setNation(self, value):
        self._setString(7, value)
        return

    def getRequiredRole(self):
        return self._getString(8)

    def setRequiredRole(self, value):
        self._setString(8, value)
        return

    def getItemsAmount(self):
        return self._getNumber(9)

    def setItemsAmount(self, value):
        self._setNumber(9, value)
        return

    def getItemsOffset(self):
        return self._getNumber(10)

    def setItemsOffset(self, value):
        self._setNumber(10, value)
        return

    def getTankmanList(self):
        return self._getArray(11)

    def setTankmanList(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getTankmanListType():
        return TankmanModel

    def getHeadersIndexes(self):
        return self._getArray(12)

    def setHeadersIndexes(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getHeadersIndexesType():
        return int

    def _initialize(self):
        super(MemberChangeViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicleInfo', VehicleInfoModel())
        self._addBoolProperty(b'hasCrew', True)
        self._addBoolProperty(b'hasFilters', False)
        self._addNumberProperty(b'roleChangeDiscountPercent', 0)
        self._addStringProperty(b'vehicle', b'')
        self._addStringProperty(b'nation', b'')
        self._addStringProperty(b'requiredRole', b'')
        self._addNumberProperty(b'itemsAmount', 0)
        self._addNumberProperty(b'itemsOffset', 0)
        self._addArrayProperty(b'tankmanList', Array())
        self._addArrayProperty(b'headersIndexes', Array())
        self.onResetFilters = self._addCommand(b'onResetFilters')
        self.onTankmanSelected = self._addCommand(b'onTankmanSelected')
        self.onRecruitSelected = self._addCommand(b'onRecruitSelected')
        self.onRecruitNewTankman = self._addCommand(b'onRecruitNewTankman')
        self.onTankmanRestore = self._addCommand(b'onTankmanRestore')
        self.onPlayRecruitVoiceover = self._addCommand(b'onPlayRecruitVoiceover')
        self.onLoadCards = self._addCommand(b'onLoadCards')
        return
