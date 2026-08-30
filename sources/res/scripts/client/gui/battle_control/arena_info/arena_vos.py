import operator
from collections import defaultdict
from enum import Enum
import nations
from constants import IGR_TYPE, FLAG_ACTION, ARENA_GUI_TYPE, ROLE_TYPE
from debug_utils import LOG_ERROR
from gui import makeHtmlString
from gui.battle_control import avatar_getter, vehicle_getter
from gui.battle_control.arena_info import settings
from gui.battle_control.arena_info.settings import VehicleSpottedStatus
from gui.battle_control.dog_tag_composer import layoutComposer
from gui.doc_loaders.badges_loader import getSelectedByLayout
from gui.shared.gui_items import Vehicle
from gui.shared.gui_items.Vehicle import VEHICLE_TAGS, VEHICLE_CLASS_NAME
from gui.Scaleform.locale.EVENT import EVENT
from helpers import dependency, i18n
from skeletons.gui.server_events import IEventsCache
_INVALIDATE_OP = settings.INVALIDATE_OP
_VEHICLE_STATUS = settings.VEHICLE_STATUS
_PLAYER_STATUS = settings.PLAYER_STATUS
_DELIVERY_STATUS = settings.INVITATION_DELIVERY_STATUS
_DEFAULT_PLAYER_GROUP = 1
_DEFAULT_PLAYER_RANK = 0
_DEFAULT_PHYSICAL_SECTOR = 1
_DEFAULT_HAS_RESPAWNS = True
_DEFAULT_ROLE_SKILL = 0
_DEFAULT_ROLE_SKILL_LEVEL = 0
_DEFAULT_PLAYER_DIVISION = 0

class EPIC_RANDOM_KEYS(object):
    PLAYER_GROUP = b'playerGroup'

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(EPIC_RANDOM_KEYS.PLAYER_GROUP, _DEFAULT_PLAYER_GROUP)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        if static:
            return [EPIC_RANDOM_KEYS.PLAYER_GROUP]
        return []


class BattleRoyaleKeys(Enum):
    RANK = b'playerRank'

    @staticmethod
    def getKeys(static=True):
        if static:
            return []
        return [(BattleRoyaleKeys.RANK.value, _DEFAULT_PLAYER_RANK)]

    @staticmethod
    def getSortingKeys(static=True):
        if not static:
            return [BattleRoyaleKeys.RANK.value]
        return []


class EventKeys(Enum):
    LIVES_COUNT = b'livesCount'
    CAMP = b'camp'
    RESURRECT_TIME_LEFT = b'resurrectTimeLeft'
    RESURRECT_TIME_TOTAL = b'resurrectTimeTotal'
    SPEED = b'replaySpeed'
    PLASMA_COUNT = b'plasmaCount'

    @staticmethod
    def getKeys(static=True):
        if static:
            return []
        return [
         (
          EventKeys.LIVES_COUNT.value, 0),
         (
          EventKeys.CAMP.value, b''),
         (
          EventKeys.RESURRECT_TIME_LEFT.value, 0.0),
         (
          EventKeys.RESURRECT_TIME_TOTAL.value, 0.0),
         (
          EventKeys.SPEED.value, 1.0),
         (
          EventKeys.PLASMA_COUNT.value, 0)]

    @staticmethod
    def getSortingKeys(static=True):
        if not static:
            return [EventKeys.LIVES_COUNT.value]
        return []


class EPIC_BATTLE_KEYS(object):
    RANK = b'playerRank'
    PLAYER_GROUP = b'playerGroup'
    PHYSICAL_SECTOR = b'physicalSector'
    HAS_RESPAWNS = b'hasRespawns'

    @staticmethod
    def getKeys(static=True):
        if static:
            return []
        return [(EPIC_BATTLE_KEYS.RANK, _DEFAULT_PLAYER_RANK),
         (
          EPIC_BATTLE_KEYS.PLAYER_GROUP, _DEFAULT_PLAYER_GROUP),
         (
          EPIC_BATTLE_KEYS.PHYSICAL_SECTOR, _DEFAULT_PHYSICAL_SECTOR),
         (
          EPIC_BATTLE_KEYS.HAS_RESPAWNS, _DEFAULT_HAS_RESPAWNS)]

    @staticmethod
    def getSortingKeys(static=True):
        if not static:
            return [EPIC_BATTLE_KEYS.RANK]
        return []


