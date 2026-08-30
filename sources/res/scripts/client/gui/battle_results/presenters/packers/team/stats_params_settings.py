from collections import namedtuple
from gui.battle_results.pbs_helpers.team_stats_helpers import getStatsParamValue, getMileageValue, isPersonalBattleResult, isNotPersonalBattleResult, hasStunEfficiency, hasArtilleryStrike
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.simple_stats_parameter_model import RegularParamType, ValueType
_Parameter = namedtuple(b'_Parameter', (b'path', b'stringId', b'fields', b'valueType', b'conditions', b'extractor', b'details'))
_STR_PATH = R.strings.battle_results.team.stats.parameter
REGULAR_PARAMETERS = {(RegularParamType.SHOTS): (_Parameter(path=_STR_PATH.shots, stringId=b'shots', fields=(b'shots',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=(
                            RegularParamType.HITS, RegularParamType.EXPLOSIONHITS))), 
   (RegularParamType.HITS): (_Parameter(path=_STR_PATH.hits, stringId=b'hits', fields=(b'directEnemyHits', b'piercingEnemyHits'), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.EXPLOSIONHITS): (_Parameter(path=_STR_PATH.explosionHits, stringId=b'explosionHits', fields=(b'explosionHits',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.DAMAGEDEALT): (_Parameter(path=_STR_PATH.damageDealt, stringId=b'damageDealt', fields=(b'damageDealt',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=(
                                  RegularParamType.SNIPERDAMAGEDEALT, RegularParamType.ARTILLERYSTRIKE))), 
   (RegularParamType.SNIPERDAMAGEDEALT): (_Parameter(path=_STR_PATH.sniperDamageDealt, stringId=b'sniperDamageDealt', fields=(b'sniperDamageDealt',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.ARTILLERYSTRIKE): (_Parameter(path=_STR_PATH.artilleryFortEquipDamageDealt, stringId=b'artilleryFortEquipDamageDealt', fields=(b'artilleryFortEquipDamageDealt',), valueType=ValueType.INTEGER, conditions=(
                                      hasArtilleryStrike,), extractor=getStatsParamValue, details=())), 
   (RegularParamType.DIRECTHITSRECEIVED): (_Parameter(path=_STR_PATH.directHitsReceived, stringId=b'directHitsReceived', fields=(b'directHitsReceived',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=(
                                         RegularParamType.PIERCINGSRECEIVED, RegularParamType.NODAMAGEDIRECTHITSRECEIVED))), 
   (RegularParamType.PIERCINGSRECEIVED): (_Parameter(path=_STR_PATH.piercingsReceived, stringId=b'piercingsReceived', fields=(b'piercingsReceived',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.NODAMAGEDIRECTHITSRECEIVED): (_Parameter(path=_STR_PATH.noDamageDirectHitsReceived, stringId=b'noDamageDirectHitsReceived', fields=(b'noDamageDirectHitsReceived',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.EXPLOSIONHITSRECEIVED): (_Parameter(path=_STR_PATH.explosionHitsReceived, stringId=b'explosionHitsReceived', fields=(b'explosionHitsReceived',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.DAMAGEBLOCKEDBYARMOR): (_Parameter(path=_STR_PATH.damageBlockedByArmor, stringId=b'damageBlockedByArmor', fields=(b'damageBlockedByArmor',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.TEAMHITSDAMAGE): (_Parameter(path=_STR_PATH.teamHitsDamage, stringId=b'teamHitsDamage', fields=(b'tkills', b'tdamageDealt'), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.SPOTTED): (_Parameter(path=_STR_PATH.spotted, stringId=b'spotted', fields=(b'spotted',), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.DAMAGEDKILLED): (_Parameter(path=_STR_PATH.damagedKilled, stringId=b'damagedKilled', fields=(b'damaged', b'kills'), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.DAMAGEASSISTED): (_Parameter(path=_STR_PATH.damageAssisted, stringId=b'damageAssisted', fields=(b'damageAssisted',), valueType=ValueType.INTEGER, conditions=(
                                     isNotPersonalBattleResult,), extractor=getStatsParamValue, details=())), 
   (RegularParamType.DAMAGEASSISTEDSELF): (_Parameter(path=_STR_PATH.damageAssistedSelf, stringId=b'damageAssistedSelf', fields=(b'damageAssisted',), valueType=ValueType.INTEGER, conditions=(
                                         isPersonalBattleResult,), extractor=getStatsParamValue, details=())), 
   (RegularParamType.STUNDURATION): (_Parameter(path=_STR_PATH.stunDuration, stringId=b'stunDuration', fields=(b'stunDuration',), valueType=ValueType.FLOAT, conditions=(
                                   hasStunEfficiency,), extractor=getStatsParamValue, details=())), 
   (RegularParamType.DAMAGEASSISTEDSTUN): (_Parameter(path=_STR_PATH.damageAssistedStun, stringId=b'damageAssistedStun', fields=(b'damageAssistedStun',), valueType=ValueType.INTEGER, conditions=(
                                         hasStunEfficiency, isNotPersonalBattleResult), extractor=getStatsParamValue, details=())), 
   (RegularParamType.DAMAGEASSISTEDSTUNSELF): (_Parameter(path=_STR_PATH.damageAssistedStunSelf, stringId=b'damageAssistedStunSelf', fields=(b'damageAssistedStun',), valueType=ValueType.INTEGER, conditions=(
                                             hasStunEfficiency, isPersonalBattleResult), extractor=getStatsParamValue, details=())), 
   (RegularParamType.STUNNUM): (_Parameter(path=_STR_PATH.stunNum, stringId=b'stunNum', fields=(b'stunNum',), valueType=ValueType.INTEGER, conditions=(
                              hasStunEfficiency,), extractor=getStatsParamValue, details=())), 
   (RegularParamType.CAPTUREPOINTSVAL): (_Parameter(path=_STR_PATH.capturePointsVal, stringId=b'capturePointsVal', fields=(b'capturePoints', b'droppedCapturePoints'), valueType=ValueType.INTEGER, conditions=None, extractor=getStatsParamValue, details=())), 
   (RegularParamType.MILEAGE): (_Parameter(path=_STR_PATH.mileage, stringId=b'mileage', fields=(b'mileage',), valueType=ValueType.FLOAT, conditions=None, extractor=getMileageValue, details=()))}
