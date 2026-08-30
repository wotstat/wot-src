from collections import namedtuple
import typing
from frameworks.wulf import Array
from copy import deepcopy
from gui.impl.gen.view_models.views.lobby.postbattle.player_details_model import PlayerDetailsModel
from gui.impl.gen.view_models.views.lobby.postbattle.stats_one_value_item import StatsOneValueItem
from gui.impl.gen.view_models.views.lobby.postbattle.stats_two_values_item import StatsTwoValuesItem
from shared_utils import CONST_CONTAINER
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable.shared import VehicleSummarizeInfo

class _Copyable(object):

    def copy(self, **kwargs):
        other = deepcopy(self)
        for k, v in kwargs.iteritems():
            setattr(other, k, v)

        return other


class Field(_Copyable):
    __slots__ = (b'__stringID',)

    def __init__(self, stringID):
        self.__stringID = stringID
        return

    @property
    def stringID(self):
        return self.__stringID

    @stringID.setter
    def stringID(self, value):
        self.__stringID = value
        return

    def getFieldValues(self, *args):
        raise NotImplementedError
        return

    def _getRecord(self, *args):
        raise NotImplementedError
        return

    def _getValue(self, *args):
        raise NotImplementedError
        return


class _TeamStatsBlockIndexes(CONST_CONTAINER):
    EXP_SEGMENTS = 0
    SHOTS = 1
    DAMAGE_DEALT = 2
    HITS_RECEIVED = 3
    EXPLOSION_HITS = 4
    BLOCKED_DAMAGE = 5
    DAMAGE_TO_ALLIES = 6
    SPOTTED = 7
    DAMAGE_TO_ENEMIES = 8
    DAMAGE_ASSISTED = 9
    DAMAGE_ASSISTED_SELF = 10
    STUN_DURATION = 11
    DAMAGE_ASSISTED_STUN = 12
    DAMAGE_ASSISTED_STUN_SELF = 13
    STUN = 14
    BASE_CAPTURE = 15
    MILEAGE = 16
    START_TIME = 17
    BATTLE_DURATION = 18
    LIFETIME = 19


TeamStats = namedtuple(b'teamStats', (b'expSegments', b'shots', b'damageDealt', b'hitsReceived', b'other', b'time'))
TeamStatsExpSegments = namedtuple(b'TeamStatsExpSegments', (b'total', b'attack', b'assist', b'role'))
TeamStatsShots = namedtuple(b'shots', (b'shots', b'hitsPiercings', b'explosionHits'))
TeamStatsDamageDealt = namedtuple(b'damageDealt', (b'damageDealt', b'sniperDamageDealt'))
TeamStatsHitsReceived = namedtuple(b'hitsReceived', (b'directHitsReceived', b'piercingsReceived', b'noDamageHitsReceived'))
TeamStatsOther = namedtuple(b'other', (b'explosionHitsReceived', b'damageBlockedByArmor', b'damageToAllies', b'spotted', b'damageToEnemies', b'damageAssisted', b'damageAssistedSelf', b'stunDuration', b'damageAssistedStun', b'damageAssistedStunSelf', b'stunNum', b'baseCapture', b'mileage'))
TeamStatsTime = namedtuple(b'time', (b'arenaCreateTime', b'battleDuration', b'playerLifetime'))

class TeamStatsField(Field):
    __slots__ = (b'__blockIdx', b'__valueType', b'__hasTooltip', b'__model')

    def __init__(self, stringID, blockIdx, valueType, model, hasTooltip=False):
        super(TeamStatsField, self).__init__(stringID)
        self.__blockIdx = blockIdx
        self.__valueType = valueType
        self.__model = model
        self.__hasTooltip = hasTooltip
        return

    @property
    def valueType(self):
        return self.__valueType

    @property
    def blockIdx(self):
        return self.__blockIdx

    @property
    def model(self):
        return self.__model

    @property
    def hasTooltip(self):
        return self.__hasTooltip

    def _getRecord(self, *args):
        return

    def _getValue(self, *args):
        return


class TeamStatsOneValueField(TeamStatsField):
    __slots__ = (b'_valueID',)

    def __init__(self, stringID, blockIdx, valueType, model, valueID, hasTooltip=False):
        super(TeamStatsOneValueField, self).__init__(stringID, blockIdx, valueType, model, hasTooltip)
        self._valueID = valueID
        return

    def getFieldValues(self, playerInfo, results):
        return getattr(playerInfo, self._valueID)


class TeamStatsMultiValueField(TeamStatsField):
    __slots__ = (b'_valueIDs',)

    def __init__(self, stringID, blockIdx, valueType, model, valueIDs, hasTooltip=False):
        super(TeamStatsMultiValueField, self).__init__(stringID, blockIdx, valueType, model, hasTooltip)
        self._valueIDs = valueIDs
        return

    def getFieldValues(self, playerInfo, results):
        record = Array()
        record.reserve(2)
        for valueID in self._valueIDs:
            record.addNumber(getattr(playerInfo, valueID))

        return record


class TeamStatsArenaCreateTimeField(TeamStatsField):
    __slots__ = ()

    def getFieldValues(self, playerInfo, results):
        return results[b'common'][b'arenaCreateTime']


class TeamStatsBattleDurationField(TeamStatsField):
    __slots__ = ()

    def getFieldValues(self, playerInfo, results):
        return results[b'common'][b'duration']