class Comp7Keys(Enum):
    ROLE_SKILL = b'vehicleRoleSkill'
    ROLE_SKILL_LEVEL = b'vehicleRoleSkillLevel'
    RANK = b'rank'
    VOIP_CONNECTED = b'voipConnected'
    IS_QUAL_ACTIVE = b'isQualActive'

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(Comp7Keys.ROLE_SKILL, _DEFAULT_ROLE_SKILL), (Comp7Keys.ROLE_SKILL_LEVEL, _DEFAULT_ROLE_SKILL_LEVEL), (Comp7Keys.RANK, (_DEFAULT_PLAYER_RANK, _DEFAULT_PLAYER_DIVISION)), (Comp7Keys.VOIP_CONNECTED, False), (Comp7Keys.IS_QUAL_ACTIVE, False)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        if static:
            return [Comp7Keys.RANK]
        return []


class TournamentComp7Keys(Enum):

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(Comp7Keys.ROLE_SKILL, _DEFAULT_ROLE_SKILL), (Comp7Keys.ROLE_SKILL_LEVEL, _DEFAULT_ROLE_SKILL_LEVEL), (Comp7Keys.VOIP_CONNECTED, False)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        return []


class RankedKeys(Enum):
    VOIP_CONNECTED = b'voipConnected'

    @staticmethod
    def getKeys(static=True):
        if static:
            return [(RankedKeys.VOIP_CONNECTED, False)]
        return []

    @staticmethod
    def getSortingKeys(static=True):
        return []


GAMEMODE_SPECIFIC_KEYS = {(ARENA_GUI_TYPE.EPIC_RANDOM): EPIC_RANDOM_KEYS, 
   (ARENA_GUI_TYPE.EPIC_RANDOM_TRAINING): EPIC_RANDOM_KEYS, 
   (ARENA_GUI_TYPE.EPIC_BATTLE): EPIC_BATTLE_KEYS, 
   (ARENA_GUI_TYPE.EPIC_TRAINING): EPIC_BATTLE_KEYS, 
   (ARENA_GUI_TYPE.BATTLE_ROYALE): BattleRoyaleKeys, 
   (ARENA_GUI_TYPE.COMP7): Comp7Keys, 
   (ARENA_GUI_TYPE.TOURNAMENT_COMP7): TournamentComp7Keys, 
   (ARENA_GUI_TYPE.RANKED): RankedKeys}

class GameModeDataVO(object):
    __slots__ = (b'__internalData', b'__sortingKeys')

    def __init__(self, gameMode, static=True):
        self.__internalData = {}
        if gameMode in GAMEMODE_SPECIFIC_KEYS:
            keys = GAMEMODE_SPECIFIC_KEYS[gameMode]
            for key, defaultValue in keys.getKeys(static):
                self.__internalData[key] = defaultValue

            self.__sortingKeys = keys.getSortingKeys(static)
        else:
            self.__sortingKeys = []
        return

    def update(self, data):
        invalidate = _INVALIDATE_OP.NONE
        for key, value in data.items():
            if key in self.__sortingKeys:
                invalidate = _INVALIDATE_OP.SORTING
            if key in self.__internalData and self.__internalData[key] != value:
                invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.VEHICLE_STATS)
            self.__internalData[key] = value

        return invalidate

    def getValue(self, key, default=None):
        if key in self.__internalData:
            return self.__internalData[key]
        return default


def isObserver(tags):
    return VEHICLE_TAGS.OBSERVER in tags


def isPremium(tags):
    return VEHICLE_TAGS.PREMIUM in tags


def isPremiumIGR(tags):
    return VEHICLE_TAGS.PREMIUM_IGR in tags


def isBattleRoyaleTank(tags):
    return VEHICLE_TAGS.BATTLE_ROYALE in tags


def isEventBotVeh(tags):
    return b'wt_bot' in tags


