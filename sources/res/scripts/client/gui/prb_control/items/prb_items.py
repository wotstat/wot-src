from collections import namedtuple
from past.builtins import cmp
from account_helpers import getAccountDatabaseID, getPlayerID
from constants import PREBATTLE_ACCOUNT_STATE, PREBATTLE_TEAM_STATE, OVERRIDDEN_BADGE
from gui.prb_control.prb_helpers import BadgesHelper
from gui.prb_control.settings import PREBATTLE_PLAYERS_SORT_TYPES
from gui.shared.gui_items.Vehicle import Vehicle, getOrderByVehicleClass
from gui.shared.sort_key import SortKey
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class PlayerPrbInfo(object):
    __slots__ = (b'accID', b'name', b'dbID', b'state', b'time', b'vehCompDescr', b'igrType', b'clanDBID', b'clanAbbrev', b'roster', b'isCreator', b'regionCode', b'badges', b'group', b'vehEnhancements', b'role')
    lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self, accID, name=b'', dbID=0, state=PREBATTLE_ACCOUNT_STATE.UNKNOWN, time=0.0, vehCompDescr=0, igrType=0, clanDBID=0, clanAbbrev=b'', roster=0, entity=None, badges=None, group=0, vehEnhancements=None, role=0):
        self.accID = accID
        self.name = name
        self.dbID = dbID
        self.state = state
        self.time = time
        self.vehCompDescr = vehCompDescr
        self.igrType = igrType
        self.clanDBID = clanDBID
        self.clanAbbrev = clanAbbrev
        self.roster = roster
        self.badges = BadgesHelper(badges or ())
        self.group = group
        self.vehEnhancements = vehEnhancements or {}
        self.role = role
        if entity is not None:
            self.isCreator = entity.isCommander(pDatabaseID=self.dbID)
        else:
            self.isCreator = False
        return

    def __repr__(self):
        badge = self.badges.getBadge()
        return (b'PlayerPrbInfo(accID = {0:n}, dbID = {1:n}, fullName = {2:>s}, state = {3:n}, isCreator = {4!r:s}, time = {5:n}, vehCompDescr = {6!r:s}, badgeID = {7}, vehEnhancements = {8}, role = {9})').format(self.accID, self.dbID, self.getFullName(), self.state, self.isCreator, self.time, self.getVehicle().name if self.isVehicleSpecified() else None, badge.badgeID if badge else None, self.vehEnhancements, self.role)

    def getFullName(self, isClan=True, isRegion=True):
        if isClan:
            clanAbbrev = self.clanAbbrev
        else:
            clanAbbrev = None
        if isRegion:
            pDBID = self.dbID
        else:
            pDBID = None
        return self.lobbyContext.getPlayerFullName(self.name, clanAbbrev=clanAbbrev, pDBID=pDBID)

    def isVehicleSpecified(self):
        return self.isReady() or self.inBattle()

    def getVehicle(self):
        return Vehicle(self.vehCompDescr)

    def isCurrentPlayer(self):
        if self.dbID > 0:
            result = self.dbID == getAccountDatabaseID()
        else:
            result = self.accID == getPlayerID()
        return result

    def isReady(self):
        return self.state & PREBATTLE_ACCOUNT_STATE.READY != 0

    def inBattle(self):
        return self.state & PREBATTLE_ACCOUNT_STATE.IN_BATTLE != 0

    def isOffline(self):
        return self.state & PREBATTLE_ACCOUNT_STATE.OFFLINE != 0

    def getBadge(self):
        return self.badges.getBadge()

    def getEnhancementVisibility(self):
        return self.vehEnhancements.get(b'badge', OVERRIDDEN_BADGE.NONE)

    def getEnhancementModules(self):
        return self.vehEnhancements.get(b'enhancements', [])


class TeamStateInfo(object):
    __slots__ = (b'state',)

    def __init__(self, state):
        super(TeamStateInfo, self).__init__()
        self.state = state
        return

    def __repr__(self):
        return (b'TeamStateInfo(state = {0:n}, isNotReady = {1!r:s}, isReady = {2!r:s}, isLocked = {3!r:s}, isInQueue = {4:n}').format(self.state, self.isNotReady(), self.isReady(), self.isLocked(), self.isInQueue())

    def isNotReady(self):
        return self.state is PREBATTLE_TEAM_STATE.NOT_READY

    def isReady(self):
        return self.state is PREBATTLE_TEAM_STATE.READY

    def isLocked(self):
        return self.state is PREBATTLE_TEAM_STATE.LOCKED

    def isInQueue(self):
        return self.state in [PREBATTLE_TEAM_STATE.READY,
         PREBATTLE_TEAM_STATE.LOCKED]


PlayersStateStats = namedtuple(b'PlayersStateStats', (b'notReadyCount', b'haveInBattle', b'playersCount', b'limitMaxCount'))

