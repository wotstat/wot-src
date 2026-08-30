from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from typing import Callable, List, Optional, Union
    from gui.server_events.event_items import Quest, BattleMattersQuest, BattleMattersTokenQuest
    from gui.game_control.battle_matters_controller import _BattleMattersProgressWatcher
    from gui.shared.gui_items.Vehicle import Vehicle
    from Event import Event

class IBattleMattersController(object):
    __slots__ = (b'onStateChanged', b'onFinish')

    def __init__(self):
        super(IBattleMattersController, self).__init__()
        self.onStateChanged = None
        self.onFinish = None
        return

    @staticmethod
    def isBattleMattersQuest(quest):
        raise NotImplementedError
        return

    @staticmethod
    def isBattleMattersQuestID(questID):
        raise NotImplementedError
        return

    @staticmethod
    def isRegularBattleMattersQuestID(questID):
        raise NotImplementedError
        return

    @staticmethod
    def isRegularBattleMattersQuest(quest):
        raise NotImplementedError
        return

    @staticmethod
    def isCompensationBattleMattersQuestID(questID):
        raise NotImplementedError
        return

    @staticmethod
    def isCompensationBattleMattersQuest(quest):
        raise NotImplementedError
        return

    @staticmethod
    def isIntermediateBattleMattersQuest(quest):
        raise NotImplementedError
        return

    @staticmethod
    def isIntermediateBattleMattersQuestID(questID):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isPaused(self):
        raise NotImplementedError
        return

    def isFinished(self):
        raise NotImplementedError
        return

    def isActive(self):
        raise NotImplementedError
        return

    @property
    def progressWatcher(self):
        raise NotImplementedError
        return

    def hasDelayedRewards(self):
        raise NotImplementedError
        return

    def hasDelayedRewardsInQuest(self, quest):
        raise NotImplementedError
        return

    def isFinalQuest(self, quest):
        raise NotImplementedError
        return

    def getFinalQuest(self):
        raise NotImplementedError
        return

    def getQuestByIdx(self, questIdx):
        raise NotImplementedError
        return

    def getCompletedBattleMattersQuests(self):
        raise NotImplementedError
        return

    def getCompletedBattleMattersQuestsCount(self):
        raise NotImplementedError
        return

    def getNotCompletedBattleMattersQuests(self):
        raise NotImplementedError
        return

    def getQuestsWithDelayedReward(self):
        raise NotImplementedError
        return

    def getRegularBattleMattersQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getCompensationBattleMattersQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getBattleMattersQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def hasLinkedIntermediateQuest(self, quest):
        raise NotImplementedError
        return

    def getIntermediateQuests(self):
        raise NotImplementedError
        return

    def getCountBattleMattersQuests(self):
        raise NotImplementedError
        return

    def showAwardView(self, questsData, clientCtx=None):
        raise NotImplementedError
        return

    def getCurrentQuest(self):
        raise NotImplementedError
        return

    def getQuestProgress(self, quest):
        raise NotImplementedError
        return

    def getSelectedVehicle(self):
        raise NotImplementedError
        return

    def hasAccessToken(self):
        raise NotImplementedError
        return

    def getDelayedRewardCurrencyToken(self):
        raise NotImplementedError
        return

    def getDelayedRewardToken(self):
        raise NotImplementedError
        return
