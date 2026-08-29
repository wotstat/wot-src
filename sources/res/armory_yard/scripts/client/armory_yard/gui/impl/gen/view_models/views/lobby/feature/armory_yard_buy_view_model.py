from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel
from gui.impl.gen.view_models.common.price_model import PriceModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_buy_step_config import ArmoryYardBuyStepConfig
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_rewards_vehicle_model import ArmoryYardRewardsVehicleModel

class ParentAlias(Enum):
    MAINVIEW = b'mainView'
    VEHICLEPREVIEW = b'vehiclePreview'


class ArmoryYardBuyViewModel(ViewModel):
    __slots__ = (b'onChangeSelectedStep', b'onBuySteps', b'onCancel', b'onBack', b'onShowVehiclePreview', b'onShowStylePreview')
    STEP_VEHICLE_TOOLTIP_TYPE = b'stepVehicle'
    FINAL_REWARD_TOOLTIP_TYPE = b'finalReward'
    MERGED_REWARD_TOOLTIP_TYPE = b'mergedReward'
    MAX_VISIBLE_REWARDS = 10

    def __init__(self, properties=12, commands=6):
        super(ArmoryYardBuyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def finalReward(self):
        return self._getViewModel(0)

    @staticmethod
    def getFinalRewardType():
        return ArmoryYardRewardsVehicleModel

    def getStartStep(self):
        return self._getNumber(1)

    def setStartStep(self, value):
        self._setNumber(1, value)
        return

    def getFinishStep(self):
        return self._getNumber(2)

    def setFinishStep(self, value):
        self._setNumber(2, value)
        return

    def getStepSelected(self):
        return self._getNumber(3)

    def setStepSelected(self, value):
        self._setNumber(3, value)
        return

    def getStepsPassed(self):
        return self._getNumber(4)

    def setStepsPassed(self, value):
        self._setNumber(4, value)
        return

    def getParentAlias(self):
        return ParentAlias(self._getString(5))

    def setParentAlias(self, value):
        self._setString(5, value.value)
        return

    def getRewards(self):
        return self._getArray(6)

    def setRewards(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRewardsType():
        return ItemBonusModel

    def getSteps(self):
        return self._getArray(7)

    def setSteps(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getStepsType():
        return ArmoryYardBuyStepConfig

    def getIsWalletAvailable(self):
        return self._getBool(8)

    def setIsWalletAvailable(self, value):
        self._setBool(8, value)
        return

    def getIsBlurEnabled(self):
        return self._getBool(9)

    def setIsBlurEnabled(self, value):
        self._setBool(9, value)
        return

    def getIsPostProgressionState(self):
        return self._getBool(10)

    def setIsPostProgressionState(self, value):
        self._setBool(10, value)
        return

    def getPrices(self):
        return self._getArray(11)

    def setPrices(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getPricesType():
        return PriceModel

    def _initialize(self):
        super(ArmoryYardBuyViewModel, self)._initialize()
        self._addViewModelProperty(b'finalReward', ArmoryYardRewardsVehicleModel())
        self._addNumberProperty(b'startStep', 0)
        self._addNumberProperty(b'finishStep', 0)
        self._addNumberProperty(b'stepSelected', 0)
        self._addNumberProperty(b'stepsPassed', 0)
        self._addStringProperty(b'parentAlias')
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'steps', Array())
        self._addBoolProperty(b'isWalletAvailable', True)
        self._addBoolProperty(b'isBlurEnabled', False)
        self._addBoolProperty(b'isPostProgressionState', False)
        self._addArrayProperty(b'prices', Array())
        self.onChangeSelectedStep = self._addCommand(b'onChangeSelectedStep')
        self.onBuySteps = self._addCommand(b'onBuySteps')
        self.onCancel = self._addCommand(b'onCancel')
        self.onBack = self._addCommand(b'onBack')
        self.onShowVehiclePreview = self._addCommand(b'onShowVehiclePreview')
        self.onShowStylePreview = self._addCommand(b'onShowStylePreview')
        return
