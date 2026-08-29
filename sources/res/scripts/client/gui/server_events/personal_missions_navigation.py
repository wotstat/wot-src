from operator import methodcaller
import WWISE
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.server_events.pm_constants import SOUNDS
from gui.shared import EVENT_BUS_SCOPE, events
from helpers import dependency
from personal_missions import PM_BRANCH
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache

class _PMNavigationInfo(object):
    _DEFAULT_OPERATIONS = {(PM_BRANCH.REGULAR): 1, (PM_BRANCH.PERSONAL_MISSION_2): 5, (PM_BRANCH.PERSONAL_MISSION_3): 8}

    def __init__(self):
        self.__operationIDs = self._DEFAULT_OPERATIONS.copy()
        self.__chainIDs = {q: 1 for q in PM_BRANCH.ACTIVE_BRANCHES}
        self.__branch = PM_BRANCH.PERSONAL_MISSION_3
        return

    def getOperationID(self, branchID=None):
        return self.__operationIDs[branchID or self.__branch]

    def setOperationID(self, operationID, branchID=None):
        self.__operationIDs[branchID or self.__branch] = operationID
        return

    def getChainID(self, branchID=None):
        return self.__chainIDs[branchID or self.__branch]

    def setChainID(self, chainID, branchID=None):
        self.__chainIDs[branchID or self.__branch] = chainID
        return

    def setBranchID(self, branchID):
        self.__branch = branchID
        return

    def getBranchID(self):
        return self.__branch


class PersonalMissionsNavigation(EventSystemEntity):
    __navigationInfo = _PMNavigationInfo()
    _eventsCache = dependency.descriptor(IEventsCache)
    _lobbyCtx = dependency.descriptor(ILobbyContext)

    def __init__(self, *args, **kwargs):
        super(PersonalMissionsNavigation, self).__init__()
        return

    def getOperationID(self):
        return self.__navigationInfo.getOperationID()

    def getOperation(self):
        return self._eventsCache.getPersonalMissions().getAllOperations().get(self.getOperationID())

    def setOperationID(self, operationID):
        self.__navigationInfo.setOperationID(operationID)
        self.__setWWISEGlobal()
        return

    def getChainID(self):
        return self.__navigationInfo.getChainID()

    def getChain(self):
        return self.getOperation().getQuests()[self.getChainID()]

    def setChainID(self, chainID):
        self.__navigationInfo.setChainID(chainID)
        return

    def setBranch(self, branch):
        self.__navigationInfo.setBranchID(branch)
        return

    def getBranch(self):
        return self.__navigationInfo.getBranchID()

    def _populate(self):
        super(PersonalMissionsNavigation, self)._populate()
        self.__setWWISEGlobal()
        self._lobbyCtx.getServerSettings().onServerSettingsChange += self._onSettingsChanged
        self._eventsCache.onProgressUpdated += self.__onProgressUpdated
        return

    def _dispose(self):
        self._eventsCache.onProgressUpdated -= self.__onProgressUpdated
        self._lobbyCtx.getServerSettings().onServerSettingsChange -= self._onSettingsChanged
        super(PersonalMissionsNavigation, self)._dispose()
        return

    def _onSettingsChanged(self, diff):
        disabledOp = False
        if b'disabledPMOperations' in diff and diff[b'disabledPMOperations']:
            disabledOp = self.getOperationID() in diff[b'disabledPMOperations'].keys()
        if b'isRegularQuestEnabled' in diff and not diff[b'isRegularQuestEnabled'] or b'isPM2QuestEnabled' in diff and not diff[b'isPM2QuestEnabled'] or disabledOp:
            self.fireEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_HANGAR)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __setWWISEGlobal(self):
        operation = self.getOperation()
        if operation:
            completedCount = len(operation.getQuestsInChainByFilter(self.getChainID(), methodcaller(b'isCompleted')))
        else:
            completedCount = 0
        WWISE.WW_setRTCPGlobal(SOUNDS.RTCP_MISSIONS_NUMBER, completedCount)
        return

    def __onProgressUpdated(self, _):
        self.__setWWISEGlobal()
        return

    def enableNavigationSoundEffect(self):
        for branch in SOUNDS.RTCP_MISSION_BRANCH.values():
            WWISE.WW_setRTCPGlobal(branch, SOUNDS.BRANCH_DEFAULT)

        WWISE.WW_setRTCPGlobal(SOUNDS.RTCP_MISSIONS_ZOOM, SOUNDS.MAX_MISSIONS_ZOOM)
        WWISE.WW_setRTCPGlobal(SOUNDS.RTCP_DEBRIS_CONTROL, SOUNDS.MAX_MISSIONS_ZOOM)
        return
