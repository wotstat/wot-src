from __future__ import absolute_import
from collections import defaultdict
from future.utils import viewitems, viewvalues
import nations
from constants import DOSSIER_TYPE
from dossiers2.common.DossierBlockBuilders import IBlockBuilderWithRecordsLayout
from dossiers2.custom import layouts as com_layouts, records
from dossiers2.custom.vehicle_layout import FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT
from dossiers2.ui import achievements
_AB = achievements.ACHIEVEMENT_BLOCK

def _7x7(achieveName):
    return (
     _AB.TEAM_7X7, achieveName)


def _total(achieveName):
    return (
     _AB.TOTAL, achieveName)


def _single(achieveName):
    return (
     _AB.SINGLE, achieveName)


def _single7x7(achieveName):
    return (
     _AB.SINGLE_7X7, achieveName)


def _fallout(achieveName):
    return (
     _AB.FALLOUT, achieveName)


def _epicBattle(achieveName):
    return (
     _AB.EPIC_BATTLE, achieveName)


_TANK_EXPERT_PREFIX = b'tankExpert'
_MECH_ENGINEER_PREFIX = b'mechanicEngineer'
_VEHICLE_COLLECTOR_PREFIX = b'collectorVehicle'
_HIST_BATTLEFIELD_POSTFIX = b'battlefield'
TANK_EXPERT_GROUP = [
 _total(_TANK_EXPERT_PREFIX)]
MECH_ENGINEER_GROUP = [_total(_MECH_ENGINEER_PREFIX)]
VEHICLE_COLLECTOR_GROUP = [_total(_VEHICLE_COLLECTOR_PREFIX)]
for _nID, _ in enumerate(nations.AVAILABLE_NAMES):
    TANK_EXPERT_GROUP.append(_total(b'%s%d' % (_TANK_EXPERT_PREFIX, _nID)))
    MECH_ENGINEER_GROUP.append(_total(b'%s%d' % (_MECH_ENGINEER_PREFIX, _nID)))
    VEHICLE_COLLECTOR_GROUP.append(_total(b'%s%d' % (_VEHICLE_COLLECTOR_PREFIX, _nID)))

HISTORY_BATTLEFIELD_GROUP = []
PERSONAL_MISSIONS_GROUP = [
 _single(b'firstMerit'), _total(b'readyForBattleLT'), _total(b'readyForBattleMT'),
 _total(b'readyForBattleSPG'), _total(b'readyForBattleATSPG'), _total(b'readyForBattleALL'),
 _total(b'tankwomenProgress'), _total(b'readyForBattleAllianceUSSR'), _total(b'readyForBattleAllianceGermany'),
 _total(b'readyForBattleAllianceUSA'), _total(b'readyForBattleAllianceFrance'), _single(b'newMeritPM2'),
 _single(b'mapboxSeason1'), _single(b'mapboxSeason2'), _single(b'mapboxSeason3'), _total(b'mapboxUniversal'),
 _total(b'mapboxClimateExpert'), _single(b'meritPM3'), _total(b'readyForBattleAssault'),
 _total(b'readyForBattleSniper'), _total(b'readyForBattleSupport'), _total(b'readyForBattleFossaAssault'),
 _total(b'readyForBattleFossaSniper'), _total(b'readyForBattleFossaSupport')]
CHRISTMAS_QUESTS_GROUP = [
 _single(b'xmasTreeBronze'), _single(b'xmasTreeSilver'), _single(b'xmasTreeGold')]
HE17_QUESTS_GROUP = [
 _single(b'HE17A1'), _single(b'HE17A2'), _single(b'HE17A3')]
NY18_QUESTS_GROUP = [
 _single(b'NY18A1'), _single(b'NY18A2'), _single(b'NY18A3')]
IGNORED_BY_BATTLE_RESULTS = [
 achievements.MARK_OF_MASTERY_RECORD, _single7x7(b'victoryMarch')]
for recordKey in records.RECORD_DB_IDS:
    if recordKey[1] in (b'maxXP', b'maxFrags', b'maxDamage', b'maxWinPoints', b'maxCoins'):
        IGNORED_BY_BATTLE_RESULTS.append(recordKey)

_COMMON_DOSSIERS_TYPE = 0
_EXCLUDED_ACHIEVES = defaultdict(tuple, {})
_CUSTOM_ACHIEVES = defaultdict(tuple, {})

def _getComLayoutRecordID(record):
    if record in TANK_EXPERT_GROUP:
        return (record[0], b'tankExpertStrg')
    if record in MECH_ENGINEER_GROUP:
        return (record[0], b'mechanicEngineerStrg')
    if record in VEHICLE_COLLECTOR_GROUP:
        return (record[0], b'collectorVehicleStrg')
    return record


def _buildComLayoutSet(dossierType, comLayout):
    global _EXCLUDED_ACHIEVES
    result = set()
    for layout in comLayout:
        if isinstance(layout, IBlockBuilderWithRecordsLayout):
            result.update(set((layout.name, r) for r in layout.recordsLayout))
        else:
            result.add(achievements.makeAchievesStorageName(layout.name))

    for dt in (_COMMON_DOSSIERS_TYPE, dossierType):
        result -= set(_EXCLUDED_ACHIEVES[dt])
        result |= set(_CUSTOM_ACHIEVES[dt])

    return result


ACCOUNT_ACHIEVEMENT_LAYOUT = []
VEHICLE_ACHIEVEMENT_LAYOUT = []
TANKMAN_ACHIEVEMENT_LAYOUT = []
FORT_ACHIEVEMENT_LAYOUT = []
RATED7x7_ACHIEVEMENT_LAYOUT = []
CLUB_ACHIEVEMENT_LAYOUT = []
_layoutsMap = {}

