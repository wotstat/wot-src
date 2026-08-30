from comp7.gui.impl.gen.view_models.views.battle.enums import BanState, CandidateState
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.battle.banned_vehicle_model import BannedVehicleModel
from comp7.gui.impl.gen.view_models.views.battle.comp7_vehicle_model import Comp7VehicleModel

class BanWidgetModel(ViewModel):
    __slots__ = (b'onOpen',)

    def __init__(self, properties=11, commands=1):
        super(BanWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bannedByAlliesVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getBannedByAlliesVehicleType():
        return Comp7VehicleModel

    @property
    def bannedByEnemiesVehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getBannedByEnemiesVehicleType():
        return Comp7VehicleModel

    @property
    def vehicleToBan(self):
        return self._getViewModel(2)

    @staticmethod
    def getVehicleToBanType():
        return Comp7VehicleModel

    def getBanState(self):
        return BanState(self._getString(3))

    def setBanState(self, value):
        self._setString(3, value.value)
        return

    def getCandidateState(self):
        return CandidateState(self._getString(4))

    def setCandidateState(self, value):
        self._setString(4, value.value)
        return

    def getConfirmedChoice(self):
        return self._getBool(5)

    def setConfirmedChoice(self, value):
        self._setBool(5, value)
        return

    def getBannedByAlliesVehicles(self):
        return self._getArray(6)

    def setBannedByAlliesVehicles(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getBannedByAlliesVehiclesType():
        return BannedVehicleModel

    def getIsAlliesRandomlySelected(self):
        return self._getBool(7)

    def setIsAlliesRandomlySelected(self, value):
        self._setBool(7, value)
        return

    def getIsEnemyRandomlySelected(self):
        return self._getBool(8)

    def setIsEnemyRandomlySelected(self, value):
        self._setBool(8, value)
        return

    def getAlliesVotes(self):
        return self._getNumber(9)

    def setAlliesVotes(self, value):
        self._setNumber(9, value)
        return

    def getEnemyVotes(self):
        return self._getNumber(10)

    def setEnemyVotes(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(BanWidgetModel, self)._initialize()
        self._addViewModelProperty(b'bannedByAlliesVehicle', Comp7VehicleModel())
        self._addViewModelProperty(b'bannedByEnemiesVehicle', Comp7VehicleModel())
        self._addViewModelProperty(b'vehicleToBan', Comp7VehicleModel())
        self._addStringProperty(b'banState')
        self._addStringProperty(b'candidateState')
        self._addBoolProperty(b'confirmedChoice', False)
        self._addArrayProperty(b'bannedByAlliesVehicles', Array())
        self._addBoolProperty(b'isAlliesRandomlySelected', False)
        self._addBoolProperty(b'isEnemyRandomlySelected', False)
        self._addNumberProperty(b'alliesVotes', 0)
        self._addNumberProperty(b'enemyVotes', 0)
        self.onOpen = self._addCommand(b'onOpen')
        return