class PlayerInfoVO(object):
    __slots__ = (b'accountDBID', b'avatarSessionID', b'name', b'fakeName', b'clanAbbrev', b'igrType', b'personaMissionIDs', b'personalMissionInfo', b'isPrebattleCreator', b'forbidInBattleInvitations', b'isTeamKiller', b'isEventBot')
    eventsCache = dependency.descriptor(IEventsCache)

    def __init__(self, accountDBID=0, avatarSessionID=b'', name=None, clanAbbrev=b'', igrType=IGR_TYPE.NONE, personalMissionIDs=None, personalMissionInfo=None, isPrebattleCreator=False, forbidInBattleInvitations=False, fakeName=b'', isEventBot=False, **kwargs):
        super(PlayerInfoVO, self).__init__()
        self.accountDBID = accountDBID
        self.avatarSessionID = avatarSessionID
        self.name = name
        self.fakeName = fakeName or b''
        self.clanAbbrev = clanAbbrev
        self.igrType = igrType
        self.personaMissionIDs = personalMissionIDs or []
        self.personalMissionInfo = personalMissionInfo or {}
        self.isPrebattleCreator = isPrebattleCreator
        self.forbidInBattleInvitations = forbidInBattleInvitations
        self.isTeamKiller = False
        self.isEventBot = isEventBot
        return

    def __cmp__(self, other):
        return cmp(self.name, other.name)

    def update(self, invalidate=_INVALIDATE_OP.NONE, name=None, accountDBID=0, avatarSessionID=b'', clanAbbrev=b'', isPrebattleCreator=False, igrType=IGR_TYPE.NONE, forbidInBattleInvitations=False, fakeName=b'', **kwargs):
        if name != self.name:
            self.name = name
            invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.SORTING)
        if fakeName and fakeName != self.fakeName:
            self.fakeName = fakeName
        self.accountDBID = accountDBID
        self.avatarSessionID = avatarSessionID
        self.clanAbbrev = clanAbbrev
        self.igrType = igrType
        self.isPrebattleCreator = isPrebattleCreator
        self.forbidInBattleInvitations = forbidInBattleInvitations
        return invalidate

    def getPlayerLabel(self):
        if self.isEventBot:
            return i18n.makeString(EVENT.PLAYERSPANEL_BOTNAME)
        if self.name:
            return self.name
        return i18n.makeString(settings.UNKNOWN_PLAYER_NAME)

    def getPlayerFakeLabel(self):
        return self.fakeName or b''

    def getRandomPersonalMissions(self):
        pmQuests = self.eventsCache.getPersonalMissions().getAllQuests()
        return self.__getPersonaMissionIDs(pmQuests)

    def __getPersonaMissionIDs(self, pmQuests):
        try:
            return [pmQuests[qID] for qID in self.personaMissionIDs]
        except KeyError as e:
            LOG_ERROR(b'Key error trying to get personal mission: no key in cache', e)
            return []

        return


