from __future__ import absolute_import
import logging, BigWorld
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.hof.hof_helpers import getHofTabCounter, isHofButtonNew, showDisabledDialog
from gui.Scaleform.daapi.view.meta.ProfileMeta import ProfileMeta
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.genConsts.PROFILE_CONSTANTS import PROFILE_CONSTANTS
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.Scaleform.locale.PROFILE import PROFILE
from gui.collection.account_settings import getCollectionsTabCounter
from gui.limited_ui.lui_rules_storage import LUI_RULES
from gui.shared import events, g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.ClientUpdateManager import g_clientUpdateManager
from helpers import dependency
from helpers.i18n import makeString
from skeletons.gui.game_control import IAchievements20Controller, ILimitedUIController, ICollectionsSystemController, IAchievementsController
from skeletons.gui.lobby_context import ILobbyContext
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_SOUND_SPACE
from gui.Scaleform.daapi.view.lobby.hof.web_handlers import createHofWebHandlers
from gui.Scaleform.daapi.view.lobby.hof.hof_helpers import getHofDisabledKeys, onServerSettingsChange
from gui.shared.events import ProfilePageEvent, CollectionsEvent
_LUI_RULES = (
 LUI_RULES.profileHof, LUI_RULES.profileTechniquePage)
_logger = logging.getLogger(__name__)

