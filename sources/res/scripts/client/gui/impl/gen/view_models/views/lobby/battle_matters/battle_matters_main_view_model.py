from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_progress_model import QuestProgressModel
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_view_model import QuestViewModel

class BattleMattersMainViewModel(ViewModel):
    __slots__ = (b'onShowView', b'onRunBootcamp', b'onShowManual', b'onShowManualForQuest', b'onShowAnimForQuest', b'onShowMainReward', b'onSelectDelayedReward', b'onClose')
    ARG_QUEST_ID = b'questID'
    ARG_TOKEN_ID = b'tokenID'
    NAME_VEHICLE_REWARD = b'vehicle'
    NAME_TOKEN_REWARD = b'token'

    def __init__(self, properties=5, commands=8):
        super(BattleMattersMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def questProgress(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestProgressType():
        return QuestProgressModel

    def getIsRewardsViewOpen(self):
        return self._getBool(1)

    def setIsRewardsViewOpen(self, value):
        self._setBool(1, value)
        return

    def getBootcampIsAvailable(self):
        return self._getBool(2)

    def setBootcampIsAvailable(self, value):
        self._setBool(2, value)
        return

    def getIsBootcampCompleted(self):
        return self._getBool(3)

    def setIsBootcampCompleted(self, value):
        self._setBool(3, value)
        return

    def getQuests(self):
        return self._getArray(4)

    def setQuests(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getQuestsType():
        return QuestViewModel

    def _initialize(self):
        super(BattleMattersMainViewModel, self)._initialize()
        self._addViewModelProperty(b'questProgress', QuestProgressModel())
        self._addBoolProperty(b'isRewardsViewOpen', False)
        self._addBoolProperty(b'bootcampIsAvailable', False)
        self._addBoolProperty(b'isBootcampCompleted', False)
        self._addArrayProperty(b'quests', Array())
        self.onShowView = self._addCommand(b'onShowView')
        self.onRunBootcamp = self._addCommand(b'onRunBootcamp')
        self.onShowManual = self._addCommand(b'onShowManual')
        self.onShowManualForQuest = self._addCommand(b'onShowManualForQuest')
        self.onShowAnimForQuest = self._addCommand(b'onShowAnimForQuest')
        self.onShowMainReward = self._addCommand(b'onShowMainReward')
        self.onSelectDelayedReward = self._addCommand(b'onSelectDelayedReward')
        self.onClose = self._addCommand(b'onClose')
        return
