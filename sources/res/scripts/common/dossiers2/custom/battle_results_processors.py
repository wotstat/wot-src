import time
from constants import DESTR_CODES_BY_TAGS, GLOBAL_MAP_DIVISION, DOSSIER_TYPE
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from battle_results_helpers import determineWinnerTeam
from debug_utils import LOG_DEBUG_DEV
from dossiers2.custom import records
from dossiers2.custom.config import RECORD_CONFIGS
from dossiers2.custom.cache import getCache
from arena_achievements import INBATTLE_SERIES_INDICES
from arena_achievements_processing.utils import getLevel, getTags
import arena_achievements
_BATTLE_HERO_CONFIG = arena_achievements.ACHIEVEMENT_CONDITIONS
_saveRecordsInAccountDescr = {(BONUS_CAPS.DOSSIER_ACHIEVEMENTS_15X15): [
                                           {b'block': b'achievements', 
                                              b'records': (b'maxInvincibleSeries', b'maxDiehardSeries', b'maxSniperSeries', b'maxKillingSeries', b'maxPiercingSeries', b'maxAimerSeries')}], 
   (BONUS_CAPS.DOSSIER_ACHIEVEMENTS_7X7): [
                                         {b'block': b'achievements7x7', 
                                            b'records': (b'maxTacticalBreakthroughSeries',)}]}

def updateVehicleDossier(dossierDescr, battleResults, dossierXP, vehDescr, avatarResults):
    __updateDossierCommonPart(DOSSIER_TYPE.VEHICLE, dossierDescr, battleResults, dossierXP, avatarResults)
    __updateVehicleDossierImpl(vehDescr, dossierDescr, battleResults, dossierXP)
    return


def getMaxVehResults(results):
    if not results:
        return {}
    tmpVehMaxResults = {}
    for vehTypeCompDescr, vehResults in results.iteritems():
        for record in (b'maxFragsVehicle', b'maxWinPointsVehicle', b'maxDamageVehicle', b'maxXPVehicle', b'maxDamageBlockedByArmorVehicle', b'maxAssistedVehicle'):
            if record == b'maxFragsVehicle':
                kills = len(vehResults[b'killList'])
                if tmpVehMaxResults.get(b'maxFragsVehicle', (0, 0))[1] <= kills:
                    tmpVehMaxResults[b'maxFragsVehicle'] = (
                     vehTypeCompDescr, kills)
            elif record == b'maxWinPointsVehicle':
                winPoints = vehResults[b'winPoints']
                if tmpVehMaxResults.get(b'maxWinPointsVehicle', (0, 0))[1] <= winPoints:
                    tmpVehMaxResults[b'maxWinPointsVehicle'] = (
                     vehTypeCompDescr, winPoints)
            elif record == b'maxDamageVehicle':
                damageDealt = vehResults[b'damageDealt']
                if tmpVehMaxResults.get(b'maxDamageVehicle', (0, 0))[1] <= damageDealt:
                    tmpVehMaxResults[b'maxDamageVehicle'] = (
                     vehTypeCompDescr, damageDealt)
            elif record == b'maxXPVehicle':
                xp = vehResults[b'xp']
                if tmpVehMaxResults.get(b'maxXPVehicle', (0, 0))[1] <= xp:
                    tmpVehMaxResults[b'maxXPVehicle'] = (
                     vehTypeCompDescr, xp)
            elif record == b'maxDamageBlockedByArmorVehicle':
                damageBlockedByArmor = vehResults[b'damageBlockedByArmor']
                if tmpVehMaxResults.get(b'maxDamageBlockedByArmorVehicle', (0, 0))[1] <= damageBlockedByArmor:
                    tmpVehMaxResults[b'maxDamageBlockedByArmorVehicle'] = (
                     vehTypeCompDescr, damageBlockedByArmor)
            elif record == b'maxAssistedVehicle':
                assisted = vehResults[b'damageAssistedTrack'] + vehResults[b'damageAssistedRadio'] + vehResults[b'damageAssistedStun']
                if tmpVehMaxResults.get(b'maxAssistedVehicle', (0, 0))[1] <= assisted:
                    tmpVehMaxResults[b'maxAssistedVehicle'] = (
                     vehTypeCompDescr, assisted)

    return {key: value[0] for key, value in tmpVehMaxResults.iteritems()}


