import sys, struct, nations
from functools import partial
from comp7_helpers import archiveSeasonsGriffin, archiveMaxSeasonsGriffin, archiveCutSeasonsGriffin, addSeasonRecord, archiveSeasonsWolf, archiveMaxSeasonsWolf, archiveCutSeasonsWolf
from dossiers2.custom.helpers import getTankExpertRequirements
from dossiers2.common.updater_utils import getNewStaticSizeBlockValues, getStaticSizeBlockRecordValues
from dossiers2.common.updater_utils import getDictBlockRecordValues, updateDictRecords
from dossiers2.common.updater_utils import getNewBinarySetBlockValues, setStaticSizeBlockRecordValues
from dossiers2.common.updater_utils import addBlock, removeBlock, addRecords, removeRecords, setVersion
from dossiers2.common.updater_utils import getHeader, getBlockSize, getBlockCompDescr, setBlockCompDescr
from dossiers2.common.updater_utils import getBinarySetValue, updateStaticSizeBlockRecords, updateBinaryBlockRecords
import dossiers2.custom.tankmen_dossier1_updater
from dossiers2.custom.config import RECORD_CONFIGS
from VersionUpdater import VersionUpdaterBase
from serialization import ComponentBinSerializer
from wotdecorators import singleton
from debug_utils import LOG_DEBUG_DEV
ACCOUNT_DOSSIER_VERSION = 161
ACCOUNT_DOSSIER_UPDATE_FUNCTION_TEMPLATE = b'__updateFromAccountDossier%d'
VEHICLE_DOSSIER_VERSION = 117
VEHICLE_DOSSIER_UPDATE_FUNCTION_TEMPLATE = b'__updateFromVehicleDossier%d'
TANKMAN_DOSSIER_VERSION = 67
TANKMAN_DOSSIER_UPDATE_FUNCTION_TEMPLATE = b'__updateFromTankmanDossier%d'
CLAN_DOSSIER_VERSION = 1
CLAN_DOSSIER_UPDATE_FUNCTION_TEMPLATE = b'__updateFromClanDossier%d'
RATED7X7_DOSSIER_VERSION = 1
RATED7X7_DOSSIER_UPDATE_FUNCTION_TEMPLATE = b'__updateFromRated7x7Dossier%d'
CLUB_DOSSIER_VERSION = 2
CLUB_DOSSIER_UPDATE_FUNCTION_TEMPLATE = b'__updateFromClubDossier%d'
VEHICLE_DOSSIER_MINIMAL_SUPPORTED_VERSION = 64

