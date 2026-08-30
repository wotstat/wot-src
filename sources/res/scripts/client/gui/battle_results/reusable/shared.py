import functools, operator
from account_shared import getFairPlayViolationName
from constants import DEATH_REASON_ALIVE
from debug_utils import LOG_CURRENT_EXCEPTION
from dossiers2.custom.records import DB_ID_TO_RECORD
from dossiers2.ui import achievements, layouts
from gui.battle_results.reusable import sort_keys
from gui.shared.crits_mask_parser import CRIT_MASK_SUB_TYPES, critsParserGenerator
from gui.shared.gui_items import Vehicle
from gui.shared.gui_items.dossier import getAchievementFactory
from items import vehicles as vehicles_core
from shared_utils import findFirst

def makeAchievementFromPersonal(results):
    popUps = results.get(b'dossierPopUps', [])
    for achievementID, value in popUps:
        record = DB_ID_TO_RECORD[achievementID]
        if record in layouts.IGNORED_BY_BATTLE_RESULTS or not layouts.isAchievementRegistered(record):
            continue
        factory = getAchievementFactory(record)
        if factory is not None:
            achievement = factory.create(value=value)
            if record == achievements.MARK_ON_GUN_RECORD:
                if b'typeCompDescr' in results:
                    try:
                        nationID = vehicles_core.parseIntCompactDescr(results[b'typeCompDescr'])[1]
                        achievement.setVehicleNationID(nationID)
                    except Exception:
                        LOG_CURRENT_EXCEPTION()

                if b'damageRating' in results:
                    achievement.setDamageRating(results[b'damageRating'])
            if achievement.getName() in achievements.BATTLE_ACHIEVES_RIGHT:
                yield (
                 1, achievement)
            else:
                yield (
                 -1, achievement)

    return


def makeMarkOfMasteryFromPersonal(results):
    markOfMastery = results.get(b'markOfMastery', 0)
    achievement = None
    if not markOfMastery:
        return
    else:
        factory = getAchievementFactory((b'achievements', b'markOfMastery'))
        if factory is not None:
            achievement = factory.create(value=markOfMastery)
            achievement.setPrevMarkOfMastery(results.get(b'prevMarkOfMastery', 0))
            achievement.setCompDescr(results.get(b'typeCompDescr'))
        return achievement


def makeCritsInfo(value):
    rv = {(CRIT_MASK_SUB_TYPES.DESTROYED_DEVICES): [], (CRIT_MASK_SUB_TYPES.CRITICAL_DEVICES): [], (CRIT_MASK_SUB_TYPES.DESTROYED_TANKMENS): []}
    critsCount = 0
    for subType, critType in critsParserGenerator(value):
        critsCount += 1
        rv[subType].append(critType)

    rv[b'critsCount'] = critsCount
    return rv


def unionCritsInfo(destination, source):
    rv = {(CRIT_MASK_SUB_TYPES.DESTROYED_DEVICES): [], (CRIT_MASK_SUB_TYPES.CRITICAL_DEVICES): [], (CRIT_MASK_SUB_TYPES.DESTROYED_TANKMENS): []}
    for subType in rv.iterkeys():
        if subType not in source:
            continue
        values = source[subType]
        if subType in destination:
            toUpdate = destination[subType]
        else:
            toUpdate = destination[subType] = []
        for value in values:
            if value not in toUpdate:
                toUpdate.append(value)

    if b'critsCount' in source:
        if b'critsCount' in destination:
            destination[b'critsCount'] += source[b'critsCount']
        else:
            destination[b'critsCount'] = source[b'critsCount']
    return


class ItemInfo(object):
    __slots__ = (b'__wasInBattle',)

    def __init__(self, wasInBattle=True):
        super(ItemInfo, self).__init__()
        self.__wasInBattle = wasInBattle
        return

    @property
    def wasInBattle(self):
        return self.__wasInBattle


class UnpackedInfo(object):
    __slots__ = (b'__unpackedItemsIDs',)

    def __init__(self):
        super(UnpackedInfo, self).__init__()
        self.__unpackedItemsIDs = []
        return

    def getNumberOfUnpackedItems(self):
        return len(self.__unpackedItemsIDs)

    def hasUnpackedItems(self):
        return self.getNumberOfUnpackedItems() > 0

    def _addUnpackedItemID(self, itemUniqueID):
        self.__unpackedItemsIDs.append(itemUniqueID)
        return


