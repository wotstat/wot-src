from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.daily_bonus_model import DailyBonusModel
from battle_royale.gui.impl.gen.view_models.views.lobby.tooltips.tech_parameters_cmp_view_model import TechParametersCmpViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel

class VehicleTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(VehicleTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tech(self):
        return self._getViewModel(0)

    @staticmethod
    def getTechType():
        return TechParametersCmpViewModel

    @property
    def eventInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getEventInfoType():
        return BattleRoyaleEventModel

    @property
    def dailyBonus(self):
        return self._getViewModel(2)

    @staticmethod
    def getDailyBonusType():
        return DailyBonusModel

    def getVehicleName(self):
        return self._getString(3)

    def setVehicleName(self, value):
        self._setString(3, value)
        return

    def getVehicleNation(self):
        return self._getString(4)

    def setVehicleNation(self, value):
        self._setString(4, value)
        return

    def getVehicleType(self):
        return self._getString(5)

    def setVehicleType(self, value):
        self._setString(5, value)
        return

    def getStatusLevel(self):
        return self._getString(6)

    def setStatusLevel(self, value):
        self._setString(6, value)
        return

    def getStatusText(self):
        return self._getString(7)

    def setStatusText(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(VehicleTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'tech', TechParametersCmpViewModel())
        self._addViewModelProperty(b'eventInfo', BattleRoyaleEventModel())
        self._addViewModelProperty(b'dailyBonus', DailyBonusModel())
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleNation', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'statusLevel', b'')
        self._addStringProperty(b'statusText', b'')
        return