class VehicleTypeInfoVO(object):
    __slots__ = (b'compactDescr', b'shortName', b'name', b'level', b'iconName', b'iconPath', b'isObserver', b'isPremiumIGR', b'isDualGunVehicle', b'isFlamethrowerVehicle', b'isAssaultVehicle', b'hasDualAccuracy', b'isAutoShootFlamethrowerVehicle', b'guiName', b'shortNameWithPrefix', b'classTag', b'nationID', b'turretYawLimits', b'maxHealth', b'strCompactDescr', b'isOnlyForBattleRoyaleBattles', b'tags', b'chassisType', b'role', b'isMultiTrack', b'hasThermalVision', b'hasDistanceFactorShells', b'isAutoShootGunVehicle', b'isEventBot')

    def __init__(self, vehicleType=None, maxHealth=None, **kwargs):
        super(VehicleTypeInfoVO, self).__init__()
        self.__setVehicleData(vehicleType, maxHealth)
        return

    def __repr__(self):
        return (b'VehicleTypeInfoVO(compactDescr = {0:n})').format(self.compactDescr)

    def __cmp__(self, other):
        result = cmp(other.level, self.level)
        if result:
            return result
        result = cmp(self.getOrderByClass(), other.getOrderByClass())
        if result:
            return result
        return cmp(self.shortName, other.shortName)

    def update(self, invalidate=_INVALIDATE_OP.NONE, vehicleType=None, maxHealth=None, **kwargs):
        if vehicleType is not None:
            if self.compactDescr != vehicleType.type.compactDescr:
                self.__setVehicleData(vehicleType, maxHealth)
                invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.SORTING)
            else:
                newStrCD = vehicleType.makeCompactDescr()
                if self.strCompactDescr != newStrCD or self.maxHealth != maxHealth:
                    self.__setVehicleData(vehicleType, maxHealth)
                    invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.SORTING)
        return invalidate

    def __setVehicleData(self, vehicleDescr=None, maxHealth=None):
        if vehicleDescr is not None:
            vehicleType = vehicleDescr.type
            self.compactDescr = vehicleType.compactDescr
            self.strCompactDescr = vehicleDescr.makeCompactDescr()
            tags = vehicleType.tags
            self.tags = tags
            self.classTag = Vehicle.getVehicleClassTag(tags)
            self.isObserver = isObserver(tags)
            self.isPremiumIGR = isPremiumIGR(tags)
            self.turretYawLimits = vehicle_getter.getYawLimits(vehicleDescr)
            self.isDualGunVehicle = vehicleDescr.isDualgunVehicle
            self.isFlamethrowerVehicle = vehicleDescr.isFlamethrower
            self.isAutoShootGunVehicle = vehicleDescr.isAutoShootGunVehicle and not vehicleDescr.isAutoShootFlamethrower
            self.isAutoShootFlamethrowerVehicle = vehicleDescr.isAutoShootFlamethrower
            self.isAssaultVehicle = vehicleDescr.isAssaultSPG
            self.hasDualAccuracy = vehicleDescr.hasDualAccuracy
            self.hasThermalVision = vehicleDescr.hasThermalVision
            self.chassisType = vehicleDescr.chassis.chassisType
            self.isMultiTrack = vehicleDescr.isMultiTrack
            self.shortName = vehicleType.shortUserString
            self.name = Vehicle.getUserName(vehicleType=vehicleType, textPrefix=True)
            self.shortNameWithPrefix = Vehicle.getShortUserName(vehicleType=vehicleType, textPrefix=True)
            self.guiName = Vehicle.getShortUserName(vehicleType)
            self.nationID = vehicleType.id[0]
            self.level = vehicleType.level
            self.maxHealth = maxHealth
            self.isOnlyForBattleRoyaleBattles = isBattleRoyaleTank(tags)
            self.isEventBot = isEventBotVeh(tags)
            vName = vehicleType.name
            self.iconName = settings.makeVehicleIconName(vName)
            self.iconPath = settings.makeContourIconSFPath(vName)
            self.role = vehicleType.role
            self.hasDistanceFactorShells = bool(vehicleDescr.shot.shell.distanceFactor)
        else:
            vehicleName = i18n.makeString(settings.UNKNOWN_VEHICLE_NAME)
            self.tags = frozenset()
            self.compactDescr = 0
            self.strCompactDescr = b''
            self.classTag = None
            self.isObserver = False
            self.isPremiumIGR = False
            self.turretYawLimits = None
            self.shortName = vehicleName
            self.isDualGunVehicle = False
            self.isFlamethrowerVehicle = False
            self.isAutoShootFlamethrowerVehicle = False
            self.isAutoShootGunVehicle = False
            self.isAssaultVehicle = False
            self.hasDualAccuracy = False
            self.hasThermalVision = False
            self.chassisType = None
            self.isMultiTrack = False
            self.name = vehicleName
            self.guiName = vehicleName
            self.shortNameWithPrefix = vehicleName
            self.nationID = nations.NONE_INDEX
            self.level = settings.UNKNOWN_VEHICLE_LEVEL
            self.iconName = settings.UNKNOWN_CONTOUR_ICON_NAME
            self.iconPath = settings.UNKNOWN_CONTOUR_ICON_SF_PATH
            self.shortNameWithPrefix = vehicleName
            self.maxHealth = None
            self.isOnlyForBattleRoyaleBattles = False
            self.role = ROLE_TYPE.NOT_DEFINED
            self.hasDistanceFactorShells = False
            self.isEventBot = False
        return

    def getClassName(self):
        if self.classTag is not None:
            return self.classTag
        else:
            return settings.UNKNOWN_VEHICLE_CLASS_NAME

    def getOrderByClass(self):
        return settings.getOrderByVehicleClass(self.classTag)


