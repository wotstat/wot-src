from __future__ import absolute_import
import logging
from chat_shared import SYS_MESSAGE_TYPE
from gui.game_control.AwardController import ServiceChannelHandler
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.gf_notifications import pushGFNotification
from helpers import dependency
from journey_marathon.gui.game_control.jm_components.jm_sys_messages import JmBonusFormatter
from journey_marathon.gui.impl.lobby.gf_notifications import JMGFNotificationTemplates
from journey_marathon.gui.shared.jm_event_dispatcher import showJmAnniversaryPresentScreen
from journey_marathon.jm_helpers import jmCtrl
from journey_marathon.skeletons.game_control import IJourneyMarathonController
from journey_marathon_common.journey_marathon_constants import isDailyRewardQuest
from messenger import g_settings
from messenger.formatters.service_channel_helpers import MessageData
from messenger.formatters.token_quest_subformatters import SyncTokenQuestsSubFormatter
_logger = logging.getLogger(__name__)

class JMDailyQuestHandler(ServiceChannelHandler):
    jmCtrl = dependency.descriptor(IJourneyMarathonController)

    def __init__(self, awardCtrl):
        super(JMDailyQuestHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        return

    def _needToShowAward(self, ctx):
        if not super(JMDailyQuestHandler, self)._needToShowAward(ctx):
            return False
        else:
            if self.jmCtrl.jmNodes.getJmNodes().getIsAllJmNodesExplored():
                return False
            _, message = ctx
            completedQuests = message.data.get(b'completedQuestIDs', None)
            return completedQuests and any(isDailyRewardQuest(questID) for questID in completedQuests)

    def _showAward(self, ctx):
        _, message = ctx
        coinToken, _, __ = self.jmCtrl.jmTokens.getJmCoinToken()
        if coinToken not in message.data.get(b'tokens', ()):
            return
        tokenDict = message.data[b'tokens'][coinToken]
        count = tokenDict.get(b'count') or 1
        messageData = {b'count': count}
        pushGFNotification(JMGFNotificationTemplates.DAILY_REWARD, data=messageData)
        return


class JmAnniversaryPresentQuestHandler(ServiceChannelHandler):

    def __init__(self, awardCtrl):
        super(JmAnniversaryPresentQuestHandler, self).__init__(SYS_MESSAGE_TYPE.tokenQuests.index(), awardCtrl)
        return

    def _needToShowAward(self, ctx):
        if not super(JmAnniversaryPresentQuestHandler, self)._needToShowAward(ctx):
            return False
        _, message = ctx
        return bool(getRawBonusesForAnniversaryPresent(message))

    def _showAward(self, ctx):
        _, message = ctx
        rawBonuses = getRawBonusesForAnniversaryPresent(message)
        showJmAnniversaryPresentScreen(rawBonuses)
        return


class JmAnniversaryPresentFormatter(SyncTokenQuestsSubFormatter):
    jmCtrl = dependency.descriptor(IJourneyMarathonController)
    __FORMATTER_NAME = b'InformationHeaderSysMessage'

    def __init__(self):
        super(JmAnniversaryPresentFormatter, self).__init__()
        self._achievesFormatter = JmBonusFormatter()
        return

    def format(self, data, *args):
        rawBonuses = getRawBonusesForAnniversaryPresent(data)
        if not rawBonuses:
            _logger.error(b'No bonuses found in chat action: data=%s', data)
            return [
             MessageData(None, None)]
        else:
            header = backport.text(R.strings.journey_marathon.systemMessage.anniversaryPresent.header())
            formattedAchieves = self._achievesFormatter.formatQuestAchieves(rawBonuses, False)
            formattedMessage = g_settings.msgTemplates.format(self.__FORMATTER_NAME, ctx={b'header': header, b'text': formattedAchieves})
            settings = self._getGuiSettings(data, key=self.__FORMATTER_NAME)
            return [
             MessageData(formattedMessage, settings)]

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return questID == cls.jmCtrl.jmConfig.getJmAnniversaryPresentQuestId()


def getRawBonusesForAnniversaryPresent(message):
    qID = jmCtrl().jmConfig.getJmAnniversaryPresentQuestId()
    return message.data.get(b'detailedRewards', {}).get(qID) or {}
