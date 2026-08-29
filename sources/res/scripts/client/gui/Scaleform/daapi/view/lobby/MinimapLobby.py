import ArenaType
from gui.Scaleform.daapi.view.meta.MinimapPresentationMeta import MinimapPresentationMeta
from gui.Scaleform.genConsts.MINIMAPENTRIES_CONSTANTS import MINIMAPENTRIES_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
from points_of_interest_shared import PoiType
_POI_TYPE_TO_STR = {(PoiType.ARTILLERY): (MINIMAPENTRIES_CONSTANTS.POI_TYPE_ARTY), 
   (PoiType.RECON): (MINIMAPENTRIES_CONSTANTS.POI_TYPE_RECON), 
   (PoiType.SMOKE): (MINIMAPENTRIES_CONSTANTS.POI_TYPE_SMOKE), 
   (PoiType.MINEFIELD): (MINIMAPENTRIES_CONSTANTS.POI_TYPE_MINEFIELD)}

class MinimapLobby(MinimapPresentationMeta):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(MinimapLobby, self).__init__()
        self.__playerTeam = 1
        self.__arenaTypeID = None
        self.__cfg = dict()
        self.__minimapSize = 300
        return

    def _populate(self):
        super(MinimapLobby, self)._populate()
        self.settingsCore.onSettingsChanged += self.onSettingsChanging
        return

    def _dispose(self):
        self.settingsCore.onSettingsChanged -= self.onSettingsChanging
        super(MinimapLobby, self)._dispose()
        return

    def onSettingsChanging(self, diff):
        if b'isColorBlind' in diff:
            self.as_updatePointsS()
        return

    def setMap(self, arenaID):
        self.setArena(arenaID)
        return

    def setMinimapData(self, arenaID, playerTeam, size):
        self.__minimapSize = size
        self.__playerTeam = playerTeam
        self.setArena(arenaID)
        return

    def setPlayerTeam(self, playerTeam):
        self.__playerTeam = playerTeam
        return

    def swapTeams(self, team):
        doBuild = False
        if not team:
            team = 1
        if team is not self.__playerTeam:
            self.__playerTeam = team
            doBuild = True
        if doBuild and self.__arenaTypeID is not None:
            self.build()
        return

    def setArena(self, arenaTypeID):
        self.__arenaTypeID = int(arenaTypeID)
        arenaType = ArenaType.g_cache[self.__arenaTypeID]
        gameplayTypeIconPath = (b'../maps/icons/map/{}/{}.png').format(arenaType.gameplayName, arenaType.geometryName)
        if gameplayTypeIconPath in RES_ICONS.MAPS_ICONS_MAP_ENUM:
            mapIconPath = gameplayTypeIconPath
        else:
            mapIconPath = RES_ICONS.getMapPath(arenaType.geometryName)
        cfg = {b'texture': mapIconPath, 
           b'size': (arenaType.boundingBox), 
           b'teamBasePositions': (arenaType.teamBasePositions), 
           b'teamSpawnPoints': (arenaType.teamSpawnPoints), 
           b'controlPoints': (arenaType.controlPoints), 
           b'pointsOfInterest': (arenaType.pointsOfInterest)}
        self.setConfig(cfg)
        return

    def setEmpty(self):
        self.as_clearS()
        path = RES_ICONS.getMapPath(b'question')
        self.as_changeMapS(path)
        return

    def setConfig(self, cfg):
        self.__cfg = cfg
        self.build()
        return

    def build(self):
        self.as_clearS()
        self.as_changeMapS(self.__cfg[b'texture'])
        bottomLeft, upperRight = self.__cfg[b'size']
        mapWidthMult, mapHeightMult = (upperRight - bottomLeft) / self.__minimapSize
        offset = (upperRight + bottomLeft) * 0.5

        def _normalizePoint(posX, posY):
            return (
             (posX - offset.x) / mapWidthMult,
             (posY - offset.y) / mapHeightMult)

        for team, teamSpawnPoints in enumerate(self.__cfg[b'teamSpawnPoints'], 1):
            for spawn, spawnPoint in enumerate(teamSpawnPoints, 1):
                posX, posY = _normalizePoint(spawnPoint[0], spawnPoint[1])
                self.as_addPointS(posX, posY, MINIMAPENTRIES_CONSTANTS.POINT_TYPE_SPAWN, self.__getTeamColor(team == self.__playerTeam), spawn + 1 if len(teamSpawnPoints) > 1 else 1)

        for team, teamBasePoints in enumerate(self.__cfg[b'teamBasePositions'], 1):
            for baseNumber, basePoint in enumerate(teamBasePoints.values(), 2):
                posX, posY = _normalizePoint(basePoint[0], basePoint[1])
                self.as_addPointS(posX, posY, MINIMAPENTRIES_CONSTANTS.POINT_TYPE_BASE, self.__getTeamColor(team == self.__playerTeam), baseNumber if len(teamBasePoints) > 1 else 1)

        for idx, point in enumerate(self.__cfg[b'pointsOfInterest'], 1):
            x, y = _normalizePoint(*point[b'position'])
            poiType = point[b'type']
            self.as_addPoiS(x, y, _POI_TYPE_TO_STR[poiType], str(idx))

        if self.__cfg[b'controlPoints']:
            for index, controlPoint in enumerate(self.__cfg[b'controlPoints'], 2):
                posX, posY = _normalizePoint(controlPoint[0], controlPoint[1])
                self.as_addPointS(posX, posY, MINIMAPENTRIES_CONSTANTS.POINT_TYPE_CONTROL, MINIMAPENTRIES_CONSTANTS.COLOR_EMPTY, index if len(self.__cfg[b'controlPoints']) > 1 else 1)

        return

    def __getTeamColor(self, isPlayerTeam):
        if isPlayerTeam:
            return MINIMAPENTRIES_CONSTANTS.COLOR_BLUE
        return MINIMAPENTRIES_CONSTANTS.COLOR_RED
