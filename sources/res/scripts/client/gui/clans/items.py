from collections import namedtuple
from datetime import datetime
from gui.impl import backport
from helpers import time_utils, int2roman
from messenger.ext import passCensor
from shared_utils import makeTupleByDict
from predefined_hosts import g_preDefinedHosts
from debug_utils import LOG_WARNING
from gui.clans import formatters as clans_fmts
from gui.clans.settings import MAX_CLAN_MEMBERS_COUNT, CLAN_INVITE_STATES_SORT_RULES, CLAN_INVITE_STATES
from debug_utils import LOG_ERROR
from helpers.time_utils import getTimeDeltaTillNow, ONE_DAY

def _getTimestamp(datetimeValue):
    return time_utils.getTimestampFromUTC(datetimeValue.timetuple())


def _toPercents(value):
    if value:
        return 100 * value
    return value


def _getEfficiency(dividend, delimiter):
    return float(dividend) / delimiter


_defDateTime = datetime.fromtimestamp(0)

def formatField(getter, dummy=None, formatter=None):
    return str(getter(doFmt=True, dummy=dummy, formatter=formatter))


def isValueAvailable(getter):
    return getter(checkAvailability=True)


class FieldsCheckerMixin(object):

    def __init__(self, *args, **kwargs):
        super(FieldsCheckerMixin, self).__init__()
        self.__class = self.__class__
        if hasattr(self, b'_fields'):
            self._invalidFields = set(arg for arg in self._fields if arg not in kwargs)
        else:
            self._invalidFields = set()
        return

    def isFieldValid(self, fieldName):
        return fieldName not in self._invalidFields

    def isValid(self):
        return not set(self._getCriticalFields()) & self._invalidFields

    def update(self, *args, **kwargs):
        obj = self._replace(**kwargs)
        obj._invalidFields = self._invalidFields
        return obj

    def _getCriticalFields(self):
        LOG_ERROR(b'Method must be override!', b'_getCriticalFields', self.__class__)
        return tuple()


def fmtUnavailableValue(fields=tuple(), dummy=clans_fmts.DUMMY_UNAVAILABLE_DATA):

    def decorator(func):

        def wrapper(self, *args, **kwargs):

            def _isAvailable(fields):
                for field in fields:
                    if not self.isFieldValid(field):
                        return False

                return True

            checkAvailability = kwargs.pop(b'checkAvailability', False)
            if checkAvailability:
                return _isAvailable(fields)
            else:
                doFmt = kwargs.get(b'doFmt', False)
                placeholder = kwargs.get(b'dummy', dummy) or dummy
                f = kwargs.get(b'formatter', None)
                if doFmt and not _isAvailable(fields):
                    return placeholder
                try:
                    value = func(self)
                except ValueError:
                    value = None

                if value is None:
                    return placeholder
                if f is not None:
                    return f(value)
                return value

        return wrapper

    return decorator


def fmtNullValue(nullValue=0, dummy=clans_fmts.DUMMY_NULL_DATA):

    def decorator(func):

        def wrapper(*args, **kwargs):
            checkAvailability = kwargs.get(b'checkAvailability', False)
            doFmt = kwargs.get(b'doFmt', False)
            value = func(*args, **kwargs)
            if not checkAvailability and doFmt and value == nullValue:
                value = dummy
            return value

        return wrapper

    return decorator


def fmtZeroDivisionValue(defValue=0, dummy=clans_fmts.DUMMY_NULL_DATA):

    def decorator(func):

        def wrapper(*args, **kwargs):
            try:
                value = func(*args, **kwargs)
            except ZeroDivisionError:
                if kwargs.get(b'doFmt', False):
                    return kwargs.get(b'dummy', dummy) or dummy
                return defValue

            return value

        return wrapper

    return decorator


def _formatString(value):
    if not value:
        return clans_fmts.DUMMY_UNAVAILABLE_DATA
    return passCensor(value)


def fmtDelegat(path, dummy=clans_fmts.DUMMY_UNAVAILABLE_DATA):

    def decorator(func):

        def wrapper(self, *args, **kwargs):

            def _getGetter(path):
                return reduce(getattr, path.split(b'.'), self)

            checkAvailability = kwargs.pop(b'checkAvailability', False)
            doFmt = kwargs.pop(b'doFmt', False)
            placeholder = kwargs.pop(b'dummy', dummy) or dummy
            f = kwargs.pop(b'formatter', None)
            if checkAvailability:
                return _getGetter(path)(checkAvailability=checkAvailability)
            else:
                if doFmt:
                    return _getGetter(path)(doFmt=doFmt, dummy=placeholder, formatter=f)
                return func(self, *args, **kwargs)

        return wrapper

    return decorator


def formatter(formatter=None):

    def decorator(func):

        def wrapper(self, *args, **kwargs):
            doFmt = kwargs.get(b'doFmt', False)
            fmt = kwargs.get(b'formatter', None) or formatter
            value = func(self)
            if doFmt and fmt:
                value = fmt(value)
            return value

        return wrapper

    return decorator


def simpleFormatter(formatter=None):

    def decorator(func):

        def wrapper(self):
            value = func(self)
            if formatter and value is not None:
                value = formatter(value)
            return value

        return wrapper

    return decorator


_ClanExtInfoData = namedtuple(b'ClanExtInfoData', [
 29, 30, 31, 32, 33, 
 34, 35, 36, 37])
_ClanExtInfoData.__new__.__defaults__ = (
 b'', b'', b'', 0, _defDateTime, 0, 0, False, 0)
_ClanExtInfoDataCritical = (b'name', b'tag', b'members_count', b'clan_id')

