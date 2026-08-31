from __future__ import absolute_import
import logging
from future.utils import viewvalues, viewitems
from adisp import adisp_async, adisp_process
from constants import LOOTBOX_TOKEN_PREFIX
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from helpers import dependency
from messenger import g_settings
from messenger.formatters.service_channel import BattleResultsFormatter
from messenger.formatters.service_channel import WaitItemsSyncFormatter
from messenger.formatters.service_channel_helpers import MessageData
from skeletons.gui.server_events import IEventsCache
from soft_exception import SoftException
from white_tiger.skeletons.economics_controller import IEconomicsController
from white_tiger_common.wt_constants import WT_TEAMS
from white_tiger.gui.white_tiger_gui_constants import WT_QUEST_BOSS_GROUP_ID, HUNTER_QUEST_CHAINS
_logger = logging.getLogger(__name__)

class WTTicketTokenWithdrawnFormatter(WaitItemsSyncFormatter):
    __TEMPLATE = b'wtTicketTokenWithdrawn'
    __economicsCtrl = dependency.descriptor(IEconomicsController)

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        data = message.data
        isSynced = yield self._waitForSyncItems()
        if isSynced and data:
            token = data[b'token']
            amountDelta = data[b'amount_delta']
            if amountDelta >= 0:
                raise SoftException(b'Unexpected ticket amount to withdraw')
            strRes = R.strings.white_tiger_lobby.notifications
            if token == self.__economicsCtrl.getTicketTokenName():
                text = backport.text(strRes.ticketToken.withdrawn.body(), ticketsCount=str(self.__economicsCtrl.getTicketCount()))
            elif token == self.__economicsCtrl.getQuickTicketTokenName():
                text = backport.text(strRes.quickBossTicketToken.withdrawn.body())
            else:
                raise SoftException(b'Unexpected ticket token')
            ctx = {b'text': text, b'description': b''}
            formatted = g_settings.msgTemplates.format(self.__TEMPLATE, ctx=ctx)
            callback([MessageData(formatted, self._getGuiSettings(message, self.__TEMPLATE))])
        else:
            callback([MessageData(None, None)])
        return


class WTBattleResultsFormatter(BattleResultsFormatter):
    __economicsCtrl = dependency.descriptor(IEconomicsController)
    __eventsCache = dependency.descriptor(IEventsCache)
    _battleResultKeys = {(-1): b'WTBattleResult', 
       0: b'WTEBattleResult', 
       1: b'WTBattleResult'}

    def _prepareFormatData(self, message):
        templateName, ctx = super(WTBattleResultsFormatter, self)._prepareFormatData(message)
        self.__fillWTSpecificCtx(message.data, ctx)
        return (templateName, ctx)

    def __fillWTSpecificCtx(self, battleResults, ctx):
        strRes = R.strings.white_tiger_lobby.notifications.battleResults
        mainResultName = b'victory' if battleResults.get(b'isWinner', -1) == 1 else b'defeat'
        ctx[b'mainResultName'] = backport.text(strRes.dyn(mainResultName).header())
        ctx[b'eventName'] = backport.text(strRes.eventName())
        team = battleResults.get(b'team', -1)
        if team == WT_TEAMS.BOSS_TEAM:
            teamName = backport.text(strRes.team.boss())
        elif team == WT_TEAMS.HUNTERS_TEAM:
            teamName = backport.text(strRes.team.hunters())
        else:
            teamName = b''
            _logger.warning(b'Unexpected team type: %r', team)
        ctx[b'teamName'] = teamName
        ctx[b'quests'] = b''
        completedQuestIDs = battleResults.get(b'completedQuestIDs', ())
        completedQuests = self.__eventsCache.getAllQuests((lambda q: q.getID() in completedQuestIDs))
        completedDailyQuestsCount = sum(1 for q in viewvalues(completedQuests) if q.getGroupID() in HUNTER_QUEST_CHAINS or q.getGroupID() == WT_QUEST_BOSS_GROUP_ID)
        completedBattleQuests = {qname: quest for qname, quest in viewitems(battleResults.get(b'detailedRewards', {})) if b'battle_quest' in qname}
        if completedDailyQuestsCount:
            ctx[b'quests'] = b'<br>%s' % text_styles.main(backport.text(strRes.questCompleted(), questsCompleted=str(completedDailyQuestsCount)))
        ctx[b'stamps'] = b''
        ctx[b'lootboxes'] = b''
        lootboxesStrs = []
        earnedStampsCount = 0
        for quest in viewvalues(completedBattleQuests):
            tokens = quest.get(b'tokens', {})
            stampToken = self.__economicsCtrl.getStampTokenName()
            if stampToken in tokens:
                earnedStampsCount += tokens[stampToken].get(b'count', 0)
            for tID, tVal in viewitems(tokens):
                if tID.startswith(LOOTBOX_TOKEN_PREFIX):
                    lootBox = self._itemsCache.items.tokens.getLootBoxByTokenID(tID)
                    if lootBox is not None:
                        lootboxesStrs.append(backport.text(strRes.lootboxes.wt_lootbox(), count=text_styles.expText(tVal.get(b'count', 0))))

        if earnedStampsCount > 0:
            ctx[b'stamps'] = b'<br>%s' % text_styles.main(backport.text(strRes.stamp(), count=text_styles.expText(earnedStampsCount)))
        if lootboxesStrs:
            ctx[b'lootboxes'] = b'<br>%s' % text_styles.main((b'<br>').join(lootboxesStrs))
        return