def updateAccountDossier(dossierDescr, battleResults, dossierXP, vehDossiers, maxVehResults, avatarResults):
    bonusType = battleResults[b'bonusType']
    maxValuesChanged, frags8p = __updateDossierCommonPart(DOSSIER_TYPE.ACCOUNT, dossierDescr, battleResults, dossierXP, avatarResults)
    checkAny = BONUS_CAPS.checkAny
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_15X15) or checkAny(bonusType, BONUS_CAPS.DOSSIER_30X30):
        for func in STEAM_UPDATE:
            func(dossierDescr, battleResults, vehDossiers)

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_ACHIEVEMENTS):
        for vehTypeCompDescr, (_, vehDossierDescr) in vehDossiers.iteritems():
            __updateAccountRecords(BONUS_CAPS.get(bonusType), dossierDescr, vehDossierDescr)

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_7X7):
        __updateCapturePointsWithBaseCapture(dossierDescr, battleResults)
        __updateDefencePoints(dossierDescr, battleResults)
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_SORTIE):
        updateAggregatedValues(dossierDescr.expand(b'fortSortiesInClan'), dossierDescr.expand(b'fortSortiesInClan'), battleResults, dossierXP, frags8p)
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_FORT_BATTLE):
        updateAggregatedValues(dossierDescr.expand(b'fortBattlesInClan'), dossierDescr.expand(b'fortBattlesInClan'), battleResults, dossierXP, frags8p)
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_RATED7X7):
        clubDBID = battleResults[b'club'].get(b'clubDBID', 0)
        achievementsRated7x7 = dossierDescr[b'achievementsRated7x7']
        if clubDBID != achievementsRated7x7[b'victoryMarchClubDBID']:
            achievementsRated7x7[b'victoryMarchClubDBID'] = clubDBID
            achievementsRated7x7[b'victoryMarchSeries'] = 0
        _updatePerBattleSeries(dossierDescr[b'achievementsRated7x7'], b'victoryMarchSeries', battleResults[b'winnerTeam'] == battleResults[b'team'])
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_GLOBAL_MAP):
        division = battleResults[b'division']
        if division in GLOBAL_MAP_DIVISION._ORDER:
            if division == GLOBAL_MAP_DIVISION.MIDDLE:
                blockName = b'globalMapMiddle'
                blockNameMax = b'maxGlobalMapMiddle'
            elif division == GLOBAL_MAP_DIVISION.CHAMPION:
                blockName = b'globalMapChampion'
                blockNameMax = b'maxGlobalMapChampion'
            elif division == GLOBAL_MAP_DIVISION.ABSOLUTE:
                blockName = b'globalMapAbsolute'
                blockNameMax = b'maxGlobalMapAbsolute'
            updateAggregatedValues(dossierDescr.expand(blockName), dossierDescr.expand(blockName), battleResults, dossierXP, frags8p)
            values = updateMaxValues(dossierDescr.expand(blockNameMax), battleResults, dossierXP)
            block = dossierDescr[blockNameMax]
            for record in values:
                block[record] = maxVehResults[record]

            for record in maxValuesChanged:
                block[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_RANKED):
        updateAggregatedValues(dossierDescr.expand(b'ranked_10x10'), dossierDescr.expand(b'ranked_10x10'), battleResults, dossierXP, frags8p)
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_EPIC_BATTLE):
        __processSupplyKillList(dossierDescr, battleResults[b'suppliesKilled'])
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX15X15):
        max15x15 = dossierDescr[b'max15x15']
        for record in maxValuesChanged:
            max15x15[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX30X30):
        max30x30 = dossierDescr[b'max30x30']
        for record in maxValuesChanged:
            max30x30[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX7X7):
        max7x7 = dossierDescr[b'max7x7']
        for record in maxValuesChanged:
            max7x7[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXRATED7X7):
        maxRated7x7 = dossierDescr[b'maxRated7x7']
        for record in maxValuesChanged:
            maxRated7x7[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXFALLOUT):
        __updateMaxValuesWithAvatar(dossierDescr[b'maxFallout'], battleResults)
    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXSORTIE):
        values = updateMaxValues(dossierDescr.expand(b'maxFortSortiesInClan'), battleResults, dossierXP)
        maxFortSortiesInClan = dossierDescr[b'maxFortSortiesInClan']
        for record in values:
            maxFortSortiesInClan[record] = maxVehResults[record]

        maxFortSorties = dossierDescr[b'maxFortSorties']
        for record in maxValuesChanged:
            maxFortSorties[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXFORTBATTLE):
        values = updateMaxValues(dossierDescr.expand(b'maxFortBattlesInClan'), battleResults, dossierXP)
        maxFortBattlesInClan = dossierDescr[b'maxFortBattlesInClan']
        for record in values:
            maxFortBattlesInClan[record] = maxVehResults[record]

        maxFortBattles = dossierDescr[b'maxFortBattles']
        for record in maxValuesChanged:
            maxFortBattles[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXRANKED):
        seasonBlock = b'maxRanked_10x10'
        values = updateMaxValues(dossierDescr.expand(seasonBlock), battleResults, dossierXP)
        seasonBlock = dossierDescr[seasonBlock]
        for record in values:
            seasonBlock[record] = maxVehResults[record]

    if checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX_EPIC_BATTLE):
        maxEpicBattle = dossierDescr[b'maxEpicBattle']
        for record in maxValuesChanged:
            maxEpicBattle[record] = maxVehResults[record]

    __updateSteamMasteryMarks(dossierDescr, battleResults, vehDossiers)
    for vehTypeCompDescr, (_, vehDossierDescr) in vehDossiers.iteritems():
        __updateAccountDossierCuts(dossierDescr, battleResults, dossierXP, vehTypeCompDescr, vehDossierDescr, avatarResults)

    return


def __updateAccountRecords(bonusCaps, dossierDescr, vehDossierDescr):
    for cap, descr in _saveRecordsInAccountDescr.iteritems():
        if cap in bonusCaps:
            for item in descr:
                blockName = item[b'block']
                achievements = dossierDescr[blockName]
                vehAchievements = vehDossierDescr[blockName]
                for recordName in item[b'records']:
                    if vehAchievements[recordName] > achievements[recordName]:
                        achievements[recordName] = vehAchievements[recordName]

    return


