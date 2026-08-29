import time
from functools import partial
from dossiers2.custom.config import RECORD_CONFIGS
from dossiers2.custom.cache import getCache
from dossiers2.custom.utils import getVehicleNationID
_SECONDS_IN_DAY = 86400
MEDAL_ALIASES = {b'medalHalonen': b'medalKrysov', 
   b'medalCarius': b'medalSamokhin', 
   b'medalLehvaslaiho': b'medalKhazov', 
   b'medalTamadaYoshio': b'medalTrubin', 
   b'medalTarczay': b'medalLyubushkin', 
   b'medalKnispel': b'medalGudz', 
   b'medalWittmann': b'medalUshakov', 
   b'medalBrunoPietro': b'medalFokin', 
   b'medalPascucci': b'medalSlyunyayev'}
A15X15_STATS_DEPENDENCIES = {}

def _set_A15X15_STATS_DEPENDENCIES():
    global A15X15_STATS_DEPENDENCIES
    A15X15_STATS_DEPENDENCIES.update({b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko]})
    return


A30X30_STATS_DEPENDENCIES = {}

def _set_A30X30_STATS_DEPENDENCIES():
    global A30X30_STATS_DEPENDENCIES
    A30X30_STATS_DEPENDENCIES.update({b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko]})
    return


A7X7_STATS_DEPENDENCIES = {}

def _set_A7X7_STATS_DEPENDENCIES():
    global A7X7_STATS_DEPENDENCIES
    A7X7_STATS_DEPENDENCIES.update({b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko], 
       b'wins': [
               _updateForTacticalOperations]})
    return


ACHIEVEMENT15X15_DEPENDENCIES = {}

def _set_ACHIEVEMENT15X15_DEPENDENCIES():
    global ACHIEVEMENT15X15_DEPENDENCIES
    ACHIEVEMENT15X15_DEPENDENCIES.update({b'warrior': [
                  _updateBattleHeroes, _updateSteamForWarriorMedal], 
       b'invader': [
                  _updateBattleHeroes], 
       b'sniper': [
                 _updateBattleHeroes], 
       b'defender': [
                   _updateBattleHeroes], 
       b'steelwall': [
                    _updateBattleHeroes, _updateSteamForSteelWallMedal], 
       b'supporter': [
                    _updateBattleHeroes], 
       b'scout': [
                _updateBattleHeroes], 
       b'evileye': [
                  _updateBattleHeroes], 
       b'battleHeroes': [
                       _updateMedalKay, _updateSteamBattleHeroes], 
       b'fragsBeast': [
                     _updateBeasthunter], 
       b'fragsSinai': [
                     _updateSinai], 
       b'fragsPatton': [
                      _updatePattonValley], 
       b'sniperSeries': [
                       _updateMaxSniperSeries], 
       b'maxSniperSeries': [
                          _updateTitleSniper], 
       b'invincibleSeries': [
                           _updateMaxInvincibleSeries], 
       b'maxInvincibleSeries': [
                              _updateInvincible], 
       b'diehardSeries': [
                        _updateMaxDiehardSeries], 
       b'maxDiehardSeries': [
                           _updateDiehard], 
       b'killingSeries': [
                        _updateMaxKillingSeries], 
       b'maxKillingSeries': [
                           _updateHandOfDeath], 
       b'piercingSeries': [
                         _updateMaxPiercingSeries], 
       b'maxPiercingSeries': [
                            _updateArmorPiercer], 
       b'maxAimerSeries': [
                         _updateAimer], 
       b'sniper2': [
                  _updateBattleHeroes], 
       b'mainGun': [
                  _updateBattleHeroes], 
       b'WFC2014WinSeries': [
                           _updateMaxWFC2014WinSeries], 
       b'deathTrackWinSeries': [
                              _updateMaxDeathTrackWinSeries], 
       b'tankwomenProgress': [
                            _updateTankwomen], 
       b'EFC2016WinSeries': [
                           _updateMaxEFC2016WinSeries], 
       b'rankedBattlesHeroProgress': [
                                    _updateRankedBattlesHeroProgress], 
       b'rankedStayingCounter': [
                               _updateRankedStayingPower], 
       b'rankedDivisionCounter': [
                                _updateRankedDivisionFighter], 
       b'RP2018sergeantCounter': [
                                _updateRP2018sergeant], 
       b'bonecrusher': [
                      _updateSteamForBonecrusherMedal]})
    return


ACHIEVEMENT7X7_DEPENDENCIES = {}

