from __future__ import absolute_import
from typing import Any, Callable, Generator
import Event
from collections import namedtuple
from adisp import adisp_async
from gui import SystemMessages
from gui.impl.lobby.gf_notifications import pushGFNotification
from gui.shared.utils import decorators
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.server_events.bonuses import getNonQuestBonuses
from halloween.gui.impl.lobby.gf_notifications.constants import HalloweenGFNotificationTemplates
from halloween.gui.shared.gui_items.processors.processors import ExchangeCommandersProcessor
from halloween.skeletons.halloween_controller import IHalloweenController
from halloween.skeletons.halloween_twitch_con_controller import IHalloweenTwitchConController
from helpers import dependency
from skeletons.gui.server_events import IEventsCache

class Commander(namedtuple(b'Commander', (b'commanderID', b'limit', b'bonuses', b'shopLimit', b'url', b'sound'))):

    def getCtx(self):
        return dict(self._asdict())


class HalloweenTwitchConController(IHalloweenTwitchConController):
    eventsCache = dependency.descriptor(IEventsCache)
    halloweenCtrl = dependency.descriptor(IHalloweenController)

    def __init__(self):
        super(HalloweenTwitchConController, self).__init__()
        self._eventManager = Event.EventManager()
        self.onTwitchConSettingsUpdated = Event.Event(self._eventManager)
        self.onLimitsUpdated = Event.Event(self._eventManager)
        self.onShopLimitsUpdated = Event.Event(self._eventManager)
        self.onCertificateCountUpdated = Event.Event(self._eventManager)
        self._commanders = {}
        return

    def init(self):
        g_clientUpdateManager.addCallbacks({b'tokens': (self.__handleTokensUpdate)})
        self.halloweenCtrl.onSettingsUpdate += self.__updateSettings
        return

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.halloweenCtrl.onSettingsUpdate -= self.__updateSettings
        self._eventManager.clear()
        self._commanders = {}
        return

    def isEnabled(self):
        return self._getConfig().get(b'enabled', False)

    def isPromoScreenEnabled(self):
        return self._getConfig().get(b'promoScreenEnabled', False)

    def getFullCrewSound(self):
        return self._getConfig().get(b'fullCrewSound', b'')

    def commanders(self):
        return sorted(self._commanders.values(), key=(lambda commander: commander.commanderID))

    def getCommanderByID(self, commanderID):
        return self._commanders.get(commanderID)

    def getCertificateTokenName(self):
        return self._getConfig().get(b'certificate_token', b'')

    def onLobbyStarted(self, ctx):
        super(HalloweenTwitchConController, self).onLobbyStarted(ctx)
        self._initCommanders()
        return

    @adisp_async
    @decorators.adisp_process(b'updating')
    def exchangeCommander(self, commandersData, callback):
        result = yield ExchangeCommandersProcessor(self, commandersData).request()
        if result.success:
            for commanderID, _ in commandersData:
                pushGFNotification(HalloweenGFNotificationTemplates.CREW_REWARD_NOTIFICATION, {b'commanderID': commanderID})

        elif result.userMsg:
            SystemMessages.pushMessage(result.userMsg, type=result.sysMsgType)
        callback(result.success)
        return

    def getCertificateCount(self):
        if not self.getCertificateTokenName():
            return 0
        return self.eventsCache.questsProgress.getTokenCount(self.getCertificateTokenName())

    def getExchangedCountByCommanderID(self, commanderID):
        return self.eventsCache.questsProgress.getTokenCount(commanderID + self._getExchanedSuffix())

    def getBlockCardCountByCommanderID(self, commanderID):
        return self.eventsCache.questsProgress.getTokenCount(commanderID + self._getBlockCardSuffix())

    def canExchangeCertificateByCommanderID(self, commanderID):
        return self.getRemainLimits(commanderID) > 0

    def getRemainLimits(self, commanderID):
        commander = self.getCommanderByID(commanderID)
        if not commander:
            return 0
        exchangedCount = self.getExchangedCountByCommanderID(commanderID)
        return max(0, commander.limit - exchangedCount)

    def getRemainShopLimits(self, commanderID):
        commander = self.getCommanderByID(commanderID)
        if not commander:
            return 0
        exchangedCount = self.getBlockCardCountByCommanderID(commanderID)
        return max(0, commander.shopLimit - exchangedCount)

    def _initCommanders(self):
        self._commanders = dict((commanderID, Commander(commanderID=commanderID, limit=self._getExchangedLimit(commanderID), bonuses=self._getBonuses(commanderID), shopLimit=self._getShopLimit(commanderID), url=self._getUrl(commanderID), sound=self._getSound(commanderID))) for commanderID in self._getCommanders())
        return

    def _getExchangedLimit(self, commanderID):
        return self._getCommanders().get(commanderID, {}).get(b'limit', 0)

    def _getShopLimit(self, commanderID):
        return self._getCommanders().get(commanderID, {}).get(b'shop_limit', 0)

    def _getUrl(self, commanderID):
        return self._getCommanders().get(commanderID, {}).get(b'url', b'')

    def _getSound(self, commanderID):
        return self._getCommanders().get(commanderID, {}).get(b'sound', b'')

    def _getCommanders(self):
        return self._getConfig().get(b'commanders', {})

    def _getBonuses(self, commanderID):
        rewards = []
        bonuses = self._getCommanders().get(commanderID, {}).get(b'bonus', {})
        for bonusType, bonusValue in bonuses.items():
            rewards.extend(getNonQuestBonuses(bonusType, bonusValue))

        return rewards

    def _getConfig(self):
        return self.halloweenCtrl.getModeSettings().twitch_con

    def _getExchanedSuffix(self):
        return self._getConfig().get(b'exchange_suffix', b'')

    def _getBlockCardSuffix(self):
        return self._getConfig().get(b'block_card_suffix', b'')

    def _getConfigPrefix(self):
        return self._getConfig().get(b'prefix', b'')

    def __updateSettings(self):
        self._initCommanders()
        self.onTwitchConSettingsUpdated()
        return

    def __handleTokensUpdate(self, diff):
        for token in diff:
            if token.startswith(self.getCertificateTokenName()):
                self.onCertificateCountUpdated()
            if token.startswith(self._getConfigPrefix()):
                if token.endswith(self._getExchanedSuffix()):
                    self.onLimitsUpdated()
                if token.endswith(self._getBlockCardSuffix()):
                    self.onShopLimitsUpdated()

        return