def updateRated7x7Dossier(dossierDescr, battleResults, dossierXP):
    bonusType = battleResults[b'bonusType']
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_RATED7X7):
        updateAggregatedValues(dossierDescr.expand(b'rated7x7'), dossierDescr.expand(b'rated7x7'), battleResults, dossierXP, frags8p=0)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXRATED7X7):
        updateMaxValues(dossierDescr.expand(b'maxRated7x7'), battleResults, dossierXP)
    return


def updateTankmanDossier(dossierDescr, battleResults):
    __updateTankmanDossierImpl(dossierDescr, battleResults)
    return


def updatePMQuestAchievements(accDossierDescr, progress):
    import pm_quests
    achievementCounters = dict()
    completedCounters = dict()
    tileCache = pm_quests.g_tileCache
    for questID, (flags, state) in progress.iteritems():
        if state < pm_quests.PM_STATE.NEED_GET_MAIN_REWARD:
            continue
        pmQuestType = pm_quests.g_cache.questByPMQuestID(questID)
        tileInfo = tileCache.getTileInfo(pmQuestType.tileID)
        seasonID = tileInfo[b'seasonID']
        completedCounters[seasonID] = completedCounters.get(seasonID, 0) + 1
        if state >= pm_quests.PM_STATE.NEED_GET_ADD_REWARD:
            pmQuestsAchievements = tileInfo[b'achievements'] or {}
            chainAchievement = pmQuestsAchievements.get(pmQuestType.chainID, None)
            if chainAchievement:
                achievementCounters[chainAchievement] = achievementCounters.get(chainAchievement, 0) + 1

    for seasonID, minCounter, dossierBlockName, achievementName in ((1, 1, b'singleAchievements', b'firstMerit'),
     (1, 1, b'steamAchievements', b'steamDoPersonalMissionQuestMedal'),
     (2, 5, b'singleAchievements', b'newMeritPM2'),
     (2, 1, b'steamAchievements', b'steamDoPersonalMissionQuestMedal')):
        needToAward = completedCounters.get(seasonID, 0) >= minCounter
        if needToAward and not accDossierDescr[dossierBlockName][achievementName]:
            accDossierDescr[dossierBlockName][achievementName] = True

    for chainAchievement, counter in achievementCounters.iteritems():
        if chainAchievement not in RECORD_CONFIGS:
            continue
        steps = RECORD_CONFIGS[chainAchievement]
        maxLevel = len(steps)
        level = sum(1 for i in xrange(maxLevel) if counter >= steps[i])
        stage = 0 if level == 0 else maxLevel - level + 1
        currStage = accDossierDescr[b'achievements'][chainAchievement]
        if currStage == 0 or stage < currStage:
            accDossierDescr[b'achievements'][chainAchievement] = stage

    return


def __updateDossierCommonPart(dossierType, dossierDescr, results, dossierXP, avatarResults):
    bonusType = results[b'bonusType']
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_TOTAL):
        __updateTotalValues(dossierDescr, results)
    frags8p = 0
    maxValuesChanged = []
    LOG_DEBUG_DEV(b'__updateDossierCommonPart', bonusType)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_KILL_LIST):
        frags8p = __processKillList(dossierDescr, results[b'killList'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_15X15):
        updateAggregatedValues(dossierDescr.expand(b'a15x15'), dossierDescr.expand(b'a15x15_2'), results, dossierXP, frags8p)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_30X30):
        updateAggregatedValues(dossierDescr.expand(b'a30x30'), dossierDescr.expand(b'a30x30'), results, dossierXP, frags8p)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_7X7):
        updateAggregatedValues(dossierDescr.expand(b'a7x7'), dossierDescr.expand(b'a7x7'), results, dossierXP, frags8p)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_RATED7X7):
        updateAggregatedValues(dossierDescr.expand(b'rated7x7'), dossierDescr.expand(b'rated7x7'), results, dossierXP, frags8p)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_CLAN):
        __updateBaseStatistics(dossierDescr.expand(b'clan'), dossierDescr.expand(b'clan2'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_FALLOUT):
        updateAggregatedValues(dossierDescr.expand(b'fallout'), dossierDescr.expand(b'fallout'), results, dossierXP, frags8p)
        for record in (b'winPoints', b'flagCapture', b'soloFlagCapture', b'resourceAbsorbed', b'deathCount'):
            dossierDescr[b'fallout'][record] += results[record]

        if dossierType == DOSSIER_TYPE.ACCOUNT:
            for record in (b'avatarDamageDealt', b'avatarKills'):
                dossierDescr[b'fallout'][record] += results[record]

    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_GLOBAL_MAP):
        if dossierDescr.isBlockInLayout(b'globalMapCommon'):
            updateAggregatedValues(dossierDescr.expand(b'globalMapCommon'), dossierDescr.expand(b'globalMapCommon'), results, dossierXP, frags8p)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_SORTIE):
        updateAggregatedValues(dossierDescr.expand(b'fortSorties'), dossierDescr.expand(b'fortSorties'), results, dossierXP, frags8p)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_FORT_BATTLE):
        updateAggregatedValues(dossierDescr.expand(b'fortBattles'), dossierDescr.expand(b'fortBattles'), results, dossierXP, frags8p, determineWinnerTeam(avatarResults))
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_EPIC_BATTLE):
        updateAggregatedValues(dossierDescr.expand(b'epicBattle'), dossierDescr.expand(b'epicBattle'), results, dossierXP, frags8p)
        for record in [b'deathCount']:
            dossierDescr[b'epicBattle'][record] += results[record]

    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_ACHIEVEMENTS, BONUS_CAPS.DOSSIER_ACHIEVEMENTS_FALLOUT):
        for recordDBID in results[b'achievements']:
            __processArenaAchievement(dossierDescr, recordDBID)

    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX15X15):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'max15x15'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX30X30):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'max30x30'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX7X7):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'max7x7'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXRATED7X7):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'maxRated7x7'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXSORTIE):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'maxFortSorties'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXFORTBATTLE):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'maxFortBattles'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXRANKED):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'maxRanked_10x10'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_GLOBAL_MAP):
        if dossierDescr.isBlockInLayout(b'maxGlobalMapCommon'):
            maxValuesChanged = updateMaxValues(dossierDescr.expand(b'maxGlobalMapCommon'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXFALLOUT):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'maxFallout'), results, dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAX_EPIC_BATTLE):
        maxValuesChanged = updateMaxValues(dossierDescr.expand(b'maxEpicBattle'), results, dossierXP)
    return (maxValuesChanged, frags8p)


