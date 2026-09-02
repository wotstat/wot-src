import copy, functools, logging, types, urlparse
from collections import namedtuple
import typing, post_progression_common
from BonusCaps import BonusCapsConst
from Event import Event
from UnitBase import PREBATTLE_TYPE_TO_UNIT_ASSEMBLER, UNIT_ASSEMBLER_IMPL_TO_CONFIG
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS
from battle_pass_common import BATTLE_PASS_CONFIG_NAME, BattlePassConfig
from collections_common import CollectionsConfig
from collector_vehicle import CollectorVehicleConsts
from comp7_ranks_common import Comp7Division
from constants import BATTLE_NOTIFIER_CONFIG, ClansConfig, Configs, DAILY_QUESTS_CONFIG, DOG_TAGS_CONFIG, MAGNETIC_AUTO_AIM_CONFIG, MISC_GUI_SETTINGS, PremiumConfigs, RENEWABLE_SUBSCRIPTION_CONFIG, PLAYER_SUBSCRIPTIONS_CONFIG, TOURNAMENT_CONFIG, ARENA_BONUS_TYPE, ACTIVE_TEST_CONFIRMATION_CONFIG, OFFERS_ENABLED_KEY, SwitchState
from debug_utils import LOG_DEBUG, LOG_NOTE
from gifts.gifts_common import ClientReqStrategy, GiftEventID, GiftEventState
from supply_shared import Supply
from gui import GUI_SETTINGS, SystemMessages
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES
from gui.SystemMessages import SM_TYPE
from gui.shared.utils.decorators import ReprInjector
from helpers import time_utils
from items import vehicles
from personal_missions import PM_BRANCH
from post_progression_common import FEATURE_BY_GROUP_ID, ROLESLOT_FEATURE
from ranked_common import SwitchState as RankedSwitchState
from renewable_subscription_common.settings_constants import GOLD_RESERVE_GAINS_SECTION
from schema_manager import getSchemaManager
from shared_utils import makeTupleByDict, updateDict, findFirst
from soft_exception import SoftException
from telecom_rentals_common import TELECOM_RENTALS_CONFIG
from trade_in_common.constants_types import CONFIG_NAME as TRADE_IN_CONFIG_NAME
from achievements20.Achievements20GeneralConfig import Achievements20GeneralConfig
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, List, Sequence, Optional, Iterable, Tuple
    from dict2model.types import ModelType
    from base_schema_manager import GameParamsSchema
_logger = logging.getLogger(__name__)
_CLAN_EMBLEMS_SIZE_MAPPING = {16: b'clan_emblems_16', 
   32: b'clan_emblems_small', 
   64: b'clan_emblems_big', 
   128: b'clan_emblems_128', 
   256: b'clan_emblems_256'}

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
        return cls(0, 0, [])


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

    def getRewardScreensDescrsUrl(self, langID):
        if isinstance(langID, unicode):
            langID = str(langID)
        baseUrl = self.__getUrl(b'reward_screens_config')
        return urlparse.urljoin(baseUrl, (b'reward_screen_descr_{}.xml').format(langID))

    def getRewardScreenBackgroundUrl(self, decorName):
        baseUrl = self.__getUrl(b'reward_screens_config')
        return urlparse.urljoin(baseUrl, (b'background/{}').format(decorName))

    def getOffersRootUrl(self):
        return self.__getUrl(b'offers')

    def getGameLoadingConfigUrl(self):
        return self.__getUrl(b'game_loading_config')

    def getCollectionsContentConfigUrl(self):
        return self.__getUrl(b'collections_content_config')

    def getLobbyCdnContentBucketUrl(self):
        return self.__getUrl(b'lobby_cdn_config')

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


class _Clientgw(namedtuple(b'_Clientgw', (b'enabled', b'url', b'type', b'loginOnStart', b'isJwtAuthorizationEnabled'))):
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
 b'yearRewardState', b'leagueRewardEnabled', b'hasSpecialSeason',
 b'createVivoxTeamChannels', b'squadRankRestrictions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs={}, winnerRankChanges=(), loserRankChanges=(), minXP=0, unburnableRanks={}, unburnableStepRanks={}, minLevel=0, maxLevel=0, accRanks=0, accSteps=(), cycleFinishSeconds=0, primeTimes={}, seasons={}, cycleTimes=(), shields={}, divisions={}, bonusBattlesMultiplier=0, expectedSeasons=0, yearAwardsMarks=(), rankGroups=(), qualificationBattles=0, yearLBSize=0, leaguesBonusBattles=(), forbiddenClassTags=(), forbiddenVehTypes=(), shopState=RankedSwitchState.DISABLED, yearLBState=RankedSwitchState.DISABLED, yearRewardState=RankedSwitchState.ENABLED, leagueRewardEnabled=True, hasSpecialSeason=False, createVivoxTeamChannels=False, squadRankRestrictions={})
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

class _Milestone(namedtuple(b'_Milestone', (b'points', b'supplyType'))):

    def getSupplyTag(self):
        return Supply.SUPPLY_ID_TO_TAG[self.supplyType]


_TeamsProgressionConfig = namedtuple(b'_TeamsProgression', (b'attackersCfg', b'defendersCfg'))

class _TeamConfig(namedtuple(b'_TeamConfig', (b'milestones',))):

    @property
    def supplyTypes(self):
        return [milestone.supplyType for milestone in self.milestones]


class _SectorsProgression(namedtuple(b'_SectorsProgression', (b'config',))):

    def getConfig(self, sectorID):
        for sectors, teamsCfg in self.config.iteritems():
            if sectorID in sectors:
                return teamsCfg

        return

    def attackersSupplyTypes(self):
        if self.config:
            return next(self.config.itervalues()).attackersCfg.supplyTypes
        return []

    def defendersSupplyTypes(self):
        if self.config:
            return next(self.config.itervalues()).defendersCfg.supplyTypes
        return []


class _ReplaySectorsProgression(_SectorsProgression):

    def getConfig(self, sectorID):
        sectorID = str(sectorID)
        return super(_ReplaySectorsProgression, self).getConfig(sectorID)


class _EpicMetaGameConfig(settingsBlock(b'_EpicMetaGameConfig', (
 b'maxCombatReserveLevel', b'seasonData', b'metaLevel', b'rewards', b'defaultSlots', b'slots',
 b'inBattleReservesByRank', b'skipParamsValidation', b'destructibleTypeId', b'sectorsProgression',
 b'sectorsProgressionConfig', b'supplyParams'))):

    @classmethod
    def defaults(cls):
        return dict(maxCombatReserveLevel=0, seasonData=(
         0, False), metaLevel=(0, 0, 0), rewards={}, defaultSlots={}, slots={}, inBattleReservesByRank={}, skipParamsValidation=0, destructibleTypeId=0, sectorsProgression={}, sectorsProgressionConfig=cls.__getSectorsProgressionConfig({}), supplyParams={})

    @classmethod
    def _preprocessData(cls, data):
        sectorsProgressionConfig = data.get(b'sectorsProgression')
        if sectorsProgressionConfig is not None:
            config = {}
            for sectors, teamsCfg in sectorsProgressionConfig.iteritems():
                config[sectors] = _TeamsProgressionConfig(*[_TeamConfig([_Milestone(*milestone) for milestone in sorted(teamData, key=(lambda x: x[0]))]) for teamData in teamsCfg])

            data[b'sectorsProgressionConfig'] = cls.__getSectorsProgressionConfig(config)
        return data

    @classmethod
    def __getSectorsProgressionConfig(cls, data):
        import BattleReplay
        if not BattleReplay.isPlaying():
            return _SectorsProgression(data)
        return _ReplaySectorsProgression(data)


