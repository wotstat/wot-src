import json
from wotdecorators import noexcept
from itertools import chain
from uilogging.base.logger import MetricsLogger
from armory_yard.uilogging.armory_yard.constants import FEATURE, FREE_REROLL, Actions, Items

class ArmoryYardLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(ArmoryYardLogger, self).__init__(FEATURE)
        return

    @noexcept
    def logRerollQuest(self, questData, currency):
        currency = currency if currency else FREE_REROLL
        self.log(action=Actions.CLICK, item=Items.REROLL_BUTTON, info=json.dumps(questData), itemState=currency)
        return

    @noexcept
    def getQuestSnapshot(self, questSubModel):
        snapshot = {}
        for quest in questSubModel.getQuests():
            questId = quest.getId().split(b':', 1)[1]
            snapshot[questId] = {b'current': [], b'total': []}
            if quest.getTotal():
                self._addQuestProgress(snapshot, questId, quest)
            else:
                for condition in chain(quest.bonusCondition.getItems(), quest.postBattleCondition.getItems()):
                    if condition.getTotal():
                        self._addQuestProgress(snapshot, questId, quest)

        return snapshot

    def _addQuestProgress(self, snapshot, questId, quest):
        snapshot[questId][b'current'].append(quest.getCurrent())
        snapshot[questId][b'total'].append(quest.getTotal())
        return
