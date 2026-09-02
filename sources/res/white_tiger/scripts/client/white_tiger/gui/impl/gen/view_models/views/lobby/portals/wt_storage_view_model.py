from white_tiger.gui.impl.gen.view_models.views.lobby.common.wt_guaranteed_reward_model import WtGuaranteedRewardModel
from white_tiger.gui.impl.gen.view_models.views.lobby.common.wt_run_portal_model import WtRunPortalModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.main_prize_model import MainPrizeModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.wt_base_portals_view_model import WtBasePortalsViewModel

class WtStorageViewModel(WtBasePortalsViewModel):
    __slots__ = (b'onGoToPortal',)

    def __init__(self, properties=7, commands=3):
        super(WtStorageViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def hunterPortal(self):
        return self._getViewModel(1)

    @staticmethod
    def getHunterPortalType():
        return WtRunPortalModel

    @property
    def bossPortal(self):
        return self._getViewModel(2)

    @staticmethod
    def getBossPortalType():
        return WtRunPortalModel

    @property
    def tankPortal(self):
        return self._getViewModel(3)

    @staticmethod
    def getTankPortalType():
        return WtRunPortalModel

    @property
    def guaranteedReward(self):
        return self._getViewModel(4)

    @staticmethod
    def getGuaranteedRewardType():
        return WtGuaranteedRewardModel

    @property
    def mainPrize(self):
        return self._getViewModel(5)

    @staticmethod
    def getMainPrizeType():
        return MainPrizeModel

    def getIsPortalTankBought(self):
        return self._getBool(6)

    def setIsPortalTankBought(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(WtStorageViewModel, self)._initialize()
        self._addViewModelProperty(b'hunterPortal', WtRunPortalModel())
        self._addViewModelProperty(b'bossPortal', WtRunPortalModel())
        self._addViewModelProperty(b'tankPortal', WtRunPortalModel())
        self._addViewModelProperty(b'guaranteedReward', WtGuaranteedRewardModel())
        self._addViewModelProperty(b'mainPrize', MainPrizeModel())
        self._addBoolProperty(b'isPortalTankBought', False)
        self.onGoToPortal = self._addCommand(b'onGoToPortal')
        return
