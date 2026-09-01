import copy, logging, typing
from shared_utils import makeTupleByDict
import BattleReplay
from Event import Event
from Event import EventManager
from comp7_common.comp7_constants import Configs
from comp7_ranks_common import Comp7Division
from helpers import dependency
from helpers.server_settings import settingsBlock
from skeletons.gui.lobby_context import ILobbyContext
if typing.TYPE_CHECKING:
    from typing import Dict, List, Tuple
_logger = logging.getLogger(__name__)

class _Comp7QualificationConfig(settingsBlock(b'_Comp7QualificationConfig', (b'battlesNumber',))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return {b'battlesNumber': 0}


class Comp7Config(settingsBlock(b'Comp7Config', (b'isEnabled', b'isShopEnabled', b'isTrainingEnabled', b'isVehicleBanEnabled', b'peripheryIDs', b'primeTimes', b'seasons', b'battleModifiersDescr', b'cycleTimes', b'roleEquipments', b'roleEquipmentsByVehicle', b'poiEquipments', b'numPlayers', b'levels', b'allowedVehTypes', b'squadRankRestriction', b'squadSizes', b'createVivoxTeamChannels', b'qualification', b'maps', b'remainingOfferTokensNotifications', b'clientEntitlementsCache', b'participantTokens', b'bans', b'vehicleCopiesInfo', b'minVehiclesRequired', b'subModes'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return dict(isEnabled=False, isShopEnabled=False, isTrainingEnabled=False, isVehicleBanEnabled=False, peripheryIDs={}, primeTimes={}, seasons={}, battleModifiersDescr=(), cycleTimes={}, roleEquipments={}, roleEquipmentsByVehicle={}, poiEquipments={}, numPlayers=7, levels=[], allowedVehTypes=set(), squadRankRestriction={}, squadSizes=[
         0, 0], createVivoxTeamChannels=False, qualification={}, maps=set(), remainingOfferTokensNotifications=[], clientEntitlementsCache={}, participantTokens=(), bans={}, vehicleCopiesInfo={}, minVehiclesRequired=1, subModes={})

    @classmethod
    def _preprocessData(cls, data):
        qualificationConfig = data.get(b'qualification')
        if qualificationConfig is not None:
            data[b'qualification'] = makeTupleByDict(_Comp7QualificationConfig, qualificationConfig)
        return data


class Comp7RanksConfig(settingsBlock(b'Comp7RanksConfig', (b'ranks', b'ranksOrder', b'eliteRankPercent', b'divisionsByRank', b'divisions', b'rankInactivityNotificationThreshold', b'businessDayStartHour'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return dict(ranks={}, ranksOrder=(), eliteRankPercent=0, divisionsByRank={}, divisions=(), rankInactivityNotificationThreshold=0, businessDayStartHour=0)

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
    def __dictDivisionsToComp7Divisions(cls, divisions):
        return tuple(Comp7Division(serialIdx, divisionInfo) for serialIdx, divisionInfo in enumerate(divisions))


class Comp7RewardsConfig(settingsBlock(b'Comp7RewardsConfig', (b'main', b'extra'))):
    __slots__ = ()

    @classmethod
    def defaults(cls):
        return {b'main': [], b'extra': []}

    def getCosts(self):
        return sorted([bonusInfo[b'cost'] for bonusInfo in self[0]])


class Comp7ServerSettings(object):
    __lobbyContext = dependency.descriptor(ILobbyContext)

    def __init__(self):
        super(Comp7ServerSettings, self).__init__()
        self.__comp7Config = Comp7Config()
        self.__comp7RanksConfig = Comp7RanksConfig()
        self.__comp7RewardsConfig = Comp7RewardsConfig()
        self.__serverSettings = self.__lobbyContext.getServerSettings()
        self.__setInitValues()
        self.__lobbyContext.onServerSettingsChanged += self.__onServerSettingsChanged
        if self.__serverSettings is not None:
            self.__serverSettings.onServerSettingsChange += self.__update
        self.__eventsManager = EventManager()
        self.onComp7SettingsChanged = Event(self.__eventsManager)
        return

    @property
    def comp7Config(self):
        return self.__comp7Config

    @property
    def comp7RanksConfig(self):
        return self.__comp7RanksConfig

    @property
    def comp7RewardsConfig(self):
        return self.__comp7RewardsConfig

    def fini(self):
        self.__comp7Config = None
        self.__comp7RanksConfig = None
        self.__comp7RewardsConfig = None
        self.__lobbyContext.onServerSettingsChanged -= self.__onServerSettingsChanged
        if self.__serverSettings is not None:
            self.__serverSettings.onServerSettingsChange -= self.__update
        self.__serverSettings = None
        self.__eventsManager.clear()
        return

    def __onServerSettingsChanged(self, serverSettings):
        if self.__serverSettings is not None:
            self.__serverSettings.onServerSettingsChange -= self.__update
        self.__serverSettings = serverSettings
        self.__serverSettings.onServerSettingsChange += self.__update
        return

    def __setInitValues(self):
        settings = self.__serverSettings.getSettings() if self.__serverSettings else {}
        if not settings and BattleReplay.isPlaying() and not BattleReplay.isServerSideReplay():
            settings = BattleReplay.g_replayCtrl.arenaInfo[b'serverSettings']
        if Configs.COMP7_CONFIG.value in settings:
            _logger.debug(Configs.COMP7_CONFIG.value, settings[Configs.COMP7_CONFIG.value])
            self.__comp7Config = makeTupleByDict(Comp7Config, settings[Configs.COMP7_CONFIG.value])
        else:
            self.__comp7Config = makeTupleByDict(Comp7Config, Comp7Config.defaults())
        if Configs.COMP7_RANKS_CONFIG.value in settings:
            _logger.debug(Configs.COMP7_RANKS_CONFIG.value, settings[Configs.COMP7_RANKS_CONFIG.value])
            self.__comp7RanksConfig = makeTupleByDict(Comp7RanksConfig, settings[Configs.COMP7_RANKS_CONFIG.value])
        else:
            self.__comp7RanksConfig = makeTupleByDict(Comp7RanksConfig, Comp7RanksConfig.defaults())
        if Configs.COMP7_REWARDS_CONFIG.value in settings:
            _logger.debug(Configs.COMP7_REWARDS_CONFIG.value, settings[Configs.COMP7_REWARDS_CONFIG.value])
            self.__comp7RewardsConfig = makeTupleByDict(Comp7RewardsConfig, settings[Configs.COMP7_REWARDS_CONFIG.value])
        else:
            self.__comp7RewardsConfig = makeTupleByDict(Comp7RewardsConfig, Comp7RewardsConfig.defaults())
        return

    def __update(self, serverSettingsDiff):
        if Configs.COMP7_CONFIG.value in serverSettingsDiff:
            self.__updateComp7(serverSettingsDiff)
        if Configs.COMP7_RANKS_CONFIG.value in serverSettingsDiff:
            self.__updateComp7PrestigeRanks(serverSettingsDiff)
        if Configs.COMP7_REWARDS_CONFIG.value in serverSettingsDiff:
            self.__updateComp7Rewards(serverSettingsDiff)
        return

    def __updateComp7(self, targetSettings):
        config = targetSettings[Configs.COMP7_CONFIG.value]
        self.__comp7Config = self.__comp7Config.replace(copy.deepcopy(config))
        if not BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.setServerSetting(Configs.COMP7_CONFIG.value, config)
        self.onComp7SettingsChanged(targetSettings)
        return

    def __updateComp7PrestigeRanks(self, targetSettings):
        config = targetSettings[Configs.COMP7_RANKS_CONFIG.value]
        self.__comp7RanksConfig = self.__comp7RanksConfig.replace(copy.deepcopy(config))
        self.onComp7SettingsChanged(targetSettings)
        return

    def __updateComp7Rewards(self, targetSettings):
        config = targetSettings[Configs.COMP7_REWARDS_CONFIG.value]
        self.__comp7RewardsConfig = self.__comp7RewardsConfig.replace(config)
        self.onComp7SettingsChanged(targetSettings)
        return
