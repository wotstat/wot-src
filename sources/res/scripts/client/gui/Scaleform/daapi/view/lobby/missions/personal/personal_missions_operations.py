import operator
from account_helpers import AccountSettings
from account_helpers.AccountSettings import PersonalMissions
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.missions import missions_helper
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import checkOldCampaignsIntroSeen
from gui.Scaleform.daapi.view.meta.PMOldOperationsMeta import PMOldOperationsMeta
from gui.Scaleform.daapi.view.meta.PersonalMissionOperationsMeta import PersonalMissionOperationsMeta
from gui.Scaleform.framework import g_entitiesFactories
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.framework.managers.optimization_manager import ExternalFullscreenGraphicsOptimizationComponent
from gui.Scaleform.genConsts.PERSONAL_MISSIONS_ALIASES import PERSONAL_MISSIONS_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.PERSONAL_MISSIONS import PERSONAL_MISSIONS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl.lobby.personal_missions.personal_missions_operations_view import PersonalMissionsOperationsView
from gui.impl.lobby.personal_missions.personal_missions_window_events import showIntroVideoView, showIntroView
from gui.server_events.personal_missions_navigation import PersonalMissionsNavigation
from gui.server_events.pm_constants import PERSONAL_MISSIONS_SOUND_SPACE
from gui.server_events.pm3_constants import PERSONAL_MISSIONS_3_SOUND_SPACE, SOUNDS
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from helpers import dependency
from personal_missions import PM_BRANCH
from skeletons.gui.server_events import IEventsCache
from gui.sounds.voice_over_phrase_player import VoiceOverHandler

