from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.epic_quest_progress import EpicQuestProgress
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.win_back_progress import WinBackProgress

class RewardProgressTypes(Enum):
    EPICQUEST = b'epicQuest'
    WINBACK = b'winBack'
    DISABLED = b'disabled'


class RewardProgressBlockModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(RewardProgressBlockModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def epicQuestProgress(self):
        return self._getViewModel(0)

    @staticmethod
    def getEpicQuestProgressType():
        return EpicQuestProgress

    @property
    def winBackProgress(self):
        return self._getViewModel(1)

    @staticmethod
    def getWinBackProgressType():
        return WinBackProgress

    def getProgressType(self):
        return RewardProgressTypes(self._getString(2))

    def setProgressType(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(RewardProgressBlockModel, self)._initialize()
        self._addViewModelProperty(b'epicQuestProgress', EpicQuestProgress())
        self._addViewModelProperty(b'winBackProgress', WinBackProgress())
        self._addStringProperty(b'progressType')
        return
