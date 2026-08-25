from frameworks.wulf import Array, ViewModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_node_model import JmNodeModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_node_popover_model import JmNodePopoverModel
from journey_marathon.gui.impl.gen.view_models.views.lobby.jm_quest_card_model import JmQuestCardModel

class JmMapViewModel(ViewModel):
    __slots__ = (b'onQuestProgressShown', b'onQuestCompletedShown', b'onSelectNode', b'onChangeCurrentNode', b'onExplore', b'onExploreAnimationFinished', b'onInterruptForScreenShow', b'onCurrentNodeSynced', b'onPreviewLore', b'onRewardPreview', b'onBannerOpen')
    VEHICLE_REWARD = b'vehicles'
    TOKEN_REWARD = b'jm_lock_token'

    def __init__(self, properties=16, commands=11):
        super(JmMapViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def nodePopover(self):
        return self._getViewModel(0)

    @staticmethod
    def getNodePopoverType():
        return JmNodePopoverModel

    def getNodes(self):
        return self._getArray(1)

    def setNodes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getNodesType():
        return JmNodeModel

    def getCurrentNodeId(self):
        return self._getString(2)

    def setCurrentNodeId(self, value):
        self._setString(2, value)
        return

    def getQuestCards(self):
        return self._getArray(3)

    def setQuestCards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getQuestCardsType():
        return JmQuestCardModel

    def getTimeTillNewQuests(self):
        return self._getNumber(4)

    def setTimeTillNewQuests(self, value):
        self._setNumber(4, value)
        return

    def getIsLastGameDay(self):
        return self._getBool(5)

    def setIsLastGameDay(self, value):
        self._setBool(5, value)
        return

    def getCoinTokenCount(self):
        return self._getNumber(6)

    def setCoinTokenCount(self, value):
        self._setNumber(6, value)
        return

    def getUnlockTokenCount(self):
        return self._getNumber(7)

    def setUnlockTokenCount(self, value):
        self._setNumber(7, value)
        return

    def getIsInteractivityLocked(self):
        return self._getBool(8)

    def setIsInteractivityLocked(self, value):
        self._setBool(8, value)
        return

    def getTimeTillEnd(self):
        return self._getNumber(9)

    def setTimeTillEnd(self, value):
        self._setNumber(9, value)
        return

    def getIsCompleted(self):
        return self._getBool(10)

    def setIsCompleted(self, value):
        self._setBool(10, value)
        return

    def getIsQuestCompletedShow(self):
        return self._getBool(11)

    def setIsQuestCompletedShow(self, value):
        self._setBool(11, value)
        return

    def getMovingFailed(self):
        return self._getBool(12)

    def setMovingFailed(self, value):
        self._setBool(12, value)
        return

    def getBannerShown(self):
        return self._getBool(13)

    def setBannerShown(self, value):
        self._setBool(13, value)
        return

    def getExploreAnimationNodeId(self):
        return self._getString(14)

    def setExploreAnimationNodeId(self, value):
        self._setString(14, value)
        return

    def getExploreAnimationUnpause(self):
        return self._getString(15)

    def setExploreAnimationUnpause(self, value):
        self._setString(15, value)
        return

    def _initialize(self):
        super(JmMapViewModel, self)._initialize()
        self._addViewModelProperty(b'nodePopover', JmNodePopoverModel())
        self._addArrayProperty(b'nodes', Array())
        self._addStringProperty(b'currentNodeId', b'')
        self._addArrayProperty(b'questCards', Array())
        self._addNumberProperty(b'timeTillNewQuests', 0)
        self._addBoolProperty(b'isLastGameDay', False)
        self._addNumberProperty(b'coinTokenCount', 0)
        self._addNumberProperty(b'unlockTokenCount', 0)
        self._addBoolProperty(b'isInteractivityLocked', False)
        self._addNumberProperty(b'timeTillEnd', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isQuestCompletedShow', False)
        self._addBoolProperty(b'movingFailed', False)
        self._addBoolProperty(b'bannerShown', False)
        self._addStringProperty(b'exploreAnimationNodeId', b'')
        self._addStringProperty(b'exploreAnimationUnpause', b'')
        self.onQuestProgressShown = self._addCommand(b'onQuestProgressShown')
        self.onQuestCompletedShown = self._addCommand(b'onQuestCompletedShown')
        self.onSelectNode = self._addCommand(b'onSelectNode')
        self.onChangeCurrentNode = self._addCommand(b'onChangeCurrentNode')
        self.onExplore = self._addCommand(b'onExplore')
        self.onExploreAnimationFinished = self._addCommand(b'onExploreAnimationFinished')
        self.onInterruptForScreenShow = self._addCommand(b'onInterruptForScreenShow')
        self.onCurrentNodeSynced = self._addCommand(b'onCurrentNodeSynced')
        self.onPreviewLore = self._addCommand(b'onPreviewLore')
        self.onRewardPreview = self._addCommand(b'onRewardPreview')
        self.onBannerOpen = self._addCommand(b'onBannerOpen')
        return
