from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.quest_progress_model import QuestProgressModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.win_back_quest_model import WinBackQuestModel

class OffersState(Enum):
    AVAILABLE = b'available'
    DISABLED = b'disabled'
    NO_OFFERS = b'no_offers'


class WinBackProgress(QuestProgressModel):
    __slots__ = (b'onTakeReward', b'onTakeAllRewards')

    def __init__(self, properties=8, commands=2):
        super(WinBackProgress, self).__init__(properties=properties, commands=commands)
        return

    def getIsBattlePassActive(self):
        return self._getBool(4)

    def setIsBattlePassActive(self, value):
        self._setBool(4, value)
        return

    def getTimeLeftToClaim(self):
        return self._getNumber(5)

    def setTimeLeftToClaim(self, value):
        self._setNumber(5, value)
        return

    def getOffersState(self):
        return OffersState(self._getString(6))

    def setOffersState(self, value):
        self._setString(6, value.value)
        return

    def getQuests(self):
        return self._getArray(7)

    def setQuests(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getQuestsType():
        return WinBackQuestModel

    def _initialize(self):
        super(WinBackProgress, self)._initialize()
        self._addBoolProperty(b'isBattlePassActive', False)
        self._addNumberProperty(b'timeLeftToClaim', 0)
        self._addStringProperty(b'offersState')
        self._addArrayProperty(b'quests', Array())
        self.onTakeReward = self._addCommand(b'onTakeReward')
        self.onTakeAllRewards = self._addCommand(b'onTakeAllRewards')
        return
