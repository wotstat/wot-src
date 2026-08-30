from collections import namedtuple
import logging, itertools, typing
from UnitBase import UNIT_ROLE
from debug_utils import LOG_ERROR
from helpers.time_utils import ONE_MINUTE, ONE_HOUR
_logger = logging.getLogger(__name__)
BATTLE_TYPE_SORTIE = b'SORTIE'
INSPIRATION = b'INSPIRATION'
ARTILLERY_STRIKE = b'ARTILLERY_STRIKE'
REQUISITION = b'REQUISITION'
HIGH_CAPACITY_TRANSPORT = b'HIGH_CAPACITY_TRANSPORT'
SUPPORT_TYPE = b'SUPPORT'
BOOST_TYPE = b'BOOST'
REQUISITION_TYPE = b'REQUISITION'
HEAVYTRUCKS_TYPE = b'HEAVYTRUCKS'
ARTILLERY_COMMANDER = b'artillery_commander'
INSPIRE_COMMANDER = b'inspiring_commander'
RESERVE_STRONGHOLD_ORDER = (
 BOOST_TYPE,
 SUPPORT_TYPE,
 HEAVYTRUCKS_TYPE,
 REQUISITION_TYPE)
RESERVE_SORTIE_ORDER = (
 BOOST_TYPE,
 SUPPORT_TYPE,
 HEAVYTRUCKS_TYPE)
SUPPORT_ORDER = (
 ARTILLERY_STRIKE,)
RESERVE_ITEMS = {BOOST_TYPE: (
              INSPIRATION,), 
   SUPPORT_TYPE: (
                ARTILLERY_STRIKE,), 
   REQUISITION_TYPE: (
                    REQUISITION,), 
   HEAVYTRUCKS_TYPE: (
                    HIGH_CAPACITY_TRANSPORT,)}
UNIT_ROLE_BY_RESERVE_TYPE = {BOOST_TYPE: (UNIT_ROLE.CAN_USE_BOOST_EQUIPMENTS), 
   SUPPORT_TYPE: (UNIT_ROLE.CAN_USE_EXTRA_EQUIPMENTS)}
_OldStrongholdDataScheme = (
 b'type', b'min_level', b'max_level', b'min_players_count', b'max_players_count',
 b'industrial_resource_multiplier', b'max_legionaries_count', b'public', b'battle_duration',
 b'battle_series_duration', b'battle_idx', b'matchmaker_next_tick', b'time_to_ready',
 b'direction', b'requisition_bonus_percent', b'enemy_clan', b'clan', b'available_reserves',
 b'permissions', b'ready_button_enabled', b'selected_reserves', b'battle_series_status',
 b'battles_end_time', b'battles_start_time', b'fort_battles_before_start_lag',
 b'sorties_before_start_lag', b'sorties_before_end_lag', b'is_players_matching_available',
 b'slots_locked_by_filter')
_OldStrongholdDataProxyScheme = {b'header': (
             b'max_legionaries_count', b'max_players_count', b'direction', b'battle_duration', b'min_level', b'max_level',
             b'industrial_resource_multiplier', b'type', b'min_players_count', b'battle_idx', b'battle_series_status',
             b'battle_series_duration', b'enemy_clan', b'clan'), 
   b'timer': (
            b'sorties_before_start_lag', b'fort_battles_before_start_lag', b'sorties_before_end_lag', b'time_to_ready',
            b'matchmaker_next_tick', b'battles_start_time', b'battles_end_time'), 
   b'state': (
            b'public', b'is_players_matching_available', b'slots_locked_by_filter'), 
   b'reserve': (
              b'available_reserves', b'selected_reserves', b'requisition_bonus_percent', b'permissions'), 
   b'all': (
          b'ready_button_enabled',)}
_StrongholdDataScheme = (
 b'header', b'timer', b'state', b'reserve', b'all')

def isEnemyBattleIndex(index):
    return index >= 3