class ProfilePage(LobbySubView, ProfileMeta):
    lobbyContext = dependency.descriptor(ILobbyContext)
    _limitedUIController = dependency.descriptor(ILimitedUIController)
    __achievements20Controller = dependency.descriptor(IAchievements20Controller)
    __advAchmntCtrl = dependency.descriptor(IAchievementsController)
    __collectionsSystem = dependency.descriptor(ICollectionsSystemController)
    _COMMON_SOUND_SPACE = ACHIEVEMENTS_SOUND_SPACE

    def __init__(self, ctx=None):
        self.__ctx = ctx
        LobbySubView.__init__(self)
        self.__tabNavigator = None
        return

    @property
    def tabId(self):
        if self.__tabNavigator:
            return self.__tabNavigator.tabId
        else:
            return

    def registerFlashComponent(self, component, alias, *args):
        if alias == VIEW_ALIAS.PROFILE_TAB_NAVIGATOR:
            player = BigWorld.player()
            super(ProfilePage, self).registerFlashComponent(component, alias, player.name, None, player.databaseID, self.__getSectionsData(), self.__ctx)
        else:
            super(ProfilePage, self).registerFlashComponent(component, alias)
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(ProfilePage, self)._onRegisterFlashComponent(viewPy, alias)
        if alias == VIEW_ALIAS.PROFILE_TAB_NAVIGATOR:
            self.__tabNavigator = viewPy
            g_clientUpdateManager.addCallbacks({b'stats.dossier': (self.__dossierUpdateCallBack)})
            self.__updateTabCounters()
        return

    def onCloseProfile(self):
        lsm = getLobbyStateMachine()
        state = lsm.getStateFromView(self)
        if state:
            state.goBack()
        return

    def updateSubView(self, ctx):
        selectedAlias = ctx.get(b'selectedAlias')
        if selectedAlias is None:
            _logger.error(b'Should be specified "selectedAlias"')
            return
        else:
            self.__ctx.update(ctx)
            self.__tabNavigator.as_setInitDataS(self.__getSectionsData(resetSelectedAlias=True))
            if selectedAlias == VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE:
                techniquePage = self.__tabNavigator.components.get(VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE)
                if techniquePage:
                    techniquePage.updateView(ctx)
            return

    def _populate(self):
        super(ProfilePage, self)._populate()
        self.lobbyContext.getServerSettings().onServerSettingsChange += self.__onServerSettingChanged
        self.__collectionsSystem.onServerSettingsChanged += self.__onCollectionsSettingsChanged
        self.__achievements20Controller.onUpdate += self.__onProfileVisited
        self.__advAchmntCtrl.onUnseenAchievementsUpdate += self.__onUnseenAchievementsUpdate
        g_eventBus.addListener(CollectionsEvent.TAB_COUNTER_UPDATED, self.__onCollectionTabUpdated, EVENT_BUS_SCOPE.LOBBY)
        self._limitedUIController.startObserves(_LUI_RULES, self.__isLuiRuleProfileCompleted)
        if self.__ctx and self.__ctx.get(b'hofPageUrl'):
            self.__loadHofUrl(self.__ctx.get(b'hofPageUrl'))
        return

    def _invalidate(self, *args, **kwargs):
        super(ProfilePage, self)._invalidate(*args, **kwargs)
        if args[0] and args[0].get(b'hofPageUrl'):
            self.__loadHofUrl(args[0].get(b'hofPageUrl'))
        return

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.lobbyContext.getServerSettings().onServerSettingsChange -= self.__onServerSettingChanged
        self.__collectionsSystem.onServerSettingsChanged -= self.__onCollectionsSettingsChanged
        self.__achievements20Controller.onUpdate -= self.__onProfileVisited
        self.__advAchmntCtrl.onUnseenAchievementsUpdate -= self.__onUnseenAchievementsUpdate
        g_eventBus.removeListener(CollectionsEvent.TAB_COUNTER_UPDATED, self.__onCollectionTabUpdated, EVENT_BUS_SCOPE.LOBBY)
        self._limitedUIController.stopObserves(_LUI_RULES, self.__isLuiRuleProfileCompleted)
        self.__tabNavigator = None
        super(ProfilePage, self)._dispose()
        return

    def __isLuiRuleProfileCompleted(self, *_):
        self.__updateTabCounters()
        return

    def __dossierUpdateCallBack(self, _):
        self.__tabNavigator.invokeUpdate()
        return

    def __getSectionsData(self, resetSelectedAlias=False):
        isHofEnabled = self.__isHofEnabled
        if self.__tabNavigator and not resetSelectedAlias:
            selectedAlias = self.__tabNavigator.tabId
        else:
            selectedAlias = self.__ctx.get(b'selectedAlias')
        itemCD = None
        if selectedAlias is None or selectedAlias == VIEW_ALIAS.PROFILE_HOF and not isHofEnabled:
            itemCD = self.__ctx.get(b'itemCD')
            selectedAlias = VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE if itemCD else VIEW_ALIAS.PROFILE_TOTAL_PAGE
        if itemCD is None and not (self.__ctx and self.__ctx.get(b'selectedAlias')):
            event = ProfilePageEvent(ProfilePageEvent.SELECT_PROFILE_ALIAS)
            g_eventBus.handleEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)
            selectedAlias = event.ctx.get(b'selectedAlias', selectedAlias)
        tabBarData = [
         (
          PROFILE.SECTION_SUMMARY_TITLE,
          PROFILE.PROFILE_TABS_TOOLTIP_SUMMARY,
          VIEW_ALIAS.PROFILE_TOTAL_PAGE,
          b'ProfileTotalPage_UI',
          True,
          b'statsSummary'),
         (
          PROFILE.SECTION_ADVANCEDACHIEVEMENTS_TITLE,
          PROFILE.PROFILE_TABS_TOOLTIP_ADVANCEDACHIEVEMENTS,
          VIEW_ALIAS.PROFILE_ACHIEVEMENTS_PAGE,
          b'ProfileTotalPage_UI',
          True,
          b'statsAchievements'),
         (
          PROFILE.SECTION_AWARDS_TITLE,
          PROFILE.PROFILE_TABS_TOOLTIP_AWARDS,
          VIEW_ALIAS.PROFILE_AWARDS,
          b'ProfileAwards_UI',
          True,
          b'statsAwards'),
         (
          PROFILE.SECTION_STATISTICS_TITLE,
          PROFILE.PROFILE_TABS_TOOLTIP_STATISTICS,
          VIEW_ALIAS.PROFILE_STATISTICS,
          b'ProfileStatistics_UI',
          True,
          b'statsStatistics'),
         (
          PROFILE.SECTION_TECHNIQUE_TITLE,
          PROFILE.PROFILE_TABS_TOOLTIP_TECHNIQUE,
          VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE,
          b'ProfileTechniquePage_UI',
          True,
          b'statsTechnique')]
        if isHofEnabled:
            tabBarData.append((
             PROFILE.SECTION_HOF_TITLE,
             PROFILE.PROFILE_TABS_TOOLTIP_HOF,
             VIEW_ALIAS.PROFILE_HOF,
             b'ProfileHofPage_UI',
             True,
             b'statsHof'))
        if self.__collectionsSystem.isEnabled():
            tabBarData.append((
             PROFILE.SECTION_COLLECTIONS_TITLE,
             PROFILE.PROFILE_TABS_TOOLTIP_COLLECTIONS,
             VIEW_ALIAS.PROFILE_COLLECTIONS_PAGE,
             b'ProfileCollectionsPage_UI',
             True,
             b'statsCollections'))
        return {b'tabBarData': [{b'label': (makeString(label)), b'tooltip': tooltip, b'alias': alias, b'linkage': linkage, b'enabled': isEnabled, b'id': uiId} for label, tooltip, alias, linkage, isEnabled, uiId in tabBarData], 
           b'selectedAlias': selectedAlias}

    @property
    def __isHofEnabled(self):
        return self.lobbyContext.getServerSettings().isHofEnabled()

    def __onServerSettingChanged(self, diff):
        if b'hallOfFame' in diff:
            if self.__ctx:
                self.__ctx.pop(b'itemCD', None)
            self.__tabNavigator.as_setInitDataS(self.__getSectionsData())
            self.__updateTabCounters()
            if not self.__isHofEnabled:
                showDisabledDialog()
        return

    def __onCollectionsSettingsChanged(self):
        self.__tabNavigator.as_setInitDataS(self.__getSectionsData())
        self.__updateTabCounters()
        return

    def __getTotalUnseenAdvancedAchievementsCount(self):
        return self.__advAchmntCtrl.getTotalUnseenAdvancedAchievementsCount()

    def __updateTabCounters(self):
        counters = []
        if self.__achievements20Controller.getAchievementsTabCounter():
            counters.append({b'componentId': (VIEW_ALIAS.PROFILE_TOTAL_PAGE), b'count': b'1'})
        advancedAchievementsCount = self.__getTotalUnseenAdvancedAchievementsCount()
        if advancedAchievementsCount:
            counters.append({b'componentId': (VIEW_ALIAS.PROFILE_ACHIEVEMENTS_PAGE), b'count': (str(advancedAchievementsCount))})
        if self.__isHofEnabled:
            hofCounter = getHofTabCounter()
            if hofCounter and self._limitedUIController.isRuleCompleted(LUI_RULES.profileHof):
                counters.append({b'componentId': (VIEW_ALIAS.PROFILE_HOF), b'count': (str(hofCounter))})
            if isHofButtonNew(PROFILE_CONSTANTS.HOF_VIEW_RATING_BUTTON) and self._limitedUIController.isRuleCompleted(LUI_RULES.profileTechniquePage):
                counters.append({b'componentId': (VIEW_ALIAS.PROFILE_TECHNIQUE_PAGE), b'count': b'1'})
        if self.__collectionsSystem.isEnabled() and getCollectionsTabCounter(collectionsSystem=self.__collectionsSystem):
            counters.append({b'componentId': (VIEW_ALIAS.PROFILE_COLLECTIONS_PAGE), b'count': b' '})
        self.__tabNavigator.as_setBtnTabCountersS(counters)
        return

    def __loadHofUrl(self, url):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.BROWSER_VIEW), ctx={b'url': url, 
           b'returnAlias': (VIEW_ALIAS.LOBBY_PROFILE), 
           b'allowRightClick': True, 
           b'webHandlers': (createHofWebHandlers()), 
           b'selectedAlias': (VIEW_ALIAS.PROFILE_HOF), 
           b'disabledKeys': (getHofDisabledKeys()), 
           b'onServerSettingsChange': onServerSettingsChange}), EVENT_BUS_SCOPE.LOBBY)
        return

    def __onProfileVisited(self):
        self.__updateTabCounters()
        return

    def __onUnseenAchievementsUpdate(self):
        self.__updateTabCounters()
        return

    def __onCollectionTabUpdated(self, *_):
        self.__updateTabCounters()
        return