def __updateFromAccountDossier64(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11]
    a15x15packing = {b'creationTime': (0, b'I'), b'battleLifeTime': (8, b'I'), b'lastBattleTime': (4, b'I')}
    a15x15_2packing = {b'mileage': (38, b'I'), b'treesCut': (36, b'H')}
    achievementsPacking = {b'maxXPVehicle': (136, b'I'), b'maxFrags': (0, b'B'), b'maxXP': (1, b'H'), b'winAndSurvived': (3, b'I'), 
       b'maxFragsVehicle': (140, b'I'), b'frags8p': (7, b'I')}
    totalLayout = [
     59, 60, 61, 
     62, 63]
    max15x15Layout = [
     64, 65, 66, 
     67, 68, 69]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    totalDefaults = getStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing)
    totalDefaults.update(getStaticSizeBlockRecordValues(updateCtx, b'a15x15_2', a15x15_2packing))
    if bool(totalDefaults):
        blockFormat, blockValues = getNewStaticSizeBlockValues(totalLayout, totalDefaults)
    else:
        blockFormat, blockValues = (b'', None)
    addBlock(updateCtx, b'total', blockFormat, blockValues)
    removeRecords(updateCtx, b'a15x15', a15x15packing)
    removeRecords(updateCtx, b'a15x15_2', a15x15_2packing)
    addBlock(updateCtx, b'a7x7Cut')
    achievementsValues = getStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking)
    addRecords(updateCtx, b'a15x15', [
     (b'winAndSurvived', b'I'), (b'frags8p', b'I')], achievementsValues)
    addRecords(updateCtx, b'a7x7', [
     (b'winAndSurvived', b'I'), (b'frags8p', b'I')], {})
    if bool(achievementsValues):
        blockFormat, blockValues = getNewStaticSizeBlockValues(max15x15Layout, achievementsValues)
    else:
        blockFormat, blockValues = (b'', None)
    addBlock(updateCtx, b'max15x15', blockFormat, blockValues)
    addBlock(updateCtx, b'max7x7')
    removeRecords(updateCtx, b'achievements', achievementsPacking)
    setVersion(updateCtx, 65)
    return (65, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier65(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'achievements', [(b'sniper2', b'H'), (b'mainGun', b'H')], {})
    setVersion(updateCtx, 66)
    return (66, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier66(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    blockFormat = b'<' + b'HHHHHHHH'
    blockValues = [0] * 8
    addBlock(updateCtx, b'achievements7x7', blockFormat, blockValues)
    setVersion(updateCtx, 67)
    return (67, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier67(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'achievements7x7', [(b'tacticalBreakthrough', b'B')], {b'tacticalBreakthrough': 0})
    setVersion(updateCtx, 68)
    return (68, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier68(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'battleCitizen', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 69)
    return (69, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier69(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordFormats = [
     (b'potentialDamageReceived', b'I'), (b'damageBlockedByArmor', b'I')]
    addRecords(updateCtx, b'a15x15_2', recordFormats, {})
    addRecords(updateCtx, b'company2', recordFormats, {})
    addRecords(updateCtx, b'clan2', recordFormats, {})
    addRecords(updateCtx, b'a7x7', recordFormats, {})
    setVersion(updateCtx, 70)
    return (70, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier70(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordFormats = [
     (b'battlesCountBefore9_0', b'I')]
    a15x15packing = {b'battlesCount': (4, b'I')}
    a15x15defaults = getStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing)
    addRecords(updateCtx, b'a15x15', recordFormats, {b'battlesCountBefore9_0': (a15x15defaults.get(b'battlesCount', 0))})
    companyPacking = {b'battlesCount': (4, b'I')}
    companyDefaults = getStaticSizeBlockRecordValues(updateCtx, b'company', companyPacking)
    addRecords(updateCtx, b'company', recordFormats, {b'battlesCountBefore9_0': (companyDefaults.get(b'battlesCount', 0))})
    clanPacking = {b'battlesCount': (4, b'I')}
    clanDefaults = getStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking)
    addRecords(updateCtx, b'clan', recordFormats, {b'battlesCountBefore9_0': (clanDefaults.get(b'battlesCount', 0))})
    a7x7packing = {b'battlesCount': (4, b'I')}
    a7x7defaults = getStaticSizeBlockRecordValues(updateCtx, b'a7x7', a7x7packing)
    addRecords(updateCtx, b'a7x7', recordFormats, {b'battlesCountBefore9_0': (a7x7defaults.get(b'battlesCount', 0))})
    setVersion(updateCtx, 71)
    return (71, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier71(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    setVersion(updateCtx, 72)
    return (72, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier72(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'historical')
    addBlock(updateCtx, b'maxHistorical')
    addBlock(updateCtx, b'historicalAchievements')
    addBlock(updateCtx, b'historicalCut')
    setVersion(updateCtx, 73)
    return (73, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier73(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     36, 
     37, 
     38, 
     39, 
     40, 
     41, 
     42]
    defaultValues = {b'godOfWar': 0, 
       b'fightingReconnaissance': 0, 
       b'fightingReconnaissanceMedal': 0, 
       b'willToWinSpirit': 0, 
       b'crucialShot': 0, 
       b'crucialShotMedal': 0, 
       b'forTacticalOperations': 0}
    addRecords(updateCtx, b'achievements7x7', formats, defaultValues)
    setVersion(updateCtx, 74)
    return (74, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier74(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     32, 
     33, 
     34, 
     35, 
     36]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 75)
    return (75, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier75(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'uniqueAchievements')
    setVersion(updateCtx, 76)
    return (76, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier76(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'fortBattles')
    addBlock(updateCtx, b'maxFortBattles')
    addBlock(updateCtx, b'fortBattlesCut')
    addBlock(updateCtx, b'fortSorties')
    addBlock(updateCtx, b'maxFortSorties')
    setVersion(updateCtx, 77)
    return (77, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier77(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 
     22, 23, 24, 
     25, 26]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'fortSortiesCut')
    addBlock(updateCtx, b'fortBattlesInClan')
    addBlock(updateCtx, b'maxFortBattlesInClan')
    addBlock(updateCtx, b'fortSortiesInClan')
    addBlock(updateCtx, b'maxFortSortiesInClan')
    addBlock(updateCtx, b'fortMisc')
    addBlock(updateCtx, b'fortMiscInClan')
    addBlock(updateCtx, b'fortAchievements')
    setVersion(updateCtx, 78)
    return (78, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier78(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 
     22, 23, 24, 
     25, 
     26, 27, 
     28, 29, 
     30, 31, 
     32, 33, 
     34]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     53, 
     54, 
     55, 
     56, 
     57, 
     58, 
     59, 
     60, 
     61, 
     62, 
     63]
    defaultValues = {b'promisingFighter': 0, 
       b'promisingFighterMedal': 0, 
       b'heavyFire': 0, 
       b'heavyFireMedal': 0, 
       b'ranger': 0, 
       b'rangerMedal': 0, 
       b'fireAndSteel': 0, 
       b'fireAndSteelMedal': 0, 
       b'pyromaniac': 0, 
       b'pyromaniacMedal': 0, 
       b'noMansLand': 0}
    addRecords(updateCtx, b'achievements7x7', formats, defaultValues)
    setVersion(updateCtx, 79)
    return (79, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier79(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 
     22, 23, 24, 
     25, 
     26, 27, 
     28, 29, 
     30, 31, 
     32, 33, 
     34]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'WFC2014', b'B'),
     (b'WFC2014WinSeries', b'B'),
     (b'maxWFC2014WinSeries', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 80)
    return (80, updateCtx[b'dossierCompDescr'])


def _count7x7awards(ctx):
    packing = {b'crucialShotMedal': (27, b'H'), 
       b'noMansLand': (50, b'H'), 
       b'fightingReconnaissanceMedal': (21, b'H'), b'godOfWar': (17, b'H'), 
       b'armoredFist': (14, b'H'), b'fireAndSteelMedal': (44, b'H'), b'forTacticalOperations': (29, b'B'), 
       b'kingOfTheHill': (8, b'H'), b'wolfAmongSheepMedal': (2, b'H'), b'willToWinSpirit': (23, b'H'), 
       b'heavyFireMedal': (36, b'H'), b'maxTacticalBreakthroughSeries': (12, b'H'), b'promisingFighterMedal': (32, b'H'), 
       b'geniusForWarMedal': (6, b'H'), b'rangerMedal': (40, b'H'), b'pyromaniacMedal': (48, b'H')}
    awardNum = 0
    values = getStaticSizeBlockRecordValues(ctx, b'achievements7x7', packing)
    if values and values[b'maxTacticalBreakthroughSeries'] >= 3:
        awardNum += 1
        del values[b'maxTacticalBreakthroughSeries']
    if values and values[b'forTacticalOperations'] > 0:
        awardNum += 5 - values[b'forTacticalOperations']
        del values[b'forTacticalOperations']
    for val in values.itervalues():
        awardNum += val

    return awardNum


def __updateFromAccountDossier80(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 
     22, 23, 24, 
     25, 
     26, 27, 
     28, 29, 
     30, 31, 
     32, 33, 
     34]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    awardCount = _count7x7awards(updateCtx)
    formats = [
     56, 
     57, 
     58, 
     59, 
     60, 
     61, 
     62, 
     63, 
     64, 
     65, 
     66, 
     67]
    defaultValues = {b'guerrilla': 0, 
       b'guerrillaMedal': 0, 
       b'infiltrator': 0, 
       b'infiltratorMedal': 0, 
       b'sentinel': 0, 
       b'sentinelMedal': 0, 
       b'prematureDetonation': 0, 
       b'prematureDetonationMedal': 0, 
       b'bruteForce': 0, 
       b'bruteForceMedal': 0, 
       b'awardCount': awardCount, 
       b'battleTested': 0}
    addRecords(updateCtx, b'achievements7x7', formats, defaultValues)
    setVersion(updateCtx, 81)
    return (81, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier81(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 
     22, 23, 24, 
     25, 
     26, 27, 
     28, 29, 
     30, 31, 
     32, 33, 
     34]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    layout = [
     40, 
     41, 
     42, 
     43, 
     44, 
     45, 
     46, 
     47]
    values = {}
    achievementsPacking = {b'titleSniper': (88, b'B'), 
       b'invincible': (89, b'B'), 
       b'diehard': (90, b'B'), 
       b'handOfDeath': (93, b'B'), 
       b'armorPiercer': (94, b'B'), 
       b'battleCitizen': (131, b'B'), 
       b'WFC2014': (142, b'B')}
    values.update(getStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking))
    achievements7x7Packing = {b'tacticalBreakthrough': (16, b'B')}
    values.update(getStaticSizeBlockRecordValues(updateCtx, b'achievements7x7', achievements7x7Packing))
    blockFormat, blockValues = getNewBinarySetBlockValues(layout, values)
    addBlock(updateCtx, b'singleAchievements', blockFormat, blockValues)
    removeRecords(updateCtx, b'achievements', achievementsPacking)
    removeRecords(updateCtx, b'achievements7x7', achievements7x7Packing)
    setVersion(updateCtx, 82)
    return (82, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier82(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 
     22, 23, 24, 
     25, 
     26, 27, 
     28, 29, 
     30, 31, 
     32, 33, 
     34, 35]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    blockLayout = [
     (b'medalRotmistrov', b'B')]
    blockFormat, blockValues = getNewStaticSizeBlockValues(blockLayout, {b'medalRotmistrov': 0})
    addBlock(updateCtx, b'clanAchievements', blockFormat, blockValues)
    setVersion(updateCtx, 83)
    return (83, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier83(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    a15x15packing = {b'battlesCountBefore9_0': (68, b'I'), b'battlesCountBefore8_8': (56, b'I')}
    values = getStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing)
    if values and values[b'battlesCountBefore8_8'] > 0 and values[b'battlesCountBefore9_0'] == 0:
        values[b'battlesCountBefore9_0'] = values[b'battlesCountBefore8_8']
        setStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing, values)
    clanPacking = {b'battlesCountBefore9_0': (60, b'I'), b'battlesCountBefore8_9': (56, b'I')}
    values = getStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking)
    if values and values[b'battlesCountBefore8_9'] > 0 and values[b'battlesCountBefore9_0'] == 0:
        values[b'battlesCountBefore9_0'] = values[b'battlesCountBefore8_9']
        setStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking, values)
    companyPacking = {b'battlesCountBefore9_0': (60, b'I'), b'battlesCountBefore8_9': (56, b'I')}
    values = getStaticSizeBlockRecordValues(updateCtx, b'company', companyPacking)
    if values and values[b'battlesCountBefore8_9'] > 0 and values[b'battlesCountBefore9_0'] == 0:
        values[b'battlesCountBefore9_0'] = values[b'battlesCountBefore8_9']
        setStaticSizeBlockRecordValues(updateCtx, b'company', companyPacking, values)
    setVersion(updateCtx, 84)
    return (84, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier84(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordFormats = [
     56, 
     57, 
     58, 
     59, 
     60, 
     61, 
     62, 
     63, 
     64, 
     65, 
     66, 
     67]
    addRecords(updateCtx, b'achievements', recordFormats, {})
    setVersion(updateCtx, 85)
    return (85, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier85(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'wins', b'H'),
     (b'capturedBasesInAttack', b'H'),
     (b'capturedBasesInDefence', b'H')]
    addRecords(updateCtx, b'fortAchievements', formats, {})
    setVersion(updateCtx, 86)
    return (86, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier86(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'deathTrackWinSeries', b'B'),
     (b'maxDeathTrackWinSeries', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 87)
    return (87, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier87(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     51, 
     52, 
     53, 
     54, 
     55, 
     56, 
     57]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 88)
    return (88, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier88(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'rated7x7')
    addBlock(updateCtx, b'maxRated7x7')
    setVersion(updateCtx, 89)
    return (89, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier89(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'achievementsRated7x7')
    setVersion(updateCtx, 90)
    return (90, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier90(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'rated7x7Cut')
    setVersion(updateCtx, 91)
    return (91, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier91(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'achievements', [(b'testartilleryman', b'H')], {})
    setVersion(updateCtx, 92)
    return (92, updateCtx[b'dossierCompDescr'])


def _countBattleHeroesBasedOn7x7Medals(ctx):
    packing = {b'wolfAmongSheepMedal': (2, b'H'), b'geniusForWarMedal': (6, b'H')}
    awardNum = 0
    values = getStaticSizeBlockRecordValues(ctx, b'achievements7x7', packing)
    for val in values.itervalues():
        awardNum += val

    return awardNum


def _medalKayClass(battleHeroes):
    medalKayCfg = (1, 10, 100, 1000)
    maxMedalClass = len(medalKayCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if battleHeroes >= medalKayCfg[maxMedalClass - medalClass]:
            break
    else:
        medalClass = 0

    return medalClass


def __updateFromAccountDossier92(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    battleHeroes7x7Count = _countBattleHeroesBasedOn7x7Medals(updateCtx)
    if battleHeroes7x7Count > 0:
        achievementsPacking = {b'battleHeroes': (20, b'H'), b'medalKay': (38, b'B')}
        values = getStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking)
        if values:
            values[b'battleHeroes'] += battleHeroes7x7Count
            values[b'medalKay'] = _medalKayClass(values[b'battleHeroes'])
            setStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking, values)
    setVersion(updateCtx, 93)
    return (93, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier93(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'globalMapCommon')
    addBlock(updateCtx, b'globalMapMiddle')
    addBlock(updateCtx, b'globalMapChampion')
    addBlock(updateCtx, b'globalMapAbsolute')
    setVersion(updateCtx, 94)
    return (94, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier94(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40, 
     41, 42, 43, 44]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    removeBlock(updateCtx, b'globalMapCommon')
    recordFormats = [
     (b'xpBefore8_9', b'I'),
     (b'battlesCountBefore8_9', b'I'),
     (b'battlesCountBefore9_0', b'I')]
    addRecords(updateCtx, b'globalMapMiddle', recordFormats, {})
    addRecords(updateCtx, b'globalMapChampion', recordFormats, {})
    addRecords(updateCtx, b'globalMapAbsolute', recordFormats, {})
    setVersion(updateCtx, 95)
    return (95, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier95(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40, 
     41, 42, 43]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'fortSortiesInClan', [
     58, 59, 60, 
     61, 62, 63, 64], {})
    setVersion(updateCtx, 96)
    return (96, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier96(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40, 
     41, 42, 43]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'maxGlobalMapMiddle')
    addBlock(updateCtx, b'maxGlobalMapChampion')
    addBlock(updateCtx, b'maxGlobalMapAbsolute')
    setVersion(updateCtx, 97)
    return (97, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier97(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40, 
     41, 42, 43, 
     44, 
     45, 46]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'globalMapCommonCut')
    setVersion(updateCtx, 98)
    return (98, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier98(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17, 18, 
     19, 20, 21, 22, 
     23, 24, 
     25, 26, 27, 
     28, 29, 30, 31, 
     32, 33, 34, 
     35, 36, 
     37, 38, 39, 40, 
     41, 42, 43, 
     44, 
     45, 46, 47]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'fallout')
    addBlock(updateCtx, b'falloutCut')
    addBlock(updateCtx, b'maxFallout')
    setVersion(updateCtx, 99)
    return (99, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier99(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39, 
     40, 
     41, 
     42, 
     43, 
     44, 
     45, 
     46, 
     47, 
     48, 
     49, 
     50]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'falloutAchievements')
    setVersion(updateCtx, 100)
    return (100, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier100(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 
     39, 40, 41, 42, 43, 
     44, 
     45, 46, 47, 48, 
     49, 50, 51]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'EFC2016WinSeries', b'H'),
     (b'maxEFC2016WinSeries', b'H'),
     (b'EFC2016Goleador', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 101)
    return (101, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier101(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 
     39, 40, 41, 42, 43, 
     44, 
     45, 46, 47, 48, 
     49, 50, 51]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'markIBomberman', b'H'),
     (b'markIRepairer', b'H'),
     (b'markI100Years', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 102)
    return (102, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier102(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 
     39, 40, 41, 42, 43, 
     44, 
     45, 46, 47, 48, 
     49, 50, 51]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    modes = (b'a15x15_2', b'clan2', b'company2', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'rated7x7', b'fallout', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute')
    for mode in modes:
        recordsFormat = [(b'battlesOnStunningVehicles', b'I'),
         (b'stunNum', b'I'),
         (b'damageAssistedStun', b'I')]
        addRecords(updateCtx, mode, recordsFormat, {})

    setVersion(updateCtx, 103)
    return (103, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier103(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 
     39, 40, 41, 42, 43, 
     44, 
     45, 46, 47, 48, 
     49, 50, 51]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    for blockName, expectedFormat in (
     (b'fortBattlesInClan', b'<IIIIIIIIIIIIIIIIIIIIIIIIIIIII'),
     (b'fortSortiesInClan', b'<IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII')):
        currentSize = getBlockSize(updateCtx, blockName)
        expectedSize = struct.calcsize(expectedFormat)
        if currentSize < expectedSize:
            recordsFormat = [(b'battlesOnStunningVehicles', b'I'),
             (b'stunNum', b'I'),
             (b'damageAssistedStun', b'I')]
            addRecords(updateCtx, blockName, recordsFormat, {})

    setVersion(updateCtx, 104)
    return (104, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier104(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 
     39, 40, 41, 42, 43, 
     44, 
     45, 46, 47, 48, 
     49, 50, 51]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'ranked')
    addBlock(updateCtx, b'maxRanked')
    addBlock(updateCtx, b'rankedCut')
    addBlock(updateCtx, b'rankedBadges')
    addBlock(updateCtx, b'rankedSeasons')
    addBlock(updateCtx, b'rankedCurrent')
    addBlock(updateCtx, b'rankedPrevious')
    addBlock(updateCtx, b'maxRankedCurrent')
    addBlock(updateCtx, b'maxRankedPrevious')
    addBlock(updateCtx, b'rankedCurrentCut')
    addBlock(updateCtx, b'rankedPreviousCut')
    addBlock(updateCtx, b'rankedCurrentCycle')
    addBlock(updateCtx, b'rankedPreviousCycle')
    setVersion(updateCtx, 105)
    return (105, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier105(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 
     39, 40, 41, 42, 43, 
     44, 
     45, 46, 47, 48, 
     49, 50, 51, 52, 53, 54, 55, 
     56, 
     57, 58, 59, 60, 
     61, 62, 63, 64]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    removeBlock(updateCtx, b'fortMisc')
    removeBlock(updateCtx, b'fortMiscInClan')
    fortSortiesInClanPacking = {b'middleWins': (128, b'I'), 
       b'middleBattlesCount': (116, b'I'), b'absoluteBattlesCount': (124, b'I'), b'absoluteWins': (136, b'I'), 
       b'fortResource': (140, b'I'), b'championWins': (132, b'I'), b'championBattlesCount': (120, b'I')}
    removeRecords(updateCtx, b'fortSortiesInClan', fortSortiesInClanPacking)
    fortAchievementsPacking = {b'wins': (8, b'H'), 
       b'capturedBasesInAttack': (10, b'H'), b'capturedBasesInDefence': (12, b'H')}
    removeRecords(updateCtx, b'fortAchievements', fortAchievementsPacking)
    setVersion(updateCtx, 106)
    return (106, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier106(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 
     50, 51, 52, 53, 
     54, 55, 56, 
     57, 58, 59, 60, 61, 
     62]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'a30x30')
    addBlock(updateCtx, b'a30x30Cut')
    addBlock(updateCtx, b'max30x30')
    setVersion(updateCtx, 107)
    return (107, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier107(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 
     50, 51, 52, 53, 
     54, 55, 56, 
     57, 58, 59, 60, 61, 
     62, 63, 
     64, 65]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    a15x15Cut = getBlockCompDescr(updateCtx, b'a15x15Cut')
    markOfMasteryCutBlockFormat = b''
    markOfMasteryCutBlockValues = None
    if a15x15Cut:
        keyFormat, valueFormat = (b'I', b'IIII')
        itemFormat = keyFormat + valueFormat
        itemSize = struct.calcsize(b'<' + itemFormat)
        length = len(a15x15Cut) / itemSize
        fmt = b'<' + itemFormat * length
        values = struct.unpack(fmt, a15x15Cut)
        newValues = []
        markOfMasteryCutBlockFormat = b'<'
        markOfMasteryCutBlockValues = []
        itemLength = len(itemFormat)
        idx = 0
        for i in xrange(length):
            items = values[idx:idx + itemLength]
            newValues += items[:3] + items[4:]
            if items[3] != 0:
                markOfMasteryCutBlockFormat += b'IB'
                markOfMasteryCutBlockValues += [items[0], items[3]]
            idx += itemLength

        newKeyFormat, newValueFormat = (b'I', b'III')
        newItemFormat = newKeyFormat + newValueFormat
        fmt = b'<' + newItemFormat * length
        newA15x15CutCompDescr = struct.pack(fmt, *newValues)
        setBlockCompDescr(updateCtx, b'a15x15Cut', newA15x15CutCompDescr)
    addBlock(updateCtx, b'markOfMasteryCut', markOfMasteryCutBlockFormat, markOfMasteryCutBlockValues)
    setVersion(updateCtx, 108)
    return (108, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier108(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 
     50, 51, 52, 53, 
     54, 55, 56, 
     57, 58, 59, 60, 61, 
     62, 63, 
     64, 65, 66]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    rankedBadgesPacking = {b'1': (0, b'H'), 
       b'2': (2, b'H'), 
       b'3': (4, b'H'), 
       b'4': (6, b'H'), 
       b'5': (8, b'H'), 
       b'6': (10, b'H'), 
       b'7': (12, b'H'), 
       b'8': (14, b'H'), 
       b'9': (16, b'H')}
    badges = getStaticSizeBlockRecordValues(updateCtx, b'rankedBadges', rankedBadgesPacking)
    addItems = {}
    _SECONDS_IN_DAY = 86400
    for strBadgeID, daysTimestamp in badges.iteritems():
        if daysTimestamp:
            addItems[int(strBadgeID)] = daysTimestamp * _SECONDS_IN_DAY

    LOG_DEBUG_DEV(b'addItems', addItems)
    itemFormat = b'II'
    subBlockFormat = b'<'
    subBlockValues = []
    for k, v in addItems.iteritems():
        subBlockFormat += itemFormat
        subBlockValues.append(k)
        subBlockValues.append(v)

    LOG_DEBUG_DEV(b'subBlockFormat', subBlockFormat, subBlockValues)
    addBlock(updateCtx, b'playerBadges', subBlockFormat, subBlockValues)
    removeBlock(updateCtx, b'rankedBadges')
    setVersion(updateCtx, 109)
    return (109, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier109(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'epicBattle')
    addBlock(updateCtx, b'epicBattleCut')
    addBlock(updateCtx, b'maxEpicBattle')
    addBlock(updateCtx, b'epicBattleAchievements')
    setVersion(updateCtx, 110)
    return (110, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier110(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    isPresent = getBinarySetValue(updateCtx, b'singleAchievements', 4, 2)
    records = [(183, b'H', 1 if isPresent else 0)]
    updateStaticSizeBlockRecords(updateCtx, b'achievements', records)
    setVersion(updateCtx, 111)
    return (111, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier111(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'FE18ClosedStage', b'B'),
     (b'FE18SoloStriker', b'B'),
     (b'FE18SoloMidfielder', b'B'),
     (b'FE18SoloDefender', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 112)
    return (112, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier112(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'readyForBattleAllianceUSSR', b'B'),
     (b'readyForBattleAllianceGermany', b'B'),
     (b'readyForBattleAllianceUSA', b'B'),
     (b'readyForBattleAllianceFrance', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 113)
    return (113, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier113(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'superTesterVeteran', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 114)
    return (114, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier114(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     90, 
     91, 
     92, 
     93, 
     94, 
     95, 
     96, 
     97, 
     98, 
     99, 
     100, 
     101]
    addRecords(updateCtx, b'singleAchievements', formats, {})
    setVersion(updateCtx, 115)
    return (115, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier115(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'NY19A1', b'B'),
     (b'NY19A2', b'B'),
     (b'NY19A3', b'B')]
    addRecords(updateCtx, b'singleAchievements', formats, {})
    setVersion(updateCtx, 116)
    return (116, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier116(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'RP2018firstmed', b'B'),
     (b'RP2018secondmed', b'B'),
     (b'RP2018thirdmed', b'B'),
     (b'RP2018sergeant', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 117)
    return (117, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier117(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'rankedDivisionFighter', b'I'),
     (b'rankedStayingPower', b'I')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 118)
    return (118, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier118(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 
     53, 
     54, 55, 56, 57, 
     58, 59, 60, 61, 
     62, 63, 
     64, 65, 66, 
     67, 68, 69, 70]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'rankedSeason1')
    addBlock(updateCtx, b'rankedSeason2')
    addBlock(updateCtx, b'rankedSeason3')
    addBlock(updateCtx, b'maxRankedSeason1')
    addBlock(updateCtx, b'maxRankedSeason2')
    addBlock(updateCtx, b'maxRankedSeason3')
    addBlock(updateCtx, b'rankedCutSeason1')
    addBlock(updateCtx, b'rankedCutSeason2')
    addBlock(updateCtx, b'rankedCutSeason3')
    addBlock(updateCtx, b'rankedArchive')
    addBlock(updateCtx, b'maxRankedArchive')
    addBlock(updateCtx, b'rankedCutArchive')
    oldBlockCompDescr = getBlockCompDescr(updateCtx, b'ranked')
    if oldBlockCompDescr:
        setBlockCompDescr(updateCtx, b'rankedArchive', oldBlockCompDescr)
    oldBlockCompDescr = getBlockCompDescr(updateCtx, b'maxRanked')
    if oldBlockCompDescr:
        setBlockCompDescr(updateCtx, b'maxRankedArchive', oldBlockCompDescr)
    oldBlockCompDescr = getBlockCompDescr(updateCtx, b'rankedCut')
    if oldBlockCompDescr:
        setBlockCompDescr(updateCtx, b'rankedCutArchive', oldBlockCompDescr)
    removeBlock(updateCtx, b'rankedCurrent')
    removeBlock(updateCtx, b'rankedPrevious')
    removeBlock(updateCtx, b'rankedCurrentCycle')
    removeBlock(updateCtx, b'rankedPreviousCycle')
    removeBlock(updateCtx, b'maxRankedCurrent')
    removeBlock(updateCtx, b'maxRankedPrevious')
    removeBlock(updateCtx, b'rankedCurrentCut')
    removeBlock(updateCtx, b'rankedPreviousCut')
    setVersion(updateCtx, 119)
    return (119, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier119(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'BR2019Top1Solo', b'I'),
     (b'BR2019Top1Squad', b'I')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 120)
    return (120, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier120(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 
     32, 33, 
     34, 35, 36, 
     37, 38, 39, 40, 41, 
     42, 43, 
     44, 45, 46, 
     47, 48, 49, 50, 51, 52, 53, 
     54, 
     55, 56, 57, 58, 
     59, 60, 61, 62, 
     63, 64, 
     65, 
     66, 67, 68, 
     69, 70, 71, 
     72, 
     73, 74]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'racing2019Achievements')
    setVersion(updateCtx, 121)
    return (121, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier121(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    rankedSeasonsValues = getDictBlockRecordValues(updateCtx, b'rankedSeasons', b'II', b'BBHHH')
    if rankedSeasonsValues:
        updateDictRecords(updateCtx, b'rankedSeasons', b'II', b'BHHHH', rankedSeasonsValues)
    setVersion(updateCtx, 122)
    return (122, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier122(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'superTesterVeteranCross', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 123)
    return (123, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier123(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    removeBlock(updateCtx, b'racing2019Achievements')
    setVersion(updateCtx, 124)
    return (124, updateCtx[b'dossierCompDescr'])


def _rankedAchievmentClass(counter, achievmentName):
    achievmentCfg = RECORD_CONFIGS[achievmentName]
    maxAchievmentClass = len(achievmentCfg)
    for achievmentClass in xrange(1, maxAchievmentClass + 1):
        if counter >= achievmentCfg[maxAchievmentClass - achievmentClass]:
            break
    else:
        achievmentClass = 0

    return achievmentClass


def __updateFromAccountDossier124(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    packing = {b'rankedDivisionFighter': (198, b'I'), b'rankedStayingPower': (202, b'I')}
    values = getStaticSizeBlockRecordValues(updateCtx, b'achievements', packing)
    rankedDivisionFighterVal = values.get(b'rankedDivisionFighter', 0)
    rankedStayingPowerVal = values.get(b'rankedStayingPower', 0)
    removeRecords(updateCtx, b'achievements', packing)
    formats = [
     (b'rankedDivisionCounter', b'I'),
     (b'rankedDivisionFighter', b'B'),
     (b'rankedStayingCounter', b'I'),
     (b'rankedStayingPower', b'B')]
    defaults = {b'rankedDivisionCounter': rankedDivisionFighterVal, 
       b'rankedDivisionFighter': (_rankedAchievmentClass(rankedDivisionFighterVal, b'rankedDivisionFighter')), 
       b'rankedStayingCounter': rankedStayingPowerVal, 
       b'rankedStayingPower': (_rankedAchievmentClass(rankedStayingPowerVal, b'rankedStayingPower'))}
    addRecords(updateCtx, b'achievements', formats, defaults)
    setVersion(updateCtx, 125)
    return (125, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier125(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'epicSeasons')
    setVersion(updateCtx, 126)
    return (126, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier126(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 75]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'collectorVehicleStrg', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 127)
    return (127, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier127(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 75]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'TenYearsCountdownStageMedal', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 128)
    return (128, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier128(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 75]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'battleRoyaleSeasons')
    setVersion(updateCtx, 129)
    return (129, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier129(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'wtHunterWins', b'I'),
     (b'wtBossWins', b'I'),
     (b'wtSpecBossDefeat', b'I')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 130)
    return (130, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier130(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordsFormat = [
     (b'playedBonusBattles', b'I')]
    addRecords(updateCtx, b'ranked', recordsFormat, {})
    addRecords(updateCtx, b'rankedSeason1', recordsFormat, {})
    addRecords(updateCtx, b'rankedSeason2', recordsFormat, {})
    addRecords(updateCtx, b'rankedSeason3', recordsFormat, {})
    addRecords(updateCtx, b'rankedArchive', recordsFormat, {})
    setVersion(updateCtx, 131)
    return (131, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier131(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordsFormat = [
     (b'RP2018sergeantCounter', b'H')]
    addRecords(updateCtx, b'achievements', recordsFormat, {})
    setVersion(updateCtx, 132)
    return (132, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier132(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'ranked_10x10')
    addBlock(updateCtx, b'maxRanked_10x10')
    addBlock(updateCtx, b'rankedCut_10x10')
    setVersion(updateCtx, 133)
    return (133, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier133(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 
     33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 
     44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    epicSeasonsValues = getDictBlockRecordValues(updateCtx, b'epicSeasons', b'II', b'HHBB')
    for key, values in epicSeasonsValues.iteritems():
        battleCount, averageFamePts, tokensCount, level = values
        epicSeasonsValues[key] = (battleCount, averageFamePts, level, 0, 0)

    LOG_DEBUG_DEV(b'__updateFromAccountDossier133 epicSeasonsValues', epicSeasonsValues)
    if epicSeasonsValues:
        updateDictRecords(updateCtx, b'epicSeasons', b'II', b'HHBHH', epicSeasonsValues)
    setVersion(updateCtx, 134)
    return (134, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier134(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    rankedCut10x10CompDescr = getBlockCompDescr(updateCtx, b'rankedCut_10x10')
    setBlockCompDescr(updateCtx, b'rankedCut', rankedCut10x10CompDescr if rankedCut10x10CompDescr else b'')
    setVersion(updateCtx, 135)
    return (135, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier135(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'wtxHunterWins', b'I'),
     (b'wtxBossWins', b'I'),
     (b'wtxSpecBossDefeat', b'I')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 136)
    return (136, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier136(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'steamAchievements')
    setVersion(updateCtx, 137)
    return (137, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier137(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 80]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordsFormat = [
     (b'whiteTiger2012', b'B')]
    addRecords(updateCtx, b'achievements', recordsFormat, {})
    setVersion(updateCtx, 138)
    return (138, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier138(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 80]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'lunarNY2022Progression', b'B')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 139)
    return (139, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier139(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 80]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'oowTankmanWins', b'H'),
     (b'oowStrategistWins', b'H'),
     (b'oowCompetetiveWin', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 140)
    return (140, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier140(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 80]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'mapboxUniversal', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 141)
    return (141, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier141(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 80]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'wclTournamentParticipant', b'H'),
     (b'wclParticipant', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 142)
    return (142, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier142(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 80]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'wt2022HunterWins', b'I'),
     (b'wt2022BossWins', b'I'),
     (b'wt2022SpecBossDefeat', b'I')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 143)
    return (143, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier143(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 80]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season1')
    addBlock(updateCtx, b'maxComp7Season1')
    addBlock(updateCtx, b'comp7CutSeason1')
    setVersion(updateCtx, 144)
    return (144, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier144(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season2')
    addBlock(updateCtx, b'maxComp7Season2')
    addBlock(updateCtx, b'comp7CutSeason2')
    setVersion(updateCtx, 145)
    return (
     145, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier145(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 79, 
     80, 81, 82, 83, 84, 85, 
     86]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'maxAssisted', b'H'),
     (b'maxAssistedVehicle', b'I'),
     (b'maxDamageBlockedByArmor', b'H'),
     (b'maxDamageBlockedByArmorVehicle', b'I')]
    addRecords(updateCtx, b'max15x15', formats, {})
    setVersion(updateCtx, 146)
    return (146, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier146(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'mtAchievements')
    setVersion(updateCtx, 147)
    return (147, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier147(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    achievements7x7Packing = {b'maxTacticalBreakthroughSeries': (12, b'H')}
    achievements7x7Values = getStaticSizeBlockRecordValues(updateCtx, b'achievements7x7', achievements7x7Packing)
    isSingleAchievementClaimed = getBinarySetValue(updateCtx, b'singleAchievements', 0, 7)
    if not isSingleAchievementClaimed and achievements7x7Values.get(b'maxTacticalBreakthroughSeries', 0) >= 3:
        updateBinaryBlockRecords(updateCtx, b'singleAchievements', [(0, 7, True)])
    setVersion(updateCtx, 148)
    return (148, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier148(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'mt_versusAI')
    addBlock(updateCtx, b'mt_maxVersusAI')
    addBlock(updateCtx, b'mt_versusAICut')
    setVersion(updateCtx, 149)
    return (
     149, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier149(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season3')
    addBlock(updateCtx, b'maxComp7Season3')
    addBlock(updateCtx, b'comp7CutSeason3')
    addBlock(updateCtx, b'comp7ArchiveGriffin')
    addBlock(updateCtx, b'maxComp7ArchiveGriffin')
    addBlock(updateCtx, b'comp7CutArchiveGriffin')
    setVersion(updateCtx, 150)
    return (
     150, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier150(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (124, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), b'droppedCapturePoints': (48, b'I'), 
       b'healthRepair': (128, b'I'), b'directHitsReceived': (64, b'I'), 
       b'comp7PrestigePoints': (120, b'I'), b'explosionHitsReceived': (76, b'I'), 
       b'winAndSurvived': (88, b'I'), b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'damageAssistedStun': (108, b'I'), 
       b'squadWinSeries': (116, b'I'), b'explosionHits': (80, b'I'), b'wins': (8, b'I'), 
       b'poiCapturable': (132, b'I'), b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 3
    archiveSeasonsGriffin(seasonsNumber, updateCtx, comp7SeasonsPacking, comp7SeasonsNewPacking)
    addSeasonRecord(updateCtx, b'comp7Season1', [(b'superSquadBattlesCount', b'I'), (b'superSquadWins', b'I')], {})
    addSeasonRecord(updateCtx, b'comp7Season2', [(b'superSquadBattlesCount', b'I'), (b'superSquadWins', b'I')], {})
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsGriffin(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    archiveCutSeasonsGriffin(seasonsNumber, updateCtx)
    setVersion(updateCtx, 151)
    return (151, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier151(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 
     33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 
     44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    setBlockCompDescr(updateCtx, b'rankedSeason1', b'')
    setBlockCompDescr(updateCtx, b'maxRankedSeason1', b'')
    setBlockCompDescr(updateCtx, b'rankedCutSeason1', b'')
    setVersion(updateCtx, 152)
    return (152, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier152(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 
     33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 
     44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    setBlockCompDescr(updateCtx, b'rankedSeason1', b'')
    setBlockCompDescr(updateCtx, b'maxRankedSeason1', b'')
    setBlockCompDescr(updateCtx, b'rankedCutSeason1', b'')
    setVersion(updateCtx, 153)
    return (153, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier153(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 
     33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 
     44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season4')
    addBlock(updateCtx, b'maxComp7Season4')
    addBlock(updateCtx, b'comp7CutSeason4')
    setVersion(updateCtx, 154)
    return (
     154, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier154(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96, 97, 
     98, 99]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 4
    archiveSeasonsWolf(seasonsNumber, updateCtx, comp7SeasonsNewPacking)
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsWolf(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    archiveCutSeasonsWolf(seasonsNumber, updateCtx)
    setVersion(updateCtx, 155)
    return (155, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier155(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96, 97, 
     98, 99]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'wt2024HunterWins', b'I'),
     (b'wt2024BossWins', b'I'),
     (b'wt2024MaxPlasma', b'I')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 156)
    return (156, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier156(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96, 97, 
     98, 99]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 4
    archiveSeasonsWolf(seasonsNumber, updateCtx, comp7SeasonsNewPacking)
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsWolf(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    archiveCutSeasonsWolf(seasonsNumber, updateCtx)
    setVersion(updateCtx, 157)
    return (157, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier157(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96, 97, 
     98, 99]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    vehTypeFrags = {vehID: kills for (vehID,), kills in getDictBlockRecordValues(updateCtx, b'vehTypeFrags', b'I', b'H').iteritems()}
    achievementsExpertPacking = {b'tankExpertStrg': (86, b'H')}
    resultBits = 0
    res = getTankExpertRequirements(vehTypeFrags)
    for record, value in res.iteritems():
        if len(value) <= 0:
            bitNum = int(record.split(b'tankExpert')[1]) + 1 if record.split(b'tankExpert')[1] else 0
            resultBits |= 1 << bitNum

    tankExpertValue = getStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsExpertPacking)
    medalsAchieved = tankExpertValue.get(b'tankExpertStrg', 0) | resultBits
    records = [(86, b'H', medalsAchieved)]
    updateStaticSizeBlockRecords(updateCtx, b'achievements', records)
    setVersion(updateCtx, 158)
    return (158, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier158(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96, 97, 
     98, 99]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'saboteur', b'B'),
     (b'saboteurProgress', b'B')]
    addRecords(updateCtx, b'epicBattleAchievements', formats, {})
    setVersion(updateCtx, 159)
    return (159, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier159(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96, 97, 
     98, 99]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'medalFomin', b'H'),
     (b'medalKrockenberger', b'H'),
     (b'medalGavryushov', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 160)
    return (160, updateCtx[b'dossierCompDescr'])


def __updateFromAccountDossier160(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 
     23, 
     24, 25, 26, 27, 28, 
     29, 30, 31, 32, 33, 
     34, 
     35, 36, 37, 38, 39, 
     40, 41, 42, 43, 44, 
     45, 
     46, 47, 48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 
     58, 
     59, 60, 61, 62, 63, 64, 
     65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 
     75, 76, 77, 
     78, 
     79, 80, 
     81, 82, 83, 
     84, 85, 86, 
     87, 
     88, 89, 90, 
     91, 92, 93, 94, 
     95, 96, 97, 
     98, 99]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 4
    archiveSeasonsWolf(seasonsNumber, updateCtx, comp7SeasonsNewPacking)
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsWolf(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    archiveCutSeasonsWolf(seasonsNumber, updateCtx)
    setVersion(updateCtx, 161)
    return (161, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier64(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9]
    a15x15packing = {b'creationTime': (0, b'I'), b'battleLifeTime': (8, b'I'), b'lastBattleTime': (4, b'I')}
    a15x15_2packing = {b'mileage': (38, b'I'), b'treesCut': (36, b'H')}
    achievementsPacking = {b'maxFrags': (0, b'B'), b'maxXP': (1, b'H'), b'winAndSurvived': (3, b'I'), b'frags8p': (7, b'I')}
    totalLayout = [
     49, 50, 51, 
     52, 53]
    max15x15Layout = [
     (b'maxXP', b'H'), (b'maxFrags', b'B'), (b'maxDamage', b'H')]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    totalDefaults = getStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing)
    totalDefaults.update(getStaticSizeBlockRecordValues(updateCtx, b'a15x15_2', a15x15_2packing))
    if bool(totalDefaults):
        blockFormat, blockValues = getNewStaticSizeBlockValues(totalLayout, totalDefaults)
    else:
        blockFormat, blockValues = (b'', None)
    addBlock(updateCtx, b'total', blockFormat, blockValues)
    removeRecords(updateCtx, b'a15x15', a15x15packing)
    removeRecords(updateCtx, b'a15x15_2', a15x15_2packing)
    achievementsValues = getStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking)
    addRecords(updateCtx, b'a15x15', [
     (b'winAndSurvived', b'I'), (b'frags8p', b'I')], achievementsValues)
    addRecords(updateCtx, b'a7x7', [
     (b'winAndSurvived', b'I'), (b'frags8p', b'I')], {})
    if bool(achievementsValues):
        blockFormat, blockValues = getNewStaticSizeBlockValues(max15x15Layout, achievementsValues)
    else:
        blockFormat, blockValues = (b'', None)
    addBlock(updateCtx, b'max15x15', blockFormat, blockValues)
    addBlock(updateCtx, b'max7x7')
    removeRecords(updateCtx, b'achievements', achievementsPacking)
    setVersion(updateCtx, 65)
    return (65, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier65(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'inscriptions')
    addBlock(updateCtx, b'emblems')
    addBlock(updateCtx, b'camouflages')
    addBlock(updateCtx, b'compensation')
    setVersion(updateCtx, 66)
    return (66, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier66(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'achievements', [(b'sniper2', b'H'), (b'mainGun', b'H')], {})
    setVersion(updateCtx, 67)
    return (67, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier67(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    blockFormat = b'<' + b'HHHHHHHH'
    blockValues = [0] * 8
    addBlock(updateCtx, b'achievements7x7', blockFormat, blockValues)
    setVersion(updateCtx, 68)
    return (68, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier68(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'achievements7x7', [(b'tacticalBreakthrough', b'B')], {b'tacticalBreakthrough': 0})
    setVersion(updateCtx, 69)
    return (69, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier69(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    headerValues = updateCtx[b'header'][1:]
    sumAllValues = sum(headerValues)
    vehDossierCompDescrLen = len(compDescr) - updateCtx[b'headerLength']
    a7x7Size = headerValues[6]
    max7x7Size = headerValues[11]
    achievements7x7Size = headerValues[16]
    if vehDossierCompDescrLen != sumAllValues and vehDossierCompDescrLen == sumAllValues - a7x7Size - max7x7Size:
        updateCtx[b'header'][7] = 0
        updateCtx[b'header'][12] = 0
        updateCtx[b'header'][17] = 0
        compDescr = struct.pack(updateCtx[b'headerFormat'], *updateCtx[b'header']) + compDescr[updateCtx[b'headerLength']:]
        if achievements7x7Size != 0:
            compDescr = compDescr[:-achievements7x7Size]
        updateCtx = {b'dossierCompDescr': compDescr, 
           b'blockSizeFormat': b'H', 
           b'versionFormat': b'H', 
           b'blocksLayout': blocksLayout}
        getHeader(updateCtx)
        headerValues = updateCtx[b'header'][1:]
        sumAllValues = sum(headerValues)
        vehDossierCompDescrLen = len(compDescr) - updateCtx[b'headerLength']
    setVersion(updateCtx, 70)
    return (70, compDescr)


def __updateFromVehicleDossier70(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordFormats = [
     (b'potentialDamageReceived', b'I'), (b'damageBlockedByArmor', b'I')]
    addRecords(updateCtx, b'a15x15_2', recordFormats, {})
    addRecords(updateCtx, b'company2', recordFormats, {})
    addRecords(updateCtx, b'clan2', recordFormats, {})
    addRecords(updateCtx, b'a7x7', recordFormats, {})
    setVersion(updateCtx, 71)
    return (71, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier71(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordFormats = [
     (b'battlesCountBefore9_0', b'I')]
    a15x15packing = {b'battlesCount': (4, b'I')}
    a15x15defaults = getStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing)
    addRecords(updateCtx, b'a15x15', recordFormats, {b'battlesCountBefore9_0': (a15x15defaults.get(b'battlesCount', 0))})
    companyPacking = {b'battlesCount': (4, b'I')}
    companyDefaults = getStaticSizeBlockRecordValues(updateCtx, b'company', companyPacking)
    addRecords(updateCtx, b'company', recordFormats, {b'battlesCountBefore9_0': (companyDefaults.get(b'battlesCount', 0))})
    clanPacking = {b'battlesCount': (4, b'I')}
    clanDefaults = getStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking)
    addRecords(updateCtx, b'clan', recordFormats, {b'battlesCountBefore9_0': (clanDefaults.get(b'battlesCount', 0))})
    a7x7packing = {b'battlesCount': (4, b'I')}
    a7x7defaults = getStaticSizeBlockRecordValues(updateCtx, b'a7x7', a7x7packing)
    addRecords(updateCtx, b'a7x7', recordFormats, {b'battlesCountBefore9_0': (a7x7defaults.get(b'battlesCount', 0))})
    setVersion(updateCtx, 72)
    return (72, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier72(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    setVersion(updateCtx, 73)
    return (73, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier73(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 
     8, 9, 10, 11, 12, 13, 
     14, 
     15, 16, 17]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'historical')
    addBlock(updateCtx, b'maxHistorical')
    setVersion(updateCtx, 74)
    return (74, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier74(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     35, 
     36, 
     37, 
     38, 
     39, 
     40, 
     41]
    defaultValues = {b'godOfWar': 0, 
       b'fightingReconnaissance': 0, 
       b'fightingReconnaissanceMedal': 0, 
       b'willToWinSpirit': 0, 
       b'crucialShot': 0, 
       b'crucialShotMedal': 0, 
       b'forTacticalOperations': 0}
    addRecords(updateCtx, b'achievements7x7', formats, defaultValues)
    setVersion(updateCtx, 75)
    return (75, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier75(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'marksOnGun', b'B'),
     (b'movingAvgDamage', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 76)
    return (76, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier76(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     31, 
     32, 
     33, 
     34, 
     35]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 77)
    return (77, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier77(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'uniqueAchievements')
    setVersion(updateCtx, 78)
    return (78, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier78(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'fortBattles')
    addBlock(updateCtx, b'maxFortBattles')
    addBlock(updateCtx, b'fortSorties')
    addBlock(updateCtx, b'maxFortSorties')
    addBlock(updateCtx, b'fortAchievements')
    setVersion(updateCtx, 79)
    return (79, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier79(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     44, 
     45, 
     46, 
     47, 
     48, 
     49, 
     50, 
     51, 
     52, 
     53, 
     54]
    defaultValues = {b'promisingFighter': 0, 
       b'promisingFighterMedal': 0, 
       b'heavyFire': 0, 
       b'heavyFireMedal': 0, 
       b'ranger': 0, 
       b'rangerMedal': 0, 
       b'fireAndSteel': 0, 
       b'fireAndSteelMedal': 0, 
       b'pyromaniac': 0, 
       b'pyromaniacMedal': 0, 
       b'noMansLand': 0}
    addRecords(updateCtx, b'achievements7x7', formats, defaultValues)
    setVersion(updateCtx, 80)
    return (80, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier80(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'damageRating', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 81)
    return (81, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier81(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    awardCount = _count7x7awards(updateCtx)
    formats = [
     47, 
     48, 
     49, 
     50, 
     51, 
     52, 
     53, 
     54, 
     55, 
     56, 
     57, 
     58]
    defaultValues = {b'guerrilla': 0, 
       b'guerrillaMedal': 0, 
       b'infiltrator': 0, 
       b'infiltratorMedal': 0, 
       b'sentinel': 0, 
       b'sentinelMedal': 0, 
       b'prematureDetonation': 0, 
       b'prematureDetonationMedal': 0, 
       b'bruteForce': 0, 
       b'bruteForceMedal': 0, 
       b'awardCount': awardCount, 
       b'battleTested': 0}
    addRecords(updateCtx, b'achievements7x7', formats, defaultValues)
    setVersion(updateCtx, 82)
    return (82, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier82(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    layout = [
     31, 
     32, 
     33, 
     34, 
     35, 
     36]
    values = {}
    achievementsPacking = {b'titleSniper': (88, b'B'), 
       b'invincible': (89, b'B'), 
       b'diehard': (90, b'B'), 
       b'handOfDeath': (93, b'B'), 
       b'armorPiercer': (94, b'B')}
    values.update(getStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking))
    achievements7x7Packing = {b'tacticalBreakthrough': (16, b'B')}
    values.update(getStaticSizeBlockRecordValues(updateCtx, b'achievements7x7', achievements7x7Packing))
    blockFormat, blockValues = getNewBinarySetBlockValues(layout, values)
    addBlock(updateCtx, b'singleAchievements', blockFormat, blockValues)
    removeRecords(updateCtx, b'achievements', achievementsPacking)
    removeRecords(updateCtx, b'achievements7x7', achievements7x7Packing)
    setVersion(updateCtx, 83)
    return (83, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier83(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    blockLayout = [
     (b'medalRotmistrov', b'B')]
    blockFormat, blockValues = getNewStaticSizeBlockValues(blockLayout, {b'medalRotmistrov': 0})
    addBlock(updateCtx, b'clanAchievements', blockFormat, blockValues)
    setVersion(updateCtx, 84)
    return (84, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier84(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    a15x15packing = {b'battlesCountBefore9_0': (68, b'I'), b'battlesCountBefore8_8': (56, b'I')}
    values = getStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing)
    if values and values[b'battlesCountBefore8_8'] > 0 and values[b'battlesCountBefore9_0'] == 0:
        values[b'battlesCountBefore9_0'] = values[b'battlesCountBefore8_8']
        setStaticSizeBlockRecordValues(updateCtx, b'a15x15', a15x15packing, values)
    clanPacking = {b'battlesCountBefore9_0': (60, b'I'), b'battlesCountBefore8_9': (56, b'I')}
    values = getStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking)
    if values and values[b'battlesCountBefore8_9'] > 0 and values[b'battlesCountBefore9_0'] == 0:
        values[b'battlesCountBefore9_0'] = values[b'battlesCountBefore8_9']
        setStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking, values)
    companyPacking = {b'battlesCountBefore9_0': (60, b'I'), b'battlesCountBefore8_9': (56, b'I')}
    values = getStaticSizeBlockRecordValues(updateCtx, b'company', companyPacking)
    if values and values[b'battlesCountBefore8_9'] > 0 and values[b'battlesCountBefore9_0'] == 0:
        values[b'battlesCountBefore9_0'] = values[b'battlesCountBefore8_9']
        setStaticSizeBlockRecordValues(updateCtx, b'company', companyPacking, values)
    setVersion(updateCtx, 85)
    return (85, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier85(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordFormats = [
     45, 
     46, 
     47, 
     48, 
     49, 
     50, 
     51, 
     52, 
     53, 
     54]
    addRecords(updateCtx, b'achievements', recordFormats, {})
    setVersion(updateCtx, 86)
    return (86, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier86(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordFormats = [
     (b'wins', b'H'),
     (b'capturedBasesInAttack', b'H'),
     (b'capturedBasesInDefence', b'H')]
    addRecords(updateCtx, b'fortAchievements', recordFormats, {})
    setVersion(updateCtx, 87)
    return (87, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier87(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'rated7x7')
    addBlock(updateCtx, b'maxRated7x7')
    setVersion(updateCtx, 88)
    return (88, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier88(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    battleHeroes7x7Count = _countBattleHeroesBasedOn7x7Medals(updateCtx)
    if battleHeroes7x7Count > 0:
        achievementsPacking = {b'battleHeroes': (20, b'H'), b'medalKay': (38, b'B')}
        values = getStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking)
        if values:
            values[b'battleHeroes'] += battleHeroes7x7Count
            values[b'medalKay'] = _medalKayClass(values[b'battleHeroes'])
            setStaticSizeBlockRecordValues(updateCtx, b'achievements', achievementsPacking, values)
    setVersion(updateCtx, 89)
    return (89, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier89(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    gmDefaults = {}
    clanPacking = {b'spotted': (32, b'I'), 
       b'damageDealt': (36, b'I'), b'wins': (8, b'I'), b'capturePoints': (44, b'I'), b'losses': (12, b'I'), 
       b'survivedBattles': (16, b'I'), b'droppedCapturePoints': (48, b'I'), b'battlesCount': (4, b'I'), 
       b'damageReceived': (40, b'I'), b'shots': (24, b'I'), b'frags': (20, b'I'), 
       b'xp': (0, b'I'), b'directHits': (28, b'I')}
    gmDefaults.update(getStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking))
    clan2Packing = {b'directHitsReceived': (12, b'I'), 
       b'damageAssistedTrack': (4, b'I'), b'explosionHitsReceived': (24, b'I'), b'potentialDamageReceived': (36, b'I'), 
       b'piercingsReceived': (20, b'I'), b'originalXP': (0, b'I'), b'damageAssistedRadio': (8, b'I'), 
       b'piercings': (32, b'I'), b'explosionHits': (28, b'I'), b'damageBlockedByArmor': (40, b'I'), 
       b'noDamageDirectHitsReceived': (16, b'I')}
    gmDefaults.update(getStaticSizeBlockRecordValues(updateCtx, b'clan2', clan2Packing))
    gmLayout = [
     101, 102, 103, 104, 105, 106, 
     107, 108, 109, 110, 
     111, 
     112, 113, 114, 115, 
     116, 117, 118, 
     119, 
     120, 121, 122, 
     123, 124, 125, 126]
    blockFormat, blockValues = getNewStaticSizeBlockValues(gmLayout, gmDefaults)
    addBlock(updateCtx, b'globalMapCommon', blockFormat, blockValues)
    setVersion(updateCtx, 90)
    return (90, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier90(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    clanPacking = {b'xpBefore8_9': (52, b'I'), b'battlesCountBefore9_0': (60, b'I'), b'battlesCountBefore8_9': (56, b'I')}
    clanValues = getStaticSizeBlockRecordValues(updateCtx, b'clan', clanPacking)
    recordFormats = [
     (b'xpBefore8_9', b'I'),
     (b'battlesCountBefore8_9', b'I'),
     (b'battlesCountBefore9_0', b'I')]
    addRecords(updateCtx, b'globalMapCommon', recordFormats, clanValues)
    setVersion(updateCtx, 91)
    return (91, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier91(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'maxGlobalMapCommon')
    setVersion(updateCtx, 92)
    return (92, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier92(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'fallout')
    addBlock(updateCtx, b'maxFallout')
    setVersion(updateCtx, 93)
    return (93, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier93(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'falloutAchievements')
    setVersion(updateCtx, 94)
    return (94, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier94(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    modes = (b'a15x15_2', b'clan2', b'company2', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'rated7x7', b'globalMapCommon', b'fallout')
    for mode in modes:
        recordsFormat = [(b'battlesOnStunningVehicles', b'I'),
         (b'stunNum', b'I'),
         (b'damageAssistedStun', b'I')]
        addRecords(updateCtx, mode, recordsFormat, {})

    setVersion(updateCtx, 95)
    return (95, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier95(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    battlesOnStunningVehiclesOffsets = {b'fortBattles': 104, b'globalMapCommon': 116, b'a15x15_2': 44, 
       b'fortSorties': 104, b'historical': 104, 
       b'rated7x7': 104, b'clan2': 44, 
       b'fallout': 128, b'company2': 44, 
       b'a7x7': 108}
    for block, offset in battlesOnStunningVehiclesOffsets.iteritems():
        lastFieldKey = {b'a7x7': b'battlesCountBefore9_0', 
           b'globalMapCommon': b'battlesCountBefore9_0', 
           b'fallout': b'deathCount'}.get(block, b'damageBlockedByArmor')
        packing = {lastFieldKey: (offset - 4, b'I'), b'battlesOnStunningVehicles': (
                                        offset, b'I'), 
           b'stunNum': (
                      offset + 4, b'I'), 
           b'damageAssistedStun': (
                                 offset + 8, b'I')}
        values = getStaticSizeBlockRecordValues(updateCtx, block, packing)
        if not values:
            continue
        lastField = values[lastFieldKey]
        stunNum = values[b'stunNum']
        damageAssistedStun = values[b'damageAssistedStun']
        if damageAssistedStun <= 65535:
            continue
        elif 0 == stunNum:
            setStaticSizeBlockRecordValues(updateCtx, block, {lastFieldKey: (offset - 4, b'I'), b'damageAssistedStun': (
                                     offset + 8, b'I')}, {lastFieldKey: (lastField + (damageAssistedStun & 4294901760L)), b'damageAssistedStun': (damageAssistedStun & 65535)})
        elif 0 != stunNum and damageAssistedStun > 65535:
            if b'a15x15_2' != block:
                continue
            else:
                piercingPacking = {b'noDamageDirectHitsReceived': (16, b'I'), b'directHitsReceived': (12, b'I'), b'potentialDamageReceived': (36, b'I'), 
                   b'piercingsReceived': (20, b'I')}
                damageReceivedPacking = {b'damageReceived': (40, b'I')}
                data = getStaticSizeBlockRecordValues(updateCtx, b'a15x15_2', piercingPacking)
                data.update(getStaticSizeBlockRecordValues(updateCtx, b'a15x15', damageReceivedPacking))
                if data[b'piercingsReceived'] < 50 or data[b'directHitsReceived'] < 50:
                    continue
                else:
                    potentialDamagePerHit = 1.0 * data[b'potentialDamageReceived'] / data[b'directHitsReceived']
                    aproxDamageBlockedByArmor = data[b'potentialDamageReceived'] - data[b'damageReceived']
                    if data[b'noDamageDirectHitsReceived'] < 50 or aproxDamageBlockedByArmor <= 65535:
                        continue
                    potentialDamagePerHitForBlockedDamage = 1.0 * lastField / data[b'noDamageDirectHitsReceived']
                    while aproxDamageBlockedByArmor >= lastField + (damageAssistedStun & 4294901760L) and potentialDamagePerHit > potentialDamagePerHitForBlockedDamage:
                        lastField += 65536
                        damageAssistedStun -= 65536
                        potentialDamagePerHitForBlockedDamage = 1.0 * lastField / data[b'noDamageDirectHitsReceived']

                    if damageAssistedStun >= 0:
                        setStaticSizeBlockRecordValues(updateCtx, block, {lastFieldKey: (offset - 4, b'I'), b'damageAssistedStun': (
                                                 offset + 8, b'I')}, {lastFieldKey: lastField, b'damageAssistedStun': damageAssistedStun})

    setVersion(updateCtx, 96)
    return (96, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier96(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 
     9, 10, 11, 12, 13, 
     14, 15, 
     16, 17, 18, 19, 20, 
     21, 22, 23, 
     24, 25, 
     26, 27, 28, 29, 30, 
     31, 32, 33, 
     34]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'ranked')
    addBlock(updateCtx, b'maxRanked')
    addBlock(updateCtx, b'rankedSeasons')
    setVersion(updateCtx, 97)
    return (97, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier97(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 
     9, 10, 11, 12, 13, 
     14, 15, 
     16, 17, 18, 19, 20, 
     21, 22, 23, 
     24, 25, 
     26, 27, 28, 29, 30, 
     31, 32, 33, 
     34, 35, 
     36, 37]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    vehFortAchievementsPacking = {b'wins': (8, b'H'), 
       b'capturedBasesInAttack': (10, b'H'), b'capturedBasesInDefence': (12, b'H')}
    removeRecords(updateCtx, b'fortAchievements', vehFortAchievementsPacking)
    setVersion(updateCtx, 98)
    return (98, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier98(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 
     9, 10, 11, 12, 13, 
     14, 15, 
     16, 17, 18, 19, 20, 
     21, 22, 23, 
     24, 25, 
     26, 27, 28, 29, 30, 
     31, 32, 33, 
     34, 
     35, 36, 37]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'a30x30')
    addBlock(updateCtx, b'max30x30')
    setVersion(updateCtx, 99)
    return (99, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier99(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'epicBattle')
    addBlock(updateCtx, b'maxEpicBattle')
    addBlock(updateCtx, b'epicBattleAchievements')
    setVersion(updateCtx, 100)
    return (100, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier100(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39, 
     40, 
     41, 
     42]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordsPacking = {b'maxDamage': (3, b'H'), b'maxFrags': (2, b'B'), b'maxXP': (0, b'H')}
    oldValues = getStaticSizeBlockRecordValues(updateCtx, b'epicBattleAchievements', recordsPacking)
    if oldValues:
        newValues = getStaticSizeBlockRecordValues(updateCtx, b'max30x30', recordsPacking)
        if newValues:
            setStaticSizeBlockRecordValues(updateCtx, b'max30x30', recordsPacking, {name: max(oldValues.get(name, 0), newValues.get(name, 0)) for name in recordsPacking.iterkeys()})
        else:
            oldBlockCompDescr = getBlockCompDescr(updateCtx, b'epicBattleAchievements')
            setBlockCompDescr(updateCtx, b'max30x30', oldBlockCompDescr)
    setBlockCompDescr(updateCtx, b'epicBattleAchievements', b'')
    setVersion(updateCtx, 101)
    return (101, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier101(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39, 
     40, 
     41, 
     42]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'maxRankedSeason1')
    addBlock(updateCtx, b'maxRankedSeason2')
    addBlock(updateCtx, b'maxRankedSeason3')
    setVersion(updateCtx, 102)
    return (102, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier102(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39, 
     40, 
     41, 
     42, 
     43, 
     44, 
     45]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordsFormat = [
     (b'marksOfMasteryCount1', b'H'),
     (b'marksOfMasteryCount2', b'H'),
     (b'marksOfMasteryCount3', b'H'),
     (b'marksOfMasteryCount4', b'H')]
    addRecords(updateCtx, b'achievements', recordsFormat, {})
    setVersion(updateCtx, 103)
    return (103, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier103(compDescr):
    blocksLayout = [
     1, 
     2, 
     3, 
     4, 
     5, 
     6, 
     7, 
     8, 
     9, 
     10, 
     11, 
     12, 
     13, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19, 
     20, 
     21, 
     22, 
     23, 
     24, 
     25, 
     26, 
     27, 
     28, 
     29, 
     30, 
     31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39, 
     40, 
     41, 
     42, 
     43, 
     44, 
     45]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    recordsFormat = [
     (b'playedBonusBattles', b'I')]
    addRecords(updateCtx, b'ranked', recordsFormat, {})
    setVersion(updateCtx, 104)
    return (104, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier104(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'ranked_10x10')
    addBlock(updateCtx, b'maxRanked_10x10')
    setVersion(updateCtx, 105)
    return (105, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier105(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    rankedPacking = {b'playedBonusBattles': (116, b'I')}
    rankedValues = getStaticSizeBlockRecordValues(updateCtx, b'ranked', rankedPacking)
    ranked10x10Values = getStaticSizeBlockRecordValues(updateCtx, b'ranked_10x10', rankedPacking)
    ranked10x10Values[b'playedBonusBattles'] = ranked10x10Values.get(b'playedBonusBattles', 0) + rankedValues.get(b'playedBonusBattles', 0)
    playedBonusBattlesRecords = [
     (
      116, b'I', ranked10x10Values[b'playedBonusBattles'])]
    updateStaticSizeBlockRecords(updateCtx, b'ranked_10x10', playedBonusBattlesRecords)
    setVersion(updateCtx, 106)
    return (106, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier106(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season1')
    addBlock(updateCtx, b'maxComp7Season1')
    setVersion(updateCtx, 107)
    return (107, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier107(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season2')
    addBlock(updateCtx, b'maxComp7Season2')
    setVersion(updateCtx, 108)
    return (108, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier108(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'maxAssisted', b'H'),
     (b'maxDamageBlockedByArmor', b'H')]
    addRecords(updateCtx, b'max15x15', formats, {})
    setVersion(updateCtx, 109)
    return (109, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier109(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season3')
    addBlock(updateCtx, b'maxComp7Season3')
    addBlock(updateCtx, b'comp7ArchiveGriffin')
    addBlock(updateCtx, b'maxComp7ArchiveGriffin')
    setVersion(updateCtx, 110)
    return (110, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier110(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51, 52, 
     53, 54, 55]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (124, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), b'droppedCapturePoints': (48, b'I'), 
       b'healthRepair': (128, b'I'), b'directHitsReceived': (64, b'I'), 
       b'comp7PrestigePoints': (120, b'I'), b'explosionHitsReceived': (76, b'I'), 
       b'winAndSurvived': (88, b'I'), b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'damageAssistedStun': (108, b'I'), 
       b'squadWinSeries': (116, b'I'), b'explosionHits': (80, b'I'), b'wins': (8, b'I'), 
       b'poiCapturable': (132, b'I'), b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 3
    archiveSeasonsGriffin(seasonsNumber, updateCtx, comp7SeasonsPacking, comp7SeasonsNewPacking)
    addRecords(updateCtx, b'comp7Season1', [(b'superSquadBattlesCount', b'I'), (b'superSquadWins', b'I')], {})
    addRecords(updateCtx, b'comp7Season2', [(b'superSquadBattlesCount', b'I'), (b'superSquadWins', b'I')], {})
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsGriffin(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    setVersion(updateCtx, 111)
    return (111, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier111(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51, 52, 
     53, 54, 55]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'mt_versusAI')
    addBlock(updateCtx, b'mt_maxVersusAI')
    setVersion(updateCtx, 112)
    return (112, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier112(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51, 52, 
     53, 54, 55, 56, 57]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'comp7Season4')
    addBlock(updateCtx, b'maxComp7Season4')
    setVersion(updateCtx, 113)
    return (113, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier113(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51, 52, 
     53, 54, 55, 56, 57, 
     58, 
     59]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 4
    archiveSeasonsWolf(seasonsNumber, updateCtx, comp7SeasonsNewPacking)
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsWolf(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    setVersion(updateCtx, 114)
    return (114, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier114(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51, 52, 
     53, 54, 55, 56, 57, 
     58, 
     59]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 4
    archiveSeasonsWolf(seasonsNumber, updateCtx, comp7SeasonsNewPacking)
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsWolf(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    setVersion(updateCtx, 115)
    return (115, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier115(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51, 52, 
     53, 54, 55, 56, 57, 
     58, 
     59]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'medalFomin', b'H'),
     (b'medalKrockenberger', b'H'),
     (b'medalGavryushov', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 116)
    return (116, updateCtx[b'dossierCompDescr'])


def __updateFromVehicleDossier116(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 
     14, 15, 16, 17, 
     18, 19, 20, 21, 22, 23, 
     24, 
     25, 26, 27, 28, 
     29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 
     47, 
     48, 49, 50, 51, 52, 
     53, 54, 55, 56, 57, 
     58, 
     59]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    comp7SeasonsNewPacking = {b'spotted': (32, b'I'), b'losses': (12, b'I'), b'roleSkillUsed': (132, b'I'), b'damageAssistedTrack': (56, b'I'), 
       b'damageReceived': (40, b'I'), b'battlesOnStunningVehicles': (100, b'I'), 
       b'piercingsReceived': (72, b'I'), b'originalXP': (52, b'I'), 
       b'damageAssistedRadio': (60, b'I'), b'battlesCount': (4, b'I'), b'survivedBattles': (16, b'I'), 
       b'winSeries': (112, b'I'), b'piercings': (84, b'I'), b'damageBlockedByArmor': (96, b'I'), 
       b'noDamageDirectHitsReceived': (68, b'I'), b'xp': (0, b'I'), 
       b'droppedCapturePoints': (48, b'I'), b'healthRepair': (136, b'I'), b'comp7PrestigePoints': (128, b'I'), 
       b'directHitsReceived': (64, b'I'), b'superSquadWins': (124, b'I'), 
       b'explosionHitsReceived': (76, b'I'), b'winAndSurvived': (88, b'I'), 
       b'capturePoints': (44, b'I'), b'potentialDamageReceived': (92, b'I'), 
       b'damageDealt': (36, b'I'), b'superSquadBattlesCount': (120, b'I'), 
       b'damageAssistedStun': (108, b'I'), b'squadWinSeries': (116, b'I'), 
       b'explosionHits': (80, b'I'), b'wins': (8, b'I'), b'poiCapturable': (140, b'I'), 
       b'frags': (20, b'I'), b'stunNum': (104, b'I'), b'shots': (24, b'I'), 
       b'directHits': (28, b'I')}
    seasonsNumber = 4
    archiveSeasonsWolf(seasonsNumber, updateCtx, comp7SeasonsNewPacking)
    maxComp7SeasonsPacking = {b'maxDamage': (3, b'H'), b'maxXPVehicle': (5, b'I'), b'maxDamageVehicle': (13, b'I'), b'maxFrags': (2, b'B'), 
       b'maxXP': (0, b'H'), b'maxHealthRepair': (29, b'H'), b'maxComp7PrestigePointsVehicle': (19, b'I'), 
       b'maxEquipmentDamageDealt': (23, b'H'), b'maxFragsVehicle': (9, b'I'), 
       b'maxSquadWinSeries': (37, b'H'), b'maxComp7PrestigePoints': (17, b'H'), 
       b'maxWinSeries': (35, b'H'), b'maxEquipmentDamageDealtVehicle': (25, b'I'), 
       b'maxHealthRepairVehicle': (31, b'I')}
    archiveMaxSeasonsWolf(seasonsNumber, updateCtx, maxComp7SeasonsPacking)
    setVersion(updateCtx, 117)
    return (117, updateCtx[b'dossierCompDescr'])


def __bootstrapTankmanDossierFrom(ver, compDescr):
    if ver > 14:
        return (ver, compDescr)
    return (
     TANKMAN_DOSSIER_VERSION, dossiers2.custom.tankmen_dossier1_updater.updateDossierCompDescr(compDescr))


def __addTankmanDossierUpdaters(module, seq):
    for v in seq:
        updaterName = b'__updateFromTankmanDossier%d' % (v,)
        if getattr(module, updaterName, None) is None:
            setattr(module, updaterName, partial(__bootstrapTankmanDossierFrom, v))
            getattr(module, updaterName).__name__ = updaterName

    return


__addTankmanDossierUpdaters(sys.modules[__name__], xrange(10, 64))

def __updateFromTankmanDossier64(compDescr):
    blocksLayout = [
     b'total', b'achievements']
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'achievements', [(b'huntsman', b'H')], {})
    setVersion(updateCtx, 65)
    return (65, updateCtx[b'dossierCompDescr'])


def __updateFromTankmanDossier65(compDescr):
    blocksLayout = [
     b'total', b'achievements']
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addRecords(updateCtx, b'achievements', [(b'sniper2', b'H'), (b'mainGun', b'H')], {})
    setVersion(updateCtx, 66)
    return (66, updateCtx[b'dossierCompDescr'])


def __updateFromTankmanDossier66(compDescr):
    blocksLayout = [
     b'total', b'achievements']
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    formats = [
     (b'medalFomin', b'H'),
     (b'medalKrockenberger', b'H'),
     (b'medalGavryushov', b'H')]
    addRecords(updateCtx, b'achievements', formats, {})
    setVersion(updateCtx, 67)
    return (67, updateCtx[b'dossierCompDescr'])


def __updateFromClubDossier1(compDescr):
    blocksLayout = [
     1, 2, 3, 4, 5]
    updateCtx = {b'dossierCompDescr': compDescr, 
       b'blockSizeFormat': b'H', 
       b'versionFormat': b'H', 
       b'blocksLayout': blocksLayout}
    getHeader(updateCtx)
    addBlock(updateCtx, b'singleAchievementsRated7x7')
    setVersion(updateCtx, 2)
    return (2, updateCtx[b'dossierCompDescr'])


class DossierVersionUpdaterBase(VersionUpdaterBase):

    def __init__(self, logID, functionTemplate, latestVersion):
        super(DossierVersionUpdaterBase, self).__init__(functionTemplate, latestVersion)
        self.__logID = logID
        return

    def updateVersion(self, currentVersion, compDescr):
        return self._updateToLatestVersion(currentVersion, (lambda *args: False), self.__logID, compDescr)[0]


@singleton
class AccountDossierVersionUpdater(DossierVersionUpdaterBase):

    def __init__(self):
        super(self.__class__, self).__init__(b'Account dossier', ACCOUNT_DOSSIER_UPDATE_FUNCTION_TEMPLATE, ACCOUNT_DOSSIER_VERSION)
        return


@singleton
class VehicleDossierVersionUpdater(DossierVersionUpdaterBase):

    def __init__(self):
        super(self.__class__, self).__init__(b'Vehicle dossier', VEHICLE_DOSSIER_UPDATE_FUNCTION_TEMPLATE, VEHICLE_DOSSIER_VERSION)
        return


@singleton
class TankmanDossierVersionUpdater(DossierVersionUpdaterBase):

    def __init__(self):
        super(self.__class__, self).__init__(b'Tankman dossier', TANKMAN_DOSSIER_UPDATE_FUNCTION_TEMPLATE, TANKMAN_DOSSIER_VERSION)
        return


@singleton
class ClanDossierVersionUpdater(DossierVersionUpdaterBase):

    def __init__(self):
        super(self.__class__, self).__init__(b'Clan dossier', CLAN_DOSSIER_UPDATE_FUNCTION_TEMPLATE, CLAN_DOSSIER_VERSION)
        return


@singleton
class Rated7x7DossierVersionUpdater(DossierVersionUpdaterBase):

    def __init__(self):
        super(self.__class__, self).__init__(b'Rated7x7 dossier', RATED7X7_DOSSIER_UPDATE_FUNCTION_TEMPLATE, RATED7X7_DOSSIER_VERSION)
        return


@singleton
class ClubDossierVersionUpdater(DossierVersionUpdaterBase):

    def __init__(self):
        super(self.__class__, self).__init__(b'Club dossier', CLUB_DOSSIER_UPDATE_FUNCTION_TEMPLATE, CLUB_DOSSIER_VERSION)
        return
