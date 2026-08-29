from helpers import dependency
from constants import ARENA_BONUS_TYPE
from gui.impl.gen.resources import R
from gui.impl import backport
from gui.Scaleform.daapi.view.meta.BattleRoyaleFullStatsMeta import BattleRoyaleFullStatsMeta
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER_INDICES_REVERSED
from skeletons.gui.battle_session import IBattleSessionProvider
from battle_royale.gui.battle_control.controllers.vehicles_count_ctrl import IVehicleCountListener

class FullStatsComponent(BattleRoyaleFullStatsMeta, IVehicleCountListener):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(FullStatsComponent, self).__init__()
        self.__vehicleTeams = {}
        self.__isSquadMode = False
        self.__teamsCount = 0
        return

    @property
    def hasTabs(self):
        return False

    def onToggleVisibility(self, _):
        return

    def setVehicles(self, count, vehicles, teams):
        vehiclesByType = []
        vehiclesSortedByType = sorted(vehicles.items(), key=(lambda (classType, _): VEHICLE_TYPES_ORDER_INDICES_REVERSED[classType]))
        self.__vehicleTeams = {}
        for classType, data in vehiclesSortedByType:
            sortedVehicles = sorted(data.items(), key=(lambda (_, isDead): isDead))
            vehiclesByType.append({b'classType': classType, b'platoons': []})
            for vehInfo in sortedVehicles:
                vehicleID, (isDead, _, isEnemy, teamID, isRespawn) = vehInfo
                data = {b'isEnemy': isEnemy, b'isDead': (isDead and not isRespawn)}
                if isEnemy or isDead and not isRespawn:
                    vehiclesByType[-1][b'platoons'].append(data)
                else:
                    vehiclesByType[-1][b'platoons'].insert(0, data)
                if not isDead or isRespawn:
                    self.__vehicleTeams[vehicleID] = teamID

        self.__teamsCount = len(set(self.__vehicleTeams.values()))
        self.as_updateVehiclesCounterS({b'vehicles': vehiclesByType})
        self.__updateScore()
        return

    def setFrags(self, frags, isPlayerVehicle):
        self.__updateScore(frags)
        return

    def _populate(self):
        super(FullStatsComponent, self)._populate()
        self.__initPanel()
        return

    def __initPanel(self):
        arenaDP = self.sessionProvider.getArenaDP()
        self.__initTeamsCount()
        bonusType = self.sessionProvider.arenaVisitor.getArenaBonusType()
        self.__isSquadMode = bonusType in ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD_RANGE
        squads = b''
        if self.__isSquadMode:
            squads = backport.text(R.strings.battle_royale.fragPanel.squadsCount(), squadsCount=str(self.__teamsCount))
        frags = arenaDP.getVehicleStats().frags
        playersCount = len(set(self.__vehicleTeams.keys()))
        data = {b'header': {b'title': (backport.text(R.strings.battle_royale.fullStats.title())), 
                       b'subTitle': (backport.text(R.strings.battle_royale.fullStats.subTitle())), 
                       b'battleType': (arenaDP.getPersonalDescription().getFrameLabel()), 
                       b'description': (backport.text(R.strings.battle_royale.fullStats.description()))}, 
           b'aliveBlock': (self.__getScoreBlock(b'fullStatsAlive', playersCount, backport.text(R.strings.battle_royale.fullStats.alive()), squads)), 
           b'destroyedBlock': (self.__getScoreBlock(b'fullStatsDestroyed', frags, backport.text(R.strings.battle_royale.fullStats.destroyed()))), 
           b'minimapItems': (self.__getMinimapItems())}
        self.as_setDataS(data)
        return

    def __getScoreBlock(self, icon, count, descr, squads=b''):
        return {b'icon': icon, 
           b'count': count, 
           b'description': descr, 
           b'squads': squads}

    def __getMinimapItems(self):
        fullStatsIcons = R.strings.battle_royale.fullStats.icons
        return [
         self.__getMinimapItem(b'tab_corpse_loot', backport.text(fullStatsIcons.corpseLoot.description()), b'add'),
         self.__getMinimapItem(b'tab_loot', backport.text(fullStatsIcons.defaultLoot.description()), b'add'),
         self.__getMinimapItem(b'tab_improved_loot', backport.text(fullStatsIcons.extendedLoot.description()), b'add'),
         self.__getMinimapItem(b'airdrop_loot', backport.text(fullStatsIcons.airDrop.description()), b'add'),
         self.__getMinimapItem(b'deathzone_info_warning', backport.text(R.strings.battle_royale.fullStats.deathZone.warning.description())),
         self.__getMinimapItem(b'deathzone_info_closed', backport.text(R.strings.battle_royale.fullStats.deathZone.closed.description()))]

    def __getMinimapItem(self, icon, description, blendMode=b'normal'):
        return {b'icon': icon, 
           b'description': description, 
           b'blendMode': blendMode}

    def __updateScore(self, frags=None):
        arenaDP = self.sessionProvider.getArenaDP()
        playersCount = len(set(self.__vehicleTeams.keys()))
        if frags is None:
            vehicleID = arenaDP.getAttachedVehicleID()
            frags = arenaDP.getVehicleStats(vehicleID).frags
        squads = b''
        if self.__isSquadMode:
            squads = backport.text(R.strings.battle_royale.fragPanel.squadsCount(), squadsCount=str(self.__teamsCount))
        self.as_updateScoreS(playersCount, frags, squads)
        return

    def __initTeamsCount(self):
        arenaDP = self.sessionProvider.getArenaDP()
        for vInfoVO, _ in arenaDP.getVehiclesItemsGenerator():
            isAlive = vInfoVO.isAlive()
            isObserver = vInfoVO.isObserver()
            if not isObserver and isAlive:
                self.__vehicleTeams[vInfoVO.vehicleID] = vInfoVO.team

        self.__teamsCount = len(set(self.__vehicleTeams.values()))
        return
