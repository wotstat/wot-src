from __future__ import absolute_import
import logging
from functools import partial
import BigWorld, constants
from adisp import adisp_process
from constants import PremiumConfigs
from gui import SystemMessages
from gui import makeHtmlString
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.customization.progression_helpers import parseEventID
from gui.Scaleform.daapi.view.lobby.customization.sound_constants import SOUNDS
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl, getWotPlusShopUrl
from gui.Scaleform.daapi.view.meta.BattleResultsMeta import BattleResultsMeta
from gui.Scaleform.framework.entities.View import ViewKey
from gui.battle_results import RequestEmblemContext, EMBLEM_TYPE
from gui.battle_results.settings import PROGRESS_ACTION
from gui.prb_control.dispatcher import g_prbLoader
from gui.prestige.prestige_helpers import showPrestigeVehicleStats
from gui.prb_control.entities.listener import IGlobalListener
from gui.server_events import events_dispatcher as quests_events
from gui.server_events.events_helpers import isC11nQuest
from gui.shared import events, EVENT_BUS_SCOPE, g_eventBus
from gui.shared import event_dispatcher
from gui.shared.event_dispatcher import showProgressiveRewardWindow, showShop, showDailyExpPageView
from gui.sounds.ambients import BattleResultsEnv
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.game_control import IGameSessionController
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
_logger = logging.getLogger(__name__)

def _wrapEmblemUrl(emblemUrl):
    return makeHtmlString(b'html_templates:lobby/battleResult', b'emblemUrl', {b'url': emblemUrl})


class IBattleResultsComponent(object):

    def setArenaUniqueID(self, arenaUniqueID):
        return