def _set_ACHIEVEMENT7X7_DEPENDENCIES():
    global ACHIEVEMENT7X7_DEPENDENCIES
    ACHIEVEMENT7X7_DEPENDENCIES.update({b'wolfAmongSheep': [
                         _updateWolfAmongSheepMedal], 
       b'geniusForWar': [
                       _updateGeniusForWarMedal], 
       b'crucialShot': [
                      _updateCrucialShotMedal], 
       b'tacticalBreakthroughSeries': [
                                     _updateMaxTacticalBreakthroughSeries], 
       b'maxTacticalBreakthroughSeries': [
                                        _updateTacticalBreakthrough, _updateAwardCount], 
       b'fightingReconnaissance': [
                                 _updateFightingReconnaissanceMedal], 
       b'pyromaniac': [
                     _updatePyromaniacMedal], 
       b'ranger': [
                 _updateRangerMedal], 
       b'promisingFighter': [
                           _updatePromisingFighterMedal], 
       b'heavyFire': [
                    _updateHeavyFireMedal], 
       b'fireAndSteel': [
                       _updateFireAndSteelMedal], 
       b'guerrilla': [
                    _updateGuerrillaMedal], 
       b'bruteForce': [
                     _updateBruteForceMedal], 
       b'prematureDetonation': [
                              _updatePrematureDetonationMedal], 
       b'sentinel': [
                   _updateSentinelMedal], 
       b'infiltrator': [
                      _updateInfiltratorMedal], 
       b'wolfAmongSheepMedal': [
                              _updateAwardCount, _updateBattleHeroes], 
       b'geniusForWarMedal': [
                            _updateAwardCount, _updateBattleHeroes], 
       b'fightingReconnaissanceMedal': [
                                      _updateAwardCount], 
       b'crucialShotMedal': [
                           _updateAwardCount], 
       b'promisingFighterMedal': [
                                _updateAwardCount], 
       b'heavyFireMedal': [
                         _updateAwardCount], 
       b'rangerMedal': [
                      _updateAwardCount], 
       b'fireAndSteelMedal': [
                            _updateAwardCount], 
       b'pyromaniacMedal': [
                          _updateAwardCount], 
       b'guerrillaMedal': [
                         _updateAwardCount], 
       b'infiltratorMedal': [
                           _updateAwardCount], 
       b'sentinelMedal': [
                        _updateAwardCount], 
       b'prematureDetonationMedal': [
                                   _updateAwardCount], 
       b'bruteForceMedal': [
                          _updateAwardCount], 
       b'kingOfTheHill': [
                        _updateAwardCount], 
       b'armoredFist': [
                      _updateAwardCount], 
       b'godOfWar': [
                   _updateAwardCount], 
       b'willToWinSpirit': [
                          _updateAwardCount], 
       b'noMansLand': [
                     _updateAwardCount], 
       b'forTacticalOperations': [
                                _updateAwardCount], 
       b'awardCount': [
                     _updateBattleTested]})
    return


ACHIEVEMENTRATED7X7_DEPENDENCIES = {}

def _set_ACHIEVEMENTRATED7X7_DEPENDENCIES():
    global ACHIEVEMENTRATED7X7_DEPENDENCIES
    ACHIEVEMENTRATED7X7_DEPENDENCIES.update({b'victoryMarchSeries': [
                             _updateMaxVictoryMarchSeries, _updateVictoryMarch]})
    return


HISTORICAL_ACHIEVEMENTS_DEPENDENCIES = {}

def _set_HISTORICAL_ACHIEVEMENTS_DEPENDENCIES():
    global HISTORICAL_ACHIEVEMENTS_DEPENDENCIES
    HISTORICAL_ACHIEVEMENTS_DEPENDENCIES.update({b'bothSidesWins': [
                        _updateMakerOfHistoryMedal], 
       b'weakVehiclesWins': [
                           _updateGuardsManMedal]})
    return


HISTORICAL_STATS_DEPENDENCIES = {}

def _set_HISTORICAL_STATS_DEPENDENCIES():
    global HISTORICAL_STATS_DEPENDENCIES
    HISTORICAL_STATS_DEPENDENCIES.update({b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko]})
    return


FORT_BATTLES_STATS_DEPENDENCIES = {}

def _set_FORT_BATTLES_STATS_DEPENDENCIES():
    global FORT_BATTLES_STATS_DEPENDENCIES
    FORT_BATTLES_STATS_DEPENDENCIES.update({b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko]})
    return


FORT_SORTIES_STATS_DEPENDENCIES = {}

def _set_FORT_SORTIES_STATS_DEPENDENCIES():
    global FORT_SORTIES_STATS_DEPENDENCIES
    FORT_SORTIES_STATS_DEPENDENCIES.update({b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko], 
       b'wins': [
               _updateSoldierOfFortune]})
    return


FORT_ACHIEVEMENTS_DEPENDENCIES = {}

def _set_FORT_ACHIEVEMENTS_DEPENDENCIES():
    return


SINGLE_ACHIEVEMENTS_DEPENDENCIES = {}

def _set_SINGLE_ACHIEVEMENTS_DEPENDENCIES():
    global SINGLE_ACHIEVEMENTS_DEPENDENCIES
    SINGLE_ACHIEVEMENTS_DEPENDENCIES.update({b'onboardingMedal': [
                          _updateSteamOnboarding]})
    return


STEAM_ACHIEVEMENT_DEPENDENCIES = {}

def _set_STEAM_ACHIEVEMENT_DEPENDENCIES():
    global STEAM_ACHIEVEMENT_DEPENDENCIES
    STEAM_ACHIEVEMENT_DEPENDENCIES.update({b'steamBattleCredits': [
                             _updateSteamBattleCredits], 
       b'steamBattleXP': [
                        _updateSteamBattleXP], 
       b'steamFreeXP': [
                      _updateSteamFreeXP], 
       b'steamMasteryMarks': [
                            _updateSteamMasteryMarksMedals], 
       b'steamBasePoints': [
                          _updateSteamBasePoints], 
       b'steamHardCharacter': [
                             _updateSteamHardCharacterMedal], 
       b'steamMedium': [
                      _updatesteamMediumMedal], 
       b'steamATSPG': [
                     _updateSteamATSPGMedal], 
       b'steamBreakThrough': [
                            _updateSteamBreakThroughMedal], 
       b'steamStop': [
                    _updateSteamStopMedal], 
       b'steamReconnoiter': [
                           _updateSteamReconnoiterMedal], 
       b'steamPotentialStun': [
                             _updateSteamPotentialStunMedal], 
       b'steamMileage': [
                       _updateSteamMileageMedal], 
       b'steamTopLeague': [
                         _updateSteamTopLeagueMedal], 
       b'steamSpotted': [
                       _updateSteamSpottedMedal], 
       b'steamFrags': [
                     _updateSteamFragsMedals], 
       b'steamBattleHeroes': [
                            _updateSteamOrderMedal]})
    return