class ClanExtInfoData(_ClanExtInfoData, FieldsCheckerMixin):

    def getDbID(self):
        return self.clan_id

    @fmtUnavailableValue(fields=(b'name',))
    def getClanName(self):
        return passCensor(self.name)

    @fmtUnavailableValue(fields=(b'name', b'tag'))
    def getFullName(self):
        if self.tag:
            return b'%s %s' % (
             clans_fmts.getClanAbbrevString(self.getTag()), self.getClanName())
        return b''

    @fmtUnavailableValue(fields=(b'tag',))
    def getTag(self):
        return passCensor(self.tag)

    @fmtUnavailableValue(fields=(b'motto',))
    def getMotto(self):
        return passCensor(self.motto)

    @fmtUnavailableValue(fields=(b'members_count',))
    def getMembersCount(self):
        return self.members_count

    @fmtUnavailableValue(fields=(b'leader_id',))
    def getLeaderDbID(self):
        return self.leader_id

    @fmtUnavailableValue(fields=(b'treasury',))
    def getTreasuryValue(self):
        return self.treasury

    def isOpened(self):
        return self.accepts_join_requests

    @fmtUnavailableValue(fields=(b'members_count',))
    def getFreePlaces(self):
        return MAX_CLAN_MEMBERS_COUNT - self.members_count

    def hasFreePlaces(self):
        return self.getFreePlaces() > 0

    @fmtUnavailableValue(fields=(b'created_at',))
    def getCreatedAt(self):
        if self.created_at:
            return _getTimestamp(self.created_at)
        return 0

    def _getCriticalFields(self):
        return _ClanExtInfoDataCritical


_ClanRatingsData = namedtuple(b'ClanRatingsData', [
 37, 41, 42, 43, 44, 
 45, 46, 47, 
 48, 49, 50, 
 51, 52, 53, 
 54, 
 55, 
 56, 
 57])
_ClanRatingsData.__new__.__defaults__ = tuple([0] * len(_ClanRatingsData._fields))
_ClanRatingsDataCriticalFields = (b'efficiency', b'battles_count_avg', b'wins_ratio_avg', b'xp_avg')

class ClanRatingsData(_ClanRatingsData, FieldsCheckerMixin):

    def getClanDbID(self):
        return self.clan_id

    @fmtUnavailableValue(fields=(b'efficiency',))
    def getEfficiency(self):
        return self.efficiency

    @fmtUnavailableValue(fields=(b'fb_elo_rating_10',))
    def getEloRating10(self):
        return self.fb_elo_rating_10

    @fmtUnavailableValue(fields=(b'fb_elo_rating_8',))
    def getEloRating8(self):
        return self.fb_elo_rating_8

    @fmtUnavailableValue(fields=(b'gm_battles_count_28d',))
    def getGlobalMapBattlesFor28Days(self):
        return self.gm_battles_count_28d

    @fmtUnavailableValue(fields=(b'gm_elo_rating_10',))
    def getGlobalMapEloRating10(self):
        return self.gm_elo_rating_10

    @fmtUnavailableValue(fields=(b'gm_elo_rating_8',))
    def getGlobalMapEloRating8(self):
        return self.gm_elo_rating_8

    @fmtUnavailableValue(fields=(b'gm_elo_rating_6',))
    def getGlobalMapEloRating6(self):
        return self.gm_elo_rating_6

    @fmtUnavailableValue(fields=(b'battles_count_avg',))
    def getBattlesCountAvg(self):
        return self.battles_count_avg

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'wins_ratio_avg', b'battles_count_avg'))
    def getWinsRatioAvg(self):
        if self.battles_count_avg > 0:
            return self.wins_ratio_avg
        raise ZeroDivisionError()
        return

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'xp_avg', b'battles_count_avg'))
    def getBattlesPerformanceAvg(self):
        if self.battles_count_avg > 0:
            return self.xp_avg
        raise ZeroDivisionError()
        return

    @fmtUnavailableValue(fields=(b'gm_elo_rating_10_rank',))
    def getGlobalMapEloRatingRank10(self):
        return self.gm_elo_rating_10_rank

    @fmtUnavailableValue(fields=(b'gm_elo_rating_8_rank',))
    def getGlobalMapEloRatingRank8(self):
        return self.gm_elo_rating_8_rank

    @fmtUnavailableValue(fields=(b'gm_elo_rating_6_rank',))
    def getGlobalMapEloRatingRank6(self):
        return self.gm_elo_rating_6_rank

    def isActive(self):
        return self.gm_battles_count_28d > 0

    def isGlobalMapOutdated(self):
        return self.gm_battles_count_28d <= 0

    def isBattlesOutdated(self):
        return self.fb_battles_count_10_28d <= 0

    def isSortiesOutdated(self):
        return self.fs_battles_count_10_28d <= 0

    def hasFortRating(self):
        for gtr in (self.getEloRating10, self.getEloRating8):
            if not isValueAvailable(gtr):
                return False

        return self.fb_elo_rating_10 != 1000 or self.fb_elo_rating_8 != 1000

    def _getCriticalFields(self):
        return _ClanRatingsDataCriticalFields


_ClanGlobalMapStatsData = namedtuple(b'ClanGlobalMapStatsData', [
 60, 61, 62, 
 63, 64, 65, 
 66, 67, 68, 
 69, 70, 71])
_ClanGlobalMapStatsData.__new__.__defaults__ = tuple([0] * len(_ClanGlobalMapStatsData._fields))

