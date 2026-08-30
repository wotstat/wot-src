import typing
from collections import namedtuple
from gui.impl.gen import R
from gui.impl import backport
from gui.battle_control.battle_constants import WinStatus
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.postbattle.achievement_model import AchievementModel
from white_tiger.gui.impl.lobby.battle_result.team_stats import getTeamStats
from soft_exception import SoftException
from dossiers2.ui.achievements import ACHIEVEMENT_TYPE, MARK_OF_MASTERY, MARK_ON_GUN_RECORD, MARK_OF_MASTERY_RECORD
from shared_utils import CONST_CONTAINER
from gui.Scaleform.genConsts.BATTLE_EFFICIENCY_TYPES import BATTLE_EFFICIENCY_TYPES
from constants import DEATH_REASON_ALIVE
from gui.shared.utils.functions import replaceHyphenToUnderscore
from gui.shared.gui_items.Vehicle import getIconResourceName, getSimpleShortUserName
from gui.battle_results.reusable.shared import makeMarkOfMasteryFromPersonal, VehicleSummarizeInfo
from dossiers2.ui import achievements, layouts
from dossiers2.custom.records import DB_ID_TO_RECORD
from shared_utils import findFirst
from gui.shared.gui_items.dossier import getAchievementFactory
from items import vehicles as vehicles_core
from debug_utils import LOG_CURRENT_EXCEPTION
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo
_AchievementData = namedtuple(b'_AchievementData', (b'achievementID', b'name', b'isEpic', b'iconName', b'groupID', b'isPersonal'))
_FinancialRecords = namedtuple(b'_FinancialRecords', (b'main', b'additional', b'alternative'))
_XpRecords = namedtuple(b'_XpRecords', (b'xp', b'freeXP'))
_PlayerNames = namedtuple(b'PlayerNames', (b'displayedName', b'hiddenName', b'isFakeNameVisible'))
MAX_TEAM_RANK = 3
STAT_STUN_FIELD_NAMES = (b'damageAssistedStun', b'stunNum', b'stunDuration')

def _findAchievementInDossier(achievementID, dossierPopUps):
    achievementData = findFirst((lambda e: e[0] == achievementID), dossierPopUps)
    return achievementData[1]


def makeAchievement(achievementID, results=None):
    popUps = results.get(b'dossierPopUps', []) if results is not None else []
    record = DB_ID_TO_RECORD[achievementID]
    if record in layouts.IGNORED_BY_BATTLE_RESULTS or not layouts.isAchievementRegistered(record):
        return
    factory = getAchievementFactory(record)
    if factory is None:
        return
    else:
        popUpsValue = _findAchievementInDossier(achievementID, popUps) if popUps else 0
        achievement = factory.create(value=popUpsValue)
        if record == achievements.MARK_ON_GUN_RECORD:
            if b'typeCompDescr' in results:
                try:
                    nationID = vehicles_core.parseIntCompactDescr(results[b'typeCompDescr'])[1]
                    achievement.setVehicleNationID(nationID)
                except SoftException:
                    LOG_CURRENT_EXCEPTION()

            if b'damageRating' in results:
                achievement.setDamageRating(results[b'damageRating'])
        return achievement


class PersonalEfficiency(CONST_CONTAINER):
    SPOTTED = b'spotted'
    KILLS = b'kills'
    STUN = b'damageAssistedStun'
    DAMAGE = b'damageDealt'
    ARMOR = b'damageBlockedByArmor'
    ASSIST = b'damageAssisted'
    CRITS = b'critsCount'
    ALL = (
     STUN, SPOTTED, ASSIST, ARMOR, CRITS, DAMAGE, KILLS)


class EfficiencyKeys(CONST_CONTAINER):
    ENEMY_PARAM_NAME = b'enemyParamName'
    TOTAL = b'summ'
    ICON = b'icon'
    TYPE = b'effType'


