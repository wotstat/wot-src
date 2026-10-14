from __future__ import absolute_import
import BigWorld
from PlayerEvents import g_playerEvents
from helpers.CallbackDelayer import CallbackDelayer
from gui.Scaleform.settings import ICONS_SIZES
from gui.shared.badges import buildBadge
from gui.battle_control import avatar_getter
from halloween.gui.battle_control.controllers.battle_gui_controller import EventBattleGoal
from halloween.gui.scaleform.daapi.view.meta.HWPlayersPanelMeta import HWPlayersPanelMeta
from HWTeamInfoStatsComponent import HWTeamInfoStatsComponent
from HWArenaPhasesComponent import HWArenaPhasesComponent
BattleGoalMapping = {(EventBattleGoal.UNKNOWN): 0, 
   (EventBattleGoal.COLLECT_SOULS): 1, 
   (EventBattleGoal.GET_TO_COLLECTOR): 2}

class HWPlayersPanel(HWPlayersPanelMeta):
    _UPDATE_PERIOD = 0.2

    def __init__(self):
        super(HWPlayersPanel, self).__init__()
        self._callbackDelayer = CallbackDelayer()
        self.__isPostmortem = False
        self.__vehsCache = {}
        return

    @property
    def arenaPhases(self):
        return HWArenaPhasesComponent.getInstance()

    @property
    def teamInfoStats(self):
        return HWTeamInfoStatsComponent.getInstance()

    def _populate(self):
        super(HWPlayersPanel, self)._populate()
        if self.teamInfoStats:
            self.teamInfoStats.onTeamHealthUpdated += self.__updateTeamPanel
            self.teamInfoStats.onTeamBuffsUpdated += self.__teamBuffsUpdated
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched += self.__onPostMortemSwitched
            ctrl.onRespawnBaseMoving += self.__onRespawnBaseMoving
        g_playerEvents.onAvatarReady += self.__onAvatarReady
        return

    def _dispose(self):
        if self.teamInfoStats:
            self.teamInfoStats.onTeamHealthUpdated -= self.__updateTeamPanel
            self.teamInfoStats.onTeamBuffsUpdated -= self.__teamBuffsUpdated
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is not None:
            ctrl.onPostMortemSwitched -= self.__onPostMortemSwitched
            ctrl.onRespawnBaseMoving -= self.__onRespawnBaseMoving
        g_playerEvents.onAvatarReady -= self.__onAvatarReady
        self._callbackDelayer.destroy()
        self.__vehsCache.clear()
        super(HWPlayersPanel, self)._dispose()
        return

    def _handleShowExtendedInfo(self, event):
        return

    def __onAvatarReady(self):
        self.__updateAllTeamates()
        return

    def __updateAllTeamates(self):
        arenaDP = self.guiSessionProvider.getArenaDP()
        vInfos = arenaDP.getVehiclesInfoIterator()
        teammateInfos = (v for v in vInfos if v.player.accountDBID > 0 and arenaDP.isAlly(v.vehicleID))
        teamhealth = self.teamInfoStats.getTeamHealth()
        for vInfo in teammateInfos:
            health = next((info[b'value'] for info in teamhealth if info[b'id'] == vInfo.vehicleID), vInfo.vehicleType.maxHealth)
            self.__updateTeammate(vInfo, health)
            self.__vehsCache.update({(vInfo.vehicleID): health})

        return

    def __updateTeamPanel(self):
        self._callbackDelayer.delayCallback(self._UPDATE_PERIOD, self.__updateTeamPanelImpl)
        return

    def __teamBuffsUpdated(self):
        self._callbackDelayer.delayCallback(self._UPDATE_PERIOD, self.__updateTeamPanelImpl, True)
        return

    def __updateTeamPanelImpl(self, forceUpdate=False):
        arenaDP = self.guiSessionProvider.getArenaDP()
        teamhealth = self.teamInfoStats.getTeamHealth()
        for info in teamhealth:
            vInfo = arenaDP.getVehicleInfo(info[b'id'])
            self.__setVehicleHealth(vInfo, info[b'value'], forceUpdate)

        return

    def __setVehicleHealth(self, vInfo, health, forceUpdate):
        prevHealth = self.__vehsCache.get(vInfo.vehicleID)
        if not forceUpdate and prevHealth is not None and prevHealth == health:
            return
        else:
            self.__vehsCache.update({(vInfo.vehicleID): health})
            if not vInfo.isObserver():
                self.as_setPlayerPanelHpS(vInfo.vehicleID, self.__getVehicleMaxHealth(vInfo), health)
            if health <= 0:
                self.as_setPlayerDeadS(vInfo.vehicleID)
            return

    def __getVehicleMaxHealth(self, vInfo):
        vehicle = BigWorld.entities.get(vInfo.vehicleID)
        if vehicle is not None:
            return vehicle.maxHealth
        else:
            return vInfo.vehicleType.maxHealth

    def __updateTeammate(self, vInfo, hpCurrent):
        arenaDP = self.guiSessionProvider.getArenaDP()
        playerVehicleID = avatar_getter.getPlayerVehicleID()
        isSelf = vInfo.vehicleID == playerVehicleID
        playerSquad = arenaDP.getVehicleInfo(playerVehicleID).squadIndex
        isSquad = False
        if playerSquad > 0 and playerSquad == vInfo.squadIndex or playerSquad == 0 and vInfo.vehicleID == playerVehicleID:
            isSquad = True
        badgeID = vInfo.selectedBadge
        badge = buildBadge(badgeID, vInfo.getBadgeExtraInfo())
        badgeVO = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': True}, shortIconName=True) if badge else None
        suffixBadgeId = vInfo.selectedSuffixBadge
        playerName = vInfo.player.name
        if vInfo.player.clanAbbrev:
            playerName = (b'{}[{}]').format(vInfo.player.name, vInfo.player.clanAbbrev)
        self.as_setPlayerPanelInfoS({b'vehID': (vInfo.vehicleID), b'name': playerName, 
           b'badgeVO': badgeVO, 
           b'suffixBadgeIcon': ((b'badge_{}').format(suffixBadgeId) if suffixBadgeId else b''), 
           b'suffixBadgeStripIcon': ((b'strip_{}').format(suffixBadgeId) if suffixBadgeId else b''), 
           b'nameVehicle': (vInfo.vehicleType.shortName), 
           b'typeVehicle': (vInfo.vehicleType.classTag), 
           b'hpMax': (vInfo.vehicleType.maxHealth), 
           b'hpCurrent': hpCurrent, 
           b'isSelf': isSelf, 
           b'isSquad': isSquad, 
           b'squadIndex': (vInfo.squadIndex), 
           b'isPostMortem': (self.__isPostmortem)})
        return

    def __onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        self.__isPostmortem = True
        self.as_setPostmortemS(True)
        return

    def __onRespawnBaseMoving(self):
        self.__isPostmortem = False
        self.as_setPostmortemS(False)
        return