VEH_TYPE_FRAGS_DEPENDENCIES = {}

def _set_VEH_TYPE_FRAGS_DEPENDENCIES():
    global VEH_TYPE_FRAGS_DEPENDENCIES
    cache = getCache()
    VEH_TYPE_FRAGS_DEPENDENCIES.update({(cache[b'mausTypeCompDescr']): [
                                     _updateMousebane], 
       b'_insert_': [
                   _updateTankExpert, _updateSaboteur]})
    return


CLAN_STATS_DEPENDENCIES = {}

def _set_CLAN_STATS_DEPENDENCIES():
    global CLAN_STATS_DEPENDENCIES
    CLAN_STATS_DEPENDENCIES.update({b'battlesCount': [
                       _updateMedalRotmistrov]})
    return


CLUB_BATTLES_STAT_DEPENDENCIES = {}

def _set_CLUB_BATTLES_STAT_DEPENDENCIES():
    global CLUB_BATTLES_STAT_DEPENDENCIES
    CLUB_BATTLES_STAT_DEPENDENCIES.update({b'wins': [
               _updateStrategicOperations]})
    return


CLUB_ACHIEVEMENTS_DEPENDENCIES = {}

def _set_CLUB_ACHIEVEMENTS_DEPENDENCIES():
    global CLUB_ACHIEVEMENTS_DEPENDENCIES
    CLUB_ACHIEVEMENTS_DEPENDENCIES.update({b'victoryMarchSeries': [
                             _updateMaxVictoryMarchSeries, _updateClubVictoryMarch]})
    return


GLOBAL_MAP_STATS_DEPENDENCIES = {}

def _set_GLOBAL_MAP_STATS_DEPENDENCIES():
    global GLOBAL_MAP_STATS_DEPENDENCIES
    GLOBAL_MAP_STATS_DEPENDENCIES.update({b'battlesCount': [
                       _updateMedalRotmistrov], 
       b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko]})
    return


FALLOUT_STATS_DEPENDENCIES = {}

def _set_FALLOUT_STATS_DEPENDENCIES():
    global FALLOUT_STATS_DEPENDENCIES
    FALLOUT_STATS_DEPENDENCIES.update({b'avatarKills': [
                      _updateStormLord], 
       b'winPoints': [
                    _updateWinnerLaurels]})
    return


def _updateRankedBadge(dossierDescr, dossierBlockDescr, key, value, prevValue):
    eventsEnabled = dossierBlockDescr.eventsEnabled
    if eventsEnabled:
        dossierBlockDescr.eventsEnabled = False
    dossierBlockDescr[key] = int(time.time()) / _SECONDS_IN_DAY if value == 1 else 0
    if eventsEnabled:
        dossierBlockDescr.eventsEnabled = True
    return


RANKED_STATS_DEPENDENCIES = {}

def _set_RANKED_STATS_DEPENDENCIES():
    global RANKED_STATS_DEPENDENCIES
    RANKED_STATS_DEPENDENCIES.update({b'winAndSurvived': [
                         _updateMedalAbrams], 
       b'frags': [
                _updateMedalSamokhin], 
       b'frags8p': [
                  _updateMedalEkins], 
       b'damageDealt': [
                      _updateMedalGudz], 
       b'damageReceived': [
                         _updateMedalGudz], 
       b'spotted': [
                  _updateMedalPoppel], 
       b'capturePoints': [
                        _updateMedalLeClerc], 
       b'droppedCapturePoints': [
                               _updateMedalLavrinenko]})
    return


EPIC_BATTLE_STATS_DEPENDENCIES = {}

def _set_EPIC_BATTLE_STATS_DEPENDENCIES():
    return


