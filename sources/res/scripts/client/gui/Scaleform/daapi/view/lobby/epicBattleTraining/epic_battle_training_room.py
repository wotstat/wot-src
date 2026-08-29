from adisp import adisp_process
from gui import SystemMessages
from gui.Scaleform.daapi.view.lobby.trainings import formatters
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.settings import ICONS_SIZES
from gui.prb_control.items.prb_items import getPlayersComparator
from gui.prb_control.settings import PREBATTLE_ROSTER, REQUEST_TYPE
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles
from gui.Scaleform.daapi.view.meta.EpicBattleTrainingRoomMeta import EpicBattleTrainingRoomMeta
from gui.prb_control.entities.base.legacy.ctx import GroupAssignLegacyCtx, GroupSwapInTeamLegacyCtx, GroupSwapBetweenTeamLegacyCtx
from debug_utils import LOG_DEBUG
from constants import PREBATTLE_TYPE
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.prb_control.entities.epic_battle_training.ctx import EpicTrainingSettingsCtx
from gui.Scaleform.genConsts.PREBATTLE_ALIASES import PREBATTLE_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from helpers import int2roman

class EpicBattleTrainingRoom(EpicBattleTrainingRoomMeta):

    def __init__(self, _=None):
        super(EpicBattleTrainingRoom, self).__init__()
        self._firstTime = True
        return

    def showTrainingSettings(self):
        settings = EpicTrainingSettingsCtx()
        self.fireEvent(events.LoadViewEvent(SFViewLoadParams(PREBATTLE_ALIASES.EPIC_TRAINING_SETTINGS_WINDOW_PY), ctx={b'isCreateRequest': False, b'settings': settings}), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def onRostersChanged(self, entity, rosters, full):
        if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1 in rosters:
            self.as_setTeam1S(self.__makeAccountsDataForLane(rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1], 1, R.strings.epic_battle.epictraining.info.team1LaneLabel()))
        if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1 in rosters:
            self.as_setTeam1S(self.__makeAccountsDataForLane(rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1], 2, R.strings.epic_battle.epictraining.info.team1LaneLabel()))
        if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1 in rosters:
            self.as_setTeam1S(self.__makeAccountsDataForLane(rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1], 3, R.strings.epic_battle.epictraining.info.team1LaneLabel()))
        if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2 in rosters:
            self.as_setTeam2S(self.__makeAccountsDataForLane(rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2], 1, R.strings.epic_battle.epictraining.info.team2LaneLabel()))
        if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2 in rosters:
            self.as_setTeam2S(self.__makeAccountsDataForLane(rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2], 2, R.strings.epic_battle.epictraining.info.team2LaneLabel()))
        if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2 in rosters:
            self.as_setTeam2S(self.__makeAccountsDataForLane(rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2], 3, R.strings.epic_battle.epictraining.info.team2LaneLabel()))
        if PREBATTLE_ROSTER.UNASSIGNED in rosters:
            self.as_setOtherS(self._makeAccountsData(rosters[PREBATTLE_ROSTER.UNASSIGNED], R.strings.epic_battle.epictraining.info.otherLabel()))
        super(EpicBattleTrainingRoom, self).onRostersChanged(entity, rosters, full)
        return

    @adisp_process
    def onSwapTeamLane(self, fromTeam, fromLane, toTeam, toLane):
        if fromTeam == toTeam:
            result = yield self.prbDispatcher.sendPrbRequest(GroupSwapInTeamLegacyCtx(fromTeam, fromLane, toLane, waitingID=b'prebattle/swap'))
        else:
            result = yield self.prbDispatcher.sendPrbRequest(GroupSwapBetweenTeamLegacyCtx(fromLane, waitingID=b'prebattle/swap'))
        if not result:
            SystemMessages.pushMessage(backport.text(R.strings.system_messages.training.error.swapTeams()), type=SystemMessages.SM_TYPE.Error)
        return

    @adisp_process
    def onChangeTeamLane(self, accID, team, lane):
        selectedLane = int(lane)
        roster = int(team)
        if not roster:
            roster = self.prbEntity.getRosterKey(accID)
            if not roster & PREBATTLE_ROSTER.UNASSIGNED:
                roster |= PREBATTLE_ROSTER.UNASSIGNED
        LOG_DEBUG(b'accID ' + str(accID) + b' lane selected ' + str(selectedLane) + b' team selected ' + str(team))
        result = yield self.prbDispatcher.sendPrbRequest(GroupAssignLegacyCtx(accID, roster, selectedLane, waitingID=b'prebattle/assign'))
        if not result:
            self._showActionErrorMessage()
        return

    def _populate(self):
        if self.prbDispatcher:
            funcState = self.prbDispatcher.getFunctionalState()
            if not funcState.isInLegacy(PREBATTLE_TYPE.EPIC_TRAINING):
                g_eventDispatcher.removeEpicTrainingFromCarousel(False)
                return
        super(EpicBattleTrainingRoom, self)._populate()
        return

    def _addListeners(self):
        super(EpicBattleTrainingRoom, self)._addListeners()
        self.addListener(events.TrainingSettingsEvent.UPDATE_EPIC_TRAINING_SETTINGS, self._updateTrainingRoom, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _removeListeners(self):
        super(EpicBattleTrainingRoom, self)._removeListeners()
        self.removeListener(events.TrainingSettingsEvent.UPDATE_EPIC_TRAINING_SETTINGS, self._updateTrainingRoom, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def _handleSetPrebattleCoolDown(self, event):
        super(EpicBattleTrainingRoom, self)._handleSetPrebattleCoolDown(event)
        if event.requestID in [REQUEST_TYPE.EPIC_SWAP_IN_TEAM, REQUEST_TYPE.EPIC_SWAP_BETWEEN_TEAM]:
            self.as_startCoolDownSwapButtonS(event.coolDown)
        return

    def _closeWindows(self):
        self._closeWindow(PREBATTLE_ALIASES.EPIC_TRAINING_SETTINGS_WINDOW_PY)
        self._closeWindow(PREBATTLE_ALIASES.SEND_INVITES_WINDOW_PY)
        return

    def _showRosters(self, entity, rosters):
        if self._firstTime:
            self.as_setTeam1S(self.__makeAccountsDataForLane([], 1, R.strings.epic_battle.epictraining.info.team1LaneLabel()))
            self.as_setTeam2S(self.__makeAccountsDataForLane([], 1, R.strings.epic_battle.epictraining.info.team2LaneLabel()))
            self.as_setOtherS(self._makeAccountsData([], R.strings.epic_battle.epictraining.info.otherLabel()))
            self._firstTime = False
        accounts = rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1]
        if accounts:
            if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1 in rosters:
                self.as_setTeam1S(self.__makeAccountsDataForLane(accounts, 1, R.strings.epic_battle.epictraining.info.team1LaneLabel()))
            if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1 in rosters:
                self.as_setTeam1S(self.__makeAccountsDataForLane(accounts, 2, R.strings.epic_battle.epictraining.info.team1LaneLabel()))
            if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM1 in rosters:
                self.as_setTeam1S(self.__makeAccountsDataForLane(accounts, 3, R.strings.epic_battle.epictraining.info.team1LaneLabel()))
        accounts = rosters[PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2]
        if accounts:
            if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2 in rosters:
                self.as_setTeam2S(self.__makeAccountsDataForLane(accounts, 1, R.strings.epic_battle.epictraining.info.team2LaneLabel()))
            if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2 in rosters:
                self.as_setTeam2S(self.__makeAccountsDataForLane(accounts, 2, R.strings.epic_battle.epictraining.info.team2LaneLabel()))
            if PREBATTLE_ROSTER.ASSIGNED_IN_TEAM2 in rosters:
                self.as_setTeam2S(self.__makeAccountsDataForLane(accounts, 3, R.strings.epic_battle.epictraining.info.team2LaneLabel()))
        accounts = rosters[PREBATTLE_ROSTER.UNASSIGNED]
        if accounts:
            self.as_setOtherS(self._makeAccountsData(accounts))
        super(EpicBattleTrainingRoom, self)._showRosters(entity, rosters)
        return

    def _isObserverModeEnabled(self):
        return False

    def _updateTrainingRoom(self, event):
        self._closeWindow(PREBATTLE_ALIASES.EPIC_TRAINING_SETTINGS_WINDOW_PY)
        super(EpicBattleTrainingRoom, self)._updateTrainingRoom(event)
        return

    def __makeAccountsDataForLane(self, accounts, lane, rLabel=None):
        listData = []
        isPlayerSpeaking = self.app.voiceChatManager.isPlayerSpeaking
        accounts = sorted(accounts, cmp=getPlayersComparator())
        getUser = self.usersStorage.getUser
        lanecounter = [
         0, 0, 0]
        for account in accounts:
            lanecounter[account.group - 1] += 1
            if lane >= 0 and lane == account.group:
                vContourIcon = b''
                vShortName = b''
                vLevel = b''
                dbID = account.dbID
                user = getUser(dbID)
                if account.isVehicleSpecified():
                    vehicle = account.getVehicle()
                    vContourIcon = vehicle.iconContour
                    vShortName = vehicle.shortUserName
                    vLevel = int2roman(vehicle.level)
                badge = account.getBadge()
                badgeVO = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': False}) if badge else {}
                listData.append({b'accID': (account.accID), 
                   b'dbID': (account.dbID), 
                   b'userName': (account.name), 
                   b'fullName': (account.getFullName()), 
                   b'stateString': (formatters.getPlayerStateString(account.state)), 
                   b'icon': vContourIcon, 
                   b'vShortName': vShortName, 
                   b'vLevel': vLevel, 
                   b'tags': (list(user.getTags()) if user else []), 
                   b'isPlayerSpeaking': (bool(isPlayerSpeaking(account.dbID))), 
                   b'clanAbbrev': (account.clanAbbrev), 
                   b'region': (self.lobbyContext.getRegionCode(account.dbID)), 
                   b'igrType': (account.igrType), 
                   b'badgeVisualVO': badgeVO})

        label = b''
        if rLabel is not None:
            label = text_styles.neutral(backport.text(rLabel, lane1=str(lanecounter[0]), lane2=str(lanecounter[1]), lane3=str(lanecounter[2])))
        result = {b'listData': listData, 
           b'teamLabel': label, 
           b'lane': lane}
        return result
