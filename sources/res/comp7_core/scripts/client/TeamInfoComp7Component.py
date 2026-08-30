import typing
from script_component.DynamicScriptComponent import DynamicScriptComponent
import VOIP
from comp7_core.gui.battle_control.arena_info.arena_vos import Comp7CoreKeys
from comp7_core.gui.comp7_core_constants import BATTLE_CTRL_ID
from constants import REQUEST_COOLDOWN
from gui.battle_control import avatar_getter
from helpers import dependency
from helpers.CallbackDelayer import CallbackDelayer
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from VOIP.VOIPManager import VOIPManager

class TeamInfoComp7Component(DynamicScriptComponent):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(TeamInfoComp7Component, self).__init__()
        self.__callbackDelayer = CallbackDelayer()
        return

    def onEnterWorld(self, *args):
        super(TeamInfoComp7Component, self).onEnterWorld(*args)
        voipManager = VOIP.getVOIPManager()
        voipManager.onJoinedChannel += self.__onJoinedVoipChannel
        voipManager.onLeftChannel += self.__onLeftVoipChannel
        self.__updateVoipConnection()
        return

    def onLeaveWorld(self):
        voipManager = VOIP.getVOIPManager()
        voipManager.onJoinedChannel -= self.__onJoinedVoipChannel
        voipManager.onLeftChannel -= self.__onLeftVoipChannel
        self.__callbackDelayer.clearCallbacks()
        super(TeamInfoComp7Component, self).onLeaveWorld()
        return

    def set_roleSkillLevels(self, prev):
        if self._isAvatarReady:
            self.__invalidateRoleSkillLevels()
        return

    def set_teamVivoxChannel(self, prev):
        if self._isAvatarReady:
            self.__invalidateTeamVivoxChannel()
        return

    def set_endPrepickTime(self, _):
        if self._isAvatarReady:
            self.__updateVehiclePrepickEndTime()
        return

    def set_endVotingTime(self, _):
        if self._isAvatarReady:
            self.__updateVehicleBanEndTime()
        return

    def set_banVotingStates(self, _):
        if self._isAvatarReady:
            self.__updatePlayersChoiceForBan()
        return

    def set_candidatesForBan(self, _):
        if self._isAvatarReady:
            self.__updateCandidatesForBan()
        return

    def _onAvatarReady(self):
        voipManager = VOIP.getVOIPManager()
        voipManager.onJoinedChannel += self.__onJoinedVoipChannel
        voipManager.onLeftChannel += self.__onLeftVoipChannel
        self.__updateVoipConnection()
        self.__invalidateRoleSkillLevels()
        self.__invalidateTeamVivoxChannel()
        self.__updateVehiclePrepickEndTime()
        self.__updateVehicleBanEndTime()
        self.__updatePlayersChoiceForBan()
        self.__updateCandidatesForBan()
        return

    def __onJoinedVoipChannel(self, *_, **__):
        self.__updateVivoxPresence()
        return

    def __onLeftVoipChannel(self, *_, **__):
        self.__updateVivoxPresence()
        return

    def __invalidateRoleSkillLevels(self):
        arena = avatar_getter.getArena()
        if not arena:
            return
        gameModeStats = {vID: {(Comp7CoreKeys.ROLE_SKILL_LEVEL): level} for vID, level in self.roleSkillLevels.iteritems()}
        arena.updateGameModeSpecificStats(isStatic=True, stats=gameModeStats)
        return

    def __invalidateTeamVivoxChannel(self):
        arena = avatar_getter.getArena()
        if not arena:
            return
        gameModeStats = {vID: {(Comp7CoreKeys.VOIP_CONNECTED): (bool(connected))} for vID, connected in self.teamVivoxChannel.iteritems()}
        arena.updateGameModeSpecificStats(isStatic=True, stats=gameModeStats)
        return

    def __updateVoipConnection(self):
        voipManager = VOIP.getVOIPManager()
        isJoined = voipManager.isCurrentChannelEnabled()
        wasJoined = self.teamVivoxChannel.get(avatar_getter.getPlayerVehicleID(), False)
        if wasJoined and not isJoined:
            self.__updateVivoxPresence()
            voipManager.enableCurrentChannel(isEnabled=True)
        return

    def __updateVivoxPresence(self):
        isVoipEnabled = VOIP.getVOIPManager().isCurrentChannelEnabled()
        if self.teamVivoxChannel.get(avatar_getter.getPlayerVehicleID(), False) != isVoipEnabled:
            self.cell.setVivoxPresence(isVoipEnabled)
            self.__callbackDelayer.delayCallback(REQUEST_COOLDOWN.SET_VIVOX_PRESENCE + 1.0, self.__updateVivoxPresence)
        return

    def __updateVehiclePrepickEndTime(self):
        vehicleBanCtrl = self.__getVehicleBanCtrl()
        if vehicleBanCtrl is not None:
            vehicleBanCtrl.vehiclePrepickEndTime = self.endPrepickTime
        return

    def __updateVehicleBanEndTime(self):
        vehicleBanCtrl = self.__getVehicleBanCtrl()
        if vehicleBanCtrl is not None:
            vehicleBanCtrl.vehicleBanEndTime = self.endVotingTime
        return

    def __updatePlayersChoiceForBan(self):
        vehicleBanCtrl = self.__getVehicleBanCtrl()
        if vehicleBanCtrl is not None:
            vehicleBanCtrl.updatePlayersChoiceForBan(self.banVotingStates)
        return

    def __updateCandidatesForBan(self):
        vehicleBanCtrl = self.__getVehicleBanCtrl()
        if vehicleBanCtrl is not None and self.candidatesForBan:
            vehicleBanCtrl.candidatesForBan = self.candidatesForBan
        return

    def __getVehicleBanCtrl(self):
        return self.__sessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.COMP7_VEHICLE_BAN_CTRL)