class PrbPropsInfo(object):
    __slots__ = (b'wins', b'battlesCount', b'createTime', b'teamsPositions')

    def __init__(self, wins=None, battlesCount=0, createTime=None, teamsPositions=None, **kwargs):
        super(PrbPropsInfo, self).__init__()
        self.wins = wins or [0, 0, 0]
        self.battlesCount = battlesCount
        self.createTime = createTime
        self.teamsPositions = teamsPositions
        return

    def getBattlesScore(self):
        return b'%d:%d' % (self.wins[1], self.wins[2])

    def __repr__(self):
        return (b'PrbPropsInfo(wins = {0!r:s}, battlesCount = {1:n}, createTime = {2:n})').format(self.wins, self.battlesCount, self.createTime)


class _PrebattlePlayersSortKey(SortKey):
    __slots__ = (b'player',)

    def __init__(self, player):
        super(_PrebattlePlayersSortKey, self).__init__()
        self.player = player
        return

    @classmethod
    def _playerNameComparator(cls, player, other):
        return cmp(player.name, other.name)

    @classmethod
    def _vehicleTypeComparator(cls, player, other):
        isPlayerVehicleSpecified = player.isVehicleSpecified()
        isOtherVehicleSpecified = other.isVehicleSpecified()
        if isPlayerVehicleSpecified != isOtherVehicleSpecified:
            return cmp(isOtherVehicleSpecified, isPlayerVehicleSpecified)
        if not isPlayerVehicleSpecified:
            return cmp(player.time, other.time)
        playerVehicle = player.getVehicle()
        otherVehicle = other.getVehicle()
        playerVehicleType = playerVehicle.type
        otherVehicleType = otherVehicle.type
        if playerVehicleType != otherVehicleType:
            return cmp(getOrderByVehicleClass(playerVehicleType), getOrderByVehicleClass(otherVehicleType))
        playerVehicleLevel = playerVehicle.level
        otherVehicleLevel = otherVehicle.level
        if playerVehicleLevel != otherVehicleLevel:
            return cmp(otherVehicleLevel, playerVehicleLevel)
        return cmp(playerVehicle.shortUserName, otherVehicle.shortUserName)


class _PrebattlePlayersRegularSortKey(_PrebattlePlayersSortKey):

    def _cmp(self, other):
        player, other = self.player, other.player
        if player.isCreator ^ other.isCreator:
            result = -1 if player.isCreator else 1
        else:
            result = cmp(player.time, other.time)
        return result


class _PrebattlePlayersObserversToBottomSortKey(_PrebattlePlayersSortKey):

    def _cmp(self, other):
        player, other = self.player, other.player
        playerIsObserver = player.isVehicleSpecified() and player.getVehicle().isObserver
        otherIsObserver = other.isVehicleSpecified() and other.getVehicle().isObserver
        if playerIsObserver ^ otherIsObserver:
            result = 1 if playerIsObserver else -1
        else:
            result = cmp(player.time, other.time)
        return result


class _PrebattlePlayersByVehicleSortKey(_PrebattlePlayersSortKey):

    def _cmp(self, other):
        return self._vehicleTypeComparator(self.player, other.player)


class _PrebattlePlayersByNameSortKey(_PrebattlePlayersSortKey):

    def _cmp(self, other):
        return self._playerNameComparator(self.player, other.player)


class _PrebattlePalyersByStateSortKey(_PrebattlePlayersSortKey):

    def _cmp(self, other):
        player, other = self.player, other.player
        if player.state != other.state:
            return cmp(other.state, player.state)
        if player.isVehicleSpecified():
            return self._vehicleTypeComparator(player, other)
        return self._playerNameComparator(player, other)


_PREBATTLE_PLAYERS_SORT_KEYS = {(PREBATTLE_PLAYERS_SORT_TYPES.REGULAR): _PrebattlePlayersRegularSortKey, 
   (PREBATTLE_PLAYERS_SORT_TYPES.OBSERVERS_TO_BOTTOM): _PrebattlePlayersObserversToBottomSortKey, 
   (PREBATTLE_PLAYERS_SORT_TYPES.BY_VEHICLE): _PrebattlePlayersByVehicleSortKey, 
   (PREBATTLE_PLAYERS_SORT_TYPES.BY_PLAYER_NAME): _PrebattlePlayersByNameSortKey, 
   (PREBATTLE_PLAYERS_SORT_TYPES.BY_STATE): _PrebattlePalyersByStateSortKey}

def getPlayersSortKey(playerSortKeyType=PREBATTLE_PLAYERS_SORT_TYPES.REGULAR):
    return _PREBATTLE_PLAYERS_SORT_KEYS.get(playerSortKeyType, _PrebattlePlayersRegularSortKey)
