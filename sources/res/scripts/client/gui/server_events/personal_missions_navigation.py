from operator import methodcaller
import WWISE
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.server_events.pm_constants import SOUNDS, IS_PM2_QUEST_ENABLED, DISABLED_PM_OPERATIONS, IS_REGULAR_QUEST_ENABLED
from helpers import dependency
from personal_missions import PM_BRANCH
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.server_events import IEventsCache

class _PMNavigationInfo(object):
    _DEFAULT_OPERATIONS = {(PM_BRANCH.REGULAR): 1, (PM_BRANCH.PERSONAL_MISSION_2): 5}

    def __init__(self):
        self.__operationIDs = self._DEFAULT_OPERATIONS.copy()
        self.__chainIDs = {q: 1 for q in PM_BRANCH.V1_BRANCHES}
        self.__branch = PM_BRANCH.REGULAR
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
        if DISABLED_PM_OPERATIONS in diff and diff[DISABLED_PM_OPERATIONS]:
            disabledOp = self.getOperationID() in diff[DISABLED_PM_OPERATIONS].keys()
        if IS_REGULAR_QUEST_ENABLED in diff and not diff[IS_REGULAR_QUEST_ENABLED] or IS_PM2_QUEST_ENABLED in diff and not diff[IS_PM2_QUEST_ENABLED] or disabledOp:
            from gui.shared.event_dispatcher import showHangar
            showHangar()
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