class EpicGameConfig(namedtuple(b'EpicGameConfig', (b'isEnabled', b'validVehicleLevels', b'battlePassDataEnabled', b'levelsToUpgrateAllReserves',
 b'seasons', b'cycleTimes', b'unlockableInBattleVehLevels', b'inBattleModifiers', b'peripheryIDs',
 b'primeTimes', b'rentVehicles', b'tooltips', b'forbiddenVehTypes'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, validVehicleLevels=[], battlePassDataEnabled=True, levelsToUpgrateAllReserves=[], unlockableInBattleVehLevels=[], inBattleModifiers={}, seasons={}, cycleTimes=(), peripheryIDs={}, primeTimes={}, rentVehicles=[], tooltips={}, forbiddenVehTypes=set())
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


class _UnitAssemblerConfig(namedtuple(b'_UnitAssemblerConfig', (b'squad', b'epic'))):
    __slots__ = ()

    def asDict(self):
        return self._asdict()

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
        return cls(squad={}, epic={})


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


class BattleRoyaleConfig(namedtuple(b'BattleRoyaleConfig', (b'isEnabled', b'peripheryIDs', b'unburnableTitles',
 b'eventProgression', b'primeTimes', b'seasons', b'cycleTimes',
 b'maps', b'battleXP', b'coneVisibility', b'loot', b'defaultAmmo',
 b'vehiclesSlotsConfig', b'economics', b'url', b'respawns', b'isShowTimeLeft',
 b'progressionTokenAward'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs={}, eventProgression={}, unburnableTitles=(), primeTimes={}, seasons={}, cycleTimes={}, maps=(), battleXP={}, coneVisibility={}, loot={}, defaultAmmo={}, vehiclesSlotsConfig={}, economics={}, url=b'', respawns={}, isShowTimeLeft=False, progressionTokenAward={})
        defaults.update(kwargs)
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
  b'endTime', int),
 (
  b'reminders', list),
 (
  b'clockOnNotification', int),
 (
  b'showRewardNotification', bool),
 (
  b'receivedRewardsToken', str),
 (
  b'rewardEligibilityToken', str),
 (
  b'claimRewardToken', str),
 (
  b'rewardQuestsPrefix', str)))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, endTime=0, reminders=[], clockOnNotification=0, showRewardNotification=False, receivedRewardsToken=b'', rewardEligibilityToken=b'', claimRewardToken=b'', rewardQuestsPrefix=b'')
        defaults.update(kwargs)
        return super(SeniorityAwardsConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class _AdventCalendarConfig(namedtuple(b'_AdventCalendarConfig', (b'calendarURL', b'popupIntervalInHours'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(calendarURL=b'', popupIntervalInHours=24)
        defaults.update(kwargs)
        return super(_AdventCalendarConfig, cls).__new__(cls, **defaults)

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


_crystalRewardInfo = namedtuple(b'_crystalRewardInfo', b'level, arenaType, winTop3, loseTop3, winTop10, loseTop10, topLength firstTopLength')
_crystalRewardComp7Info = namedtuple(b'_crystalRewardInfo', b'level, arenaType, winTop2, loseTop2, winTop5, loseTop5, winTop7, loseTop7, topLength firstTopLength')
_crystalRewardRankedInfo = namedtuple(b'_crystalRewardInfo', b'level, arenaType, winTop3, loseTop3, winTop7, loseTop7, winTop10, loseTop10, topLength firstTopLength')

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

    def getRewardInfoData(self):
        results = []
        for level, rewardData in self.rewards.level.iteritems():
            for arenaBonusType, scoreData in rewardData.iteritems():
                topWinRewards = list(scoreData[True].itervalues())
                winTop3 = max(topWinRewards)
                if arenaBonusType == ARENA_BONUS_TYPE.COMP7:
                    results.append(_crystalRewardComp7Info(level, arenaBonusType, winTop2=scoreData[True].get(1, 0), loseTop2=scoreData[False].get(1, 0), winTop5=scoreData[True].get(5, 0), loseTop5=scoreData[False].get(5, 0), winTop7=scoreData[True].get(7, 0), loseTop7=scoreData[False].get(7, 0), topLength=len(scoreData[True]), firstTopLength=topWinRewards.count(winTop3)))
                elif arenaBonusType == ARENA_BONUS_TYPE.RANKED:
                    results.append(_crystalRewardRankedInfo(level, arenaBonusType, winTop3=scoreData[True].get(1, 0), loseTop3=scoreData[False].get(1, 0), winTop7=scoreData[True].get(7, 0), loseTop7=scoreData[False].get(7, 0), winTop10=scoreData[True].get(10, 0), loseTop10=scoreData[False].get(10, 0), topLength=len(scoreData[True]), firstTopLength=topWinRewards.count(winTop3)))
                else:
                    results.append(_crystalRewardInfo(level, arenaBonusType, winTop3=winTop3, loseTop3=max(scoreData[False].itervalues()), winTop10=min(scoreData[True].itervalues()), loseTop10=min(scoreData[False].itervalues()), topLength=len(scoreData[True]), firstTopLength=topWinRewards.count(winTop3)))

        return results

    def isCrystalEarnPossible(self, arenaType):
        return findFirst((lambda item: item.arenaType == arenaType), self.getRewardInfoData(), None) is not None


class _ReactiveCommunicationConfig(object):
    __slots__ = (b'__isEnabled', b'__url')

    def __init__(self, **kwargs):
        super(_ReactiveCommunicationConfig, self).__init__()
        self.__isEnabled = kwargs.get(b'isEnabled', False)
        self.__url = kwargs.get(b'url', b'')
        if self.__isEnabled and not self.__url:
            _logger.error(b'Connection to web subscription service is enabled, but url is empty')
            self.__isEnabled = False
        return

    @property
    def isEnabled(self):
        return self.__isEnabled

    @property
    def url(self):
        return self.__url


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
 b'primeTimes', b'seasons', b'cycleTimes', b'levels', b'geometryIDs'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, peripheryIDs={}, forbiddenClassTags=set(), forbiddenVehTypes=set(), primeTimes={}, seasons={}, cycleTimes={}, levels=[], geometryIDs={}, progressionUpdateInterval=time_utils.ONE_MINUTE * 2)
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
        return cls(False, frozenset(), frozenset(), frozenset())

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
        return cls(GiftEventID.UNKNOWN, GiftEventState.DISABLED, [], ClientReqStrategy.AUTO)

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
        return cls({})

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        self.__packEventConfigs(dataToUpdate)
        return self._replace(**dataToUpdate)

    @classmethod
    def __packEventConfigs(cls, data):
        data[b'events'] = {eID: makeTupleByDict(GiftEventConfig, eData) for eID, eData in data[b'events'].iteritems()}
        return


class _WellRewardConfig(namedtuple(b'_WellRewardConfig', (b'bonus', b'limit', b'isSerial', b'sequence', b'rewardId'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(bonus={}, limit=0, isSerial=False, sequence=b'', rewardId=b'')
        defaults.update(kwargs)
        return super(_WellRewardConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()


class _ResourceConfig(namedtuple(b'_ResourceConfig', (b'name', b'rate', b'limit'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(name=b'', rate=0, limit=0)
        defaults.update(kwargs)
        return super(_ResourceConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()


class ResourceWellConfig(namedtuple(b'_ResourceWellConfig', (
 b'isEnabled', b'season', b'finishTime', b'remindTime', b'rewards', b'points', b'resources', b'startTime'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, season=0, finishTime=0, remindTime=0, rewards={}, points=0, resources={}, startTime=0)
        defaults.update(kwargs)
        cls.__packResourceConfigs(defaults)
        cls.__packRewardsConfigs(defaults)
        return super(ResourceWellConfig, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        self.__packResourceConfigs(dataToUpdate)
        self.__packRewardsConfigs(dataToUpdate)
        return self._replace(**dataToUpdate)

    @classmethod
    def __packResourceConfigs(cls, data):
        resources = {}
        for resourceType, resourceConfig in data[b'resources'].iteritems():
            resources[resourceType] = {name: _ResourceConfig(name=name, rate=resourceData.get(b'rate'), limit=resourceData.get(b'limit')) for name, resourceData in resourceConfig.iteritems()}

        data[b'resources'] = resources
        return

    @classmethod
    def __packRewardsConfigs(cls, data):
        data[b'rewards'] = {rewardId: makeTupleByDict(_WellRewardConfig, reward) for rewardId, reward in data[b'rewards'].iteritems()}
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


class _CollectiveGoalEntryPointConfig(namedtuple(b'_CollectiveGoalConfig', (
 b'isEnabled',
 b'startTime',
 b'finishTime',
 b'marathonPrefix',
 b'hermodChannelName',
 b'marathonName',
 b'goalType',
 b'goalDescription',
 b'rulesCaption'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, startTime=None, finishTime=None, marathonPrefix=None, hermodChannelName=None, marathonName=None, goalType=None, goalDescription=None, rulesCaption=None)
        defaults.update(kwargs)
        return super(_CollectiveGoalEntryPointConfig, cls).__new__(cls, **defaults)

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _BlackMarketConfig(namedtuple(b'_BlackMarketConfig', (
 b'isEnabled',
 b'isPaused',
 b'startTime',
 b'finishTime',
 b'lootboxSchedule',
 b'offerLaunchSchedule'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, isPaused=False, startTime=None, finishTime=None, lootboxSchedule={}, offerLaunchSchedule=[])
        defaults.update(kwargs)
        return super(_BlackMarketConfig, cls).__new__(cls, **defaults)

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _IngameBrowserEventConfig(namedtuple(b'_IngameBrowserEventConfig', (
 b'isEnabled',
 b'startTime',
 b'finishTime',
 b'url',
 b'secondaryUrl'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, startTime=None, finishTime=None, url=None, secondaryUrl=None)
        defaults.update(kwargs)
        return super(_IngameBrowserEventConfig, cls).__new__(cls, **defaults)

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _CollectiveGoalMarathonsConfig(namedtuple(b'_CollectiveGoalMarathonsConfig', (
 b'isEnabled',
 b'startTime',
 b'finishTime',
 b'url',
 b'eventName'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, startTime=None, finishTime=None, url=None, eventName=None)
        defaults.update(kwargs)
        return super(_CollectiveGoalMarathonsConfig, cls).__new__(cls, **defaults)

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
        return cls({})

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)


class _Comp7QualificationConfig(settingsBlock(b'_Comp7QualificationConfig', (b'battlesNumber',))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return {b'battlesNumber': 0}


class Comp7Config(settingsBlock(b'Comp7Config', (
 b'isEnabled',
 b'isTournamentEnabled',
 b'peripheryIDs',
 b'primeTimes',
 b'seasons',
 b'cycleTimes',
 b'numPlayers',
 b'levels',
 b'forbiddenClassTags',
 b'forbiddenVehTypes',
 b'squadRatingRestriction',
 b'squadSizes',
 b'createVivoxTeamChannels',
 b'qualification'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return dict(isEnabled=False, isTournamentEnabled=False, peripheryIDs={}, primeTimes={}, seasons={}, cycleTimes={}, numPlayers=7, levels=[], forbiddenClassTags=set(), forbiddenVehTypes=set(), squadRatingRestriction={}, squadSizes=[], createVivoxTeamChannels=False, qualification=makeTupleByDict(_Comp7QualificationConfig, {}))

    @classmethod
    def _preprocessData(cls, data):
        qualificationConfig = data.get(b'qualification')
        if qualificationConfig is not None:
            data[b'qualification'] = makeTupleByDict(_Comp7QualificationConfig, qualificationConfig)
        return data


class Comp7RanksConfig(settingsBlock(b'Comp7RanksConfig', (
 b'ranks',
 b'ranksOrder',
 b'eliteRankPercent',
 b'divisionsByRank',
 b'divisions',
 b'rankInactivityNotificationThreshold'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return dict(ranks={}, ranksOrder=(), eliteRankPercent=0, divisionsByRank={}, divisions=(), rankInactivityNotificationThreshold=0)

    @classmethod
    def _preprocessData(cls, data):
        divisions = data.get(b'divisions')
        if divisions:
            data[b'divisions'] = cls.__dictDivisionsToComp7Divisions(divisions)
        divisionsByRank = data.get(b'divisionsByRank')
        if divisionsByRank:
            for rankID, divisions in divisionsByRank.iteritems():
                data[b'divisionsByRank'][rankID] = cls.__dictDivisionsToComp7Divisions(divisions)

        return data

    @classmethod
    def __dictDivisionsToComp7Divisions(cls, divisionsList):
        divs = []
        for dvsnDict in divisionsList:
            comp7Division = Comp7Division(dvsnDict)
            divs.append(comp7Division)

        return tuple(divs)


class Comp7RewardsConfig(settingsBlock(b'Comp7RewardsConfig', (
 b'main',
 b'extra'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return {b'main': [], b'extra': []}


class Comp7SkillsConfig(settingsBlock(b'Comp7SkillsConfig', (
 b'balanceVersion',
 b'roleEquipments'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return dict(balanceVersion=0, roleEquipments={})


class BattleModifiersConfig(settingsBlock(b'BattleModifiersConfig', (
 b'isEnabled',
 b'fortBattle_10',
 b'sortie_10',
 b'sortie_9',
 b'sortie_8',
 b'sortie_7',
 b'sortie_6',
 b'global_map',
 b'comp7'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return dict(isEnabled=False, fortBattle_10=(), sortie_10=(), sortie_9=(), sortie_8=(), sortie_7=(), sortie_6=(), global_map=(), comp7=())


class WinbackConfig(namedtuple(b'WinbackConfig', (
 b'isEnabled',
 b'versusAIIsDefaultModeToken',
 b'defaultProgression',
 b'progressions'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, versusAIIsDefaultModeToken=b'', defaultProgression=b'', progressions={})
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


GUI_LOOT_BOXES_CONFIG = b'gui_loot_boxes_config'

class _GuiLootBoxesConfig(object):
    __slots__ = (b'__isEnabled', b'__lootBoxBuyDayLimit', b'__isBuyAvailable', b'__shopCategoryUrl', b'__isShowStatistic')

    def __init__(self, **kwargs):
        super(_GuiLootBoxesConfig, self).__init__()
        self.__isEnabled = kwargs.get(b'enabled', False)
        self.__lootBoxBuyDayLimit = kwargs.get(b'lootBoxBuyDayLimit', 0)
        self.__isBuyAvailable = kwargs.get(b'isBuyAvailable', False)
        self.__isShowStatistic = kwargs.get(b'isShowStatistic', False)
        self.__shopCategoryUrl = kwargs.get(b'shopCategoryUrl', b'')
        return

    @property
    def isEnabled(self):
        return self.__isEnabled

    @property
    def lootBoxBuyDayLimit(self):
        return self.__lootBoxBuyDayLimit

    @property
    def isBuyAvailable(self):
        return self.__isBuyAvailable

    def getShopCategoryUrl(self):
        return self.__shopCategoryUrl


class ArmoryYardConfig(namedtuple(b'ArmoryYardConfig', (
 b'isEnabled', b'isPaused', b'seasons', b'animations', b'cycleTimes', b'tokenBase', b'receivedRewardTokenPostfix',
 b'stageTokenPostfix', b'currencyTokenPostfix', b'tokenCost', b'rewards', b'introVideoLink', b'infoPageLink',
 b'announcementCountdown', b'starterPacks', b'purchaseStage', b'shop',
 b'rerollSubsection', b'seasonsConfig', b'postProgression'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, isPaused=False, seasons={}, animations={}, cycleTimes={}, tokenBase=b'', receivedRewardTokenPostfix=b'', stageTokenPostfix=b'', currencyTokenPostfix=b'', tokenCost={}, rewards={}, introVideoLink=b'', infoPageLink=b'', announcementCountdown=0, starterPacks={}, purchaseStage={}, shop={}, rerollSubsection={}, seasonsConfig={}, postProgression={})
        defaults.update(kwargs)
        return super(ArmoryYardConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()

    @property
    def rerollPrices(self):
        return self.rerollSubsection.get(b'rerollPrices', {})

    def getDefaultConditionByQuestID(self, groupName, questID):
        return findFirst((lambda d: d[0] == questID), self.rerollSubsection.get(b'defaultQuests', {}).get(groupName, []), (None, None))[1]

    def iterByDefaultRerollQuests(self):
        for data in self.rerollSubsection.get(b'defaultQuests', {}).itervalues():
            for tokenQuestID, conditionID in data:
                yield (
                 tokenQuestID, conditionID)

        return


class _LimitedUIConfig(namedtuple(b'_LimitedUIConfig', (b'enabled', b'rules'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, rules=[])
        defaults.update(kwargs)
        return super(_LimitedUIConfig, cls).__new__(cls, **defaults)

    def hasRules(self):
        return bool(self.rules)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class RPConfig(namedtuple(b'RPConfig', (
 b'messageBarGUIEnabled',
 b'pgbCapacity',
 b'pgbDayLimit'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(messageBarGUIEnabled=True, pgbCapacity=0, pgbDayLimit=0)
        defaults.update(kwargs)
        return super(RPConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class RestoreConfig(namedtuple(b'RestoreConfig', (b'tankmen', b'vehicles'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(tankmen={}, vehicles={})
        defaults.update(kwargs)
        return super(RestoreConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class VersusAIConfig(namedtuple(b'VersusAIConfig', (b'isEnabled', b'isDefaultModeForNoob', b'levels', b'forbiddenVehicleTags'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, isDefaultModeForNoob=False, levels=tuple(), forbiddenVehicleTags=set())
        defaults.update(kwargs)
        return super(VersusAIConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class DebutBoxesConfig(namedtuple(b'DebutBoxesConfig', (b'isEnabled', b'startDate', b'endDate', b'infoPageUrl', b'questIDs'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, startDate=0, endDate=0, infoPageUrl=b'', questIDs=[])
        defaults.update(kwargs)
        return super(DebutBoxesConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class EarlyAccessConfig(namedtuple(b'EarlyAccessConfig', (b'isEnabled', b'isPaused', b'infoPageLink', b'seasons'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, isPaused=False, infoPageLink=b'', seasons={})
        defaults.update(kwargs)
        return super(EarlyAccessConfig, cls).__new__(cls, **defaults)

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    def getAffectedVehicles(self, seasonID):
        return self.seasons.get(seasonID, {}).get(b'affectedVehicles', {})

    def getBlockedVehicles(self, seasonID):
        return self.seasons.get(seasonID, {}).get(b'blockedVehicles', set())

    def getTokenCompensation(self, seasonID):
        return self.seasons.get(seasonID, {}).get(b'tokenCompensation', {})

    def getTokenCost(self, seasonID):
        return self.seasons.get(seasonID, {}).get(b'tokenCost', {})


class RandomBattlesConfig(namedtuple(b'RandomBattlesConfig', (b'isEnabled', b'levels'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, levels=tuple())
        defaults.update(kwargs)
        return super(RandomBattlesConfig, cls).__new__(cls, **defaults)

    def getLevels(self):
        return self.levels

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class ModeSelectorConfig(namedtuple(b'ModeSelectorConfig', b'columnSettings')):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(columnSettings={})
        defaults.update(kwargs)
        return super(ModeSelectorConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()

    def isValid(self):
        if not isinstance(self.columnSettings, dict):
            return False
        if not all(isinstance(k, int) for k in self.columnSettings.keys()):
            return False
        if not all(isinstance(v, (tuple, list)) and len(v) == 2 and all(isinstance(i, int) for i in v) for v in self.columnSettings.values()):
            return False
        return True


class _ParagonsDefaultResetVehicleConfig(namedtuple(b'_ParagonsDefaultResetVehicleConfig', (
 b'level',
 b'resetBonusBlueprintsCount',
 b'progressPointsAmount',
 b'progressPointsMultiplier',
 b'firstUnlockPoints'))):
    pass


class _ParagonsResetVehicleConfig(namedtuple(b'_ParagonsResetVehicleConfig', (
 b'compactDescr',
 b'resetBranchId',
 b'resetBonusBlueprintsCount',
 b'progressPointsAmount',
 b'progressPointsMultiplier',
 b'firstUnlockPoints'))):
    pass


class _ParagonsResetBranchConfig(object):
    __slots__ = (b'__data', b'__resetVehicles', b'__id')

    def __init__(self, branchId, data):
        self.__id = branchId
        self.__data = data
        self.__resetVehicles = None
        return

    @property
    def id(self):
        return self.__id

    @property
    def resetVehicles(self):
        if self.__resetVehicles is None:
            self.__resetVehicles = {vehicleCd: _ParagonsResetVehicleConfig(compactDescr=vehicleCd, resetBranchId=self.id, resetBonusBlueprintsCount=vehicleConfig[0], progressPointsAmount=vehicleConfig[1], progressPointsMultiplier=vehicleConfig[2], firstUnlockPoints=vehicleConfig[3]) for vehicleCd, vehicleConfig in self.__data.items()}
        return self.__resetVehicles

    def getVehicleToResetConfig(self, vehicleCd):
        return self.resetVehicles.get(vehicleCd)


class ParagonsConfig(object):
    __slots__ = (b'__data', b'__resetBranches', b'__resetVehicles', b'__defaultResetVehicleConfigs', b'__expandedResetBranchesConfig', b'__defaultSelectedRewardOrder')

    def __init__(self, data):
        self.__data = data
        self.__resetBranches = None
        self.__resetVehicles = None
        self.__defaultResetVehicleConfigs = None
        self.__expandedResetBranchesConfig = None
        self.__defaultSelectedRewardOrder = None
        return

    @property
    def data(self):
        return self.__data

    @property
    def isEnabled(self):
        return self.__data[b'isEnabled']

    @property
    def isPaused(self):
        return self.__data.get(b'isPaused', False)

    @property
    def accessCondition(self):
        return self.__data[b'accessCondition']

    @property
    def restrictions(self):
        return self.__data[b'restrictions']

    @property
    def minUnlockXLevelVehiclesCount(self):
        return self.accessCondition.get(b'minUnlockXLevelVehiclesCount', 0)

    @property
    def maxResetBranchesCount(self):
        return self.restrictions.get(b'maxResetBranchesCount', 0)

    @property
    def resetBranches(self):
        if self.__resetBranches is None:
            self.__expandResetBranchesConfig()
            self.__resetBranches = {branchId: _ParagonsResetBranchConfig(branchId, branchConfig) for branchId, branchConfig in self.__expandedResetBranchesConfig.items()}
        return self.__resetBranches

    @property
    def defaultResetVehicleConfigs(self):
        if self.__defaultResetVehicleConfigs is None:
            self.__defaultResetVehicleConfigs = {vehicleLevel: _ParagonsDefaultResetVehicleConfig(vehicleLevel, *defaultVehicleConfig) for vehicleLevel, defaultVehicleConfig in self.__data[b'paragonsResetBranches'][b'default'].iteritems()}
        return self.__defaultResetVehicleConfigs

    @property
    def defaultSelectedRewardOrder(self):
        if self.__defaultSelectedRewardOrder is None:
            self.__defaultSelectedRewardOrder = []
            for chapterID in sorted(self.rewards.keys()):
                for levelID in sorted(self.getChapterLevelIDs(chapterID)):
                    for entCode in self.getRewardsByChapterAndLevel(chapterID, levelID).get(b'entitlements', {}).keys():
                        self.__defaultSelectedRewardOrder.append((chapterID, levelID, entCode))

        return self.__defaultSelectedRewardOrder

    @property
    def resetVehicles(self):
        if self.__resetVehicles is None:
            self.__resetVehicles = {}
            for resetBranch in self.resetBranches.values():
                self.__resetVehicles.update(resetBranch.resetVehicles)

        return self.__resetVehicles

    @property
    def rewards(self):
        return self.__data[b'rewards']

    @property
    def paragonsUnlocks(self):
        return self.__data[b'paragonsUnlocks']

    def isParagonsUnlockEnabled(self, paragonsUnlockID):
        return self.paragonsUnlocks.get(paragonsUnlockID, {}).get(b'enabled', False)

    def getParagonsUnlockNationName(self, paragonsUnlockID):
        return self.paragonsUnlocks.get(paragonsUnlockID, {}).get(b'nationName')

    def getParagonsUnlockVehicles(self, paragonsUnlockID):
        return self.paragonsUnlocks.get(paragonsUnlockID, {}).get(b'lockedItemsByItemTypeName', {}).get(b'vehicle', set())

    def getRewardsByChapterAndLevel(self, chapterID, levelID):
        return self.rewards.get(chapterID, {}).get(b'levels', {}).get(levelID, {}).get(b'bonus', {})

    def getAnnouncementChapterIDs(self):
        return {chapterID for chapterID in self.rewards.iterkeys() if self.rewards.get(chapterID).get(b'isAnnouncement')}

    def getChapterIDs(self):
        return set(self.rewards.keys())

    def getChapterLevelIDs(self, chapterID):
        return set(self.rewards.get(chapterID).get(b'levels').keys())

    def getChapterCloseoutTimeStamp(self, chapterID):
        return self.rewards.get(chapterID, {}).get(b'closeoutDate', 0)

    def getParagonsCoinsAmountForLevelUnlock(self, chapterID, levelID):
        return self.rewards.get(chapterID).get(b'levels').get(levelID).get(b'paragonsCoin')

    def getResetBranchConfig(self, branchId):
        return self.resetBranches.get(branchId)

    def getResetVehicleConfig(self, vehicleCd):
        return self.resetVehicles.get(vehicleCd)

    def getBranchCompleteBonus(self):
        return self.__data.get(b'branchCompleteBonus', {}).get(b'paragonsCoins', 0)

    def getCoinsForBranchReset(self):
        return self.__data[b'paragonsCoinsForReset']

    def getBranchCompleteBonusLimit(self):
        return self.__data.get(b'branchCompleteBonus', {}).get(b'limit', 0)

    def replace(self, data):
        self.__data = data
        self.__resetBranches = None
        self.__resetVehicles = None
        self.__defaultResetVehicleConfigs = None
        self.__expandedResetBranchesConfig = None
        return self

    @classmethod
    def defaults(cls):
        return cls({b'isEnabled': False, 
           b'accessCondition': {}, b'restrictions': {}, b'paragonsResetBranches': {}, b'paragonsUnlocks': {}, b'rewards': {}})

    def __expandResetBranchesConfig(self):
        paragonsResetBranches = self.__data[b'paragonsResetBranches']
        vehiclesConfigValues = paragonsResetBranches.get(b'vehicles', {})
        data = {}
        cachedParagonBranchesCollection = vehicles.g_cache.paragonsBranchesToReset.branches
        for branchID, branch in cachedParagonBranchesCollection.items():
            resetVehiclesCDs = branch.resetVehicles
            data[branchID] = self.__getResetVehiclesValues(resetVehiclesCDs, vehiclesConfigValues, paragonsResetBranches[b'default'])

        self.__expandedResetBranchesConfig = data
        return

    def __getResetVehiclesValues(self, resetVehiclesCDs, vehiclesConfigValues, defaultConfigValues):
        result = {}
        for vehicleCD in resetVehiclesCDs:
            vehicleLevel = vehicles.getItemByCompactDescr(vehicleCD).level
            defaultValues = defaultConfigValues[vehicleLevel]
            vehicleValues = vehiclesConfigValues.get(vehicleCD)
            if vehicleValues is None:
                result[vehicleCD] = defaultValues
            else:
                result[vehicleCD] = self.__mergeConfigValues(vehicleValues, defaultValues)

        return result

    def __mergeConfigValues(self, vehicleValues, defaultValues):
        return tuple(defaultValue if vehicleValues[idx] is None else vehicleValues[idx] for idx, defaultValue in enumerate(defaultValues))


class _LootBoxStatisticsConfig(namedtuple(b'_LootBoxStatisticsConfig', (b'enabled',))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False)
        defaults.update(kwargs)
        return super(_LootBoxStatisticsConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _BattleContextHintsConfig(namedtuple(b'_BattleContextHintsConfig', (b'enabled', b'hints'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, hints={})
        defaults.update(kwargs)
        return super(_BattleContextHintsConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _SettingsLoggingConfig(namedtuple(b'_SettingsLoggingConfig', (
 b'isEnabled',
 b'logChangesPerSession'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, logChangesPerSession=False)
        defaults.update(kwargs)
        return super(_SettingsLoggingConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _ControlPointOverrideConfig(namedtuple(b'_ControlPointOverrideConfig', (
 b'isEnabled',
 b'flagPath',
 b'flagstaffPath',
 b'wweventName'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, flagPath=b'', flagstaffPath=b'', wweventName=b'')
        defaults.update(kwargs)
        return super(_ControlPointOverrideConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _NewbieStartPageConfig(namedtuple(b'NewbieStartPageConfig', (b'isEnabled',))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False)
        defaults.update(kwargs)
        return super(_NewbieStartPageConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _StallConfig(namedtuple(b'StallConfig', (b'isEnabled', b'products'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(isEnabled=False, products={})
        defaults.update(kwargs)
        return super(_StallConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class _NewbieChatLockConfig(namedtuple(b'_NewbieChatLockConfig', (b'enabled', b'battlesCountThreshold', b'vehicleLevelThreshold'))):
    __slots__ = ()

    def __new__(cls, **kwargs):
        defaults = dict(enabled=False, battlesCountThreshold=0, vehicleLevelThreshold=0)
        defaults.update(kwargs)
        return super(_NewbieChatLockConfig, cls).__new__(cls, **defaults)

    def asDict(self):
        return self._asdict()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        return self._replace(**dataToUpdate)

    @classmethod
    def defaults(cls):
        return cls()


class ServerSettings(object):

    def __init__(self, serverSettings):
        self.onServerSettingsChange = Event()
        self.__serverSettings = {}
        self.__roamingSettings = RoamingSettings.defaults()
        self.__fileServerSettings = _FileServerSettings.defaults()
        self.__regionalSettings = _RegionalSettings.defaults()
        self.__eSportCurrentSeason = _ESportCurrentSeason.defaults()
        self.__clientgw = _Clientgw.defaults()
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
        self.__adventCalendar = _AdventCalendarConfig()
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
        self.__resourceWellConfig = ResourceWellConfig()
        self.__battleMattersConfig = _BattleMattersConfig()
        self.__collectiveGoalEntryPointConfig = _CollectiveGoalEntryPointConfig()
        self.__collectiveGoalMarathonsConfig = _CollectiveGoalMarathonsConfig()
        self.__peripheryRoutingConfig = PeripheryRoutingConfig()
        self.__comp7Config = Comp7Config()
        self.__battleModifiersConfig = BattleModifiersConfig()
        self.__comp7RanksConfig = Comp7RanksConfig()
        self.__comp7RewardsConfig = Comp7RewardsConfig()
        self.__comp7SkillsConfig = Comp7SkillsConfig()
        self.__personalReservesConfig = PersonalReservesConfig()
        self.__playLimitsConfig = PlayLimitsConfig()
        self.__preModerationConfig = PreModerationConfig()
        self.__guiLootBoxesConfig = _GuiLootBoxesConfig()
        self.__collectionsConfig = CollectionsConfig()
        self.__winbackConfig = WinbackConfig()
        self.__limitedUIConfig = _LimitedUIConfig()
        self.__referralProgramConfig = RPConfig()
        self.__restoreConfig = RestoreConfig()
        self.__versusAISettings = VersusAIConfig()
        self.__debutBoxesConfig = DebutBoxesConfig()
        self.__earlyAccessConfig = EarlyAccessConfig()
        self.__armoryYardSettings = ArmoryYardConfig.defaults()
        self.__randomBattlesConfig = RandomBattlesConfig()
        self.__modeSelectorConfig = ModeSelectorConfig()
        self.__paragonsConfig = ParagonsConfig.defaults()
        self.__blackMarketConfig = _BlackMarketConfig()
        self.__ingameBrowserEventConfig = _IngameBrowserEventConfig()
        self.__lootBoxStatisticsConfig = _LootBoxStatisticsConfig.defaults()
        self.__battleContextHintsConfig = _BattleContextHintsConfig.defaults()
        self.__settingsLoggingConfig = _SettingsLoggingConfig()
        self.__controlPointConfig = _ControlPointOverrideConfig.defaults()
        self.__newbieStartPageConfig = _NewbieStartPageConfig()
        self.__stallConfig = _StallConfig()
        self.__newbieChatLockConfig = _NewbieChatLockConfig()
        self.__schemaManager = getSchemaManager()
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

        if b'clientgw' in self.__serverSettings:
            self.__updateClientgw(self.__serverSettings)
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
        if b'advent_calendar_config' in self.__serverSettings:
            self.__adventCalendar = makeTupleByDict(_AdventCalendarConfig, self.__serverSettings[b'advent_calendar_config'])
        if b'epic_config' in self.__serverSettings:
            LOG_DEBUG(b'epic_config', self.__serverSettings[b'epic_config'])
            self.__epicMetaGameSettings = makeTupleByDict(_EpicMetaGameConfig, self.__serverSettings[b'epic_config'][b'epicMetaGame'])
            self.__epicGameSettings = makeTupleByDict(EpicGameConfig, self.__serverSettings[b'epic_config'])
        if b'unit_assembler_config' in self.__serverSettings:
            self.__unitAssemblerConfig = makeTupleByDict(_UnitAssemblerConfig, self.__serverSettings[b'unit_assembler_config'])
        if PremiumConfigs.PREM_SQUAD in self.__serverSettings:
            self.__squadPremiumBonus = _SquadPremiumBonus.create(self.__serverSettings[PremiumConfigs.PREM_SQUAD])
        if Configs.BATTLE_ROYALE_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(b'battle_royale_config', self.__serverSettings[Configs.BATTLE_ROYALE_CONFIG.value])
            self.__battleRoyaleSettings = makeTupleByDict(BattleRoyaleConfig, self.__serverSettings[Configs.BATTLE_ROYALE_CONFIG.value])
        else:
            self.__battleRoyaleSettings = BattleRoyaleConfig.defaults()
        if Configs.VERSUS_AI_CONFIG.value in self.__serverSettings:
            self.__versusAISettings = makeTupleByDict(VersusAIConfig, self.__serverSettings[Configs.VERSUS_AI_CONFIG.value])
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
        if b'seniority_awards_config' in self.__serverSettings:
            self.__seniorityAwardsConfig = makeTupleByDict(SeniorityAwardsConfig, self.__serverSettings[b'seniority_awards_config'])
        else:
            self.__seniorityAwardsConfig = SeniorityAwardsConfig()
        if BATTLE_PASS_CONFIG_NAME in self.__serverSettings:
            self.__battlePassConfig = BattlePassConfig(self.__serverSettings.get(BATTLE_PASS_CONFIG_NAME, {}))
        else:
            self.__battlePassConfig = BattlePassConfig({})
        if _crystalRewardsConfig.CONFIG_NAME in self.__serverSettings:
            self.__crystalRewardsConfig = makeTupleByDict(_crystalRewardsConfig, self.__serverSettings[_crystalRewardsConfig.CONFIG_NAME])
        self.__updateReactiveCommunicationConfig(self.__serverSettings)
        self.__updateGuiLootBoxesConfig(self.__serverSettings)
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
        if Configs.RESOURCE_WELL.value in self.__serverSettings:
            self.__resourceWellConfig = makeTupleByDict(ResourceWellConfig, self.__serverSettings[Configs.RESOURCE_WELL.value])
        if Configs.BATTLE_MATTERS_CONFIG.value in self.__serverSettings:
            self.__battleMattersConfig = makeTupleByDict(_BattleMattersConfig, self.__serverSettings[Configs.BATTLE_MATTERS_CONFIG.value])
        if Configs.COLLECTIVE_GOAL_ENTRY_POINT_CONFIG.value in self.__serverSettings:
            self.__collectiveGoalEntryPointConfig = makeTupleByDict(_CollectiveGoalEntryPointConfig, self.__serverSettings[Configs.COLLECTIVE_GOAL_ENTRY_POINT_CONFIG.value])
        if Configs.BLACK_MARKET_CONFIG.value in self.__serverSettings:
            self.__blackMarketConfig = makeTupleByDict(_BlackMarketConfig, self.__serverSettings[Configs.BLACK_MARKET_CONFIG.value])
        if Configs.INGAME_BROWSER_EVENT_CONFIG.value in self.__serverSettings:
            self.__ingameBrowserEventConfig = makeTupleByDict(_IngameBrowserEventConfig, self.__serverSettings[Configs.INGAME_BROWSER_EVENT_CONFIG.value])
        if Configs.COLLECTIVE_GOAL_MARATHONS_CONFIG.value in self.__serverSettings:
            self.__collectiveGoalMarathonsConfig = makeTupleByDict(_CollectiveGoalMarathonsConfig, self.__serverSettings[Configs.COLLECTIVE_GOAL_MARATHONS_CONFIG.value])
        if Configs.PERIPHERY_ROUTING_CONFIG.value in self.__serverSettings:
            self.__peripheryRoutingConfig = makeTupleByDict(PeripheryRoutingConfig, self.__serverSettings[Configs.PERIPHERY_ROUTING_CONFIG.value])
        if Configs.COMP7_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(Configs.COMP7_CONFIG.value, self.__serverSettings[Configs.COMP7_CONFIG.value])
            self.__comp7Config = makeTupleByDict(Comp7Config, self.__serverSettings[Configs.COMP7_CONFIG.value])
        else:
            self.__comp7Config = Comp7Config()
        if Configs.COMP7_RANKS_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(Configs.COMP7_RANKS_CONFIG.value, self.__serverSettings[Configs.COMP7_RANKS_CONFIG.value])
            self.__comp7RanksConfig = makeTupleByDict(Comp7RanksConfig, self.__serverSettings[Configs.COMP7_RANKS_CONFIG.value])
        else:
            self.__comp7RanksConfig = Comp7RanksConfig.defaults()
        if Configs.COMP7_REWARDS_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(Configs.COMP7_REWARDS_CONFIG.value, self.__serverSettings[Configs.COMP7_REWARDS_CONFIG.value])
            self.__comp7RewardsConfig = makeTupleByDict(Comp7RewardsConfig, self.__serverSettings[Configs.COMP7_REWARDS_CONFIG.value])
        else:
            self.__comp7RewardsConfig = Comp7RewardsConfig.defaults()
        if Configs.COMP7_SKILLS_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(Configs.COMP7_SKILLS_CONFIG.value, self.__serverSettings[Configs.COMP7_SKILLS_CONFIG.value])
            self.__comp7SkillsConfig = makeTupleByDict(Comp7SkillsConfig, self.__serverSettings[Configs.COMP7_SKILLS_CONFIG.value])
        else:
            self.__comp7SkillsConfig = Comp7SkillsConfig.defaults()
        if Configs.BATTLE_MODIFIER_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(Configs.BATTLE_MODIFIER_CONFIG.value, self.__serverSettings[Configs.BATTLE_MODIFIER_CONFIG.value])
            self.__battleModifiersConfig = makeTupleByDict(BattleModifiersConfig, self.__serverSettings[Configs.BATTLE_MODIFIER_CONFIG.value])
        else:
            self.__battleModifiersConfig = BattleModifiersConfig.defaults()
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
        if Configs.ARMORY_YARD_CONFIG.value in self.__serverSettings:
            self.__armoryYardSettings = makeTupleByDict(ArmoryYardConfig, self.__serverSettings[Configs.ARMORY_YARD_CONFIG.value])
        else:
            self.__armoryYardSettings = ArmoryYardConfig.defaults()
        if Configs.LIMITED_UI_CONFIG.value in self.__serverSettings:
            self.__limitedUIConfig = makeTupleByDict(_LimitedUIConfig, self.__serverSettings[Configs.LIMITED_UI_CONFIG.value])
        else:
            self.__limitedUIConfig = _LimitedUIConfig.defaults()
        if Configs.REFERRAL_PROGRAM_CONFIG.value in self.__serverSettings:
            self.__referralProgramConfig = makeTupleByDict(RPConfig, self.__serverSettings[Configs.REFERRAL_PROGRAM_CONFIG.value])
        else:
            self.__referralProgramConfig = RPConfig.defaults()
        if Configs.RESTORE_CONFIG.value in self.__serverSettings:
            self.__restoreConfig = makeTupleByDict(RestoreConfig, self.__serverSettings[Configs.RESTORE_CONFIG.value])
        if Configs.DEBUT_BOXES_CONFIG.value in self.__serverSettings:
            self.__debutBoxesConfig = makeTupleByDict(DebutBoxesConfig, self.__serverSettings[Configs.DEBUT_BOXES_CONFIG.value])
        else:
            self.__debutBoxesConfig = DebutBoxesConfig.defaults()
        if Configs.EARLY_ACCESS_CONFIG.value in self.__serverSettings:
            self.__earlyAccessConfig = makeTupleByDict(EarlyAccessConfig, self.__serverSettings[Configs.EARLY_ACCESS_CONFIG.value])
        if Configs.RANDOM_BATTLES_CONFIG.value in self.__serverSettings:
            self.__randomBattlesConfig = makeTupleByDict(RandomBattlesConfig, self.__serverSettings[Configs.RANDOM_BATTLES_CONFIG.value])
        if Configs.MODE_SELECTOR_CONFIG.value in self.__serverSettings:
            self.__modeSelectorConfig = makeTupleByDict(ModeSelectorConfig, self.__serverSettings[Configs.MODE_SELECTOR_CONFIG.value])
        else:
            self.__modeSelectorConfig = ModeSelectorConfig.defaults()
        if Configs.BATTLE_CONTEXT_HINTS_CONFIG.value in self.__serverSettings:
            self.__battleContextHintsConfig = makeTupleByDict(_BattleContextHintsConfig, self.__serverSettings[Configs.BATTLE_CONTEXT_HINTS_CONFIG.value])
        self.__schemaManager.set(self.__serverSettings)
        if Configs.PARAGONS_CONFIG.value in self.__serverSettings:
            LOG_DEBUG(Configs.PARAGONS_CONFIG.value, self.__serverSettings[Configs.PARAGONS_CONFIG.value])
            self.__paragonsConfig = ParagonsConfig(self.__serverSettings[Configs.PARAGONS_CONFIG.value])
        else:
            self.__paragonsConfig = ParagonsConfig.defaults()
        if Configs.LOOTBOX_STATISTICS_CONFIG.value in self.__serverSettings:
            self.__lootBoxStatisticsConfig = makeTupleByDict(_LootBoxStatisticsConfig, self.__serverSettings[Configs.LOOTBOX_STATISTICS_CONFIG.value])
        if Configs.SETTINGS_LOGGING_CONFIG.value in self.__serverSettings:
            self.__settingsLoggingConfig = makeTupleByDict(_SettingsLoggingConfig, self.__serverSettings[Configs.SETTINGS_LOGGING_CONFIG.value])
        if Configs.CONTROL_POINT_OVERRIDE_CONFIG.value in self.__serverSettings:
            self.__controlPointConfig = makeTupleByDict(_ControlPointOverrideConfig, self.__serverSettings[Configs.CONTROL_POINT_OVERRIDE_CONFIG.value])
        if Configs.NEWBIE_START_PAGE_CONFIG.value in self.__serverSettings:
            self.__newbieStartPageConfig = makeTupleByDict(_NewbieStartPageConfig, self.__serverSettings[Configs.NEWBIE_START_PAGE_CONFIG.value])
        if Configs.STALL_CONFIG.value in self.__serverSettings:
            self.__stallConfig = makeTupleByDict(_StallConfig, self.__serverSettings[Configs.STALL_CONFIG.value])
        else:
            self.__stallConfig = _StallConfig.defaults()
        if Configs.NEWBIE_CHAT_LOCK_CONFIG.value in self.__serverSettings:
            self.__newbieChatLockConfig = makeTupleByDict(_NewbieChatLockConfig, self.__serverSettings[Configs.NEWBIE_CHAT_LOCK_CONFIG.value])
        self.onServerSettingsChange(serverSettings)
        return

    def update(self, serverSettingsDiff):
        self.__serverSettings = updateDict(self.__serverSettings, serverSettingsDiff)
        if b'clanProfile' in serverSettingsDiff:
            self.__updateClanProfile(serverSettingsDiff)
        if b'spgRedesignFeatures' in self.__serverSettings:
            self.__spgRedesignFeatures = makeTupleByDict(_SpgRedesignFeatures, self.__serverSettings[b'spgRedesignFeatures'])
        if b'ranked_config' in serverSettingsDiff:
            self.__updateRanked(serverSettingsDiff)
        if b'hallOfFame' in serverSettingsDiff:
            self.__bwHallOfFame = makeTupleByDict(_BwHallOfFame, serverSettingsDiff[b'hallOfFame'])
        if b'clientgw' in serverSettingsDiff:
            self.__updateClientgw(serverSettingsDiff)
        if b'wgnp' in serverSettingsDiff:
            self.__updateWgnp(serverSettingsDiff)
        if Configs.UI_LOGGING.value in serverSettingsDiff:
            self.__updateUILogging(serverSettingsDiff)
        if b'eula_config' in serverSettingsDiff:
            self.__updateEULA(serverSettingsDiff)
        if b'advent_calendar_config' in serverSettingsDiff:
            self.__updateAdventCalendar(serverSettingsDiff)
            self.__serverSettings[b'advent_calendar_config'] = serverSettingsDiff[b'advent_calendar_config']
        if b'epic_config' in serverSettingsDiff:
            self.__updateEpic(serverSettingsDiff)
            self.__serverSettings[b'epic_config'] = serverSettingsDiff[b'epic_config']
        if Configs.BATTLE_ROYALE_CONFIG.value in serverSettingsDiff:
            self.__updateBattleRoyale(serverSettingsDiff)
        if Configs.MAPBOX_CONFIG.value in serverSettingsDiff:
            self.__updateMapbox(serverSettingsDiff)
        if b'unit_assembler_config' in serverSettingsDiff:
            self.__updateUnitAssemblerConfig(serverSettingsDiff)
            self.__serverSettings[b'unit_assembler_config'] = serverSettingsDiff[b'unit_assembler_config']
        if b'comp7_config' in serverSettingsDiff:
            self.__updateComp7(serverSettingsDiff)
        if Configs.COMP7_RANKS_CONFIG.value in serverSettingsDiff:
            self.__updateComp7PrestigeRanks(serverSettingsDiff)
        if Configs.COMP7_REWARDS_CONFIG.value in serverSettingsDiff:
            self.__updateComp7Rewards(serverSettingsDiff)
        if Configs.COMP7_SKILLS_CONFIG.value in serverSettingsDiff:
            self.__updateComp7Skills(serverSettingsDiff)
        if Configs.BATTLE_MODIFIER_CONFIG.value in serverSettingsDiff:
            self.__updateBattleModifiers(serverSettingsDiff)
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
        if b'seniority_awards_config' in serverSettingsDiff:
            self.__updateSeniorityAwards(serverSettingsDiff)
        if b'event_battles_config' in serverSettingsDiff:
            self.__updateEventBattles(serverSettingsDiff)
        if Configs.PARAGONS_CONFIG.value in serverSettingsDiff:
            self.__updateParagons(serverSettingsDiff)
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
        if Configs.RESOURCE_WELL.value in serverSettingsDiff:
            self.__updateResourceWellConfig(serverSettingsDiff)
        if Configs.UNIVERSAL_FLAG_ENTRY_POINT_CONFIG.value in serverSettingsDiff:
            newUniverslaFlagSettings = serverSettingsDiff[Configs.UNIVERSAL_FLAG_ENTRY_POINT_CONFIG.value]
            self.__serverSettings[Configs.UNIVERSAL_FLAG_ENTRY_POINT_CONFIG.value] = newUniverslaFlagSettings
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
        if Configs.COLLECTIVE_GOAL_ENTRY_POINT_CONFIG.value in serverSettingsDiff:
            self.__updateCollectiveGoalEntryPointConfig(serverSettingsDiff)
        if Configs.COLLECTIVE_GOAL_MARATHONS_CONFIG.value in serverSettingsDiff:
            self.__updateCollectiveGoalMarathonsConfig(serverSettingsDiff)
        if Configs.ARMORY_YARD_CONFIG.value in serverSettingsDiff:
            self.__updateArmoryYard(serverSettingsDiff)
        if Configs.REFERRAL_PROGRAM_CONFIG.value in serverSettingsDiff:
            self.__updateRPConfig(serverSettingsDiff)
        if Configs.VERSUS_AI_CONFIG.value in serverSettingsDiff:
            self.__updateVersusAI(serverSettingsDiff)
        self.__updatePersonalReserves(serverSettingsDiff)
        self.__updateGuiLootBoxesConfig(serverSettingsDiff)
        if Configs.COLLECTIONS_CONFIG.value in serverSettingsDiff:
            self.__updateCollectionsConfig(serverSettingsDiff)
        self.__updateLimitedUIConfig(serverSettingsDiff)
        if Configs.RESTORE_CONFIG.value in serverSettingsDiff:
            self.__updateRestoreConfig(serverSettingsDiff)
        if Configs.DEBUT_BOXES_CONFIG.value in serverSettingsDiff:
            self.__updateDebutBoxesConfig(serverSettingsDiff)
        if Configs.EARLY_ACCESS_CONFIG.value in serverSettingsDiff:
            self.__updateEarlyAccessConfig(serverSettingsDiff)
        if Configs.MODE_SELECTOR_CONFIG.value in serverSettingsDiff:
            self.__updateModeSelectorConfig(serverSettingsDiff)
        lbKeyConfig = Configs.LOOTBOX_KEYS_CONFIG.value
        if lbKeyConfig in serverSettingsDiff:
            self.__serverSettings[lbKeyConfig] = serverSettingsDiff[lbKeyConfig]
        if Configs.RANDOM_BATTLES_CONFIG.value in serverSettingsDiff:
            self.__updateRandomBattlesConfig(serverSettingsDiff)
        if Configs.BLACK_MARKET_CONFIG.value in serverSettingsDiff:
            self.__updateBlackMarketConfig(serverSettingsDiff)
        if Configs.INGAME_BROWSER_EVENT_CONFIG.value in serverSettingsDiff:
            self.__updateIngameBrowserEventConfig(serverSettingsDiff)
        if Configs.LOOTBOX_STATISTICS_CONFIG.value in serverSettingsDiff:
            self.__updateLootBoxStatisticsConfig(serverSettingsDiff)
        if Configs.BATTLE_CONTEXT_HINTS_CONFIG.value in serverSettingsDiff:
            self.__updateBattleContextHintsConfig(serverSettingsDiff)
        if Configs.SETTINGS_LOGGING_CONFIG.value in serverSettingsDiff:
            self.__updateSettingsLogging(serverSettingsDiff)
        if Configs.STALL_CONFIG.value in serverSettingsDiff:
            self.__updateStallConfig(serverSettingsDiff)
        if Configs.CONTROL_POINT_OVERRIDE_CONFIG.value in serverSettingsDiff:
            self.__updateControlPointConfig(serverSettingsDiff)
        if Configs.NEWBIE_CHAT_LOCK_CONFIG.value in serverSettingsDiff:
            self.__updateNewbieChatLockConfig(serverSettingsDiff)
        self.__schemaManager.update(serverSettingsDiff)
        self.onServerSettingsChange(serverSettingsDiff)
        return

    def clear(self):
        self.__schemaManager.clear()
        self.onServerSettingsChange.clear()
        return

    def getSettings(self):
        return self.__serverSettings

    def getConfigModel(self, schema):
        configModel = self.__schemaManager.get(schema)
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
    def clientgw(self):
        return self.__clientgw

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
    def adventCalendar(self):
        return self.__adventCalendar

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
    def comp7Config(self):
        return self.__comp7Config

    @property
    def battleModifiersConfig(self):
        return self.__battleModifiersConfig

    @property
    def comp7RanksConfig(self):
        return self.__comp7RanksConfig

    @property
    def comp7RewardsConfig(self):
        return self.__comp7RewardsConfig

    @property
    def comp7SkillsConfig(self):
        return self.__comp7SkillsConfig

    @property
    def telecomConfig(self):
        return self.__telecomConfig

    @property
    def blueprintsConfig(self):
        return self.__blueprintsConfig

    @property
    def paragonsConfig(self):
        return self.__paragonsConfig

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
    def resourceWellConfig(self):
        return self.__resourceWellConfig

    @property
    def playLimitsConfig(self):
        return self.__playLimitsConfig

    @property
    def battleMattersConfig(self):
        return self.__battleMattersConfig

    @property
    def collectiveGoalEntryPointConfig(self):
        return self.__collectiveGoalEntryPointConfig

    @property
    def universalFlagEntryPointConfig(self):
        return self.__getGlobalSetting(Configs.UNIVERSAL_FLAG_ENTRY_POINT_CONFIG.value, {b'isEnabled': False})

    @property
    def blackMarketConfig(self):
        return self.__blackMarketConfig

    @property
    def ingameBrowserEventConfig(self):
        return self.__ingameBrowserEventConfig

    @property
    def collectiveGoalMarathonsConfig(self):
        return self.__collectiveGoalMarathonsConfig

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
    def armoryYard(self):
        return self.__armoryYardSettings

    @property
    def limitedUIConfig(self):
        return self.__limitedUIConfig

    @property
    def restoreConfig(self):
        return self.__restoreConfig

    @property
    def versusAIConfig(self):
        return self.__versusAISettings

    @property
    def debutBoxesConfig(self):
        return self.__debutBoxesConfig

    @property
    def earlyAccessConfig(self):
        return self.__earlyAccessConfig

    @property
    def randomBattlesConfig(self):
        return self.__randomBattlesConfig

    @property
    def modeSelectorConfig(self):
        return self.__modeSelectorConfig

    @property
    def battleContextHintsConfig(self):
        return self.__battleContextHintsConfig

    @property
    def settingsLoggingConfig(self):
        return self.__settingsLoggingConfig

    @property
    def controlPointConfig(self):
        return self.__controlPointConfig

    @property
    def newbieStartPageConfig(self):
        return self.__newbieStartPageConfig

    @property
    def stallConfig(self):
        return self.__stallConfig

    @property
    def newbieChatLockConfig(self):
        return self.__newbieChatLockConfig

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

    def isStaticWeatherSwitchEnabled(self):
        return self.__getGlobalSetting(b'isStaticWeatherSwitchEnabled', True)

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

    def isGoldFishEnabled(self):
        return self.__getGlobalSetting(b'isGoldFishEnabled', False)

    def isStorageEnabled(self):
        return self.__bwShop.isStorageEnabled

    def isLootBoxesEnabled(self):
        return self.__getGlobalSetting(b'isLootBoxesEnabled')

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

    def isBootcampEnabled(self):
        return self.__getGlobalSetting(b'isBootcampEnabled', False)

    def getBootcampBonuses(self):
        return self.__getGlobalSetting(b'bootcampBonuses', {})

    def isMapsTrainingEnabled(self):
        return self.__getGlobalSetting(b'isMapsTrainingEnabled', False)

    def recertificationFormState(self):
        return self.__getGlobalSetting(b'recertificationFormState', SwitchState.DISABLED.value)

    def getLootBoxConfig(self):
        return self.__getGlobalSetting(b'lootBoxes_config', {})

    def getLootBoxKeyConfig(self):
        return self.__getGlobalSetting(Configs.LOOTBOX_KEYS_CONFIG.value, {})

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

    def isRenewableSubEnabled(self):
        return self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enabled', False)

    def isWotPlusEnabledForSteam(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enabledForSteam', False)

    def isRenewableSubGoldReserveEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableGoldReserve', False)

    def isRenewableSubPassiveCrewXPEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enablePassiveCrewXP', False)

    def isWotPlusExcludedMapEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableExcludedMap', False)

    def isPreferredMapsSlotsEnabled(self, slotsTypeName):
        return bool(self.getPreferredMapsConfig().get(slotsTypeName, 0))

    def isWoTPlusExclusiveVehicleEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableWoTPlusExclusiveVehicle', False)

    def isFreeEquipmentDemountingEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableFreeEquipmentDemounting', False)

    def isFreeDeluxeEquipmentDemountingEnabled(self):
        return self.isFreeEquipmentDemountingEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableFreeDeluxeEquipmentDemounting', False)

    def isDailyAttendancesEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableDailyAttendances', False)

    def isDailyQuestsExtraRewardsEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableDailyQuestsExtraRewards', False)

    def isTeamCreditsBonusEnabled(self):
        return self.isRenewableSubEnabled() and self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'enableTeamCreditsBonus', False)

    def getWotPlusExclusiveVehicleInfo(self):
        return self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'exclusiveVehicle', {})

    def getDailyAttendanceQuestPrefix(self):
        return self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'dailyAttendanceQuestPrefix', b'')

    def getRenewableSubCrewXPPerMinute(self):
        return self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'crewXPPerMinute', 0)

    def getRenewableSubMaxGoldReserveCapacity(self):
        return self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'maxGoldReserveCapacity', 0)

    def getArenaTypesWithGoldReserve(self):
        return self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(GOLD_RESERVE_GAINS_SECTION, {}).keys()

    def getWotPlusProductCode(self):
        return self.__getGlobalSetting(RENEWABLE_SUBSCRIPTION_CONFIG, {}).get(b'subscriptionProductCode', b'subscription_dev')

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

    def isPromoCodeRewardScreenEnabled(self):
        return self.getMiscGUISettings().get(b'isPromoCodeRewardScreenEnabled', True)

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

    def isOnly10ModeEnabled(self):
        return self.__getGlobalSetting(b'isOnly10ModeEnabled', False)

    def isMapsInDevelopmentEnabled(self):
        mapsInDevCongig = self.__getGlobalSetting(Configs.MAPS_IN_DEVELOPMENT_CONFIG.value, None)
        if mapsInDevCongig:
            return bool(mapsInDevCongig[b'isEnabled'])
        else:
            return False

    def getMaxSPGinSquads(self):
        return self.__getGlobalSetting(b'maxSPGinSquads', 0)

    def getMaxFlamethrowerInSquads(self):
        return self.__getGlobalSetting(b'maxFlamethrowerInSquads', 0)

    def getMaxScoutInSquads(self):
        return self.__getGlobalSetting(b'maxScoutInSquads', 0)

    def getMaxScoutInSquadsLevels(self):
        return self.__getGlobalSetting(b'maxScoutInSquadsLevels', [])

    def getPossibleSquadsVehicleLevels(self):
        return self.__getGlobalSetting(b'possibleSquadsVehicleLevels', [])

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

    def isOptionalDeviceRestoreEnabled(self):
        return self.__getGlobalSetting(b'isOptionalDeviceRestoreEnabled', True)

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

    def isTrophyDevicesEnabled(self):
        return self.__getGlobalSetting(b'isTrophyDevicesEnabled', False)

    def isTrainingBattleEnabled(self):
        return self.__getGlobalSetting(b'isTrainingBattleEnabled', False)

    def isCollectorVehicleEnabled(self):
        return self.__getGlobalSetting(CollectorVehicleConsts.CONFIG_NAME, {}).get(CollectorVehicleConsts.IS_ENABLED, False)

    def isOffersEnabled(self):
        return self.__getGlobalSetting(OFFERS_ENABLED_KEY, False)

    def getProgressiveRewardConfig(self):
        return self.__progressiveReward

    def getMarathonConfig(self):
        return self.__getGlobalSetting(b'marathon_config', {})

    def getClansConfig(self):
        return self.__getGlobalSetting(ClansConfig.SECTION_NAME, {})

    def getSeniorityAwardsConfig(self):
        return self.__seniorityAwardsConfig

    def getBattlePassConfig(self):
        return self.__battlePassConfig

    def getReactiveCommunicationConfig(self):
        return self.__reactiveCommunicationConfig

    def isLegacyModeSelectorEnabled(self):
        return self.__getGlobalSetting(b'isLegacyModeSelectorEnabled', False)

    def getBlueprintsConvertSaleConfig(self):
        return self.__blueprintsConvertSaleConfig

    def getActiveTestConfirmationConfig(self):
        return self.__getGlobalSetting(ACTIVE_TEST_CONFIRMATION_CONFIG, {})

    def getTradeInConfig(self):
        return self.__getGlobalSetting(TRADE_IN_CONFIG_NAME, {})

    def getGuiLootBoxesConfig(self):
        return self.__guiLootBoxesConfig

    def getAchievements20GeneralConfig(self):
        return Achievements20GeneralConfig(self.__getGlobalSetting(Configs.ACHIEVEMENTS20_CONFIG.value, {}))

    def getRPConfig(self):
        return self.__referralProgramConfig

    def getBlackMarketConfig(self):
        return self.__getGlobalSetting(Configs.BLACK_MARKET_CONFIG.value, {})

    def getIngameBrowserEventConfig(self):
        return self.__getGlobalSetting(Configs.INGAME_BROWSER_EVENT_CONFIG.value, {})

    def getLootBoxStatisticsConfig(self):
        return self.__getGlobalSetting(Configs.LOOTBOX_STATISTICS_CONFIG.value, {})

    def getMuseumOfGloryConfig(self):
        return self.__getGlobalSetting(b'museum_of_glory_config', {})

    def __getGlobalSetting(self, settingsName, default=None):
        return self.__serverSettings.get(settingsName, default)

    def __updateClanProfile(self, targetSettings):
        cProfile = targetSettings[b'clanProfile']
        self.__clanProfile = _ClanProfile(cProfile.get(b'isEnabled', False))
        return

    def __updateClientgw(self, targetSettings):
        cProfile = targetSettings[b'clientgw']
        self.__clientgw = _Clientgw(cProfile.get(b'isEnabled', False), cProfile.get(b'gateUrl', b''), cProfile.get(b'type', b'gateway'), cProfile.get(b'loginOnStart', False), cProfile.get(b'isJwtAuthorizationEnabled', True))
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

    def __updateAdventCalendar(self, targetSettings):
        self.__adventCalendar = self.__adventCalendar.replace(targetSettings[b'advent_calendar_config'])
        return

    def __updateRanked(self, targetSettings):
        self.__rankedBattlesSettings = self.__rankedBattlesSettings.replace(targetSettings[b'ranked_config'])
        return

    def __updateEpic(self, targetSettings):
        self.__epicMetaGameSettings = self.__epicMetaGameSettings.replace(targetSettings[b'epic_config'].get(b'epicMetaGame', {}))
        self.__epicGameSettings = self.__epicGameSettings.replace(targetSettings[b'epic_config'])
        return

    def __updateUnitAssemblerConfig(self, targetSettings):
        self.__unitAssemblerConfig = self.__unitAssemblerConfig.replace(targetSettings[b'unit_assembler_config'])
        return

    def __updateComp7(self, targetSettings):
        config = targetSettings[Configs.COMP7_CONFIG.value]
        self.__comp7Config = self.__comp7Config.replace(copy.deepcopy(config))
        return

    def __updateComp7PrestigeRanks(self, targetSettings):
        config = targetSettings[Configs.COMP7_RANKS_CONFIG.value]
        self.__comp7RanksConfig = self.__comp7RanksConfig.replace(copy.deepcopy(config))
        return

    def __updateComp7Rewards(self, targetSettings):
        config = targetSettings[Configs.COMP7_REWARDS_CONFIG.value]
        self.__comp7RewardsConfig = self.__comp7RewardsConfig.replace(config)
        return

    def __updateComp7Skills(self, targetSettings):
        config = targetSettings[Configs.COMP7_SKILLS_CONFIG.value]
        self.__comp7SkillsConfig = self.__comp7SkillsConfig.replace(config)
        return

    def __updateBattleModifiers(self, targetSettings):
        config = targetSettings[Configs.BATTLE_MODIFIER_CONFIG.value]
        self.__battleModifiersConfig = self.__battleModifiersConfig.replace(copy.deepcopy(config))
        return

    def __updateParagons(self, targetSettings):
        self.__paragonsConfig = self.__paragonsConfig.replace(targetSettings[Configs.PARAGONS_CONFIG.value])
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
        self.__seniorityAwardsConfig = self.__seniorityAwardsConfig.replace(targetSettings[b'seniority_awards_config'])
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

    def __updateResourceWellConfig(self, diff):
        self.__resourceWellConfig = self.__resourceWellConfig.replace(diff[Configs.RESOURCE_WELL.value])
        return

    def __updatePlayLimitsConfig(self, serverSettingsDiff):
        self.__playLimitsConfig = self.__playLimitsConfig.replace(serverSettingsDiff[Configs.PLAY_LIMITS_CONFIG.value])
        return

    def __updateBattleMatters(self, targetSettings):
        self.__battleMattersConfig = self.__battleMattersConfig.replace(targetSettings[Configs.BATTLE_MATTERS_CONFIG.value])
        return

    def __updateCollectiveGoalEntryPointConfig(self, diff):
        self.__collectiveGoalEntryPointConfig = self.__collectiveGoalEntryPointConfig.replace(diff[Configs.COLLECTIVE_GOAL_ENTRY_POINT_CONFIG.value])
        return

    def __updateBlackMarketConfig(self, diff):
        self.__blackMarketConfig = self.__blackMarketConfig.replace(diff[Configs.BLACK_MARKET_CONFIG.value])
        return

    def __updateIngameBrowserEventConfig(self, diff):
        self.__ingameBrowserEventConfig = self.__ingameBrowserEventConfig.replace(diff[Configs.INGAME_BROWSER_EVENT_CONFIG.value])
        return

    def __updateCollectiveGoalMarathonsConfig(self, diff):
        self.__collectiveGoalMarathonsConfig = self.__collectiveGoalMarathonsConfig.replace(diff[Configs.COLLECTIVE_GOAL_MARATHONS_CONFIG.value])
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

    def __updateGuiLootBoxesConfig(self, settings):
        if GUI_LOOT_BOXES_CONFIG in settings:
            config = settings[GUI_LOOT_BOXES_CONFIG]
            if config is None:
                self.__guiLootBoxesConfig = _GuiLootBoxesConfig()
            elif isinstance(config, dict):
                self.__guiLootBoxesConfig = _GuiLootBoxesConfig(**config)
            else:
                _logger.error(b'Unexpected format of subscriptions service config: %r', config)
                self.__guiLootBoxesConfig = _GuiLootBoxesConfig()
        return

    def __updateCollectionsConfig(self, diff):
        self.__collectionsConfig = self.__collectionsConfig.replace(diff[Configs.COLLECTIONS_CONFIG.value])
        return

    def __updateRPConfig(self, diff):
        self.__referralProgramConfig = self.__referralProgramConfig.replace(diff[Configs.REFERRAL_PROGRAM_CONFIG.value])
        return

    def __updateWinbackConfig(self, diff):
        self.__winbackConfig = self.__winbackConfig.replace(diff[Configs.WINBACK_CONFIG.value])
        return

    def __updateArmoryYard(self, diff):
        self.__armoryYardSettings = self.__armoryYardSettings.replace(diff[Configs.ARMORY_YARD_CONFIG.value])
        return

    def __updateLimitedUIConfig(self, serverSettingsDiff):
        if Configs.LIMITED_UI_CONFIG.value in serverSettingsDiff:
            self.__limitedUIConfig = self.__limitedUIConfig.replace(serverSettingsDiff[Configs.LIMITED_UI_CONFIG.value])
        return

    def __updateRestoreConfig(self, serverSettingsDiff):
        self.__restoreConfig = self.__restoreConfig.replace(serverSettingsDiff[Configs.RESTORE_CONFIG.value])
        return

    def __updateDebutBoxesConfig(self, diff):
        self.__debutBoxesConfig = self.__debutBoxesConfig.replace(diff[Configs.DEBUT_BOXES_CONFIG.value])
        return

    def __updateVersusAI(self, targetSettings):
        data = targetSettings[Configs.VERSUS_AI_CONFIG.value]
        self.__versusAISettings = self.__versusAISettings.replace(data)
        return

    def __updateEarlyAccessConfig(self, diff):
        self.__earlyAccessConfig = self.__earlyAccessConfig.replace(diff[Configs.EARLY_ACCESS_CONFIG.value])
        return

    def __updateRandomBattlesConfig(self, diff):
        self.__randomBattlesConfig = self.__randomBattlesConfig.replace(diff[Configs.RANDOM_BATTLES_CONFIG.value])
        return

    def __updateModeSelectorConfig(self, diff):
        self.__modeSelectorConfig = self.__modeSelectorConfig.replace(diff[Configs.MODE_SELECTOR_CONFIG.value])
        return

    def __updateLootBoxStatisticsConfig(self, diff):
        self.__lootBoxStatisticsConfig = self.__lootBoxStatisticsConfig.replace(diff[Configs.LOOTBOX_STATISTICS_CONFIG.value])
        return

    def __updateBattleContextHintsConfig(self, diff):
        self.__battleContextHintsConfig = self.__battleContextHintsConfig.replace(diff[Configs.BATTLE_CONTEXT_HINTS_CONFIG.value])
        return

    def __updateSettingsLogging(self, diff):
        self.__settingsLoggingConfig = self.__settingsLoggingConfig.replace(diff[Configs.SETTINGS_LOGGING_CONFIG.value])
        return

    def __updateStallConfig(self, diff):
        self.__stallConfig = self.__stallConfig.replace(diff[Configs.STALL_CONFIG.value])
        return

    def __updateControlPointConfig(self, diff):
        self.__controlPointConfig = self.__controlPointConfig.replace(diff[Configs.CONTROL_POINT_OVERRIDE_CONFIG.value])
        return

    def __updateNewbieChatLockConfig(self, serverSettingsDiff):
        if Configs.NEWBIE_CHAT_LOCK_CONFIG.value in serverSettingsDiff:
            self.__newbieChatLockConfig = self.__newbieChatLockConfig.replace(serverSettingsDiff[Configs.NEWBIE_CHAT_LOCK_CONFIG.value])
        return


def serverSettingsChangeListener(*configKeys):

    def decorator(func):

        @functools.wraps(func)
        def wrapper(self, diff):
            if any(configKey in diff for configKey in configKeys):
                func(self, diff)
            return

        return wrapper

    return decorator