def __updateTotalValues(dossierDescr, results):
    total = dossierDescr.expand(b'total')
    total[b'battleLifeTime'] += results[b'lifeTime']
    total[b'lastBattleTime'] = int(time.time())
    total[b'treesCut'] += results[b'destroyedObjects'].get(DESTR_CODES_BY_TAGS[b'tree'], 0)
    total[b'mileage'] += results[b'mileage']
    return


def __processKillList(dossierDescr, killList):
    if not killList:
        return 0
    cache = getCache()
    vehicles8p = cache[b'vehicles8+']
    vehiclesByTag = cache[b'vehiclesByTag']
    frags8p = 0
    killsByTag = {}
    vehTypeFrags = dossierDescr[b'vehTypeFrags']
    vehTypeFragsGet = vehTypeFrags.get
    killsByTagGet = killsByTag.get
    for _, vehTypeCompDescr, _ in killList:
        vehTypeFrags[vehTypeCompDescr] = min(vehTypeFragsGet(vehTypeCompDescr, 0) + 1, 60001)
        if vehTypeCompDescr in vehicles8p:
            frags8p += 1
        for tag, record in ((b'beast', b'fragsBeast'), (b'sinai', b'fragsSinai'),
         (b'patton', b'fragsPatton')):
            if vehTypeCompDescr in vehiclesByTag[tag]:
                killsByTag[record] = killsByTagGet(record, 0) + 1

    if killsByTag:
        achievements = dossierDescr[b'achievements']
        for record, frags in killsByTag.iteritems():
            achievements[record] += frags

    return frags8p


def __processSupplyKillList(dossierDescr, supplyKillList):
    if not supplyKillList:
        return 0
    vehTypeFrags = dossierDescr[b'vehTypeFrags']
    vehTypeFragsGet = vehTypeFrags.get
    for vehTypeCompDescr in supplyKillList:
        vehTypeFrags[vehTypeCompDescr] = min(vehTypeFragsGet(vehTypeCompDescr, 0) + 1, 60001)

    return


def updateAggregatedValues(block, block2, results, dossierXP, frags8p, winnerTeam=None):
    __updateBaseStatistics(block, block2, results, dossierXP, winnerTeam)
    if results[b'deathCount'] == 0 and results[b'winnerTeam'] == results[b'team']:
        block[b'winAndSurvived'] += 1
    if frags8p != 0:
        block[b'frags8p'] += frags8p
    return


def __updateBaseStatistics(block, block2, results, dossierXP, winnerTeam=None):
    block[b'battlesCount'] += 1
    if results[b'canStun']:
        block2[b'battlesOnStunningVehicles'] += 1
    if dossierXP != 0:
        block[b'xp'] += dossierXP
        block2[b'originalXP'] += results[b'originalXP']
    if not winnerTeam:
        winnerTeam = results[b'winnerTeam']
    if winnerTeam == results[b'team']:
        block[b'wins'] += 1
    elif winnerTeam == 0:
        pass
    else:
        block[b'losses'] += 1
    if results[b'deathCount'] == 0:
        block[b'survivedBattles'] += 1
    directHits = results[b'directEnemyHits']
    if directHits != 0:
        block[b'directHits'] += directHits
    for record in (b'shots', b'spotted', b'damageDealt', b'damageReceived', b'capturePoints'):
        if bool(results[record]):
            block[record] += results[record]

    droppedCapturePoints = min(results[b'droppedCapturePoints'], 100)
    if droppedCapturePoints != 0:
        block[b'droppedCapturePoints'] += droppedCapturePoints
    kills = len(results[b'killList'])
    if kills:
        block[b'frags'] += kills
    for record in (b'damageAssistedTrack', b'damageAssistedRadio', b'directHitsReceived', b'noDamageDirectHitsReceived', b'piercingsReceived', b'explosionHitsReceived', b'explosionHits', b'piercings', b'potentialDamageReceived', b'damageBlockedByArmor', b'stunNum', b'damageAssistedStun'):
        if bool(results[record]):
            block2[record] += results[record]

    return