class VehicleArenaInfoVO(object):
    __slots__ = (b'vehicleID', b'team', b'player', b'playerStatus', b'vehicleType', b'vehicleStatus', b'prebattleID', b'events', b'squadIndex', b'invitationDeliveryStatus', b'ranked', b'gameModeSpecific', b'overriddenBadge', b'badges', b'__prefixBadge', b'__suffixBadge', b'dogTag', b'selectedComp7Skill')

    def __init__(self, vehicleID, team=0, isAlive=None, isAvatarReady=None, isTeamKiller=None, prebattleID=None, events=None, forbidInBattleInvitations=False, ranked=None, badges=None, overriddenBadge=None, selectedComp7Skill=0, **kwargs):
        super(VehicleArenaInfoVO, self).__init__()
        self.vehicleID = vehicleID
        self.team = team
        self.player = PlayerInfoVO(forbidInBattleInvitations=forbidInBattleInvitations, **kwargs)
        self.vehicleType = VehicleTypeInfoVO(**kwargs)
        self.prebattleID = prebattleID
        self.vehicleStatus = self.__getVehicleStatus(isAlive, isAvatarReady)
        self.playerStatus = self.__getPlayerStatus(isTeamKiller)
        self.invitationDeliveryStatus = self.__getInvitationStatus(forbidInBattleInvitations)
        self.events = events or {}
        self.squadIndex = 0
        self.ranked = PlayerRankedInfoVO(ranked) if ranked is not None else PlayerRankedInfoVO()
        self.selectedComp7Skill = selectedComp7Skill
        arena = avatar_getter.getArena()
        guiType = None if not arena else arena.guiType
        self.gameModeSpecific = GameModeDataVO(guiType, True)
        self.overriddenBadge = overriddenBadge
        self.badges = badges or ((), ())
        self.__prefixBadge, self.__suffixBadge = getSelectedByLayout(self.badges[0])
        self.dogTag = None
        if self.vehicleType.isEventBot:
            self.player.isEventBot = True
            self.gameModeSpecific.update({(EventKeys.CAMP.value): (self.player.name)})
        return

    def __repr__(self):
        return (b'VehicleArenaInfoVO(vehicleID = {0!r:s}, team = {1!r:s}, player = {2!r:s}, playerStatus = {3:n}, vehicleType = {4!r:s}, vehicleStatus = {5:n}, prebattleID = {6!r:s}), dogTag={7!r:s}').format(self.vehicleID, self.team, self.player, self.playerStatus, self.vehicleType, self.vehicleStatus, self.prebattleID, self.dogTag)

    def __eq__(self, other):
        return self.vehicleID == other.vehicleID

    def __cmp__(self, other):
        result = cmp(self.team, other.team)
        if result:
            return result
        result = cmp(other.isAlive(), self.isAlive())
        if result:
            return result
        result = cmp(self.vehicleType, other.vehicleType)
        if result:
            return result
        return cmp(self.player, other.player)

    @property
    def selectedBadge(self):
        return self.__prefixBadge

    @property
    def selectedSuffixBadge(self):
        return self.__suffixBadge

    def getBadgeExtraInfo(self):
        if self.badges:
            _, extraInfo = self.badges
            return extraInfo
        else:
            return

    def updateVehicleStatus(self, invalidate=_INVALIDATE_OP.NONE, isAlive=None, isAvatarReady=None, stopRespawn=False, **kwargs):
        prev, self.vehicleStatus = self.vehicleStatus, self.__getVehicleStatus(isAlive, isAvatarReady, stopRespawn)
        diff = self.vehicleStatus ^ prev
        if diff:
            invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.VEHICLE_STATUS)
            if diff & _VEHICLE_STATUS.IS_ALIVE > 0 or diff & _VEHICLE_STATUS.STOP_RESPAWN > 0:
                invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.SORTING)
        invalidate = self.updateEvents(invalidate=invalidate, **kwargs)
        return invalidate

    def updatePlayerStatus(self, invalidate=_INVALIDATE_OP.NONE, isTeamKiller=None, isSquadMan=None, **kwargs):
        if isTeamKiller:
            status = _PLAYER_STATUS.addIfNot(self.playerStatus, _PLAYER_STATUS.IS_TEAM_KILLER)
            if self.playerStatus ^ status:
                self.playerStatus = status
                invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.PLAYER_STATUS)
        elif isTeamKiller is not None and not isTeamKiller:
            status = _PLAYER_STATUS.removeIfHas(self.playerStatus, _PLAYER_STATUS.IS_TEAM_KILLER)
            if self.playerStatus ^ status:
                self.playerStatus = status
                invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.PLAYER_STATUS)
        if isSquadMan:
            status = _PLAYER_STATUS.addIfNot(self.playerStatus, _PLAYER_STATUS.IS_SQUAD_MAN)
            if self.playerStatus ^ status:
                self.playerStatus = status
                invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.PLAYER_STATUS)
        return invalidate

    def updateInvitationStatus(self, invalidate=_INVALIDATE_OP.NONE, include=_DELIVERY_STATUS.NONE, exclude=_DELIVERY_STATUS.NONE, forbidInBattleInvitations=False, **kwargs):
        status = self.invitationDeliveryStatus
        if forbidInBattleInvitations:
            status = _DELIVERY_STATUS.addIfNot(status, _DELIVERY_STATUS.FORBIDDEN_BY_RECEIVER)
        status = _DELIVERY_STATUS.addIfNot(status, include)
        status = _DELIVERY_STATUS.removeIfHas(status, exclude)
        if self.invitationDeliveryStatus ^ status:
            self.invitationDeliveryStatus = status
            invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.INVITATION_DELIVERY_STATUS)
        return invalidate

    def updateRanked(self, invalidate=_INVALIDATE_OP.NONE, ranked=None, **kwargs):
        if ranked is not None:
            self.ranked = PlayerRankedInfoVO(ranked)
            invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.VEHICLE_INFO)
        return invalidate

    def updateEvents(self, invalidate=_INVALIDATE_OP.NONE, events=None, **kwargs):
        if events is not None:
            self.events.update(events)
            invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.VEHICLE_INFO)
        return invalidate

    def updateGameModeSpecificStats(self, *args):
        return self.gameModeSpecific.update(*args)

    def updateVehicleDogTag(self, invalidate=_INVALIDATE_OP.NONE, dogTag=None, **kwargs):
        if dogTag:
            self.dogTag = layoutComposer.getModelFromDict(dogTag)
            invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.VEHICLE_STATUS)
        return invalidate

    def update(self, **kwargs):
        invalidate = _INVALIDATE_OP.VEHICLE_INFO
        newPrbID = kwargs.get(b'prebattleID', 0)
        if self.prebattleID != newPrbID:
            self.prebattleID = newPrbID
            invalidate = _INVALIDATE_OP.addIfNot(invalidate, _INVALIDATE_OP.PREBATTLE_CHANGED)
        invalidate = self.player.update(invalidate=invalidate, **kwargs)
        invalidate = self.vehicleType.update(invalidate=invalidate, **kwargs)
        invalidate = self.updateVehicleStatus(invalidate=invalidate, **kwargs)
        invalidate = self.updatePlayerStatus(invalidate=invalidate, **kwargs)
        invalidate = self.updateInvitationStatus(invalidate=invalidate, **kwargs)
        invalidate = self.updateRanked(invalidate=invalidate, **kwargs)
        invalidate = self.updateEvents(invalidate=invalidate, **kwargs)
        return invalidate

    def getSquadID(self):
        if self.isSquadMan():
            return self.prebattleID
        return 0

    def isSquadMan(self, prebattleID=None, playerTeam=None):
        if playerTeam and self.team != playerTeam:
            return False
        else:
            if prebattleID is not None and self.prebattleID != prebattleID:
                return False
            return self.playerStatus & _PLAYER_STATUS.IS_SQUAD_MAN > 0

    def isSquadCreator(self):
        return self.player.isPrebattleCreator and self.isSquadMan()

    def isTeamKiller(self, playerTeam=None):
        if self.vehicleID == avatar_getter.getPlayerVehicleID() and avatar_getter.isPlayerTeamKillSuspected():
            return True
        return self.playerStatus & _PLAYER_STATUS.IS_TEAM_KILLER > 0

    def getPlayerStatusInTeam(self, playerTeam=None):
        playerStatus = 0
        if self.isSquadMan():
            playerStatus |= _PLAYER_STATUS.IS_SQUAD_MAN
        if self.isTeamKiller(playerTeam=playerTeam):
            playerStatus |= _PLAYER_STATUS.IS_TEAM_KILLER
        return playerStatus

    def isAlive(self):
        return self.vehicleStatus & _VEHICLE_STATUS.IS_ALIVE > 0

    def isReady(self):
        return self.vehicleStatus & _VEHICLE_STATUS.IS_READY > 0

    def isObserver(self):
        if self.vehicleType.isObserver:
            return True
        if self.vehicleID == avatar_getter.getPlayerVehicleID() and not self.isAlive():
            return avatar_getter.isBecomeObserverAfterDeath() and avatar_getter.isObserverBothTeams()
        return False

    def isEnemy(self):
        return self.team != avatar_getter.getPlayerTeam()

    def isSPG(self):
        return self.vehicleType.classTag == VEHICLE_CLASS_NAME.SPG

    def isDualGunVehicle(self):
        return self.vehicleType.isDualGunVehicle

    def isFlamethrowerVehicle(self):
        return self.vehicleType.isFlamethrowerVehicle

    def isAutoShootFlamethrowerVehicle(self):
        return self.vehicleType.isAutoShootFlamethrowerVehicle

    def isAssaultVehicle(self):
        return self.vehicleType.isAssaultVehicle

    def isActionsDisabled(self):
        return not self.player.avatarSessionID

    def isPlayer(self):
        return not self.isObserver() and bool(self.player.avatarSessionID)

    def isPlayerVehicle(self):
        return self.vehicleID == avatar_getter.getPlayerVehicleID()

    def isChatCommandsDisabled(self, isAlly):
        arena = avatar_getter.getArena()
        isEvent = arena.guiType in (ARENA_GUI_TYPE.EVENT_BATTLES, ARENA_GUI_TYPE.WHITE_TIGER) if arena else False
        if not (self.player.avatarSessionID or isEvent):
            if isAlly:
                return True
            if arena is None or arena.guiType not in (ARENA_GUI_TYPE.RANDOM, ARENA_GUI_TYPE.TRAINING,
             ARENA_GUI_TYPE.EPIC_BATTLE, ARENA_GUI_TYPE.EPIC_TRAINING,
             ARENA_GUI_TYPE.VERSUS_AI):
                return True
        return False

    def hasDualAccuracy(self):
        return self.vehicleType.hasDualAccuracy

    def hasThermalVision(self):
        return self.vehicleType.hasThermalVision

    def getTypeInfo(self):
        return (
         self.vehicleType.classTag, self.vehicleType.level,
         nations.NAMES[self.vehicleType.nationID])

    def getIGRLabel(self):
        if self.vehicleType.isPremiumIGR:
            if self.player.igrType == IGR_TYPE.PREMIUM:
                key = b'premium'
            else:
                key = b'basic'
            igrLabel = makeHtmlString(b'html_templates:igr/iconBig', key)
        else:
            igrLabel = b''
        return igrLabel

    @staticmethod
    def __getVehicleStatus(isAlive=None, isAvatarReady=None, stopRespawn=False):
        vehicleStatus = _VEHICLE_STATUS.DEFAULT
        if isAlive:
            vehicleStatus |= _VEHICLE_STATUS.IS_ALIVE
        if isAvatarReady:
            vehicleStatus |= _VEHICLE_STATUS.IS_READY
        if isAlive is None or isAvatarReady is None:
            vehicleStatus = _VEHICLE_STATUS.NOT_AVAILABLE
        if stopRespawn:
            vehicleStatus |= _VEHICLE_STATUS.STOP_RESPAWN
        return vehicleStatus

    def __getPlayerStatus(self, isTeamKiller=None):
        playerStatus = _PLAYER_STATUS.DEFAULT
        if isTeamKiller:
            playerStatus |= _PLAYER_STATUS.IS_TEAM_KILLER
        if self.isActionsDisabled():
            playerStatus |= _PLAYER_STATUS.IS_ACTION_DISABLED
        return playerStatus

    @staticmethod
    def __getInvitationStatus(forbidInBattleInvitations=False):
        invitationStatus = _DELIVERY_STATUS.NONE
        if forbidInBattleInvitations:
            invitationStatus = _DELIVERY_STATUS.FORBIDDEN_BY_RECEIVER
        return invitationStatus


