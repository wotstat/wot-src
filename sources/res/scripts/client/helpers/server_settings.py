import copy, functools, logging, types
from collections import namedtuple
from itertools import chain
import typing
from shared_utils import makeTupleByDict, updateDict
import constants, post_progression_common
from BonusCaps import BonusCapsConst
from Event import Event
from UnitBase import PREBATTLE_TYPE_TO_UNIT_ASSEMBLER, UNIT_ASSEMBLER_IMPL_TO_CONFIG
from achievements20.Achievements20GeneralConfig import Achievements20GeneralConfig
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from battle_modifiers_common import BattleModifiers, BattleParams, ModifiersContext
from battle_pass_common import BATTLE_PASS_CONFIG_NAME, BattlePassConfig
from collections_common import CollectionsConfig
from collector_vehicle import CollectorVehicleConsts
from constants import BATTLE_NOTIFIER_CONFIG, DAILY_QUESTS_CONFIG, DOG_TAGS_CONFIG, MAGNETIC_AUTO_AIM_CONFIG, MISC_GUI_SETTINGS, OPTIONAL_DEVICES_USAGE_CONFIG, PLAYER_SUBSCRIPTIONS_CONFIG, TOURNAMENT_CONFIG, ClansConfig, Configs, PremiumConfigs
from challenges_common import ChallengesConfig
from debug_utils import LOG_DEBUG, LOG_NOTE
from gifts.gifts_common import ClientReqStrategy, GiftEventID, GiftEventState
from gui import GUI_SETTINGS, SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.SystemMessages import SM_TYPE
from gui.limited_ui.lui_rules_storage import LuiRuleTypes
from gui.shared.utils.decorators import ReprInjector
from helpers import time_utils
from items import vehicles
from personal_missions import PM_BRANCH
from pet_system_common import pet_constants
from pet_system_common.BonusConfig import BonusConfig as PetBonusConfig
from pet_system_common.EventConfig import EventConfig as PetEventConfig
from pet_system_common.GeneralConfig import GeneralConfig as PetGeneralConfig
from pet_system_common.PetConfig import PetConfig
from pet_system_common.PetPromoConfig import PetPromoConfig
from pet_system_common.PetSynergyConfig import PetSynergyConfig
from pet_system_common.pet_constants import PETS_SYSTEM_CONFIG
from post_progression_common import FEATURE_BY_GROUP_ID, ROLESLOT_FEATURE
from prestige_system.prestige_common import PrestigeConfig
from prestige_system.prestige_milestones_common import PrestigeMilestonesConfig
from ranked_common import SwitchState
from schema_manager import getSchemaManager
from soft_exception import SoftException
from telecom_rentals_common import TELECOM_RENTALS_CONFIG
from trade_in_common.constants_types import CONFIG_NAME as TRADE_IN_CONFIG_NAME
from helpers.ingame_tournament_helper import IngameTournamentType
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, List, Sequence
    from dict2model.schemas import SchemaModelType
    from game_params_common.schema import GameParamsSchema
_logger = logging.getLogger(__name__)
_CLAN_EMBLEMS_SIZE_MAPPING = {16: b'clan_emblems_16', 
   32: b'clan_emblems_small', 
   64: b'clan_emblems_big', 
   128: b'clan_emblems_128', 
   256: b'clan_emblems_256'}

@ReprInjector.simple((
 b'centerID', b'centerID'), (b'dbidMin', b'dbidMin'), (
 b'dbidMax', b'dbidMax'), (b'regionCode', b'regionCode'))
class _ServerInfo(object):
    __slots__ = (b'centerID', b'dbidMin', b'dbidMax', b'regionCode')

    def __init__(self, centerID, dbidMin, dbidMax, regionCode):
        self.centerID = centerID
        self.dbidMin = dbidMin
        self.dbidMax = dbidMax
        self.regionCode = regionCode
        return

    def isPlayerHome(self, playerDBID):
        return self.dbidMin <= playerDBID <= self.dbidMax


class RoamingSettings(namedtuple(b'RoamingSettings', (b'homeCenterID', b'curCenterID', b'servers'))):
    __slots__ = ()

    def getHomeCenterID(self):
        return self.homeCenterID

    def getCurrentCenterID(self):
        return self.curCenterID

    def getRoamingServers(self):
        return self.servers

    def getPlayerHome(self, playerDBID):
        for s in self.getRoamingServers():
            if s.isPlayerHome(playerDBID):
                return (s.centerID, s.regionCode)

        return (None, None)

    def isEnabled(self):
        return GUI_SETTINGS.roaming

    def isSameRealm(self, playerDBID):
        centerID, _ = self.getPlayerHome(playerDBID)
        return centerID == self.getHomeCenterID()

    def isInRoaming(self):
        return self.getCurrentCenterID() != self.getHomeCenterID()

    def isPlayerInRoaming(self, playerDBID):
        centerID, _ = self.getPlayerHome(playerDBID)
        return centerID != self.getCurrentCenterID()

    @classmethod
    def defaults(cls):
        dbIDMin = 0
        dbIDMax = 9223372036854775807L
        regionCode = None
        homeCenterID = 0
        currentCenterID = 0
        return cls(homeCenterID, currentCenterID, [
         _ServerInfo(currentCenterID, dbIDMin, dbIDMax, regionCode)])


class _FileServerSettings(object):

    def __init__(self, fsSettings):
        self.__urls = dict((n, d.get(b'url_template', b'')) for n, d in fsSettings.iteritems())
        return

    def getUrls(self):
        return self.__urls

    def getClanEmblemBySize(self, clanDBID, size):
        return self.__getUrl(_CLAN_EMBLEMS_SIZE_MAPPING[size], clanDBID)

    def getClanEmblem64x64VehicleUrl(self, clanDBID):
        return self.__getUrl(b'clan_emblems', clanDBID)

    def getRareAchievement67x71Url(self, rareAchieveID):
        return self.__getUrl(b'rare_achievements_images', rareAchieveID)

    def getRareAchievement128x128Url(self, rareAchieveID):
        return self.__getUrl(b'rare_achievements_images_big', rareAchieveID)

    def getRareAchievementTextsUrl(self, langID):
        return self.__getUrl(b'rare_achievements_texts', langID)

    def getMissionsTokenImageUrl(self, tokenID, size):
        return self.__getUrl(b'missions_token_image', size, tokenID)

    def getMissionsTokenDescrsUrl(self, langID):
        if isinstance(langID, unicode):
            langID = str(langID)
        return self.__getUrl(b'missions_token_descrs', langID)

    def getMissionsDecorationUrl(self, decorationID, size):
        return self.__getUrl(b'missions_decoration', size, decorationID)

    def getOffersRootUrl(self):
        return self.__getUrl(b'offers')

    def getGameLoadingConfigUrl(self):
        return self.__getUrl(b'game_loading_config')

    def getServiceRecordCustomizationRootUrl(self):
        return self.__getUrl(b'service_record_customization')

    def getCollectionsContentConfigUrl(self):
        return self.__getUrl(b'collections_content_config')

    def __getUrl(self, urlKey, *args):
        try:
            return self.__urls[urlKey] % args
        except (KeyError, TypeError):
            LOG_NOTE(b'There is invalid url while getting emblem from web', urlKey, args)

        return

    @classmethod
    def defaults(cls):
        return cls({})


class _RegionalSettings(namedtuple(b'_RegionalSettings', (
 b'starting_day_of_a_new_week',
 b'starting_time_of_a_new_day',
 b'starting_time_of_a_new_game_day'))):
    __slots__ = ()

    def getWeekStartingDay(self):
        return self.starting_day_of_a_new_week

    def getDayStartingTime(self):
        return self.starting_time_of_a_new_day

    def getGameDayStartingTime(self):
        return self.starting_time_of_a_new_game_day

    @classmethod
    def defaults(cls):
        return cls(0, 0, 3)


class _ESportCurrentSeason(namedtuple(b'_ESportSeason', (
 b'eSportSeasonID',
 b'eSportSeasonStart',
 b'eSportSeasonFinish'))):
    __slots__ = ()

    def getID(self):
        return self.eSportSeasonID

    def getStartTime(self):
        return self.eSportSeasonStart

    def getFinishTime(self):
        return self.eSportSeasonFinish

    @classmethod
    def defaults(cls):
        return cls(0, 0, 0)


class _Wgcg(namedtuple(b'_Wgcg', (b'enabled', b'url', b'type', b'loginOnStart', b'isJwtAuthorizationEnabled'))):
    __slots__ = ()

    def isEnabled(self):
        return self.enabled

    def getAccessorType(self):
        return self.type

    def getGateUrl(self):
        return self.url

    def getLoginOnStart(self):
        return self.loginOnStart

    def isJwtEnabled(self):
        return self.isJwtAuthorizationEnabled

    @classmethod
    def defaults(cls):
        return cls(False, b'', b'', False, False)


class _Wgnp(namedtuple(b'_Wgnp', (b'enabled', b'url', b'renameApiEnabled'))):
    __slots__ = ()

    def isEnabled(self):
        return self.enabled

    def getUrl(self):
        return self.url

    def isRenameApiEnabled(self):
        return self.enabled and self.renameApiEnabled

    @classmethod
    def defaults(cls):
        return cls(False, b'', False)


class _UILogging(namedtuple(b'_UILogging', (b'enabled',))):
    __slots__ = ()

    def isEnabled(self):
        return self.enabled

    @classmethod
    def defaults(cls):
        return cls(False)


class _EULA(namedtuple(b'_EULA', (b'enabled', b'demoAccEnabled', b'steamAccEnabled'))):
    __slots__ = ()

    def isEnabled(self):
        return self.enabled

    def isDemoAccEnabled(self):
        return self.enabled and self.demoAccEnabled

    def isSteamAccEnabled(self):
        return self.enabled and self.steamAccEnabled

    @classmethod
    def defaults(cls):
        return cls(False, False, False)


class _ClanProfile(namedtuple(b'_ClanProfile', (b'enabled',))):
    __slots__ = ()

    def isEnabled(self):
        return self.enabled

    @classmethod
    def defaults(cls):
        return cls(False)


