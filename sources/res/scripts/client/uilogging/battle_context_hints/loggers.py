from uilogging.base.logger import MetricsLogger, createPartnerID
from uilogging.battle_context_hints.constants import FEATURE, BattleContextHintsLogActions, BattleContextHintsLogItems
from uilogging.constants import CommonLogActions

class BattleContextHintsLogger(MetricsLogger):
    __slots__ = (b'__partnerId', b'__hintId')

    def __init__(self, hintId):
        super(BattleContextHintsLogger, self).__init__(FEATURE)
        self.__partnerId = createPartnerID()
        self.__hintId = hintId
        return

    def logHintActivated(self):
        self.log(action=BattleContextHintsLogActions.HINT_ACTIVATED, item=self.__hintId, partnerID=self.__partnerId)
        return

    def logHintShowed(self):
        self.log(action=BattleContextHintsLogActions.HINT_SHOWED, item=self.__hintId, partnerID=self.__partnerId)
        return

    def logHintApplied(self):
        self.log(action=BattleContextHintsLogActions.HINT_APPLIED, item=self.__hintId, partnerID=self.__partnerId)
        return

    def logHintMaxViewsReached(self):
        self.log(action=BattleContextHintsLogActions.HINT_MAX_VIEWS_REACHED, item=self.__hintId, partnerID=self.__partnerId)
        return


class BattleContextHintsSettingsLogger(MetricsLogger):

    def __init__(self):
        super(BattleContextHintsSettingsLogger, self).__init__(FEATURE)
        return

    def logResetHintsCountersClicked(self):
        self.log(action=CommonLogActions.CLICK, item=BattleContextHintsLogItems.RESET_HINTS_COUNTERS_BUTTON)
        return