class BattleResultsWindow(BattleResultsMeta, IGlobalListener):
    __battleResults = dependency.descriptor(IBattleResultsService)
    __lobbyContext = dependency.descriptor(ILobbyContext)
    __gameSession = dependency.descriptor(IGameSessionController)
    __appLoader = dependency.descriptor(IAppLoader)
    __itemsCache = dependency.descriptor(IItemsCache)
    __sound_env__ = BattleResultsEnv

    def __init__(self, ctx):
        super(BattleResultsWindow, self).__init__()
        if b'arenaUniqueID' not in ctx:
            raise SoftException(b'Key "arenaUniqueID" is not found in context', ctx)
        if not ctx[b'arenaUniqueID']:
            raise SoftException(b'Value of "arenaUniqueID" must be greater than 0')
        self.__arenaUniqueID = ctx[b'arenaUniqueID']
        self.__dataSet = False
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        if isinstance(viewPy, IBattleResultsComponent):
            viewPy.setArenaUniqueID(arenaUniqueID=self.__arenaUniqueID)
        return

    def onWindowClose(self):
        self.destroy()
        return

    @adisp_process
    def showEventsWindow(self, questID, eventType):
        if self.__canNavigate():
            if eventType == constants.EVENT_TYPE.C11N_PROGRESSION or isC11nQuest(questID):
                app = self.__appLoader.getApp()
                view = app.containerManager.getViewByKey(ViewKey(VIEW_ALIAS.LOBBY_CUSTOMIZATION))
                if view is None:
                    lobbyHeaderNavigationPossible = yield self.__lobbyContext.isHeaderNavigationPossible()
                    if not lobbyHeaderNavigationPossible:
                        return
                if eventType == constants.EVENT_TYPE.C11N_PROGRESSION:
                    _, vehicleIntCD = parseEventID(questID)
                    vehicle = self.__itemsCache.items.getVehicleCopyByCD(vehicleIntCD)
                    if not vehicle.isCustomizationEnabled():
                        _logger.warning(b'Trying to open customization from PBS for incompatible vehicle.')
                        return
                    self.soundManager.playInstantSound(SOUNDS.SELECT)
            else:
                lobbyHeaderNavigationPossible = yield self.__lobbyContext.isHeaderNavigationPossible()
                if not lobbyHeaderNavigationPossible:
                    return
            quests_events.showMission(questID, eventType)
            self.destroy()
        return

    def saveSorting(self, iconType, sortDirection, bonusType):
        self.__battleResults.saveStatsSorting(bonusType, iconType, sortDirection)
        return

    def getClanEmblem(self, textureID, clanDBID):
        self.__requestClanEmblem(textureID, clanDBID)
        return

    def startCSAnimationSound(self, soundEffectID=b'cs_animation_league_up'):
        self.app.soundManager.playEffectSound(soundEffectID)
        return

    def onResultsSharingBtnPress(self):
        raise NotImplementedError(b'This feature is not longer supported')
        return

    def showUnlockWindow(self, itemId, unlockType):
        if not self.__canNavigate():
            return
        if unlockType in (PROGRESS_ACTION.RESEARCH_UNLOCK_TYPE, PROGRESS_ACTION.PURCHASE_UNLOCK_TYPE):
            event_dispatcher.showResearchView(itemId)
        elif unlockType in (PROGRESS_ACTION.NEW_SKILL_UNLOCK_TYPE, PROGRESS_ACTION.NEW_FREE_SKILL_UNLOCK_TYPE):
            event_dispatcher.showPersonalCase(itemId)
        self.onWindowClose()
        return

    def showDogTagWindow(self, componentId):
        if self.__canNavigate():
            event_dispatcher.showDogTags(componentId, False)
            self.destroy()
        return

    def showVehicleStats(self, vehCD):
        if self.__canNavigate():
            showPrestigeVehicleStats(vehCD)
            self.destroy()
        return

    def showProgressiveRewardView(self):
        showProgressiveRewardWindow()
        return

    def onAppliedPremiumBonus(self):
        self.__battleResults.applyAdditionalBonus(self.__arenaUniqueID)
        return

    def onPrbEntitySwitched(self):
        super(BattleResultsWindow, self).onPrbEntitySwitched()
        self.__updateVO()
        return

    def onShowDetailsPremium(self):
        if self.__canNavigate():
            url = getBuyPremiumUrl()
            BigWorld.callback(0.0, partial(showShop, url))
            self.destroy()
        return

    def onShowDetailsWotPlus(self):
        if self.__canNavigate():
            url = getWotPlusShopUrl()
            BigWorld.callback(0.0, partial(showShop, url))
            self.destroy()
        return

    def onShowManageableXPScreen(self):
        if self.__canNavigate():
            showDailyExpPageView()
            self.destroy()
        return

    def _populate(self):
        super(BattleResultsWindow, self)._populate()
        self.addListener(events.LobbySimpleEvent.BATTLE_RESULTS_POSTED, self.__handleBattleResultsPosted, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.HideWindowEvent.HIDE_BATTLE_RESULT_WINDOW, self.__handleBattleResultsClose, scope=EVENT_BUS_SCOPE.LOBBY)
        self.addListener(events.LobbySimpleEvent.PREMIUM_XP_BONUS_CHANGED, self.__onPremiumXpBonusChanged)
        self.addListener(events.LobbySimpleEvent.BATTLE_RESULTS_SHOW_QUEST, self.__onBattleResultWindowShowQuest)
        g_clientUpdateManager.addCallbacks({b'account._additionalXPCache': (self.__updateVO), 
           b'inventory.1': (self.__updateVO), 
           b'inventory.8': (self.__updateVO), 
           b'cache.vehsLock': (self.__updateVO)})
        self.__gameSession.onPremiumTypeChanged += self.__onPremiumStateChanged
        self.__lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingsChange
        self.startGlobalListening()
        if self.__battleResults.areResultsPosted(self.__arenaUniqueID):
            self.__setBattleResults()
            g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.BATTLE_RESULTS_PROCESSED), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _dispose(self):
        self.removeListener(events.LobbySimpleEvent.BATTLE_RESULTS_POSTED, self.__handleBattleResultsPosted, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.HideWindowEvent.HIDE_BATTLE_RESULT_WINDOW, self.__handleBattleResultsClose, scope=EVENT_BUS_SCOPE.LOBBY)
        self.removeListener(events.LobbySimpleEvent.PREMIUM_XP_BONUS_CHANGED, self.__onPremiumXpBonusChanged)
        self.removeListener(events.LobbySimpleEvent.BATTLE_RESULTS_SHOW_QUEST, self.__onBattleResultWindowShowQuest)
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__gameSession.onPremiumTypeChanged -= self.__onPremiumStateChanged
        self.__lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingsChange
        self.stopGlobalListening()
        super(BattleResultsWindow, self)._dispose()
        return

    def onEnqueued(self, queueType, *args):
        self.as_setIsInBattleQueueS(True)
        return

    def onDequeued(self, queueType, *args):
        self.as_setIsInBattleQueueS(False)
        return

    @adisp_process
    def __requestClanEmblem(self, textureID, clanDBID):
        emblemID = yield self.__battleResults.requestEmblem(RequestEmblemContext(EMBLEM_TYPE.CLAN, clanDBID, textureID))
        if not self.isDisposed():
            self.as_setClanEmblemS(textureID, _wrapEmblemUrl(emblemID))
        return

    def __setBattleResults(self):
        if not self.__dataSet:
            battleResultsVO = self.__battleResults.getResultsVO(self.__arenaUniqueID)
            self.as_setDataS(battleResultsVO)
            self.__dataSet = True
        return

    def __handleBattleResultsPosted(self, event):
        ctx = event.ctx
        if b'arenaUniqueID' not in ctx:
            raise SoftException(b'Key "arenaUniqueID" is not found in context', ctx)
        if not ctx[b'arenaUniqueID']:
            raise SoftException(b'Value of "arenaUniqueID" must be greater than 0')
        if self.__arenaUniqueID == ctx[b'arenaUniqueID']:
            self.__setBattleResults()
        return

    def __handleBattleResultsClose(self, _):
        self.destroy()
        return

    @classmethod
    def __canNavigate(cls):
        prbDispatcher = g_prbLoader.getDispatcher()
        if prbDispatcher is not None and prbDispatcher.getFunctionalState().isNavigationDisabled():
            SystemMessages.pushI18nMessage(b'#system_messages:queue/isInQueue', type=SystemMessages.SM_TYPE.Error)
            return False
        else:
            return True

    def __onPremiumStateChanged(self, *_):
        self.__updateVO()
        return

    def __onPremiumXpBonusChanged(self, event):
        if event.ctx.get(b'isBonusApplied', False):
            self.__updateVO()
        return

    def __onBattleResultWindowShowQuest(self, event):
        ctx = event.ctx if event is not None else None
        if ctx is None:
            return
        else:
            if b'questId' in ctx and b'eventType' in ctx:
                self.showEventsWindow(ctx[b'questId'], ctx[b'eventType'])
            return

    def __updateVO(self, _=None):
        battleResultsVO = self.__battleResults.getResultsVO(self.__arenaUniqueID)
        self.as_setDataS(battleResultsVO)
        return

    def __onServerSettingsChange(self, diff):
        if PremiumConfigs.DAILY_BONUS in diff:
            self.__updateVO()
        return
