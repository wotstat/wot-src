from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.lootboxes.loot_box_guaranteed_reward_model import LootBoxGuaranteedRewardModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_sidebar_common_model import NySidebarCommonModel

class NyLootBoxMainViewModel(ViewModel):
    __slots__ = (b'onWindowClose', b'onTabClick', b'onCountSelected', b'onOpenBoxHitAreaClick', b'onOpenBoxBtnClick', b'onBuyBoxBtnClick', b'onQuestsBtnClick', b'onAnimationSwitchClick', b'onStatisticsButtonClick', b'onSwitchBoxHover')

    def __init__(self, properties=15, commands=10):
        super(NyLootBoxMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def sidebar(self):
        return self._getViewModel(0)

    @staticmethod
    def getSidebarType():
        return NySidebarCommonModel

    @property
    def boxesCountButtons(self):
        return self._getViewModel(1)

    @staticmethod
    def getBoxesCountButtonsType():
        return UserListModel

    @property
    def guaranteedReward(self):
        return self._getViewModel(2)

    @staticmethod
    def getGuaranteedRewardType():
        return LootBoxGuaranteedRewardModel

    def getCurrentName(self):
        return self._getString(3)

    def setCurrentName(self, value):
        self._setString(3, value)
        return

    def getSelectedBoxType(self):
        return self._getString(4)

    def setSelectedBoxType(self, value):
        self._setString(4, value)
        return

    def getIsPremiumType(self):
        return self._getBool(5)

    def setIsPremiumType(self, value):
        self._setBool(5, value)
        return

    def getIsOpenBoxBtnVisible(self):
        return self._getBool(6)

    def setIsOpenBoxBtnVisible(self, value):
        self._setBool(6, value)
        return

    def getCurrentCountButton(self):
        return self._getNumber(7)

    def setCurrentCountButton(self, value):
        self._setNumber(7, value)
        return

    def getIsBoxChangeAnimation(self):
        return self._getBool(8)

    def setIsBoxChangeAnimation(self, value):
        self._setBool(8, value)
        return

    def getIsBoxOpenEnabled(self):
        return self._getBool(9)

    def setIsBoxOpenEnabled(self, value):
        self._setBool(9, value)
        return

    def getIsViewHidden(self):
        return self._getBool(10)

    def setIsViewHidden(self, value):
        self._setBool(10, value)
        return

    def getIsVideoOff(self):
        return self._getBool(11)

    def setIsVideoOff(self, value):
        self._setBool(11, value)
        return

    def getIsBoxesAvailable(self):
        return self._getBool(12)

    def setIsBoxesAvailable(self, value):
        self._setBool(12, value)
        return

    def getIsStatisticsHintActive(self):
        return self._getBool(13)

    def setIsStatisticsHintActive(self, value):
        self._setBool(13, value)
        return

    def getRealm(self):
        return self._getString(14)

    def setRealm(self, value):
        self._setString(14, value)
        return

    def _initialize(self):
        super(NyLootBoxMainViewModel, self)._initialize()
        self._addViewModelProperty(b'sidebar', NySidebarCommonModel())
        self._addViewModelProperty(b'boxesCountButtons', UserListModel())
        self._addViewModelProperty(b'guaranteedReward', LootBoxGuaranteedRewardModel())
        self._addStringProperty(b'currentName', b'')
        self._addStringProperty(b'selectedBoxType', b'')
        self._addBoolProperty(b'isPremiumType', False)
        self._addBoolProperty(b'isOpenBoxBtnVisible', False)
        self._addNumberProperty(b'currentCountButton', 0)
        self._addBoolProperty(b'isBoxChangeAnimation', False)
        self._addBoolProperty(b'isBoxOpenEnabled', True)
        self._addBoolProperty(b'isViewHidden', False)
        self._addBoolProperty(b'isVideoOff', False)
        self._addBoolProperty(b'isBoxesAvailable', False)
        self._addBoolProperty(b'isStatisticsHintActive', False)
        self._addStringProperty(b'realm', b'')
        self.onWindowClose = self._addCommand(b'onWindowClose')
        self.onTabClick = self._addCommand(b'onTabClick')
        self.onCountSelected = self._addCommand(b'onCountSelected')
        self.onOpenBoxHitAreaClick = self._addCommand(b'onOpenBoxHitAreaClick')
        self.onOpenBoxBtnClick = self._addCommand(b'onOpenBoxBtnClick')
        self.onBuyBoxBtnClick = self._addCommand(b'onBuyBoxBtnClick')
        self.onQuestsBtnClick = self._addCommand(b'onQuestsBtnClick')
        self.onAnimationSwitchClick = self._addCommand(b'onAnimationSwitchClick')
        self.onStatisticsButtonClick = self._addCommand(b'onStatisticsButtonClick')
        self.onSwitchBoxHover = self._addCommand(b'onSwitchBoxHover')
        return
