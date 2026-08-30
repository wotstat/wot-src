from gui.Scaleform.daapi.view.meta.EpicQuestProgressInfoMeta import EpicQuestProgressInfoMeta
from gui.shared import g_eventBus, events
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService

class EpicQuestProgressView(EpicQuestProgressInfoMeta):
    __slots__ = ()
    __battleResults = dependency.descriptor(IBattleResultsService)

    def showQuestById(self, questId, eventType):
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.BATTLE_RESULTS_SHOW_QUEST, ctx={b'questId': questId, 
           b'eventType': eventType}))
        return

    def updateQuestsInfo(self, arenaUniqueID):
        battleResultsVO = self.__battleResults.getResultsVO(arenaUniqueID)
        if not battleResultsVO:
            return
        quests = []
        quests.extend(battleResultsVO.get(b'battlePass', []))
        quests.extend(battleResultsVO.get(b'quests', []))
        questsArray = []
        for quest in quests:
            questInfo = quest[b'questInfo']
            questModel = {b'id': (questInfo[b'questID']), 
               b'eventType': (questInfo[b'eventType']), 
               b'name': (quest.get(b'title', b'') or questInfo.get(b'description', b'')), 
               b'progressList': (quest[b'progressList']), 
               b'status': (questInfo[b'status']), 
               b'statusTooltip': (questInfo.get(b'statusTooltip', b''))}
            rewards = self.__getRewards(quest)
            if rewards:
                questModel[b'rewards'] = [
                 {b'linkage': b'EpicQuestTextAwardBlockUI', 
                    b'items': [
                             (b', ').join(rewards)]}]
            questsArray.append(questModel)

        self.as_updateDataS(questsArray)
        return

    @staticmethod
    def __getRewards(quest):
        awards = quest.get(b'awards', [])
        if not awards:
            return []
        return [item for award in awards for item in award.get(b'items', [])]
