from enum import Enum
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.surprise_machine.video_reward_view_model import VideoRewardViewModel

class MachineViews(Enum):
    SPEND_TOKENS = b'spendTokens'
    SPEND_TOKENS_ACTIVE = b'spendTokensActive'


class PurchaseFormState(Enum):
    AVAILABLE = b'available'
    NOT_AVAILABLE = b'notAvailable'
    ERROR = b'error'


class NySurpriseMachineModel(ViewModel):
    __slots__ = (b'onBuyBtnClick', b'onButtonPress', b'goToMachineMain', b'goToQuest', b'changePersonVoicesEnabled')

    def __init__(self, properties=8, commands=5):
        super(NySurpriseMachineModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicleReward(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehicleRewardType():
        return VideoRewardViewModel

    def getCurrentAtmosphereLevel(self):
        return self._getNumber(1)

    def setCurrentAtmosphereLevel(self, value):
        self._setNumber(1, value)
        return

    def getMachineViews(self):
        return MachineViews(self._getString(2))

    def setMachineViews(self, value):
        self._setString(2, value.value)
        return

    def getPurchaseFormState(self):
        return PurchaseFormState(self._getString(3))

    def setPurchaseFormState(self, value):
        self._setString(3, value.value)
        return

    def getExchangeRate(self):
        return self._getNumber(4)

    def setExchangeRate(self, value):
        self._setNumber(4, value)
        return

    def getIsBtnHovered(self):
        return self._getBool(5)

    def setIsBtnHovered(self, value):
        self._setBool(5, value)
        return

    def getIsBuyBtnLoading(self):
        return self._getBool(6)

    def setIsBuyBtnLoading(self, value):
        self._setBool(6, value)
        return

    def getIsPersonVoicesEnabled(self):
        return self._getBool(7)

    def setIsPersonVoicesEnabled(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(NySurpriseMachineModel, self)._initialize()
        self._addViewModelProperty(b'vehicleReward', VideoRewardViewModel())
        self._addNumberProperty(b'currentAtmosphereLevel', 9)
        self._addStringProperty(b'machineViews')
        self._addStringProperty(b'purchaseFormState')
        self._addNumberProperty(b'exchangeRate', 0)
        self._addBoolProperty(b'isBtnHovered', False)
        self._addBoolProperty(b'isBuyBtnLoading', False)
        self._addBoolProperty(b'isPersonVoicesEnabled', False)
        self.onBuyBtnClick = self._addCommand(b'onBuyBtnClick')
        self.onButtonPress = self._addCommand(b'onButtonPress')
        self.goToMachineMain = self._addCommand(b'goToMachineMain')
        self.goToQuest = self._addCommand(b'goToQuest')
        self.changePersonVoicesEnabled = self._addCommand(b'changePersonVoicesEnabled')
        return
