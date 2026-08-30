from enum import Enum
from gui.impl.gen.view_models.common.price_model import PriceModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.early_access.early_access_animation_params import EarlyAccessAnimationParams

class State(Enum):
    INPROGRESS = b'inProgress'
    ININVENTORY = b'inInventory'
    LOCKED = b'locked'
    PURCHASABLE = b'purchasable'


class VehicleViewTooltipStates(Enum):
    QUESTSWIDGET = b'questsWidget'


class EarlyAccessVehicleModel(VehicleModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(EarlyAccessVehicleModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def commonPrice(self):
        return self._getViewModel(9)

    @staticmethod
    def getCommonPriceType():
        return PriceModel

    @property
    def animationParams(self):
        return self._getViewModel(10)

    @staticmethod
    def getAnimationParamsType():
        return EarlyAccessAnimationParams

    def getState(self):
        return State(self._getString(11))

    def setState(self, value):
        self._setString(11, value.value)
        return

    def getPrice(self):
        return self._getNumber(12)

    def setPrice(self, value):
        self._setNumber(12, value)
        return

    def getUnlockPriceAfterEA(self):
        return self._getNumber(13)

    def setUnlockPriceAfterEA(self, value):
        self._setNumber(13, value)
        return

    def getIsPostProgression(self):
        return self._getBool(14)

    def setIsPostProgression(self, value):
        self._setBool(14, value)
        return

    def getIsAffordable(self):
        return self._getBool(15)

    def setIsAffordable(self, value):
        self._setBool(15, value)
        return

    def _initialize(self):
        super(EarlyAccessVehicleModel, self)._initialize()
        self._addViewModelProperty(b'commonPrice', PriceModel())
        self._addViewModelProperty(b'animationParams', EarlyAccessAnimationParams())
        self._addStringProperty(b'state')
        self._addNumberProperty(b'price', 0)
        self._addNumberProperty(b'unlockPriceAfterEA', 0)
        self._addBoolProperty(b'isPostProgression', False)
        self._addBoolProperty(b'isAffordable', False)
        return