EfficiencyItems = {(PersonalEfficiency.SPOTTED): {(EfficiencyKeys.TOTAL): b'summSpotted', 
                                  (EfficiencyKeys.ENEMY_PARAM_NAME): b'spotted', 
                                  (EfficiencyKeys.TYPE): (BATTLE_EFFICIENCY_TYPES.DETECTION)}, 
   (PersonalEfficiency.ASSIST): {(EfficiencyKeys.TOTAL): b'summAssist', 
                                 (EfficiencyKeys.ENEMY_PARAM_NAME): b'damageAssisted', 
                                 (EfficiencyKeys.TYPE): (BATTLE_EFFICIENCY_TYPES.ASSIST)}, 
   (PersonalEfficiency.ARMOR): {(EfficiencyKeys.TOTAL): b'summArmor', 
                                (EfficiencyKeys.ENEMY_PARAM_NAME): b'damageBlockedByArmor', 
                                (EfficiencyKeys.TYPE): (BATTLE_EFFICIENCY_TYPES.ARMOR)}, 
   (PersonalEfficiency.DAMAGE): {(EfficiencyKeys.TOTAL): b'summDamage', 
                                 (EfficiencyKeys.ENEMY_PARAM_NAME): b'damageDealt', 
                                 (EfficiencyKeys.TYPE): (BATTLE_EFFICIENCY_TYPES.DAMAGE)}, 
   (PersonalEfficiency.KILLS): {(EfficiencyKeys.TOTAL): b'summKill', 
                                (EfficiencyKeys.ENEMY_PARAM_NAME): b'targetKills', 
                                (EfficiencyKeys.TYPE): (BATTLE_EFFICIENCY_TYPES.DESTRUCTION)}, 
   (PersonalEfficiency.STUN): {(EfficiencyKeys.TOTAL): b'summStun', 
                               (EfficiencyKeys.ENEMY_PARAM_NAME): b'damageAssistedStun', 
                               (EfficiencyKeys.TYPE): (BATTLE_EFFICIENCY_TYPES.ASSIST_STUN)}, 
   (PersonalEfficiency.CRITS): {(EfficiencyKeys.TOTAL): b'summCrits', 
                                (EfficiencyKeys.ENEMY_PARAM_NAME): b'critsCount', 
                                (EfficiencyKeys.TYPE): (BATTLE_EFFICIENCY_TYPES.CRITS)}}

def getKillerID(result, vehicleCD):
    return result[b'personal'][vehicleCD].get(b'killerID', 0)


def getPersonalTeamResult(reusable):
    winnerTeam = reusable.common.winnerTeam
    if not winnerTeam:
        return WinStatus.DRAW
    if winnerTeam == reusable.personal.avatar.team:
        return WinStatus.WIN
    return WinStatus.LOSE


def isPersonalResults(reusable, playerDBID):
    personalInfo = reusable.getPlayerInfo()
    return personalInfo.dbID == playerDBID


def isOwnSquad(reusable, vehicleID):
    personalInfo = reusable.getPlayerInfo()
    playerInfo = reusable.getPlayerInfoByVehicleID(vehicleID)
    personalPrebattleID = personalInfo.prebattleID if personalInfo.squadIndex else 0
    return personalPrebattleID != 0 and personalPrebattleID == playerInfo.prebattleID


def getUserNames(reusable, vehicleID):
    playerInfo = reusable.getPlayerInfoByVehicleID(vehicleID)
    if isBot(playerInfo):
        botName = backport.text(R.strings.event.postbattle_screen.botName())
        return _PlayerNames(displayedName=botName, hiddenName=botName, isFakeNameVisible=False)
    if playerInfo.realName == playerInfo.fakeName:
        return _PlayerNames(displayedName=playerInfo.realName, hiddenName=playerInfo.realName, isFakeNameVisible=False)
    isRealNameShown = isPersonalResults(reusable, playerInfo.dbID) or isOwnSquad(reusable, vehicleID)
    if isRealNameShown:
        displayedName = playerInfo.realName
        hiddenName = playerInfo.fakeName
    else:
        displayedName = playerInfo.fakeName
        hiddenName = playerInfo.realName
    return _PlayerNames(displayedName=displayedName, hiddenName=hiddenName, isFakeNameVisible=not isRealNameShown)


