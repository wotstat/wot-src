from __future__ import absolute_import
import logging, typing, Event
from future.utils import viewvalues
from constants import EVENT_CLIENT_DATA, EVENT_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.prb_control.entities.listener import IGlobalListener
from helpers import dependency
from helpers import time_utils
from gui.server_events.events_helpers import EventInfoModel
from skeletons.gui.game_control import IRestBonusController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Dict, Optional
    from gui.server_events.event_items import Quest
    from gui.shared.gui_items.Vehicle import Vehicle
_logger = logging.getLogger(__name__)
REST_BONUS_PREFIX = b'rest_bonus'
SEPARATOR = b':'
REST_BONUS_ACCESS_TOKEN = REST_BONUS_PREFIX + SEPARATOR + b'xp_boost' + SEPARATOR + b'token'
REST_BONUS_XP_FACTOR_BONUS = b'xpFactor'
REST_BONUS_BASE_FACTOR = 1

class RestBonusController(IRestBonusController, IGlobalListener):
    __slots__ = (b'_questsCache', b'__expiryTime', b'onUpdated')
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __itemsCache = dependency.descriptor(IItemsCache)
    __eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self):
        super(RestBonusController, self).__init__()
        self._questsCache = {}
        self.__expiryTime = 0
        self.onUpdated = Event.Event()
        return

    @property
    def dailyXPFactor(self):
        return self.__itemsCache.items.shop.dailyXPFactor

    @property
    def restBonusQuests(self):
        return self._questsCache

    @staticmethod
    def isRestBonusQuestID(quest):
        return quest.getID().startswith(REST_BONUS_PREFIX)

    def getXpFactor(self, vehicle):
        total = 0.0
        for quest in self.__getActiveBattleQuests(vehicle):
            bonuses = quest.getBonuses(REST_BONUS_XP_FACTOR_BONUS)
            if bonuses:
                total += sum(b.getValue() - REST_BONUS_BASE_FACTOR for b in bonuses)

        if total:
            return total
        else:
            return

    def getRestBonusExpiryTime(self):
        return max(0, self.__expiryTime)

    def getActualXPFactor(self, vehicle):
        xpFactor = self.getXpFactor(vehicle) or 0
        return int(vehicle.dailyXPFactor + xpFactor)

    def getDailyResetTime(self):
        return int(time_utils.getServerUTCTime()) + int(EventInfoModel.getDailyProgressResetTimeDelta())

    def fini(self):
        self.__clear()
        super(RestBonusController, self).fini()
        return

    def onLobbyInited(self, event):
        self.startGlobalListening()
        return

    def onLobbyStarted(self, ctx):
        super(RestBonusController, self).onLobbyStarted(ctx)
        self.__initQuestsCache()
        self.__expiryTime = self.__itemsCache.items.tokens.getTokenExpiryTime(REST_BONUS_ACCESS_TOKEN)
        return

    def onAvatarBecomePlayer(self):
        self.stopGlobalListening()
        return

    def onAccountBecomePlayer(self):
        super(RestBonusController, self).onAccountBecomePlayer()
        self.__addListeners()
        return

    def onAccountBecomeNonPlayer(self):
        super(RestBonusController, self).onAccountBecomeNonPlayer()
        self.__clear()
        return

    def onPrbEntitySwitched(self):
        self.onUpdated()
        return

    def onDisconnected(self):
        self.__clear()
        super(RestBonusController, self).onDisconnected()
        return

    def hasActiveBattleQuest(self, vehicle):
        return bool(self.__getActiveBattleQuests(vehicle))

    def __getActiveBattleQuests(self, vehicle):
        if not self.prbEntity:
            return []
        queueType = self.prbEntity.getQueueType()
        return [q for q in viewvalues(self.restBonusQuests) if q.getType() == EVENT_TYPE.BATTLE_QUEST and self.__isQuestAvailable(q, queueType, vehicle)]

    def __isQuestAvailable(self, quest, queueType, vehicle):
        isAccountOK = quest.accountReqs.isAvailable()
        isVehicleOK = quest.vehicleReqs.isAvailable(vehicle)
        isBattleTypeOK = quest.hasBonusType(queueType)
        return isAccountOK and isVehicleOK and isBattleTypeOK

    def __addListeners(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onSettingsChanged
        self.__itemsCache.onSyncCompleted += self.__onItemsCacheUpdated
        g_clientUpdateManager.addCallbacks({(b'eventsData.' + str(EVENT_CLIENT_DATA.QUEST)): (self.__initQuestsCache)})
        return

    def __removeListeners(self):
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onSettingsChanged
        self.__itemsCache.onSyncCompleted -= self.__onItemsCacheUpdated
        g_clientUpdateManager.removeObjectCallbacks(self)
        return

    def __validateBattleQuests(self):
        for quest in self.restBonusQuests.values():
            if quest.getType() != EVENT_TYPE.BATTLE_QUEST:
                continue
            bonusTypesCond = quest.preBattleCond.getConditions().find(b'bonusTypes')
            if bonusTypesCond is None:
                _logger.error(b"Rest bonus battleQuest '%s' is missing <bonusTypes> in preBattle conditions", quest.getID())

        return

    def __clear(self):
        self.stopGlobalListening()
        self.__removeListeners()
        self._questsCache.clear()
        self.__expiryTime = 0
        return

    def __initQuestsCache(self, *args, **kwargs):
        oldQuestIDs = set(self._questsCache)
        self._questsCache = self.__eventsCache.getAllQuests(filterFunc=self.isRestBonusQuestID)
        self.__validateBattleQuests()
        if set(self._questsCache) != oldQuestIDs:
            self.onUpdated()
        return

    def __onSettingsChanged(self, diff):
        return

    def __onItemsCacheUpdated(self, reason, diff):
        self.__expiryTime = self.__itemsCache.items.tokens.getTokenExpiryTime(REST_BONUS_ACCESS_TOKEN)
        self.__initQuestsCache()
        return
