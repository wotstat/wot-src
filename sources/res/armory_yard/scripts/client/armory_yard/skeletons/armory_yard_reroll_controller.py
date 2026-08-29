import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from armory_yard.gui.shared.armory_dynamic_quest import ArmoryDynamicQuest
    from typing import List, Optional
    from gui.server_events.event_items import TokenQuest
    from Event import Event

class IArmoryYardRerollController(IGameController):
    onQuestConditionUpdated = None
    onQuestConditionsReset = None
    onPDataUpdated = None
    onFreeRerollTokensUpdated = None
    onRerollQuest = None
    onAcceptReroll = None

    def getConditionQuestsByTokenQuest(self, tokenQuest):
        raise NotImplementedError
        return

    def getArmoryTokenQuestByID(self, questID):
        raise NotImplementedError
        return

    def getConditionQuestsByID(self, reqToken):
        raise NotImplementedError
        return

    def getRerollCurrencies(self):
        raise NotImplementedError
        return

    def getRerollCost(self, currency):
        raise NotImplementedError
        return

    def getFreeRerollsCount(self, groupName):
        raise NotImplementedError
        return

    def getFreeRerollsCountByCycleID(self, cycleID):
        raise NotImplementedError
        return

    def getNextFreeRerollTimestamp(self):
        raise NotImplementedError
        return

    def getFreeRerollCountdown(self):
        raise NotImplementedError
        return

    def getHideBattleTypes(self):
        raise NotImplementedError
        return

    def isRerollEnabled(self):
        raise NotImplementedError
        return

    def getTokenQuestIDByConditionID(self, conditionID):
        raise NotImplementedError
        return

    def getReplacedTokenQuestID(self):
        raise NotImplementedError
        return

    def getConditionIDsForReroll(self, replacedTokenQuestID):
        raise NotImplementedError
        return

    def validateAcceptQuestID(self, questID):
        raise NotImplementedError
        return

    def getRerollContext(self):
        raise NotImplementedError
        return