def isBot(playerInfo):
    return playerInfo.dbID == 0


def isPlayerLeftBattle(reusable):
    return reusable.personal.avatar.isPrematureLeave


def _processAchievement(item, groupID):
    achievement = item.achievement
    achievementID = item.achievementID
    isPersonal = item.isPersonal
    return _AchievementData(achievementID=achievementID, name=achievement.getName(), isEpic=achievement.hasRibbon(), iconName=achievement.getIconName(), groupID=groupID, isPersonal=isPersonal)


def setTeamStatsAchievements(model, info):
    rawAchievements = info.getAchievements()
    processedAchievements = [_processAchievement(item, AchievementModel.ACHIEVEMENT_RIGHT_BLOCK) for item in rawAchievements]
    _setAchievements(processedAchievements, model)
    return


def _setAchievements(processedAchievements, model):
    achievementsArr = Array()
    for achievement in processedAchievements:
        achievementModel = AchievementModel()
        achievementModel.setName(achievement.name)
        achievementModel.setIsEpic(achievement.isEpic)
        achievementModel.setIconName(achievement.iconName)
        achievementModel.setGroupID(achievement.groupID)
        achievementModel.setAchievementID(achievement.achievementID)
        achievementModel.setIsPersonal(achievement.isPersonal)
        achievementsArr.addViewModel(achievementModel)

    model.setAchievements(achievementsArr)
    return


class PostbattleFieldsGetter(object):
    __slots__ = (b'__teamStats',)

    def __init__(self, teamStatsFields):
        self.__teamStats = teamStatsFields
        return

    def clear(self):
        self.__teamStats = None
        return

    def getTeamStats(self, isSPG, isPersonal, isRoleExp):
        roleExpFields = (
         self.__teamStats.expSegments.total, self.__teamStats.expSegments.attack,
         self.__teamStats.expSegments.assist, self.__teamStats.expSegments.role)
        spgFields = (
         self.__teamStats.other.stunNum, self.__teamStats.other.stunDuration,
         self.__teamStats.other.damageAssistedStun, self.__teamStats.other.damageAssistedStunSelf)
        personalFields = (
         self.__teamStats.other.damageAssistedSelf, self.__teamStats.other.damageAssistedStunSelf)
        nonPersonalFields = (
         self.__teamStats.other.damageAssisted, self.__teamStats.other.damageAssistedStun)

        def filterFunc(field):
            return (field not in spgFields or isSPG) and (field not in personalFields or isPersonal) and (field not in nonPersonalFields or not isPersonal) and (field not in roleExpFields or isRoleExp)

        teamStats = self.__teamStats.expSegments + self.__teamStats.shots + self.__teamStats.damageDealt + self.__teamStats.hitsReceived + self.__teamStats.other + self.__teamStats.time
        for field in filter(filterFunc, teamStats):
            yield field

        return


def createFieldsGetter():
    return PostbattleFieldsGetter(teamStatsFields=getTeamStats())


def getAchievementTooltipData(achievementID, achievementName, isPersonal, reusable, results):
    if not isPersonal:
        achievement = makeAchievement(achievementID)
    else:
        playerInfo = reusable.getPlayerInfo()
        playerId = playerInfo.dbID
        vehicleId = reusable.vehicles.getVehicleID(playerId)
        vehicleInfo = reusable.vehicles.getVehicleInfo(vehicleId)
        intCD = vehicleInfo.intCD
        if achievementName == MARK_OF_MASTERY:
            results = results[b'personal'][intCD]
            achievement = makeMarkOfMasteryFromPersonal(results)
            achievement.setPrevMarkOfMastery(results.get(b'prevMarkOfMastery', 0))
            achievement.setCompDescr(results.get(b'typeCompDescr'))
        else:
            achievement = makeAchievement(achievementID, results[b'personal'][intCD])
    if achievement is None:
        SoftException((b'Achievement with id={} is incorrect').format(achievementID))
    return _packAchievementTooltipArgs(achievement, reusable)