def _updateMedalSamokhin(dossierDescr, dossierBlockDescr, key, value, prevValue):
    frags = 0
    for block in (b'a15x15', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'globalMapCommon', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute', b'a30x30'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                frags += dossierDescr[block][b'frags']

    medalSamokhinCfg = RECORD_CONFIGS[b'medalSamokhin']
    maxMedalClass = len(medalSamokhinCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if frags >= medalSamokhinCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierDescr[b'achievements'][b'medalSamokhin']
    if curClass == 0 or curClass > medalClass:
        dossierDescr[b'achievements'][b'medalSamokhin'] = medalClass
    return


def _updateMedalGudz(dossierDescr, dossierBlockDescr, key, value, prevValue):
    damage = 0
    for block in (b'a15x15', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'globalMapCommon', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute', b'a30x30'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                damage += dossierDescr[block][b'damageDealt']
                damage += dossierDescr[block][b'damageReceived']

    medalGudzCfg = RECORD_CONFIGS[b'medalGudz']
    maxMedalClass = len(medalGudzCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if damage >= medalGudzCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierDescr[b'achievements'][b'medalGudz']
    if curClass == 0 or curClass > medalClass:
        dossierDescr[b'achievements'][b'medalGudz'] = medalClass
    return


def _updateMedalPoppel(dossierDescr, dossierBlockDescr, key, value, prevValue):
    spotted = 0
    for block in (b'a15x15', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'globalMapCommon', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute', b'a30x30'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                spotted += dossierDescr[block][b'spotted']

    medalPoppelCfg = RECORD_CONFIGS[b'medalPoppel']
    maxMedalClass = len(medalPoppelCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if spotted >= medalPoppelCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierDescr[b'achievements'][b'medalPoppel']
    if curClass == 0 or curClass > medalClass:
        dossierDescr[b'achievements'][b'medalPoppel'] = medalClass
    return


def _updateMedalLeClerc(dossierDescr, dossierBlockDescr, key, value, prevValue):
    capturePoints = 0
    for block in (b'a15x15', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'globalMapCommon', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute', b'a30x30'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                capturePoints += dossierDescr[block][b'capturePoints']

    medalLeClercCfg = RECORD_CONFIGS[b'medalLeClerc']
    maxMedalClass = len(medalLeClercCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if capturePoints >= medalLeClercCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierDescr[b'achievements'][b'medalLeClerc']
    if curClass == 0 or curClass > medalClass:
        dossierDescr[b'achievements'][b'medalLeClerc'] = medalClass
    return


def _updateMedalLavrinenko(dossierDescr, dossierBlockDescr, key, value, prevValue):
    droppedCapturePoints = 0
    for block in (b'a15x15', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'globalMapCommon', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute', b'a30x30'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                droppedCapturePoints += dossierDescr[block][b'droppedCapturePoints']

    medalLavrinenkoCfg = RECORD_CONFIGS[b'medalLavrinenko']
    maxMedalClass = len(medalLavrinenkoCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if droppedCapturePoints >= medalLavrinenkoCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierDescr[b'achievements'][b'medalLavrinenko']
    if curClass == 0 or curClass > medalClass:
        dossierDescr[b'achievements'][b'medalLavrinenko'] = medalClass
    return


def _updateBattleHeroes(dossierDescr, dossierBlockDescr, key, value, prevValue):
    dossierDescr[b'achievements'][b'battleHeroes'] += value - prevValue
    return


def _updateSteamBattleHeroes(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if dossierDescr.isBlockInLayout(b'steamAchievements') and not dossierDescr[b'steamAchievements'][b'steamOrderMedal']:
        dossierDescr[b'steamAchievements'][b'steamBattleHeroes'] += value - prevValue
    return


def _updateTankwomen(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'tankwomen']:
        dossierDescr[b'singleAchievements'][b'tankwomen'] = 1
        dossierDescr.addPopUp(b'singleAchievements', b'tankwomen', 1)
    return


def _updateMedalKay(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalKayCfg = RECORD_CONFIGS[b'medalKay']
    maxMedalClass = len(medalKayCfg)
    battleHeroes = dossierBlockDescr[b'battleHeroes']
    for medalClass in xrange(1, maxMedalClass + 1):
        if battleHeroes >= medalKayCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierBlockDescr[b'medalKay']
    if curClass == 0 or curClass > medalClass:
        dossierBlockDescr[b'medalKay'] = medalClass
    return


def _updateMedalAbrams(dossierDescr, dossierBlockDescr, key, value, prevValue):
    winAndSurvived = 0
    for block in (b'a15x15', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'globalMapCommon', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute', b'a30x30'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                winAndSurvived += dossierDescr[block][b'winAndSurvived']

    medalAbramsCfg = RECORD_CONFIGS[b'medalAbrams']
    maxMedalClass = len(medalAbramsCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if winAndSurvived >= medalAbramsCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierDescr[b'achievements'][b'medalAbrams']
    if curClass == 0 or curClass > medalClass:
        dossierDescr[b'achievements'][b'medalAbrams'] = medalClass
    return


def _updateMedalEkins(dossierDescr, dossierBlockDescr, key, value, prevValue):
    frags8p = 0
    for block in (b'a15x15', b'a7x7', b'historical', b'fortBattles', b'fortSorties', b'globalMapCommon', b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute', b'a30x30'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                frags8p += dossierDescr[block][b'frags8p']

    medalEkinsCfg = RECORD_CONFIGS[b'medalEkins']
    maxMedalClass = len(medalEkinsCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if frags8p >= medalEkinsCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierDescr[b'achievements'][b'medalEkins']
    if curClass == 0 or curClass > medalClass:
        dossierDescr[b'achievements'][b'medalEkins'] = medalClass
    return


def _updateBeasthunter(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medals, series = divmod(value, RECORD_CONFIGS[b'beasthunter'])
    if dossierBlockDescr[b'beasthunter'] != medals:
        dossierBlockDescr[b'beasthunter'] = medals
    return


def _updateSinai(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medals, series = divmod(value, RECORD_CONFIGS[b'sinai'])
    if dossierBlockDescr[b'sinai'] != medals:
        dossierBlockDescr[b'sinai'] = medals
    return


def _updatePattonValley(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medals, series = divmod(value, RECORD_CONFIGS[b'pattonValley'])
    if dossierBlockDescr[b'pattonValley'] != medals:
        dossierBlockDescr[b'pattonValley'] = medals
    return


def _updateMaxSniperSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxSniperSeries']:
        dossierBlockDescr[b'maxSniperSeries'] = value
    return


def _updateTitleSniper(dossierDescr, dossierBlockDescr, key, value, prevValue, block=b'singleAchievements'):
    if value >= RECORD_CONFIGS[b'titleSniper']:
        dossierDescr[block][b'titleSniper'] = 1
        dossierDescr.addPopUp(block, b'titleSniper', 1)
    return


def _updateMaxInvincibleSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxInvincibleSeries']:
        dossierBlockDescr[b'maxInvincibleSeries'] = value
    return


def _updateInvincible(dossierDescr, dossierBlockDescr, key, value, prevValue, block=b'singleAchievements'):
    if value >= RECORD_CONFIGS[b'invincible']:
        dossierDescr[block][b'invincible'] = 1
        dossierDescr.addPopUp(block, b'invincible', 1)
    return


def _updateMaxDiehardSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxDiehardSeries']:
        dossierBlockDescr[b'maxDiehardSeries'] = value
    return


def _updateDiehard(dossierDescr, dossierBlockDescr, key, value, prevValue, block=b'singleAchievements'):
    if value >= RECORD_CONFIGS[b'diehard']:
        dossierDescr[block][b'diehard'] = 1
        dossierDescr.addPopUp(block, b'diehard', 1)
    return


def _updateMaxKillingSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxKillingSeries']:
        dossierBlockDescr[b'maxKillingSeries'] = value
    return


def _updateHandOfDeath(dossierDescr, dossierBlockDescr, key, value, prevValue, block=b'singleAchievements'):
    if value >= RECORD_CONFIGS[b'handOfDeath']:
        dossierDescr[block][b'handOfDeath'] = 1
        dossierDescr.addPopUp(block, b'handOfDeath', 1)
    return


def _updateMaxPiercingSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxPiercingSeries']:
        dossierBlockDescr[b'maxPiercingSeries'] = value
    return


def _updateArmorPiercer(dossierDescr, dossierBlockDescr, key, value, prevValue, block=b'singleAchievements'):
    if value >= RECORD_CONFIGS[b'armorPiercer']:
        dossierDescr[block][b'armorPiercer'] = 1
        dossierDescr.addPopUp(block, b'armorPiercer', 1)
    return


def _updateAimer(dossierDescr, dossierBlockDescr, key, value, prevValue, block=b'singleAchievements'):
    dossierDescr[block][b'aimer'] = 1
    return


def _updateMaxWFC2014WinSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxWFC2014WinSeries']:
        dossierBlockDescr[b'maxWFC2014WinSeries'] = value
    if value >= 1:
        dossierDescr[b'singleAchievements'][b'WFC2014'] = 1
        dossierDescr.addPopUp(b'singleAchievements', b'WFC2014', 1)
    return


def _updateMaxEFC2016WinSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxEFC2016WinSeries']:
        dossierBlockDescr[b'maxEFC2016WinSeries'] = value
    return


def _updateRankedBattlesHeroProgress(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= 1:
        dossierDescr[b'singleAchievements'][b'rankedBattlesHero'] = 1
        dossierDescr.addPopUp(b'singleAchievements', b'rankedBattlesHero', 1)
    elif value == 0:
        dossierDescr[b'singleAchievements'][b'rankedBattlesHero'] = 0
    return


def _updateRankedDivisionFighter(dossierDescr, dossierBlockDescr, key, value, prevValue):
    achievmentName = b'rankedDivisionFighter'
    prevClass = __getNewMedalClass(achievmentName, prevValue, 0)
    curClass = __getNewMedalClass(achievmentName, value, 0)
    if prevClass != curClass:
        dossierBlockDescr[achievmentName] = curClass
        dossierDescr.addPopUp(b'achievements', achievmentName, curClass)
    return


def _updateRankedStayingPower(dossierDescr, dossierBlockDescr, key, value, prevValue):
    achievmentName = b'rankedStayingPower'
    prevClass = __getNewMedalClass(achievmentName, prevValue, 0)
    curClass = __getNewMedalClass(achievmentName, value, 0)
    if prevClass != curClass:
        dossierBlockDescr[achievmentName] = curClass
        dossierDescr.addPopUp(b'achievements', achievmentName, curClass)
    return


def _updateMaxDeathTrackWinSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxDeathTrackWinSeries']:
        dossierBlockDescr[b'maxDeathTrackWinSeries'] = value
    if value >= 1:
        dossierDescr[b'singleAchievements'][b'deathTrack'] = 1
        dossierDescr.addPopUp(b'singleAchievements', b'deathTrack', 1)
    return


def _updateMousebane(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medals, series = divmod(value, RECORD_CONFIGS[b'mousebane'])
    if dossierDescr[b'achievements'][b'mousebane'] != medals:
        dossierDescr[b'achievements'][b'mousebane'] = medals
    return


def _updateTankExpert(dossierDescr, dossierBlockDescr, key, value):
    cache = getCache()
    killedVehTypes = set(dossierBlockDescr.iterkeys())
    vehiclesInTrees = cache[b'vehiclesInTrees']
    if key not in vehiclesInTrees:
        return
    if not bool(vehiclesInTrees - killedVehTypes):
        dossierDescr[b'achievements'][b'tankExpert'] = True
        dossierDescr.addPopUp(b'achievements', b'tankExpert', True)
    nationID = getVehicleNationID(key)
    if not bool(cache[b'vehiclesInTreesByNation'][nationID] - killedVehTypes):
        record = (b'').join([b'tankExpert', str(nationID)])
        dossierDescr[b'achievements'][record] = True
        dossierDescr.addPopUp(b'achievements', record, True)
    return


def _updateWolfAmongSheepMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'wolfAmongSheepMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'wolfAmongSheepMedal'] += medals
        dossierBlockDescr[b'wolfAmongSheep'] = amountLeft
    return


def _updateGeniusForWarMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'geniusForWarMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'geniusForWarMedal'] += medals
        dossierBlockDescr[b'geniusForWar'] = amountLeft
    return


def _updateCrucialShotMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'crucialShotMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'crucialShotMedal'] += medals
        dossierBlockDescr[b'crucialShot'] = amountLeft
    return


def _updateMaxTacticalBreakthroughSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxTacticalBreakthroughSeries']:
        dossierBlockDescr[b'maxTacticalBreakthroughSeries'] = value
    return


def _updateTacticalBreakthrough(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'tacticalBreakthrough']:
        dossierDescr[b'singleAchievements'][b'tacticalBreakthrough'] = 1
        dossierDescr.addPopUp(b'singleAchievements', b'tacticalBreakthrough', 1)
    return


def _updateFightingReconnaissanceMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'fightingReconnaissanceMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'fightingReconnaissanceMedal'] += medals
        dossierBlockDescr[b'fightingReconnaissance'] = amountLeft
    return


def _updatePyromaniacMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'pyromaniacMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'pyromaniacMedal'] += medals
        dossierBlockDescr[b'pyromaniac'] = amountLeft
    return


def _updateRangerMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'rangerMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'rangerMedal'] += medals
        dossierBlockDescr[b'ranger'] = amountLeft
    return


def _updatePromisingFighterMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'promisingFighterMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'promisingFighterMedal'] += medals
        dossierBlockDescr[b'promisingFighter'] = amountLeft
    return


def _updateHeavyFireMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'heavyFireMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'heavyFireMedal'] += medals
        dossierBlockDescr[b'heavyFire'] = amountLeft
    return


def _updateFireAndSteelMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'fireAndSteelMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'fireAndSteelMedal'] += medals
        dossierBlockDescr[b'fireAndSteel'] = amountLeft
    return


def _updateGuerrillaMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'guerrillaMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'guerrillaMedal'] += medals
        dossierBlockDescr[b'guerrilla'] = amountLeft
    return


def _updateBruteForceMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'bruteForceMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'bruteForceMedal'] += medals
        dossierBlockDescr[b'bruteForce'] = amountLeft
    return


def _updatePrematureDetonationMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'prematureDetonationMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'prematureDetonationMedal'] += medals
        dossierBlockDescr[b'prematureDetonation'] = amountLeft
    return


def _updateSentinelMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'sentinelMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'sentinelMedal'] += medals
        dossierBlockDescr[b'sentinel'] = amountLeft
    return


def _updateSteamBattleCredits(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamLittleSavingsMedal'] and not dossierBlockDescr[b'steamLittleSavingsMedal']:
        dossierBlockDescr[b'steamLittleSavingsMedal'] = True
    if value >= RECORD_CONFIGS[b'steamMintedCoinMedal'] and not dossierBlockDescr[b'steamMintedCoinMedal']:
        dossierBlockDescr[b'steamMintedCoinMedal'] = True
    if value >= RECORD_CONFIGS[b'steamKingMidasMedal']:
        dossierBlockDescr[b'steamKingMidasMedal'] = True
    return


def _updateSteamBattleXP(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamGoodStudentMedal'] and not dossierBlockDescr[b'steamGoodStudentMedal']:
        dossierBlockDescr[b'steamGoodStudentMedal'] = True
    if value >= RECORD_CONFIGS[b'steamBattleHardenedMedal'] and not dossierBlockDescr[b'steamBattleHardenedMedal']:
        dossierBlockDescr[b'steamBattleHardenedMedal'] = True
    if value >= RECORD_CONFIGS[b'steamExperienceMedal']:
        dossierBlockDescr[b'steamExperienceMedal'] = True
    return


def _updateSteamFreeXP(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamHandyMedal'] and not dossierBlockDescr[b'steamHandyMedal']:
        dossierBlockDescr[b'steamHandyMedal'] = True
    if value >= RECORD_CONFIGS[b'steamUniversalResourceMedal'] and not dossierBlockDescr[b'steamUniversalResourceMedal']:
        dossierBlockDescr[b'steamUniversalResourceMedal'] = True
    if value >= RECORD_CONFIGS[b'steamPowerKnowledgeMedal']:
        dossierBlockDescr[b'steamPowerKnowledgeMedal'] = True
    return


def _updateSteamFragsMedals(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamSuchWorkMedal'] and not dossierBlockDescr[b'steamSuchWorkMedal']:
        dossierBlockDescr[b'steamSuchWorkMedal'] = True
    if value >= RECORD_CONFIGS[b'steamNothingPersonalMedal'] and not dossierBlockDescr[b'steamNothingPersonalMedal']:
        dossierBlockDescr[b'steamNothingPersonalMedal'] = True
    if value >= RECORD_CONFIGS[b'steamTheBeginningMedal']:
        dossierBlockDescr[b'steamTheBeginningMedal'] = True
    return


def _updateSteamMasteryMarksMedals(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamGetMaxMedal'] and not dossierBlockDescr[b'steamGetMaxMedal']:
        dossierBlockDescr[b'steamGetMaxMedal'] = True
    if value >= RECORD_CONFIGS[b'steamThreeCheersMedal'] and not dossierBlockDescr[b'steamThreeCheersMedal']:
        dossierBlockDescr[b'steamThreeCheersMedal'] = True
    if value >= RECORD_CONFIGS[b'steamGoldenFiveMedal']:
        dossierBlockDescr[b'steamGoldenFiveMedal'] = True
    return


def _updateSteamForWarriorMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if dossierDescr.isBlockInLayout(b'steamAchievements') and not dossierDescr[b'steamAchievements'][b'steamForWarriorMedal']:
        dossierDescr[b'steamAchievements'][b'steamForWarriorMedal'] = True
    return


def _updateSteamForSteelWallMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if dossierDescr.isBlockInLayout(b'steamAchievements') and not dossierDescr[b'steamAchievements'][b'steamForSteelWallMedal']:
        dossierDescr[b'steamAchievements'][b'steamForSteelWallMedal'] = True
    return


def _updateSteamForBonecrusherMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if dossierDescr.isBlockInLayout(b'steamAchievements') and not dossierDescr[b'steamAchievements'][b'steamForBonecrusherMedal']:
        dossierDescr[b'steamAchievements'][b'steamForBonecrusherMedal'] = True
    return


def _updateSteamOrderMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamOrderMedal']:
        dossierDescr[b'steamAchievements'][b'steamOrderMedal'] = True
    return


def _updateSteamSpottedMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamSpottedMedal']:
        dossierBlockDescr[b'steamSpottedMedal'] = True
    return


def _updateSteamBasePoints(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamBasePointsMedal']:
        dossierBlockDescr[b'steamBasePointsMedal'] = True
    return


def _updateSteamHardCharacterMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamHardCharacterMedal']:
        dossierBlockDescr[b'steamHardCharacterMedal'] = True
    return


def _updatesteamMediumMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamMediumMedal']:
        dossierBlockDescr[b'steamMediumMedal'] = True
    return


def _updateSteamATSPGMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamATSPGMedal']:
        dossierBlockDescr[b'steamATSPGMedal'] = True
    return


def _updateSteamBreakThroughMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamBreakThroughMedal']:
        dossierBlockDescr[b'steamBreakThroughMedal'] = True
    return


def _updateSteamStopMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamStopMedal']:
        dossierBlockDescr[b'steamStopMedal'] = True
    return


def _updateSteamReconnoiterMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamReconnoiterMedal']:
        dossierBlockDescr[b'steamReconnoiterMedal'] = True
    return


def _updateSteamPotentialStunMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamPotentialStunMedal']:
        dossierBlockDescr[b'steamPotentialStunMedal'] = True
    return


def _updateSteamMileageMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamMileageMedal']:
        dossierBlockDescr[b'steamMileageMedal'] = True
    return


def _updateSteamOnboarding(dossierDescr, dossierBlockDescr, value, added):
    if dossierDescr.isBlockInLayout(b'steamAchievements') and added:
        dossierDescr[b'steamAchievements'][b'steamBootcampMedal'] = True
    return


def _updateSteamTopLeagueMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'steamTopLeagueMedal']:
        dossierBlockDescr[b'steamTopLeagueMedal'] = True
    return


def _updateInfiltratorMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    amountRequired = RECORD_CONFIGS[b'infiltratorMedal']
    if value >= amountRequired:
        medals, amountLeft = divmod(value, amountRequired)
        dossierBlockDescr[b'infiltratorMedal'] += medals
        dossierBlockDescr[b'infiltrator'] = amountLeft
    return


def _updateAwardCount(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if key == b'maxTacticalBreakthroughSeries':
        amountRequired = RECORD_CONFIGS[b'tacticalBreakthrough']
        if prevValue < amountRequired <= value:
            dossierBlockDescr[b'awardCount'] += 1
    elif key == b'forTacticalOperations' and value - prevValue != 0:
        dossierBlockDescr[b'awardCount'] += 1
    else:
        dossierBlockDescr[b'awardCount'] += value - prevValue
    return


def _updateBattleTested(dossierDescr, dossierBlockDescr, key, value, prevValue):
    awardCountCnfg = RECORD_CONFIGS[b'battleTested']
    maxMedalClass = len(awardCountCnfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if value >= awardCountCnfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierBlockDescr[b'battleTested']
    if curClass == 0 or curClass > medalClass:
        dossierBlockDescr[b'battleTested'] = medalClass
    return


def _updateMakerOfHistoryMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    minWinsCnfg = RECORD_CONFIGS[b'makerOfHistory']
    maxMedalClass = len(minWinsCnfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if value >= minWinsCnfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierBlockDescr[b'makerOfHistory']
    if curClass == 0 or curClass > medalClass:
        dossierBlockDescr[b'makerOfHistory'] = medalClass
    return


def _updateGuardsManMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    minWinsCnfg = RECORD_CONFIGS[b'guardsman']
    maxMedalClass = len(minWinsCnfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if value >= minWinsCnfg[maxMedalClass - medalClass]:
            break
    else:
        return

    curClass = dossierBlockDescr[b'guardsman']
    if curClass == 0 or curClass > medalClass:
        dossierBlockDescr[b'guardsman'] = medalClass
    return


def _updateForTacticalOperations(dossierDescr, dossierBlockDescr, key, value, prevValue):
    wins7x7 = dossierBlockDescr[b'wins']
    medalCfg = RECORD_CONFIGS[b'forTacticalOperations']
    maxMedalClass = len(medalCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if wins7x7 >= medalCfg[maxMedalClass - medalClass]:
            break
    else:
        return

    achievements7x7 = dossierDescr[b'achievements7x7']
    curClass = achievements7x7[b'forTacticalOperations']
    if curClass == 0 or curClass > medalClass:
        achievements7x7[b'forTacticalOperations'] = medalClass
    return


def _updateConquerorMedal(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'conqueror'
    medalClass = dossierDescr[b'fortAchievements'][medalName]
    newMedalClass = __getNewMedalClass(medalName, value, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'fortAchievements'][medalName] = newMedalClass
    return


def _updateSoldierOfFortune(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'soldierOfFortune'
    medalClass = dossierDescr[b'fortAchievements'][medalName]
    wins = dossierBlockDescr[b'wins']
    newMedalClass = __getNewMedalClass(medalName, wins, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'fortAchievements'][medalName] = newMedalClass
    return


def _updateMedalRotmistrov(dossierDescr, dossierBlockDescr, key, value, prevValue):
    cfg = RECORD_CONFIGS[b'medalRotmistrov']
    battlesCount = 0
    for block in (b'globalMapMiddle', b'globalMapChampion', b'globalMapAbsolute'):
        if dossierDescr.isBlockInLayout(block):
            if block in dossierDescr:
                battlesCount += dossierDescr[block][key]

    i = 0
    for cfgBattlesCount in cfg:
        if battlesCount < cfgBattlesCount:
            break
        i += 1

    if i > 0:
        medalClass = len(cfg) - i + 1
        dossierDescr[b'clanAchievements'][b'medalRotmistrov'] = medalClass
    return


def _updateKampfer(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'kampfer'
    medalClass = dossierDescr[b'fortAchievements'][medalName]
    newMedalClass = __getNewMedalClass(medalName, value, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'fortAchievements'][medalName] = newMedalClass
    return


def _updateFireAndSword(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'fireAndSword'
    medalClass = dossierDescr[b'fortAchievements'][medalName]
    newMedalClass = __getNewMedalClass(medalName, value, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'fortAchievements'][medalName] = newMedalClass
    return


def _updateCrusher(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'crusher'
    medalValue = dossierDescr[b'fortAchievements'][medalName]
    cfg = RECORD_CONFIGS[medalName]
    newValue = value // cfg
    if newValue > medalValue:
        dossierDescr[b'fortAchievements'][medalName] = newValue
    return


def _updateCounterblow(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'counterblow'
    medalValue = dossierDescr[b'fortAchievements'][medalName]
    cfg = RECORD_CONFIGS[medalName]
    newValue = value // cfg
    if newValue > medalValue:
        dossierDescr[b'fortAchievements'][medalName] = newValue
    return


def _updateStrategicOperations(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'strategicOperations'
    medalClass = dossierDescr[b'achievementsRated7x7'][medalName]
    newMedalClass = __getNewMedalClass(medalName, value, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'achievementsRated7x7'][medalName] = newMedalClass
    return


def _updateMaxVictoryMarchSeries(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value > dossierBlockDescr[b'maxVictoryMarchSeries']:
        dossierBlockDescr[b'maxVictoryMarchSeries'] = value
    return


def _updateVictoryMarch(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'victoryMarch']:
        dossierDescr[b'singleAchievements'][b'victoryMarch'] = 1
        dossierDescr.addPopUp(b'singleAchievements', b'victoryMarch', 1)
    return


def _updateClubVictoryMarch(dossierDescr, dossierBlockDescr, key, value, prevValue):
    if value >= RECORD_CONFIGS[b'victoryMarch']:
        dossierDescr[b'singleAchievementsRated7x7'][b'victoryMarch'] = 1
        dossierDescr.addPopUp(b'singleAchievementsRated7x7', b'victoryMarch', 1)
    return


def _updateStormLord(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'stormLord'
    medalClass = dossierDescr[b'falloutAchievements'][medalName]
    newMedalClass = __getNewMedalClass(medalName, value, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'falloutAchievements'][medalName] = newMedalClass
    return


def _updateWinnerLaurels(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'winnerLaurels'
    medalClass = dossierDescr[b'falloutAchievements'][medalName]
    newMedalClass = __getNewMedalClass(medalName, value, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'falloutAchievements'][medalName] = newMedalClass
    return


def _updateRP2018sergeant(dossierDescr, dossierBlockDescr, key, value, prevValue):
    medalName = b'RP2018sergeant'
    medalClass = dossierDescr[b'achievements'][medalName]
    newMedalClass = __getNewMedalClass(medalName, value, medalClass)
    if newMedalClass is not None:
        dossierDescr[b'achievements'][medalName] = newMedalClass
    return


def _updateSaboteur(dossierDescr, dossierBlockDescr, key, value):
    cache = getCache()
    allSupplies = cache[b'vehiclesByTag'].get(b'supply', set())
    if key not in allSupplies:
        return
    killedVehTypes = set(dossierBlockDescr.iterkeys())
    diff = allSupplies - killedVehTypes
    dossierDescr[b'epicBattleAchievements'][b'saboteurProgress'] = len(allSupplies) - len(diff)
    if not bool(diff):
        dossierDescr[b'epicBattleAchievements'][b'saboteur'] = True
        dossierDescr.addPopUp(b'epicBattleAchievements', b'saboteur', True)
    return


def __getNewMedalClass(medalConfigName, valueToCheck, curMedalClass):
    medalCfg = RECORD_CONFIGS[medalConfigName]
    maxMedalClass = len(medalCfg)
    for medalClass in xrange(1, maxMedalClass + 1):
        if valueToCheck >= medalCfg[maxMedalClass - medalClass]:
            if curMedalClass == 0 or curMedalClass > medalClass:
                return medalClass
            break

    return


def init():
    _set_A15X15_STATS_DEPENDENCIES()
    _set_A7X7_STATS_DEPENDENCIES()
    _set_ACHIEVEMENT15X15_DEPENDENCIES()
    _set_ACHIEVEMENT7X7_DEPENDENCIES()
    _set_ACHIEVEMENTRATED7X7_DEPENDENCIES()
    _set_VEH_TYPE_FRAGS_DEPENDENCIES()
    _set_HISTORICAL_STATS_DEPENDENCIES()
    _set_HISTORICAL_ACHIEVEMENTS_DEPENDENCIES()
    _set_SINGLE_ACHIEVEMENTS_DEPENDENCIES()
    _set_FORT_BATTLES_STATS_DEPENDENCIES()
    _set_FORT_SORTIES_STATS_DEPENDENCIES()
    _set_FORT_ACHIEVEMENTS_DEPENDENCIES()
    _set_CLAN_STATS_DEPENDENCIES()
    _set_CLUB_BATTLES_STAT_DEPENDENCIES()
    _set_CLUB_ACHIEVEMENTS_DEPENDENCIES()
    _set_GLOBAL_MAP_STATS_DEPENDENCIES()
    _set_FALLOUT_STATS_DEPENDENCIES()
    _set_RANKED_STATS_DEPENDENCIES()
    _set_EPIC_BATTLE_STATS_DEPENDENCIES()
    _set_STEAM_ACHIEVEMENT_DEPENDENCIES()
    return