class ClanGlobalMapStatsData(_ClanGlobalMapStatsData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'battles_played', b'provinces_captured'))
    def hasGlobalMap(self):
        return self.battles_played > 0 or self.provinces_captured > 0

    @fmtUnavailableValue(fields=(b'battles_played',))
    def getBattlesCount(self):
        return self.battles_played

    @fmtUnavailableValue(fields=(b'battles_won',))
    def getWinsCount(self):
        return self.battles_won

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'battles_won', b'battles_played'))
    def getWinsEfficiency(self):
        return _getEfficiency(self.battles_won, self.battles_played)

    @fmtUnavailableValue(fields=(b'battles_lost',))
    def getLoosesCount(self):
        return self.battles_lost

    @fmtUnavailableValue(fields=(b'influence_points',))
    def getInfluencePointsCount(self):
        return self.influence_points

    @fmtUnavailableValue(fields=(b'provinces_captured',))
    def getCapturedProvincesCount(self):
        return self.provinces_captured

    @fmtUnavailableValue(fields=(b'provinces_count',))
    def getCurrentProvincesCount(self):
        return self.provinces_count

    @fmtUnavailableValue(fields=(b'battles_played_on_6_level',))
    def getBattles6LevelCount(self):
        return self.battles_played_on_6_level

    @fmtUnavailableValue(fields=(b'battles_won_on_6_level',))
    def getWins6LevelCount(self):
        return self.battles_won_on_6_level

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'battles_won_on_6_level', b'battles_played_on_6_level'))
    def getWins6LevelEfficiency(self):
        return _getEfficiency(self.battles_won_on_6_level, self.battles_played_on_6_level)

    @fmtUnavailableValue(fields=(b'battles_played_on_8_level',))
    def getBattles8LevelCount(self):
        return self.battles_played_on_8_level

    @fmtUnavailableValue(fields=(b'battles_won_on_8_level',))
    def getWins8LevelCount(self):
        return self.battles_won_on_8_level

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'battles_won_on_8_level', b'battles_played_on_8_level'))
    def getWins8LevelEfficiency(self):
        return _getEfficiency(self.battles_won_on_8_level, self.battles_played_on_8_level)

    @fmtUnavailableValue(fields=(b'battles_played_on_10_level',))
    def getBattles10LevelCount(self):
        return self.battles_played_on_10_level

    @fmtUnavailableValue(fields=(b'battles_won_on_10_level',))
    def getWins10LevelCount(self):
        return self.battles_won_on_10_level

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'battles_won_on_10_level', b'battles_played_on_10_level'))
    def getWins10LevelEfficiency(self):
        return _getEfficiency(self.battles_won_on_10_level, self.battles_played_on_10_level)


Building = namedtuple(b'Building', b'type direction level position')
_ClanStrongholdInfoData = namedtuple(b'ClanStrongholdData', [
 76, 77, 78, 
 79, 80, 
 81, 82, 83, 
 84, 85, 
 86, 87, 
 88, 
 89, 
 90, 91, 
 92, 93, 
 94, 95, 96, 97, 
 98, 99, 100, 
 101, 
 102, 103, 104])
_ClanStrongholdInfoData.__new__.__defaults__ = ([],) + tuple([0] * (len(_ClanStrongholdInfoData._fields) - 1))
DefClanStrongholdInfoData = _ClanStrongholdInfoData([], 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None)

class ClanStrongholdInfoData(_ClanStrongholdInfoData, FieldsCheckerMixin):

    def hasFort(self):
        return self.level > 0

    def getBuildings(self):
        result = []
        for b in self.buildings:
            try:
                result.append(makeTupleByDict(Building, b))
            except Exception:
                LOG_WARNING(b'There is error while collecting Buildings list', self.buildings)

        return result

    @fmtUnavailableValue(fields=(b'level',))
    def getLevel(self):
        return self.level

    @fmtUnavailableValue(fields=(b'sortie_battles_count',))
    def getSortieBattlesCount(self):
        return self.sortie_battles_count

    @fmtUnavailableValue(fields=(b'sortie_wins',))
    def getSortieWinsCount(self):
        return self.sortie_wins

    @fmtUnavailableValue(fields=(b'sortie_losses',))
    def getSortieLossesCount(self):
        return self.sortie_losses

    @fmtUnavailableValue(fields=(b'sortie_middle_battles_count',))
    def getSortieMiddleBattlesCount(self):
        return self.sortie_middle_battles_count

    @fmtUnavailableValue(fields=(b'sortie_champion_battles_count',))
    def getSortieChampionBattlesCount(self):
        return self.sortie_champion_battles_count

    @fmtUnavailableValue(fields=(b'sortie_absolute_battles_count',))
    def getSortieAbsoluteBattlesCount(self):
        return self.sortie_absolute_battles_count

    @fmtUnavailableValue(fields=(b'sortie_fort_resource_in_middle',))
    def getSortieMiddleResourcesCount(self):
        return self.sortie_fort_resource_in_middle

    @fmtUnavailableValue(fields=(b'sortie_fort_resource_in_champion',))
    def getSortieChampionResourcesCount(self):
        return self.sortie_fort_resource_in_champion

    @fmtUnavailableValue(fields=(b'sortie_fort_resource_in_absolute',))
    def getSortieAbsoluteResourcesCount(self):
        return self.sortie_fort_resource_in_absolute

    @fmtUnavailableValue(fields=(b'defence_battles_count',))
    def getDefenceBattlesCount(self):
        return self.defence_battles_count

    @fmtUnavailableValue(fields=(b'defence_combat_wins',))
    def getDefenceCombatsCount(self):
        return self.defence_combat_wins

    @fmtUnavailableValue(fields=(b'defence_resource_capture_count',))
    def getDefenceCapturedResourcesCount(self):
        return self.defence_resource_capture_count

    @fmtUnavailableValue(fields=(b'defence_resource_loss_count',))
    def getDefenceLostResourcesCount(self):
        return self.defence_resource_loss_count

    @fmtUnavailableValue(fields=(b'defence_enemy_base_capture_count',))
    def getDefenceEnemyBaseCapturesPointsCount(self):
        return self.defence_enemy_base_capture_count

    @fmtUnavailableValue(fields=(b'defence_capture_enemy_building_total_count',))
    def getDefenceCapturedEnemyBuildingsCount(self):
        return self.defence_capture_enemy_building_total_count

    @fmtUnavailableValue(fields=(b'defence_loss_own_building_total_count',))
    def getDefenceLostOwnBuildingsCount(self):
        return self.defence_loss_own_building_total_count

    @fmtUnavailableValue(fields=(b'defence_attack_count',))
    def getAttacksCount(self):
        return self.defence_attack_count

    @fmtUnavailableValue(fields=(b'defence_success_attack_count',))
    def getSuccessAttacksCount(self):
        return self.defence_success_attack_count

    @fmtUnavailableValue(fields=(b'defence_defence_count',))
    def getDefencesCount(self):
        return self.defence_defence_count

    @fmtUnavailableValue(fields=(b'defence_hour',))
    def getDefenceHour(self):
        return self.defence_hour

    @fmtUnavailableValue(fields=(b'defence_success_defence_count',))
    def getSuccessDefencesCount(self):
        return self.defence_success_defence_count

    @fmtUnavailableValue(fields=(b'fb_battles_count_8',))
    def getFbBattlesCount8(self):
        return self.fb_battles_count_8

    @fmtUnavailableValue(fields=(b'fb_battles_count_10',))
    def getFbBattlesCount10(self):
        return self.fb_battles_count_10

    def isDefenceModeActivated(self):
        return self.defence_mode_is_activated