class TeamStatsLifetimeField(TeamStatsField):
    __slots__ = ()

    def getFieldValues(self, playerInfo, results):
        return results[b'vehicles'][playerInfo.vehicleID][0][b'lifeTime']


def getTeamStats():
    return TeamStats(expSegments=_getExpSegments(), shots=_getTeamStatsShots(), damageDealt=_getTeamStatsDamageDealt(), hitsReceived=_getTeamStatsHitsReceived(), other=_getTeamStatsOther(), time=_getTeamStatsTime())


def _getExpSegments():
    return TeamStatsExpSegments(total=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.EXP_SEGMENTS, stringID=b'xpTotal', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'xp'), attack=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.EXP_SEGMENTS, stringID=b'xpForAttack', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'xpForAttack', hasTooltip=True), assist=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.EXP_SEGMENTS, stringID=b'xpForAssist', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'xpForAssist', hasTooltip=True), role=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.EXP_SEGMENTS, stringID=b'xpOther', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'xpOther', hasTooltip=True))


def _getTeamStatsShots():
    return TeamStatsShots(shots=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.SHOTS, stringID=b'shots', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'shots'), hitsPiercings=TeamStatsMultiValueField(blockIdx=_TeamStatsBlockIndexes.SHOTS, stringID=b'hitsPiercings', valueType=PlayerDetailsModel.INT_ARRAY, model=StatsTwoValuesItem, valueIDs=(b'directHits', b'piercings')), explosionHits=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.SHOTS, stringID=b'explosionHits', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'explosionHits'))


def _getTeamStatsDamageDealt():
    return TeamStatsDamageDealt(damageDealt=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_DEALT, stringID=b'damageDealt', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'damageDealt'), sniperDamageDealt=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_DEALT, stringID=b'sniperDamageDealt', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'sniperDamageDealt'))


def _getTeamStatsHitsReceived():
    return TeamStatsHitsReceived(directHitsReceived=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.HITS_RECEIVED, stringID=b'directHitsReceived', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'directHitsReceived'), piercingsReceived=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.HITS_RECEIVED, stringID=b'piercingsReceived', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'piercingsReceived'), noDamageHitsReceived=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.HITS_RECEIVED, stringID=b'noDamageDirectHitsReceived', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'noDamageDirectHitsReceived'))


def _getTeamStatsOther():
    return TeamStatsOther(explosionHitsReceived=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.EXPLOSION_HITS, stringID=b'explosionHitsReceived', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'explosionHitsReceived'), damageBlockedByArmor=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.BLOCKED_DAMAGE, stringID=b'damageBlockedByArmor', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'damageBlockedByArmor'), damageToAllies=TeamStatsMultiValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_TO_ALLIES, stringID=b'damageToAllies', valueType=PlayerDetailsModel.INT_ARRAY, model=StatsTwoValuesItem, valueIDs=(b'tkills', b'tdamageDealt')), spotted=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.SPOTTED, stringID=b'spotted', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'spotted'), damageToEnemies=TeamStatsMultiValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_TO_ENEMIES, stringID=b'damageToEnemies', valueType=PlayerDetailsModel.INT_ARRAY, model=StatsTwoValuesItem, valueIDs=(b'damaged', b'kills')), damageAssisted=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_ASSISTED, stringID=b'damageAssisted', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'damageAssisted'), damageAssistedSelf=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_ASSISTED_SELF, stringID=b'damageAssistedSelf', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'damageAssisted'), stunDuration=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.STUN_DURATION, stringID=b'stunDuration', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'stunDuration'), damageAssistedStun=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_ASSISTED_STUN, stringID=b'damageAssistedStun', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'damageAssistedStun'), damageAssistedStunSelf=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.DAMAGE_ASSISTED_STUN_SELF, stringID=b'damageAssistedStunSelf', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'damageAssistedStun'), stunNum=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.STUN, stringID=b'stunNum', valueType=PlayerDetailsModel.INTEGER, model=StatsOneValueItem, valueID=b'stunNum'), baseCapture=TeamStatsMultiValueField(blockIdx=_TeamStatsBlockIndexes.BASE_CAPTURE, stringID=b'baseCapture', valueType=PlayerDetailsModel.INT_ARRAY, model=StatsTwoValuesItem, valueIDs=(b'capturePoints', b'droppedCapturePoints')), mileage=TeamStatsOneValueField(blockIdx=_TeamStatsBlockIndexes.MILEAGE, stringID=b'mileage', valueType=PlayerDetailsModel.MILEAGE, model=StatsOneValueItem, valueID=b'mileage'))


def _getTeamStatsTime():
    return TeamStatsTime(arenaCreateTime=TeamStatsArenaCreateTimeField(blockIdx=_TeamStatsBlockIndexes.START_TIME, stringID=b'arenaCreateTime', valueType=PlayerDetailsModel.LOCAL_TIME, model=StatsOneValueItem), battleDuration=TeamStatsBattleDurationField(blockIdx=_TeamStatsBlockIndexes.BATTLE_DURATION, stringID=b'duration', valueType=PlayerDetailsModel.BATTLE_DURATION, model=StatsOneValueItem), playerLifetime=TeamStatsLifetimeField(blockIdx=_TeamStatsBlockIndexes.LIFETIME, stringID=b'lifetime', valueType=PlayerDetailsModel.LIFETIME, model=StatsOneValueItem))