class VehicleArenaInteractiveStatsVO(object):
    __slots__ = (b'xp', b'damageDealt', b'capturePts', b'flagActions', b'winPoints', b'deathCount', b'resourceAbsorbed', b'stopRespawn', b'equipmentDamage', b'equipmentKills', b'teamWinPoints', b'team')

    def __init__(self, xp=0, damageDealt=0, capturePts=0, flagActions=None, winPoints=0, deathCount=0, resourceAbsorbed=0, stopRespawn=False, equipmentDamage=0, equipmentKills=0, *args):
        super(VehicleArenaInteractiveStatsVO, self).__init__()
        self.xp = xp
        self.damageDealt = damageDealt
        self.capturePts = capturePts
        self.flagActions = flagActions or (0,) * len(FLAG_ACTION.RANGE)
        self.winPoints = winPoints
        self.deathCount = deathCount
        self.resourceAbsorbed = resourceAbsorbed
        self.stopRespawn = stopRespawn
        self.equipmentDamage = equipmentDamage
        self.equipmentKills = equipmentKills
        self.teamWinPoints = 0
        return

    def clear(self):
        self.xp = 0
        self.damageDealt = 0
        self.capturePts = 0
        self.flagActions = (0,) * len(FLAG_ACTION.RANGE)
        self.winPoints = 0
        self.deathCount = 0
        self.resourceAbsorbed = 0
        self.stopRespawn = False
        self.equipmentDamage = 0
        self.equipmentKills = 0
        self.teamWinPoints = 0
        return

    def update(self, xp=0, damageDealt=0, capturePts=0, flagActions=None, winPoints=0, deathCount=0, resourceAbsorbed=0, stopRespawn=False, equipmentDamage=0, equipmentKills=0, *args):
        result = _INVALIDATE_OP.VEHICLE_ISTATS
        self.xp += xp
        self.damageDealt += damageDealt
        self.capturePts += capturePts
        if flagActions is not None:
            self.flagActions = map(operator.add, self.flagActions, flagActions)
        if winPoints:
            result |= _INVALIDATE_OP.SORTING
        self.winPoints += winPoints
        self.deathCount += deathCount
        self.resourceAbsorbed += resourceAbsorbed
        self.stopRespawn = self.stopRespawn or stopRespawn
        self.equipmentDamage += equipmentDamage
        self.equipmentKills += equipmentKills
        return result

    def getCapturedFlags(self):
        return self.flagActions[FLAG_ACTION.CAPTURED]

    def getTotalDamage(self):
        return self.damageDealt + self.equipmentDamage