BuildingStats = namedtuple(b'BuildingStats', b'position type level hp storage')
BuildingStats.__new__.__defaults__ = (0, 0, 0, 0, 0)
_StrongholdStatisticsData = namedtuple(b'ClanStrongholdData', [
 110, 111, 112, 
 113, 114, 
 115, 116])
_StrongholdStatisticsData.__new__.__defaults__ = (
 None, None, None, None, None, None, [])

class StrongholdStatisticsData(_StrongholdStatisticsData, FieldsCheckerMixin):

    @simpleFormatter(backport.getIntegralFormat)
    def getElo10(self):
        return self.elo_10

    @simpleFormatter(backport.getIntegralFormat)
    def getElo8(self):
        return self.elo_8

    @simpleFormatter(backport.getIntegralFormat)
    def getElo6(self):
        return self.elo_6

    @simpleFormatter(backport.getIntegralFormat)
    def getSortiesIn28Days(self):
        return self.sorties_in_28_days

    @simpleFormatter(backport.getIntegralFormat)
    def getFortBattlesIn28Days(self):
        return self.fort_battles_in_28_days

    @simpleFormatter(int2roman)
    def getStrongholdLevel(self):
        return self.stronghold_level

    def getLeagues(self):
        return self.leagues

    def hasSorties(self):
        return self.sorties_in_28_days and self.sorties_in_28_days > 0

    def hasFortBattles(self):
        return self.fort_battles_in_28_days and self.fort_battles_in_28_days > 0


_AccountClanData = namedtuple(b'_AccountClanData', (b'account_id', b'joined_at', b'clan_id', b'role_bw_flag', b'role_name', b'in_clan_cooldown_till'))
_AccountClanData.__new__.__defaults__ = (
 0, _defDateTime, 0, 0, b'', _defDateTime)

class AccountClanData(_AccountClanData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'account_id',))
    def getDbID(self):
        return self.account_id

    def getClanCooldownTill(self):
        return time_utils.getTimestampFromUTC(self.in_clan_cooldown_till.timetuple())


_ClanMemberData = namedtuple(b'_ClanMemberData', b'account_id role_bw_flag clan_id joined_at ratings')
_ClanMemberData.__new__.__defaults__ = (
 0, 0, 0, _defDateTime, None)

class ClanMemberData(_ClanMemberData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'account_id',))
    def getDbID(self):
        return self.account_id

    @fmtUnavailableValue(fields=(b'role_bw_flag',))
    def getRole(self):
        return self.role_bw_flag

    @fmtUnavailableValue(fields=(b'role_bw_flag',))
    def getRoleString(self):
        return clans_fmts.getClanRoleString(self.role_bw_flag)

    @fmtUnavailableValue(fields=(b'role_bw_flag',))
    def getRoleIcon(self):
        return clans_fmts.getClanRoleIcon(self.role_bw_flag)

    def getClanDbID(self):
        return self.clan_id

    @fmtUnavailableValue(fields=(b'joined_at',))
    def getJoiningTime(self):
        return time_utils.getTimestampFromUTC(self.joined_at.timetuple())

    @fmtUnavailableValue(fields=(b'joined_at',))
    def getDaysInClan(self):
        return getTimeDeltaTillNow(self.getJoiningTime()) / ONE_DAY

    @fmtDelegat(path=b'ratings.getGlobalRating')
    def getGlobalRating(self):
        return self.ratings.getGlobalRating()

    @fmtDelegat(path=b'ratings.getBattlesCount')
    def getBattlesCount(self):
        return self.ratings.getBattlesCount()

    @fmtDelegat(path=b'ratings.getBattlesPerformanceAvg')
    def getBattlesPerformanceAvg(self):
        return self.ratings.getBattlesPerformanceAvg()

    @fmtDelegat(path=b'ratings.getXp')
    def getXp(self):
        return self.ratings.getXp()

    @fmtDelegat(path=b'ratings.getBattleXpAvg')
    def getBattleXpAvg(self):
        return self.ratings.getBattleXpAvg()


_AccountClanRatingsData = namedtuple(b'_AccountClanRatingsData', [
 120, 132, 133, 134, 
 135, 136])
_AccountClanRatingsData.__new__.__defaults__ = (0, 0, 0, 0, 0, 0)