class PersonalMissionOperations(LobbySubView, PersonalMissionOperationsMeta, PersonalMissionsNavigation):
    _COMMON_SOUND_SPACE = PERSONAL_MISSIONS_3_SOUND_SPACE
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, ctx):
        super(PersonalMissionOperations, self).__init__(ctx)
        self.__graphicOptimization = ExternalFullscreenGraphicsOptimizationComponent()
        self.__voiceHandler = VoiceOverHandler()
        ctx = ctx or {}
        branch = ctx.get(b'branch')
        if branch:
            self.setBranch(branch)
        operationID = ctx.get(b'operationID')
        if operationID:
            self.setOperationID(operationID)
        return

    def closeView(self):
        event = g_entitiesFactories.makeLoadEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_HANGAR))
        self.fireEvent(event, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def onTabSelected(self, tabIdx):
        branch = self.__getBranchByTabIndex(tabIdx)
        self.setBranch(branch)
        self._handleCampaignTab(branch)
        return

    def _handleCampaignTab(self, branch):
        if branch == PM_BRANCH.PERSONAL_MISSION_3:
            if self.__isIntroSeenShown():
                self.soundManager.setState(SOUNDS.STATE_SCREEN_GROUP, SOUNDS.STATE_PLACE_SPLIT_SCREEN)
                self.__voiceHandler.createPlayer()
                self._switchCommonSoundSpace(PERSONAL_MISSIONS_3_SOUND_SPACE)
        else:
            self.__voiceHandler.destroyPlayer()
            self._switchCommonSoundSpace(PERSONAL_MISSIONS_SOUND_SPACE)
            checkOldCampaignsIntroSeen()
        return

    def __isIntroSeenShown(self):
        isNotShown = not AccountSettings.getPersonalMissions(PersonalMissions.INTRO_SEEN)
        if isNotShown:
            showIntroView()
            showIntroVideoView()
            return False
        return True

    def _populate(self):
        super(PersonalMissionOperations, self)._populate()
        self.__graphicOptimization.init()
        tabIdx = self.__getTabIndexByBranch()
        self.as_setSelectedTabS(tabIdx)
        self.eventsCache.onPersonalQuestsVisited()
        return

    def _dispose(self):
        self.__voiceHandler.destroyPlayer()
        self.__graphicOptimization.fini()
        super(PersonalMissionOperations, self)._dispose()
        return

    def __getTabIndexByBranch(self):
        if self.getBranch() < PM_BRANCH.PERSONAL_MISSION_3:
            return 1
        return 0

    def __getBranchByTabIndex(self, tabIdx):
        if tabIdx > 0:
            return PM_BRANCH.REGULAR
        return PM_BRANCH.PERSONAL_MISSION_3


class PMOldOperations(PMOldOperationsMeta, PersonalMissionsNavigation):
    eventsCache = dependency.descriptor(IEventsCache)

    def _populate(self):
        super(PMOldOperations, self)._populate()
        self.eventsCache.onSyncCompleted += self.__onQuestsUpdated
        self.eventsCache.onProgressUpdated += self.__onQuestsUpdated
        self.__setTitle()
        self.__update()
        return

    def _dispose(self):
        self.eventsCache.onSyncCompleted -= self.__onQuestsUpdated
        self.eventsCache.onProgressUpdated -= self.__onQuestsUpdated
        super(PMOldOperations, self)._dispose()
        return

    def showInfo(self):
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSION_FIRST_ENTRY_VIEW_ALIAS)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def onOperationClick(self, branch, operationID):
        self.setBranch(branch)
        self.setOperationID(operationID)
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(PERSONAL_MISSIONS_ALIASES.PERSONAL_MISSIONS_PAGE_ALIAS), ctx={b'branch': branch, 
           b'operationID': operationID}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __update(self):
        operations = []
        timeIconAlreadySet = False
        for branch in PM_BRANCH.OLD_BRANCHES:
            for oID, o in sorted(self.eventsCache.getPersonalMissions().getOperationsForBranch(branch).iteritems(), key=operator.itemgetter(0)):
                state = PERSONAL_MISSIONS_ALIASES.OPERATION_LOCKED_STATE
                tooltipAlias = TOOLTIPS_CONSTANTS.OPERATION
                postponedTime = b''
                enabled = True
                if o.isDisabled():
                    state, postponedTime = missions_helper.getPostponedOperationState(oID)
                    if postponedTime:
                        tooltipAlias = TOOLTIPS_CONSTANTS.OPERATION_POSTPONED
                    enabled = False
                elif o.isFullCompleted():
                    state = PERSONAL_MISSIONS_ALIASES.OPERATION_COMPLETE_FULL_STATE
                elif o.isAwardAchieved():
                    state = PERSONAL_MISSIONS_ALIASES.OPERATION_COMPLETE_STATE
                elif o.isInProgress():
                    state = PERSONAL_MISSIONS_ALIASES.OPERATION_CURRENT_STATE
                elif o.isUnlocked():
                    state = PERSONAL_MISSIONS_ALIASES.OPERATION_UNLOCKED_STATE
                operationVO = {b'id': oID, 
                   b'pmType': branch, 
                   b'state': state, 
                   b'icon': (RES_ICONS.getPersonalMissionOperation(str(oID), self.__formatImageState(state))), 
                   b'postponedTime': (postponedTime if not timeIconAlreadySet else b''), 
                   b'enabled': enabled, 
                   b'tooltipAlias': tooltipAlias}
                if postponedTime:
                    timeIconAlreadySet = True
                operations.append(operationVO)

        self.as_setOperationsS(operations)
        self.enableNavigationSoundEffect()
        return

    def __onQuestsUpdated(self, *args):
        self.__update()
        return

    def __setTitle(self):
        titleVO = {b'title': (PERSONAL_MISSIONS.OPERATIONINFO_TITLE), 
           b'tooltip': {b'tooltip': b'', 
                        b'specialArgs': [], b'specialAlias': None, 
                        b'isSpecial': False}}
        self.as_setTitleS(titleVO)
        return

    def __formatImageState(self, state):
        if state == PERSONAL_MISSIONS_ALIASES.OPERATION_DISABLED_STATE:
            return PERSONAL_MISSIONS_ALIASES.OPERATION_LOCKED_STATE
        if state == PERSONAL_MISSIONS_ALIASES.OPERATION_COMPLETE_FULL_STATE:
            return PERSONAL_MISSIONS_ALIASES.OPERATION_COMPLETE_STATE
        return state

    def _onSettingsChanged(self, diff):
        if b'isRegularQuestEnabled' in diff and not diff[b'isRegularQuestEnabled'] or b'isPM2QuestEnabled' in diff and not diff[b'isPM2QuestEnabled'] or b'disabledPMOperations' in diff and diff[b'disabledPMOperations'] or b'disabledPersonalMissions' in diff and diff[b'disabledPersonalMissions']:
            self.__update()
        return


class PM3Operations(InjectComponentAdaptor):

    def onSectionActivated(self):
        if self.__view is not None:
            self.__view.activate()
        return

    def onSectionDeactivated(self):
        if self.__view is not None:
            self.__view.deactivate()
        return

    def _makeInjectView(self, *args):
        self.__view = PersonalMissionsOperationsView()
        return self.__view