class StrongholdSettings(object):

    def __init__(self):
        self.__data = StrongholdData()
        self.__rawData = None
        self.__setDataMapping = {b'header': (self.__setHeader), 
           b'timer': (self.__setTimer), 
           b'state': (self.__setState), 
           b'reserve': (self.__setReserve), 
           b'all': (self.__setReadyButtonEnabled)}
        return

    def init(self):
        self.__setDataMapping = {b'header': (self.__setHeader), 
           b'timer': (self.__setTimer), 
           b'state': (self.__setState), 
           b'reserve': (self.__setReserve), 
           b'all': (self.__setReadyButtonEnabled)}
        return

    def fini(self):
        self.__setDataMapping = {}
        return

    def forceCleanData(self):
        if self.__rawData:
            self.__rawData = {}
        return

    def updateData(self, rawData):
        if not self.__validateData(rawData):
            LOG_ERROR(b'StrongholdSettings::updateData invalid data format')
            return None
        else:
            newRawData = self.__strongholdDataProxy(rawData)
            diffToUpdate = self.__makeDiff(newRawData)
            self.__setData(newRawData, diffToUpdate)
            return diffToUpdate

    def getData(self):
        return self.__data

    def getHeader(self):
        return self.__data.getHeader()

    def getTimer(self):
        return self.__data.getTimer()

    def getState(self):
        return self.__data.getState()

    def getReserve(self):
        return self.__data.getReserve()

    def isValid(self):
        return self.__data is not None and self.__rawData is not None

    def isStrongholdUnitFreezed(self):
        return not self.__data.getReadyButtonEnabled()

    def isFirstBattle(self):
        return self.__data.getHeader().getCurrentBattle() is None

    def isSortie(self):
        return self.__data.getHeader().isSortie()

    def isPlayersMatchingAvailable(self):
        return self.__data.getState().isPlayersMatchingAvailable()

    def getSlotsInPlayersMatching(self):
        return self.__data.getState().getSlotsLockedByFilter()

    def getReserveOrder(self):
        if self.isSortie():
            return RESERVE_SORTIE_ORDER
        return RESERVE_STRONGHOLD_ORDER

    def __validateData(self, rawData):
        for field in _OldStrongholdDataScheme:
            if field not in rawData:
                return False

        return True

    def __makeDiff(self, newRawData):
        diff = set()
        if newRawData is not None:
            for k, v in newRawData.iteritems():
                if self.__rawData is None or cmp(self.__rawData.get(k), v):
                    diff.add(k)

            self.__rawData = newRawData
        return diff

    def __setData(self, newRawData, diff):
        self.__rawData = newRawData
        for toUpdate in diff:
            dataSetFunc = self.__setDataMapping.get(toUpdate)
            if dataSetFunc is not None:
                dataSetFunc()

        return

    def __setHeader(self):
        self.__data.setHeader(self.__rawData[b'header'])
        return

    def __setTimer(self):
        self.__data.setTimer(self.__rawData[b'timer'])
        return

    def __setState(self):
        self.__data.setState(self.__rawData[b'state'])
        return

    def __setReadyButtonEnabled(self):
        self.__data.setReadyButtonEnabled(self.__rawData[b'all'])
        return

    def __setReserve(self):
        self.__data.setReserve(self.__rawData[b'reserve'])
        return

    def __strongholdDataProxy(self, rawData):
        correctRawData = {}
        for rootField, rootFieldValues in _OldStrongholdDataProxyScheme.iteritems():
            correctRawData[rootField] = {}
            for rootFieldItem in rootFieldValues:
                if rootFieldItem in rawData:
                    correctRawData[rootField][rootFieldItem] = rawData[rootFieldItem]

        return correctRawData