class _StrongholdSettings(namedtuple(b'_StrongholdSettings', (b'wgshHostUrl',))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return cls(b'')


class _TournamentSettings(namedtuple(b'_TournamentSettings', (
 b'isExternalBattleEnabled',
 b'isTournamentEnabled',
 b'igbHostUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isExternalBattleEnabled=False, isTournamentEnabled=False, igbHostUrl=b'')
        defaults.update(**kwargs)
        return super(_TournamentSettings, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class _FrontlineSettings(namedtuple(b'_FrontlineSettings', (
 b'isEpicTrainingEnabled',))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return cls(False)


class _SpgRedesignFeatures(namedtuple(b'_SpgRedesignFeatures', (
 b'stunEnabled',
 b'markTargetAreaEnabled'))):
    __slots__ = ()

    def isStunEnabled(self):
        return self.stunEnabled

    @classmethod
    def defaults(cls):
        return cls(False, False)


class _BwHallOfFame(namedtuple(b'_BwHallOfFame', (b'hofHostUrl', b'isHofEnabled', b'isStatusEnabled'))):
    __slots__ = ()

    def __new__(cls, hofHostUrl=None, isHofEnabled=False, isStatusEnabled=False):
        return super(_BwHallOfFame, cls).__new__(cls, hofHostUrl, isHofEnabled, isStatusEnabled)

    @classmethod
    def defaults(cls):
        return cls()


class _BwShop(namedtuple(b'_BwShop', (
 b'hostUrl', b'isStorageEnabled'))):

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


_BwShop.__new__.__defaults__ = (
 b'', b'', False)

class _BwProductCatalog(namedtuple(b'_BwProductCatalog', (b'url',))):

    @classmethod
    def defaults(cls):
        return cls(b'')


_BwProductCatalog.__new__.__defaults__ = (
 b'',)

class RankedBattlesConfig(namedtuple(b'RankedBattlesConfig', (b'isEnabled', b'peripheryIDs', b'winnerRankChanges', b'loserRankChanges', b'minXP',
 b'unburnableRanks', b'unburnableStepRanks', b'minLevel', b'maxLevel', b'accRanks',
 b'accSteps', b'cycleFinishSeconds', b'primeTimes', b'seasons', b'cycleTimes', b'shields',
 b'divisions', b'bonusBattlesMultiplier', b'expectedSeasons', b'yearAwardsMarks',
 b'rankGroups', b'qualificationBattles', b'yearLBSize', b'leaguesBonusBattles',
 b'forbiddenClassTags', b'forbiddenVehTypes', b'shopState', b'yearLBState',
 b'yearRewardState', b'seasonRatingPageUrl', b'yearRatingPageUrl', b'infoPageUrl',
 b'introPageUrl', b'seasonGapPageUrl', b'shopPageUrl', b'hasSpecialSeason'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs={}, winnerRankChanges=(), loserRankChanges=(), minXP=0, unburnableRanks={}, unburnableStepRanks={}, minLevel=0, maxLevel=0, accRanks=0, accSteps=(), cycleFinishSeconds=0, primeTimes={}, seasons={}, cycleTimes=(), shields={}, divisions={}, bonusBattlesMultiplier=0, expectedSeasons=0, yearAwardsMarks=(), rankGroups=(), qualificationBattles=0, yearLBSize=0, leaguesBonusBattles=(), forbiddenClassTags=(), forbiddenVehTypes=(), shopState=SwitchState.DISABLED, yearLBState=SwitchState.DISABLED, yearRewardState=SwitchState.ENABLED, seasonRatingPageUrl=b'', yearRatingPageUrl=b'', infoPageUrl=b'', introPageUrl=b'', seasonGapPageUrl=b'', shopPageUrl=b'', hasSpecialSeason=False)
        defaults.update(kwargs)
        return super(RankedBattlesConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _ProgressiveReward(namedtuple(b'_ProgressiveReward', (
 b'isEnabled', b'levelTokenID', b'probabilityTokenID', b'maxLevel'))):

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


_ProgressiveReward.__new__.__defaults__ = (
 True, b'pr:level', b'pr:probability', 0)

class _EpicMetaGameConfig(namedtuple(b'_EpicMetaGameConfig', [171, 172, 173, 174, 175, 176, 
 177, 178, 179, 
 180])):

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


_EpicMetaGameConfig.__new__.__defaults__ = (
 0, (0, False), (0, 0, 0), {}, {}, {}, {}, 0, 0, {})

class EpicGameConfig(namedtuple(b'EpicGameConfig', (b'isEnabled', b'enableWelcomeScreen', b'validVehicleLevels', b'battlePassDataEnabled',
 b'levelsToUpgrateAllReserves', b'seasons', b'cycleTimes', b'unlockableInBattleVehLevels',
 b'inBattleModifiers', b'peripheryIDs', b'primeTimes', b'rentVehicles', b'tooltips',
 b'reservesModifiers', b'squadRestrictions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, enableWelcomeScreen=True, validVehicleLevels=[], battlePassDataEnabled=True, levelsToUpgrateAllReserves=[], unlockableInBattleVehLevels=[], inBattleModifiers={}, seasons={}, cycleTimes=(), peripheryIDs={}, primeTimes={}, rentVehicles=[], tooltips={}, reservesModifiers=[], squadRestrictions={})
        defaults.update(kwargs)
        return super(EpicGameConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _UnitAssemblerConfig(namedtuple(b'_UnitAssemblerConfig', (b'configs',))):
    __slots__ = ()

    def asDict(self):
        return self._asdict().get(b'configs', {})

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @staticmethod
    def isPrebattleSupported(prebattleType):
        return prebattleType in PREBATTLE_TYPE_TO_UNIT_ASSEMBLER

    def getConfigOfQueue(self, prebattleType):
        if not self.isPrebattleSupported(prebattleType):
            return {}
        return self.asDict().get(UNIT_ASSEMBLER_IMPL_TO_CONFIG[PREBATTLE_TYPE_TO_UNIT_ASSEMBLER[prebattleType]], {})

    def isVoicePreferenceEnabled(self, prebattleType):
        return self.getConfigOfQueue(prebattleType).get(b'voiceChatPreferenceEnabled', False)

    def isTankLevelPreferenceEnabled(self, prebattleType):
        return self.getConfigOfQueue(prebattleType).get(b'tankLevelPreferenceEnabled', False)

    def getAllowedTankLevels(self, prebattleType):
        return self.getConfigOfQueue(prebattleType).get(b'allowedTankLevels', 0)

    def isAssemblingEnabled(self, prebattleType):
        return self.getConfigOfQueue(prebattleType).get(b'isAssemblingEnabled', False)

    def getExtendTierFilter(self, prebattleType):
        return self.getConfigOfQueue(prebattleType).get(b'extendTierFilter', [])

    @classmethod
    def defaults(cls):
        return cls(configs={})


class _SquadPremiumBonus(namedtuple(b'_SquadPremiumBonus', (b'isEnabled', b'ownCredits', b'mateCredits'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=True, ownCredits=0, mateCredits=0)
        defaults.update(kwargs)
        return super(_SquadPremiumBonus, cls).__new__(cls, **defaults)

    def replace(self, data):
        return self._replace(**self.__extractFields(data))

    @classmethod
    def create(cls, data):
        return cls(**cls.__extractFields(data))

    @classmethod
    def defaults(cls):
        return cls()

    @staticmethod
    def __extractFields(data):
        creditsSettings = data.get(b'creditsFactor', {})
        result = {}
        if b'enabled' in data:
            result[b'isEnabled'] = data[b'enabled']
        if b'premium_plus' in creditsSettings:
            result[b'ownCredits'] = creditsSettings[b'premium_plus']
        if b'premium_owner_squadmate' in creditsSettings:
            result[b'mateCredits'] = creditsSettings[b'premium_owner_squadmate']
        return result


class BattleRoyaleConfig(namedtuple(b'BattleRoyaleConfig', (b'isEnabled', b'isStPatrick', b'peripheryIDs', b'unburnableTitles',
 b'eventProgression', b'primeTimes', b'seasons', b'cycleTimes',
 b'maps', b'battleXP', b'coneVisibility', b'loot', b'defaultAmmo',
 b'vehiclesSlotsConfig', b'economics', b'url', b'respawns', b'progressionTokenAward',
 b'tournamentsWidget', b'coinAward', b'dailyBonus'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, isStPatrick=False, peripheryIDs={}, eventProgression={}, unburnableTitles=(), primeTimes={}, seasons={}, cycleTimes={}, maps=(), battleXP={}, coneVisibility={}, loot={}, defaultAmmo={}, vehiclesSlotsConfig={}, economics={}, url=b'', respawns={}, progressionTokenAward={}, tournamentsWidget={}, coinAward={}, dailyBonus={})
        defaults.update(kwargs)
        cls.__packStpCoinAwardConfig(defaults)
        return super(BattleRoyaleConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()

    @classmethod
    def __packStpCoinAwardConfig(cls, data):
        data[b'coinAward'] = {int(bonusType): value for bonusType, value in data[b'coinAward'].iteritems()}
        return


class _TelecomConfig(object):
    __slots__ = (b'__bundleIdToProvider',)

    def __init__(self, telecomConfig):
        self.__bundleIdToProvider = {bundleId: bundleData[b'operator'] for bundleId, bundleData in telecomConfig[b'bundles'].iteritems()}
        return

    def getInternetProvider(self, bundleId):
        provider = self.__bundleIdToProvider.get(bundleId, b'')
        return provider

    @classmethod
    def defaults(cls):
        return cls({b'bundles': {}})


class _BlueprintsConfig(namedtuple(b'_BlueprintsConfig', (b'allowBlueprintsConversion',
 b'isEnabled',
 b'useBlueprintsForUnlock',
 b'levels'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return cls(False, False, False, {})

    def allowConversion(self):
        return self.allowBlueprintsConversion

    def enabled(self):
        return self.isEnabled

    def useBlueprints(self):
        return self.useBlueprintsForUnlock

    def countAndDiscountByLevels(self):
        return self.levels

    def getAllianceConversionCoeffs(self, level):
        if not self.isBlueprintsAvailable() or level not in self.levels:
            return {}
        return self.levels[level][4]

    def getRequiredFragmentsForConversion(self, level):
        if not self.isBlueprintsAvailable() or level not in self.levels:
            return (0, 0)
        return self.levels[level][2]

    def getFragmentCount(self, level):
        if not self.isBlueprintsAvailable():
            return 0
        if level == 1:
            return 1
        if level in self.levels:
            return self.levels[level][0]
        return 0

    def getFragmentDiscount(self, level):
        discount = 0
        if self.isBlueprintsAvailable() and level > 1 and level in self.levels:
            discount = self.levels[level][1]
        return discount

    def isBlueprintsAvailable(self):
        return self.isEnabled and self.useBlueprintsForUnlock

    @staticmethod
    def isBlueprintModeChange(diff):
        return b'isEnabled' in diff or b'useBlueprintsForUnlock' in diff


class SeniorityAwardsConfig(typing.NamedTuple(b'SeniorityAwardsConfig', (
 (
  b'enabled', bool),
 (
  b'active', bool),
 (
  b'endTime', int),
 (
  b'reminders', list),
 (
  b'clockOnNotification', int),
 (
  b'showRewardNotification', bool),
 (
  b'eventPrefix', str),
 (
  b'receivedRewardsToken', str),
 (
  b'claimVehicleRewardTokenPattern', str),
 (
  b'rewardEligibilityToken', str),
 (
  b'claimRewardToken', str),
 (
  b'vehicleSelectionTokenPattern', str),
 (
  b'rewardQuestsPrefix', str),
 (
  b'categories', dict),
 (
  b'vehicleSelectionQuestPattern', str)))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, active=False, endTime=0, reminders=[], clockOnNotification=0, showRewardNotification=False, eventPrefix=b'', receivedRewardsToken=b'', rewardEligibilityToken=b'', claimRewardToken=b'', claimVehicleRewardTokenPattern=b'', vehicleSelectionTokenPattern=b'', rewardQuestsPrefix=b'', categories={}, vehicleSelectionQuestPattern=b'')
        defaults.update(kwargs)
        return super(SeniorityAwardsConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class EasyTankEquipConfig(typing.NamedTuple(b'EasyTankEquipConfig', (
 (
  b'enabled', bool),
 (
  b'minVehicleLevel', int),
 (
  b'ammunitionReductionFactor', float)))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, minVehicleLevel=1, ammunitionReductionFactor=0.0)
        defaults.update(kwargs)
        return super(EasyTankEquipConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


_crystalRewardInfo = namedtuple(b'_crystalRewardInfo', b'level, arenaType, winTop3, loseTop3, winTop10, loseTop10, topLength, firstTopLength')

class _crystalRewardConfigSection(namedtuple(b'_crystalRewardConfigSection', (b'level', b'vehicle'))):
    __slots__ = ()

    def __new__(cls, params):
        defaults = {b'level': {}, b'vehicle': {}}
        defaults.update(params)
        return super(_crystalRewardConfigSection, cls).__new__(cls, **defaults)


class _crystalRewardsConfig(namedtuple(b'_crystalRewardsConfig', (b'limits', b'rewards'))):
    __slots__ = ()
    CONFIG_NAME = b'crystal_rewards_config'

    def __new__(cls, **kwargs):
        defaults = {b'limits': (_crystalRewardConfigSection(kwargs.get(b'limits', {}))), b'rewards': (_crystalRewardConfigSection(kwargs.get(b'rewards', {})))}
        return super(_crystalRewardsConfig, cls).__new__(cls, **defaults)

    def isCrystalEarnPossible(self, arenaType, battleModifiers=None):
        battleModifiers = battleModifiers or BattleModifiers()
        for level, rewardData in self.rewards.level.iteritems():
            battleModifiersCtx = ModifiersContext(modifiers=battleModifiers, level=level)
            if self.__isCrystalEarnPossible(arenaType, battleModifiersCtx(BattleParams.CRYSTAL_REWARDS, rewardData)):
                return True

        for vehCD, rewardData in self.rewards.vehicle.iteritems():
            battleModifiersCtx = ModifiersContext(modifiers=battleModifiers, vehType=vehicles.getVehicleType(vehCD))
            if self.__isCrystalEarnPossible(arenaType, battleModifiersCtx(BattleParams.CRYSTAL_REWARDS, rewardData)):
                return True

        return False

    def getRewardInfoData(self):
        results = []
        for level, rewardData in self.rewards.level.iteritems():
            for arenaBonusType, scoreData in rewardData.iteritems():
                topWinRewards = list(scoreData[True].itervalues())
                winTop3 = max(topWinRewards)
                results.append(_crystalRewardInfo(level, arenaBonusType, winTop3=winTop3, loseTop3=max(scoreData[False].itervalues()), winTop10=min(scoreData[True].itervalues()), loseTop10=min(scoreData[False].itervalues()), topLength=len(scoreData[True]), firstTopLength=topWinRewards.count(winTop3)))

        return results

    def __isCrystalEarnPossible(self, arenaType, rewardData):
        if arenaType in rewardData:
            return sum(chain(rewardData[arenaType][False].itervalues(), rewardData[arenaType][True].itervalues())) > 0
        return False


class _ReactiveCommunicationConfig(namedtuple(b'_ReactiveCommunicationConfig', (b'isEnabled', b'url'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, url=b'')
        defaults.update(kwargs)
        if cls.isEnabled and not cls.url:
            _logger.error(b'Connection to web subscription service is enabled, but url is empty')
            defaults.update(dict(isEnabled=False))
        return super(_ReactiveCommunicationConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()


class _BlueprintsConvertSaleConfig(namedtuple(b'_BlueprintsConvertSaleConfig', (b'enabled', b'options'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, options={})
        defaults.update(kwargs)
        return super(_BlueprintsConvertSaleConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    def isEnabled(self):
        return self.enabled

    def getOptions(self):
        return self.options


class _MapboxConfig(namedtuple(b'_MapboxConfig', (
 b'isEnabled', b'progressionUpdateInterval', b'peripheryIDs', b'forbiddenClassTags', b'forbiddenVehTypes',
 b'primeTimes', b'seasons', b'cycleTimes', b'levels', b'geometryIDs', b'squadRestrictions', b'infoPageUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs={}, forbiddenClassTags=set(), forbiddenVehTypes=set(), primeTimes={}, seasons={}, cycleTimes={}, levels=[], geometryIDs={}, progressionUpdateInterval=time_utils.ONE_MINUTE * 2, squadRestrictions={}, infoPageUrl=b'')
        defaults.update(kwargs)
        return super(_MapboxConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = {k: v for k, v in data.iteritems() if k in allowedFields}
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class VehiclePostProgressionConfig(namedtuple(b'_VehiclePostProgression', (
 b'isPostProgressionEnabled',
 b'enabledFeatures',
 b'forbiddenVehicles',
 b'enabledRentedVehicles'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isPostProgressionEnabled=False, enabledFeatures=frozenset(), forbiddenVehicles=frozenset(), enabledRentedVehicles=frozenset())
        defaults.update(kwargs)
        return super(VehiclePostProgressionConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    @property
    def isEnabled(self):
        return self.isPostProgressionEnabled

    @property
    def isRoleSlotEnabled(self):
        return ROLESLOT_FEATURE in self.enabledFeatures

    def isSetupSwitchEnabled(self, groupID):
        return FEATURE_BY_GROUP_ID[groupID] in self.enabledFeatures

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class _EventBattlesConfig(namedtuple(b'_EventBattlesConfig', (
 b'isEnabled',
 b'peripheryIDs',
 b'primeTimes',
 b'seasons',
 b'cycleTimes'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs={}, primeTimes={}, seasons={}, cycleTimes={})
        defaults.update(kwargs)
        return super(_EventBattlesConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class GiftEventConfig(namedtuple(b'_GiftEventConfig', (
 b'eventID',
 b'giftEventState',
 b'giftItemIDs',
 b'clientReqStrategy'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(eventID=GiftEventID.UNKNOWN, giftEventState=GiftEventState.DISABLED, giftItemIDs=[], clientReqStrategy=ClientReqStrategy.AUTO)
        defaults.update(kwargs)
        return super(GiftEventConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    @property
    def isEnabled(self):
        return self.giftEventState == GiftEventState.ENABLED

    @property
    def isSuspended(self):
        return self.giftEventState == GiftEventState.SUSPENDED

    @property
    def isDisabled(self):
        return self.giftEventState == GiftEventState.DISABLED


class GiftSystemConfig(namedtuple(b'_GiftSystemConfig', (b'events',))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(events={})
        defaults.update(kwargs)
        cls.__packEventConfigs(defaults)
        return super(GiftSystemConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        self.__packEventConfigs(dataToUpdate)
        return self._replace(**dataToUpdate)

    @classmethod
    def __packEventConfigs(cls, data):
        data[b'events'] = {eID: makeTupleByDict(GiftEventConfig, eData) for eID, eData in data[b'events'].iteritems()}
        return


class PlayLimitsConfig(namedtuple(b'PlayLimitsConfig', (
 b'lockTimeBeforeBattle',))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(lockTimeBeforeBattle={})
        defaults.update(kwargs)
        return super(PlayLimitsConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _BattleMattersConfig(namedtuple(b'_BattleMattersConfig', (
 b'isEnabled',
 b'isPaused',
 b'delayedRewardOfferVisibilityToken',
 b'delayedRewardOfferCurrencyToken'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, isPaused=False, delayedRewardOfferVisibilityToken=b'BattleMattersEmptyToken', delayedRewardOfferCurrencyToken=b'BattleMattersEmptyCurrencyToken')
        defaults.update(kwargs)
        return super(_BattleMattersConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class PeripheryRoutingConfig(namedtuple(b'_PeripheryRoutingConfig', (b'isEnabled', b'peripheryRoutingGroups'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryRoutingGroups={})
        defaults.update(kwargs)
        return super(PeripheryRoutingConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


def settingsBlock(className, fields):

    class SettingsBlock(namedtuple(className, fields)):
        __slots__ = ()

        def __new__(cls, **kwargs):
            defaults = cls.defaults()
            defaults.update(cls._preprocessData(kwargs))
            return super(SettingsBlock, cls).__new__(cls, **defaults)

        def asDict(self):
            return self._asdict()

        def replace(self, data):
            allowedFields = self._fields
            dataToUpdate = {k: v for k, v in self._preprocessData(data).iteritems() if k in allowedFields}
            return self._replace(**dataToUpdate)

        @classmethod
        def defaults(cls):
            raise NotImplementedError
            return

        @classmethod
        def _preprocessData(cls, data):
            return data

    return SettingsBlock


class WinbackConfig(namedtuple(b'WinbackConfig', (
 b'isEnabled',
 b'isModeEnabled',
 b'isWhatsNewEnabled',
 b'isProgressionEnabled',
 b'tokenQuestPrefix',
 b'offerTokenPrefix',
 b'winbackAccessToken',
 b'winbackModeAccessTokens',
 b'winbackBattlesCountToken',
 b'winbackShowPromoToken',
 b'winbackPromoURL',
 b'lastQuestEnabler',
 b'winbackStartingQuest',
 b'chainVersions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, isModeEnabled=False, isWhatsNewEnabled=False, isProgressionEnabled=False, tokenQuestPrefix=b'', offerTokenPrefix=b'', winbackAccessToken=b'', winbackModeAccessTokens=[], winbackBattlesCountToken=b'', winbackShowPromoToken=b'', winbackPromoURL=b'', lastQuestEnabler=b'', winbackStartingQuest=b'', chainVersions=list())
        defaults.update(kwargs)
        return super(WinbackConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class PersonalReservesConfig(namedtuple(b'_PersonalReserves', (b'isReservesInBattleActivationEnabled',
 b'supportedQueueTypes'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isReservesInBattleActivationEnabled=False, supportedQueueTypes={})
        defaults.update(**kwargs)
        return super(PersonalReservesConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class PreModerationConfig(namedtuple(b'_PreModerationConfig', (b'prebattleDescriptionEnabled',))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(prebattleDescriptionEnabled=False)
        defaults.update(kwargs)
        return super(PreModerationConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class LootBoxSystemEventConfig(namedtuple(b'_LootBoxSystemEventConfig', (
 b'enabled', b'eventName', b'boxesPriority', b'start', b'finish', b'dailyPurchaseLimit'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, eventName=b'', boxesPriority=tuple(), start=0, finish=0, dailyPurchaseLimit=0)
        defaults.update(kwargs)
        return super(LootBoxSystemEventConfig, cls).__new__(cls, **defaults)

    def getActiveTime(self):
        return (
         self.start, self.finish)


LOOTBOX_SYSTEM_CONFIG = b'lootbox_system_config'

class _LootBoxSystemConfig(namedtuple(b'_LootBoxSystemConfig', (b'events', b'mainEntryPoint'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(events={}, mainEntryPoint=b'')
        defaults.update(kwargs)
        cls.__packEventConfigs(defaults)
        return super(_LootBoxSystemConfig, cls).__new__(cls, **defaults)

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        self.__packEventConfigs(dataToUpdate)
        return self._replace(**dataToUpdate)

    @classmethod
    def __packEventConfigs(cls, dataToUpdate):
        dataToUpdate[b'events'] = {eventName: LootBoxSystemEventConfig(eventName=eventName, **event) for eventName, event in dataToUpdate[b'events'].iteritems()}
        return


class _LimitedUIConfig(namedtuple(b'_LimitedUIConfig', (b'enabled', b'rules', b'version'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, rules={ruleType: [] for ruleType in LuiRuleTypes.ALL()}, version=0)
        defaults.update(kwargs)
        return super(_LimitedUIConfig, cls).__new__(cls, **defaults)

    def hasRules(self):
        return any(self.rules.values())

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _SteamShadeConfig(namedtuple(b'_SteamShadeConfig', (b'battlesPlayed', b'sessions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(battlesPlayed=10, sessions=3)
        defaults.update(kwargs)
        return super(_SteamShadeConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _ABFeatureTestConfig(namedtuple(b'_ABFeatureTestConfig', (b'newbieHints', b'storyMode'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = {field: {} for field in cls._fields}
        defaults.update(kwargs)
        return super(_ABFeatureTestConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class ReferralProgramConfig(namedtuple(b'ReferralProgramConfig', (
 b'periodNumber', b'periodStartDatetime', b'periodEndDatetime'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(periodNumber=0, periodStartDatetime=0, periodEndDatetime=0)
        defaults.update(kwargs)
        return super(ReferralProgramConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class LiveOpsWebEventsConfig(namedtuple(b'LiveOpsWebEventsConfig', (
 b'eventUniqueName', b'isEnabled', b'url', b'preEventStart', b'eventStart', b'eventEnd', b'postEventEnd',
 b'isEntryPointSmall'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(eventUniqueName=b'', isEnabled=False, url=b'', preEventStart=0, eventStart=0, eventEnd=0, postEventEnd=0, isEntryPointSmall=True)
        defaults.update(kwargs)
        return super(LiveOpsWebEventsConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _AdvancedAchievementsConfig(namedtuple(b'_AdvancedAchievementsConfig', (
 b'enabled', b'vehicleAchievementsEnabled', b'customizationAchievementsEnabled'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, vehicleAchievementsEnabled=False, customizationAchievementsEnabled=False)
        defaults.update(kwargs)
        return super(_AdvancedAchievementsConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _ExchangeRatesConfig(namedtuple(b'_ExchangeRatesConfig', (b'isGoldExchangePesronalDiscountsAvailable',
 b'isExperienceExchangePesronalDiscountsAvailable'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isGoldExchangePesronalDiscountsAvailable=False, isExperienceExchangePesronalDiscountsAvailable=False)
        defaults.update(kwargs)
        return super(_ExchangeRatesConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class PetSystemServerSettings(object):

    def __init__(self, config):
        self.__config = config
        return

    def getPetGeneralConfig(self):
        return PetGeneralConfig(self.__config.get(pet_constants.PetSystemGeneralConsts.CONFIG_NAME, {}))

    def getPetsConfig(self):
        return PetConfig(self.__config.get(pet_constants.PetsConsts.CONFIG_NAME, {}))

    def getPetBonusConfig(self):
        return PetBonusConfig(self.__config.get(pet_constants.PetBonusesConsts.CONFIG_NAME, {}))

    def getPetEventConfig(self):
        return PetEventConfig(self.__config.get(pet_constants.PetEventsConsts.CONFIG_NAME, {}))

    def getPetPromoConfig(self):
        return PetPromoConfig(self.__config.get(pet_constants.PetPromoConsts.CONFIG_NAME, {}))

    def getPetSynergyConfig(self):
        return PetSynergyConfig(self.__config.get(pet_constants.PetSynergyConsts.CONFIG_NAME, {}))


class _IngameTournamentShowmatchConfig(settingsBlock(b'_IngameTournamentShowmatchConfig', (
 b'startTime',
 b'endTime'))):

    @classmethod
    def defaults(cls):
        return {b'startTime': None, 
           b'endTime': None}


class _IngameTournamentShopConfig(settingsBlock(b'_IngameTournamentShopConfig', (
 b'realms',
 b'ingameShopRelativePath',
 b'shopUrl'))):

    @classmethod
    def defaults(cls):
        return {b'realms': [], b'ingameShopRelativePath': b'', 
           b'shopUrl': b''}

    @classmethod
    def _preprocessData(cls, data):
        realms = data.get(b'realms')
        if realms is not None:
            data[b'realms'] = realms.split()
        return data


class _IngameTournamentConfigByTournamentType(settingsBlock(b'_IngameTournamentConfigByTournamentType', (
 b'isEnabled',
 b'startTime',
 b'endTime',
 b'showmatches',
 b'shop',
 b'offerGiftsToken',
 b'tokenStoreOpeningTime'))):

    @classmethod
    def defaults(cls):
        return {b'isEnabled': False, 
           b'startTime': 0, 
           b'endTime': 0, 
           b'showmatches': [], b'shop': [], b'offerGiftsToken': b'', 
           b'tokenStoreOpeningTime': 0}

    @classmethod
    def _preprocessData(cls, data):
        showmatches = []
        for showmatchConfig in data.get(b'showmatches', []):
            showmatches.append(makeTupleByDict(_IngameTournamentShowmatchConfig, showmatchConfig))

        data[b'showmatches'] = showmatches
        shopConfigs = []
        for shopConfig in data.get(b'shop', []):
            shopConfigs.append(makeTupleByDict(_IngameTournamentShopConfig, shopConfig))

        data[b'shop'] = shopConfigs
        return data


class _IngameTournamentConfig(settingsBlock(b'_IngameTournamentConfig', (
 IngameTournamentType.WCI.value,
 IngameTournamentType.OLS.value))):

    @classmethod
    def defaults(cls):
        res = {}
        for tournamentType in IngameTournamentType:
            res[tournamentType.value] = _IngameTournamentConfigByTournamentType.defaults()

        return res

    @classmethod
    def _preprocessData(cls, data):
        for tournamentType in IngameTournamentType:
            tournamentTypeStr = tournamentType.value
            tournamentTypeData = data.get(tournamentTypeStr)
            if tournamentTypeData:
                data[tournamentTypeStr] = makeTupleByDict(_IngameTournamentConfigByTournamentType, tournamentTypeData)
            else:
                data[tournamentTypeStr] = _IngameTournamentConfigByTournamentType.defaults()

        return data


class _W2GTConfig(namedtuple(b'_W2GTConfig', (b'enabled', b'dataLifetime', b'timeLimits', b'restrictedVehicles'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, dataLifetime=0, timeLimits={}, restrictedVehicles={})
        defaults.update(kwargs)
        return super(_W2GTConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    def getTimeLimitByStage(self, stage):
        return self.timeLimits.get(stage, 0)


class ServerSettings(object):

    def __init__(self, serverSettings):
        self.onServerSettingsChange = Event()
        self.__serverSettings = {}
        self.__roamingSettings = RoamingSettings.defaults()
        self.__fileServerSettings = _FileServerSettings.defaults()
        self.__regionalSettings = _RegionalSettings.defaults()
        self.__eSportCurrentSeason = _ESportCurrentSeason.defaults()
        self.__wgcg = _Wgcg.defaults()
        self.__wgnp = _Wgnp.defaults()
        self.__uiLogging = _UILogging.defaults()
        self.__eula = _EULA.defaults()
        self.__clanProfile = _ClanProfile.defaults()
        self.__spgRedesignFeatures = _SpgRedesignFeatures.defaults()
        self.__strongholdSettings = _StrongholdSettings.defaults()
        self.__tournamentSettings = _TournamentSettings.defaults()
        self.__frontlineSettings = _FrontlineSettings.defaults()
        self.__bwHallOfFame = _BwHallOfFame.defaults()
        self.__bwShop = _BwShop()
        self.__rankedBattlesSettings = RankedBattlesConfig.defaults()
        self.__epicMetaGameSettings = _EpicMetaGameConfig()
        self.__epicGameSettings = EpicGameConfig()
        self.__unitAssemblerConfig = _UnitAssemblerConfig.defaults()
        self.__telecomConfig = _TelecomConfig.defaults()
        self.__squadPremiumBonus = _SquadPremiumBonus.defaults()
        self.__battlePassConfig = BattlePassConfig({})
        self.__crystalRewardsConfig = _crystalRewardsConfig()
        self.__reactiveCommunicationConfig = _ReactiveCommunicationConfig()
        self.__blueprintsConvertSaleConfig = _BlueprintsConvertSaleConfig()
        self.__bwProductCatalog = _BwProductCatalog()
        self.__vehiclePostProgressionConfig = VehiclePostProgressionConfig()
        self.__eventBattlesConfig = _EventBattlesConfig()
        self.__giftSystemConfig = GiftSystemConfig()
        self.__battleMattersConfig = _BattleMattersConfig()
        self.__peripheryRoutingConfig = PeripheryRoutingConfig()
        self.__personalReservesConfig = PersonalReservesConfig()
        self.__playLimitsConfig = PlayLimitsConfig()
        self.__preModerationConfig = PreModerationConfig()
        self.__lootBoxSystemConfig = _LootBoxSystemConfig()
        self.__collectionsConfig = CollectionsConfig()
        self.__winbackConfig = WinbackConfig()
        self.__limitedUIConfig = _LimitedUIConfig()
        self.__prestigeConfig = PrestigeConfig({})
        self.__prestigeMilestonesConfig = PrestigeMilestonesConfig({})
        self.__steamShadeConfig = _SteamShadeConfig()
        self.__abFeatureTestConfig = _ABFeatureTestConfig()
        self.__referralProgramConfig = ReferralProgramConfig()
        self.__liveOpsWebEventsConfig = LiveOpsWebEventsConfig()
        self.__advancedAchievementsConfig = _AdvancedAchievementsConfig()
        self.__schemaManager = getSchemaManager()
        self.__exchangeRatesConfig = _ExchangeRatesConfig()
        self.__easyTankEquipConfig = EasyTankEquipConfig()
        self.__ingameTournamentConfig = _IngameTournamentConfig()
        self.__w2gtConfig = _W2GTConfig()
        self.__challengesConfig = ChallengesConfig({})
        self.set(serverSettings)
        return

    def set(self, serverSettings):
        self.__serverSettings = copy.deepcopy(serverSettings) if serverSettings else {}
        if b'roaming' in self.__serverSettings:
            roamingSettings = self.__serverSettings[b'roaming']
            self.__roamingSettings = RoamingSettings(roamingSettings[0], roamingSettings[1], [_ServerInfo(*s) for s in roamingSettings[2]])
        if b'file_server' in self.__serverSettings:
            self.__fileServerSettings = _FileServerSettings(self.__serverSettings[b'file_server'])
        if b'regional_settings' in self.__serverSettings:
            self.__regionalSettings = makeTupleByDict(_RegionalSettings, self.__serverSettings[b'regional_settings'])
        try:
            self.__eSportCurrentSeason = makeTupleByDict(_ESportCurrentSeason, self.__serverSettings)
        except TypeError:
            self.__eSportCurrentSeason = _ESportCurrentSeason.defaults()

        if b'wgcg' in self.__serverSettings:
            self.__updateWgcg(self.__serverSettings)
        if b'wgnp' in self.__serverSettings:
            self.__updateWgnp(self.__serverSettings)
        if Configs.UI_LOGGING.value in self.__serverSettings:
            self.__updateUILogging(self.__serverSettings)
        if b'eula_config' in self.__serverSettings:
            self.__updateEULA(self.__serverSettings)
        if b'clanProfile' in self.__serverSettings:
            self.__updateClanProfile(self.__serverSettings)
        if b'spgRedesignFeatures' in self.__serverSettings:
            self.__spgRedesignFeatures = makeTupleByDict(_SpgRedesignFeatures, self.__serverSettings[b'spgRedesignFeatures'])
        if b'strongholdSettings' in self.__serverSettings:
            settings = self.__serverSettings[b'strongholdSettings']
            self.__strongholdSettings = _StrongholdSettings(settings.get(b'wgshHostUrl', b''))
        if b'frontlineSettings' in self.__serverSettings:
            settings = self.__serverSettings[b'frontlineSettings']
            self.__frontlineSettings = _FrontlineSettings(settings.get(b'isEpicTrainingEnabled', True))
        if b'hallOfFame' in self.__serverSettings:
            self.__bwHallOfFame = makeTupleByDict(_BwHallOfFame, self.__serverSettings[b'hallOfFame'])
        if b'shop' in self.__serverSettings:
            self.__bwShop = makeTupleByDict(_BwShop, self.__serverSettings[b'shop'])
        if b'ranked_config' in self.__serverSettings:
            self.__rankedBattlesSettings = makeTupleByDict(RankedBattlesConfig, self.__serverSettings[b'ranked_config'])
        if b'epic_config' in self.__serverSettings:
            LOG_DEBUG(b'epic_config', self.__serverSettings[b'epic_config'])
            self.__epicMetaGameSettings = makeTupleByDict(_EpicMetaGameConfig, self.__serverSettings[b'epic_config'][b'epicMetaGame'])
            self.__epicGameSettings = makeTupleByDict(EpicGameConfig, self.__serverSettings[b'epic_config'])
        if Configs.UNIT_ASSEMBLER_CONFIG.value in self.__serverSettings:
            self.__unitAssemblerConfig = makeTupleByDict(_UnitAssemblerConfig, self.__serverSettings[Configs.UNIT_ASSEMBLER_CONFIG.value])
        if PremiumConfigs.PREM_SQUAD in self.__serverSettings:
            self.__squadPremiumBonus = _SquadPremiumBonus.create(self.__serverSettings[PremiumConfigs.PREM_SQUAD])
        if Configs.BATTLE_ROYALE_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(b'battle_royale_config', self.__serverSettings[Configs.BATTLE_ROYALE_CONFIG.value])
            self.__battleRoyaleSettings = makeTupleByDict(BattleRoyaleConfig, self.__serverSettings[Configs.BATTLE_ROYALE_CONFIG.value])
        else:
            self.__battleRoyaleSettings = BattleRoyaleConfig.defaults()
        if b'telecom_config' in self.__serverSettings:
            self.__telecomConfig = _TelecomConfig(self.__serverSettings[b'telecom_config'])
        if b'blueprints_config' in self.__serverSettings:
            self.__blueprintsConfig = makeTupleByDict(_BlueprintsConfig, self.__serverSettings[b'blueprints_config'])
        else:
            self.__blueprintsConfig = _BlueprintsConfig.defaults()
        if b'progressive_reward_config' in self.__serverSettings:
            self.__progressiveReward = makeTupleByDict(_ProgressiveReward, self.__serverSettings[b'progressive_reward_config'])
        else:
            self.__progressiveReward = _ProgressiveReward()
        if Configs.SENIORITY_AWARDS_CONFIG.value in self.__serverSettings:
            self.__seniorityAwardsConfig = makeTupleByDict(SeniorityAwardsConfig, self.__serverSettings[Configs.SENIORITY_AWARDS_CONFIG.value])
        else:
            self.__seniorityAwardsConfig = SeniorityAwardsConfig()
        if b'exchange_rates_config' in self.__serverSettings:
            self.__exchangeRatesConfig = makeTupleByDict(_ExchangeRatesConfig, self.__serverSettings[b'exchange_rates_config'])
        else:
            self.__exchangeRatesConfig = _ExchangeRatesConfig()
        if Configs.EASY_TANK_EQUIP_CONFIG.value in self.__serverSettings:
            self.__easyTankEquipConfig = makeTupleByDict(EasyTankEquipConfig, self.__serverSettings[Configs.EASY_TANK_EQUIP_CONFIG.value])
        if BATTLE_PASS_CONFIG_NAME in self.__serverSettings:
            self.__battlePassConfig = BattlePassConfig(self.__serverSettings.get(BATTLE_PASS_CONFIG_NAME, {}))
        else:
            self.__battlePassConfig = BattlePassConfig({})
        if _crystalRewardsConfig.CONFIG_NAME in self.__serverSettings:
            self.__crystalRewardsConfig = makeTupleByDict(_crystalRewardsConfig, self.__serverSettings[_crystalRewardsConfig.CONFIG_NAME])
        self.__updateReactiveCommunicationConfig(self.__serverSettings)
        if LOOTBOX_SYSTEM_CONFIG in self.__serverSettings:
            self.__lootBoxSystemConfig = makeTupleByDict(_LootBoxSystemConfig, self.__serverSettings[LOOTBOX_SYSTEM_CONFIG])
        if BonusCapsConst.CONFIG_NAME in self.__serverSettings:
            BONUS_CAPS.OVERRIDE_BONUS_CAPS = self.__serverSettings[BonusCapsConst.CONFIG_NAME]
        else:
            BONUS_CAPS.OVERRIDE_BONUS_CAPS = dict()
        if b'blueprints_convert_sale_config' in self.__serverSettings:
            self.__blueprintsConvertSaleConfig = makeTupleByDict(_BlueprintsConvertSaleConfig, self.__serverSettings[b'blueprints_convert_sale_config'])
        else:
            self.__blueprintsConvertSaleConfig = _BlueprintsConvertSaleConfig()
        if Configs.MAPBOX_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(b'mapbox_config', self.__serverSettings[Configs.MAPBOX_CONFIG.value])
            self.__mapboxSettings = makeTupleByDict(_MapboxConfig, self.__serverSettings[Configs.MAPBOX_CONFIG.value])
        else:
            self.__mapboxSettings = _MapboxConfig.defaults()
        if b'productsCatalog' in self.__serverSettings:
            self.__bwProductCatalog = makeTupleByDict(_BwProductCatalog, self.__serverSettings[b'productsCatalog'])
        if post_progression_common.SERVER_SETTINGS_KEY in self.__serverSettings:
            self.__vehiclePostProgressionConfig = makeTupleByDict(VehiclePostProgressionConfig, self.__serverSettings[post_progression_common.SERVER_SETTINGS_KEY])
        if b'event_battles_config' in self.__serverSettings:
            self.__eventBattlesConfig = makeTupleByDict(_EventBattlesConfig, self.__serverSettings[b'event_battles_config'])
        else:
            self.__eventBattlesConfig = _EventBattlesConfig.defaults()
        if Configs.GIFTS_CONFIG.value in self.__serverSettings:
            self.__giftSystemConfig = makeTupleByDict(GiftSystemConfig, {b'events': (self.__serverSettings[Configs.GIFTS_CONFIG.value])})
        if Configs.BATTLE_MATTERS_CONFIG.value in self.__serverSettings:
            self.__battleMattersConfig = makeTupleByDict(_BattleMattersConfig, self.__serverSettings[Configs.BATTLE_MATTERS_CONFIG.value])
        if Configs.PERIPHERY_ROUTING_CONFIG.value in self.__serverSettings:
            self.__peripheryRoutingConfig = makeTupleByDict(PeripheryRoutingConfig, self.__serverSettings[Configs.PERIPHERY_ROUTING_CONFIG.value])
        if Configs.PERSONAL_RESERVES_CONFIG.value in self.__serverSettings:
            self.__personalReservesConfig = makeTupleByDict(PersonalReservesConfig, self.__serverSettings[Configs.PERSONAL_RESERVES_CONFIG.value])
        else:
            self.__personalReservesConfig = PersonalReservesConfig.defaults()
        if Configs.PLAY_LIMITS_CONFIG.value in self.__serverSettings:
            self.__playLimitsConfig = makeTupleByDict(PlayLimitsConfig, self.__serverSettings[Configs.PLAY_LIMITS_CONFIG.value])
        if Configs.PRE_MODERATION_CONFIG.value in self.__serverSettings:
            self.__preModerationConfig = makeTupleByDict(PreModerationConfig, self.__serverSettings[Configs.PRE_MODERATION_CONFIG.value])
        else:
            self.__preModerationConfig = PreModerationConfig.defaults()
        if TOURNAMENT_CONFIG in self.__serverSettings:
            self.__tournamentSettings = makeTupleByDict(_TournamentSettings, self.__serverSettings[TOURNAMENT_CONFIG])
        else:
            self.__tournamentSettings = _TournamentSettings.defaults()
        if Configs.COLLECTIONS_CONFIG.value in self.__serverSettings:
            self.__collectionsConfig = makeTupleByDict(CollectionsConfig, self.__serverSettings[Configs.COLLECTIONS_CONFIG.value])
        if Configs.WINBACK_CONFIG.value in self.__serverSettings:
            _logger.info(Configs.WINBACK_CONFIG.value, self.__serverSettings[Configs.WINBACK_CONFIG.value])
            self.__winbackConfig = makeTupleByDict(WinbackConfig, self.__serverSettings[Configs.WINBACK_CONFIG.value])
        else:
            self.__winbackConfig = WinbackConfig.defaults()
        if Configs.LIMITED_UI_CONFIG.value in self.__serverSettings:
            self.__limitedUIConfig = makeTupleByDict(_LimitedUIConfig, self.__serverSettings[Configs.LIMITED_UI_CONFIG.value])
        else:
            self.__limitedUIConfig = _LimitedUIConfig.defaults()
        if Configs.PRESTIGE_CONFIG.value in self.__serverSettings:
            self.__prestigeConfig = PrestigeConfig(self.__serverSettings.get(Configs.PRESTIGE_CONFIG.value, {}))
        else:
            self.__prestigeConfig = PrestigeConfig({})
        if Configs.PRESTIGE_MILESTONES_CONFIG.value in self.__serverSettings:
            self.__prestigeMilestonesConfig = PrestigeMilestonesConfig(self.__serverSettings.get(Configs.PRESTIGE_MILESTONES_CONFIG.value, {}))
        else:
            self.__prestigeMilestonesConfig = PrestigeMilestonesConfig({})
        self.__schemaManager.set(self.__serverSettings)
        if Configs.STEAM_SHADE_CONFIG.value in self.__serverSettings:
            self.__steamShadeConfig = makeTupleByDict(_SteamShadeConfig, self.__serverSettings[Configs.STEAM_SHADE_CONFIG.value])
        else:
            self.__steamShadeConfig = _SteamShadeConfig.defaults()
        if Configs.AB_FEATURE_TEST.value in self.__serverSettings:
            self.__abFeatureTestConfig = makeTupleByDict(_ABFeatureTestConfig, self.__serverSettings[Configs.AB_FEATURE_TEST.value])
        else:
            self.__abFeatureTestConfig = _ABFeatureTestConfig.defaults()
        if Configs.REFERRAL_PROGRAM_CONFIG.value in self.__serverSettings:
            self.__referralProgramConfig = makeTupleByDict(ReferralProgramConfig, self.__serverSettings[Configs.REFERRAL_PROGRAM_CONFIG.value])
        else:
            self.__referralProgramConfig = ReferralProgramConfig.defaults()
        if Configs.LIVE_OPS_EVENTS_CONFIG.value in self.__serverSettings:
            self.__liveOpsWebEventsConfig = makeTupleByDict(LiveOpsWebEventsConfig, self.__serverSettings[Configs.LIVE_OPS_EVENTS_CONFIG.value])
        else:
            self.__liveOpsWebEventsConfig = LiveOpsWebEventsConfig.defaults()
        if Configs.INGAME_TOURNAMENT_CONFIG.value in self.__serverSettings:
            self.__ingameTournamentConfig = makeTupleByDict(_IngameTournamentConfig, self.__serverSettings[Configs.INGAME_TOURNAMENT_CONFIG.value])
        else:
            self.__ingameTournamentConfig = _IngameTournamentConfig.defaults()
        if Configs.W2GT_CONFIG.value in self.__serverSettings:
            self.__w2gtConfig = makeTupleByDict(_W2GTConfig, self.__serverSettings[Configs.W2GT_CONFIG.value])
        else:
            self.__w2gtConfig = _W2GTConfig()
        if Configs.CHALLENGES_CONFIG.value in self.__serverSettings:
            self.__challengesConfig = ChallengesConfig(self.__serverSettings[Configs.CHALLENGES_CONFIG.value])
        else:
            self.__challengesConfig = ChallengesConfig({})
        self.onServerSettingsChange(serverSettings)
        return

    def update(self, serverSettingsDiff):
        processedDiff = self.__schemaManager.updateSettings(self.__serverSettings, serverSettingsDiff)
        self.__serverSettings = updateDict(self.__serverSettings, processedDiff)
        if b'clanProfile' in serverSettingsDiff:
            self.__updateClanProfile(serverSettingsDiff)
        if b'spgRedesignFeatures' in self.__serverSettings:
            self.__spgRedesignFeatures = makeTupleByDict(_SpgRedesignFeatures, self.__serverSettings[b'spgRedesignFeatures'])
        if b'ranked_config' in serverSettingsDiff:
            self.__updateRanked(serverSettingsDiff)
        if b'hallOfFame' in serverSettingsDiff:
            self.__bwHallOfFame = makeTupleByDict(_BwHallOfFame, serverSettingsDiff[b'hallOfFame'])
        if b'wgcg' in serverSettingsDiff:
            self.__updateWgcg(serverSettingsDiff)
        if b'wgnp' in serverSettingsDiff:
            self.__updateWgnp(serverSettingsDiff)
        if Configs.UI_LOGGING.value in serverSettingsDiff:
            self.__updateUILogging(serverSettingsDiff)
        if b'eula_config' in serverSettingsDiff:
            self.__updateEULA(serverSettingsDiff)
        if b'exchange_rates_config' in serverSettingsDiff:
            self.__updateExchangeRates(serverSettingsDiff)
            self.__serverSettings[b'exchange_rates_config'] = serverSettingsDiff[b'exchange_rates_config']
        if b'epic_config' in serverSettingsDiff:
            self.__updateEpic(serverSettingsDiff)
            self.__serverSettings[b'epic_config'] = serverSettingsDiff[b'epic_config']
        if b'epicMetaGame' in serverSettingsDiff:
            self.__updateEpic(serverSettingsDiff)
            epicSettings = self.__serverSettings.setdefault(b'epic_config', {})
            epicSettings[b'epicMetaGame'] = serverSettingsDiff[b'epicMetaGame']
        if Configs.BATTLE_ROYALE_CONFIG.value in serverSettingsDiff:
            self.__updateBattleRoyale(serverSettingsDiff)
        if Configs.MAPBOX_CONFIG.value in serverSettingsDiff:
            self.__updateMapbox(serverSettingsDiff)
        if Configs.UNIT_ASSEMBLER_CONFIG.value in serverSettingsDiff:
            self.__updateUnitAssemblerConfig(serverSettingsDiff)
            configName = Configs.UNIT_ASSEMBLER_CONFIG.value
            self.__serverSettings[configName] = serverSettingsDiff[configName]
        if b'telecom_config' in serverSettingsDiff:
            self.__telecomConfig = _TelecomConfig(self.__serverSettings[b'telecom_config'])
        if b'disabledPMOperations' in serverSettingsDiff:
            self.__serverSettings[b'disabledPMOperations'] = serverSettingsDiff[b'disabledPMOperations']
        if b'shop' in serverSettingsDiff:
            self.__updateShop(serverSettingsDiff)
        if b'disabledPersonalMissions' in serverSettingsDiff:
            self.__serverSettings[b'disabledPersonalMissions'] = serverSettingsDiff[b'disabledPersonalMissions']
        if b'blueprints_config' in serverSettingsDiff:
            self.__updateBlueprints(serverSettingsDiff[b'blueprints_config'])
        if b'lootBoxes_config' in serverSettingsDiff:
            self.__serverSettings[b'lootBoxes_config'] = serverSettingsDiff[b'lootBoxes_config']
        if b'progressive_reward_config' in serverSettingsDiff:
            self.__updateProgressiveReward(serverSettingsDiff)
        if Configs.SENIORITY_AWARDS_CONFIG.value in serverSettingsDiff:
            self.__updateSeniorityAwards(serverSettingsDiff)
        if b'event_battles_config' in serverSettingsDiff:
            self.__updateEventBattles(serverSettingsDiff)
        if BonusCapsConst.CONFIG_NAME in serverSettingsDiff:
            BONUS_CAPS.OVERRIDE_BONUS_CAPS = serverSettingsDiff[BonusCapsConst.CONFIG_NAME]
        if PremiumConfigs.PIGGYBANK in serverSettingsDiff:
            self.__serverSettings[PremiumConfigs.PIGGYBANK] = serverSettingsDiff[PremiumConfigs.PIGGYBANK]
        if PremiumConfigs.DAILY_BONUS in serverSettingsDiff:
            self.__serverSettings[PremiumConfigs.DAILY_BONUS] = serverSettingsDiff[PremiumConfigs.DAILY_BONUS]
        if PremiumConfigs.PREM_QUESTS in serverSettingsDiff:
            self.__serverSettings[PremiumConfigs.PREM_QUESTS] = serverSettingsDiff[PremiumConfigs.PREM_QUESTS]
        if PremiumConfigs.PREM_SQUAD in serverSettingsDiff:
            self.__updateSquadBonus(serverSettingsDiff)
        if PremiumConfigs.PREFERRED_MAPS in serverSettingsDiff:
            self.__serverSettings[PremiumConfigs.PREFERRED_MAPS] = serverSettingsDiff[PremiumConfigs.PREFERRED_MAPS]
        if BATTLE_PASS_CONFIG_NAME in serverSettingsDiff:
            self.__serverSettings[BATTLE_PASS_CONFIG_NAME] = serverSettingsDiff[BATTLE_PASS_CONFIG_NAME]
            self.__battlePassConfig = BattlePassConfig(self.__serverSettings.get(BATTLE_PASS_CONFIG_NAME, {}))
        if CollectorVehicleConsts.CONFIG_NAME in serverSettingsDiff:
            self.__serverSettings[CollectorVehicleConsts.CONFIG_NAME] = serverSettingsDiff[CollectorVehicleConsts.CONFIG_NAME]
        if _crystalRewardsConfig.CONFIG_NAME in serverSettingsDiff:
            self.__crystalRewardsConfig = makeTupleByDict(_crystalRewardsConfig, serverSettingsDiff[_crystalRewardsConfig.CONFIG_NAME])
        if post_progression_common.SERVER_SETTINGS_KEY in serverSettingsDiff:
            self.__updateVehiclePostProgressionConfig(serverSettingsDiff)
        if Configs.GIFTS_CONFIG.value in serverSettingsDiff:
            self.__updateGiftSystemConfig(serverSettingsDiff)
        if Configs.BATTLE_MATTERS_CONFIG.value in serverSettingsDiff:
            self.__updateBattleMatters(serverSettingsDiff)
        if TRADE_IN_CONFIG_NAME in serverSettingsDiff:
            self.__serverSettings[TRADE_IN_CONFIG_NAME] = serverSettingsDiff[TRADE_IN_CONFIG_NAME]
        if Configs.PERIPHERY_ROUTING_CONFIG.value in serverSettingsDiff:
            self.__updatePeripheryRoutingConfig(serverSettingsDiff)
        if Configs.PLAY_LIMITS_CONFIG.value in serverSettingsDiff:
            self.__updatePlayLimitsConfig(serverSettingsDiff)
        if Configs.PRE_MODERATION_CONFIG.value in serverSettingsDiff:
            self.__updatePreModerationConfig(serverSettingsDiff)
        if TOURNAMENT_CONFIG in serverSettingsDiff:
            self.__updateTournamentsConfig(serverSettingsDiff)
        self.__updateBlueprintsConvertSaleConfig(serverSettingsDiff)
        self.__updateReactiveCommunicationConfig(serverSettingsDiff)
        if Configs.CUSTOMIZATION_QUESTS.value in serverSettingsDiff:
            key = Configs.CUSTOMIZATION_QUESTS.value
            self.__serverSettings[key] = serverSettingsDiff[key]
        if Configs.WINBACK_CONFIG.value in serverSettingsDiff:
            self.__updateWinbackConfig(serverSettingsDiff)
        self.__updatePersonalReserves(serverSettingsDiff)
        if LOOTBOX_SYSTEM_CONFIG in serverSettingsDiff:
            self.__updateLootBoxSystemConfig(serverSettingsDiff)
        self.__updateLootBoxesTooltipConfig(serverSettingsDiff)
        if Configs.COLLECTIONS_CONFIG.value in serverSettingsDiff:
            self.__updateCollectionsConfig(serverSettingsDiff)
        self.__updateLimitedUIConfig(serverSettingsDiff)
        self.__updateEasyTankEquipConfig(serverSettingsDiff)
        if Configs.PRESTIGE_CONFIG.value in serverSettingsDiff:
            self.__serverSettings[Configs.PRESTIGE_CONFIG.value] = serverSettingsDiff[Configs.PRESTIGE_CONFIG.value]
            self.__prestigeConfig = PrestigeConfig(self.__serverSettings.get(Configs.PRESTIGE_CONFIG.value, {}))
        self.__updatePrestigeMilestonesConfig(serverSettingsDiff)
        self.__schemaManager.update(serverSettingsDiff)
        self.__updateSteamShadeConfig(serverSettingsDiff)
        self.__updateABFeatureTestConfig(serverSettingsDiff)
        if Configs.REFERRAL_PROGRAM_CONFIG.value in serverSettingsDiff:
            self.__updateReferralProgramConfig(serverSettingsDiff)
        if Configs.LIVE_OPS_EVENTS_CONFIG.value in serverSettingsDiff:
            self.__updateLiveOpsWebEventsConfig(serverSettingsDiff)
        if PETS_SYSTEM_CONFIG in serverSettingsDiff:
            self.__serverSettings[PETS_SYSTEM_CONFIG] = serverSettingsDiff[PETS_SYSTEM_CONFIG]
        if Configs.INGAME_TOURNAMENT_CONFIG.value in serverSettingsDiff:
            self.__updateIngameTournamentConfig(serverSettingsDiff)
        if Configs.W2GT_CONFIG.value in serverSettingsDiff:
            self.__updateW2GTConfig(serverSettingsDiff)
        if Configs.CHALLENGES_CONFIG.value in serverSettingsDiff:
            self.__challengesConfig = ChallengesConfig(serverSettingsDiff[Configs.CHALLENGES_CONFIG.value])
        self.onServerSettingsChange(serverSettingsDiff)
        return

    def clear(self):
        self.__schemaManager.clear()
        self.onServerSettingsChange.clear()
        return

    def getSettings(self):
        return self.__serverSettings

    def getConfigModel(self, schema):
        configModel = self.__schemaManager.getModel(schema)
        if configModel is None:
            raise SoftException(b'Schema %s was not registered. All schemas must be registered before ServerSettings inited.', schema.gpKey)
        return configModel

    @property
    def roaming(self):
        return self.__roamingSettings

    @property
    def fileServer(self):
        return self.__fileServerSettings

    @property
    def regionals(self):
        return self.__regionalSettings

    @property
    def eSportCurrentSeason(self):
        return self.__eSportCurrentSeason

    @property
    def clanProfile(self):
        return self.__clanProfile

    @property
    def wgcg(self):
        return self.__wgcg

    @property
    def wgnp(self):
        return self.__wgnp

    @property
    def uiLogging(self):
        return self.__uiLogging

    @property
    def eula(self):
        return self.__eula

    @property
    def spgRedesignFeatures(self):
        return self.__spgRedesignFeatures

    @property
    def stronghold(self):
        return self.__strongholdSettings

    @property
    def tournament(self):
        return self.__tournamentSettings

    @property
    def frontline(self):
        return self.__frontlineSettings

    @property
    def bwHallOfFame(self):
        return self.__bwHallOfFame

    @property
    def rankedBattles(self):
        return self.__rankedBattlesSettings

    @property
    def exchangeRates(self):
        return self.__exchangeRatesConfig

    @property
    def epicMetaGame(self):
        return self.__epicMetaGameSettings

    @property
    def epicBattles(self):
        return self.__epicGameSettings

    @property
    def battleRoyale(self):
        return self.__battleRoyaleSettings

    @property
    def mapbox(self):
        return self.__mapboxSettings

    @property
    def unitAssemblerConfig(self):
        return self.__unitAssemblerConfig

    @property
    def telecomConfig(self):
        return self.__telecomConfig

    @property
    def blueprintsConfig(self):
        return self.__blueprintsConfig

    @property
    def squadPremiumBonus(self):
        return self.__squadPremiumBonus

    @property
    def vehiclePostProgression(self):
        return self.__vehiclePostProgressionConfig

    @property
    def eventBattlesConfig(self):
        return self.__eventBattlesConfig

    @property
    def giftSystemConfig(self):
        return self.__giftSystemConfig

    @property
    def playLimitsConfig(self):
        return self.__playLimitsConfig

    @property
    def battleMattersConfig(self):
        return self.__battleMattersConfig

    @property
    def peripheryRoutingConfig(self):
        return self.__peripheryRoutingConfig

    @property
    def personalReservesConfig(self):
        return self.__personalReservesConfig

    @property
    def preModerationConfig(self):
        return self.__preModerationConfig

    @property
    def collectionsConfig(self):
        return self.__collectionsConfig

    @property
    def winbackConfig(self):
        return self.__winbackConfig

    @property
    def limitedUIConfig(self):
        return self.__limitedUIConfig

    @property
    def prestigeConfig(self):
        return self.__prestigeConfig

    @property
    def prestigeMilestonesConfig(self):
        return self.__prestigeMilestonesConfig

    @property
    def steamShadeConfig(self):
        return self.__steamShadeConfig

    @property
    def abFeatureTestConfig(self):
        return self.__abFeatureTestConfig

    @property
    def referralProgramConfig(self):
        return self.__referralProgramConfig

    @property
    def liveOpsWebEventsConfig(self):
        return self.__liveOpsWebEventsConfig

    @property
    def advancedAchievementsConfig(self):
        return self.__advancedAchievementsConfig

    @property
    def ingameTournamentConfig(self):
        return self.__ingameTournamentConfig

    @property
    def w2gtConfig(self):
        return self.__w2gtConfig

    @property
    def challengesConfig(self):
        return self.__challengesConfig

    def isEpicBattleEnabled(self):
        return self.epicBattles.isEnabled

    def isPersonalMissionsEnabled(self, branch=None):
        if branch == PM_BRANCH.REGULAR:
            return self.__getGlobalSetting(b'isRegularQuestEnabled', True)
        if branch == PM_BRANCH.PERSONAL_MISSION_2:
            return self.__getGlobalSetting(b'isPM2QuestEnabled', True)
        if branch == PM_BRANCH.PERSONAL_MISSION_3:
            return self.__getGlobalSetting(b'isPM3QuestEnabled', True)
        return self.__getGlobalSetting(b'isRegularQuestEnabled', True) or self.__getGlobalSetting(b'isPM2QuestEnabled', True) or self.__getGlobalSetting(b'isPM3QuestEnabled', True)

    def isPMBattleProgressEnabled(self):
        return self.__getGlobalSetting(b'isPMBattleProgressEnabled', True)

    def getDisabledPMOperations(self):
        return self.__getGlobalSetting(b'disabledPMOperations', dict())

    def getDisabledPersonalMissions(self):
        return self.__getGlobalSetting(b'disabledPersonalMissions', dict())

    def isStrongholdsEnabled(self):
        return self.__getGlobalSetting(b'strongholdSettings', {}).get(b'isStrongholdsEnabled', False)

    def isTournamentEnabled(self):
        return self.__getGlobalSetting(b'tournamentSettings', {}).get(b'isTournamentEnabled', False)

    def isLeaguesEnabled(self):
        return self.__getGlobalSetting(b'strongholdSettings', {}).get(b'isLeaguesEnabled', False)

    def isElenEnabled(self):
        return self.__getGlobalSetting(b'elenSettings', {}).get(b'isElenEnabled', True)

    def elenUpdateInterval(self):
        return self.__getGlobalSetting(b'elenSettings', {}).get(b'elenUpdateInterval', 60)

    def isStorageEnabled(self):
        return self.__bwShop.isStorageEnabled

    def isLootBoxesEnabled(self):
        return self.__getGlobalSetting(b'isLootBoxesEnabled')

    def isMentoringLicenseEnabled(self):
        return self.__getGlobalSetting(b'isMentoringLicenseEnabled')

    def isAnonymizerEnabled(self):
        return self.__getGlobalSetting(b'isAnonymizerEnabled', False)

    def isSessionStatsEnabled(self):
        return self.__getGlobalSetting(b'sessionStats', {}).get(b'isSessionStatsEnabled', False)

    def isLinkWithHoFEnabled(self):
        return self.__getGlobalSetting(b'sessionStats', {}).get(b'isLinkWithHoFEnabled', False)

    def isWTREnabled(self):
        wtrSettings = self.__getGlobalSetting(b'sessionStats', {}).get(b'WTR', {})
        return wtrSettings.get(b'enabled', False)

    def isNationChangeEnabled(self):
        return self.__getGlobalSetting(b'isNationChangeEnabled', True)

    def getCrystalRewardConfig(self):
        return self.__crystalRewardsConfig

    @property
    def shop(self):
        return self.__bwShop

    @property
    def productCatalog(self):
        return self.__bwProductCatalog

    def isShopDataChangedInDiff(self, diff, fieldName=None):
        if b'shop' in diff:
            if fieldName is not None:
                if fieldName in diff[b'shop']:
                    return True
            else:
                return True
        return False

    def isBlueprintDataChangedInDiff(self, diff):
        return b'blueprints_config' in diff

    def isMapsTrainingEnabled(self):
        return self.__getGlobalSetting(b'isMapsTrainingEnabled', False)

    def recertificationFormState(self):
        return self.__getGlobalSetting(b'recertificationFormState', constants.SwitchState.DISABLED.value)

    def getLootBoxConfig(self):
        return self.__getGlobalSetting(b'lootBoxes_config', {})

    def getPiggyBankConfig(self):
        return self.__getGlobalSetting(PremiumConfigs.PIGGYBANK, {})

    def getAdditionalBonusConfig(self):
        return self.__getGlobalSetting(PremiumConfigs.DAILY_BONUS, {})

    def getPremQuestsConfig(self):
        return self.__getGlobalSetting(PremiumConfigs.PREM_QUESTS, {})

    def getDailyQuestConfig(self):
        return self.__getGlobalSetting(DAILY_QUESTS_CONFIG, {})

    def getDogTagsConfig(self):
        return self.__getGlobalSetting(DOG_TAGS_CONFIG, {})

    def getCustomizationQuestsConfig(self):
        return self.__getGlobalSetting(Configs.CUSTOMIZATION_QUESTS.value, {})

    def isDogTagEnabled(self):
        return self.__getGlobalSetting(DOG_TAGS_CONFIG, {}).get(b'enabled', True)

    def isHangarGeneralChatEnabled(self):
        return not self.__getGlobalSetting(constants.Configs.SYSTEM_CHANNELS.value, {}).get(b'disableHangarGeneralChat', False)

    def isChatEnabled(self):
        return not self.__getGlobalSetting(constants.Configs.SYSTEM_CHANNELS.value, {}).get(b'disableAllChats', False)

    def isDogTagCustomizationScreenEnabled(self):
        return self.isDogTagEnabled() and self.__getGlobalSetting(DOG_TAGS_CONFIG, {}).get(b'enableDogTagsCustomizationScreen', True)

    def isSkillComponentsEnabled(self):
        return self.isDogTagEnabled() and self.__getGlobalSetting(DOG_TAGS_CONFIG, {}).get(b'enableSkillComponents', True)

    def isDogTagInBattleEnabled(self):
        return self.isDogTagEnabled() and self.__getGlobalSetting(DOG_TAGS_CONFIG, {}).get(b'enableDogTagsInBattle', True)

    def isDogTagInPostBattleEnabled(self):
        return self.isDogTagEnabled() and self.__getGlobalSetting(DOG_TAGS_CONFIG, {}).get(b'enableDogTagsInPostBattle', True)

    def isDogTagComponentUnlockingEnabled(self):
        return self.isDogTagEnabled() and self.__getGlobalSetting(DOG_TAGS_CONFIG, {}).get(b'enableComponentUnlocking', True)

    def isDogTagsBattleMarkerEnabled(self):
        return self.isDogTagEnabled() and self.__getGlobalSetting(DOG_TAGS_CONFIG, {}).get(b'enableDogTagsBattleMarker', True)

    def getOptionalDevicesUsageConfig(self):
        return self.__getGlobalSetting(OPTIONAL_DEVICES_USAGE_CONFIG, {})

    def isTelecomRentalsEnabled(self):
        return self.__getGlobalSetting(TELECOM_RENTALS_CONFIG, {}).get(b'enabled', True)

    def isPlayerSubscriptionsEnabled(self):
        return self.__getGlobalSetting(PLAYER_SUBSCRIPTIONS_CONFIG, {}).get(b'enabled', True)

    def isPlayerSubscriptionsEntrypointHidden(self):
        return not self.isPlayerSubscriptionsEnabled() and self.__getGlobalSetting(PLAYER_SUBSCRIPTIONS_CONFIG, {}).get(b'hideEntrypoint', False)

    def isBattleNotifierEnabled(self):
        return self.__getGlobalSetting(BATTLE_NOTIFIER_CONFIG, {}).get(b'enabled', False)

    def isAutoSellCheckBoxEnabled(self):
        return self.getMiscGUISettings().get(b'buyModuleDialog', {}).get(b'enableAutoSellCheckBox', False)

    def isPhysicsSoundEnabled(self):
        return self.getMiscGUISettings().get(b'soundSettings', {}).get(b'physicsSoundEnabled', True)

    def getMiscGUISettings(self):
        return self.__getGlobalSetting(MISC_GUI_SETTINGS, {})

    def getMagneticAutoAimConfig(self):
        return self.__getGlobalSetting(MAGNETIC_AUTO_AIM_CONFIG, {})

    def getPreferredMapsConfig(self):
        return self.__getGlobalSetting(PremiumConfigs.PREFERRED_MAPS, {})

    def isEpicRandomEnabled(self):
        return self.__getGlobalSetting(b'isEpicRandomEnabled', False)

    def isEpicRandomAchievementsEnabled(self):
        return self.__getGlobalSetting(b'isEpicRandomAchievementsEnabled', False)

    def isEpicRandomMarkOfMasteryEnabled(self):
        return self.__getGlobalSetting(b'isEpicRandomMarkOfMasteryEnabled', False)

    def isEpicRandomMarksOnGunEnabled(self):
        return self.__getGlobalSetting(b'isEpicRandomMarksOnGunEnabled', False)

    def isCommandBattleEnabled(self):
        return self.__getGlobalSetting(b'isCommandBattleEnabled', False)

    def isHofEnabled(self):
        return self.__getGlobalSetting(b'hallOfFame', {}).get(b'isHofEnabled', False)

    def isMapsInDevelopmentEnabled(self):
        mapsInDevCongig = self.__getGlobalSetting(Configs.MAPS_IN_DEVELOPMENT_CONFIG.value, None)
        if mapsInDevCongig:
            return bool(mapsInDevCongig[b'isEnabled'])
        else:
            return False

    def getSquadRestrictions(self):
        return self.__getGlobalSetting(b'squadRestrictions', {})

    def getRandomMapsForDemonstrator(self):
        return self.__getGlobalSetting(b'randomMapsForDemonstrator', {})

    def getRandomBattleLevelsForDemonstrator(self):
        return self.__getGlobalSetting(b'randomBattleLevelsForDemonstrator', {})

    def isPremiumInPostBattleEnabled(self):
        return self.__getGlobalSetting(b'isPremiumInPostBattleEnabled', True)

    def isVehicleComparingEnabled(self):
        return bool(self.__getGlobalSetting(b'isVehiclesCompareEnabled', True))

    def isTankmanRestoreEnabled(self):
        return self.__getGlobalSetting(b'isTankmanRestoreEnabled', True)

    def isVehicleRestoreEnabled(self):
        return self.__getGlobalSetting(b'isVehicleRestoreEnabled', True)

    def isCustomizationEnabled(self):
        return self.__getGlobalSetting(b'isCustomizationEnabled', True)

    def getHeroVehicles(self):
        return self.__getGlobalSetting(b'hero_vehicles', {})

    def isManualEnabled(self):
        return self.__getGlobalSetting(b'isManualEnabled', False)

    def isFieldPostEnabled(self):
        return self.__getGlobalSetting(b'isFieldPostEnabled', True)

    def isPromoLoggingEnabled(self):
        return self.__getGlobalSetting(b'isPromoLoggingEnabled', False)

    def isReferralProgramEnabled(self):
        return self.__getGlobalSetting(b'isReferralProgramEnabled', False)

    def getPremiumXPBonus(self):
        return self.__getGlobalSetting(b'tankPremiumBonus', {}).get(b'xp', 0.5)

    def getPremiumCreditsBonus(self):
        return self.__getGlobalSetting(b'tankPremiumBonus', {}).get(b'credits', 0.5)

    def isPreferredMapsEnabled(self):
        return self.__getGlobalSetting(b'isPreferredMapsEnabled', False)

    def isGlobalMapEnabled(self):
        return self.__getGlobalSetting(b'isGlobalMapEnabled', False)

    def isBattleBoostersEnabled(self):
        return self.__getGlobalSetting(b'isBattleBoostersEnabled', False)

    def isCrewBooksPurchaseEnabled(self):
        return self.__getGlobalSetting(b'isCrewBooksPurchaseEnabled', False)

    def isCrewBooksSaleEnabled(self):
        return self.__getGlobalSetting(b'isCrewBooksSaleEnabled', False)

    def isJunkCrewConversionEnabled(self):
        return self.__getGlobalSetting(b'isJunkCrewConversionEnabled', False)

    def xppToConvert(self):
        return self.__getGlobalSetting(b'XppToConvert', 0)

    def rewardBookId(self):
        return self.__getGlobalSetting(b'rewardBookId', 0)

    def isTrophyDevicesEnabled(self):
        return self.__getGlobalSetting(b'isTrophyDevicesEnabled', False)

    def isTrainingBattleEnabled(self):
        return self.__getGlobalSetting(b'isTrainingBattleEnabled', False)

    def isCollectorVehicleEnabled(self):
        return self.__getGlobalSetting(CollectorVehicleConsts.CONFIG_NAME, {}).get(CollectorVehicleConsts.IS_ENABLED, False)

    def isOffersEnabled(self):
        return self.__getGlobalSetting(constants.OFFERS_ENABLED_KEY, False)

    def getProgressiveRewardConfig(self):
        return self.__progressiveReward

    def getMarathonConfig(self):
        return self.__getGlobalSetting(b'marathon_config', {})

    def getClansConfig(self):
        return self.__getGlobalSetting(ClansConfig.SECTION_NAME, {})

    def getSeniorityAwardsConfig(self):
        return self.__seniorityAwardsConfig

    def getEasyTankEquip(self):
        return self.__easyTankEquipConfig

    def getBattlePassConfig(self):
        return self.__battlePassConfig

    def getReactiveCommunicationConfig(self):
        return self.__reactiveCommunicationConfig

    def isLegacyModeSelectorEnabled(self):
        return self.__getGlobalSetting(b'isLegacyModeSelectorEnabled', False)

    def getBlueprintsConvertSaleConfig(self):
        return self.__blueprintsConvertSaleConfig

    def getActiveTestConfirmationConfig(self):
        return self.__getGlobalSetting(constants.ACTIVE_TEST_CONFIRMATION_CONFIG, {})

    def getTradeInConfig(self):
        return self.__getGlobalSetting(TRADE_IN_CONFIG_NAME, {})

    def getLootBoxSystemConfig(self):
        return self.__lootBoxSystemConfig

    def getAchievements20GeneralConfig(self):
        return Achievements20GeneralConfig(self.__getGlobalSetting(Configs.ACHIEVEMENTS20_CONFIG.value, {}))

    def getLootBoxesTooltipConfig(self):
        return self.__getGlobalSetting(Configs.LOOTBOXES_TOOLTIP_CONFIG.value, {})

    def getPetSystemConfig(self):
        return PetSystemServerSettings(self.__getGlobalSetting(PETS_SYSTEM_CONFIG, {}))

    def __getGlobalSetting(self, settingsName, default=None):
        return self.__serverSettings.get(settingsName, default)

    def __updateClanProfile(self, targetSettings):
        cProfile = targetSettings[b'clanProfile']
        self.__clanProfile = _ClanProfile(cProfile.get(b'isEnabled', False))
        return

    def __updateWgcg(self, targetSettings):
        cProfile = targetSettings[b'wgcg']
        self.__wgcg = _Wgcg(cProfile.get(b'isEnabled', False), cProfile.get(b'gateUrl', b''), cProfile.get(b'type', b'gateway'), cProfile.get(b'loginOnStart', False), cProfile.get(b'isJwtAuthorizationEnabled', True))
        return

    def __updateWgnp(self, targetSettings):
        cProfile = targetSettings[b'wgnp']
        self.__wgnp = _Wgnp(cProfile.get(b'enabled', False), cProfile.get(b'url', b''), cProfile.get(b'renameApiEnabled', False))
        return

    def __updateUILogging(self, targetSettings):
        settings = targetSettings[Configs.UI_LOGGING.value]
        self.__uiLogging = _UILogging(settings.get(b'enabled', False))
        return

    def __updateEULA(self, targetSettings):
        cProfile = targetSettings[b'eula_config']
        self.__eula = _EULA(cProfile.get(b'enabled', False), cProfile.get(b'demoAccEnabled', False), cProfile.get(b'steamAccEnabled', False))
        return

    def __updateExchangeRates(self, targetSettings):
        self.__exchangeRatesConfig = self.__exchangeRatesConfig.replace(targetSettings[b'exchange_rates_config'])
        return

    def __updateRanked(self, targetSettings):
        self.__rankedBattlesSettings = self.__rankedBattlesSettings.replace(targetSettings[b'ranked_config'])
        return

    def __updateEpic(self, targetSettings):
        self.__epicMetaGameSettings = self.__epicMetaGameSettings.replace(targetSettings[b'epic_config'].get(b'epicMetaGame', {}))
        self.__epicGameSettings = self.__epicGameSettings.replace(targetSettings[b'epic_config'])
        return

    def __updateUnitAssemblerConfig(self, targetSettings):
        config = targetSettings[Configs.UNIT_ASSEMBLER_CONFIG.value]
        self.__unitAssemblerConfig = self.__unitAssemblerConfig.replace(config)
        return

    def __updateSquadBonus(self, sourceSettings):
        self.__squadPremiumBonus = self.__squadPremiumBonus.replace(sourceSettings[PremiumConfigs.PREM_SQUAD])
        return

    def __updateShop(self, targetSettings):
        self.__bwShop = self.__bwShop.replace(targetSettings[b'shop'])
        return

    def __updateBattleRoyale(self, targetSettings):
        data = targetSettings[Configs.BATTLE_ROYALE_CONFIG.value]
        self.__battleRoyaleSettings = self.__battleRoyaleSettings.replace(data)
        return

    def __updateMapbox(self, targetSettings):
        self.__mapboxSettings = self.__mapboxSettings.replace(targetSettings[Configs.MAPBOX_CONFIG.value])
        return

    def __updateBlueprints(self, targetSettings):
        self.__blueprintsConfig = self.__blueprintsConfig._replace(**targetSettings)
        if self.__blueprintsConfig.isBlueprintModeChange(targetSettings):
            if not self.__blueprintsConfig.isEnabled or not self.__blueprintsConfig.useBlueprintsForUnlock:
                SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.BLUEPRINTS_SWITCH_OFF, type=SM_TYPE.Information, priority=b'medium')
            else:
                SystemMessages.pushI18nMessage(SYSTEM_MESSAGES.BLUEPRINTS_SWITCH_ON, type=SM_TYPE.Information, priority=b'medium')
        return

    def __updateProgressiveReward(self, targetSettings):
        self.__progressiveReward = self.__progressiveReward.replace(targetSettings[b'progressive_reward_config'])
        return

    def __updateSeniorityAwards(self, targetSettings):
        self.__seniorityAwardsConfig = self.__seniorityAwardsConfig.replace(targetSettings[Configs.SENIORITY_AWARDS_CONFIG.value])
        return

    def __updateReactiveCommunicationConfig(self, settings):
        if b'reactiveCommunicationConfig' in settings:
            config = settings[b'reactiveCommunicationConfig']
            if config is None:
                self.__reactiveCommunicationConfig = _ReactiveCommunicationConfig()
            elif isinstance(config, dict):
                self.__reactiveCommunicationConfig = _ReactiveCommunicationConfig(**config)
            else:
                _logger.error(b'Unexpected format of subscriptions service config: %r', config)
                self.__reactiveCommunicationConfig = _ReactiveCommunicationConfig()
        return

    def __updateBlueprintsConvertSaleConfig(self, targetSettings):
        if b'blueprints_convert_sale_config' in targetSettings:
            self.__blueprintsConvertSaleConfig = self.__blueprintsConvertSaleConfig.replace(targetSettings[b'blueprints_convert_sale_config'])
        return

    def __updateVehiclePostProgressionConfig(self, serverSettingsDiff):
        self.__vehiclePostProgressionConfig = self.__vehiclePostProgressionConfig.replace(serverSettingsDiff[post_progression_common.SERVER_SETTINGS_KEY])
        return

    def __updateEventBattles(self, targetSettings):
        self.__eventBattlesConfig = self.__eventBattlesConfig.replace(targetSettings[b'event_battles_config'])
        return

    def __updateGiftSystemConfig(self, serverSettingsDiff):
        self.__giftSystemConfig = self.__giftSystemConfig.replace({b'events': (serverSettingsDiff[Configs.GIFTS_CONFIG.value])})
        return

    def __updatePlayLimitsConfig(self, serverSettingsDiff):
        self.__playLimitsConfig = self.__playLimitsConfig.replace(serverSettingsDiff[Configs.PLAY_LIMITS_CONFIG.value])
        return

    def __updateBattleMatters(self, targetSettings):
        self.__battleMattersConfig = self.__battleMattersConfig.replace(targetSettings[Configs.BATTLE_MATTERS_CONFIG.value])
        return

    def __updatePeripheryRoutingConfig(self, diff):
        self.__peripheryRoutingConfig = self.__peripheryRoutingConfig.replace(diff[Configs.PERIPHERY_ROUTING_CONFIG.value])
        return

    def __updatePersonalReserves(self, serverSettingsDiff):
        if Configs.PERSONAL_RESERVES_CONFIG.value in serverSettingsDiff:
            self.__personalReservesConfig = self.__personalReservesConfig.replace(serverSettingsDiff[Configs.PERSONAL_RESERVES_CONFIG.value])
        return

    def __updatePreModerationConfig(self, serverSettingsDiff):
        if Configs.PRE_MODERATION_CONFIG.value in serverSettingsDiff:
            self.__preModerationConfig = self.__preModerationConfig.replace(serverSettingsDiff[Configs.PRE_MODERATION_CONFIG.value])
        return

    def __updateTournamentsConfig(self, diff):
        self.__tournamentSettings = self.__tournamentSettings.replace(diff[TOURNAMENT_CONFIG])
        return

    def __updateLootBoxSystemConfig(self, diff):
        self.__lootBoxSystemConfig = self.__lootBoxSystemConfig.replace(diff[LOOTBOX_SYSTEM_CONFIG])
        return

    def __updateLootBoxesTooltipConfig(self, settings):
        if Configs.LOOTBOXES_TOOLTIP_CONFIG.value in settings:
            self.__serverSettings[Configs.LOOTBOXES_TOOLTIP_CONFIG.value] = settings[Configs.LOOTBOXES_TOOLTIP_CONFIG.value]
        return

    def __updateCollectionsConfig(self, diff):
        self.__collectionsConfig = self.__collectionsConfig.replace(diff[Configs.COLLECTIONS_CONFIG.value])
        return

    def __updateWinbackConfig(self, diff):
        self.__winbackConfig = self.__winbackConfig.replace(diff[Configs.WINBACK_CONFIG.value])
        return

    def __updateLimitedUIConfig(self, serverSettingsDiff):
        if Configs.LIMITED_UI_CONFIG.value in serverSettingsDiff:
            self.__limitedUIConfig = self.__limitedUIConfig.replace(serverSettingsDiff[Configs.LIMITED_UI_CONFIG.value])
        return

    def __updateEasyTankEquipConfig(self, serverSettingsDiff):
        if Configs.EASY_TANK_EQUIP_CONFIG.value in serverSettingsDiff:
            self.__easyTankEquipConfig = self.__easyTankEquipConfig.replace(serverSettingsDiff[Configs.EASY_TANK_EQUIP_CONFIG.value])
        return

    def __updateSteamShadeConfig(self, serverSettingsDiff):
        if Configs.STEAM_SHADE_CONFIG.value in serverSettingsDiff:
            self.__steamShadeConfig = self.__steamShadeConfig.replace(serverSettingsDiff[Configs.STEAM_SHADE_CONFIG.value])
        return

    def __updatePrestigeMilestonesConfig(self, serverSettingsDiff):
        if Configs.PRESTIGE_MILESTONES_CONFIG.value in serverSettingsDiff:
            self.__serverSettings[Configs.PRESTIGE_MILESTONES_CONFIG.value] = serverSettingsDiff[Configs.PRESTIGE_MILESTONES_CONFIG.value]
            if Configs.PRESTIGE_MILESTONES_CONFIG.value in serverSettingsDiff:
                self.__prestigeMilestonesConfig = PrestigeMilestonesConfig(self.__serverSettings.get(Configs.PRESTIGE_MILESTONES_CONFIG.value, {}))
        return

    def __updateABFeatureTestConfig(self, serverSettingsDiff):
        if Configs.AB_FEATURE_TEST.value in serverSettingsDiff:
            self.__abFeatureTestConfig = self.__abFeatureTestConfig.replace(serverSettingsDiff[Configs.AB_FEATURE_TEST.value])
        return

    def __updateReferralProgramConfig(self, serverSettingsDiff):
        self.__referralProgramConfig = self.__referralProgramConfig.replace(serverSettingsDiff[Configs.REFERRAL_PROGRAM_CONFIG.value])
        return

    def __updateLiveOpsWebEventsConfig(self, serverSettingsDiff):
        self.__liveOpsWebEventsConfig = self.__liveOpsWebEventsConfig.replace(serverSettingsDiff[Configs.LIVE_OPS_EVENTS_CONFIG.value])
        return

    def __updateIngameTournamentConfig(self, serverSettingsDiff):
        self.__ingameTournamentConfig = self.__ingameTournamentConfig.replace(serverSettingsDiff[Configs.INGAME_TOURNAMENT_CONFIG.value])
        return

    def __updateAdvancedAchievementsConfig(self, serverSettingsDiff):
        if Configs.ADVANCED_ACHIEVEMENTS_CONFIG.value in serverSettingsDiff:
            self.__advancedAchievementsConfig = self.__advancedAchievementsConfig.replace(serverSettingsDiff[Configs.ADVANCED_ACHIEVEMENTS_CONFIG.value])
        return

    def __updateW2GTConfig(self, serverSettingsDiff):
        self.__w2gtConfig = self.__w2gtConfig.replace(serverSettingsDiff[Configs.W2GT_CONFIG.value])
        return


def serverSettingsChangeListener(*configKeys):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(self, diff):
            if any(configKey in diff for configKey in configKeys):
                func(self, diff)
                return True
            return False

        return wrapper

    return decorator