class AccountClanRatingsData(_AccountClanRatingsData, FieldsCheckerMixin):

    def getAccountDbID(self):
        return self.account_id

    @fmtUnavailableValue(fields=(b'global_rating',))
    def getGlobalRating(self):
        return self.global_rating

    @fmtUnavailableValue(fields=(b'battles_count',))
    def getBattlesCount(self):
        return self.battles_count

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'battle_avg_xp', b'battles_count'))
    def getBattleXpAvg(self):
        if self.battles_count > 0:
            return self.battle_avg_xp
        raise ZeroDivisionError()
        return

    @fmtZeroDivisionValue()
    @fmtUnavailableValue(fields=(b'battle_avg_performance', b'battles_count'))
    def getBattlesPerformanceAvg(self):
        if self.battles_count > 0:
            return _toPercents(self.battle_avg_performance)
        raise ZeroDivisionError()
        return

    @fmtUnavailableValue(fields=(b'xp_amount',))
    def getXp(self):
        return self.xp_amount


_ClanProvinceData = namedtuple(b'_ClanProvinceData', [
 140, 141, 142, 143, 
 144, 145, 146, 147, 148, 149, 
 150, 151, 152, 
 153])
_ClanProvinceData.__new__.__defaults__ = (
 b'', 0, 0, False, 0, 0, b'', 0, b'', None, None, None, None, None)

class ClanProvinceData(_ClanProvinceData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'front_name_localized',))
    def getFrontLocalizedName(self):
        return self.front_name_localized

    @fmtDelegat(path=b'frontInfo.getMaxVehicleLevel')
    def getFrontLevel(self):
        return self.frontInfo.getMaxVehicleLevel()

    @fmtUnavailableValue(fields=(b'province_id_localized',))
    def getProvinceLocalizedName(self):
        return self.province_id_localized

    @fmtUnavailableValue(fields=(b'revenue',))
    def getRevenue(self):
        return self.revenue

    def isHqConnected(self):
        return self.hq_connected

    def getPrimeTime(self):
        return self.prime_time

    @fmtUnavailableValue(fields=(b'prime_time',))
    def getUserPrimeTime(self):
        return backport.getShortTimeFormat(self.prime_time.hour * time_utils.ONE_HOUR + self.prime_time.minute * time_utils.ONE_MINUTE)

    def getPeripheryID(self):
        return self.periphery

    @fmtUnavailableValue(fields=(b'periphery',))
    def getPeripheryName(self):
        periphery = g_preDefinedHosts.periphery(self.periphery)
        if periphery is not None:
            return periphery.name
        else:
            return b''

    @fmtUnavailableValue(fields=(b'game_map',))
    def getArenaName(self):
        return self.game_map

    @fmtUnavailableValue(fields=(b'arena_id',))
    def getArenaId(self):
        return self.arena_id

    @fmtUnavailableValue(fields=(b'turns_owned',))
    def getTurnsOwned(self):
        return self.turns_owned

    @fmtUnavailableValue(fields=(b'pillage_cooldown',))
    def getPillageCooldown(self):
        return self.pillage_cooldown

    @fmtUnavailableValue(fields=(b'pillage_end_datetime',))
    def getPillageEndDatetime(self):
        if self.pillage_end_datetime:
            return _getTimestamp(self.pillage_end_datetime)
        return 0


_GlobalMapFrontInfoData = namedtuple(b'_GlobalMapFrontInfoData', [
 b'front_name', b'min_vehicle_level', b'max_vehicle_level'])
_GlobalMapFrontInfoData.__new__.__defaults__ = tuple([0] * len(_ClanRatingsData._fields))

class GlobalMapFrontInfoData(_GlobalMapFrontInfoData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'front_name',))
    def getFrontName(self):
        return self.front_name

    @fmtUnavailableValue(fields=(b'min_vehicle_level',))
    def getMinVehicleLevel(self):
        return self.min_vehicle_level

    @fmtUnavailableValue(fields=(b'max_vehicle_level',))
    def getMaxVehicleLevel(self):
        return self.max_vehicle_level


_ClanSearchData = namedtuple(b'_ClanSearchData', [
 29, 30, 31, 37, 34, 32, 
 33, 36, 35, 162])
_ClanSearchData.__new__.__defaults__ = (
 b'', b'', b'', 0, 0, 0, _defDateTime, False, 0, ClanRatingsData())
_ClanSearchDataCriticalFields = (b'tag', b'name', b'members_count')

class ClanSearchData(_ClanSearchData, FieldsCheckerMixin):

    def getClanDbID(self):
        return self.clan_id

    @fmtUnavailableValue(fields=(b'name',))
    def getClanName(self):
        return passCensor(self.name)

    @fmtUnavailableValue(fields=(b'tag',))
    def getClanAbbrev(self):
        return passCensor(self.tag)

    @fmtUnavailableValue(fields=(b'motto',))
    def getClanMotto(self):
        return passCensor(self.motto)

    @fmtUnavailableValue(fields=(b'leader_id',))
    def getLeaderDbID(self):
        return self.leader_id

    @fmtUnavailableValue(fields=(b'tag', b'name'))
    def getClanFullName(self):
        return clans_fmts.getClanFullName(self.getClanName(), self.getClanAbbrev())

    @fmtUnavailableValue(fields=(b'members_count',))
    def getMembersCount(self):
        return self.members_count

    @fmtUnavailableValue(fields=(b'created_at',))
    def getCreationDate(self):
        return time_utils.getTimestampFromUTC(self.created_at.timetuple())

    def canAcceptsJoinRequests(self):
        return self.accepts_join_requests

    @fmtDelegat(path=b'clan_ratings_data.getEfficiency')
    def getPersonalRating(self):
        return self.clan_ratings_data.getEfficiency()

    @fmtDelegat(path=b'clan_ratings_data.getBattlesCountAvg')
    def getBattlesCount(self):
        return self.clan_ratings_data.getBattlesCountAvg()

    @fmtDelegat(path=b'clan_ratings_data.getWinsRatioAvg')
    def getBattleXpAvg(self):
        return self.clan_ratings_data.getWinsRatioAvg()

    @fmtDelegat(path=b'clan_ratings_data.getBattlesPerformanceAvg')
    def getBattlesPerformanceAvg(self):
        return self.clan_ratings_data.getBattlesPerformanceAvg()

    def isClanActive(self):
        return self.clan_ratings_data.isActive()

    def isValid(self):
        return super(ClanSearchData, self).isValid() and self.clan_ratings_data.isValid()

    def _getCriticalFields(self):
        return _ClanSearchDataCriticalFields