class StrongholdData(object):

    class StrongholdDataHeader(object):

        class StrongholdBattleSeriesItem(object):

            def __init__(self, index, data):
                self.__index = index
                self.__clan_owner_id = data[b'clan_owner_id']
                self.__map_id = data[b'map_id']
                self.__geometry_id = data[b'geometry_id']
                self.__gameplay_id = data[b'gameplay_id']
                self.__first_resp_clan_id = data[b'first_resp_clan_id']
                self.__battle_reward = data[b'battle_reward']
                self.__current_battle = data[b'current_battle']
                self.__attacker = data[b'attacker']
                return

            def getIndex(self):
                return self.__index

            def getClanId(self):
                return self.__clan_owner_id

            def getMapId(self):
                return self.__map_id

            def getGeometryId(self):
                return self.__geometry_id

            def getGameplayId(self):
                return self.__gameplay_id

            def getFirstClanId(self):
                return self.__first_resp_clan_id

            def getBattleReward(self):
                return self.__battle_reward

            def getCurrentBattle(self):
                return self.__current_battle

            def getAttacker(self):
                return self.__attacker

        class StrongholdClanData(object):

            def __init__(self, data):
                self.__id = data[b'id']
                self.__tag = data[b'tag']
                self.__name = data[b'name']
                self.__color = data[b'color']
                self.__status_ready = data[b'status_ready']
                return

            def getId(self):
                return self.__id

            def getTag(self):
                return self.__tag

            def getName(self):
                return self.__name

            def getColor(self):
                return self.__color

            def getReadyStatus(self):
                return self.__status_ready

        def __init__(self):
            self.__max_legionaries_count = None
            self.__max_players_count = None
            self.__min_players_count = None
            self.__max_level = None
            self.__min_level = None
            self.__type = None
            self.__direction = None
            self.__battle_duration = None
            self.__battle_idx = None
            self.__battle_series_duration = None
            self.__industrial_resource_multiplier = None
            self.__battle_series_status = None
            self.__current_battle = None
            self.__clan = None
            self.__enemy_clan = None
            return

        def setData(self, data):
            clan = data[b'clan']
            enemy_clan = data[b'enemy_clan']
            self.__clan = self.StrongholdClanData(clan) if clan else None
            self.__enemy_clan = self.StrongholdClanData(enemy_clan) if enemy_clan else None
            self.__max_legionaries_count = data[b'max_legionaries_count']
            self.__max_players_count = data[b'max_players_count']
            self.__min_players_count = data[b'min_players_count']
            self.__max_level = data[b'max_level']
            self.__min_level = data[b'min_level']
            self.__type = data[b'type']
            self.__direction = data[b'direction']
            self.__battle_duration = data[b'battle_duration']
            self.__battle_idx = data[b'battle_idx']
            self.__battle_series_duration = data[b'battle_series_duration']
            self.__industrial_resource_multiplier = data[b'industrial_resource_multiplier']
            self.__battle_series_status = [self.StrongholdBattleSeriesItem(index, v) for index, v in enumerate(data[b'battle_series_status'])]
            self.__current_battle = None
            for bs in self.__battle_series_status:
                if bs.getCurrentBattle():
                    self.__current_battle = bs

            return

        def getMaxLegionariesCount(self):
            return self.__max_legionaries_count

        def getMaxPlayersCount(self):
            return self.__max_players_count

        def getMinPlayersCount(self):
            return self.__min_players_count

        def getMaxLevel(self):
            return self.__max_level

        def getMinLevel(self):
            return self.__min_level

        def getType(self):
            return self.__type

        def getDirection(self):
            return self.__direction

        def getBattleDuration(self):
            return self.__battle_duration

        def getBattleIdx(self):
            return self.__battle_idx

        def getBattleSeriesStatus(self):
            return self.__battle_series_status

        def getBattleSeriesDuration(self):
            return self.__battle_series_duration

        def getIndustrialResourceMultiplier(self):
            return self.__industrial_resource_multiplier

        def getCurrentBattle(self):
            return self.__current_battle

        def getClan(self):
            return self.__clan

        def getEnemyClan(self):
            return self.__enemy_clan

        def getBattleDurationMinutes(self):
            return self.__battle_duration / ONE_MINUTE

        def getBattleSeriesDurationMinuts(self):
            return self.__battle_series_duration / ONE_MINUTE

        def getBattleSeriesDurationHours(self):
            return self.__battle_series_duration / ONE_HOUR

        def isSortie(self):
            return self.getType() == BATTLE_TYPE_SORTIE

    class StrongholdDataTimer(object):

        def __init__(self):
            self.__sorties_before_start_lag = None
            self.__fort_battles_before_start_lag = None
            self.__sorties_before_end_lag = None
            self.__time_to_ready = None
            self.__matchmaker_next_tick = None
            self.__battles_start_time = None
            self.__battles_end_time = None
            return

        def setData(self, data):
            self.__sorties_before_start_lag = data[b'sorties_before_start_lag']
            self.__fort_battles_before_start_lag = data[b'fort_battles_before_start_lag']
            self.__sorties_before_end_lag = data[b'sorties_before_end_lag']
            self.__time_to_ready = data[b'time_to_ready']
            self.__matchmaker_next_tick = data[b'matchmaker_next_tick']
            self.__battles_start_time = data[b'battles_start_time']
            self.__battles_end_time = data[b'battles_end_time']
            return

        def getSortiesBeforeStartLag(self):
            return self.__sorties_before_start_lag

        def getFortBattlesBeforeStartLag(self):
            return self.__fort_battles_before_start_lag

        def getSortiesBeforeEndLag(self):
            return self.__sorties_before_end_lag

        def getTimeToReady(self):
            return self.__time_to_ready

        def getMatchmakerNextTick(self):
            return self.__matchmaker_next_tick

        def getBattlesStartTime(self):
            return self.__battles_start_time

        def getBattlesEndTime(self):
            return self.__battles_end_time

    class StrongholdDataState(object):

        def __init__(self):
            self.__public = None
            self.__is_players_matching_available = None
            self.__slots_locked_by_filter = None
            return

        def setData(self, data):
            self.__public = data[b'public']
            self.__is_players_matching_available = data[b'is_players_matching_available']
            self.__slots_locked_by_filter = data[b'slots_locked_by_filter']
            return

        def getPublic(self):
            return self.__public

        def isPlayersMatchingAvailable(self):
            return self.__is_players_matching_available

        def getSlotsLockedByFilter(self):
            return self.__slots_locked_by_filter

    class StrongholdDataReserve(object):

        class StrongholdReserveItem(object):
            __slots__ = (b'__id', b'__type', b'__level', b'__bonus_percent', b'__description', b'__title', b'__production_elapsed', b'__intCD')

            def __init__(self, data):
                self.__id = data[b'id']
                self.__type = data[b'type']
                self.__level = data[b'level']
                self.__bonus_percent = data[b'bonus_percent']
                self.__description = data[b'description']
                self.__title = data[b'title']
                self.__production_elapsed = data[b'production_elapsed']
                self.__intCD = data.get(b'intCD')
                return

            def getId(self):
                return self.__id

            @property
            def intCD(self):
                return self.__intCD

            def getType(self):
                return self.__type

            def getGroupType(self):
                for groupType, group in RESERVE_ITEMS.iteritems():
                    if self.__type in group:
                        return groupType

                return

            def getLevel(self):
                return self.__level

            def getBonusPercent(self):
                return self.__bonus_percent

            def getDescription(self):
                return self.__description

            def getTitle(self):
                return self.__title

            def getProductionElapsed(self):
                return self.__production_elapsed

            def isUsingInBattle(self):
                return self.intCD is not None

            def isRequisition(self):
                return self.getGroupType() == REQUISITION

            def __eq__(self, other):
                if isinstance(other, self.__class__):
                    return self.__type == other.__type and self.__level == other.__level
                return False

            def __cmp__(self, other):
                if not isinstance(other, self.__class__):
                    return NotImplemented
                group = RESERVE_ITEMS[self.getGroupType()]
                typeOrder1 = group.index(self.__type)
                typeOrder2 = group.index(other.__type)
                return cmp((other.__level, typeOrder1), (
                 self.__level, typeOrder2))

        def __init__(self):
            self.__permissions = None
            self.__selected_reserves = []
            self.__available_reserves = {}
            self.__requisition_bonus_percent = None
            return

        def setData(self, data):
            self.__permissions = data[b'permissions']
            self.__requisition_bonus_percent = data[b'requisition_bonus_percent']
            self.__available_reserves = {group: [self.StrongholdReserveItem(v) for v in groupvalues] for group, groupvalues in data[b'available_reserves'].iteritems()}
            self.__selected_reserves = [self.getReserveById(reserveId) for reserveId in data[b'selected_reserves']]
            return

        def getPermissions(self):
            return self.__permissions

        def getSelectedReserves(self):
            return self.__selected_reserves

        def getAvailableReserves(self):
            return self.__available_reserves

        def getRequisitionBonusPercent(self):
            return self.__requisition_bonus_percent

        def getReserveById(self, reserveId):
            if reserveId is None or self.__available_reserves is None:
                return
            for reserve in itertools.chain(*self.__available_reserves.itervalues()):
                if reserve.getId() == reserveId:
                    return reserve

            return

        def getUniqueReservesByGroupType(self, groupType):
            reserves = []
            for rType in RESERVE_ITEMS[groupType]:
                if rType in self.__available_reserves:
                    reserves.extend(self.__available_reserves[rType])
                else:
                    _logger.warning(b'%s not in available reserves. Check wgsh settings.', rType)

            unique = []
            for reserve in self.__selected_reserves:
                if reserve and reserve.getGroupType() == groupType:
                    unique.append(reserve)

            for item in reserves:
                if item not in unique:
                    unique.append(item)

            uniqueAndSorted = sorted(unique, cmp=(lambda x, y: x.__cmp__(y)))
            return uniqueAndSorted

        def getReserveCount(self, rType, level):
            count = 0
            for reserve in itertools.chain(*self.__available_reserves.itervalues()):
                if reserve.getType() == rType and reserve.getLevel() == level:
                    count += 1

            return count

    def __init__(self):
        self.__header = self.StrongholdDataHeader()
        self.__timer = self.StrongholdDataTimer()
        self.__state = self.StrongholdDataState()
        self.__reserve = self.StrongholdDataReserve()
        self.__ready_button_enabled = None
        return

    def getHeader(self):
        return self.__header

    def setHeader(self, data):
        self.__header.setData(data)
        return

    def getTimer(self):
        return self.__timer

    def setTimer(self, data):
        self.__timer.setData(data)
        return

    def getState(self):
        return self.__state

    def setState(self, data):
        self.__state.setData(data)
        return

    def getReadyButtonEnabled(self):
        return self.__ready_button_enabled

    def setReadyButtonEnabled(self, data):
        self.__ready_button_enabled = data[b'ready_button_enabled']
        return

    def getReserve(self):
        return self.__reserve

    def setReserve(self, data):
        self.__reserve.setData(data)
        return


StrongholdUnitStats = namedtuple(b'UnitStats', (
 b'readyCount',
 b'occupiedSlotsCount',
 b'openedSlotsCount',
 b'freeSlotsCount',
 b'curTotalLevel',
 b'levelsSeq',
 b'clanMembersInRoster',
 b'legionariesInRoster',
 b'playersMatchingSlotsCount'))
StrongholdUnitStats.__new__.__defaults__ = (
 0, 0, 0, 0, 0, (), 0, 0, 0)
