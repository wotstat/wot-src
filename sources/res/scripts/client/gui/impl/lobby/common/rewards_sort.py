import logging, re
from functools import partial
from enum import Enum, unique
from gui import GUI_NATIONS, GUI_NATIONS_ORDER_INDEX
from gui.impl.gen import R
from gui.impl import backport
from nations import NONE_INDEX
from shared_utils import safeIndexOf
_logger = logging.getLogger(__name__)

class _Enum(Enum):

    @classmethod
    def makeValue(cls, value):
        if value in cls._value2member_map_:
            return cls(value)
        else:
            _logger.error(b'%s is not a valid init value for %s', value, cls.__name__)
            return


@unique
class _RewardType(_Enum):
    BLUEPRINT = b'blueprint'
    BROCHURE = b'brochure'
    DEVICE_FV = b'new_device_fv'
    DEVICE_MI = b'new_device_mi'
    GUIDE = b'guide'
    TROPHY = b'trophy'
    BOOK = b'book'
    BATTLE_BOOSTER = b'battleBooster'
    EXP_EQUIPMENTS = b'expequipments'
    DEVICE_PM3 = b'new_device_pm3'
    EXP_EQUIPMENTS_GIFT = b'expequipments_gift'
    DEVICE_PM3_GIFT = b'new_device_pm3_gift'


@unique
class _Reward(_Enum):
    AIM_DRIVES = b'AimDrives'
    AIM_STABILIZER = b'AimingStabilizer'
    ANTI_FRAGMENTATION = b'AntifragmentationLining'
    BLUEPRINT = b'Blueprint'
    BROCHURE = b'Brochure'
    CAMOUFLAGE = b'CamouflageNet'
    COMM_VIEW = b'CommandersView'
    CONFIGURATION = b'Configuration'
    GROUSERS = b'Grousers'
    GUIDE = b'Guide'
    HEALTH_RESERVE = b'ExtraHealthReserve'
    INVIS_DEVICE = b'AdditionalInvisibilityDevice'
    OPTICS = b'CoatedOptics'
    RADIO = b'RadioCommunication'
    ROT_MECHANISM = b'RotationMechanism'
    SIGHTS = b'Sights'
    STEREOSCOPE = b'Stereoscope'
    TANK_RAMMER = b'TankRammer'
    TURBOCHARGER = b'Turbocharger'
    VENTILATION = b'Ventilation'
    MODERNIZED_AIM_STABILIZER = b'ModernizedAimDrivesAimingStabilizer1'
    MODERNIZED_TURBO_CHARGER_ROTATION = b'ModernizedTurbochargerRotationMechanism1'
    MODERNIZED_EXTRA_HEALTH_RESERVE = b'ModernizedExtraHealthReserveAntifragmentationLining1'
    MODERNIZED_DAMAGE_VENTILATION = b'ModernizedDamageVentilation1'
    MODERNIZED_TANK_RAMMER_SIGHTS = b'ModernizedTankRammerSights1'


_REWARDS_TYPES_ORDER = (
 _RewardType.TROPHY,
 _RewardType.EXP_EQUIPMENTS,
 _RewardType.DEVICE_FV,
 _RewardType.DEVICE_MI,
 _RewardType.BOOK,
 _RewardType.GUIDE,
 _RewardType.BROCHURE,
 _RewardType.BLUEPRINT)