class VehicleArenaStatsVO(object):
    __slots__ = (b'vehicleID', b'__frags', b'__interactive', b'__gameModeSpecific', b'__chatCommand', b'__spottedStatus')

    def __init__(self, vehicleID, frags=0, **kwargs):
        super(VehicleArenaStatsVO, self).__init__()
        self.vehicleID = vehicleID
        self.__frags = frags
        self.__chatCommand = ChatCommandVO()
        self.__spottedStatus = VehicleSpottedStatus.DEFAULT
        self.__interactive = None
        self.__gameModeSpecific = None
        return

    def __repr__(self):
        return (b'VehicleArenaStatsVO(vehicleID = {}, frags = {}, interactive = {})').format(self.vehicleID, self.__frags, self.__interactive)

    @property
    def frags(self):
        if self.__interactive is not None:
            return self.__frags + self.__interactive.equipmentKills
        else:
            return self.__frags

    @property
    def interactive(self):
        if self.__interactive is None:
            self.__interactive = VehicleArenaInteractiveStatsVO()
        return self.__interactive

    @property
    def gameModeSpecific(self):
        if self.__gameModeSpecific is None:
            arena = avatar_getter.getArena()
            guiType = None if not arena else arena.guiType
            self.__gameModeSpecific = GameModeDataVO(guiType, False)
        return self.__gameModeSpecific

    @property
    def stopRespawn(self):
        if self.__interactive is not None:
            return self.__interactive.stopRespawn
        else:
            return False

    @property
    def winPoints(self):
        if self.__interactive is not None:
            return self.__interactive.winPoints
        else:
            return 0

    @property
    def chatCommandState(self):
        return self.__chatCommand

    @property
    def spottedStatus(self):
        return self.__spottedStatus

    def clearInteractiveStats(self):
        if self.__interactive is not None:
            self.__interactive.clear()
        return

    def clearGameModeSpecificStats(self):
        if self.__gameModeSpecific is not None:
            self.__gameModeSpecific.clear()
        return

    def updateInteractiveStats(self, *args):
        if self.__interactive is None:
            self.__interactive = VehicleArenaInteractiveStatsVO()
        return self.__interactive.update(*args)

    def updateGameModeSpecificStats(self, *args):
        if self.__gameModeSpecific is None:
            arena = avatar_getter.getArena()
            guiType = None if not arena else arena.guiType
            self.__gameModeSpecific = GameModeDataVO(guiType, False)
        return self.__gameModeSpecific.update(*args)

    def updateChatCommandState(self, chatCommandState):
        chatCmd, chatCommandFlags = chatCommandState
        if chatCmd == self.__chatCommand.activeChatCommand and chatCommandFlags == self.__chatCommand.chatCommandFlags:
            return _INVALIDATE_OP.NONE
        self.__chatCommand = ChatCommandVO(chatCmd=chatCmd, chatCommandFlags=chatCommandFlags)
        return _INVALIDATE_OP.VEHICLE_STATS

    def updateSpottedStatus(self, spottedStatus):
        if self.__spottedStatus == spottedStatus or self.__spottedStatus == VehicleSpottedStatus.DEFAULT and spottedStatus == VehicleSpottedStatus.UNSPOTTED:
            return _INVALIDATE_OP.NONE
        self.__spottedStatus = spottedStatus
        return _INVALIDATE_OP.VEHICLE_STATS

    def updateVehicleStats(self, frags=None, **kwargs):
        if frags is not None:
            self.__frags = frags
            return _INVALIDATE_OP.VEHICLE_STATS
        else:
            return _INVALIDATE_OP.NONE


