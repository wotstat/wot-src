from frameworks.wulf import Array
from white_tiger.gui.impl.gen.view_models.views.lobby.common.wt_guaranteed_reward_model import WtGuaranteedRewardModel
from white_tiger.gui.impl.gen.view_models.views.lobby.common.wt_run_portal_model import WtRunPortalModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.wt_base_portals_view_model import WtBasePortalsViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.wt_portal_bonus_model import WtPortalBonusModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.wt_portal_rewardList import WtPortalRewardlist

class WtPortalViewModel(WtBasePortalsViewModel):
    __slots__ = (b'onGoBack', b'onRunPortal', b'onSwitchAnimation', b'onPreview')

    def __init__(self, properties=16, commands=6):
        super(WtPortalViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def portalRun(self):
        return self._getViewModel(1)

    @staticmethod
    def getPortalRunType():
        return WtRunPortalModel

    @property
    def guaranteedReward(self):
        return self._getViewModel(2)

    @staticmethod
    def getGuaranteedRewardType():
        return WtGuaranteedRewardModel

    def getPortalType(self):
        return self._getString(3)

    def setPortalType(self, value):
        self._setString(3, value)
        return

    def getSelectedLootBoxesCount(self):
        return self._getNumber(4)

    def setSelectedLootBoxesCount(self, value):
        self._setNumber(4, value)
        return

    def getBackButtonText(self):
        return self._getString(5)

    def setBackButtonText(self, value):
        self._setString(5, value)
        return

    def getFirstLaunchReward(self):
        return self._getNumber(6)

    def setFirstLaunchReward(self, value):
        self._setNumber(6, value)
        return

    def getIsLaunchAnimated(self):
        return self._getBool(7)

    def setIsLaunchAnimated(self, value):
        self._setBool(7, value)
        return

    def getHighProbability(self):
        return self._getReal(8)

    def setHighProbability(self, value):
        self._setReal(8, value)
        return

    def getMediumProbability(self):
        return self._getReal(9)

    def setMediumProbability(self, value):
        self._setReal(9, value)
        return

    def getLowProbability(self):
        return self._getReal(10)

    def setLowProbability(self, value):
        self._setReal(10, value)
        return

    def getIsViewActive(self):
        return self._getBool(11)

    def setIsViewActive(self, value):
        self._setBool(11, value)
        return

    def getHighProbabilityRewards(self):
        return self._getArray(12)

    def setHighProbabilityRewards(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getHighProbabilityRewardsType():
        return WtPortalBonusModel

    def getMediumProbabilityRewards(self):
        return self._getArray(13)

    def setMediumProbabilityRewards(self, value):
        self._setArray(13, value)
        return

    @staticmethod
    def getMediumProbabilityRewardsType():
        return WtPortalBonusModel

    def getLowProbabilityRewards(self):
        return self._getArray(14)

    def setLowProbabilityRewards(self, value):
        self._setArray(14, value)
        return

    @staticmethod
    def getLowProbabilityRewardsType():
        return WtPortalBonusModel

    def getRewardList(self):
        return self._getArray(15)

    def setRewardList(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getRewardListType():
        return WtPortalRewardlist

    def _initialize(self):
        super(WtPortalViewModel, self)._initialize()
        self._addViewModelProperty(b'portalRun', WtRunPortalModel())
        self._addViewModelProperty(b'guaranteedReward', WtGuaranteedRewardModel())
        self._addStringProperty(b'portalType', b'')
        self._addNumberProperty(b'selectedLootBoxesCount', 1)
        self._addStringProperty(b'backButtonText', b'')
        self._addNumberProperty(b'firstLaunchReward', 100)
        self._addBoolProperty(b'isLaunchAnimated', False)
        self._addRealProperty(b'highProbability', 0.0)
        self._addRealProperty(b'mediumProbability', 0.0)
        self._addRealProperty(b'lowProbability', 0.0)
        self._addBoolProperty(b'isViewActive', True)
        self._addArrayProperty(b'highProbabilityRewards', Array())
        self._addArrayProperty(b'mediumProbabilityRewards', Array())
        self._addArrayProperty(b'lowProbabilityRewards', Array())
        self._addArrayProperty(b'rewardList', Array())
        self.onGoBack = self._addCommand(b'onGoBack')
        self.onRunPortal = self._addCommand(b'onRunPortal')
        self.onSwitchAnimation = self._addCommand(b'onSwitchAnimation')
        self.onPreview = self._addCommand(b'onPreview')
        return
