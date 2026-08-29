import itertools, logging
from gui.battle_results.components.base import StatsItem
from gui.battle_results.templates.regular import TEAM_STATS_UI_LINK
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from helpers.events_handler import EventsHandler
from helpers.extension_components import ExtensionComponent, extensionMethod
from gui.gift_system.constants import GifterResponseState
from gui.gift_system.wrappers import SendGiftResponse
from helpers import dependency
from messenger.m_constants import USER_ACTION_ID
from messenger.proto.events import g_messengerEvents
from mt_birthday.birthday_constants import BIRTHDAY_STAMP_CODE, BIRTHDAY_STAMP_CODE_SPECIAL, POST_BATTLE_REDEFINED_TAB_UI
from mt_birthday.gui.shared.event_dispatcher import showQuestsToEarnStamps
from mt_birthday.skeletons.mt_birthday_controller import ITanksBirthdayController
from skeletons.gui.battle_results import IBattleResultsService
from th_async import th_async, th_await
_logger = logging.getLogger(__name__)

class GiftSystemDataProvider(object):
    __mtBirthday = dependency.descriptor(ITanksBirthdayController)

    def __init__(self):
        self.__data = {b'isEnabled': False}
        return

    def getVO(self):
        return self.__data

    def prepareData(self, arenaUniqueID, battleResultsData):
        isEnabled = self.__mtBirthday.isEnabled()
        self.__data[b'isEnabled'] = isEnabled
        self.updateStampBalance(arenaUniqueID)
        if isEnabled:
            players = set()
            for teamMember in itertools.chain(battleResultsData[b'team1'], battleResultsData[b'team2']):
                databaseID = teamMember[b'playerId']
                if not teamMember[b'isSelf'] and self.__mtBirthday.isPlayerBlocked(databaseID):
                    players.add(databaseID)

            self.__data[b'blockedPlayers'] = [p for p in players]
        else:
            self.__data[b'blockedPlayers'] = []
        self.__data[b'bannerTitle'] = backport.text(R.strings.battle_results.giftSystem.banner.title(), emphasized=text_styles.brownText(backport.text(R.strings.battle_results.giftSystem.banner.title.emphasized())))
        return

    def updateSendInProgress(self, inSendProgressPlayer):
        self.__data[b'inSendProgressPlayer'] = inSendProgressPlayer
        return

    def updateStampBalance(self, arenaUniqueID):
        self.__data[b'stamp'] = {b'name': BIRTHDAY_STAMP_CODE, b'count': (self.__mtBirthday.getStampCount())}
        self.__data[b'specialStamp'] = {b'name': BIRTHDAY_STAMP_CODE_SPECIAL, b'count': 0}
        if self.__mtBirthday.isFirstBloggerAfterBattleGift(arenaUniqueID) and self.__mtBirthday.getSpecialStampCount():
            self.__data[b'specialStamp'][b'count'] = 1
        return

    def updatePlayersStatus(self, playerIDs):
        if b'blockedPlayers' in self.__data:
            self.__data[b'blockedPlayers'] = [playerId for playerId in self.__data[b'blockedPlayers'] if playerId not in playerIDs]
            for playerId in playerIDs:
                if self.__mtBirthday.isPlayerBlocked(playerId):
                    self.__data[b'blockedPlayers'].append(playerId)

        return


class BattleResultsWindowGiftsComponent(ExtensionComponent, EventsHandler):
    __mtBirthday = dependency.descriptor(ITanksBirthdayController)
    __battleResults = dependency.descriptor(IBattleResultsService)

    def __init__(self, battleResultPoxy):
        super(BattleResultsWindowGiftsComponent, self).__init__(battleResultPoxy)
        self.__arenaUniqueId = self.parent.getArenaUniqueID()
        self.__initData()
        self._subscribe()
        self.__isDestroyed = False
        _logger.info(b'BattleResultsWindowGiftsComponent crated')
        return

    def destroy(self):
        self.__isDestroyed = True
        self._unsubscribe()
        super(BattleResultsWindowGiftsComponent, self).destroy()
        _logger.info(b'BattleResultsWindowGiftsComponent destroyed')
        return

    @extensionMethod
    @th_async
    def sendGift(self, playerId, stampName):
        if not self.__mtBirthday.isEnabled():
            return
        if self.__mtBirthday.isGiftSystemEventActive:
            self.__data.updateSendInProgress(playerId)
            self._updateData()
            result = yield th_await(self.__mtBirthday.sendGifts(stampName, [
             playerId], self.__mtBirthday.getRandomBloggerPhraseID(), arenaUniqueID=self.__arenaUniqueId))
            self.__onSentCallback(result)
        else:
            _logger.debug(b'GIft Event is not enabled, cannot send gift')
        return

    @extensionMethod
    def gotoGiftStamps(self):
        if not self.__mtBirthday.isEnabled():
            return
        showQuestsToEarnStamps()
        self.parent.onWindowClose()
        return

    def _updateData(self):
        self.parent.as_setGiftSystemDataS(self.__data.getVO())
        return

    def _getEvents(self):
        return (
         (
          self.__mtBirthday.giftSystem.updateStampBalance, self.__onEntitlementsUpdated),
         (
          self.__mtBirthday.giftSystem.onOutcomeGift, self.__onOutcomeGift),
         (
          self.__mtBirthday.giftSystem.onWebStateUpdated, self.__onWebStateUpdated),
         (
          self.__mtBirthday.onEventSettingsUpdated, self.__onEventSettingsUpdated),
         (
          g_messengerEvents.users.onUserActionReceived, self.__onUserActionReceived))

    def __onOutcomeGift(self, sendGiftInfo, *_, **__):
        if not isinstance(sendGiftInfo, SendGiftResponse):
            return
        if sendGiftInfo.receiverIDs:
            self.__data.updatePlayersStatus(sendGiftInfo.receiverIDs)
            self._updateData()
        return

    def __onUserActionReceived(self, actionID, user, *_, **__):
        if actionID in (USER_ACTION_ID.IGNORED_ADDED,
         USER_ACTION_ID.IGNORED_REMOVED):
            self.__data.updatePlayersStatus((user.getID(),))
            self._updateData()
        return

    def __onWebStateUpdated(self, *_, **__):
        self.__fullUpdate()
        return

    def __onEventSettingsUpdated(self):
        self.__fullUpdate()
        return

    def __onEntitlementsUpdated(self):
        self.__data.updateStampBalance(self.__arenaUniqueId)
        self._updateData()
        return

    def __onSentCallback(self, result):
        if self.__isDestroyed:
            return
        if result.state is GifterResponseState.WEB_SUCCESS:
            if result.entitlementCode == BIRTHDAY_STAMP_CODE_SPECIAL and result.receiverIDs == result.declinedReceivers:
                self.__data.updateStampBalance(self.__arenaUniqueId)
            self.__data.updatePlayersStatus(result.receiverIDs)
        self.__data.updateSendInProgress(-1)
        self._updateData()
        return

    def __initData(self):
        self.__data = GiftSystemDataProvider()
        self.__fullUpdate()
        return

    def __fullUpdate(self):
        self.__battleResultsData = self.__battleResults.getResultsVO(self.__arenaUniqueId)
        self.__data.prepareData(self.__arenaUniqueId, self.__battleResultsData)
        self._updateData()
        return


class GiftSystemTeamStatsLink(StatsItem):
    __mtBirthday = dependency.descriptor(ITanksBirthdayController)

    def getVO(self):
        if self.__mtBirthday.isEnabled():
            return POST_BATTLE_REDEFINED_TAB_UI
        return TEAM_STATS_UI_LINK
