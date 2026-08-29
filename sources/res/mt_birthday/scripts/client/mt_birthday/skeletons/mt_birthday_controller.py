import typing
from skeletons.gui.game_control import IGameController
from gui.server_events.event_items import Quest
from th_async import th_async
if typing.TYPE_CHECKING:
    from typing import Sequence, List, Dict, Optional, Tuple
    from mt_birthday.skeletons.sub_controllers import IGiftSystemSubController, ITanksBirthdayProgressionSubController
    from gui.shared.view_helpers.UsersInfoHelper import BatchUsersInfoHelper
    from gui.Scaleform.daapi.view.lobby.hangar.entry_points.gf_header_widget import GFWidgetAliases
    from mt_birthday.gui.feature_types import BattlePlayerData
    from Event import Event

class ITanksBirthdayController(IGameController):
    onEventSettingsUpdated = None
    onNewGiftsReceived = None
    onLootboxSeen = None
    onQuestsUpdated = None

    @property
    def progression(self):
        raise NotImplementedError
        return

    @property
    def giftSystem(self):
        raise NotImplementedError
        return

    @property
    def userInfoHelper(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isPaused(self):
        raise NotImplementedError
        return

    def isDisabled(self):
        raise NotImplementedError
        return

    def isEnding(self):
        raise NotImplementedError
        return

    def isAlreadyReceivedGift(self, spaID):
        raise NotImplementedError
        return

    def isBlogger(self):
        raise NotImplementedError
        return

    def isPlayerBlocked(self, spaID):
        raise NotImplementedError
        return

    def isPlayerInBlackList(self, spaID):
        raise NotImplementedError
        return

    def getHangarWidgetAlias(self):
        raise NotImplementedError
        return

    def getExpiryTime(self):
        raise NotImplementedError
        return

    def getBadgeQuestRequiredReplyTokens(self):
        raise NotImplementedError
        return

    def getStartTime(self):
        raise NotImplementedError
        return

    def getEventState(self):
        raise NotImplementedError
        return

    def getLastFightsPlayers(self):
        raise NotImplementedError
        return

    def addLastFightsPlayerID(self, playerId):
        raise NotImplementedError
        return

    def addLastFightsPlayersIDs(self, playersIDs):
        raise NotImplementedError
        return

    def getBannedPlayersIDs(self):
        raise NotImplementedError
        return

    def addBannedPlayersID(self, playerID):
        raise NotImplementedError
        return

    def getStampCount(self):
        raise NotImplementedError
        return

    def getPhrasesIds(self):
        raise NotImplementedError
        return

    def setPhrasesIds(self, phrasesIds):
        raise NotImplementedError
        return

    def getGoldenTicketsCount(self):
        raise NotImplementedError
        return

    def getMaxSelectedPlayers(self):
        raise NotImplementedError
        return

    def getSpecialStampCount(self):
        raise NotImplementedError
        return

    def getCooldownGiftTime(self):
        raise NotImplementedError
        return

    def getLocalEndDate(self):
        raise NotImplementedError
        return

    def getEconomicBonusTypes(self):
        raise NotImplementedError
        return

    def getEconomyBonusValue(self):
        raise NotImplementedError
        return

    def getBattleQuests(self):
        raise NotImplementedError
        return

    def getQuestGiverBattleQuests(self):
        raise NotImplementedError
        return

    def hasActiveQuestGiverQuest(self):
        raise NotImplementedError
        return

    def getMaxProgressionLevel(self):
        raise NotImplementedError
        return

    def getUnseenGiftsCount(self):
        raise NotImplementedError
        return

    def getUnseenGiftId(self):
        raise NotImplementedError
        return

    def pushNewGiftReceived(self, giftId, count):
        raise NotImplementedError
        return

    def seenGiftNotification(self, count):
        raise NotImplementedError
        return

    def getNewGiftForNotification(self):
        raise NotImplementedError
        return

    def getGoldWagonURL(self):
        raise NotImplementedError
        return

    def isGoldWagonEnabled(self):
        raise NotImplementedError
        return

    def getTicketExchangeURL(self):
        raise NotImplementedError
        return

    def isTicketExchangeEnabled(self):
        raise NotImplementedError
        return

    @staticmethod
    def getRandomBloggerPhraseID(currPhraseID=None):
        raise NotImplementedError
        return

    def shufflePhrases(self):
        raise NotImplementedError
        return

    def shuffleLastPhrases(self):
        raise NotImplementedError
        return

    def getNextPhraseID(self):
        raise NotImplementedError
        return

    def getAccountSettingsTipPathByTabId(self, tabId=None):
        raise NotImplementedError
        return

    def isGeneralTipCompleted(self):
        raise NotImplementedError
        return

    def isTabTipsCompleted(self, tabId=None):
        raise NotImplementedError
        return

    @th_async
    def sendGifts(self, stampType, receiversIDs, messageIdx, arenaUniqueID=None):
        raise NotImplementedError
        return


class ILastBattlesPlayersController(IGameController):

    def getLastFightsPlayers(self):
        raise NotImplementedError
        return

    def addLastFightsPlayerID(self, playerId):
        raise NotImplementedError
        return

    def addLastFightsPlayersIDs(self, playersIDs):
        raise NotImplementedError
        return