def no_key_error(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            LOG_CURRENT_EXCEPTION()

        return

    return wrapper


class TeamBasesInfo(object):
    __slots__ = (b'__capturePoints', b'__droppedCapturePoints')

    def __init__(self, capturePoints=0, droppedCapturePoints=0):
        super(TeamBasesInfo, self).__init__()
        self.__capturePoints = capturePoints
        self.__droppedCapturePoints = droppedCapturePoints
        return

    @property
    def capturePoints(self):
        return self.__capturePoints

    @property
    def droppedCapturePoints(self):
        return self.__droppedCapturePoints


class _VehicleInfo(object):
    __slots__ = (b'_vehicleID', b'_vehicle', b'_player', b'_deathReason')

    def __init__(self, vehicleID, player, deathReason=DEATH_REASON_ALIVE):
        super(_VehicleInfo, self).__init__()
        self._vehicleID = vehicleID
        self._player = player
        self._deathReason = deathReason
        return

    @property
    def vehicleID(self):
        return self._vehicleID

    @property
    def vehicle(self):
        raise NotImplementedError
        return

    @property
    def killerID(self):
        raise NotImplementedError
        return

    @property
    def player(self):
        return self._player

    @property
    def deathReason(self):
        return self._deathReason

    @property
    def achievementsIDs(self):
        raise NotImplementedError
        return

    @property
    def spotted(self):
        raise NotImplementedError
        return

    @property
    def piercings(self):
        raise NotImplementedError
        return

    @property
    def piercingsReceived(self):
        raise NotImplementedError
        return

    @property
    def damageDealt(self):
        raise NotImplementedError
        return

    @property
    def tdamageDealt(self):
        raise NotImplementedError
        return

    @property
    def sniperDamageDealt(self):
        raise NotImplementedError
        return

    @property
    def artilleryFortEquipDamageDealt(self):
        raise NotImplementedError
        return

    @property
    def kills(self):
        raise NotImplementedError
        return

    @property
    def tkills(self):
        raise NotImplementedError
        return

    @property
    def targetKills(self):
        raise NotImplementedError
        return

    @property
    def noDamageDirectHitsReceived(self):
        raise NotImplementedError
        return

    @property
    def damageBlockedByArmor(self):
        raise NotImplementedError
        return

    @property
    def rickochetsReceived(self):
        raise NotImplementedError
        return

    @property
    def damageAssistedTrack(self):
        raise NotImplementedError
        return

    @property
    def damageAssistedRadio(self):
        raise NotImplementedError
        return

    @property
    def damageAssisted(self):
        raise NotImplementedError
        return

    @property
    def damageAssistedStun(self):
        raise NotImplementedError
        return

    @property
    def stunNum(self):
        raise NotImplementedError
        return

    @property
    def stunDuration(self):
        raise NotImplementedError
        return

    @property
    def critsInfo(self):
        raise NotImplementedError
        return

    @property
    def critsCount(self):
        raise NotImplementedError
        return

    @property
    def shots(self):
        raise NotImplementedError
        return

    @property
    def explosionHits(self):
        raise NotImplementedError
        return

    @property
    def directHits(self):
        raise NotImplementedError
        return

    @property
    def directHitsReceived(self):
        raise NotImplementedError
        return

    @property
    def explosionHitsReceived(self):
        raise NotImplementedError
        return

    @property
    def damaged(self):
        raise NotImplementedError
        return

    @property
    def mileage(self):
        raise NotImplementedError
        return

    @property
    def capturePoints(self):
        raise NotImplementedError
        return

    @property
    def droppedCapturePoints(self):
        raise NotImplementedError
        return

    @property
    def xp(self):
        raise NotImplementedError
        return

    @property
    def xpForAttack(self):
        raise NotImplementedError
        return

    @property
    def xpForAssist(self):
        raise NotImplementedError
        return

    @property
    def xpOther(self):
        raise NotImplementedError
        return

    @property
    def xpPenalty(self):
        raise NotImplementedError
        return

    @property
    def isTeamKiller(self):
        raise NotImplementedError
        return

    @property
    def isKilledByTeamKiller(self):
        raise NotImplementedError
        return

    @property
    def deathCount(self):
        raise NotImplementedError
        return

    @property
    def rollouts(self):
        raise NotImplementedError
        return

    @property
    def respawns(self):
        raise NotImplementedError
        return

    @property
    def numDefended(self):
        raise NotImplementedError
        return

    @property
    def numRecovered(self):
        raise NotImplementedError
        return

    @property
    def numCaptured(self):
        raise NotImplementedError
        return

    @property
    def numDestroyed(self):
        raise NotImplementedError
        return

    @property
    def destructiblesDamageDealt(self):
        raise NotImplementedError
        return

    @property
    def damageToSupplies(self):
        raise NotImplementedError
        return

    @property
    def damageFromSupplies(self):
        raise NotImplementedError
        return

    @property
    def suppliesDestroyed(self):
        raise NotImplementedError
        return

    @property
    def distributedSupplyDamage(self):
        raise NotImplementedError
        return

    @property
    def distributedSupplyCapturePoints(self):
        raise NotImplementedError
        return

    @property
    def distributedSupplyDefensePoints(self):
        raise NotImplementedError
        return

    @property
    def questsCompleted(self):
        raise NotImplementedError
        return

    @property
    def equipmentDamageDealt(self):
        raise NotImplementedError
        return

    @property
    def equipmentDamageAssisted(self):
        raise NotImplementedError
        return

    def getOrderByClass(self):
        return Vehicle.getOrderByVehicleClass(Vehicle.getVehicleClassTag(self.vehicle.descriptor.type.tags))


class VehicleDetailedInfo(_VehicleInfo):
    __slots__ = (b'_vehicle', b'_killerID', b'_achievementsIDs', b'_critsInfo', b'_spotted', b'_piercings', b'_piercingEnemyHits', b'_piercingsReceived', b'_damageDealt', b'_tdamageDealt', b'_sniperDamageDealt', b'_artilleryFortEquipDamageDealt', b'_damageBlockedByArmor', b'_damageAssistedTrack', b'_damageAssistedRadio', b'_damageAssistedStun', b'_stunNum', b'_stunDuration', b'_rickochetsReceived', b'_noDamageDirectHitsReceived', b'_targetKills', b'_directHits', b'_directEnemyHits', b'_directHitsReceived', b'_explosionHits', b'_explosionHitsReceived', b'_shots', b'_kills', b'_tkills', b'_damaged', b'_mileage', b'_capturePoints', b'_droppedCapturePoints', b'_xp', b'_fire', b'_isTeamKiller', b'_isKilledByTeamKiller', b'_rollouts', b'_respawns', b'_deathCount', b'_equipmentDamageDealt', b'_equipmentDamageAssisted', b'_xpForAttack', b'_xpForAssist', b'_xpOther', b'_xpPenalty', b'_numDefended', b'_vehicleNumCaptured', b'_numRecovered', b'_destructiblesNumDestroyed', b'_destructiblesDamageDealt', b'_achievedLevel', b'_prestigePoints', b'_roleSkillUsed', b'_healthRepair', b'_alliedHealthRepair', b'_entityCaptured', b'_damageToSupplies', b'_damageFromSupplies', b'_suppliesDestroyed', b'_distributedSupplyDamage', b'_distributedSupplyCapturePoints', b'_distributedSupplyDefensePoints', b'_questsCompleted')

    def __init__(self, vehicleID, vehicle, player, deathReason=DEATH_REASON_ALIVE):
        super(VehicleDetailedInfo, self).__init__(vehicleID, player, deathReason)
        self._vehicle = vehicle
        self._killerID = 0
        self._achievementsIDs = set()
        self._critsInfo = makeCritsInfo(0)
        self._spotted = 0
        self._piercings = 0
        self._piercingEnemyHits = 0
        self._piercingsReceived = 0
        self._damageBlockedByArmor = 0
        self._rickochetsReceived = 0
        self._noDamageDirectHitsReceived = 0
        self._targetKills = 0
        self._damageDealt = 0
        self._tdamageDealt = 0
        self._sniperDamageDealt = 0
        self._artilleryFortEquipDamageDealt = 0
        self._equipmentDamageDealt = 0
        self._damageAssistedTrack = 0
        self._damageAssistedRadio = 0
        self._damageAssistedStun = 0
        self._equipmentDamageAssisted = 0
        self._stunNum = 0
        self._stunDuration = 0
        self._directHits = 0
        self._directEnemyHits = 0
        self._directHitsReceived = 0
        self._explosionHits = 0
        self._explosionHitsReceived = 0
        self._shots = 0
        self._kills = 0
        self._tkills = 0
        self._damaged = 0
        self._mileage = 0
        self._capturePoints = 0
        self._droppedCapturePoints = 0
        self._xp = 0
        self._fire = 0
        self._isTeamKiller = False
        self._rollouts = 0
        self._respawns = 0
        self._deathCount = 0
        self._xpForAssist = 0
        self._xpForAttack = 0
        self._xpOther = 0
        self._xpPenalty = 0
        self._isKilledByTeamKiller = False
        self._numRecovered = 0
        self._vehicleNumCaptured = 0
        self._destructiblesNumDestroyed = 0
        self._destructiblesDamageDealt = 0
        self._numDefended = 0
        self._achievedLevel = 0
        self._prestigePoints = 0
        self._roleSkillUsed = 0
        self._healthRepair = 0
        self._alliedHealthRepair = 0
        self._damageToSupplies = 0
        self._damageFromSupplies = 0
        self._suppliesDestroyed = 0
        self._distributedSupplyDamage = 0
        self._distributedSupplyCapturePoints = 0
        self._distributedSupplyDefensePoints = 0
        self._questsCompleted = 0
        self._entityCaptured = {}
        return

    @property
    def vehicle(self):
        return self._vehicle

    @property
    def killerID(self):
        return self._killerID

    @property
    def achievementsIDs(self):
        return self._achievementsIDs

    @property
    def spotted(self):
        return self._spotted

    @property
    def piercings(self):
        return self._piercings

    @property
    def piercingEnemyHits(self):
        return self._piercingEnemyHits

    @property
    def piercingsReceived(self):
        return self._piercingsReceived

    @property
    def damageDealt(self):
        return self._damageDealt + self.destructiblesDamageDealt

    @property
    def damageToSupplies(self):
        return self._damageToSupplies

    @property
    def damageFromSupplies(self):
        return self._damageFromSupplies

    @property
    def suppliesDestroyed(self):
        return self._suppliesDestroyed

    @property
    def distributedSupplyDamage(self):
        return self._distributedSupplyDamage

    @property
    def distributedSupplyCapturePoints(self):
        return self._distributedSupplyCapturePoints

    @property
    def distributedSupplyDefensePoints(self):
        return self._distributedSupplyDefensePoints

    @property
    def questsCompleted(self):
        return self._questsCompleted

    @property
    def tdamageDealt(self):
        return self._tdamageDealt

    @property
    def sniperDamageDealt(self):
        return self._sniperDamageDealt

    @property
    def artilleryFortEquipDamageDealt(self):
        return self._artilleryFortEquipDamageDealt

    @property
    def equipmentDamageDealt(self):
        return self._equipmentDamageDealt

    @property
    def targetKills(self):
        return self._targetKills

    @property
    def noDamageDirectHitsReceived(self):
        return self._noDamageDirectHitsReceived

    @property
    def damageBlockedByArmor(self):
        return self._damageBlockedByArmor

    @property
    def rickochetsReceived(self):
        return self._rickochetsReceived

    @property
    def damageAssistedTrack(self):
        return self._damageAssistedTrack

    @property
    def damageAssistedRadio(self):
        return self._damageAssistedRadio

    @property
    def damageAssisted(self):
        return self._damageAssistedTrack + self._damageAssistedRadio

    @property
    def damageAssistedStun(self):
        return self._damageAssistedStun

    @property
    def equipmentDamageAssisted(self):
        return self._equipmentDamageAssisted

    @property
    def stunNum(self):
        return self._stunNum

    @property
    def stunDuration(self):
        return self._stunDuration

    @property
    def critsInfo(self):
        return self._critsInfo

    @property
    def critsCount(self):
        return self.critsInfo[b'critsCount']

    @property
    def shots(self):
        return self._shots

    @property
    def explosionHits(self):
        return self._explosionHits

    @property
    def directHits(self):
        return self._directHits

    @property
    def directEnemyHits(self):
        return self._directEnemyHits

    @property
    def directHitsReceived(self):
        return self._directHitsReceived

    @property
    def explosionHitsReceived(self):
        return self._explosionHitsReceived

    @property
    def kills(self):
        return self._kills

    @property
    def tkills(self):
        return self._tkills

    @property
    def damaged(self):
        return self._damaged

    @property
    def mileage(self):
        return self._mileage

    @property
    def capturePoints(self):
        return self._capturePoints

    @property
    def droppedCapturePoints(self):
        return self._droppedCapturePoints

    @property
    def xp(self):
        return self._xp

    @property
    def isTeamKiller(self):
        return self._isTeamKiller

    @property
    def isKilledByTeamKiller(self):
        return self._isKilledByTeamKiller

    @property
    def deathCount(self):
        return self._deathCount

    @property
    def rollouts(self):
        return self._rollouts

    @property
    def respawns(self):
        return self._respawns

    @property
    def achievedLevel(self):
        return self._achievedLevel

    @property
    def numDefended(self):
        return self._numDefended

    @property
    def numRecovered(self):
        return self._numRecovered

    @property
    def numCaptured(self):
        return self._vehicleNumCaptured

    @property
    def numDestroyed(self):
        return self._destructiblesNumDestroyed

    @property
    def destructiblesDamageDealt(self):
        return self._destructiblesDamageDealt

    @property
    def xpForAssist(self):
        return self._xpForAssist

    @property
    def xpForAttack(self):
        return self._xpForAttack

    @property
    def xpOther(self):
        return self._xpOther

    @property
    def xpPenalty(self):
        return self._xpPenalty

    @property
    def prestigePoints(self):
        return self._prestigePoints

    @property
    def roleSkillUsed(self):
        return self._roleSkillUsed

    @property
    def healthRepair(self):
        return self._healthRepair

    @property
    def alliedHealthRepair(self):
        return self._alliedHealthRepair

    @property
    def entityCaptured(self):
        return self._entityCaptured

    def haveInteractionDetails(self):
        return self._spotted != 0 or self._deathReason > DEATH_REASON_ALIVE or self._directHits != 0 or self._directEnemyHits != 0 or self._explosionHits != 0 or self._piercings != 0 or self._piercingEnemyHits != 0 or self._damageDealt != 0 or self.damageAssisted != 0 or self.damageAssistedStun != 0 or self.stunNum != 0 or self.critsCount != 0 or self._fire != 0 or self._targetKills != 0 or self.stunDuration != 0 or self._damageBlockedByArmor != 0

    @classmethod
    @no_key_error
    def makeForEnemy(cls, vehicleID, vehicle, player, detailsRecords, deathReason=DEATH_REASON_ALIVE, isTeamKiller=False):
        info = cls(vehicleID, vehicle, player, deathReason=deathReason)
        info._critsInfo = makeCritsInfo(detailsRecords[b'crits'])
        info._rickochetsReceived = detailsRecords[b'rickochetsReceived']
        info._targetKills = detailsRecords[b'targetKills']
        info._fire = detailsRecords[b'fire']
        info._isTeamKiller = isTeamKiller
        info._isKilledByTeamKiller = False
        cls._setSharedRecords(info, detailsRecords)
        return info

    @classmethod
    @no_key_error
    def makeForVehicle(cls, vehicleID, vehicle, player, vehicleRecords, critsRecords=None):
        info = cls(vehicleID, vehicle, player)
        if critsRecords is not None:
            critsInfo = makeCritsInfo(0)
            for crits in critsRecords:
                unionCritsInfo(critsInfo, makeCritsInfo(crits))

            info._critsInfo = critsInfo
        info._killerID = vehicleRecords[b'killerID']
        info._achievementsIDs = set(vehicleRecords[b'achievements'])
        info._piercingsReceived = vehicleRecords[b'piercingsReceived']
        info._tdamageDealt = vehicleRecords[b'tdamageDealt']
        info._sniperDamageDealt = vehicleRecords[b'sniperDamageDealt']
        info._artilleryFortEquipDamageDealt = vehicleRecords[b'artilleryFortEquipDamageDealt']
        info._equipmentDamageDealt = vehicleRecords[b'equipmentDamageDealt']
        info._shots = vehicleRecords[b'shots']
        info._directHitsReceived = vehicleRecords[b'directHitsReceived']
        info._explosionHitsReceived = vehicleRecords[b'explosionHitsReceived']
        info._kills = vehicleRecords[b'kills']
        info._tkills = vehicleRecords[b'tkills']
        info._damaged = vehicleRecords[b'damaged']
        info._mileage = vehicleRecords[b'mileage']
        info._capturePoints = vehicleRecords[b'capturePoints']
        info._droppedCapturePoints = vehicleRecords[b'droppedCapturePoints']
        if b'originalXP' in vehicleRecords:
            info._xp = vehicleRecords[b'originalXP']
        else:
            info._xp = vehicleRecords[b'xp'] - vehicleRecords[b'achievementXP']
        info._xpOther = vehicleRecords[b'xp/other']
        info._xpForAssist = vehicleRecords[b'xp/assist']
        info._xpForAttack = vehicleRecords[b'xp/attack']
        info._xpPenalty = vehicleRecords[b'xpPenalty']
        info._isTeamKiller = vehicleRecords[b'isTeamKiller']
        info._isKilledByTeamKiller = vehicleRecords.get(b'isKilledByTeamKiller', False)
        info._rollouts = vehicleRecords[b'rolloutsCount']
        info._respawns = vehicleRecords[b'rolloutsCount'] - 1 if vehicleRecords[b'rolloutsCount'] > 0 else 0
        info._deathCount = vehicleRecords[b'deathCount']
        info._numRecovered = vehicleRecords[b'numRecovered']
        info._vehicleNumCaptured = vehicleRecords[b'vehicleNumCaptured']
        info._destructiblesNumDestroyed = vehicleRecords[b'destructiblesNumDestroyed']
        info._destructiblesDamageDealt = vehicleRecords[b'destructiblesDamageDealt']
        info._numDefended = vehicleRecords[b'numDefended']
        info._equipmentDamageAssisted = vehicleRecords.get(b'damageAssistedInspire', 0) + vehicleRecords.get(b'damageAssistedSmoke', 0)
        info._achievedLevel = vehicleRecords.get(b'achivedLevel', 0)
        info._prestigePoints = vehicleRecords.get(b'comp7PrestigePoints', 0)
        info._roleSkillUsed = vehicleRecords.get(b'roleSkillUsed', 0)
        info._healthRepair = vehicleRecords.get(b'healthRepair', 0)
        info._alliedHealthRepair = vehicleRecords.get(b'alliedHealthRepair', 0)
        info._entityCaptured = vehicleRecords.get(b'entityCaptured', {})
        info._damageToSupplies = vehicleRecords.get(b'damageToSupplies', 0)
        info._damageFromSupplies = vehicleRecords.get(b'damageFromSupplies', 0)
        info._suppliesDestroyed = vehicleRecords.get(b'suppliesDestroyed', 0)
        info._distributedSupplyDamage = vehicleRecords.get(b'distributedSupplyDamage', 0)
        info._distributedSupplyCapturePoints = vehicleRecords.get(b'distributedSupplyCapturePoints', 0)
        info._distributedSupplyDefensePoints = vehicleRecords.get(b'distributedSupplyDefensePoints', 0)
        info._questsCompleted = vehicleRecords.get(b'frontlineQuestsCompleted', 0)
        cls._setSharedRecords(info, vehicleRecords)
        return info

    @classmethod
    def _setSharedRecords(cls, info, records):
        info._deathReason = max(info._deathReason, records[b'deathReason'])
        info._spotted = records[b'spotted']
        info._piercings = records[b'piercings']
        info._piercingEnemyHits = records[b'piercingEnemyHits']
        info._damageDealt = records[b'damageDealt']
        info._damageBlockedByArmor = records[b'damageBlockedByArmor']
        info._noDamageDirectHitsReceived = records[b'noDamageDirectHitsReceived']
        info._damageAssistedTrack = records[b'damageAssistedTrack']
        info._damageAssistedRadio = records[b'damageAssistedRadio']
        info._directHits = records[b'directHits']
        info._directEnemyHits = records[b'directEnemyHits']
        info._explosionHits = records[b'explosionHits']
        info._damageAssistedStun = records[b'damageAssistedStun']
        info._stunNum = records[b'stunNum']
        info._stunDuration = records[b'stunDuration']
        return


class VehicleSummarizeInfo(_VehicleInfo):
    __slots__ = (b'__avatar', b'__vehicles')

    def __init__(self, vehicleID, player):
        super(VehicleSummarizeInfo, self).__init__(vehicleID, player)
        self.__avatar = None
        self.__vehicles = []
        return

    @property
    def avatar(self):
        return self.__avatar

    @property
    def vehicle(self):
        if self.__vehicles:
            return self.__vehicles[0].vehicle
        else:
            return

    @property
    def isTeamKiller(self):
        return any(self._getAtrributeGenerator(b'isTeamKiller'))

    @property
    def isKilledByTeamKiller(self):
        return any(self._getAtrributeGenerator(b'isKilledByTeamKiller'))

    @property
    def vehicles(self):
        if self.__vehicles:
            return self.__vehicles
        return []

    @property
    def killerID(self):
        return self._findFirstNoZero(b'killerID')

    @property
    def deathReason(self):
        return self._findMaxInt(b'deathReason', start=DEATH_REASON_ALIVE)

    @property
    def achievementsIDs(self):
        return self._collectToSet(b'achievementsIDs')

    @property
    def spotted(self):
        return self._accumulate(b'spotted')

    @property
    def piercings(self):
        return self._accumulate(b'piercings')

    @property
    def piercingEnemyHits(self):
        return self._accumulate(b'piercingEnemyHits')

    @property
    def piercingsReceived(self):
        return self._accumulate(b'piercingsReceived')

    @property
    def damageDealt(self):
        value = self._accumulate(b'damageDealt')
        if self.__avatar is not None:
            value += self.__avatar.avatarDamageDealt
        return value

    @property
    def tdamageDealt(self):
        return self._accumulate(b'tdamageDealt')

    @property
    def sniperDamageDealt(self):
        return self._accumulate(b'sniperDamageDealt')

    @property
    def artilleryFortEquipDamageDealt(self):
        return self._accumulate(b'artilleryFortEquipDamageDealt')

    @property
    def targetKills(self):
        return self._accumulate(b'targetKills')

    @property
    def noDamageDirectHitsReceived(self):
        return self._accumulate(b'noDamageDirectHitsReceived')

    @property
    def damageBlockedByArmor(self):
        return self._accumulate(b'damageBlockedByArmor')

    @property
    def rickochetsReceived(self):
        return self._accumulate(b'rickochetsReceived')

    @property
    def damageAssistedTrack(self):
        return self._accumulate(b'damageAssistedTrack')

    @property
    def damageAssistedRadio(self):
        return self._accumulate(b'damageAssistedRadio')

    @property
    def damageAssisted(self):
        return self._accumulate(b'damageAssisted')

    @property
    def damageAssistedStun(self):
        return self._accumulate(b'damageAssistedStun')

    @property
    def stunNum(self):
        return self._accumulate(b'stunNum')

    @property
    def stunDuration(self):
        return self._accumulate(b'stunDuration')

    @property
    def critsInfo(self):
        result = {b'critsCount': 0}
        for value in self._getAtrributeGenerator(b'critsInfo'):
            unionCritsInfo(result, value)

        return result

    @property
    def critsCount(self):
        return self.critsInfo[b'critsCount']

    @property
    def shots(self):
        return self._accumulate(b'shots')

    @property
    def explosionHits(self):
        return self._accumulate(b'explosionHits')

    @property
    def directHits(self):
        return self._accumulate(b'directHits')

    @property
    def directEnemyHits(self):
        return self._accumulate(b'directEnemyHits')

    @property
    def directHitsReceived(self):
        return self._accumulate(b'directHitsReceived')

    @property
    def explosionHitsReceived(self):
        return self._accumulate(b'explosionHitsReceived')

    @property
    def kills(self):
        value = self._accumulate(b'kills')
        if self.__avatar is not None:
            value += self.__avatar.avatarKills
        return value

    @property
    def tkills(self):
        return self._accumulate(b'tkills')

    @property
    def damaged(self):
        return self._accumulate(b'damaged')

    @property
    def mileage(self):
        return self._accumulate(b'mileage')

    @property
    def capturePoints(self):
        return self._accumulate(b'capturePoints')

    @property
    def droppedCapturePoints(self):
        return self._accumulate(b'droppedCapturePoints')

    @property
    def xp(self):
        return self._accumulate(b'xp')

    @property
    def xpForAttack(self):
        return self._accumulate(b'xpForAttack')

    @property
    def xpForAssist(self):
        return self._accumulate(b'xpForAssist')

    @property
    def xpOther(self):
        return self._accumulate(b'xpOther')

    @property
    def xpPenalty(self):
        return self._accumulate(b'xpPenalty')

    @property
    def deathCount(self):
        return self._accumulate(b'deathCount')

    @property
    def rollouts(self):
        return self._accumulate(b'rollouts')

    @property
    def respawns(self):
        return self._accumulate(b'rollouts') - 1

    @property
    def numDefended(self):
        return self._accumulate(b'numDefended')

    @property
    def numRecovered(self):
        return self._accumulate(b'numRecovered')

    @property
    def numCaptured(self):
        return self._accumulate(b'numCaptured')

    @property
    def numDestroyed(self):
        return self._accumulate(b'numDestroyed')

    @property
    def destructiblesDamageDealt(self):
        return self._accumulate(b'destructiblesDamageDealt')

    @property
    def damageToSupplies(self):
        return self._accumulate(b'damageToSupplies')

    @property
    def damageFromSupplies(self):
        return self._accumulate(b'damageFromSupplies')

    @property
    def suppliesDestroyed(self):
        return self._accumulate(b'suppliesDestroyed')

    @property
    def distributedSupplyDamage(self):
        if self.avatar is not None:
            return self.avatar.extensionInfo.get(b'distributedSupplyDamage', 0)
        else:
            return 0

    @property
    def distributedSupplyCapturePoints(self):
        if self.avatar is not None:
            return self.avatar.extensionInfo.get(b'distributedSupplyCapturePoints', 0)
        else:
            return 0

    @property
    def distributedSupplyDefensePoints(self):
        if self.avatar is not None:
            return self.avatar.extensionInfo.get(b'distributedSupplyDefensePoints', 0)
        else:
            return 0

    @property
    def questsCompleted(self):
        return self._accumulate(b'questsCompleted')

    @property
    def equipmentDamageDealt(self):
        return self._accumulate(b'equipmentDamageDealt')

    @property
    def equipmentDamageAssisted(self):
        return self._accumulate(b'equipmentDamageAssisted')

    @property
    def prestigePoints(self):
        return self._accumulate(b'prestigePoints')

    @property
    def roleSkillUsed(self):
        return self._accumulate(b'roleSkillUsed')

    @property
    def healthRepair(self):
        return self._accumulate(b'healthRepair')

    @property
    def alliedHealthRepair(self):
        return self._accumulate(b'alliedHealthRepair')

    @property
    def entityCaptured(self):
        return self._collectToDict(b'entityCaptured')

    def addVehicleInfo(self, info):
        self.__vehicles.append(info)
        return

    def addAvatarInfo(self, avatar):
        self.__avatar = avatar
        return

    def getVehiclesIterator(self):
        yield self
        for vehicle in self.__vehicles:
            yield vehicle

        return

    def getAchievements(self):
        result = []
        for achievementID in self.achievementsIDs:
            record = DB_ID_TO_RECORD[achievementID]
            factory = getAchievementFactory(record)
            if factory is not None and layouts.isAchievementRegistered(record):
                achievement = factory.create(value=0)
                if not achievement.isApproachable():
                    result.append((achievement, True))

        return sorted(result, key=sort_keys.AchievementSortKey)

    def _getAtrributeGenerator(self, attr):
        getter = operator.attrgetter(attr)
        for vehicle in self.__vehicles:
            yield getter(vehicle)

        return

    def _findFirstNoZero(self, attr):
        return findFirst((lambda value: value > 0), self._getAtrributeGenerator(attr), default=0)

    def _findMaxInt(self, attr, start=0):
        result = start
        for value in self._getAtrributeGenerator(attr):
            result = max(result, value)

        return result

    def _collectToSet(self, attr):
        result = set()
        for value in self._getAtrributeGenerator(attr):
            result |= value

        return result

    def _collectToDict(self, attr):
        result = {}
        for value in self._getAtrributeGenerator(attr):
            result.update(value)

        return result

    def _accumulate(self, attr):
        return sum(self._getAtrributeGenerator(attr))


class FairplayViolationsInfo(object):
    __slots__ = (b'_warningsMask', b'_penaltiesMask', b'_violationsMask', b'_penaltiesInPercent')

    def __init__(self, warningsMask=0, penaltiesMask=0, violationsMask=0, penaltiesInPercent=-100):
        super(FairplayViolationsInfo, self).__init__()
        self._warningsMask = warningsMask
        self._penaltiesMask = penaltiesMask
        self._violationsMask = violationsMask
        self._penaltiesInPercent = penaltiesInPercent
        return

    def hasWarnings(self):
        return self._warningsMask != 0

    def hasPenalties(self):
        return self._penaltiesMask != 0

    def hasViolations(self):
        return self._violationsMask != 0

    def getWarningName(self):
        return getFairPlayViolationName(self._warningsMask)

    def getPenaltyName(self):
        return getFairPlayViolationName(self._penaltiesMask)

    def getViolationName(self):
        return getFairPlayViolationName(self._violationsMask)

    def getPenaltyDetails(self):
        if self.hasPenalties():
            return (self.getPenaltyName(), self._penaltiesInPercent)
        else:
            return