_REWARDS_ORDER = {(_RewardType.TROPHY): (
                        _Reward.AIM_DRIVES,
                        _Reward.TANK_RAMMER,
                        _Reward.VENTILATION,
                        _Reward.OPTICS,
                        _Reward.AIM_STABILIZER,
                        _Reward.CONFIGURATION,
                        _Reward.ROT_MECHANISM,
                        _Reward.SIGHTS,
                        _Reward.INVIS_DEVICE), 
   (_RewardType.DEVICE_FV): (
                           _Reward.VENTILATION,
                           _Reward.TANK_RAMMER,
                           _Reward.AIM_DRIVES,
                           _Reward.AIM_STABILIZER,
                           _Reward.SIGHTS,
                           _Reward.ROT_MECHANISM,
                           _Reward.ANTI_FRAGMENTATION,
                           _Reward.HEALTH_RESERVE,
                           _Reward.CONFIGURATION), 
   (_RewardType.DEVICE_MI): (
                           _Reward.VENTILATION,
                           _Reward.GROUSERS,
                           _Reward.ROT_MECHANISM,
                           _Reward.TURBOCHARGER,
                           _Reward.STEREOSCOPE,
                           _Reward.CAMOUFLAGE,
                           _Reward.INVIS_DEVICE,
                           _Reward.OPTICS,
                           _Reward.RADIO,
                           _Reward.COMM_VIEW), 
   (_RewardType.BATTLE_BOOSTER): (
                                _Reward.VENTILATION,
                                _Reward.TANK_RAMMER,
                                _Reward.AIM_DRIVES,
                                _Reward.AIM_STABILIZER,
                                _Reward.SIGHTS,
                                _Reward.ROT_MECHANISM,
                                _Reward.ANTI_FRAGMENTATION,
                                _Reward.HEALTH_RESERVE,
                                _Reward.CONFIGURATION), 
   (_RewardType.EXP_EQUIPMENTS): (
                                _Reward.MODERNIZED_AIM_STABILIZER,
                                _Reward.MODERNIZED_TURBO_CHARGER_ROTATION,
                                _Reward.MODERNIZED_EXTRA_HEALTH_RESERVE,
                                _Reward.MODERNIZED_DAMAGE_VENTILATION,
                                _Reward.MODERNIZED_TANK_RAMMER_SIGHTS)}
_REWARD_NAME_EXTRACTOR = re.compile(b'(basic|enhanced|improved|trophy)*([a-z]+)(_(\\w+\\d*))*', re.I)
_REWARD_NATION_EXTRACTOR = re.compile((b'.*({})').format((b'|').join(GUI_NATIONS)), re.I)

def _extractRewardName(rewardRawName):
    name = _REWARD_NAME_EXTRACTOR.sub(b'\\2', rewardRawName)
    return name[0].upper() + name[1:]


def _extractRewardNation(rewardRawName):
    return _REWARD_NATION_EXTRACTOR.sub(b'\\1', rewardRawName)


def _rewardTypeComparator(first, second):
    return cmp(safeIndexOf(_RewardType.makeValue(first[0]), _REWARDS_TYPES_ORDER), safeIndexOf(_RewardType.makeValue(second[0]), _REWARDS_TYPES_ORDER))


def _compareRewardsByNation(first, second):
    return cmp(GUI_NATIONS_ORDER_INDEX.get(_extractRewardNation(first[0]), NONE_INDEX), GUI_NATIONS_ORDER_INDEX.get(_extractRewardNation(second[0]), NONE_INDEX))


def _compareRewardsByType(rewardType, first, second):
    order = _REWARDS_ORDER[rewardType]
    return cmp(safeIndexOf(_Reward.makeValue(_extractRewardName(first[0])), order), safeIndexOf(_Reward.makeValue(_extractRewardName(second[0])), order))


def _compareRewardsByArtifactName(first, second):
    artefacts = R.strings.artefacts

    def _safeExtract(path):
        folder = artefacts.dyn(path)
        if folder:
            return backport.text(folder.name())
        return b''

    return cmp(_safeExtract(first[0]), _safeExtract(second[0]))


def _defaultComparator(first, second):
    return cmp(first[0], second[0])


_REWARDS_COMPARATORS = {(_RewardType.TROPHY): (partial(_compareRewardsByType, _RewardType.TROPHY)), 
   (_RewardType.DEVICE_FV): (partial(_compareRewardsByType, _RewardType.DEVICE_FV)), 
   (_RewardType.DEVICE_MI): (partial(_compareRewardsByType, _RewardType.DEVICE_MI)), 
   (_RewardType.GUIDE): _compareRewardsByNation, 
   (_RewardType.BROCHURE): _compareRewardsByNation, 
   (_RewardType.BOOK): _compareRewardsByNation, 
   (_RewardType.BLUEPRINT): _compareRewardsByNation, 
   (_RewardType.BATTLE_BOOSTER): _compareRewardsByArtifactName, 
   (_RewardType.EXP_EQUIPMENTS): (partial(_compareRewardsByType, _RewardType.EXP_EQUIPMENTS))}

def getRewardTypesComparator():
    return _rewardTypeComparator


def getRewardsComparator(rewardTypeName):
    return _REWARDS_COMPARATORS.get(_RewardType.makeValue(rewardTypeName), _defaultComparator)
