import typing, BigWorld
from portal.gui.Scaleform.daapi.view.meta.PortalPlayersPanelMeta import PortalPlayersPanelMeta
from PortalTeamInfoComponent import PortalTeamInfoComponent
from gui.Scaleform.framework.entities.DAAPIDataProvider import ListDAAPIDataProvider
from gui.Scaleform.settings import ICONS_SIZES
from gui.battle_control import avatar_getter
from gui.battle_control.arena_info.arena_vos import VehicleArenaInfoVO
from gui.battle_control.arena_info.settings import INVITATION_DELIVERY_STATUS, PLAYER_STATUS
from gui.battle_control.controllers.battle_field_ctrl import IBattleFieldListener
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.shared.badges import buildBadge
from gui.shared.view_helpers import UsersInfoHelper
from helpers import dependency, int2roman
from skeletons.account_helpers.settings_core import ISettingsCore
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from typing import Dict, Optional, List

class PortalPlayersDataPanel(IBattleFieldListener, PortalPlayersPanelMeta, IAbstractPeriodView, IArenaVehiclesController):
    settingsCore = dependency.descriptor(ISettingsCore)
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(PortalPlayersDataPanel, self).__init__()
        self.__arenaDP = self.sessionProvider.getArenaDP()
        self.__playersListDP = PlayersListDataProvider()
        self.__vehListIndices = {}
        self.__prevVehHP = {}
        self.__userInfoHelper = UsersInfoHelper()
        return

    @property
    def teamInfo(self):
        if BigWorld.player() is not None:
            arena = BigWorld.player().arena
            if arena:
                return arena.teamInfo.dynamicComponents.get(b'portalTeamInfoComponent')
        return

    def updateVehicleHealth(self, vehicleID, newHealth, maxHealth):
        if vehicleID in self.__vehListIndices:
            self.__setVehicleHealth(vehicleID, newHealth)
        return

    def _populate(self):
        super(PortalPlayersDataPanel, self)._populate()
        self.__playersListDP.setFlashObject(self.as_getDPS())
        PortalTeamInfoComponent.onAllyInfoUpdated += self.__onVehicleUpdated
        self.sessionProvider.addArenaCtrl(self)
        self.__updateAllTeammates()
        return

    def _dispose(self):
        self.sessionProvider.removeArenaCtrl(self)
        PortalTeamInfoComponent.onAllyInfoUpdated -= self.__onVehicleUpdated
        self.__playersListDP.dispose()
        self.__playersListDP = None
        self.__arenaDP = None
        self.__vehListIndices = None
        self.__prevVehHP = None
        self.__userInfoHelper = None
        super(PortalPlayersDataPanel, self)._dispose()
        return

    def invalidateVehicleStatus(self, _, vInfoVO, __):
        self.__updateOneTeammate(vInfoVO.vehicleID)
        return

    def updateVehiclesInfo(self, updated, _):
        for _, vInfo in updated:
            self.__updateOneTeammate(vInfo.vehicleID)

        return

    def __onVehicleUpdated(self, vehID):
        self.__updateOneTeammate(vehID)
        return

    def __updateAllTeammates(self):
        arenaDP = self.__arenaDP
        vInfos = arenaDP.getVehiclesInfoIterator()
        teammateInfos = (v for v in vInfos if not v.isBot and arenaDP.isAlly(v.vehicleID))
        usersList = [self.__getUserVo(vInfo) for vInfo in teammateInfos]
        self.__sortTeammates(usersList)
        self.__saveVehicleListIndices(usersList)
        self.__playersListDP.buildList(usersList)
        return

    def __updateOneTeammate(self, vehicleID):
        index = self.__vehListIndices.get(vehicleID, None)
        if index is None:
            self.__updateAllTeammates()
            return
        else:
            arenaDP = self.__arenaDP
            vInfo = arenaDP.getVehicleInfo(vehicleID)
            self.__playersListDP.updateItemData(index, self.__getUserVo(vInfo))
            return

    def __sortTeammates(self, usersList):
        usersList.sort(key=(lambda x: (
         -self.__getVehicleLevel(x[b'vehicleID']),
         x[b'playerName'],
         x[b'vehicleType'])))
        return

    def __saveVehicleListIndices(self, usersList):
        self.__vehListIndices.clear()
        self.__vehListIndices = {item[b'vehicleID']: i for i, item in enumerate(usersList)}
        return

    def __getUserVo(self, vInfo):
        vehicleHealthInfo = self.sessionProvider.dynamic.battleField.getVehicleHealthInfo(vInfo.vehicleID)
        player = vInfo.player
        sessionID = player.avatarSessionID
        vType = vInfo.vehicleType
        userVO = {b'accountDBID': (player.accountDBID), 
           b'sessionID': sessionID, 
           b'playerName': (player.name), 
           b'playerFakeName': (player.fakeName), 
           b'clanAbbrev': (player.clanAbbrev), 
           b'region': b'', 
           b'igrType': (player.igrType), 
           b'userTags': (self.__userInfoHelper.getUserTags(sessionID, player.igrType)), 
           b'squadIndex': (vInfo.squadIndex), 
           b'playerStatus': (self.__getTeammatePlayerStatus(vInfo)), 
           b'invitationStatus': (INVITATION_DELIVERY_STATUS.NONE), 
           b'vehicleID': (vInfo.vehicleID), 
           b'vehicleName': (vType.shortName), 
           b'vehicleType': (vType.classTag), 
           b'vehicleLevel': (int2roman(self.__getVehicleLevel(vInfo.vehicleID))), 
           b'vehicleStatus': (vInfo.vehicleStatus), 
           b'hpMax': (vType.maxHealth), 
           b'hpCurrent': (vehicleHealthInfo[0] if vehicleHealthInfo and vehicleHealthInfo[0] > 0 else 0), 
           b'secondsToRespawn': (self.__getSecondsToRespawn(vInfo.vehicleID))}
        badge = buildBadge(vInfo.selectedBadge, vInfo.getBadgeExtraInfo())
        if badge is not None:
            userVO[b'badge'] = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': True}, shortIconName=True)
        return userVO

    def __getVehicleLevel(self, vehID):
        if self.teamInfo:
            return self.teamInfo.getVehicleLevel(vehID)
        return 0

    def __getSecondsToRespawn(self, vehID):
        if self.teamInfo:
            return self.teamInfo.getRespawnTime(vehID)
        return 0.0

    def __setVehicleHealth(self, vehID, health):
        vInfo = self.__arenaDP.getVehicleInfo(vehID)
        if self.__arenaDP.isAlly(vInfo.vehicleID):
            isSkipAnimation = True
            if 0 < self.__prevVehHP.setdefault(vehID, health) < vInfo.vehicleType.maxHealth:
                isSkipAnimation = False
            self.as_setPlayerHpS(vehID, vInfo.vehicleType.maxHealth, health, isSkipAnimation)
            self.__prevVehHP[vehID] = health
        return

    def __getTeammatePlayerStatus(self, vInfo):
        if vInfo.isSquadMan(self.__arenaDP.getVehicleInfo(avatar_getter.getPlayerVehicleID()).prebattleID):
            return PLAYER_STATUS.IS_SQUAD_PERSONAL
        return vInfo.playerStatus


class PlayersListDataProvider(ListDAAPIDataProvider):

    def __init__(self):
        super(PlayersListDataProvider, self).__init__()
        self._list = []
        return

    @property
    def collection(self):
        return self._list

    def emptyItem(self):
        return {}

    def clear(self):
        self._list = []
        return

    def dispose(self):
        self.clear()
        self.destroy()
        return

    def buildList(self, itemsVoList):
        if itemsVoList != self._list and self._isDAAPIInited():
            self._list = itemsVoList
            self.refresh()
        return

    def updateItemData(self, index, itemVO):
        if self._isDAAPIInited():
            self._list[index] = itemVO
            self.refreshSingleItem(index, itemVO)
        return