_ClanInviteData = namedtuple(b'_ClanInviteData', [
 120, 37, 166, 33, 
 167, 168, 169, 170, 171])
_ClanInviteData.__new__.__defaults__ = (
 0, 0, b'', _defDateTime, 0, 0, b'', _defDateTime, 0)

class ClanInviteData(_ClanInviteData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'id',))
    def getDbID(self):
        return self.id

    @fmtUnavailableValue(fields=(b'account_id',))
    def getAccountDbID(self):
        return self.account_id

    @fmtUnavailableValue(fields=(b'sender_id',))
    def getSenderDbID(self):
        return self.sender_id

    @fmtUnavailableValue(fields=(b'status_changer_id',))
    def getChangerDbID(self):
        return self.status_changer_id

    @fmtUnavailableValue(fields=(b'status_changer_id',))
    def getChangedBy(self):
        return self.status_changer_id

    @fmtUnavailableValue(fields=(b'clan_id',))
    def getClanDbID(self):
        return self.clan_id

    @fmtUnavailableValue(fields=(b'comment',))
    def getComment(self):
        return passCensor(str(self.comment))

    @fmtUnavailableValue(fields=(b'status',))
    def getStatus(self):
        return self.status

    @fmtUnavailableValue(fields=(b'created_at',))
    def getCreatedAt(self):
        return time_utils.getTimestampFromUTC(self.created_at.timetuple())

    @fmtUnavailableValue(fields=(b'updated_at',))
    def getUpdatedAt(self):
        return time_utils.getTimestampFromUTC(self.updated_at.timetuple())

    def isActive(self):
        return CLAN_INVITE_STATES.isActive(self.status)

    @classmethod
    def fromClanCreateInviteData(cls, data):
        return ClanInviteData(id=data.getDbID(), clan_id=data.getClanDbID(), account_id=data.getAccountDbID())

    @classmethod
    def fromClanInviteItem(cls, data):
        return ClanInviteData(id=data.getInviteId(), clan_id=data.getClanId(), account_id=data.getAccountDbID())

    @classmethod
    def fromClanApplicationItem(cls, data, clanDbID):
        return ClanInviteData(id=data.getApplicationID(), clan_id=clanDbID, account_id=data.getAccountID())


_ClanCreateInviteData = namedtuple(b'_ClanCreateInviteData', [
 b'clan_id', b'id', b'account_id'])
_ClanCreateInviteData.__new__.__defaults__ = (0, 0, 0)

class ClanCreateInviteData(_ClanCreateInviteData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'id',))
    def getDbID(self):
        return self.id

    @fmtUnavailableValue(fields=(b'account_id',))
    def getAccountDbID(self):
        return self.account_id

    @fmtUnavailableValue(fields=(b'clan_id',))
    def getClanDbID(self):
        return self.clan_id


_ClanADInviteData = namedtuple(b'_ClanADInviteData', [
 b'id', b'transaction_id', b'clan_id', b'account_id'])
_ClanADInviteData.__new__.__defaults__ = (0, 0, 0, 0)

class ClanADInviteData(_ClanADInviteData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'id',))
    def getDbID(self):
        return self.id

    @fmtUnavailableValue(fields=(b'transaction_id',))
    def getTransactionID(self):
        return self.transaction_id

    @fmtUnavailableValue(fields=(b'clan_id',))
    def getClanDbID(self):
        return self.clan_id

    @fmtUnavailableValue(fields=(b'account_id',))
    def getAccountDbID(self):
        return self.account_id


_StrongholdEventClanInfoData = namedtuple(b'_StrongholdEventClanInfoData', [
 b'primetime_start', b'primetime_end'])
_StrongholdEventClanInfoData.__new__.__defaults__ = (0, 0)

class StrongholdEventClanInfoData(_StrongholdEventClanInfoData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'primetime_start',))
    def getPrimeTimeStart(self):
        return self.primetime_start

    @fmtUnavailableValue(fields=(b'primetime_end',))
    def getPrimeTimeEnd(self):
        return self.primetime_end


_StrongholdEventConfig = namedtuple(b'_StrongholdEventConfig', [
 29, 187, 188, 189, 190, 
 191, 192, 193, 
 194, 195, 196, 197, 198])
_StrongholdEventConfig.__new__.__defaults__ = (
 b'', [], [], b'', b'', 0, 0, 0, 0, 0, 0, False, {})

class StrongholdEventConfig(_StrongholdEventConfig, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'sprint_config',))
    def getStartDate(self):
        return self.sprint_config.get(b'sprint_start_date', 0)

    @fmtUnavailableValue(fields=(b'sprint_config',))
    def getEndDate(self):
        return self.sprint_config.get(b'sprint_end_date', 0)

    @fmtUnavailableValue(fields=(b'sprint_config',))
    def getSprintType(self):
        return self.sprint_config.get(b'sprint_type', b'')

    @fmtUnavailableValue(fields=(b'sprint_config',))
    def getSprintNumber(self):
        return self.sprint_config.get(b'sprint_number', b'')


