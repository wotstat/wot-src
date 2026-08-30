from gui.prb_control.entities.base.listener import IPrbListener

class IUnitIntroListener(IPrbListener):

    def onUnitAutoSearchStarted(self, timeLeft):
        return

    def onUnitAutoSearchFinished(self):
        return

    def onUnitAutoSearchSuccess(self, acceptDelta):
        return

    def onUnitBrowserErrorReceived(self, errorCode):
        return


class IUnitListener(IUnitIntroListener):

    def onUnitFlagsChanged(self, flags, timeLeft):
        return

    def onUnitPlayerStateChanged(self, pInfo):
        return

    def onUnitPlayerRolesChanged(self, pInfo, pPermissions):
        return

    def onUnitPlayerOnlineStatusChanged(self, pInfo):
        return

    def onUnitPlayerBecomeCreator(self, pInfo):
        return

    def onUnitPlayerNoLongerCreator(self, pInfo):
        return

    def onUnitPlayerEnterOrLeaveArena(self, pInfo):
        return

    def onUnitRosterChanged(self):
        return

    def onUnitMembersListChanged(self):
        return

    def onUnitPlayerAdded(self, pInfo):
        return

    def onUnitPlayerInfoChanged(self, pInfo):
        return

    def onUnitPlayerRemoved(self, pInfo):
        return

    def onUnitPlayersListChanged(self):
        return

    def onUnitVehiclesChanged(self, dbID, vInfos):
        return

    def onUnitPlayerVehDictChanged(self, pInfo):
        return

    def onUnitSettingChanged(self, opCode, value):
        return

    def onUnitRejoin(self):
        return

    def onUnitErrorReceived(self, errorCode):
        return

    def onUnitExtraChanged(self, extra):
        return

    def onUnitCurfewChanged(self):
        return

    def onUnitPlayerProfileVehicleChanged(self, accountDBID):
        return

    def onUnitSearchFlagsChanged(self, flags):
        return


class IStrongholdListener(IPrbListener):

    def onUpdateHeader(self, header, isFirstBattle, isUnitFreezed):
        return

    def onUpdateTimer(self, timer):
        return

    def onUpdateState(self, state):
        return

    def onUpdateReserve(self, reserve, reserveOrder):
        return

    def onStrongholdDataChanged(self, header, isFirstBattle, reserve, reserveOrder):
        return

    def onStrongholdOnReadyStateChanged(self):
        return

    def onStrongholdMaintenance(self, state):
        return

    def onCommanderIsReady(self, isReady):
        return

    def onStrongholdDoBattleQueue(self, isFirstBattle, readyButtonEnabled, reserveOrder):
        return

    def onPlayersMatching(self, state):
        return

    def onSlotVehileFiltersChanged(self):
        return

    def onEventFrozenVehiclesChanged(self, data):
        return