def __processArenaAchievement(dossierDescr, recordDBID):
    block, record = records.DB_ID_TO_RECORD[recordDBID]
    if not dossierDescr.isBlockInLayout(block):
        return
    blockDescr = dossierDescr[block]
    if record not in blockDescr:
        return
    blockDescr[record] += 1
    return


def updateMaxValues(block, results, dossierXP):
    maxValuesChanged = []
    if dossierXP != 0 and dossierXP >= block[b'maxXP']:
        block[b'maxXP'] = dossierXP
        maxValuesChanged.append(b'maxXPVehicle')
    kills = len(results[b'killList'])
    if kills > 0 and kills >= block[b'maxFrags']:
        block[b'maxFrags'] = kills
        maxValuesChanged.append(b'maxFragsVehicle')
    damageDealt = results[b'damageDealt']
    if damageDealt > 0 and damageDealt >= block[b'maxDamage']:
        block[b'maxDamage'] = damageDealt
        maxValuesChanged.append(b'maxDamageVehicle')
    if BONUS_CAPS.checkAny(results[b'bonusType'], BONUS_CAPS.DOSSIER_MAXFALLOUT):
        winPoints = results[b'winPoints']
        if winPoints > 0 and winPoints >= block[b'maxWinPoints']:
            block[b'maxWinPoints'] = winPoints
        maxValuesChanged.append(b'maxWinPointsVehicle')
    if BONUS_CAPS.checkAny(results[b'bonusType'], BONUS_CAPS.DOSSIER_MAX15X15):
        damageBlockedByArmor = results[b'damageBlockedByArmor']
        if damageBlockedByArmor > 0 and damageBlockedByArmor >= block[b'maxDamageBlockedByArmor']:
            block[b'maxDamageBlockedByArmor'] = damageBlockedByArmor
            maxValuesChanged.append(b'maxDamageBlockedByArmorVehicle')
        assisted = results[b'damageAssistedTrack'] + results[b'damageAssistedRadio'] + results[b'damageAssistedStun']
        if assisted > 0 and assisted >= block[b'maxAssisted']:
            block[b'maxAssisted'] = assisted
            maxValuesChanged.append(b'maxAssistedVehicle')
    return maxValuesChanged


def __updateMaxValuesWithAvatar(block, results):
    if BONUS_CAPS.checkAny(results[b'bonusType'], BONUS_CAPS.DOSSIER_MAXFALLOUT):
        kills = len(results[b'killList']) + results[b'avatarKills']
        if kills > 0 and kills >= block[b'maxFragsWithAvatar']:
            block[b'maxFragsWithAvatar'] = kills
        damageDealt = results[b'damageDealt'] + results[b'avatarDamageDealt']
        if damageDealt > 0 and damageDealt >= block[b'maxDamageWithAvatar']:
            block[b'maxDamageWithAvatar'] = damageDealt
    return


def __updateMarksOnGun(dossierDescr, results):
    if not BONUS_CAPS.checkAny(results[b'bonusType'], BONUS_CAPS.DOSSIER_MARKS_ON_GUN):
        return
    achievements = dossierDescr[b'achievements']
    damageRating = int(results[b'damageRating'] * 100)
    if damageRating != 0:
        achievements[b'damageRating'] = damageRating
    achievements[b'movingAvgDamage'] = results[b'movingAvgDamage']
    if achievements[b'marksOnGun'] < results[b'marksOnGun']:
        achievements[b'marksOnGun'] = results[b'marksOnGun']
    return


def __updateMarkOfMastery(dossierDescr, results):
    if not BONUS_CAPS.checkAny(results[b'bonusType'], BONUS_CAPS.DOSSIER_MARK_OF_MASTERY):
        return
    achievements = dossierDescr[b'achievements']
    markOfMasterField = (b'marksOfMasteryCount{}').format(results[b'markOfMastery'])
    if markOfMasterField in achievements:
        achievements[markOfMasterField] += 1
    if achievements[b'markOfMastery'] < results[b'markOfMastery']:
        achievements[b'markOfMastery'] = results[b'markOfMastery']
    return


def __updateVehicleDossierImpl(vehDescr, dossierDescr, results, dossierXP):
    bonusType = results[b'bonusType']
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_ACHIEVEMENTS_7X7):
        _updatePerBattleSeries(dossierDescr[b'achievements7x7'], b'tacticalBreakthroughSeries', results[b'winnerTeam'] == results[b'team'])
        return
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_RANKED):
        updateAggregatedValues(dossierDescr.expand(b'ranked_10x10'), dossierDescr.expand(b'ranked_10x10'), results, dossierXP, 0)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MAXRANKED):
        updateMaxValues(dossierDescr.expand(b'maxRanked_10x10'), results, dossierXP)
    __updateMarksOnGun(dossierDescr, results)
    __updateMarkOfMastery(dossierDescr, results)
    if not BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_ACHIEVEMENTS_15X15):
        return
    achievements = dossierDescr[b'achievements']
    if results[b'winnerTeam'] == results[b'team'] and results[b'aimerSeries'] > 0:
        dossierDescr[b'singleAchievements'][b'aimer'] = 1
        if achievements[b'maxAimerSeries'] < results[b'aimerSeries']:
            achievements[b'maxAimerSeries'] = results[b'aimerSeries']
    noDeath = b'SPG' not in vehDescr.type.tags and results[b'deathCount'] == 0
    _updatePerBattleSeries(achievements, b'invincibleSeries', results[b'damageReceived'] == 0 and noDeath)
    _updatePerBattleSeries(achievements, b'diehardSeries', noDeath)
    _updateInBattleSeries(achievements, b'killing', results)
    if not vehDescr.isAutoShootGunVehicle:
        _updateInBattleSeries(achievements, b'sniper', results)
        _updateInBattleSeries(achievements, b'piercing', results)
    return