_StrongholdEventSettingsData = namedtuple(b'_StrongholdEventClanInfoData', [
 b'event_config'])
_StrongholdEventSettingsData.__new__.__defaults__ = (None,)

class StrongholdEventSettingsData(_StrongholdEventSettingsData, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'event_config',))
    def getEventConfig(self):
        return makeTupleByDict(StrongholdEventConfig, self.event_config)

    def getVisibleStartDate(self):
        return self.getEventConfig().getStartDate()

    def getVisibleEndDate(self):
        return self.getEventConfig().getEndDate()

    def getSprintType(self):
        return self.getEventConfig().getSprintType()

    def getSprintNumber(self):
        return self.getEventConfig().getSprintNumber()


class ClanInviteWrapper(object):

    def __init__(self, invite, account, accountName, sender, senderName, changerName):
        super(ClanInviteWrapper, self).__init__()
        self.__invite = invite or ClanInviteData()
        self.__account = account or AccountClanRatingsData()
        self.__sender = sender or AccountClanRatingsData()
        self.__accountName = accountName
        self.__senderName = senderName
        self.__changerName = changerName
        self.__statusCode = None
        return

    @property
    def status(self):
        return CLAN_INVITE_STATES_SORT_RULES.get(self.__invite.status, 0)

    @property
    def message(self):
        return self.__invite.comment

    @property
    def sent(self):
        return self.getCreatedAt()

    @property
    def createdAt(self):
        return self.getCreatedAt()

    @property
    def updatedAt(self):
        return self.getUpdatedAt()

    @property
    def userName(self):
        return self.getAccountName()

    @property
    def personalRating(self):
        return self.getPersonalRating()

    @property
    def battlesCount(self):
        return self.getBattlesCount()

    @property
    def avgXP(self):
        return self.getBattleXpAvg()

    @property
    def wins(self):
        return self.getBattlesPerformanceAvg()

    @property
    def invite(self):
        return self.__invite

    @property
    def account(self):
        return self.__account

    @property
    def sender(self):
        return self.__sender

    def getDbID(self):
        return self.__invite.getDbID()

    @fmtDelegat(path=b'invite.getClanDbID')
    def getClanDbID(self):
        return self.__invite.getClanDbID()

    @fmtDelegat(path=b'invite.getCreatedAt')
    def getCreatedAt(self):
        return self.__invite.getCreatedAt()

    @fmtDelegat(path=b'invite.getUpdatedAt')
    def getUpdatedAt(self):
        return self.__invite.getUpdatedAt()

    @fmtDelegat(path=b'invite.getAccountDbID')
    def getAccountDbID(self):
        return self.__invite.getAccountDbID()

    @fmtDelegat(path=b'invite.getSenderDbID')
    def getSenderDbID(self):
        return self.__invite.getSenderDbID()

    @fmtDelegat(path=b'invite.getChangedBy')
    def getChangedBy(self):
        return self.__invite.getChangedBy()

    @fmtDelegat(path=b'invite.getChangerDbID')
    def getChangerDbID(self):
        return self.__invite.getChangerDbID()

    @formatter(formatter=_formatString)
    def getAccountName(self):
        return self.__accountName

    @formatter(formatter=_formatString)
    def getSenderName(self):
        return self.__senderName

    @formatter(formatter=_formatString)
    def getChangerName(self):
        return self.__changerName

    @fmtDelegat(path=b'account.getGlobalRating')
    def getPersonalRating(self):
        return self.__account.getGlobalRating()

    @fmtDelegat(path=b'account.getBattlesCount')
    def getBattlesCount(self):
        return self.__account.getBattlesCount()

    @fmtDelegat(path=b'account.getBattleXpAvg')
    def getBattleXpAvg(self):
        return self.__account.getBattleXpAvg()

    @fmtDelegat(path=b'account.getBattlesPerformanceAvg')
    def getBattlesPerformanceAvg(self):
        return self.__account.getBattlesPerformanceAvg()

    @fmtDelegat(path=b'invite.getStatus')
    def getStatus(self):
        return self.__invite.getStatus()

    @fmtDelegat(path=b'invite.getComment')
    def getComment(self):
        return self.__invite.getComment()

    def getStatusCode(self):
        return self.__statusCode

    def setInvite(self, invite):
        self.__invite = invite
        return

    def setSender(self, sender):
        self.__sender = sender
        return

    def setSenderName(self, name):
        self.__senderName = name
        return

    def setChangerName(self, name):
        self.__changerName = name
        return

    def setUserName(self, name):
        self.__accountName = name
        return

    def setStatusCode(self, code):
        self.__statusCode = code
        return