def getAchievementsLayout(dossierType):
    global _layoutsMap
    if dossierType in _layoutsMap:
        return _layoutsMap[dossierType][0]
    return tuple()


def isAchievementRegistered(record):
    return record in achievements.ACHIEVEMENTS


_MODE_ACHIEVEMENTS = defaultdict(set)

def getAchievementsByMode(mode):
    result = set()
    for modeID, achieves in viewitems(_MODE_ACHIEVEMENTS):
        if mode & modeID:
            result |= achieves

    return result


NEAREST_ACHIEVEMENTS = TANK_EXPERT_GROUP + MECH_ENGINEER_GROUP + VEHICLE_COLLECTOR_GROUP + [
 _total(b'mousebane'),
 _total(b'beasthunter'),
 _total(b'pattonValley'),
 _total(b'sinai'),
 _total(b'medalKnispel'),
 _total(b'medalCarius'),
 _total(b'medalAbrams'),
 _total(b'medalPoppel'),
 _total(b'medalKay'),
 _total(b'medalEkins'),
 _total(b'medalLeClerc'),
 _total(b'medalLavrinenko'),
 _total(b'readyForBattleLT'),
 _total(b'readyForBattleMT'),
 _total(b'readyForBattleHT'),
 _total(b'readyForBattleSPG'),
 _total(b'readyForBattleATSPG'),
 _7x7(b'geniusForWarMedal'),
 _7x7(b'wolfAmongSheepMedal'),
 _7x7(b'fightingReconnaissanceMedal'),
 _7x7(b'crucialShotMedal'),
 _7x7(b'forTacticalOperations'),
 _total(b'readyForBattleAllianceUSSR'),
 _total(b'readyForBattleAllianceGermany'),
 _total(b'readyForBattleAllianceUSA'),
 _total(b'readyForBattleAllianceFrance'),
 _total(b'rankedDivisionFighter'),
 _total(b'rankedStayingPower'),
 _total(b'readyForBattleAssault'),
 _total(b'readyForBattleSniper'),
 _total(b'readyForBattleSupport')]

def init():
    global HISTORY_BATTLEFIELD_GROUP
    global _EXCLUDED_ACHIEVES
    global _layoutsMap
    HISTORY_BATTLEFIELD_GROUP = [_r for _r in achievements.ACHIEVEMENTS if str(_r[1]).endswith(_HIST_BATTLEFIELD_POSTFIX)]
    _EXCLUDED_ACHIEVES = defaultdict(tuple, {_COMMON_DOSSIERS_TYPE: (
                             achievements.MARK_OF_MASTERY_RECORD, achievements.MARK_ON_GUN_RECORD), 
       (DOSSIER_TYPE.VEHICLE): (tuple(r for r, v in viewitems(achievements.ACHIEVEMENTS) if v[b'section'] == achievements.ACHIEVEMENT_TYPE.CLASS) + (_7x7(b'wolfAmongSheepMedal'), _7x7(b'geniusForWarMedal'), _7x7(b'fightingReconnaissanceMedal'), _7x7(b'crucialShotMedal'), _7x7(b'forTacticalOperations'), _7x7(b'promisingFighterMedal'), _7x7(b'heavyFireMedal'), _7x7(b'rangerMedal'), _7x7(b'guerrillaMedal'), _7x7(b'infiltratorMedal'), _7x7(b'sentinelMedal'), _7x7(b'prematureDetonationMedal'), _7x7(b'bruteForceMedal')) + tuple(map(_fallout, FALLOUT_ACHIEVEMENTS_BLOCK_LAYOUT)))})
    for _r in achievements.ACHIEVEMENTS:
        name = str(_r[1])
        if name.startswith(_TANK_EXPERT_PREFIX) and _r not in TANK_EXPERT_GROUP or name.startswith(_MECH_ENGINEER_PREFIX) and _r not in MECH_ENGINEER_GROUP or name.startswith(_VEHICLE_COLLECTOR_PREFIX) and _r not in VEHICLE_COLLECTOR_GROUP:
            _EXCLUDED_ACHIEVES[_COMMON_DOSSIERS_TYPE] += (_r,)

    _layoutsMap = {(DOSSIER_TYPE.ACCOUNT): (
                              ACCOUNT_ACHIEVEMENT_LAYOUT,
                              _buildComLayoutSet(DOSSIER_TYPE.ACCOUNT, com_layouts.accountDossierLayout)), 
       (DOSSIER_TYPE.VEHICLE): (
                              VEHICLE_ACHIEVEMENT_LAYOUT,
                              _buildComLayoutSet(DOSSIER_TYPE.VEHICLE, com_layouts.vehicleDossierLayout)), 
       (DOSSIER_TYPE.TANKMAN): (
                              TANKMAN_ACHIEVEMENT_LAYOUT,
                              _buildComLayoutSet(DOSSIER_TYPE.TANKMAN, com_layouts.tmanDossierLayout)), 
       (DOSSIER_TYPE.RATED7X7): (
                               RATED7x7_ACHIEVEMENT_LAYOUT,
                               _buildComLayoutSet(DOSSIER_TYPE.RATED7X7, com_layouts.rated7x7DossierLayout)), 
       (DOSSIER_TYPE.CLUB): (
                           CLUB_ACHIEVEMENT_LAYOUT,
                           _buildComLayoutSet(DOSSIER_TYPE.CLUB, com_layouts.clubDossierLayout))}
    for record, values in viewitems(achievements.ACHIEVEMENTS):
        _MODE_ACHIEVEMENTS[values[b'mode']].add(record)
        for uiLayout, comLayout in viewvalues(_layoutsMap):
            if _getComLayoutRecordID(record) in comLayout:
                uiLayout.append(record)

    return
