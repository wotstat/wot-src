from comp7.gui.impl.gen.view_models.views.battle.enums import BanState
from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.battle.comp7_vehicle_model import Comp7VehicleModel

class BanEntryPointModel(ViewModel):
    __slots__ = (b'onOpen', b'pollServerTime')

    def __init__(self, properties=7, commands=2):
        super(BanEntryPointModel, self).__init__(properties=properties, commands=commands)
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

    def getState(self):
        return BanState(self._getString(2))

    def setState(self, value):
        self._setString(2, value.value)
        return

    def getEndTimestamp(self):
        return self._getNumber(3)

    def setEndTimestamp(self, value):
        self._setNumber(3, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(4)

    def setServerTimestamp(self, value):
        self._setNumber(4, value)
        return

    def getAlliesVehicleCD(self):
        return self._getNumber(5)

    def setAlliesVehicleCD(self, value):
        self._setNumber(5, value)
        return

    def getEnemiesVehicleCD(self):
        return self._getNumber(6)

    def setEnemiesVehicleCD(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(BanEntryPointModel, self)._initialize()
        self._addViewModelProperty(b'bannedByAlliesVehicle', Comp7VehicleModel())
        self._addViewModelProperty(b'bannedByEnemiesVehicle', Comp7VehicleModel())
        self._addStringProperty(b'state')
        self._addNumberProperty(b'endTimestamp', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self._addNumberProperty(b'alliesVehicleCD', -1)
        self._addNumberProperty(b'enemiesVehicleCD', -1)
        self.onOpen = self._addCommand(b'onOpen')
        self.pollServerTime = self._addCommand(b'pollServerTime')
        return
