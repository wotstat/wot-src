from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class Comp7BansModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(Comp7BansModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bannedByAlliesVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getBannedByAlliesVehicleType():
        return VehicleModel

    @property
    def bannedByEnemiesVehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getBannedByEnemiesVehicleType():
        return VehicleModel

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsAlliesRandomlySelected(self):
        return self._getBool(3)

    def setIsAlliesRandomlySelected(self, value):
        self._setBool(3, value)
        return

    def getIsEnemyRandomlySelected(self):
        return self._getBool(4)

    def setIsEnemyRandomlySelected(self, value):
        self._setBool(4, value)
        return

    def getAlliesVotes(self):
        return self._getNumber(5)

    def setAlliesVotes(self, value):
        self._setNumber(5, value)
        return

    def getEnemyVotes(self):
        return self._getNumber(6)

    def setEnemyVotes(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(Comp7BansModel, self)._initialize()
        self._addViewModelProperty(b'bannedByAlliesVehicle', VehicleModel())
        self._addViewModelProperty(b'bannedByEnemiesVehicle', VehicleModel())
        self._addBoolProperty(b'isEnabled', True)
        self._addBoolProperty(b'isAlliesRandomlySelected', False)
        self._addBoolProperty(b'isEnemyRandomlySelected', False)
        self._addNumberProperty(b'alliesVotes', 0)
        self._addNumberProperty(b'enemyVotes', 0)
        return