class PlayerRankedInfoVO(object):
    __slots__ = (b'rank', b'rankStep')

    def __init__(self, rank=None):
        super(PlayerRankedInfoVO, self).__init__()
        self.rank, self.rankStep = rank or (0, 0)
        return


class ChatCommandVO(object):
    __slots__ = (b'activeChatCommand', b'chatCommandFlags')

    def __init__(self, chatCmd=b'', chatCommandFlags=0):
        super(ChatCommandVO, self).__init__()
        self.activeChatCommand, self.chatCommandFlags = chatCmd, chatCommandFlags
        return


class VehicleArenaStatsDict(defaultdict):

    def __missing__(self, key):
        self[key] = value = VehicleArenaStatsVO(key)
        return value

    def clearInteractiveStats(self):
        for vo in self.itervalues():
            vo.clearInteractiveStats()

        return


class VehicleActions(object):
    __ACTIONS = {b'hunting': 1}

    @staticmethod
    def getBitMask(actions):
        bitMask = 0
        for key, value in actions.items():
            mask = VehicleActions.__ACTIONS.get(key, 0)
            if isinstance(mask, dict):
                mask = mask.get(value, 0)
            bitMask |= mask

        return bitMask

    @staticmethod
    def isHunting(actions):
        return b'hunting' in actions.keys()