def _packAchievementTooltipArgs(achievement, reusable):
    args = [
     achievement.getBlock(),
     achievement.getName(),
     achievement.getValue() if achievement.getType() != ACHIEVEMENT_TYPE.SERIES else 0,
     _getAchievementCustomData(achievement),
     _getVehicleLevel(reusable),
     reusable.common.arenaBonusType]
    return args


def _getVehicleLevel(reusable):
    playerVehiclesIterator = reusable.personal.getVehicleItemsIterator()
    for _, vehicle in playerVehiclesIterator:
        return vehicle.level

    return


def _getAchievementCustomData(item):
    customData = []
    achievementName = item.getRecordName()
    if achievementName == MARK_ON_GUN_RECORD:
        customData.extend([
         item.getDamageRating(), item.getVehicleNationID()])
    if achievementName == MARK_OF_MASTERY_RECORD:
        customData.extend([
         item.getPrevMarkOfMastery(), item.getCompDescr()])
    return customData


def getPlayerPlaceInTeam(reusableInfo, result, paramName, playerValue):
    if playerValue == 0:
        return MAX_TEAM_RANK
    allies, _ = reusableInfo.getBiDirectionTeamsIterator(result[b'vehicles'])
    winners = set()
    for ally in allies:
        allyValue = getattr(ally, paramName)
        if allyValue > playerValue:
            winners.add(allyValue)
        if len(winners) >= MAX_TEAM_RANK:
            return MAX_TEAM_RANK

    return len(winners)


def getEnemies(reusable, result):
    enemies = []
    for _, enemies in reusable.getPersonalDetailsIterator(result[b'personal']):
        continue

    return enemies


def setBaseUserInfo(model, vehicleID, reusable):
    playerInfo = reusable.getPlayerInfoByVehicleID(vehicleID)
    model.setClanAbbrev(playerInfo.clanAbbrev)
    model.setIgrType(playerInfo.igrType)
    userNames = getUserNames(reusable, vehicleID)
    model.setUserName(userNames.displayedName)
    model.setHiddenUserName(userNames.hiddenName)
    model.setIsFakeNameVisible(userNames.isFakeNameVisible)
    shortVehicleInfo = reusable.vehicles.getVehicleInfo(vehicleID)
    model.setIsTeamKiller(shortVehicleInfo.isTeamKiller)
    model.setIsKilled(shortVehicleInfo.deathReason > DEATH_REASON_ALIVE)
    if playerInfo.dbID:
        setBadges(model, playerInfo.dbID, reusable)
    return


def setBadges(model, playerDbID, reusable):
    if not playerDbID:
        return
    else:
        avatar = reusable.getAvatarInfo(playerDbID)
        if avatar is None:
            return
        badgeInfo = avatar.getFullBadgeInfo()
        if badgeInfo is not None:
            model.badge.setBadgeID(badgeInfo.getIconPostfix())
            level = badgeInfo.getDynamicContent()
            model.badge.setLevel(level if level is not None else b'')
        suffixBadge = avatar.suffixBadge
        model.suffixBadge.setBadgeID(str(suffixBadge) if suffixBadge else b'')
        return


def setBaseEnemyVehicleInfo(model, enemy):
    model.setTankType(replaceHyphenToUnderscore(enemy.vehicle.type))
    model.setTankName(replaceHyphenToUnderscore(getIconResourceName(enemy.vehicle.name)))
    model.setShortTankName(getSimpleShortUserName(enemy.vehicle))
    model.setVehicleIconName(getIconResourceName(enemy.vehicle.name))
    model.setVehicleLevel(enemy.vehicle.level)
    return