class ClanPersonalInviteWrapper(object):

    def __init__(self, invite, clanInfo, clanRatings, senderName):
        super(ClanPersonalInviteWrapper, self).__init__()
        self.__invite = invite or ClanInviteData()
        self.__clanRatings = clanRatings or ClanRatingsData()
        self.__clanInfo = clanInfo or ClanExtInfoData()
        self.__senderName = senderName
        return

    @property
    def status(self):
        return CLAN_INVITE_STATES_SORT_RULES.get(self.__invite.status, 0)

    @property
    def message(self):
        return self.__invite.comment

    @property
    def createdAt(self):
        return self.getCreatedAt()

    @property
    def sent(self):
        return self.getCreatedAt()

    @property
    def updatedAt(self):
        return self.getUpdatedAt()

    @property
    def clanName(self):
        return self.getClanFullName()

    @property
    def personalRating(self):
        return self.getPersonalRating()

    @property
    def battlesCount(self):
        return self.getBattlesCount()

    @property
    def wins(self):
        return self.getBattleXpAvg()

    @property
    def avgXP(self):
        return self.getBattlesPerformanceAvg()

    @property
    def invite(self):
        return self.__invite

    @property
    def clanInfo(self):
        return self.__clanInfo

    @property
    def clanRatings(self):
        return self.__clanRatings

    def getDbID(self):
        return self.__invite.getDbID()

    @fmtDelegat(path=b'invite.getChangerDbID')
    def getChangerDbID(self):
        return self.__invite.getChangerDbID()

    @fmtDelegat(path=b'invite.getChangedBy')
    def getChangedBy(self):
        return self.__invite.getChangedBy()

    @fmtDelegat(path=b'invite.getStatus')
    def getStatus(self):
        return self.__invite.getStatus()

    @fmtDelegat(path=b'invite.getCreatedAt')
    def getCreatedAt(self):
        return self.__invite.getCreatedAt()

    @fmtDelegat(path=b'invite.getUpdatedAt')
    def getUpdatedAt(self):
        return self.__invite.getUpdatedAt()

    @fmtDelegat(path=b'invite.getComment')
    def getComment(self):
        return self.__invite.getComment()

    @fmtDelegat(path=b'clanInfo.getFullName')
    def getClanFullName(self):
        return self.__clanInfo.getFullName()

    @fmtDelegat(path=b'clanInfo.getClanName')
    def getClanName(self):
        return self.__clanInfo.getClanName()

    @fmtDelegat(path=b'clanInfo.getMotto')
    def getClanMotto(self):
        return self.__clanInfo.getMotto()

    @fmtDelegat(path=b'clanInfo.getTag')
    def getClanAbbrev(self):
        return self.__clanInfo.getTag()

    def getClanDbID(self):
        return self.__clanInfo.getDbID()

    def isClanActive(self):
        return self.__clanRatings.isActive()

    @fmtDelegat(path=b'clanRatings.getEfficiency')
    def getPersonalRating(self):
        return self.__clanRatings.getEfficiency()

    @fmtDelegat(path=b'clanRatings.getBattlesCountAvg')
    def getBattlesCount(self):
        return self.__clanRatings.getBattlesCountAvg()

    @fmtDelegat(path=b'clanRatings.getWinsRatioAvg')
    def getBattleXpAvg(self):
        return self.__clanRatings.getWinsRatioAvg()

    @fmtDelegat(path=b'clanRatings.getBattlesPerformanceAvg')
    def getBattlesPerformanceAvg(self):
        return self.__clanRatings.getBattlesPerformanceAvg()

    @fmtDelegat(path=b'clanInfo.getLeaderDbID')
    def getLeaderDbID(self):
        return self.__clanInfo.getLeaderDbID()

    @formatter(formatter=_formatString)
    def getSenderName(self):
        return self.__senderName

    def setInvite(self, invite):
        self.__invite = invite
        return

    def setSenderName(self, name):
        self.__senderName = name
        return


class ClanCommonData(object):

    def __init__(self, proxy):
        self._proxy = proxy
        return

    def getDbID(self):
        return self._proxy.getClanDbID()

    @fmtDelegat(path=b'_proxy.getClanName')
    def getName(self):
        return self._proxy.getClanName()

    @fmtDelegat(path=b'_proxy.getClanAbbrev')
    def getAbbrev(self):
        return self._proxy.getClanAbbrev()

    @fmtDelegat(path=b'_proxy.getClanMotto')
    def getMotto(self):
        return self._proxy.getClanMotto()

    @fmtDelegat(path=b'_proxy.getClanFullName')
    def getFullName(self):
        return self._proxy.getClanFullName()

    @fmtDelegat(path=b'_proxy.getPersonalRating')
    def getRating(self):
        return self._proxy.getPersonalRating()

    @fmtDelegat(path=b'_proxy.getBattlesCount')
    def getBattlesCount(self):
        return self._proxy.getBattlesCount()

    @fmtDelegat(path=b'_proxy.getBattleXpAvg')
    def getWinsRatio(self):
        return self._proxy.getBattleXpAvg()

    def isActive(self):
        return self._proxy.isClanActive()

    @fmtDelegat(path=b'_proxy.getBattlesPerformanceAvg')
    def getAvgExp(self):
        return self._proxy.getBattlesPerformanceAvg()

    @fmtDelegat(path=b'_proxy.getLeaderDbID')
    def getLeaderDbID(self):
        return self._proxy.getLeaderDbID()

    @classmethod
    def fromClanSearchData(cls, data):
        return ClanCommonData(data)

    @classmethod
    def fromClanPersonalInviteWrapper(cls, data):
        return ClanCommonData(data)


_ClanFavouriteAttrs = namedtuple(b'_ClanFavouriteAttrs', [
 37, 211, 212, 213, 
 214, 215])
_ClanFavouriteAttrs.__new__.__defaults__ = (0, None, None, None, 0, None)

class ClanFavouriteAttrs(_ClanFavouriteAttrs, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'favorite_arena_6',))
    def getFavouriteArena6(self):
        return self.favorite_arena_6

    @fmtUnavailableValue(fields=(b'favorite_arena_8',))
    def getFavouriteArena8(self):
        return self.favorite_arena_8

    @fmtUnavailableValue(fields=(b'favorite_arena_10',))
    def getFavouriteArena10(self):
        return self.favorite_arena_10

    @fmtUnavailableValue(fields=(b'favorite_primetime',))
    def getFavoritePrimetime(self):
        return self.favorite_primetime


_HofAttrs = namedtuple(b'_HofAttrs', [
 b'status', b'errors'])
_HofAttrs.__new__.__defaults__ = (
 None, {})

class HofAttrs(_HofAttrs, FieldsCheckerMixin):

    @fmtUnavailableValue(fields=(b'status',))
    def getStatus(self):
        return self.status

    @fmtUnavailableValue(fields=(b'errors',))
    def getErrors(self):
        return self.errors.keys()