def _updatePerBattleSeries(achievements, achieveName, isNotInterrupted):
    if isNotInterrupted:
        achievements[achieveName] += 1
    else:
        achievements[achieveName] = 0
    return


def _updateInBattleSeries(achievements, seriesName, results):
    seriesIdx = INBATTLE_SERIES_INDICES[seriesName]
    recordName = seriesName + b'Series'
    series = results[b'series'].get(seriesIdx, [])
    if series:
        achievements[recordName] = achievements[recordName] + series[0]
    for runLength in series[1:]:
        achievements[recordName] = runLength

    return


def __updateAccountDossierCuts(dossierDescr, results, dossierXP, vehTypeCompDescr, vehDossierDescr, avatarResults):
    bonusType = results[b'bonusType']
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_15X15):
        a15x15Cut = dossierDescr[b'a15x15Cut']
        vehA15x15 = vehDossierDescr[b'a15x15']
        a15x15Cut[vehTypeCompDescr] = (
         vehA15x15[b'battlesCount'],
         vehA15x15[b'wins'],
         vehA15x15[b'xp'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_30X30):
        a30x30Cut = dossierDescr[b'a30x30Cut']
        vehA30x30 = vehDossierDescr[b'a30x30']
        a30x30Cut[vehTypeCompDescr] = (
         vehA30x30[b'battlesCount'],
         vehA30x30[b'wins'],
         vehA30x30[b'xp'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_7X7):
        a7x7Cut = dossierDescr[b'a7x7Cut']
        vehA7x7 = vehDossierDescr[b'a7x7']
        a7x7Cut[vehTypeCompDescr] = (
         vehA7x7[b'battlesCount'],
         vehA7x7[b'wins'],
         vehA7x7[b'xp'],
         vehA7x7[b'originalXP'],
         vehA7x7[b'damageDealt'],
         vehA7x7[b'damageAssistedRadio'],
         vehA7x7[b'damageAssistedTrack'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_SORTIE):
        sortieCut = dossierDescr[b'fortSortiesCut']
        vehSortie = vehDossierDescr[b'fortSorties']
        sortieCut[vehTypeCompDescr] = (
         vehSortie[b'battlesCount'],
         vehSortie[b'wins'],
         vehSortie[b'xp'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_FORT_BATTLE):
        battleCut = dossierDescr[b'fortBattlesCut']
        vehBattles = vehDossierDescr[b'fortBattles']
        battleCut[vehTypeCompDescr] = (
         vehBattles[b'battlesCount'],
         vehBattles[b'wins'],
         vehBattles[b'xp'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_SUMMARY_VEHICLE_RANKED_CUT):
        cut = dossierDescr[b'rankedCut']
        veh = vehDossierDescr[b'ranked_10x10']
        cut[vehTypeCompDescr] = (
         veh[b'battlesCount'],
         veh[b'wins'],
         veh[b'xp'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_RANKED):
        currentCut = dossierDescr[b'rankedCut_10x10']
        battlesCount, wins, xp = currentCut.get(vehTypeCompDescr, (0, 0, 0))
        win = 1 if results[b'winnerTeam'] == results[b'team'] else 0
        currentCut[vehTypeCompDescr] = (battlesCount + 1, wins + win, xp + dossierXP)
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_RATED7X7):
        rated7x7Cut = dossierDescr[b'rated7x7Cut']
        vehRated7x7 = vehDossierDescr[b'rated7x7']
        rated7x7Cut[vehTypeCompDescr] = (
         vehRated7x7[b'battlesCount'],
         vehRated7x7[b'wins'],
         vehRated7x7[b'xp'],
         vehRated7x7[b'originalXP'],
         vehRated7x7[b'damageDealt'],
         vehRated7x7[b'damageAssistedRadio'],
         vehRated7x7[b'damageAssistedTrack'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_GLOBAL_MAP):
        globalMapCommonCut = dossierDescr[b'globalMapCommonCut']
        vehGlobalMapCommon = vehDossierDescr[b'globalMapCommon']
        globalMapCommonCut[vehTypeCompDescr] = (
         vehGlobalMapCommon[b'battlesCount'],
         vehGlobalMapCommon[b'wins'],
         vehGlobalMapCommon[b'xp'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_FALLOUT):
        falloutAccountDossierCut = dossierDescr[b'falloutCut']
        falloutVehicleDossier = vehDossierDescr[b'fallout']
        falloutAccountDossierCut[vehTypeCompDescr] = (
         falloutVehicleDossier[b'battlesCount'],
         falloutVehicleDossier[b'wins'],
         falloutVehicleDossier[b'xp'],
         falloutVehicleDossier[b'winPoints'])
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_MARK_OF_MASTERY):
        if vehDossierDescr[b'achievements'][b'markOfMastery'] != 0:
            markOfMasteryCut = dossierDescr[b'markOfMasteryCut']
            markOfMasteryCut[vehTypeCompDescr] = vehDossierDescr[b'achievements'][b'markOfMastery']
    if BONUS_CAPS.checkAny(bonusType, BONUS_CAPS.DOSSIER_EPIC_BATTLE):
        epicBattleAccountDossierCut = dossierDescr[b'epicBattleCut']
        epicBattleVehicleDossier = vehDossierDescr[b'epicBattle']
        epicBattleAccountDossierCut[vehTypeCompDescr] = (
         epicBattleVehicleDossier[b'battlesCount'], epicBattleVehicleDossier[b'wins'],
         epicBattleVehicleDossier[b'xp'])
    return


def __updateTankmanDossierImpl(dossierDescr, results):
    if not BONUS_CAPS.checkAny(results[b'bonusType'], BONUS_CAPS.DOSSIER_TOTAL):
        return
    dossierDescr[b'total'][b'battlesCount'] += 1
    if not BONUS_CAPS.checkAny(results[b'bonusType'], BONUS_CAPS.DOSSIER_ACHIEVEMENTS_15X15):
        return
    for recordDBID in results[b'achievements']:
        __processArenaAchievement(dossierDescr, recordDBID)

    return


def __updateCapturePointsWithBaseCapture(dossierDescr, results):
    if results[b'isEnemyBaseCaptured'] and results[b'winnerTeam'] == results[b'team']:
        dossierDescr[b'achievements7x7'][b'infiltrator'] += results[b'capturePoints']
    return


def __updateDefencePoints(dossierDescr, results):
    if results[b'winnerTeam'] == results[b'team']:
        dossierDescr[b'achievements7x7'][b'sentinel'] += results[b'droppedCapturePoints']
    return


def __updateSteamBasePoints(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamBasePointsMedal']:
        return
    if results[b'isEnemyBaseCaptured'] and results[b'winnerTeam'] == results[b'team']:
        dossierDescr[b'steamAchievements'][b'steamBasePoints'] += results[b'capturePoints']
    dossierDescr[b'steamAchievements'][b'steamBasePoints'] += results[b'droppedCapturePoints']
    return


def __updateSteamFighter(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamFighterMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        killerLevel = getLevel(vehTypeCompDescr)
        break

    for _, victimTypeCompDescr, _ in results[b'killList']:
        victimLevel = getLevel(victimTypeCompDescr)
        if victimLevel - killerLevel >= RECORD_CONFIGS[b'steamFighterMedal']:
            dossierDescr[b'steamAchievements'][b'steamFighterMedal'] = True

    return


def __updateSteamHardCharacter(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamHardCharacterMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'heavyTank' not in getTags(vehTypeCompDescr):
            return
        break

    dossierDescr[b'steamAchievements'][b'steamHardCharacter'] += results[b'damageBlockedByArmor']
    return


def __updateSteamMedium(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamMediumMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'mediumTank' not in getTags(vehTypeCompDescr):
            return
        break

    dossierDescr[b'steamAchievements'][b'steamMedium'] += results[b'damageDealt']
    return


def __updateSteamATSPG(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamATSPGMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'AT-SPG' not in getTags(vehTypeCompDescr):
            return
        break

    dossierDescr[b'steamAchievements'][b'steamATSPG'] += results[b'damageDealt']
    return


def __updateSteamDieHard(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamDieHardMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'heavyTank' not in getTags(vehTypeCompDescr):
            return
        break

    value = results[b'damageDealt'] + results[b'damageBlockedByArmor'] + results[b'damageReceived']
    if value >= RECORD_CONFIGS[b'steamDieHardMedal']:
        dossierDescr[b'steamAchievements'][b'steamDieHardMedal'] = True
    return


def __updateSteamDestroyer(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamDestroyerMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'AT-SPG' not in getTags(vehTypeCompDescr):
            return
        break

    if results[b'damageDealt'] >= RECORD_CONFIGS[b'steamDestroyerMedal'] and len(results[b'killList']) >= 2:
        dossierDescr[b'steamAchievements'][b'steamDestroyerMedal'] = True
    return


def __updateSteamMediumPerformance(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamMediumPerformanceMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'mediumTank' not in getTags(vehTypeCompDescr):
            return
        break

    if results[b'damageDealt'] >= RECORD_CONFIGS[b'steamMediumPerformanceMedal']:
        dossierDescr[b'steamAchievements'][b'steamMediumPerformanceMedal'] = True
    return


def __updateSteamReconnoiter(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamReconnoiterMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'lightTank' not in getTags(vehTypeCompDescr):
            return
        break

    dossierDescr[b'steamAchievements'][b'steamReconnoiter'] += results[b'damageAssistedRadio']
    return


def __updateSteamPotentialStun(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamPotentialStunMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'SPG' not in getTags(vehTypeCompDescr):
            return
        break

    dossierDescr[b'steamAchievements'][b'steamPotentialStun'] += results[b'stunDuration']
    return


def __updateSteamMileage(dossierDescr, results, vehDossiers):
    if not dossierDescr[b'steamAchievements'][b'steamMileageMedal'] and results[b'mileage']:
        dossierDescr[b'steamAchievements'][b'steamMileage'] += int(round(results[b'mileage'], -1))
    return


def __updateSteamHorizonSupport(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamHorizonSupportMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'SPG' not in getTags(vehTypeCompDescr):
            return
        break

    value = results[b'damageAssistedStun'] + results[b'damageAssistedTrack']
    if value >= RECORD_CONFIGS[b'steamHorizonSupportMedal']:
        dossierDescr[b'steamAchievements'][b'steamHorizonSupportMedal'] = True
    return


def __updateSteamSmallSupport(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamSmallSupportMedal']:
        return
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        if b'lightTank' not in getTags(vehTypeCompDescr):
            return
        break

    value = results[b'damageAssistedRadio'] + results[b'damageAssistedTrack'] + results[b'damageDealt']
    if value >= RECORD_CONFIGS[b'steamSmallSupportMedal']:
        dossierDescr[b'steamAchievements'][b'steamSmallSupportMedal'] = True
    return


def __updateSteamMasteryMarks(dossierDescr, results, vehDossiers):
    if results[b'markOfMastery'] == RECORD_CONFIGS[b'steamMasteryMarksMedal3'] and not dossierDescr[b'steamAchievements'][b'steamNotPerfectMedal']:
        dossierDescr[b'steamAchievements'][b'steamNotPerfectMedal'] = True
    if dossierDescr[b'steamAchievements'][b'steamGoldenFiveMedal']:
        return
    if results[b'markOfMastery'] == RECORD_CONFIGS[b'steamMasteryMarksMedal']:
        dossierDescr[b'steamAchievements'][b'steamMasteryMarks'] += 1
        if not dossierDescr[b'steamAchievements'][b'steamNotPerfectMedal']:
            dossierDescr[b'steamAchievements'][b'steamNotPerfectMedal'] = True
    return


def __updateSteamCumulativeMedalsCounters(dossierDescr, results, vehDossiers):
    if not dossierDescr[b'steamAchievements'][b'steamKingMidasMedal']:
        dossierDescr[b'steamAchievements'][b'steamBattleCredits'] += results[b'originalCredits']
    if not dossierDescr[b'steamAchievements'][b'steamExperienceMedal']:
        dossierDescr[b'steamAchievements'][b'steamBattleXP'] += results[b'originalXP']
    if not dossierDescr[b'steamAchievements'][b'steamPowerKnowledgeMedal']:
        dossierDescr[b'steamAchievements'][b'steamFreeXP'] += results[b'originalFreeXP']
    return


def __updateSteamBreakThrough(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamBreakThroughMedal']:
        return
    dossierDescr[b'steamAchievements'][b'steamBreakThrough'] += results[b'piercingEnemyHits']
    return


def __updateSteamStop(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamStopMedal']:
        return
    else:
        critsByType = results[b'critsByType']
        if critsByType.get(b'destroyed') is not None and critsByType.get(b'destroyed').get(b'track') is not None:
            dossierDescr[b'steamAchievements'][b'steamStop'] += critsByType[b'destroyed'][b'track']
        return


def __updateSteamRandomFight(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamRandomFightMedal']:
        return
    dossierDescr[b'steamAchievements'][b'steamRandomFightMedal'] = True
    return


def __updateSteamMainGun(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamMainGunMedal']:
        return
    team = 2 if results[b'team'] == 1 else 1
    enemyTeamHealth = results[b'teamHealth'][team]
    if enemyTeamHealth > 0 and results[b'damageDealt'] >= 0.25 * enemyTeamHealth:
        dossierDescr[b'steamAchievements'][b'steamMainGunMedal'] = True
    return


def __updateSteamSpotted(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamSpottedMedal']:
        return
    dossierDescr[b'steamAchievements'][b'steamSpotted'] += results[b'spotted']
    return


def __updateSteamFrags(dossierDescr, results, vehDossiers):
    if dossierDescr[b'steamAchievements'][b'steamTheBeginningMedal']:
        return
    dossierDescr[b'steamAchievements'][b'steamFrags'] += results[b'kills']
    return


def __updateSteamTopLeague(dossierDescr, results, vehDossiers):
    if results[b'winnerTeam'] != results[b'team'] or dossierDescr[b'steamAchievements'][b'steamTopLeagueMedal']:
        return
    originalXP = -1
    if results[b'misc'].get(b'max') is not None:
        originalXP = results[b'misc'][b'max'][b'xp']
    for vehTypeCompDescr, (_, _) in vehDossiers.iteritems():
        level = getLevel(vehTypeCompDescr)
        if originalXP == 1 and level == _BATTLE_HERO_CONFIG[b'steamTopLeague'][b'level'] and results[b'originalXP'] >= _BATTLE_HERO_CONFIG[b'steamTopLeague'][b'minXP']:
            dossierDescr[b'steamAchievements'][b'steamTopLeague'] += 1
        break

    return


STEAM_UPDATE = [
 __updateSteamBasePoints, 
 __updateSteamFighter, 
 __updateSteamHardCharacter, 
 __updateSteamMedium, 
 __updateSteamATSPG, 
 __updateSteamDieHard, 
 __updateSteamDestroyer, 
 __updateSteamMediumPerformance, 
 __updateSteamReconnoiter, 
 __updateSteamPotentialStun, 
 __updateSteamMileage, 
 __updateSteamHorizonSupport, 
 __updateSteamSmallSupport, 
 __updateSteamCumulativeMedalsCounters, 
 __updateSteamBreakThrough, 
 __updateSteamStop, 
 __updateSteamRandomFight, 
 __updateSteamMainGun, 
 __updateSteamSpotted, 
 __updateSteamFrags, 
 __updateSteamTopLeague]
