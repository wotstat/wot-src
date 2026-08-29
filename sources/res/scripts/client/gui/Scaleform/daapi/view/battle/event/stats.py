from PlayerEvents import g_playerEvents
from constants import ARENA_PERIOD
from gui.Scaleform.daapi.view.meta.EventStatsMeta import EventStatsMeta
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
from gui.shared.badges import buildBadge
from gui.Scaleform.settings import ICONS_SIZES

class EventStats(EventStatsMeta, IArenaVehiclesController):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(EventStats, self).__init__()
        self._title = None
        self._desc = None
        self._points = dict()
        self.__arenaDP = self.sessionProvider.getArenaDP()
        return

    def invalidateArenaInfo(self):
        self.__updateTitleAndDescription()
        self.__updateStats()
        return

    def invalidateVehiclesStats(self, arenaDP):
        self.__updateStats()
        return

    def addVehicleInfo(self, vo, arenaDP):
        if not arenaDP.isAllyTeam(vo.team):
            return
        self.__updateStats()
        return

    def updateVehiclesInfo(self, updated, arenaDP):
        self.__updateStats()
        return

    def updateVehiclesStats(self, updated, arenaDP):
        self.__updateStats()
        return

    def _populate(self):
        super(EventStats, self)._populate()
        self.sessionProvider.addArenaCtrl(self)
        g_playerEvents.onArenaPeriodChange += self.__onArenaPeriodChange
        self.__updateTitleAndDescription()
        self.__updateStats()
        return

    def _dispose(self):
        g_playerEvents.onArenaPeriodChange -= self.__onArenaPeriodChange
        self.sessionProvider.removeArenaCtrl(self)
        super(EventStats, self)._dispose()
        return

    def __updateTitleAndDescription(self):
        if self._title and self._desc:
            self.as_updateTitleS(self._title, self._desc)
        return

    def __updateStats(self):
        infoIterator = self.__arenaDP.getVehiclesInfoIterator()
        self.as_updatePlayerStatsS([self.__makePlayerInfo(vInfo) for vInfo in infoIterator if self.__arenaDP.isAllyTeam(vInfo.team)])
        return

    def __makePlayerInfo(self, vInfo):
        playerVehicle = self.__arenaDP.getVehicleInfo()
        playerSquad = playerVehicle.squadIndex
        vehID = vInfo.vehicleID
        badgeID = vInfo.selectedBadge
        suffixBadgeId = vInfo.selectedSuffixBadge
        vStats = self.__arenaDP.getVehicleStats(vehID)
        frags = vStats.frags if vStats is not None else 0
        isSquad = playerSquad > 0 and playerSquad == vInfo.squadIndex
        isPlayerHimself = vehID == playerVehicle.vehicleID
        playerName = vInfo.player.name
        if vInfo.player.clanAbbrev:
            playerName = (b'{}[{}]').format(vInfo.player.name, vInfo.player.clanAbbrev)
        badge = buildBadge(badgeID, vInfo.getBadgeExtraInfo())
        badgeVO = badge.getBadgeVO(ICONS_SIZES.X24, {b'isAtlasSource': True}, shortIconName=True) if badge else None
        return {b'playerName': playerName, 
           b'squadIndex': (str(vInfo.squadIndex) if vInfo.squadIndex else b''), 
           b'badgeVO': badgeVO, 
           b'suffixBadgeIcon': ((b'badge_{}').format(suffixBadgeId) if suffixBadgeId else b''), 
           b'suffixBadgeStripIcon': ((b'strip_{}').format(suffixBadgeId) if suffixBadgeId else b''), 
           b'isAlive': (vInfo.isAlive()), 
           b'isSquad': isSquad, 
           b'points': (str(int(self.getPoints(vehID)))), 
           b'kills': (str(int(frags))), 
           b'vehicleName': (vInfo.vehicleType.shortName), 
           b'vehicleTypeIcon': ((b'fullStatsVehicleType_green_{}').format(vInfo.vehicleType.classTag)), 
           b'isPlayerHimself': isPlayerHimself}

    def getPoints(self, vehID):
        return self._points.get(vehID, 0)

    def setPoints(self, vehID, points):
        self._points[vehID] = points
        return

    def setTitle(self, title):
        self._title = title
        return

    def setDescription(self, desc):
        self._desc = desc
        return

    def __onArenaPeriodChange(self, period, periodEndTime, periodLength, periodAdditionalInfo):
        if period == ARENA_PERIOD.BATTLE:
            self.__updateStats()
        return
