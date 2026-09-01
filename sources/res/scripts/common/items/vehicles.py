from __future__ import absolute_import, division
import BigWorld, copy, items, itertools, nation_change, nations, os, struct, typing
from builtins import zip
from future.utils import listitems, lmap, lrange, viewitems, viewkeys, viewvalues
from past.builtins import intern, long, xrange
from bwdebug import ERROR_MSG
from cache import cached_property
import persistent_data_cache_common as pdc
from Math import Vector2, Vector3
from backports.functools_lru_cache import lru_cache
from collections import namedtuple, defaultdict
from constants import ACTION_LABEL_TO_TYPE, ROLE_LABEL_TO_TYPE, ROLE_TYPE, DamageAbsorptionLabelToType, ROLE_LEVELS, ROLE_TYPE_TO_LABEL, VEHICLE_HEALTH_DECIMALS, IGR_TYPE, IS_RENTALS_ENABLED, IS_CELLAPP, IS_BASEAPP, IS_CLIENT, IS_UE_EDITOR, IS_BOT, IS_WEB, IS_PROCESS_REPLAY, ITEM_DEFS_PATH, SHELL_TYPES, VEHICLE_SIEGE_STATE, VEHICLE_MODE, VEHICLE_CLASSES, ShootImpulseApplicationPoint, SHELL_MECHANICS_TYPE, TrackBreakMode, HighExplosiveImpact, RandomizationType, INFINITE_SHELL_TAG, FORCE_FINITE_SHELL_TAG, MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL, VehiclePartName, VEHICLE_SECRET_TAG, ModuleKind, IS_COMMON_ENV
from debug_utils import LOG_WARNING, LOG_ERROR, LOG_CURRENT_EXCEPTION
from functools import partial
from items import ItemsPrices
from items import _xml, makeIntCompactDescrByID, parseIntCompactDescr, ITEM_TYPES
from items import common_extras, decodeEnum
from items import vehicle_items
from items._xml import cachedFloat
from items.attributes_helpers import onCollectAttributes, readModifiers, STATIC_ATTR_PREFIX, DYNAMIC_ATTR_PREFIX, MODIFIER_FILTER_TYPE
from items.artefacts_helpers import readKpi
from items.components import shared_components, gun_components, component_constants, shell_components, chassis_components, skills_constants
from items.components.c11n_constants import ApplyArea, CamouflageTilingType, CamouflageTilingTypeNameToType, ProjectionDecalMatchingTags
from items.components.gun_installation_components import GunInstallationSlot
from items.components.post_progression_components import PostProgressionCache, getActiveModifications
from items.components.shell_components import HighExplosiveImpactParams
from items.components.supply_slot_categories import LevelsFactor
from items.descr_modify_attrs import applyDescrModifyAttrs
from items.readers import chassis_readers
from items.readers import gun_readers
from items.readers import json_vehicle_reader
from items.readers import shared_readers
from items.readers import sound_readers
from items.readers import prefab_effects_readers
from items.writers import chassis_writers
from items.writers import gun_writers
from items.writers import shared_writers
from items.writers import sound_writers
from math import radians, cos, tan, atan, pi, isnan, degrees
from math_common import ceilTo, round_py2_style_int
from persistent_data_cache_common.serializers import WGPickleSerializer
from post_progression_common import POST_PROGRESSION_ALL_PRICES, ALLOWED_CURRENCIES_FOR_TREE_STEP, ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP, ALLOWED_CURRENCIES_FOR_CUSTOM_ROLE_SLOT_CHANGE, POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES, CUSTOM_ROLE_SLOT_CHANGE_PRICE, POST_PROGRESSION_BUY_MODIFICATIONS_PRICES, VEH_SKILL_TREE_ID_OFFSET
from py2to3.patched_future import with_metaclass
from soft_exception import SoftException
from typing import List, Optional, Tuple, Dict, Any, TYPE_CHECKING, Union, Generator, Set, FrozenSet, DefaultDict
from wrapped_reflection_framework import ReflectionMetaclass
from collector_vehicle import CollectorVehicleConsts
from material_kinds import IDS_BY_NAMES
from items.customization_slot_tags_validator import getDirectionAndFormFactorTags
from extension_utils import ResMgr, importClass
from battle_modifiers_common import BattleParams, BattleModifiers, ModifiersContext
from struct_helpers import unpackByte, packByte
if IS_UE_EDITOR:
    from meta_objects.items.vehicle_items_meta.utils import getEffectNameByEffect, getPrefabEffectNameByEffect, isSecondaryGun as isSecondaryGunCheck
    from combined_data_section import CombinedDataSection
    from reflection import ReflectedObject
    from wrapped_reflection_framework import reflectedNamedTuple
    import Math, tankArmor
if IS_CELLAPP or IS_CLIENT or IS_BOT or IS_UE_EDITOR:
    from ModelHitTester import HitTesterManager, BoundingBoxManager, createBBoxManagerForModels
if IS_CELLAPP or IS_CLIENT or IS_UE_EDITOR or IS_WEB or IS_PROCESS_REPLAY or IS_COMMON_ENV:
    import material_kinds
    from material_kinds import EFFECT_MATERIALS
if IS_CLIENT or IS_UE_EDITOR:
    from helpers import i18n
    from helpers import EffectsList
    import Vehicular
    from CustomEffect import SelectorDescFactory, CustomEffectsDescriptor, ExhaustEffectDescriptor
    import CustomEffect, ReloadEffect
elif IS_WEB:
    from web_stubs import i18n
if IS_CELLAPP:
    from vehicle_constants import OVERMATCH_MECHANICS_VER
if TYPE_CHECKING:
    from ResMgr import DataSection
    from items.artefacts import OptionalDevice, Equipment
    from items.components.supply_slots_components import SupplySlotsCache, SupplySlot
    from persistent_data_cache_common.types import TData
    from helpers.EntityExtra import EntityExtra
    from items.components.shared_components import MechanicsParams, GunMechanicsParams
VEHICLE_CLASS_TAGS = frozenset((b'lightTank', b'mediumTank', b'heavyTank', b'SPG', b'AT-SPG'))
VEHICLE_LEVELS_EARN_CRYSTAL = (
 10, 11)
MODES_WITHOUT_CRYSTAL_EARNINGS = set((b'bob', b'fallout', b'event_battles', b'battle_royale',
 b'clanWarsBattles'))
EXTENDED_VEHICLE_TYPE_ID_FLAG = 2

class VEHICLE_PHYSICS_TYPE():
    TANK = 0
    WHEELED_TECH = 1


VEHICLE_DEVICE_TYPE_NAMES = (
 b'engine', b'ammoBay', b'fuelTank', b'radio', b'track', b'gun', b'turretRotator', b'surveyingDevice', b'STUN_PLACEHOLDER',
 b'wheel')
VEHICLE_TANKMAN_TYPE_NAMES = (
 b'commander', b'driver', b'radioman', b'gunner', b'loader')
VEHICLE_DEVICE_INDICES = {deviceName: index for index, deviceName in enumerate(VEHICLE_DEVICE_TYPE_NAMES)}

def _makeExtraNames(tankmanNames):
    retVal = {}
    extraSuffix = b'Health'
    edgeCases = {b'track': [
                b'leftTrack0' + extraSuffix, b'rightTrack0' + extraSuffix], 
       b'radioman': [
                   b'radioman1' + extraSuffix, b'radioman2' + extraSuffix], 
       b'gunner': [
                 b'gunner1' + extraSuffix, b'gunner2' + extraSuffix], 
       b'loader': [
                 b'loader1' + extraSuffix, b'loader2' + extraSuffix]}
    for name in tankmanNames:
        retVal[name] = edgeCases.get(name, [name + extraSuffix])

    return retVal


DEVICE_TANKMAN_NAMES_TO_VEHICLE_EXTRA_NAMES = _makeExtraNames(VEHICLE_DEVICE_TYPE_NAMES + VEHICLE_TANKMAN_TYPE_NAMES)
PREMIUM_IGR_TAGS = frozenset((b'premiumIGR',))
MAX_OPTIONAL_DEVICES_SLOTS = 4
NUM_SHELLS_SLOTS = 3
EQUIPMENT_TYPES_ORDER = (
 items.EQUIPMENT_TYPES.regular, items.EQUIPMENT_TYPES.battleBoosters)
CAMOUFLAGE_KINDS = {b'winter': 0, b'summer': 1, b'desert': 2}
CAMOUFLAGE_KIND_INDICES = {v: k for k, v in viewitems(CAMOUFLAGE_KINDS)}
NATIONAL_EMBLEMS = set()
VEHICLE_MODE_FILE_SUFFIX = {(VEHICLE_MODE.DEFAULT): b'', 
   (VEHICLE_MODE.SIEGE): b'_siege_mode'}
NUM_INSCRIPTION_COLORS = 16
_ITEM_STATUS = vehicle_items.VEHICLE_ITEM_STATUS
g_list = None
g_cache = None
_VEHICLE_TYPE_XML_PATH = ITEM_DEFS_PATH + b'vehicles/'
_DEFAULT_HEALTH_BURN_PER_SEC_LOSS_FRACTION = 0.0875
_CUSTOMIZATION_EPOCH = 1306886400
_CUSTOMIZATION_XML_PATH = ITEM_DEFS_PATH + b'customization/'
_PREFAB_EFFECTS_XML_PATH = _VEHICLE_TYPE_XML_PATH + b'common/prefab_effects/'
_readTags = shared_readers.readAllowedTags
EmblemSlot = namedtuple(b'EmblemSlot', [
 117, 
 118, 
 119, 
 120, 
 121, 
 122, 
 123, 
 124, 
 125])
VEHICLE_MISC_ATTRIBUTE_FACTOR_NAMES = (
 b'fuelTankHealthFactor',
 b'repairSpeedFactor',
 b'additiveShotDispersionFactor',
 b'antifragmentationLiningFactor',
 b'circularVisionRadiusFactor',
 b'gunReloadTimeFactor',
 b'gunAimingTimeFactor',
 b'ammoBayHealthFactor',
 b'engineHealthFactor',
 b'chassisHealthFactor',
 b'vehicleByChassisDamageFactor',
 b'fuelTankHealthFactor',
 b'crewLevelIncrease',
 b'crewChanceToHitFactor',
 b'stunResistanceEffect',
 b'stunResistanceDuration',
 b'repeatedStunDurationFactor',
 b'healthFactor',
 b'damageFactor',
 b'enginePowerFactor',
 b'radioHealthFactor',
 b'turretRotatorHealthFactor',
 b'surveyingDeviceHealthFactor',
 b'gunHealthFactor',
 b'increaseEnemySpottingTime',
 b'decreaseOwnSpottingTime',
 b'demaskFoliageFactor',
 b'demaskMovingFactor',
 b'chassisRepairSpeedFactor',
 b'turretRotationSpeed',
 b'invisibilityAdditiveTerm',
 b'invisibilityMultFactor',
 b'forwardMaxSpeedKMHTerm',
 b'backwardMaxSpeedKMHTerm',
 b'onStillRotationSpeedFactor',
 b'onMoveRotationSpeedFactor',
 b'fireStartingChanceFactor',
 b'multShotDispersionFactor',
 b'isSetChassisMaxHealthAfterHysteresis',
 b'centerRotationFwdSpeedFactor',
 b'hullMaxHealth',
 b'turretMaxHealth',
 b'discreteDamageFactor',
 b'damageDistributionLowerBound',
 b'piercingDistributionLowerBound')
VEHICLE_MISC_ATTRIBUTE_FACTOR_INDICES = {value: index for index, value in enumerate(VEHICLE_MISC_ATTRIBUTE_FACTOR_NAMES)}

class EnhancementItem(object):
    __slots__ = (b'name', b'value', b'op')
    _operations = {b'mul': (lambda x, y: x * y), 
       b'sum': (lambda x, y: x + y)}
    _OPERATION_NAMES = list(_operations)
    _OPERATION_IDS_TO_NAMES = dict(enumerate(_OPERATION_NAMES))
    _OPERATION_NAMES_TO_IDS = {name: i for i, name in enumerate(_OPERATION_NAMES)}

    def __init__(self, name, value, op):
        self.name = name
        self.value = value
        self.op = op
        return

    def getOpIndex(self):
        return self._OPERATION_NAMES_TO_IDS[self.op]

    @classmethod
    def getOpName(cls, opIdx):
        return cls._OPERATION_IDS_TO_NAMES[opIdx]

    def applyFactor(self, factor):
        func = self._operations[self.op]
        return func(factor, self.value)


def vehicleAttributeFactors():
    factors = {b'engine/power': 1.0, 
       b'turret/rotationSpeed': 1.0, 
       b'circularVisionRadius': 1.0, 
       b'increaseCircularVisionRadius': 1.0, 
       b'penaltyToDamagedSurveyingDevice': 1.0, 
       b'invisibility': [
                       0.0, 1.0], 
       b'radio/distance': 1.0, 
       b'gun/rotationSpeed': 1.0, 
       b'chassis/shotDispersionFactors/movement': 1.0, 
       b'chassis/shotDispersionFactors/rotation': 1.0, 
       b'gun/shotDispersionFactors/turretRotation': 1.0, 
       b'gun/shots/speed': 1.0, 
       b'gun/reloadTime': 1.0, 
       b'gun/aimingTime': 1.0, 
       b'gun/piercing': 1.0, 
       b'gun/clipTimeBetweenShots': 1.0, 
       b'gun/canShoot': True, 
       b'gun/canClientChangeCurrentShell': True, 
       b'gun/canBurst': True, 
       b'gun/canReload': True, 
       b'engine/fireStartingChance': 1.0, 
       b'healthBurnPerSecLossFraction': 0.57, 
       b'repairSpeed': 1.0, 
       b'additiveShotDispersionFactor': 1.0, 
       b'brokenTrack': 0, 
       b'vehicle/rotationSpeed': 1.0, 
       b'vehicle/maxSpeed': 1.0, 
       b'vehicle/maxSpeed/forward': 1.0, 
       b'vehicle/maxSpeed/backward': 1.0, 
       b'vehicle/fwMaxSpeedBonus': 0.0, 
       b'vehicle/bkMaxSpeedBonus': 0.0, 
       b'chassis/terrainResistance': [
                                    1.0, 1.0, 1.0], 
       b'chassis/terrainResistanceRotation': [
                                            1.0, 1.0, 1.0], 
       b'ramming': 1.0, 
       b'crewLevelIncrease': 0.0, 
       b'crewChanceToHitFactor': 1.0, 
       b'damageMonitoringDelay': (float(b'inf')), 
       b'artNotificationDelay': (float(b'inf')), 
       b'crewRolesFactor': 1.0, 
       b'radioDistanceFactor': 0.0, 
       b'stunResistanceEffect': 0.0, 
       b'stunResistanceDuration': 0.0, 
       b'repeatedStunDurationFactor': 1.0, 
       b'healthFactor': 1.0, 
       b'damageFactor': 1.0, 
       b'enginePowerFactor': 1.0, 
       b'deathZones/sensitivityFactor': 1.0, 
       b'xRayFactor': 1.0, 
       b'tankAcceleration': 1.0, 
       b'reverseEnginePower': 1.0, 
       b'multShotDispersionFactor': 1.0, 
       b'gun/changeShell/reloadFactor': 1.0, 
       b'invisibilityFactorAtShot': 1.0, 
       b'demaskMovingFactor': 1.0, 
       b'demaskFoliageFactor': 1.0, 
       b'invisibilityAdditiveTerm': 0.0, 
       b'invisibilityMultFactor': 1.0, 
       b'foliageInvisibilityFactor': 1.0, 
       b'engineReduceFineFactor': 1.0, 
       b'ammoBayReduceFineFactor': 1.0, 
       b'chassis/forwardFrictionFactor': 1.0, 
       b'chassis/sideFrictionFactor': 1.0, 
       b'chassis/dirtReleaseRateFactor': 1.0, 
       b'chassis/maxDirtFactor': 1.0, 
       b'hull_aiming/pitch/wheelsCorrectionSpeedFactor': 1.0, 
       b'mutualHidingTimeFactor': 1.0, 
       b'discreteDamageFactor': 1.0, 
       b'gun/shotDispersionFactors/afterShot': 1.0, 
       b'gun/extraReloadTime': 0.0, 
       b'gun/isExtraFullGunReload': False, 
       b'gun/needToAdjustPotentialDamage': False, 
       b'inConeVision/visionFactor': 1.0, 
       b'inConeVision/demaskFoliageFactor': 1.0, 
       b'inConeVision/demaskMovingFactor': 1.0, 
       b'inConeVision/circularVisionRadiusFactor': 1.0}
    return factors


_DEFAULT_VEHICLE_ATTRIBUTE_FACTORS = vehicleAttributeFactors()

def defaultVehicleAttributeFactors():
    return _DEFAULT_VEHICLE_ATTRIBUTE_FACTORS


WHEEL_SIZE_COEF = 2.2
_g_prices = None
if IS_CLIENT:
    AIRSTRIKE_DATA = b'airstrikeData'
    ARTILLERY_DATA = b'artilleryData'
    DAMAGE_STICKERS_DATA = b'damageStickersData'
    _auxSerializingData = None

    class _CacheSerializer(WGPickleSerializer):
        __slots__ = ()

        def deserialize(self, serializedData):
            deserialized = super(_CacheSerializer, self).deserialize(serializedData)
            cache, effectList, auxiliaryData, prohibitedNumbers = deserialized
            CustomEffect.setEffectList(effectList)
            from items.components.c11n_components import PersonalNumberItem
            PersonalNumberItem.setProhibitedNumbers(prohibitedNumbers)
            for stickerParams, res in auxiliaryData[DAMAGE_STICKERS_DATA]:
                self._validate(BigWorld.wg_registerDamageSticker(*stickerParams), res)

            for airStrikeData, res in auxiliaryData[AIRSTRIKE_DATA]:
                self._validate(BigWorld.PyGroundEffectManager().loadAirstrike(airStrikeData), res)

            for artilleryData, res in auxiliaryData[ARTILLERY_DATA]:
                self._validate(BigWorld.PyGroundEffectManager().loadArtillery(artilleryData), res)

            return cache

        def serialize(self, rawData):
            global _auxSerializingData
            auxiliaryData, _auxSerializingData = _auxSerializingData, None
            from items.components.c11n_components import PersonalNumberItem
            return super(_CacheSerializer, self).serialize((
             rawData, CustomEffect.gEffectLists, auxiliaryData, PersonalNumberItem.getProhibitedNumbers()))

        def rollbackSideEffects(self):
            global _auxSerializingData
            BigWorld.PyGroundEffectManager().clear()
            BigWorld.wg_clearDamageStickers()
            CustomEffect.setEffectList({})
            from items.components.c11n_components import PersonalNumberItem
            PersonalNumberItem.setProhibitedNumbers(())
            _auxSerializingData = None
            return

        @staticmethod
        def _validate(actual, expected):
            if actual != expected:
                raise SoftException(b"Couldn't deserialize data properly!")
            return


    def _createCacheClient(preloadEverything, step):
        global _auxSerializingData
        _auxSerializingData = defaultdict(list)
        return _createCache(preloadEverything, step)


def _createCache(preloadEverything, step):
    global g_cache
    global g_list
    g_cache = Cache()
    if preloadEverything:
        g_cache.optionalDevices()
        g_cache.equipments()
        g_cache.playerEmblems()
        for nationID in xrange(len(nations.NAMES)):
            g_cache.customization(nationID)
            for vehicleTypeID in g_list.getList(nationID):
                g_cache.vehicle(nationID, vehicleTypeID)
                if step is not None:
                    step()

        g_cache.customization20()
        g_cache.supplySlots()
        g_cache.postProgression()
    return g_cache


def init(preloadEverything, pricesToCollect, step=None):
    global _g_prices
    global g_cache
    global g_list
    if IS_CLIENT or IS_CELLAPP or IS_BOT:
        import vehicle_extras
    _g_prices = pricesToCollect
    g_list = pdc.load(b'vehicles_list', VehicleList)
    if IS_CLIENT and pdc.isEnabled():
        createCache, serializer = _createCacheClient, _CacheSerializer()
    else:
        createCache, serializer = _createCache, None
    g_cache = pdc.load(b'vehicles_cache', partial(createCache, preloadEverything, step), serializer)
    if preloadEverything:
        _g_prices = None
    return


def reload(full=True):
    import vehicle_extras
    vehicle_extras.reload()
    from sys import modules
    from py2to3.moves import importLib
    importLib.reload(modules[reload.__module__])
    init(full, None)
    return


class VehicleDescriptor(with_metaclass(ReflectionMetaclass, object)):
    __slots__ = (b'enhancements', b'turret', b'gun', b'hull', b'engine', b'fuelTank', b'radio', b'chassis', b'turrets', b'optionalDevices', b'shot', b'supplySlots', b'camouflages', b'playerEmblems', b'playerInscriptions', b'type', b'name', b'level', b'extras', b'extrasDict', b'miscAttrs', b'physics', b'xphysics', b'visibilityCheckPoints', b'observerPosOnChassis', b'observerPosOnTurret', b'battleModifiers', b'gunInstallations', b'_customRoleSlotTypeId', b'_modifications', b'_optDevSlotsMap', b'_defaultMaxHealth', b'_maxHealth', b'__activeTurretPos', b'__activeGunShotIdx', b'__activeGunShotPosition', b'__boundingRadius', b'mechanicsParams', b'descrModifyAttrsApplied')

    def __init__(self, compactDescr=None, typeID=None, typeName=None, vehMode=VEHICLE_MODE.DEFAULT, xmlPath=None, extData=None, forceUpdateAttrs=False):
        extData = extData if extData is not None else {}
        battleModifiers = self.__getExtDataValue(extData, b'battleModifiers')
        self.battleModifiers = battleModifiers if battleModifiers is not None else BattleModifiers()
        self.enhancements = []
        self.descrModifyAttrsApplied = False
        vehType = None
        if compactDescr is None:
            vehicleItem = None
            if typeID is not None:
                nationID, vehicleTypeID = typeID
            elif typeName is not None:
                nationID, vehicleTypeID = g_list.getIDsByName(typeName)
            elif xmlPath is not None:
                nation, vehicleType = _deduceNamesFromTankXmlPath(xmlPath)
                typeName = nation + b':' + vehicleType
                try:
                    nationID, vehicleTypeID = g_list.getIDsByName(typeName)
                    vehicleItem = g_list.getList(nationID)[vehicleTypeID]
                except Exception:
                    nationID = nations.INDICES[nation]
                    vehicleTypeID = 65535

            if xmlPath is None:
                type = g_cache.vehicle(nationID, vehicleTypeID)
            elif vehicleItem is None:
                vehicleItem = vehicle_items.VehicleItem(ITEM_TYPES[b'vehicle'], vehicleTypeID, typeName, makeIntCompactDescrByID(b'vehicle', nationID, vehicleTypeID))
            if vehMode != VEHICLE_MODE.DEFAULT:
                xmlName, xmlExt = os.path.splitext(xmlPath)
                xmlPath = xmlName + VEHICLE_MODE_FILE_SUFFIX[vehMode] + xmlExt
            type = VehicleType(nationID, vehicleItem, xmlPath, vehMode)
            vehType = type
            if IS_UE_EDITOR:
                ReflectedObject(type).edVisible = vehMode is VEHICLE_MODE.DEFAULT
            turretDescr = type.turrets[0][0]
            header = items.ITEM_TYPES.vehicle + (nationID << 4)
            ext = vehicleTypeID >> 8
            header += EXTENDED_VEHICLE_TYPE_ID_FLAG if ext else 0
            compactDescr = struct.pack(b'<2B', header, vehicleTypeID & 255)
            compactDescr += packByte(ext) if ext else b''
            compactDescr += struct.pack(b'<6HB', type.chassis[0].id[1], type.engines[0].id[1], type.fuelTanks[0].id[1], type.radios[0].id[1], turretDescr.id[1], turretDescr.guns[0].id[1], 0)
        self.__initFromCompactDescr(compactDescr, vehMode, vehType)
        self.__applyExternalData(extData)
        self.__updateAttributes(onAnyApp=forceUpdateAttrs)
        return

    @property
    def objectSlots(self):
        gunObjectSlots = itertools.chain.from_iterable(gunInstallation.objectSlots for gunInstallation in self.gunInstallations)
        return list(itertools.chain([(VehiclePartName.CHASSIS, slot) for slot in self.chassis.objectSlots], [(VehiclePartName.HULL, slot) for slot in self.hull.objectSlots], [(VehiclePartName.TURRET, slot) for slot in self.turret.objectSlots], [(VehiclePartName.GUN, slot) for slot in gunObjectSlots]))

    @property
    def maxHealth(self):
        if IS_BASEAPP:
            if not self.physics:
                self.__updateAttributes(onAnyApp=True)
        return self._maxHealth

    @property
    def defaultMaxHealth(self):
        return self._defaultMaxHealth

    def getShot(self, shotIdx=None):
        if shotIdx is None:
            return self.shot
        else:
            return self.gun.shots[shotIdx]

    def getSlotPrefabs(self, outfit=None, styleName=None):
        if not styleName and outfit and outfit.styleId:
            style = g_cache.customization20().styles.get(outfit.styleId)
            styleName = style.modelsSet if style else None
        allSlotPrefabs = [
         self.chassis.slotPrefabs,
         self.hull.slotPrefabs,
         self.turret.slotPrefabs] + [gunInstallation.getSlotPrefabs(styleName) for gunInstallation in self.gunInstallations]
        result = list(itertools.chain.from_iterable(allSlotPrefabs))
        if IS_UE_EDITOR:
            for _, slot in self.objectSlots:
                if not slot.edVisible and slot.prefab:
                    result.remove((slot.name, slot.prefab))

        return result

    def __set_activeTurretPos(self, turretPosition):
        self.turret, self.gun = self.turrets[turretPosition]
        self.gunInstallations = [GunInstallationSlot(0, self.gun)]
        if self.gun.secondaryGunID:
            self.gunInstallations.append(GunInstallationSlot(1, _descrByID(self.turret.secondaryGuns, self.gun.secondaryGunID)))
        self.__activeTurretPos = turretPosition
        self.activeGunShotPosition = self.turret.gunPosition + self.gun.shotOffset
        self.activeGunShotIndex = 0
        return

    activeTurretPosition = property((lambda self: self.__activeTurretPos), __set_activeTurretPos)

    def __set_activeGunShotIndex(self, shotIndex):
        self.shot = self.gun.shots[shotIndex]
        self.__activeGunShotIdx = shotIndex
        return

    activeGunShotIndex = property((lambda self: self.__activeGunShotIdx), __set_activeGunShotIndex)

    def __set_activeGunShotPosition(self, gunShotPos):
        self.__activeGunShotPosition = gunShotPos
        return

    activeGunShotPosition = property((lambda self: self.__activeGunShotPosition), __set_activeGunShotPosition)
    modifications = property((lambda self: self._modifications))
    customRoleSlotTypeId = property((lambda self: self._customRoleSlotTypeId))
    hasSiegeMode = property((lambda self: self.type.hasSiegeMode))
    hasAutoSiegeMode = property((lambda self: self.type.hasAutoSiegeMode))
    isWheeledVehicle = property((lambda self: self.type.isWheeledVehicle))
    hasSpeedometer = property((lambda self: self.type.hasSpeedometer))
    isTwinGunVehicle = property((lambda self: b'twinGun' in self.gun.tags))
    isDualgunVehicle = property((lambda self: b'dualGun' in self.gun.tags))
    hasDualAccuracy = property((lambda self: b'dualAccuracy' in self.gun.tags))
    isAutoShootGunVehicle = property((lambda self: b'autoShoot' in self.gun.tags))
    isUnlimitedClipVehicle = property((lambda self: b'unlimitedClip' in self.gun.tags))
    hasTurboshaftEngine = property((lambda self: self.type.hasTurboshaftEngine))
    hasHydraulicChassis = property((lambda self: self.type.hasHydraulicChassis))
    hasCharge = property((lambda self: self.type.hasCharge))
    hasRocketAcceleration = property((lambda self: self.type.hasRocketAcceleration))
    hasWheeledDash = property((lambda self: self.type.hasWheeledDash))
    hasStagedJetBoosters = property((lambda self: self.type.hasStagedJetBoosters))
    hasBurst = property((lambda self: self.gun.burst != component_constants.DEFAULT_GUN_BURST))
    role = property((lambda self: self.type.role))
    isPitchHullAimingAvailable = property((lambda self: self.type.hullAimingParams[b'pitch'][b'isAvailable']))
    isYawHullAimingAvailable = property((lambda self: self.type.hullAimingParams[b'yaw'][b'isAvailable']))

    @property
    def minHullAimingPitch(self):
        return self.type.hullAimingParams[b'pitch'][b'wheelsCorrectionAngles'][b'pitchMin']

    @property
    def maxHullAimingPitch(self):
        return self.type.hullAimingParams[b'pitch'][b'wheelsCorrectionAngles'][b'pitchMax']

    @property
    def hasBurnout(self):
        return self.isWheeledVehicle and self.chassisCfg[b'burnout'] is not None

    @property
    def isWheeledOnSpotRotation(self):
        return self.isWheeledVehicle and self.chassisCfg[b'isWheeledOnSpotRotation']

    @property
    def isWheeledOnMoveRotation(self):
        return self.isWheeledVehicle and self.chassisCfg[b'isWheeledOnMoveRotation']

    @property
    def isTrackWithinTrack(self):
        return self.chassis.isTrackWithinTrack

    @property
    def rollingFriction(self):
        grounds = self.chassisCfg[b'grounds']
        return (grounds[b'firm'][b'rollingFriction'], grounds[b'medium'][b'rollingFriction'],
         grounds[b'soft'][b'rollingFriction'])

    @property
    def chassisCfg(self):
        physics = self.type.xphysics if IS_CLIENT or IS_WEB else self.type.xphysics[b'detailed']
        return physics[b'chassis'][self.chassis.name]

    def __getIsHullAimingAvailable(self):
        hap = self.type.hullAimingParams
        return hap[b'yaw'][b'isAvailable'] or hap[b'pitch'][b'isAvailable']

    isHullAimingAvailable = property(__getIsHullAimingAvailable)

    def onSiegeStateChanged(self, siegeMode):
        return

    def __get_boundingRadius(self):
        radius = getattr(self, b'_VehicleDescriptor__boundingRadius', None)
        if radius is None:
            chassisDescr = self.chassis
            hullDescr = self.hull
            hullOnChassisOffsetZ = chassisDescr.hullPosition.z
            turretOnHullOffsetZ = hullDescr.turretPositions[0].z
            gunOnTurretOffsetZ = self.turret.gunPosition.z
            chassisBbox = chassisDescr.totalBBox
            hullBbox = hullDescr.hitTester.bbox
            bboxMin = Vector2(min(chassisBbox[0].x, hullBbox[0].x), min(chassisBbox[0].z, hullBbox[0].z + hullOnChassisOffsetZ))
            bboxMax = Vector2(max(chassisBbox[1].x, hullBbox[1].x), max(chassisBbox[1].z, hullBbox[1].z + hullOnChassisOffsetZ))
            gunOnTurretMaxZ = gunOnTurretOffsetZ + self.gun.hitTester.bbox[1].z
            radius = max(bboxMin.length, bboxMax.length, abs(hullOnChassisOffsetZ + turretOnHullOffsetZ + gunOnTurretMaxZ), abs(hullOnChassisOffsetZ + turretOnHullOffsetZ - gunOnTurretMaxZ))
            self.__boundingRadius = radius
        return radius

    boundingRadius = property(__get_boundingRadius)

    def __applyExternalData(self, extData):
        self.battleModifiers = ModifiersContext(self.battleModifiers, vehType=self.type)
        self._customRoleSlotTypeId = 0
        self._modifications = []
        value = self.__getExtDataValue(extData, b'customRoleSlotTypeId') or 0
        self.installCustomRoleSlot(value, False)
        value = self.__getExtDataValue(extData, b'vehPostProgression') or []
        modificationIDs = getActiveModifications(value, g_cache.postProgression(), self.type.postProgressionTree)
        self.installModifications(modificationIDs, False)
        return

    def installCustomRoleSlot(self, customRoleSlotTypeId, rebuildAttrs=True):
        self._customRoleSlotTypeId = customRoleSlotTypeId
        self._updateSupplySlots()
        self._rebuildOptDevSlotsMap()
        if rebuildAttrs:
            self.__updateAttributes(updateDescrAttrs=False)
        return

    def installModifications(self, modificationIDs, rebuildAttrs=True):
        self._modifications = modificationIDs
        if rebuildAttrs:
            self.__updateAttributes()
        return

    def setCamouflage(self, position, camouflageID, startTime, durationDays):
        p = self.camouflages
        if camouflageID is None:
            startTime = _CUSTOMIZATION_EPOCH
            durationDays = 0
            p[position]
        else:
            descr = g_cache.customization(self.type.customizationNationID)[b'camouflages'][camouflageID]
            if position is None:
                position = descr[b'kind']
            elif position != descr[b'kind']:
                raise SoftException(b'wrong camouflage kind = %d' % position)
            cd = self.type.compactDescr
            if cd in descr[b'deny'] or descr[b'allow'] and cd not in descr[b'allow']:
                raise SoftException(b'camouflage = %d is incompatible with vehicle' % cd)
            startTime = int(startTime // 60) * 60
            if startTime < _CUSTOMIZATION_EPOCH:
                raise SoftException(b'wrong camouflage start time = %d' % startTime)
            durationDays = int(durationDays)
            if not 0 <= durationDays <= 255:
                raise SoftException(b'wrong camouflage duration = %d' % durationDays)
        self.camouflages = p[:position] + ((camouflageID, startTime, durationDays),) + p[position + 1:]
        return

    def setPlayerEmblem(self, position, emblemID, startTime, durationDays):
        p = self.playerEmblems
        p[position]
        defEmblemID = self.type.defaultPlayerEmblemID
        if emblemID is None or emblemID == defEmblemID:
            emblemID = defEmblemID
            startTime = _CUSTOMIZATION_EPOCH
            durationDays = 0
        else:
            groups, emblems, _ = g_cache.playerEmblems()
            emblem = emblems[emblemID]
            groupName = emblem[0]
            group = groups[groupName]
            eNations = group[3]
            if eNations is not None and self.type.customizationNationID not in eNations:
                raise SoftException(b'emblem nation mismatch')
            allow, deny = group[4:6]
            cd = self.type.compactDescr
            if cd in deny:
                raise SoftException(b'emblem is incompatible with vehicle')
            if allow and cd not in allow:
                raise SoftException(b'emblem is incompatible with vehicle')
            startTime = int(startTime // 60) * 60
            if startTime < _CUSTOMIZATION_EPOCH:
                raise SoftException(b'wrong emblem start time')
            durationDays = int(durationDays)
            if not 0 <= durationDays <= 255:
                raise SoftException(b'wrong emblem duration')
        self.playerEmblems = p[:position] + ((emblemID, startTime, durationDays),) + p[position + 1:]
        return

    def setPlayerInscription(self, position, inscriptionID, startTime, durationDays, color):
        if IS_CLIENT:
            LOG_WARNING(b'This method cannot be executed on client')
            return
        else:
            p = self.playerInscriptions
            p[position]
            if inscriptionID is None:
                startTime = _CUSTOMIZATION_EPOCH
                durationDays = 0
                color = 0
            else:
                customization = g_cache.customization(self.type.customizationNationID)
                groupName = customization[b'inscriptions'][inscriptionID][0]
                customization[b'inscriptionColors'][color]
                allow, deny = customization[b'inscriptionGroups'][groupName][3:5]
                cd = self.type.compactDescr
                if cd in deny:
                    raise SoftException(b'inscription is incompatible with vehicle')
                if allow and cd not in allow:
                    raise SoftException(b'inscription is incompatible with vehicle')
                startTime = int(startTime // 60) * 60
                if startTime < _CUSTOMIZATION_EPOCH:
                    raise SoftException(b'wrong inscription start time')
                durationDays = int(durationDays)
                if not 0 <= durationDays <= 255:
                    raise SoftException(b'wrong inscription duration')
            self.playerInscriptions = p[:position] + ((inscriptionID, startTime, durationDays, color),) + p[position + 1:]
            return

    def getComponentsByType(self, itemTypeName, positionIndex=0):
        if itemTypeName == b'vehicleChassis':
            return (self.chassis, self.type.chassis)
        if itemTypeName == b'vehicleEngine':
            return (self.engine, self.type.engines)
        if itemTypeName == b'vehicleRadio':
            return (self.radio, self.type.radios)
        if itemTypeName == b'vehicleFuelTank':
            return (self.fuelTank, self.type.fuelTanks)
        if itemTypeName == b'vehicleTurret':
            return (self.turrets[positionIndex][0], self.type.turrets[positionIndex])
        if itemTypeName == b'vehicleGun':
            turretDescr, gunDescr = self.turrets[positionIndex]
            return (
             gunDescr, turretDescr.guns)
        return

    def mayInstallTurret(self, turretCompactDescr, gunCompactDescr, positionIndex=0, optDevicesLayouts=None):
        selfType = self.type
        selfTurrets = self.turrets
        itemTypeID, nationID, turretID = parseIntCompactDescr(turretCompactDescr)
        if items.ITEM_TYPE_NAMES[itemTypeID] != b'vehicleTurret':
            return (False, b'wrong item type')
        else:
            if nationID != selfType.id[0]:
                return (False, b'wrong nation')
            if gunCompactDescr == 0:
                gunID = selfTurrets[positionIndex][1].id[1]
            else:
                itemTypeID, nationID, gunID = parseIntCompactDescr(gunCompactDescr)
                if items.ITEM_TYPE_NAMES[itemTypeID] != b'vehicleGun':
                    return (False, b'wrong item type')
                if nationID != selfType.id[0]:
                    return (False, b'wrong nation')
            newTurretDescr = _findDescrByID(selfType.turrets[positionIndex], turretID)
            if newTurretDescr is None:
                return (False, b'not for this vehicle type')
            newGunDescr = _findDescrByID(newTurretDescr.guns, gunID)
            if newGunDescr is None:
                if gunCompactDescr not in selfType.installableComponents:
                    return (False, b'not for this vehicle type')
                return (False, b'not for current vehicle')
            result, reason = self.__checkCompatibilityWithOptDevices(optDevicesLayouts)
            if not result:
                return (result, reason)
            return (True, None)

    def installTurret(self, turretCompactDescr, gunCompactDescr, positionIndex=0):
        turretID = parseIntCompactDescr(turretCompactDescr)[2]
        if gunCompactDescr == 0:
            gunID = self.turrets[positionIndex][1].id[1]
        else:
            gunID = parseIntCompactDescr(gunCompactDescr)[2]
        prevTurretDescr, prevGunDescr = self.turrets[positionIndex]
        newTurretDescr = _descrByID(self.type.turrets[positionIndex], turretID)
        newGunDescr = _descrByID(newTurretDescr.guns, gunID)
        self.turrets[positionIndex] = (
         newTurretDescr, newGunDescr)
        if len(self.type.hulls) > 1:
            self.hull = self.__selectBestHull(self.turrets, self.chassis)
        if self.__activeTurretPos == positionIndex:
            self.activeTurretPosition = positionIndex
        removed = [prevTurretDescr.compactDescr]
        if gunCompactDescr != 0:
            removed.append(prevGunDescr.compactDescr)
        self.__updateAttributes()
        return removed

    def installEnhancements(self, enhancements, rebuildAttrs=True):
        for modsInSlot in viewvalues(enhancements):
            for mod in viewvalues(modsInSlot):
                for attr in mod[b'attributes']:
                    self.enhancements.append(EnhancementItem(attr[b'name'], attr[b'value'], attr[b'operation']))

        if rebuildAttrs:
            self.__updateAttributes()
        return

    def mayInstallComponent(self, compactDescr, positionIndex=0, optDevicesLayouts=None):
        itemTypeID, nationID, compID = parseIntCompactDescr(compactDescr)
        itemTypeName = items.ITEM_TYPE_NAMES[itemTypeID]
        selfType = self.type
        if nationID != selfType.id[0]:
            return (
             False, b'wrong nation')
        if itemTypeName == b'vehicleGun':
            hullDescr = self.hull
            turretDescr = self.turrets[positionIndex][0]
            newDescr = _findDescrByID(turretDescr.guns, compID)
            if newDescr is None and positionIndex in hullDescr.fakeTurrets[b'lobby']:
                newDescr, turretDescr, hullDescr = self.__selectTurretForGun(compID, positionIndex)
        elif itemTypeName == b'vehicleChassis':
            newDescr = _findDescrByID(selfType.chassis, compID)
        elif itemTypeName == b'vehicleEngine':
            newDescr = _findDescrByID(selfType.engines, compID)
        elif itemTypeName == b'vehicleRadio':
            newDescr = _findDescrByID(selfType.radios, compID)
        elif itemTypeName == b'vehicleFuelTank':
            newDescr = _findDescrByID(selfType.fuelTanks, compID)
        else:
            return (
             False, b'wrong item type')
        if newDescr is None:
            if compactDescr not in selfType.installableComponents:
                return (False, b'not for this vehicle type')
            return (False, b'not for current vehicle')
        else:
            result, reason = self.__checkCompatibilityWithOptDevices(optDevicesLayouts)
            if not result:
                return (result, reason)
            return (True, None)

    def rebuildAttrs(self):
        return self.__updateAttributes()

    def installComponent(self, compactDescr, positionIndex=0):
        itemTypeID, nationID, compID = parseIntCompactDescr(compactDescr)
        itemTypeName = items.ITEM_TYPE_NAMES[itemTypeID]
        if nationID != self.type.id[0]:
            raise SoftException(b'incompatible nation of component')
        if itemTypeName == b'vehicleGun':
            return self.__installGun(compID, positionIndex)
        if itemTypeName == b'vehicleChassis':
            attrName = b'chassis'
            compList = self.type.chassis
        elif itemTypeName == b'vehicleEngine':
            attrName = b'engine'
            compList = self.type.engines
        elif itemTypeName == b'vehicleRadio':
            attrName = b'radio'
            compList = self.type.radios
        elif itemTypeName == b'vehicleFuelTank':
            attrName = b'fuelTank'
            compList = self.type.fuelTanks
        prevDescr = getattr(self, attrName)
        newDescr = _descrByID(compList, compID)
        setattr(self, attrName, newDescr)
        if attrName == b'chassis' and len(self.type.hulls) > 1:
            self.hull = self.__selectBestHull(self.turrets, self.chassis)
        self.__updateAttributes()
        return (
         prevDescr.compactDescr,)

    def mayInstallOptionalDevice(self, compactDescr, slotIdx):
        itemTypeID, _, deviceID = parseIntCompactDescr(compactDescr)
        if items.ITEM_TYPE_NAMES[itemTypeID] != b'optionalDevice':
            return (False, b'wrong item type')
        else:
            device = g_cache.optionalDevices()[deviceID]
            prevDevices = self.optionalDevices
            if device in prevDevices:
                return (False, b'already installed')
            if slotIdx >= self.supplySlots.getAmountForType(ITEM_TYPES.optionalDevice):
                return (False, (b'Wrong slotIDx ({})').format(slotIdx))
            for idx, installedDevice in enumerate(self.optionalDevices):
                if idx != slotIdx and installedDevice and not device.checkCompatibilityWithOther(installedDevice):
                    return (False, b'similar device already installed')

            res = device.checkCompatibilityWithVehicle(self)
            if not res[0]:
                return res
            return (True, None)

    def mayInstallOptDevsSequence(self, optDevSequence):
        result, errorStr = self.supplySlots.checkLayoutCompatibility(ITEM_TYPES.optionalDevice, optDevSequence)
        if not result:
            return (False, errorStr)
        else:
            optDevs = [getItemByCompactDescr(cd) if cd != 0 else None for cd in optDevSequence]
            optDevsLen = len(optDevs)
            for i in range(0, optDevsLen):
                device = optDevs[i]
                if device is None:
                    continue
                result, errorStr = device.checkCompatibilityWithVehicle(self)
                if not result:
                    return (False, errorStr)
                for j in range(i + 1, optDevsLen):
                    otherDevice = optDevs[j]
                    if otherDevice is not None and not device.checkCompatibilityWithOther(otherDevice):
                        return (False, b'Similar devices in sequence')

            return (
             True, None)

    def installOptDevsSequence(self, optDevSequence):
        optDevs = [getItemByCompactDescr(cd) if cd != 0 else None for cd in optDevSequence]
        self.optionalDevices = optDevs
        self._rebuildOptDevSlotsMap()
        self.__updateAttributes(updateDescrAttrs=False)
        return

    def installOptionalDevice(self, compactDescr, slotIdx, rebuildAttrs=True):
        device = g_cache.optionalDevices()[parseIntCompactDescr(compactDescr)[2]]
        devices = self.optionalDevices
        prevDevice = devices[slotIdx]
        devices[slotIdx] = device
        self._optDevSlotsMap[compactDescr] = self.supplySlots.getSlotByIdxInItemType(ITEM_TYPES.optionalDevice, slotIdx)
        if rebuildAttrs:
            self.__updateAttributes(updateDescrAttrs=False)
        if prevDevice is None:
            return (component_constants.EMPTY_TUPLE, component_constants.EMPTY_TUPLE)
        else:
            if prevDevice.removable:
                return ((prevDevice.compactDescr,), component_constants.EMPTY_TUPLE)
            return (component_constants.EMPTY_TUPLE, (prevDevice.compactDescr,))

    def removeOptionalDevice(self, slotIdx, rebuildAttrs=True):
        device = self.optionalDevices[slotIdx]
        if device is None:
            return (component_constants.EMPTY_TUPLE, component_constants.EMPTY_TUPLE)
        else:
            self.optionalDevices[slotIdx] = None
            self._optDevSlotsMap.pop(device.compactDescr, None)
            if rebuildAttrs:
                self.__updateAttributes(updateDescrAttrs=False)
            if device.removable:
                return ((device.compactDescr,), component_constants.EMPTY_TUPLE)
            return (component_constants.EMPTY_TUPLE, (device.compactDescr,))

    def maySwapOptionalDevice(self, leftID, rightID):
        if leftID >= self.supplySlots.getAmountForType(ITEM_TYPES.optionalDevice):
            return (False, (b'Wrong slotIDx ({})').format(leftID))
        else:
            if rightID >= self.supplySlots.getAmountForType(ITEM_TYPES.optionalDevice):
                return (False, (b'Wrong slotIDx ({})').format(rightID))
            return (True, None)

    def swapOptionalDevice(self, leftID, rightID):
        devices = self.optionalDevices
        leftDevice, rightDevice = devices[leftID], devices[rightID]
        devices[leftID], devices[rightID] = rightDevice, leftDevice
        if leftDevice:
            self._optDevSlotsMap[leftDevice.compactDescr] = self.supplySlots.getSlotByIdxInItemType(ITEM_TYPES.optionalDevice, rightID)
        if rightDevice:
            self._optDevSlotsMap[rightDevice.compactDescr] = self.supplySlots.getSlotByIdxInItemType(ITEM_TYPES.optionalDevice, leftID)
        self.__updateAttributes(updateDescrAttrs=False)
        return

    def iterOptDevsWithSlots(self):
        optDevSlotIDs = self.supplySlots.getSlotIDsByType(ITEM_TYPES.optionalDevice)
        supplySlots = g_cache.supplySlots()
        for optDev, slotID in zip(self.optionalDevices, optDevSlotIDs):
            yield (optDev, supplySlots.getSlotDescr(slotID))

        return

    def _rebuildOptDevSlotsMap(self):
        self._optDevSlotsMap = {}
        for optDev, slot in self.iterOptDevsWithSlots():
            if optDev is not None:
                self._optDevSlotsMap[optDev.compactDescr] = slot

        return

    def getOptDevSupplySlot(self, optDevCompDescr):
        return self._optDevSlotsMap.get(optDevCompDescr, None)

    def _updateSupplySlots(self):
        supplySlotIDs = list(self.type.supplySlots.slotIDs)
        customRoleSlotTypeId = self._customRoleSlotTypeId
        if customRoleSlotTypeId:
            supplySlots = g_cache.supplySlots()
            for slotIdx, slotID in enumerate(supplySlotIDs):
                slotDescr = supplySlots.getSlotDescr(slotID)
                if slotDescr.itemType == ITEM_TYPES.optionalDevice and not slotDescr.categories:
                    supplySlotIDs[slotIdx] = customRoleSlotTypeId
                    break

        self.supplySlots = g_cache.supplySlotsStorage().getStorage(supplySlotIDs)
        return

    def makeCompactDescr(self):
        type = self.type
        pack = struct.pack
        components = pack(b'<4H', self.chassis.id[1], self.engine.id[1], self.fuelTank.id[1], self.radio.id[1])
        turrets = self.turrets
        for n in xrange(len(type.turrets)):
            turretDescr, gunDescr = turrets[n]
            components += pack(b'<2H', turretDescr.id[1], gunDescr.id[1])

        optDevSlots = self.supplySlots.getAmountForType(ITEM_TYPES.optionalDevice)
        if len(self.optionalDevices) != optDevSlots:
            raise SoftException((b'Optional devices num ({}) is incorrect. Should be equal to {}').format(len(self.optionalDevices), optDevSlots))
        optionalDevices = b''
        optionalDeviceSlots = 0
        for device in self.optionalDevices:
            optionalDeviceSlots <<= 1
            if device is not None:
                optionalDevices = pack(b'<H', device.id[1]) + optionalDevices
                optionalDeviceSlots |= 1

        enhancements = b''
        if self.enhancements:
            enhancements = pack(b'<B', len(self.enhancements))
            for enhancement in self.enhancements:
                enhancements += pack(b'<BfB', VEHICLE_MISC_ATTRIBUTE_FACTOR_INDICES[enhancement.name], enhancement.value * 1000, enhancement.getOpIndex())

        emblemPositions = 0
        emblems = b''
        for idx, item in enumerate(self.playerEmblems):
            if item[0] is not None and item[0] != type.defaultPlayerEmblemID:
                emblemPositions |= 1 << idx
                emblems += _packIDAndDuration(*item)

        inscriptions = b''
        for idx, item in enumerate(self.playerInscriptions):
            if item[0] is not None:
                emblemPositions |= 1 << idx + 4
                inscriptions += _packIDAndDuration(item[0], item[1], item[2]) + packByte(item[3])

        camouflages = b''
        for item in self.camouflages:
            if item[0] is not None:
                camouflages += _packIDAndDuration(*item)

        return _combineVehicleCompactDescr(type, components, optionalDeviceSlots, optionalDevices, enhancements, emblemPositions, emblems, inscriptions, camouflages)

    def getCost(self, itemPrices):
        type = self.type
        cost = itemPrices[type.compactDescr]
        for idx in xrange(len(self.turrets)):
            currentTurret, currentGun = self.turrets[idx]
            defaultTurret = type.turrets[idx][0]
            cost = _summPriceDiff(cost, itemPrices[currentTurret.compactDescr], itemPrices[defaultTurret.compactDescr])
            cost = _summPriceDiff(cost, itemPrices[currentGun.compactDescr], itemPrices[defaultTurret.guns[0].compactDescr])

        cost = _summPriceDiff(cost, itemPrices[self.chassis.compactDescr], itemPrices[type.chassis[0].compactDescr])
        cost = _summPriceDiff(cost, itemPrices[self.engine.compactDescr], itemPrices[type.engines[0].compactDescr])
        cost = _summPriceDiff(cost, itemPrices[self.fuelTank.compactDescr], itemPrices[type.fuelTanks[0].compactDescr])
        cost = _summPriceDiff(cost, itemPrices[self.radio.compactDescr], itemPrices[type.radios[0].compactDescr])
        for device in self.optionalDevices:
            if device is not None:
                cost = _summPriceDiff(cost, itemPrices[device.compactDescr], (0, 0))

        return cost

    def getMaxRepairCost(self):
        type = self.type
        cost = self.maxHealth * type.repairCost
        for turretDescr, gunDescr in self.turrets:
            cost += gunDescr.maxRepairCost + turretDescr.turretRotatorHealth.maxRepairCost + turretDescr.surveyingDeviceHealth.maxRepairCost

        cost += self.hull.ammoBayHealth.maxRepairCost + self.chassis.maxRepairCost * 2 + self.engine.maxRepairCost + self.fuelTank.maxRepairCost + self.radio.maxRepairCost
        return cost

    def getDevices(self):
        defComps = []
        instComps = []
        type = self.type
        instComps.append(self.chassis.compactDescr)
        defComps.append(type.chassis[0].compactDescr)
        instComps.append(self.engine.compactDescr)
        defComps.append(type.engines[0].compactDescr)
        instComps.append(self.fuelTank.compactDescr)
        defComps.append(type.fuelTanks[0].compactDescr)
        instComps.append(self.radio.compactDescr)
        defComps.append(type.radios[0].compactDescr)
        for (turretDescr, gunDescr), turrets in zip(self.turrets, type.turrets):
            instComps.append(turretDescr.compactDescr)
            defComps.append(turrets[0].compactDescr)
            instComps.append(gunDescr.compactDescr)
            defComps.append(turrets[0].guns[0].compactDescr)

        optDevices = []
        for device in self.optionalDevices:
            if device is not None:
                optDevices.append(device.compactDescr)

        return (
         defComps, instComps, optDevices)

    def getHitTesterManagers(self):
        hitTesters = [
         self.chassis.hitTesterManager, self.hull.hitTesterManager]
        for turretDescr, gunDescr in self.turrets:
            hitTesters.append(turretDescr.hitTesterManager)
            hitTesters.append(gunDescr.hitTesterManager)

        if self.isWheeledVehicle and self.chassis.generalWheelsAnimatorConfig is None:
            for wheel in self.chassis.wheels.wheels:
                hitTesters.append(wheel.hitTesterManager)

        if not self.isWheeledVehicle:
            for trackPair in self.chassis.trackPairs[1:]:
                hitTesters.append(trackPair.hitTesterManager)

        return hitTesters

    def prerequisites(self, newPhysic=True, styleName=None):
        prereqs = set()
        for effGroup in self.type.effects.values():
            for _, effects, readyPrereqs in effGroup:
                if not readyPrereqs:
                    prereqs.update(effects.prerequisites())

        if self.chassis.effects is not None and not newPhysic:
            if self.chassis.effects[b'dust'] is not None:
                effGroup, readyPrereqs = self.chassis.effects[b'dust']
                if not readyPrereqs:
                    prereqs.update(self.__getChassisEffectNames(effGroup))
            if self.chassis.effects[b'mud'] is not None:
                effGroup, readyPrereqs = self.chassis.effects[b'mud']
                if not readyPrereqs:
                    prereqs.update(self.__getChassisEffectNames(effGroup))
        for turretDescr, gunDescr in self.turrets:
            detachmentEff = turretDescr.turretDetachmentEffects
            detachmentEff = itertools.chain((
             detachmentEff[b'flight'], detachmentEff[b'flamingOnGround']), viewvalues(detachmentEff[b'collision']))
            for _, effects, readyPrereqs in detachmentEff:
                if not readyPrereqs:
                    prereqs.update(effects.prerequisites())

            if gunDescr.effects is not None:
                if isinstance(gunDescr.effects, list):
                    for effect in gunDescr.effects:
                        _, effects, readyPrereqs = effect
                        if not readyPrereqs:
                            prereqs.update(effects.prerequisites())

                else:
                    _, effects, readyPrereqs = gunDescr.effects
                    if not readyPrereqs:
                        prereqs.update(effects.prerequisites())
            if gunDescr.prefabEffects is not None:
                prereqs.add(gunDescr.prefabEffects.explosion.prefab)
                if gunDescr.prefabEffects.groundwave.prefab:
                    prereqs.add(gunDescr.prefabEffects.groundwave.prefab)
            for shotDescr in gunDescr.shots:
                for effectsIndex in shotDescr.shell.prereqEffectIndexes:
                    effectsDescr = g_cache.shotEffects[effectsIndex]
                    if not effectsDescr[b'prereqs']:
                        projectileModel, projectileOwnShotModel, effects = effectsDescr[b'projectile']
                        prereqs.add(projectileModel)
                        prereqs.add(projectileOwnShotModel)
                        prereqs.update(effects.prerequisites())
                        for materialName in EFFECT_MATERIALS:
                            prereqs.update(effectsDescr[materialName + b'Hit'][1].prerequisites())

                        prereqs.update(effectsDescr[b'shallowWaterHit'][1].prerequisites())
                        prereqs.update(effectsDescr[b'deepWaterHit'][1].prerequisites())
                        prereqs.update(effectsDescr[b'armorResisted'][1].prerequisites())
                        prereqs.update(effectsDescr[b'armorBasicRicochet'][1].prerequisites())
                        prereqs.update(effectsDescr[b'armorRicochet'][1].prerequisites())
                        prereqs.update(effectsDescr[b'armorHit'][1].prerequisites())
                        prereqs.update(effectsDescr[b'armorCriticalHit'][1].prerequisites())

                iPrefabEff = shotDescr.shell.prefabEffectsIndex
                if iPrefabEff == component_constants.INVALID_EFFECT_INDEX:
                    continue
                for effDesc in viewvalues(g_cache.prefabEffects.shot.effects[iPrefabEff].groups):
                    prereqs.add(effDesc.prefab)
                    if effDesc.decal != component_constants.INVALID_EFFECT_INDEX:
                        prereqs.add(g_cache.prefabEffects.decals.effects[effDesc.decal].prefab)

        for _, prefab in self.getSlotPrefabs(styleName=styleName):
            prereqs.add(prefab)

        if self.type._prereqs is None and not newPhysic:
            prereqs.update(self.hull[b'exhaust'].prerequisites())
            for extra in self.extras:
                prereqs.update(extra.prerequisites())

        def cacheListPrereqs(destructionData):
            if destructionData is not None:
                for _, effects, _1 in destructionData:
                    prereqs.update(effects.prerequisites())

            return

        tracks = self.chassis.tracks
        if tracks is not None:
            for trackVisual in viewvalues(tracks.trackPairs):
                if trackVisual.tracksDebris is None:
                    continue
                debris = trackVisual.tracksDebris.left
                if debris:
                    cacheListPrereqs(debris.destructionEffectData)
                debris = trackVisual.tracksDebris.right
                if debris:
                    cacheListPrereqs(debris.destructionEffectData)

        for elem in copy.copy(prereqs):
            if elem in g_cache.requestOncePrereqs:
                prereqs.remove(elem)

        return list(prereqs)

    def keepPrereqs(self, prereqs):
        if not prereqs:
            return
        else:
            for effGroup in self.type.effects.values():
                for _, effects, readyPrereqs in effGroup:
                    if not readyPrereqs:
                        readyPrereqs.update(_extractNeededPrereqs(prereqs, effects.prerequisites()))

            for turretDescr, gunDescr in self.turrets:
                detachmentEff = turretDescr.turretDetachmentEffects
                detachmentEff = itertools.chain((
                 detachmentEff[b'flight'], detachmentEff[b'flamingOnGround']), viewvalues(detachmentEff[b'collision']))
                for _, effects, readyPrereqs in detachmentEff:
                    if not readyPrereqs:
                        readyPrereqs.update(_extractNeededPrereqs(prereqs, effects.prerequisites()))

                if isinstance(gunDescr.effects, list):
                    for gunEffect in gunDescr.effects:
                        _, effects, readyPrereqs = gunEffect
                        if not readyPrereqs:
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effects.prerequisites()))

                elif gunDescr.effects is not None:
                    _, effects, readyPrereqs = gunDescr.effects
                    if not readyPrereqs:
                        readyPrereqs.update(_extractNeededPrereqs(prereqs, effects.prerequisites()))
                for shotDescr in gunDescr.shots:
                    for effectsIndex in shotDescr.shell.prereqEffectIndexes:
                        effectsDescr = g_cache.shotEffects[effectsIndex]
                        readyPrereqs = effectsDescr[b'prereqs']
                        if not readyPrereqs:
                            projectileModel, projectileOwnShotModel, effects = effectsDescr[b'projectile']
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, (projectileModel, projectileOwnShotModel)))
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effects.prerequisites()))
                            for materialName in EFFECT_MATERIALS:
                                readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[materialName + b'Hit'][1].prerequisites()))

                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[b'shallowWaterHit'][1].prerequisites()))
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[b'deepWaterHit'][1].prerequisites()))
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[b'armorResisted'][1].prerequisites()))
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[b'armorBasicRicochet'][1].prerequisites()))
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[b'armorRicochet'][1].prerequisites()))
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[b'armorHit'][1].prerequisites()))
                            readyPrereqs.update(_extractNeededPrereqs(prereqs, effectsDescr[b'armorCriticalHit'][1].prerequisites()))

            if self.type._prereqs is None:
                resourceNames = []
                for extra in self.extras:
                    resourceNames += extra.prerequisites()

                self.type._prereqs = _extractNeededPrereqs(prereqs, resourceNames)
            return

    def computeBaseInvisibility(self, crewFactor, camouflageId):
        if not camouflageId:
            camouflageBonus = 0.0
        else:
            camouflageBonus = self.type.invisibilityDeltas[b'camouflageBonus'] * g_cache.customization20().camouflages[camouflageId].invisibilityFactor
        vehicleFactor = self.miscAttrs[b'invisibilityFactor']
        invMoving, invStill = self.type.invisibility
        return (
         invMoving * crewFactor * vehicleFactor + camouflageBonus,
         invStill * crewFactor * vehicleFactor + camouflageBonus)

    def __checkCompatibilityWithOptDevices(self, optDevicesLayouts):
        if optDevicesLayouts:
            for optDevSequence in optDevicesLayouts:
                if areOptDevicesLayoutsEqual(self.optionalDevices, optDevSequence):
                    continue
                installPossible, reason = self.mayInstallOptDevsSequence(optDevSequence)
                if not installPossible:
                    return (False, reason)
                optDevs = [getItemByCompactDescr(cd) for cd in optDevSequence if cd != 0]
                for device in optDevs:
                    if device is not None and not device.checkCompatibilityWithVehicle(self):
                        return (False, b'not for current vehicle')

        for device in self.optionalDevices:
            if device is not None and not device.checkCompatibilityWithVehicle(self):
                return (False, b'not for current vehicle')

        return (
         True, None)

    def __getChassisEffectNames(self, effectGroup):
        ret = []
        for v in effectGroup.values():
            if isinstance(v, list):
                for s in v:
                    ret.append(s)

            else:
                ret.append(v)

        return ret

    def __installGun(self, gunID, turretPositionIdx):
        turretDescr, prevGunDescr = self.turrets[turretPositionIdx]
        newGunDescr = _findDescrByID(turretDescr.guns, gunID)
        hullDescr = self.hull
        if newGunDescr is None and turretPositionIdx in self.hull.fakeTurrets[b'lobby']:
            newGunDescr, turretDescr, hullDescr = self.__selectTurretForGun(gunID, turretPositionIdx)
        if newGunDescr is None:
            raise SoftException
        self.turrets[turretPositionIdx] = (turretDescr, newGunDescr)
        self.hull = hullDescr
        if self.__activeTurretPos == turretPositionIdx:
            self.activeTurretPosition = turretPositionIdx
        self.__updateAttributes()
        return (
         prevGunDescr.compactDescr,)

    def __selectBestHull(self, turrets, chassis):
        turretIDs = [descr[0].id[1] for descr in turrets]
        chassisID = chassis.id[1]
        return selectBestHull(self.type.hulls, turretIDs, chassisID)

    def __selectTurretForGun(self, gunID, turretPositionIdx):
        hullDescr = self.hull
        for turretDescr in self.type.turrets[turretPositionIdx]:
            gunDescr = _findDescrByID(turretDescr.guns, gunID)
            if gunDescr is not None:
                if len(self.type.hulls) > 1:
                    turrets = list(self.turrets)
                    turrets[turretPositionIdx] = (turretDescr, gunDescr)
                    hullDescr = self.__selectBestHull(turrets, self.chassis)
                return (gunDescr, turretDescr, hullDescr)

        return (None, None, None)

    def __setHullAndCall(self, hullDescr, callable):
        self.hull = hullDescr
        callable()
        return

    def __initFromCompactDescr(self, compactDescr, vehMode, vehType=None):
        unpack = struct.unpack
        try:
            type, components, optionalDeviceSlots, optionalDevices, enhancements, emblemPositions, emblems, inscriptions, camouflages = _splitVehicleCompactDescr(compactDescr, vehMode, vehType)
            if not IS_UE_EDITOR:
                type = self.battleModifiers.getVehicleModification(type)
            custNationID = type.customizationNationID
            customization = g_cache.customization(custNationID)
            self.type = type
            self.name = type.name
            self.level = type.level
            if IS_CLIENT or IS_UE_EDITOR or IS_CELLAPP or IS_BOT:
                self.extras = type.extras
                self.extrasDict = type.extrasDict
            chassisID, engineID, fuelTankID, radioID = unpack(b'<4H', components[:8])
            self.chassis = _descrByID(type.chassis, chassisID)
            self.engine = _descrByID(type.engines, engineID)
            self.fuelTank = _descrByID(type.fuelTanks, fuelTankID)
            self.radio = _descrByID(type.radios, radioID)
            turrets = []
            for idx in xrange(len(type.turrets)):
                turretID, gunID = unpack(b'<2H', components[8 + idx * 4:12 + idx * 4])
                turret = _descrByID(type.turrets[idx], turretID)
                turrets.append((turret, _descrByID(turret.guns, gunID)))

            self.turrets = turrets
            self.activeTurretPosition = 0
            if len(type.hulls) == 1:
                self.hull = type.hulls[0]
            else:
                self.hull = self.__selectBestHull(self.turrets, self.chassis)
            self.supplySlots = self.type.supplySlots
            optDevSlots = self.supplySlots.getAmountForType(ITEM_TYPES.optionalDevice)
            self.optionalDevices = [None] * optDevSlots
            self._optDevSlotsMap = {}
            optDevsCache = g_cache.optionalDevices()
            idx = optDevSlots - 1
            while optionalDeviceSlots:
                if optionalDeviceSlots & 1:
                    self.optionalDevices[idx] = optDevsCache[unpack(b'<H', optionalDevices[:2])[0]]
                    optionalDevices = optionalDevices[2:]
                optionalDeviceSlots >>= 1
                idx -= 1

            self._rebuildOptDevSlotsMap()
            if enhancements:
                enhancements = enhancements[1:]
                for idx in xrange(0, len(enhancements), 6):
                    attrId, value, opIdx = unpack(b'<BfB', enhancements[idx:idx + 6])
                    self.enhancements.append(EnhancementItem(VEHICLE_MISC_ATTRIBUTE_FACTOR_NAMES[attrId], value / 1000, EnhancementItem.getOpName(opIdx)))

            if IS_CLIENT:
                self.playerEmblems = _EMPTY_EMBLEMS
                self.playerInscriptions = _EMPTY_INSCRIPTIONS
                self.camouflages = _EMPTY_CAMOUFLAGES
            else:
                if not emblemPositions & 15:
                    self.playerEmblems = type._defEmblems
                else:
                    emblemCache = g_cache.playerEmblems()[1]
                    slots = [None, None, None, None]
                    for idx in _RANGE_4:
                        if emblemPositions & 1 << idx:
                            slots[idx] = _unpackIDAndDuration(emblems[:6])
                            emblems = emblems[6:]
                            emblemCache[slots[idx][0]]
                        else:
                            slots[idx] = type._defEmblem

                    self.playerEmblems = tuple(slots)
                if not emblemPositions & 240:
                    self.playerInscriptions = _EMPTY_INSCRIPTIONS
                else:
                    slots = [
                     None, None, None, None]
                    for idx in _RANGE_4:
                        if emblemPositions & 1 << idx + 4:
                            slots[idx] = _unpackIDAndDuration(inscriptions[:6]) + (
                             unpackByte(inscriptions[6]),)
                            inscriptions = inscriptions[7:]
                            customization[b'inscriptions'][slots[idx][0]]
                            customization[b'inscriptionColors'][slots[idx][3]]
                        else:
                            slots[idx] = _EMPTY_INSCRIPTION

                    self.playerInscriptions = tuple(slots)
                if not camouflages:
                    self.camouflages = _EMPTY_CAMOUFLAGES
                else:
                    slots = list(_EMPTY_CAMOUFLAGES)
                    while camouflages:
                        item = _unpackIDAndDuration(camouflages[:6])
                        camouflages = camouflages[6:]
                        idx = customization[b'camouflages'][item[0]][b'kind']
                        if slots[idx][0] is not None:
                            LOG_WARNING(b'Second camouflage of same kind', custNationID, item[0], slots[idx][0])
                        slots[idx] = item

                    self.camouflages = tuple(slots)
        except Exception:
            LOG_ERROR(b'(compact descriptor to XML mismatch?)', compactDescr)
            raise

        return

    def __recoveryOriginalComponents(self):
        type = self.type = g_cache.vehicle(self.type.id[0], self.type.id[1], self.type.mode)
        self.chassis = _descrByID(type.chassis, self.chassis.id[1])
        self.engine = _descrByID(type.engines, self.engine.id[1])
        self.fuelTank = _descrByID(type.fuelTanks, self.fuelTank.id[1])
        self.radio = _descrByID(type.radios, self.radio.id[1])
        for idx, (turret, gun) in enumerate(self.turrets):
            for turrets in type.turrets:
                origTurret = _findDescrByID(turrets, turret.id[1])
                if origTurret:
                    self.turrets[idx] = (
                     origTurret, _descrByID(origTurret.guns, gun.id[1]))
                    break

        self.activeTurretPosition = 0
        self.hull = self.__selectBestHull(self.turrets, self.chassis)
        self.descrModifyAttrsApplied = False
        return

    def __computeWeight(self):
        weight = self.hull.weight + self.chassis.weight + self.engine.weight + self.fuelTank.weight + self.radio.weight
        for turretDescr, gunDescr in self.turrets:
            weight += turretDescr.weight + gunDescr.weight

        vehWeightFraction = 0.0
        vehWeightAddition = 0.0
        for device in self.optionalDevices:
            if device is not None:
                fraction, addition = device.weightOnVehicle(self)
                vehWeightFraction += fraction
                vehWeightAddition += addition

        return weight * (1.0 + vehWeightFraction) + vehWeightAddition

    def applyOptionalDevicesMiscAttrs(self):
        for optDev in self.optionalDevices:
            if optDev is not None:
                optDev.updateVehicleDescrAttrs(self)

        return

    def applyDescrModifyAttrs(self):
        if self.descrModifyAttrsApplied:
            self.__recoveryOriginalComponents()
        pItems = list(self.getPostProgressionModifications())
        if not pItems:
            return
        modeFilter = self.getModificationsFilter()
        self.descrModifyAttrsApplied = applyDescrModifyAttrs(self, pItems, modeFilter)
        return

    def applyOptDevFactorsForAspect(self, factors, aspect):
        for optDev in self.optionalDevices:
            if optDev is not None:
                optDev.updateVehicleAttrFactorsForAspect(self, factors, aspect)

        return

    def applyModificationsAttrs(self):
        pItems = self.getPostProgressionModifications()
        modeFilter = self.getModificationsFilter()
        onCollectAttributes(self.miscAttrs, pItems, STATIC_ATTR_PREFIX, True, filter=modeFilter)
        return

    def getModificationsFilter(self):
        modeFilter = None
        if self.type.mode == VEHICLE_MODE.DEFAULT:
            modeFilter = (
             MODIFIER_FILTER_TYPE.COMMON, MODIFIER_FILTER_TYPE.DEFAULT)
        elif self.type.mode == VEHICLE_MODE.SIEGE:
            modeFilter = (
             MODIFIER_FILTER_TYPE.COMMON, MODIFIER_FILTER_TYPE.SIEGE)
        return modeFilter

    def getPostProgressionModifications(self):
        vppCache = g_cache.postProgression()
        modifications = vppCache.modifications
        return iter(modifications[modificationID].modifiers for modificationID in self._modifications)

    def getPostProgressionDynAttrs(self):
        postProgressionModifications = self.getPostProgressionModifications()
        dynAttrs = []
        for modifiers in postProgressionModifications:
            for modifier in modifiers:
                if modifier[1] != DYNAMIC_ATTR_PREFIX:
                    continue
                dynAttrs.append(modifier)

        return dynAttrs

    @property
    def shootExtraName(self):
        if self.isDualgunVehicle:
            return b'dualShoot'
        if self.isTwinGunVehicle:
            return b'undefined'
        return b'shoot'

    @property
    def clipReloadExtraName(self):
        if self.hasTag(b'controllableReload'):
            return b'controllableClipReload'
        return b'clipReload'

    @property
    def gunReloadExtraName(self):
        if self.hasTag(b'controllableReload'):
            return b'gunReloadBetweenShots'
        return b'gunReload'

    def hasTag(self, tag):
        return tag in self.type.tags or any(tag in gunInstallation.gun.tags for gunInstallation in self.gunInstallations)

    def __updateAttributes(self, onAnyApp=False, updateDescrAttrs=True):
        self.miscAttrs = None
        self.physics = None
        self.mechanicsParams = {}
        computeArenaGameplayParams = IS_CELLAPP or IS_CLIENT or IS_UE_EDITOR or IS_WEB or IS_BOT or onAnyApp
        if computeArenaGameplayParams and (updateDescrAttrs or not self.descrModifyAttrsApplied):
            self.applyDescrModifyAttrs()
        type = self.type
        chassis = self.chassis
        chassisShotDispersionFactors = chassis.shotDispersionFactors
        gunShotDispersionFactors = self.gun.shotDispersionFactors
        weight = self.__computeWeight()
        self.miscAttrs = miscAttrs = {b'repairSpeedFactor': 1.0, 
           b'additiveShotDispersionFactor': 1.0, 
           b'antifragmentationLiningFactor': 1.0, 
           b'circularVisionRadiusFactor': 1.0, 
           b'circularVisionRadiusBaseFactor': 1.0, 
           b'gunReloadTimeFactor': 1.0, 
           b'gunAimingTimeFactor': 1.0, 
           b'vehicleByChassisDamageFactor': 1.0, 
           b'crewLevelIncrease': 0.0, 
           b'crewChanceToHitFactor': 1.0, 
           b'stunResistanceEffect': 0.0, 
           b'stunResistanceDuration': 0.0, 
           b'repeatedStunDurationFactor': 1.0, 
           b'radioDistanceFactor': 0.0, 
           b'healthFactor': 1.0, 
           b'damageFactor': 1.0, 
           b'enginePowerFactor': 1.0, 
           b'armorSpallsDamageDevicesFactor': 1.0, 
           b'increaseEnemySpottingTime': 0.0, 
           b'decreaseOwnSpottingTime': 0.0, 
           b'demaskFoliageFactor': 1.0, 
           b'chassisRepairSpeedFactor': 1.0, 
           b'turretRotationSpeed': 1.0, 
           b'invisibilityAdditiveTerm': 0.0, 
           b'invisibilityMultFactor': 1.0, 
           b'invisibilityBaseAdditive': 0.0, 
           b'forwardMaxSpeedKMHTerm': 0.0, 
           b'backwardMaxSpeedKMHTerm': 0.0, 
           b'onStillRotationSpeedFactor': 1.0, 
           b'onMoveRotationSpeedFactor': 1.0, 
           b'fireStartingChanceFactor': 1.0, 
           b'multShotDispersionFactor': 1.0, 
           b'isSetChassisMaxHealthAfterHysteresis': False, 
           b'ammoBayHealthFactor': 1.0, 
           b'engineHealthFactor': 1.0, 
           b'chassisHealthFactor': 1.0, 
           b'fuelTankHealthFactor': 1.0, 
           b'turretRotatorHealthFactor': 1.0, 
           b'radioHealthFactor': 1.0, 
           b'surveyingDeviceHealthFactor': 1.0, 
           b'gunHealthFactor': 1.0, 
           b'demaskMovingFactor': 1.0, 
           b'centerRotationFwdSpeedFactor': 1.0, 
           b'deathZones/sensitivityFactor': 1.0, 
           b'rammingFactor': 1.0, 
           b'rollingFrictionFactor': 1.0, 
           b'chassis/shotDispersionFactors/movement': (chassisShotDispersionFactors[0]), 
           b'chassis/shotDispersionFactors/rotation': (chassisShotDispersionFactors[1]), 
           b'invisibilityFactorAtShot': (self.gun.invisibilityFactorAtShot), 
           b'gun/shotDispersionFactors/afterShot': (gunShotDispersionFactors[b'afterShot']), 
           b'gun/shotDispersionFactors/turretRotation': (gunShotDispersionFactors[b'turretRotation']), 
           b'gun/shotDispersionFactors/whileGunDamaged': (gunShotDispersionFactors[b'whileGunDamaged']), 
           b'ammoBayReduceFineFactor': 1.0, 
           b'engineReduceFineFactor': 1.0, 
           b'hullMaxHealth': 0, 
           b'turretMaxHealth': 0, 
           b'discreteDamageFactor': 1.0, 
           b'damageDistributionLowerBound': 0.0, 
           b'piercingDistributionLowerBound': 0.0, 
           b'inConeVision/visionFactor': 1.0, 
           b'inConeVision/demaskFoliageFactor': 1.0, 
           b'inConeVision/demaskMovingFactor': 1.0, 
           b'inConeVision/circularVisionRadiusFactor': 1.0}
        for name, params in viewitems(type.mechanicsParams):
            self.mechanicsParams[name] = params.createMechanicsParamsOrigin()

        for gunInstallation in self.gunInstallations:
            for name, params in viewitems(gunInstallation.gun.mechanicsParams):
                if name in self.mechanicsParams:
                    LOG_ERROR(b'Gun mechanics will be overridden', self.type.name, name)
                self.mechanicsParams[name] = gunParams = params.createMechanicsParamsOrigin()
                gunParams.setGunInstallationSlot(gunInstallation)

        for name, params in listitems(self.mechanicsParams):
            if params.isActiveMechanics(self):
                self.miscAttrs.update(params.getMechanicsMiscAttributes())
            else:
                self.mechanicsParams.pop(name, None)

        if computeArenaGameplayParams:
            trackCenterOffset = chassis.topRightCarryingPoint[0]
            self.physics = {b'weight': weight, 
               b'enginePower': (self.engine.power), 
               b'specificFriction': (chassis.specificFriction), 
               b'minPlaneNormalY': (chassis.minPlaneNormalY), 
               b'trackCenterOffset': trackCenterOffset, 
               b'rotationIsAroundCenter': (chassis.rotationIsAroundCenter), 
               b'speedLimits': (self.type.speedLimits), 
               b'navmeshGirth': (chassis.navmeshGirth), 
               b'carryingTriangles': (chassis.carryingTriangles), 
               b'brakeForce': (chassis.brakeForce), 
               b'terrainResistance': (chassis.terrainResistance), 
               b'rollingFrictionFactors': [
                                         1.0, 1.0, 1.0]}
            self.applyModificationsAttrs()
            self.applyOptionalDevicesMiscAttrs()
            physics = self.physics
            rff = physics[b'rollingFrictionFactors']
            rollingFrictionFactor = miscAttrs[b'rollingFrictionFactor']
            physics[b'rollingFrictionFactors'] = list(rffi * rollingFrictionFactor for rffi in rff)
            defWeight = type.hulls[0].weight + chassis.weight + type.engines[0].weight + type.fuelTanks[0].weight + type.radios[0].weight
            for turretList in type.turrets:
                defWeight += turretList[0].weight + turretList[0].guns[0].weight

            defResistance = chassis.terrainResistance[0]
            rotationEnergy = type.engines[0].power * (weight / defWeight) / (chassis.rotationSpeed * defResistance)
            rotationSpeedLimit = physics[b'enginePower'] / (rotationEnergy * physics[b'terrainResistance'][0])
            if not chassis.rotationIsAroundCenter:
                rotationEnergy -= trackCenterOffset * weight * chassis.specificFriction / defResistance
                if rotationEnergy <= 0.0:
                    raise SoftException(b'wrong parameters of rotation of ' + type.name)
            if chassis.rotationSpeedLimit is not None:
                rotationSpeedLimit = min(rotationSpeedLimit, chassis.rotationSpeedLimit)
            physics[b'rotationSpeedLimit'] = rotationSpeedLimit
            physics[b'rotationEnergy'] = rotationEnergy
            physics[b'massRotationFactor'] = defWeight / weight
            if IS_CELLAPP or IS_CLIENT or IS_UE_EDITOR or IS_BOT:
                invisibilityFactor = 1.0
                for turretDescr, _ in self.turrets:
                    invisibilityFactor *= turretDescr.invisibilityFactor

                miscAttrs[b'invisibilityFactor'] = invisibilityFactor
        if IS_CELLAPP or IS_UE_EDITOR:
            hullPos = self.chassis.hullPosition
            hullBboxMin, hullBboxMax, _ = self.hull.hitTester.bbox
            turretPosOnHull = self.hull.turretPositions[0]
            turretLocalTopY = max(hullBboxMax.y, turretPosOnHull.y + self.turret.hitTester.bbox[1].y)
            gunPosition = self.turret.gunPosition
            gunPosOnHull = turretPosOnHull + gunPosition
            hullLocalCenterY = (hullBboxMin.y + hullBboxMax.y) / 2.0
            hullLocalPt1 = Vector3(0.0, hullLocalCenterY, hullBboxMax.z)
            hullLocalPt2 = Vector3(0.0, hullLocalCenterY, hullBboxMin.z)
            hullLocalCenterZ = (hullBboxMin.z + hullBboxMax.z) / 2.0
            hullLocalPt3 = Vector3(hullBboxMax.x, gunPosOnHull.y, hullLocalCenterZ)
            hullLocalPt4 = Vector3(hullBboxMin.x, gunPosOnHull.y, hullLocalCenterZ)
            self.visibilityCheckPoints = (
             Vector3(0.0, hullPos.y + turretLocalTopY, 0.0),
             hullPos + gunPosOnHull,
             hullPos + hullLocalPt1,
             hullPos + hullLocalPt2,
             hullPos + hullLocalPt3,
             hullPos + hullLocalPt4)
            self.observerPosOnChassis = Vector3(0, hullPos.y + turretLocalTopY, 0)
            self.observerPosOnTurret = gunPosition
        for attribute in self.enhancements:
            miscAttrs[attribute.name] = attribute.applyFactor(miscAttrs[attribute.name])

        hullMaxHealth = round_py2_style_int(miscAttrs[b'hullMaxHealth'])
        if hullMaxHealth <= 0:
            hullMaxHealth = self.hull.maxHealth
        turretMaxHealth = round_py2_style_int(miscAttrs[b'turretMaxHealth'])
        if turretMaxHealth <= 0:
            turretMaxHealth = sum((turretDescr.maxHealth for turretDescr, _ in self.turrets), 0)
        maxHealth = hullMaxHealth + turretMaxHealth
        self._defaultMaxHealth = maxHealth
        self._maxHealth = self.battleModifiers(BattleParams.VEHICLE_HEALTH, maxHealth)
        if miscAttrs[b'healthFactor'] != 1.0:
            self._maxHealth = int(ceilTo(self._maxHealth * miscAttrs[b'healthFactor'], VEHICLE_HEALTH_DECIMALS))
        postProgressionDynAttrs = self.getPostProgressionDynAttrs()
        for params in viewvalues(self.mechanicsParams):
            params.applyMiscAttrToMechanics(miscAttrs)
            params.applyDynModifiersToMechanics(postProgressionDynAttrs)

        if self.isUnlimitedClipVehicle and self.gun.clip[0] != self.gun.maxAmmo:
            raise SoftException(b'Wrong settings of clip size and maxAmmo for <unlimitedClip> vehicle = ' + type.name)
        return

    def __getExtDataValue(self, extData, key):
        if isinstance(extData, dict):
            return extData.get(key)
        else:
            if hasattr(extData, key):
                return getattr(extData, key)
            else:
                return

            return


class VehicleComponents(object):

    def __init__(self, compactDescr):
        self.type, components = _splitVehicleCompactDescr(compactDescr, onlyComponents=True)
        self.__componentIDs = struct.unpack(b'<6H', components[:12])
        return

    @cached_property
    def chassis(self):
        return _descrByID(self.type.chassis, self.__componentIDs[0])

    @cached_property
    def engine(self):
        return _descrByID(self.type.engines, self.__componentIDs[1])

    @cached_property
    def fuelTank(self):
        return _descrByID(self.type.fuelTanks, self.__componentIDs[2])

    @cached_property
    def turret(self):
        return _descrByID(self.type.turrets[0], self.__componentIDs[4])

    @cached_property
    def gun(self):
        return _descrByID(self.turret.guns, self.__componentIDs[5])

    @cached_property
    def hull(self):
        hulls = self.type.hulls
        if len(hulls) == 1:
            return hulls[0]
        return selectBestHull(self.type.hulls, [self.__componentIDs[4]], self.__componentIDs[0])


class CompositeVehicleDescriptor(object):
    defaultVehicleDescr = property((lambda self: self.__vehicleDescr))
    siegeVehicleDescr = property((lambda self: self.__siegeDescr))
    vehicleMode = property((lambda self: self.__vehicleMode))
    currentDescr = property((lambda self: self.__siegeDescr if self.__vehicleMode == VEHICLE_MODE.SIEGE else self.__vehicleDescr))

    def __init__(self, vehicleDescr, siegeDescr):
        self.__dict__[b'_CompositeVehicleDescriptor__vehicleDescr'] = vehicleDescr
        self.__dict__[b'_CompositeVehicleDescriptor__siegeDescr'] = siegeDescr
        self.__dict__[b'_CompositeVehicleDescriptor__vehicleMode'] = VEHICLE_MODE.DEFAULT
        if IS_CLIENT:
            self.__siegeDescr.chassis.hitTesterManager = self.__vehicleDescr.chassis.hitTesterManager
            self.__siegeDescr.hull.hitTesterManager = self.__vehicleDescr.hull.hitTesterManager
            self.__siegeDescr.turret.hitTesterManager = self.__vehicleDescr.turret.hitTesterManager
            self.__siegeDescr.gun.hitTesterManager = self.__vehicleDescr.gun.hitTesterManager
            self.__siegeDescr.type.extras = self.__vehicleDescr.type.extras
            self.__siegeDescr.type.extrasDict = self.__vehicleDescr.type.extrasDict
        return

    def __getattr__(self, item):
        if self.__vehicleMode == VEHICLE_MODE.SIEGE:
            return getattr(self.__siegeDescr, item)
        return getattr(self.__vehicleDescr, item)

    def __setattr__(self, key, value):
        setattr(self.__siegeDescr, key, value)
        setattr(self.__vehicleDescr, key, value)
        return

    def onSiegeStateChanged(self, siegeState):
        self.__dict__[b'_CompositeVehicleDescriptor__vehicleMode'] = VEHICLE_SIEGE_STATE.getMode(siegeState)
        return

    def installComponent(self, compactDescr, positionIndex=0):
        self.__siegeDescr.installComponent(compactDescr, positionIndex)
        return self.__vehicleDescr.installComponent(compactDescr, positionIndex)

    def installEnhancements(self, enhancements, rebuildAttrs=True):
        self.__siegeDescr.installEnhancements(enhancements, rebuildAttrs)
        return self.__vehicleDescr.installEnhancements(enhancements, rebuildAttrs)

    def installModifications(self, modificationIDs, rebuildAttrs=True):
        self.__siegeDescr.installModifications(modificationIDs, rebuildAttrs)
        return self.__vehicleDescr.installModifications(modificationIDs, rebuildAttrs)

    def installOptionalDevice(self, compactDescr, slotIdx, rebuildAttrs=True):
        self.__siegeDescr.installOptionalDevice(compactDescr, slotIdx, rebuildAttrs)
        return self.__vehicleDescr.installOptionalDevice(compactDescr, slotIdx, rebuildAttrs)

    def installOptDevsSequence(self, optDevSequence):
        self.__siegeDescr.installOptDevsSequence(optDevSequence)
        return self.__vehicleDescr.installOptDevsSequence(optDevSequence)

    def installTurret(self, turretCompactDescr, gunCompactDescr, positionIndex=0):
        self.__siegeDescr.installTurret(turretCompactDescr, gunCompactDescr, positionIndex)
        return self.__vehicleDescr.installTurret(turretCompactDescr, gunCompactDescr, positionIndex)

    def removeOptionalDevice(self, slotIdx, rebuildAttrs=True):
        self.__siegeDescr.removeOptionalDevice(slotIdx, rebuildAttrs)
        return self.__vehicleDescr.removeOptionalDevice(slotIdx, rebuildAttrs)

    def rebuildAttrs(self):
        self.__siegeDescr.rebuildAttrs()
        return self.__vehicleDescr.rebuildAttrs()

    def __installGun(self, gunID, turretPositionIdx):
        self.__siegeDescr.__installGun(gunID, turretPositionIdx)
        return self.__vehicleDescr.__installGun(gunID, turretPositionIdx)


def VehicleDescr(compactDescr=None, typeID=None, typeName=None, xmlPath=None, extData=None, forceUpdateAttrs=False):
    defaultDescriptor = VehicleDescriptor(compactDescr, typeID, typeName, xmlPath=xmlPath, extData=extData, forceUpdateAttrs=forceUpdateAttrs)
    if not defaultDescriptor.hasSiegeMode:
        return defaultDescriptor
    siegeDescriptor = VehicleDescriptor(compactDescr, typeID, typeName, VEHICLE_MODE.SIEGE, xmlPath=xmlPath, extData=extData, forceUpdateAttrs=forceUpdateAttrs)
    return CompositeVehicleDescriptor(defaultDescriptor, siegeDescriptor)


def isVehicleDescr(descr):
    return isinstance(descr, (VehicleDescriptor, CompositeVehicleDescriptor))


VehicleDescrType = Union[VehicleDescriptor, CompositeVehicleDescriptor]

class NoneVehicleSelector(list):

    def matches(self, vehTypeOrDescr=None, vehName=None):
        return False

    def match(self, tags=(), excludedTags=()):
        return self


class VehicleSelector(NoneVehicleSelector):
    ANY = (b'', b'*')
    ctags = property((lambda self: self.__tags & VEHICLE_CLASS_TAGS))
    vtags = property((lambda self: self.__tags - VEHICLE_CLASS_TAGS))
    etags = property((lambda self: self.__etags - VEHICLE_CLASS_TAGS))

    def __init__(self, ns=(), levels=(), vehClasses=(), vehTags=(), excludedVehTags=()):
        self.__nations = {str(n) for n in ns if str(n) in nations.NAMES} if ns else nations.NAMES
        self.__levels = {int(l) for l in levels} if levels else set(range(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1))
        self.__tags = {str(vc) for vc in vehClasses if vc in VEHICLE_CLASS_TAGS} if vehClasses else VEHICLE_CLASS_TAGS
        vtags = set(items.getTypeInfoByName(b'vehicle')[b'tags']) - VEHICLE_CLASS_TAGS
        self.__tags |= {str(vt) for vt in vehTags if vt in vtags}
        self.__etags = {str(vt) for vt in excludedVehTags if vt in vtags}
        return

    def match(self, tags=(), excludedTags=()):
        tags = frozenset(tags)
        excludedTags = frozenset(excludedTags)
        if not self:
            nset, _, vtags, vetags = (
             self.__nations, self.__levels, self.__tags, self.__etags)
            tags |= vtags
            excludedTags |= vetags
            self.extend(vdict.compactDescr for nn in nset for vdict in viewvalues(g_list.getList(nations.INDICES[nn])) if self.matches(vehTypeOrDescr=vdict.compactDescr))
        return self

    def matches(self, vehTypeOrDescr=None, vehName=None):
        if not bool(vehTypeOrDescr) ^ bool(vehName):
            raise SoftException(b'Value Error')
        if vehTypeOrDescr is not None:
            _, nid, vnid = parseIntCompactDescr(vehTypeOrDescr)
        elif vehName is not None:
            nid, vnid = g_list.getIDsByName(vehName)
        vdata = g_list.getList(nid)[vnid]
        vct, vt, vet = self.ctags, self.vtags, self.etags
        return (not self.__nations or nations.MAP[nid] in self.__nations) and (not self.__levels or vdata.level in self.__levels) and not (vct and vdata.tags.isdisjoint(vct)) and not (vt and not vdata.tags >= vt) and not (vet and vdata.tags >= vet)

    def __repr__(self):
        if self:
            return super(VehicleSelector, self).__repr__()
        return (b':').join(((b'|').join(self.__nations),
         (b'|').join(str(l) for l in self.__levels),
         (b'|').join(self.ctags),
         (b'&').join(self.vtags | {(b'~{}').format(et) for et in self.etags})))

    @staticmethod
    def fromString(vstr):
        try:
            nset, levels, ctags, tags = itertools.islice(itertools.chain(vstr.split(b':', 3), iter(str, -1)), 4)
            nset = VehicleSelector.predicateAsSet(nset, nations.NAMES, str)
            levels = VehicleSelector.predicateAsSet(levels, lrange(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1), int)
            vehClasses = VehicleSelector.predicateAsSet(ctags, VEHICLE_CLASS_TAGS, str)
            tags = tags.split(b'&')
            vehTags = {t for t in tags if not t in VEHICLE_CLASS_TAGS or t.startswith(b'~')}
            excludedVehTags = {t[1:] for t in tags if t and t[1:] not in VEHICLE_CLASS_TAGS and t.startswith(b'~')}
        except ValueError:
            LOG_ERROR((b'Unable to match any vehicle by {}').format(vstr))
            return NoneVehicleSelector()

        return VehicleSelector(nset, levels, vehClasses, vehTags, excludedVehTags)

    @staticmethod
    def predicateAsSet(predicate, dom, fun=(lambda _: _)):
        result = set()
        dom = frozenset(dom)
        for p in str(predicate).split(b'|'):
            try:
                if p.startswith(b'~'):
                    result |= dom - {fun(p[1:])} if fun(p[1:]) in dom else set()
                elif fun(p) in dom:
                    result.add(fun(p))
            except ValueError:
                pass

        return result or dom


class VehicleType(with_metaclass(ReflectionMetaclass, object)):
    currentReadingVeh = None
    __slots__ = (
     b'name', b'id', b'compactDescr', b'mode', b'tags', b'level', b'hasSiegeMode', b'hasAutoSiegeMode', b'isWheeledVehicle',
     b'isDualgunVehicleType', b'hasCustomDefaultCamouflage', b'customizationNationID', b'baseColorID', b'speedLimits',
     b'repairCost', b'crewXpFactor', b'premiumVehicleXPFactor', b'xpFactor',
     b'creditsFactor', b'freeXpFactor', b'healthBurnPerSec', b'healthBurnPerSecLossFraction',
     b'invisibility', b'invisibilityDeltas', b'crewRoles', b'extras', b'extrasDict', b'extrasProtection',
     b'devices', b'tankmen', b'damageByStaticsChances', b'i18nInfo', b'balanceByClass',
     b'balanceByComponentLevels', b'damageStickersLodDist', b'heavyCollisionEffectVelocities', b'effects', b'prefabs',
     b'camouflage', b'emblemsLodDist', b'emblemsAlpha', b'_prereqs', b'clientAdjustmentFactors',
     b'defaultPlayerEmblemID', b'_defEmblem', b'_defEmblems', b'unlocks', b'chassis', b'engines',
     b'fuelTanks', b'radios', b'turrets', b'hulls', b'installableComponents', b'unlocksDescrs',
     b'autounlockedItems', b'collisionEffectVelocities', b'isRotationStill', b'useHullZSize', b'useHullZOffset',
     b'siegeModeParams', b'hullAimingParams', b'overmatchMechanicsVer', b'xphysics', b'repaintParameters',
     b'rollerExtras', b'hasCharge', b'role', b'actionsGroup', b'actions', b'builtins',
     b'nationChangeGroupId', b'isCollectorVehicle', b'isPremium', b'hasTurboshaftEngine', b'hasHydraulicChassis',
     b'hasSpeedometer', b'supplySlots', b'optDevsOverrides', b'postProgressionTree', b'postProgressionPricesOverrides',
     b'customRoleSlotOptions', b'hasRocketAcceleration', b'rocketAccelerationParams', b'classTag', b'armorMaxHealth',
     b'visualScript', b'mechanicsParams', b'eliteByProgression', b'hasWheeledDash', b'hasStagedJetBoosters',
     b'__weakref__')

    def __init__(self, nationID, basicInfo, xmlPath, vehMode=VEHICLE_MODE.DEFAULT):
        self.name = basicInfo.name
        self.id = (nationID, basicInfo.id)
        self.compactDescr = basicInfo.compactDescr
        self.mode = vehMode
        self.nationChangeGroupId = nation_change.findVehicleNationGroupId(self.name)
        section = ResMgr.openSection(xmlPath)
        if section is None:
            _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
        xmlCtx = (
         None, xmlPath)
        self.tags = basicInfo.tags
        self.level = basicInfo.level
        self.hasSiegeMode = b'siegeMode' in self.tags
        self.hasHydraulicChassis = b'hydraulicChassis' in self.tags
        self.hasAutoSiegeMode = b'autoSiege' in self.tags
        self.isWheeledVehicle = b'wheeledVehicle' in self.tags
        self.isDualgunVehicleType = b'dualgun' in self.tags
        self.hasTurboshaftEngine = b'turboshaftEngine' in self.tags
        self.hasSpeedometer = b'speedometer' in self.tags
        self.hasCharge = b'charger' in self.tags
        self.builtins = {t.split(b'_user')[0] for t in self.tags if t.startswith(b'builtin')}
        self.hasRocketAcceleration = b'rocketAcceleration' in self.tags
        self.hasWheeledDash = b'wheeledDash' in self.tags
        self.hasStagedJetBoosters = b'stagedJetBoosters' in self.tags
        self.isCollectorVehicle = CollectorVehicleConsts.COLLECTOR_VEHICLES_TAG in self.tags
        self.isPremium = b'premium' in self.tags
        self.role = self.__getRoleFromTags() if self.level in ROLE_LEVELS else ROLE_TYPE.NOT_DEFINED
        self.actions = self.__getActionsFromRole(self.role)
        self.classTag = self.__getClassFromTags()
        VehicleType.currentReadingVeh = self
        self.baseColorID = section.readInt(b'baseColorID', 0)
        self.hasCustomDefaultCamouflage = section.readBool(b'customDefaultCamouflage', False)
        customizationNation = section.readString(b'customizationNation')
        if not customizationNation:
            self.customizationNationID = nationID
        else:
            self.customizationNationID = nations.INDICES.get(customizationNation)
            if self.customizationNationID is None:
                _xml.raiseWrongXml(xmlCtx, b'customizationNation', b'unknown nation name:' + customizationNation)
        self.speedLimits = (component_constants.KMH_TO_MS * _xml.readPositiveFloat(xmlCtx, section, b'speedLimits/forward'),
         component_constants.KMH_TO_MS * _xml.readPositiveFloat(xmlCtx, section, b'speedLimits/backward'))
        if IS_UE_EDITOR:
            self.speedLimits = list(self.speedLimits)
        self.repairCost = _xml.readNonNegativeFloat(xmlCtx, section, b'repairCost')
        self.crewXpFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'crewXpFactor')
        self.premiumVehicleXPFactor = component_constants.DEFAULT_PREMIUM_VEHICLE_XP_FACTOR
        if section.has_key(b'premiumVehicleXPFactor'):
            self.premiumVehicleXPFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'premiumVehicleXPFactor')
        self.premiumVehicleXPFactor = max(self.premiumVehicleXPFactor, 0.0)
        supplySlotIDs = _xml.readTupleOfInts(xmlCtx, section, b'supplySlots')
        self.supplySlots = g_cache.supplySlotsStorage().getStorage(supplySlotIDs)
        if section.has_key(b'postProgressionTree'):
            treeName = _xml.readString(xmlCtx, section, b'postProgressionTree')
            treeID = g_cache.postProgression().treeIDs.get(treeName)
            if treeID is None:
                _xml.raiseWrongXml(xmlCtx, b'postProgressionTree', (b'Unknown postProgression tree: {}').format(treeName))
            self.postProgressionTree = treeID
        else:
            self.postProgressionTree = None
        self.eliteByProgression = False
        if self.postProgressionTree and self.postProgressionTree >= VEH_SKILL_TREE_ID_OFFSET:
            self.eliteByProgression = True
        if section.has_key(b'postProgressionPricesOverrides'):
            self.postProgressionPricesOverrides = _readPostProgressionPricesOverrides(xmlCtx, section[b'postProgressionPricesOverrides'])
        else:
            self.postProgressionPricesOverrides = None
        if self.role == ROLE_TYPE.NOT_DEFINED and self.postProgressionTree is not None:
            LOG_ERROR((b'Vehicle {} must have role').format(self.name))
        if section.has_key(b'customRoleSlotOptions'):
            self.customRoleSlotOptions = _xml.readTupleOfInts(xmlCtx, section, b'customRoleSlotOptions')
            intersection = set(supplySlotIDs) & set(self.customRoleSlotOptions)
            if intersection:
                _xml.raiseWrongXml(xmlCtx, b'customRoleSlotOptions', (b'Duplicate custom slots: {}').format(intersection))
        else:
            self.customRoleSlotOptions = ()
        if not IS_CLIENT and not IS_BOT:
            self.xpFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'xpFactor')
            self.creditsFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'creditsFactor')
            self.freeXpFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'freeXpFactor')
            self.healthBurnPerSec = _xml.readNonNegativeFloat(xmlCtx, section, b'healthBurnPerSec')
            self.healthBurnPerSecLossFraction = _DEFAULT_HEALTH_BURN_PER_SEC_LOSS_FRACTION
        self.invisibility = (
         _xml.readFraction(xmlCtx, section, b'invisibility/moving'),
         _xml.readFraction(xmlCtx, section, b'invisibility/still'))
        self.invisibilityDeltas = {b'camouflageBonus': (_xml.readFraction(xmlCtx, section, b'invisibility/camouflageBonus')), 
           b'firePenalty': (_xml.readFraction(xmlCtx, section, b'invisibility/firePenalty'))}
        self.optDevsOverrides = _readOptDevsOverrides(xmlCtx, section[b'optDevsOverrides'])
        self.crewRoles = _readCrew(xmlCtx, section, b'crew')
        commonConfig = g_cache.commonConfig
        if IS_CLIENT or IS_UE_EDITOR or IS_CELLAPP or IS_BOT:
            _id = lambda args: args
            copyMethod = copy.copy if section.has_key(b'extras') else _id
            self.extras = copyMethod(commonConfig[b'extras'])
            self.extrasDict = copyMethod(commonConfig[b'extrasDict'])
            self.devices = copyMethod(commonConfig[b'_devices'])
            self.tankmen = _selectCrewExtras(self.crewRoles, self.extrasDict)
        if IS_CLIENT or IS_WEB or IS_BOT:
            self.i18nInfo = basicInfo.i18n
        if IS_CLIENT or IS_UE_EDITOR:
            self.damageStickersLodDist = commonConfig[b'miscParams'][b'damageStickersLodDist']
            collisionVelCfg = commonConfig[b'miscParams'][b'collisionEffectVelocities']
            self.heavyCollisionEffectVelocities = {b'hull': (collisionVelCfg[b'hull'][1]), 
               b'track': (collisionVelCfg[b'track'][1]), 
               b'waterContact': (collisionVelCfg[b'waterContact'][1])}
            if not IS_UE_EDITOR:
                self.effects = _readVehicleEffects(xmlCtx, section, b'effects', commonConfig[b'defaultVehicleEffects'], useOverride=True)
            else:
                self.effects, self.editorData.damagedStateGroup = _readVehicleEffects(xmlCtx, section, b'effects', commonConfig[b'defaultVehicleEffects'][0], useOverride=True)
                if self.editorData.damagedStateGroup is None:
                    self.editorData.damagedStateGroup = commonConfig[b'defaultDamagedStateGroup']
            self.prefabs = shared_readers.readPrefabsSets(section[b'prefabs'], (b'mechanicEffects',))
            self.camouflage = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=shared_components.DEFAULT_CAMOUFLAGE)
            self.emblemsLodDist = shared_readers.readLodDist(xmlCtx, section, b'emblems/lodDist', g_cache)
            self.emblemsAlpha = _xml.readFraction(xmlCtx, section, b'emblems/alpha')
            self._prereqs = None
            self.clientAdjustmentFactors = _readClientAdjustmentFactors(xmlCtx, section)
        if IS_CELLAPP or IS_CLIENT or IS_UE_EDITOR:
            collisionVelCfg = commonConfig[b'miscParams'][b'collisionEffectVelocities']
            self.collisionEffectVelocities = {b'hull': (collisionVelCfg[b'hull'][0]), 
               b'track': (collisionVelCfg[b'track'][0]), 
               b'waterContact': (collisionVelCfg[b'waterContact'][0]), 
               b'ramming': (collisionVelCfg[b'ramming'])}
        g_cache.playerEmblems()
        self.defaultPlayerEmblemID = _xml.readNonNegativeInt(xmlCtx, section, b'emblems/default')
        NATIONAL_EMBLEMS.add(self.defaultPlayerEmblemID)
        self._defEmblem = (
         self.defaultPlayerEmblemID, _CUSTOMIZATION_EPOCH, 0)
        self._defEmblems = (self._defEmblem, self._defEmblem, self._defEmblem, self._defEmblem)
        pricesDest = _g_prices
        if pricesDest is not None:
            pricesDest[b'vehicleCamouflagePriceFactors'][self.compactDescr] = _xml.readNonNegativeFloat(xmlCtx, section, b'camouflage/priceFactor')
        unlocksDescrs = []
        self.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs)
        defHull = _readHull((xmlCtx, b'hull'), _xml.getSubsection(xmlCtx, section, b'hull'))
        self.damageByStaticsChances = _readDamageByStaticsChances(xmlCtx, section, b'damageByStaticsChances')
        self.chassis = _readInstallableComponents(xmlCtx, section, b'chassis', nationID, _readChassis, _readChassisLocals, g_cache.chassis(nationID), g_cache.chassisIDs(nationID), unlocksDescrs, isWheeledVehicle=self.isWheeledVehicle)
        self.engines = _readInstallableComponents(xmlCtx, section, b'engines', nationID, _readEngine, _readEngineLocal, g_cache.engines(nationID), g_cache.engineIDs(nationID), unlocksDescrs)
        self.fuelTanks = _readInstallableComponents(xmlCtx, section, b'fuelTanks', nationID, _readFuelTank, _defaultLocalReader, g_cache.fuelTanks(nationID), g_cache.fuelTankIDs(nationID), unlocksDescrs)
        self.radios = _readInstallableComponents(xmlCtx, section, b'radios', nationID, _readRadio, _defaultLocalReader, g_cache.radios(nationID), g_cache.radioIDs(nationID), unlocksDescrs)
        turretsList = []
        for n in xrange(len(defHull.turretPositions)):
            turrets = _readInstallableComponents(xmlCtx, section, b'turrets' + repr(n), nationID, _readTurret, _readTurretLocals, g_cache.turrets(nationID), g_cache.turretIDs(nationID), unlocksDescrs)
            turretsList.append(turrets)

        self.turrets = tuple(turretsList)
        self.hulls = (
         defHull,)
        if section.has_key(b'hull/variants'):
            self.hulls += _readHullVariants((
             xmlCtx, b'hull/variants'), section[b'hull/variants'], defHull, self.chassis, self.turrets)
        compactDescrs = set()
        _collectComponents(compactDescrs, self.chassis)
        _collectComponents(compactDescrs, self.engines)
        _collectComponents(compactDescrs, self.fuelTanks)
        _collectComponents(compactDescrs, self.radios)
        for turrets in self.turrets:
            _collectComponents(compactDescrs, turrets)
            for turret in turrets:
                _collectComponents(compactDescrs, turret.guns)

        self.installableComponents = compactDescrs
        self.unlocksDescrs = self.__convertAndValidateUnlocksDescrs(unlocksDescrs)
        self.autounlockedItems = self.__collectDefaultUnlocks()
        self.isRotationStill = section.readBool(b'isRotationStill', False)
        self.useHullZSize = section.readBool(b'useHullZSize', False)
        self.useHullZOffset = section.readBool(b'useHullZOffset', False)
        self.siegeModeParams = _readSiegeModeParams(xmlCtx, section, self)
        self.hullAimingParams = _readHullAimingParams(xmlCtx, section)
        self.armorMaxHealth = _xml.readIntOrNone(xmlCtx, section, b'armorMaxHealth')
        mechanicsSection = section[b'mechanics']
        self.mechanicsParams = {}
        if mechanicsSection is not None:
            for mechanicsCls in shared_components.MechanicsParams.getSubClasses():
                if mechanicsCls.COMPONENT_TYPE_ID is not None:
                    continue
                params = mechanicsCls.readMechanicsParams(xmlCtx, mechanicsSection, readModifiers)
                if params is not None:
                    self.mechanicsParams[mechanicsCls.MECHANICS_NAME] = params

        if self.hasRocketAcceleration:
            self.rocketAccelerationParams = _readRocketAccelerationParams(xmlCtx, section)
        else:
            self.rocketAccelerationParams = None
        if IS_CELLAPP:
            overmatchVer = _xml.readIntOrNone(xmlCtx, section, b'overmatchMechanicsVer')
            if overmatchVer is None:
                overmatchVer = OVERMATCH_MECHANICS_VER.DEFAULT
            self.overmatchMechanicsVer = overmatchVer
            try:
                self.xphysics = _readXPhysics(xmlCtx, section, b'physics', self)
            except:
                LOG_CURRENT_EXCEPTION()
                self.xphysics = None

            if self.xphysics:
                _validateBrokenTrackLosses(xmlCtx, self)
        elif IS_CLIENT or IS_WEB:
            self.xphysics = _readXPhysicsClient(xmlCtx, section, b'physics', self)
        elif IS_UE_EDITOR:
            self.xphysics = _readXPhysicsEditor(xmlCtx, section, b'physics', self)
        else:
            self.xphysics = None
        if (IS_CLIENT or IS_UE_EDITOR) and section.has_key(b'repaintParameters'):
            self.repaintParameters = _readRepaintParams(xmlCtx, _xml.getSubsection(xmlCtx, section, b'repaintParameters'))
        if (IS_CLIENT or IS_UE_EDITOR or IS_CELLAPP or IS_BOT) and section.has_key(b'extras'):
            _readExtraLocals(self, (xmlCtx, b'extras'), section)
        if IS_CELLAPP or IS_UE_EDITOR:
            self.extrasProtection = _readExtrasProtection(self, xmlCtx, section)
        if IS_CELLAPP:
            self.rollerExtras = [extra for extra in self.devices if extra.isTrack and getattr(extra, b'isWheel', False) == self.isWheeledVehicle]
            if self.isWheeledVehicle:
                self.rollerExtras.sort(key=(lambda extra: extra.getNumber()))
            else:
                self.rollerExtras.sort(key=(lambda extra: (not extra.isLeft) + (extra.name not in self.extrasProtection[b'protecting'])))
            _provideMultipleExtras(self)
        if IS_CLIENT or IS_UE_EDITOR:
            self.__checkMatchingTags()
        if IS_CELLAPP or IS_CLIENT and section.has_key(b'visualScript'):
            from visual_script.misc import ASPECT, readVisualScriptSection
            self.visualScript = readVisualScriptSection(section, [ASPECT.CLIENT, ASPECT.SERVER])
        VehicleType.currentReadingVeh = None
        section = None
        ResMgr.purge(xmlPath, True)
        return

    def retrieveSectionToSave(self, mainXmlPath, useSharedSections=True):
        mainSection = ResMgr.openSection(mainXmlPath)
        if mainSection is None:
            _xml.raiseWrongXml(None, mainXmlPath, b'can not open or read')
        _writeCamouflageSettings(mainSection, b'camouflage', self.camouflage)
        _xml.rewriteFloat(mainSection, b'speedLimits/forward', self.speedLimits[0] * component_constants.MS_TO_KMH)
        _xml.rewriteFloat(mainSection, b'speedLimits/backward', self.speedLimits[1] * component_constants.MS_TO_KMH)
        _xml.rewriteFloat(mainSection, b'emblems/alpha', self.emblemsAlpha)
        _xml.rewriteString(mainSection, b'effects/damagedStateGroup', self.editorData.damagedStateGroup, b'medium')
        sharedSections = {}
        nationID = self.id[0]
        nationName = nations.NAMES[nationID]
        extension = mainXmlPath[0:mainXmlPath.find(b'scripts/')]
        if useSharedSections:
            for componentId in ITEM_TYPES.values():
                if componentId in Cache.NATION_ITEM_SOURCE:
                    compsXmlPath = (b'{vehcilePath}{nationName}{componentsPath}{componentSource}').format(vehcilePath=extension + _VEHICLE_TYPE_XML_PATH, nationName=nationName, componentsPath=Cache.NATION_COMPONENTS_SECTION, componentSource=Cache.NATION_ITEM_SOURCE[componentId])
                    ResMgr.purge(compsXmlPath, True)
                    section = ResMgr.openSection(compsXmlPath)
                    if section is None:
                        _xml.raiseWrongXml(None, compsXmlPath, b"Can't open shared section")
                    sharedSections[componentId] = section

        materialData = tankArmor.TankArmorHelper().collectData()
        _writeXPhysicsDetailed(self.xphysics[b'detailed'], mainSection[b'physics/detailed'])
        _writeHulls(self.hulls, mainSection, materialData.get(b'hull', None))
        _writeInstallableComponents(self.chassis, mainSection, b'chassis', _writeChassis, g_cache.chassisIDs(nationID), sharedSections, materialData=materialData)
        defHull = self.hulls[0]
        for n in xrange(len(defHull.turretPositions)):
            _writeInstallableComponents(self.turrets[n], mainSection, b'turrets' + repr(n), _writeTurret, g_cache.turretIDs(nationID), sharedSections, materialData=materialData)

        for section in sharedSections.values():
            section.save()

        return mainSection

    @staticmethod
    def saveCustomization():
        from items.writers import c11n_writers
        customizationCache = g_cache.customization20(False)
        if customizationCache is not None:
            c11n_writers.saveCustomizationItems(customizationCache, _CUSTOMIZATION_XML_PATH)
        return

    @property
    def userString(self):
        return self.i18nInfo.userString

    @property
    def shortUserString(self):
        return self.i18nInfo.shortString

    @property
    def description(self):
        return self.i18nInfo.description

    @property
    def shortDescriptionSpecial(self):
        return self.i18nInfo.shortDescriptionSpecial

    @property
    def longDescriptionSpecial(self):
        return self.i18nInfo.longDescriptionSpecial

    @property
    def isCustomizationLocked(self):
        return b'lockOutfit' in self.tags

    @property
    def isRestoredWithStyle(self):
        return b'restoreWithStyle' in self.tags

    @property
    def progressionDecalsOnly(self):
        return b'lockExceptProgression' in self.tags

    @property
    def isEquipmentLocked(self):
        return b'lockEquipment' in self.tags

    @property
    def isOptionalDevicesLocked(self):
        return b'lockOptionalDevices' in self.tags

    @property
    def innationID(self):
        return self.id[1]

    @property
    def siegeDeviceName(self):
        if self.siegeModeParams is not None:
            return self.siegeModeParams[b'device']
        else:
            return b''

    @property
    def shouldStopEngineOnSiegeSwitch(self):
        if self.siegeModeParams is not None:
            return self.siegeModeParams[b'stopEngineOnSwitch']
        else:
            return True

    @property
    def isEliteByDefault(self):
        return not self.unlocksDescrs and not self.eliteByProgression

    def update(self, data):
        if json_vehicle_reader:
            json_vehicle_reader.readVehicle(self, data)
        else:
            LOG_WARNING(b'Json vehicle reader is not found')
        return

    def getGuns(self):
        res = []
        for data in self.turrets:
            for turret in data:
                for gun in turret.guns:
                    res.append(gun)

        return res

    def getVehicleClass(self):
        return getVehicleClassFromVehicleType(self)

    def __getRoleFromTags(self):
        roles = g_cache.roles()
        suitableRoles = [tag for tag in roles if ROLE_TYPE_TO_LABEL[tag] in self.tags]
        if not suitableRoles:
            return ROLE_TYPE.NOT_DEFINED
        if len(suitableRoles) > 1:
            raise SoftException(b"There are several roles for vehicle '%s': '%s'" % (self.name, suitableRoles))
        return suitableRoles[0]

    def __getActionsFromRole(self, role):
        actionsByRoles = g_cache.roles()
        return actionsByRoles.get(role, None)

    def __getClassFromTags(self):
        classes = [classTag for classTag in VEHICLE_CLASSES if classTag in self.tags]
        if len(classes) > 1:
            raise SoftException(b"There are several classes for vehicle '%s': '%s'" % (self.name, classes))
        return classes[0]

    def __convertAndValidateUnlocksDescrs(self, srcList):
        nationID = self.id[0]
        destList = []
        reqItems = {}
        for descr in srcList:
            itemTypeName = descr[1]
            itemName = descr[2]
            itemID = None
            try:
                if itemTypeName == b'vehicle':
                    itemID = g_list.getIDsByName(nations.NAMES[nationID] + b':' + itemName)[1]
                if itemTypeName == b'vehicleChassis':
                    itemID = g_cache.chassisIDs(nationID)[itemName]
                if itemTypeName == b'vehicleTurret':
                    itemID = g_cache.turretIDs(nationID)[itemName]
                if itemTypeName == b'vehicleGun':
                    itemID = g_cache.gunIDs(nationID)[itemName]
                if itemTypeName == b'vehicleEngine':
                    itemID = g_cache.engineIDs(nationID)[itemName]
                if itemTypeName == b'vehicleFuelTank':
                    itemID = g_cache.fuelTankIDs(nationID)[itemName]
                if itemTypeName == b'vehicleRadio':
                    itemID = g_cache.radioIDs(nationID)[itemName]
            except Exception:
                LOG_CURRENT_EXCEPTION()
                raise SoftException(b"wrong name '%s' in <unlocks> of '%s'" % (itemName, self.name))

            compactDescr = makeIntCompactDescrByID(itemTypeName, nationID, itemID)
            if itemTypeName != b'vehicle' and compactDescr not in self.installableComponents:
                raise SoftException(b"component '%s' in <unlocks> is not for '%s'" % (itemName, self.name))
            reqItems.setdefault(compactDescr, set()).update(descr[3:])
            destList.append((descr[0], compactDescr))

        for descr in viewvalues(reqItems):
            for compactDescr in tuple(descr):
                _collectReqItemsRecursively(descr, tuple(reqItems.get(compactDescr, ())), reqItems)

        for idx in xrange(len(destList)):
            descr = destList[idx]
            destList[idx] = descr + tuple(reqItems[descr[1]])

        return destList

    def __collectDefaultUnlocks(self):
        autounlocks = []
        autounlocks.append(self.chassis[0].compactDescr)
        autounlocks.append(self.engines[0].compactDescr)
        autounlocks.append(self.fuelTanks[0].compactDescr)
        autounlocks.append(self.radios[0].compactDescr)
        for posIndex, turrets in enumerate(self.turrets):
            turret = turrets[0]
            autounlocks.append(turret.compactDescr)
            autounlocks.append(turret.guns[0].compactDescr)
            if posIndex in self.hulls[0].fakeTurrets[b'lobby']:
                for turret in turrets[1:]:
                    autounlocks.append(turret.compactDescr)

        return autounlocks

    def __checkMatchingTags(self):
        hullsMatchingTags = set()
        for hull in self.hulls:
            hullsMatchingTags = self.____checkPartMatchingTags(hull)

        for turrets in self.turrets:
            for turret in turrets:
                turretsMatchingTags = self.____checkPartMatchingTags(turret)
                for gun in turret.guns:
                    gunMatchingTags = self.____checkPartMatchingTags(gun)
                    repeatingTags = hullsMatchingTags & gunMatchingTags | hullsMatchingTags & turretsMatchingTags | gunMatchingTags & turretsMatchingTags
                    if repeatingTags:
                        LOG_ERROR(b'repeating matching tags between hull, turret and gun : %s for %s' % (
                         repeatingTags, self.name))

        return

    def ____checkPartMatchingTags(self, part):
        tags = set()
        projectionDecalSlots = [slot for slot in part.slotsAnchors if slot.type == b'projectionDecal']
        for slot in projectionDecalSlots:
            matchingTags = [tag for tag in slot.tags if tag in ProjectionDecalMatchingTags.ALL]
            if len(matchingTags) > 1:
                LOG_ERROR(b'several matching tags for slot ID%i' % slot.slotId)
            for matchingTag in matchingTags:
                addTags = getDirectionAndFormFactorTags(slot)
                if addTags:
                    directionTag, formfactorTag = addTags
                    tagsSet = (matchingTag, directionTag, formfactorTag)
                    if tagsSet not in tags:
                        tags.add(tagsSet)
                    else:
                        LOG_ERROR(b'repeating matching tags: %s for %s' % (tagsSet, self.name))

        return tags


class SupplySlotsStorageCache(object):
    __slots__ = (b'__cache',)

    def __init__(self):
        self.__cache = {}
        return

    def getStorage(self, slotIDs):
        slotIDs = tuple(slotIDs)
        if slotIDs not in self.__cache:
            self.__cache[slotIDs] = SupplySlotsStorage(slotIDs)
        return self.__cache[slotIDs]


class SupplySlotsStorage(object):
    __slots__ = (b'_slotIDs', b'_slotsByType')
    ALL_IDS_KEY = -1

    def __init__(self, slotIDs):
        super(SupplySlotsStorage, self).__init__()
        self._slotIDs = slotIDs
        self._slotsByType = {}
        supplySlots = g_cache.supplySlots()
        for slotID in slotIDs:
            slotDescr = supplySlots.getSlotDescr(slotID)
            subType = slotDescr.getSubType()
            itemTypeStorage = self._slotsByType.setdefault(slotDescr.itemType, {})
            itemTypeStorage.setdefault(SupplySlotsStorage.ALL_IDS_KEY, []).append(slotID)
            if subType is not None:
                itemTypeStorage.setdefault(subType, []).append(slotID)

        self._checkRestrictions()
        return

    def getSlotIDsByType(self, itemType, subItemType=None):
        slotsByType = self._slotsByType
        if itemType in slotsByType:
            if itemType not in slotsByType:
                return []
            slotsForType = slotsByType[itemType]
            subItemType = subItemType if subItemType is not None else SupplySlotsStorage.ALL_IDS_KEY
            if subItemType in slotsForType:
                return slotsForType[subItemType]
        return []

    def getAmountForType(self, itemType, *subItemTypes):
        if len(subItemTypes) == 0:
            return len(self.getSlotIDsByType(itemType))
        res = 0
        getSlotIDsByType = self.getSlotIDsByType
        for subType in subItemTypes:
            res += len(getSlotIDsByType(itemType, subType))

        return res

    def getSlotByIdxInItemType(self, itemType, inItemTypeIdx):
        slotIDs = self.getSlotIDsByType(itemType)
        if inItemTypeIdx < len(slotIDs):
            return g_cache.supplySlots().getSlotDescr(slotIDs[inItemTypeIdx])
        else:
            return

    @property
    def slotIDs(self):
        return self._slotIDs

    def checkLayoutCompatibility(self, itemType, itemLayout):
        slotIDs = self.getSlotIDsByType(itemType)
        if len(itemLayout) > len(slotIDs):
            return (False,
             (b'Cannot apply layout for itemType {}, exceed allowed number of supply ({} > {})').format(itemType, len(itemLayout), len(slotIDs)))
        else:
            supplySlots = g_cache.supplySlots()
            for slotID, itemCompDescr in zip(slotIDs, itemLayout):
                if itemCompDescr == 0:
                    continue
                slotDescr = supplySlots.getSlotDescr(slotID)
                res = slotDescr.checkSlotCompatibility(compDescr=itemCompDescr)
                if not res[0]:
                    return res

            return (
             True, None)

    def _checkRestrictions(self):
        optDevs = self.getSlotIDsByType(ITEM_TYPES.optionalDevice)
        if len(optDevs) > MAX_OPTIONAL_DEVICES_SLOTS:
            raise SoftException((b'Number of optional devices ({}) must be less that MAX_OPTIONAL_DEVICES_SLOTS({})').format(len(optDevs), MAX_OPTIONAL_DEVICES_SLOTS))
        shellSlots = self.getAmountForType(ITEM_TYPES.shell)
        if shellSlots != NUM_SHELLS_SLOTS:
            raise SoftException((b'Number of shells ({}) must be equal to NUM_SHELLS_SLOTS({}) now').format(shellSlots, NUM_SHELLS_SLOTS))
        return


PrefabEffects = typing.NamedTuple(b'PrefabEffects', (
 (
  b'gun', prefab_effects_readers.GunEffectDescMap),
 (
  b'shot', prefab_effects_readers.ShotEffects),
 (
  b'decals', prefab_effects_readers.Decals)))

class Cache(object):
    __slots__ = (b'__vehicles', b'__commonConfig', b'__chassis', b'__engines', b'__fuelTanks', b'__radios', b'__turrets', b'__guns', b'__shells', b'__optionalDevices', b'__optionalDeviceIDs', b'__equipments', b'__equipmentIDs', b'__chassisIDs', b'__engineIDs', b'__fuelTankIDs', b'__radioIDs', b'__turretIDs', b'__gunIDs', b'__shellIDs', b'__customization', b'__playerEmblems', b'__shotEffects', b'__shotEffectsIndexes', b'__shotEffectsNames', b'__damageStickers', b'__vehicleEffects', b'__gunEffects', b'__gunReloadEffects', b'__gunRecoilEffects', b'__turretDetachmentEffects', b'__customEffects', b'__requestOncePrereqs', b'__customization20', b'__roles', b'__supplySlots', b'__supplySlotsStorages', b'__moduleKind', b'__postProgression', b'__prefabEffects', b'__vehicleMechanics', b'__camouflageBonusDelta')
    NATION_COMPONENTS_SECTION = b'/components/'
    NATION_ITEM_SOURCE = {(ITEM_TYPES.vehicleChassis): b'chassis.xml', 
       (ITEM_TYPES.vehicleEngine): b'engines.xml', 
       (ITEM_TYPES.vehicleFuelTank): b'fuelTanks.xml', 
       (ITEM_TYPES.vehicleRadio): b'radios.xml', 
       (ITEM_TYPES.vehicleGun): b'guns.xml', 
       (ITEM_TYPES.vehicleTurret): b'turrets.xml'}

    def __init__(self):
        self.__vehicles = {}
        self.__commonConfig = None
        self.__chassis = [None for _ in nations.NAMES]
        self.__engines = [None for _ in nations.NAMES]
        self.__fuelTanks = [None for _ in nations.NAMES]
        self.__radios = [None for _ in nations.NAMES]
        self.__turrets = [None for _ in nations.NAMES]
        self.__guns = [None for _ in nations.NAMES]
        self.__shells = [None for _ in nations.NAMES]
        self.__optionalDevices = None
        self.__optionalDeviceIDs = None
        self.__equipments = None
        self.__equipmentIDs = None
        self.__chassisIDs = [None for _ in nations.NAMES]
        self.__engineIDs = [None for _ in nations.NAMES]
        self.__fuelTankIDs = [None for _ in nations.NAMES]
        self.__radioIDs = [None for _ in nations.NAMES]
        self.__turretIDs = [None for _ in nations.NAMES]
        self.__gunIDs = [None for _ in nations.NAMES]
        self.__shellIDs = [None for _ in nations.NAMES]
        self.__customization20 = None
        self.__customization = [None for _ in nations.NAMES]
        self.__playerEmblems = None
        self.__shotEffects = None
        self.__shotEffectsIndexes = None
        self.__shotEffectsNames = None
        self.__damageStickers = None
        self.__roles = None
        self.__supplySlots = None
        self.__supplySlotsStorages = None
        self.__moduleKind = {}
        self.__postProgression = None
        self.__vehicleMechanics = None
        self.__prefabEffects = None
        self.__camouflageBonusDelta = (1.0, 0.0)
        if IS_CLIENT or IS_UE_EDITOR:
            self.__vehicleEffects = None
            self.__gunEffects = None
            self.__gunReloadEffects = None
            self.__gunRecoilEffects = None
            self.__turretDetachmentEffects = None
            self.__customEffects = None
            self.__requestOncePrereqs = set()
        return

    @property
    def requestOncePrereqs(self):
        return self.__requestOncePrereqs

    def clearPrereqs(self):
        return

    def vehicle(self, nationID, vehicleTypeID, vehMode=VEHICLE_MODE.DEFAULT):
        if vehMode == VEHICLE_MODE.DEFAULT:
            id = (
             nationID, vehicleTypeID)
        else:
            id = (
             nationID, vehicleTypeID, vehMode)
        vt = self.__vehicles.get(id)
        if vt:
            return vt
        nation = nations.NAMES[nationID]
        basicInfo = g_list.getList(nationID)[vehicleTypeID]
        xmlName = basicInfo.name.split(b':')[1] + VEHICLE_MODE_FILE_SUFFIX[vehMode]
        xmlPath = _VEHICLE_TYPE_XML_PATH + nation + b'/' + xmlName + b'.xml'
        vt = VehicleType(nationID, basicInfo, xmlPath, vehMode)
        self.__vehicles[id] = vt
        if VEHICLE_SECRET_TAG not in vt.tags:
            camouflageBonus = vt.invisibilityDeltas[b'camouflageBonus']
            minBonus, maxBonus = self.__camouflageBonusDelta
            self.__camouflageBonusDelta = (min(minBonus, camouflageBonus), max(maxBonus, camouflageBonus))
        return vt

    def getVehicles(self):
        return viewvalues(self.__vehicles)

    def getCamouflageBonusDelta(self):
        return self.__camouflageBonusDelta

    def chassis(self, nationID):
        return self.__getList(nationID, b'chassis')

    def chassisIDs(self, nationID):
        return self.__getList(nationID, b'chassisIDs')

    def engines(self, nationID):
        return self.__getList(nationID, b'engines')

    def engineIDs(self, nationID):
        return self.__getList(nationID, b'engineIDs')

    def fuelTanks(self, nationID):
        return self.__getList(nationID, b'fuelTanks')

    def fuelTankIDs(self, nationID):
        return self.__getList(nationID, b'fuelTankIDs')

    def radios(self, nationID):
        return self.__getList(nationID, b'radios')

    def radioIDs(self, nationID):
        return self.__getList(nationID, b'radioIDs')

    def turrets(self, nationID):
        return self.__getList(nationID, b'turrets')

    def turretIDs(self, nationID):
        return self.__getList(nationID, b'turretIDs')

    def guns(self, nationID):
        return self.__getList(nationID, b'guns')

    def gunIDs(self, nationID):
        return self.__getList(nationID, b'gunIDs')

    def shells(self, nationID):
        return self.__getList(nationID, b'shells')

    def shellIDs(self, nationID):
        return self.__getList(nationID, b'shellIDs')

    def exhaustEffect(self, effectName):
        if b'exhaust' in self.__customEffects:
            return self.__customEffects[b'exhaust'].get(effectName)
        else:
            return

    @property
    def exhaustEffects(self):
        return self.__customEffects.get(b'exhaust', {})

    def customization20(self, createNew=True):
        if self.__customization20 is None and createNew:
            from items.components.c11n_components import CustomizationCache
            from items.readers.c11n_readers import readCustomizationCacheFromXml
            self.__customization20 = CustomizationCache()
            readCustomizationCacheFromXml(self.__customization20, _CUSTOMIZATION_XML_PATH)
        return self.__customization20

    def supplySlots(self):
        if self.__supplySlots is None:
            from items.components.supply_slots_components import SupplySlotsCache
            self.__supplySlots = SupplySlotsCache(_VEHICLE_TYPE_XML_PATH + b'common/supply_slot_types.xml')
        return self.__supplySlots

    def supplySlotsStorage(self):
        if self.__supplySlotsStorages is None:
            self.__supplySlotsStorages = SupplySlotsStorageCache()
        return self.__supplySlotsStorages

    def postProgression(self):
        if self.__postProgression is None:
            _POST_PROGRESSION_XML_ROOT = _VEHICLE_TYPE_XML_PATH + b'common/post_progression/'
            self.__postProgression = PostProgressionCache(_POST_PROGRESSION_XML_ROOT + b'features.xml', _POST_PROGRESSION_XML_ROOT + b'modifications.xml', _POST_PROGRESSION_XML_ROOT + b'pairs.xml', _POST_PROGRESSION_XML_ROOT + b'trees.xml', _POST_PROGRESSION_XML_ROOT + b'prices.xml')
        return self.__postProgression

    def customization(self, nationID):
        descr = self.__customization[nationID]
        if descr is None:
            nationName = nations.NAMES[nationID]
            descr = {}
            if nationName in nations.AVAILABLE_NAMES:
                commonDescr = _readCustomization(_VEHICLE_TYPE_XML_PATH + b'common/customization.xml', nationID, idsRange=(5001, 65535))
                customDescr = _readCustomization(_VEHICLE_TYPE_XML_PATH + nationName + b'/customization.xml', nationID, idsRange=(1, 5000))
                descr = _joinCustomizationParams(nationID, commonDescr, customDescr)
            self.__customization[nationID] = descr
        return descr

    def playerEmblems(self):
        if IS_CLIENT:
            descr = ({}, {}, {})
            return descr
        else:
            descr = self.__playerEmblems
            if descr is None:
                descr = self.__playerEmblems = _readPlayerEmblems(_VEHICLE_TYPE_XML_PATH + b'common/player_emblems.xml')
            return descr

    def optionalDevices(self):
        if self.__optionalDevices is None:
            self.__loadOptionalDevices()
        return self.__optionalDevices

    def optionalDeviceIDs(self):
        if self.__optionalDeviceIDs is None:
            self.__loadOptionalDevices()
        return self.__optionalDeviceIDs

    def getOptionalDeviceByName(self, name):
        if self.__optionalDeviceIDs is None:
            self.__loadOptionalDevices()
        return self.__optionalDevices.get(self.__optionalDeviceIDs.get(name))

    def __loadOptionalDevices(self):
        self.__optionalDevices, self.__optionalDeviceIDs = _readArtefacts(_VEHICLE_TYPE_XML_PATH + b'common/optional_devices.xml')
        return

    def equipments(self):
        descr = self.__equipments
        if descr is None:
            self.__equipments, self.__equipmentIDs = _readArtefacts(_VEHICLE_TYPE_XML_PATH + b'common/equipments.xml')
            descr = self.__equipments
        return descr

    @lru_cache(maxsize=20)
    def equipmentCDsByTags(self, requiredTags=frozenset(), forbiddenTags=frozenset()):
        equipmentCDs = set()
        for equipment in viewvalues(self.equipments()):
            eqTags = equipment.tags
            if requiredTags.issubset(eqTags) and not eqTags & forbiddenTags:
                equipmentCDs.add(equipment.compactDescr)

        return equipmentCDs

    def equipmentIDs(self):
        descr = self.__equipmentIDs
        if descr is None:
            self.__equipments, self.__equipmentIDs = _readArtefacts(_VEHICLE_TYPE_XML_PATH + b'common/equipments.xml')
            descr = self.__equipmentIDs
        return descr

    def roles(self):
        roles = self.__roles
        if roles is None:
            self.__roles = _readVehicleRoles(_VEHICLE_TYPE_XML_PATH + b'common/roleExp/roles.xml')
            roles = self.__roles
        return roles

    @property
    def shotEffects(self):
        descr = self.__shotEffects
        if descr is None:
            self.__shotEffectsIndexes, self.__shotEffects = _readShotEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/shot_effects.xml')
            descr = self.__shotEffects
        return descr

    @property
    def shotEffectsIndexes(self):
        descr = self.__shotEffectsIndexes
        if descr is None:
            self.__shotEffectsIndexes, self.__shotEffects = _readShotEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/shot_effects.xml')
            descr = self.__shotEffectsIndexes
        return descr

    @property
    def shotEffectsNames(self):
        if self.__shotEffectsNames is None:
            self.__shotEffectsNames = {name: idx for idx, name in viewitems(self.shotEffectsIndexes)}
        return self.__shotEffectsNames

    @property
    def damageStickers(self):
        descr = self.__damageStickers
        if descr is None:
            descr = self.__damageStickers = _readDamageStickers(_VEHICLE_TYPE_XML_PATH + b'common/damage_stickers.xml')
        return descr

    @property
    def commonConfig(self):
        descr = self.__commonConfig
        if descr is None:
            commonXmlPath = _VEHICLE_TYPE_XML_PATH + b'common/vehicle.xml'
            commonXml = ResMgr.openSection(commonXmlPath)
            if commonXml is None:
                _xml.raiseWrongXml(None, commonXmlPath, b'can not open or read')
            descr = self.__commonConfig = _readCommonConfig((None, commonXmlPath), commonXml)
            commonXml = None
            ResMgr.purge(commonXmlPath, True)
        return descr

    @property
    def vehicleMechanics(self):
        mechanics = self.__vehicleMechanics
        if mechanics is None:
            mechanics = self.__vehicleMechanics = _readVehicleMechanics(_VEHICLE_TYPE_XML_PATH + b'common/vehicle_mechanics.xml')
        return mechanics

    def getGunRecoilEffects(self, effectName):
        return self._gunRecoilEffects.get(effectName, None)

    def getVehicleEffect(self, effectID):
        return self._vehicleEffects.get(effectID)

    def getEquipmentByName(self, name):
        equipmentID = self.equipmentIDs().get(name)
        if equipmentID is None:
            raise SoftException(b"unknown equipment '%s'" % name)
        return self.equipments()[equipmentID]

    @property
    def _vehicleEffects(self):
        if self.__vehicleEffects is None:
            self.__vehicleEffects = _readEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/vehicle_effects.xml', True)
        return self.__vehicleEffects

    @property
    def gunEffects(self):
        if self.__gunEffects is None:
            self.__gunEffects = _readEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/gun_effects.xml')
        return self.__gunEffects

    @property
    def _gunReloadEffects(self):
        if self.__gunReloadEffects is None:
            self.__gunReloadEffects = _readReloadEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/gun_reload_effects.xml')
        return self.__gunReloadEffects

    @property
    def _gunRecoilEffects(self):
        if self.__gunRecoilEffects is None:
            self.__gunRecoilEffects = _readRecoilEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/gun_recoil_effects.xml')
        return self.__gunRecoilEffects

    @property
    def _customEffects(self):
        if self.__customEffects is None:
            self.__customEffects = {}
            self.__customEffects[b'slip'] = _readCustomEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/trackSlip_effects.xml')
            self.__customEffects[b'exhaust'] = _readCustomEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/exhaust_effects.xml')
        return self.__customEffects

    @property
    def prefabEffects(self):
        if self.__prefabEffects is None:
            decals = prefab_effects_readers.readDecals(_PREFAB_EFFECTS_XML_PATH + b'damage_stickers.xml')
            self.__prefabEffects = PrefabEffects(prefab_effects_readers.readGunEffects(_PREFAB_EFFECTS_XML_PATH + b'gun_effects.xml'), prefab_effects_readers.readShotEffects(_PREFAB_EFFECTS_XML_PATH + b'shot_effects.xml', decals), decals)
        return self.__prefabEffects

    @property
    def defaultPrefabEffects(self):
        return self.__commonConfig[b'defaultPrefabEffects']

    @property
    def _turretDetachmentEffects(self):
        if self.__turretDetachmentEffects is None:
            self.__turretDetachmentEffects = _readEffectGroups(_VEHICLE_TYPE_XML_PATH + b'common/turret_effects.xml')
        return self.__turretDetachmentEffects

    def __getList(self, nationID, listName):
        cachedNations = getattr(self, b'_Cache__' + listName)
        if cachedNations[nationID] is None:
            self.__readNation(nationID)
        return cachedNations[nationID]

    def _readModulesLists(self, xmlPath):
        section = ResMgr.openSection(xmlPath)
        if section is None:
            _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
        for key in ModuleKind.ALL:
            self.__moduleKind[key] = _xml.readString(xmlPath, section, b'moduleKind/' + key).split()
            moduleName = self.__moduleKind[key]
            modules = set()
            for module in moduleName:
                moduleID = IDS_BY_NAMES.get(module)
                if not moduleID:
                    _xml.raiseWrongXml((_VEHICLE_TYPE_XML_PATH + b'common', b'vehicle_common.xml'), b'moduleKind/' + key, b'module is not existing in system/data/vehicle_common.xml')
                modules.add(moduleID)

            self.__moduleKind[key] = modules

        return

    @property
    def moduleKind(self):
        if not self.__moduleKind:
            self._readModulesLists(_VEHICLE_TYPE_XML_PATH + b'common/vehicle_common.xml')
        return self.__moduleKind

    def __readNation(self, nationID):
        nationName = nations.NAMES[nationID]
        if nationName not in nations.AVAILABLE_NAMES:
            emptyDict = {}
            self.__chassis[nationID], self.__chassisIDs[nationID] = emptyDict, emptyDict
            self.__engines[nationID], self.__engineIDs[nationID] = emptyDict, emptyDict
            self.__fuelTanks[nationID], self.__fuelTankIDs[nationID] = emptyDict, emptyDict
            self.__radios[nationID], self.__radioIDs[nationID] = emptyDict, emptyDict
            self.__turrets[nationID], self.__turretIDs[nationID] = emptyDict, emptyDict
            self.__guns[nationID], self.__gunIDs[nationID] = emptyDict, emptyDict
            self.__shells[nationID], self.__shellIDs[nationID] = emptyDict, emptyDict
            return
        compsXmlPath = _VEHICLE_TYPE_XML_PATH + nationName + self.NATION_COMPONENTS_SECTION
        self.__chassis[nationID], self.__chassisIDs[nationID] = _readComponents(compsXmlPath + self.NATION_ITEM_SOURCE[ITEM_TYPES.vehicleChassis], _readChassis, nationID, ITEM_TYPES.vehicleChassis)
        self.__engines[nationID], self.__engineIDs[nationID] = _readComponents(compsXmlPath + self.NATION_ITEM_SOURCE[ITEM_TYPES.vehicleEngine], _readEngine, nationID, ITEM_TYPES.vehicleEngine)
        self.__fuelTanks[nationID], self.__fuelTankIDs[nationID] = _readComponents(compsXmlPath + self.NATION_ITEM_SOURCE[ITEM_TYPES.vehicleFuelTank], _readFuelTank, nationID, ITEM_TYPES.vehicleFuelTank)
        self.__radios[nationID], self.__radioIDs[nationID] = _readComponents(compsXmlPath + self.NATION_ITEM_SOURCE[ITEM_TYPES.vehicleRadio], _readRadio, nationID, ITEM_TYPES.vehicleRadio)
        self.__shells[nationID], self.__shellIDs[nationID] = _readShells(compsXmlPath + b'shells.xml', nationID)
        self.__guns[nationID], self.__gunIDs[nationID] = _readComponents(compsXmlPath + self.NATION_ITEM_SOURCE[ITEM_TYPES.vehicleGun], _readGun, nationID, ITEM_TYPES.vehicleGun)
        self.__turrets[nationID], self.__turretIDs[nationID] = _readComponents(compsXmlPath + self.NATION_ITEM_SOURCE[ITEM_TYPES.vehicleTurret], _readTurret, nationID, ITEM_TYPES.vehicleTurret)
        return


class VehicleList(object):

    def __init__(self):
        self.__ids = {}
        self.__categories = {}
        self.__typeCompDescrToLevel = typeCompDescrToLevel = {}
        typeCompDescrsByLevel = {level: [] for level in range(MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL + 1)}
        list = []
        for nation in nations.NAMES:
            if nation not in nations.AVAILABLE_NAMES:
                list.append({})
                continue
            xmlPath = _VEHICLE_TYPE_XML_PATH + nation + b'/list.xml'
            section = ResMgr.openSection(xmlPath)
            if section is None:
                _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
            descrs = self.__readVehicleList(nation, section, xmlPath)
            list.append(descrs)
            nationID = nations.INDICES[nation]
            for d in viewvalues(descrs):
                self.__categories.setdefault((nationID, (set(d.tags) & VEHICLE_CLASS_TAGS).pop(), d.level), 0)
                self.__categories[(nationID, (set(d.tags) & VEHICLE_CLASS_TAGS).pop(), d.level)] += 1

            self.__ids.update(dict((d.name, (nationID, d.id)) for d in viewvalues(descrs)))
            for descr in viewvalues(descrs):
                typeCompDescrsByLevel[descr.level].append(descr.compactDescr)
                typeCompDescrToLevel[descr.compactDescr] = descr.level

            ResMgr.purge(xmlPath, True)

        self.__nations = tuple(list)
        self.__typeCompDescrsByLevel = {level: frozenset(vehTypeCompDescrs) for level, vehTypeCompDescrs in viewitems(typeCompDescrsByLevel)}
        return

    def getList(self, nationID):
        if nationID < len(self.__nations):
            return self.__nations[nationID]
        else:
            return

    def getCategories(self, nationID=None, vehClass=None, level=None, excluded=()):
        result = copy.copy(self.__categories)
        for tcd in excluded:
            if parseIntCompactDescr(tcd)[0] != ITEM_TYPES.vehicle:
                continue
            category = (lambda vt: (
             vt.id[0], (set(vt.tags) & VEHICLE_CLASS_TAGS).pop(),
             vt.level))(getVehicleType(tcd))
            result[category] = count = result[category] - 1
            if count < 1:
                result.pop(category, None)

        return {args for args in result if (nationID is None or args[0] == nationID) and (vehClass is None or args[1] == vehClass) and (level is None or args[2] == level)}

    def getTypeCompDescrsByLevel(self, level):
        return self.__typeCompDescrsByLevel[level]

    def getLevelByTypeCompDescr(self, compDescr):
        return self.__typeCompDescrToLevel[compDescr]

    def isVehicleExisting(self, name):
        return name in self.__ids

    def isVehicleExistingByType(self, nationID, vehicleTypeID):
        nation = self.getList(nationID)
        return nation is not None and nation.get(vehicleTypeID) is not None

    def isVehicleExistingByCD(self, vehTypeCompDescr):
        itemTypeID, nationID, innationID = parseIntCompactDescr(vehTypeCompDescr)
        return itemTypeID == items.ITEM_TYPES.vehicle and innationID in self.getList(nationID)

    def getIDsByVehName(self, name):
        for nation in nations.NAMES:
            fullName = b'%s:%s' % (nation, name)
            if fullName in self.__ids:
                return self.__ids[fullName]

        raise SoftException(b"unknown vehicle name '%s'" % name)
        return

    def getIDsByName(self, name):
        ids = self.__ids.get(name)
        if ids is None:
            raise SoftException(b"unknown vehicle type name '%s'" % name)
        return ids

    def __readVehicleList(self, nation, section, xmlPath):
        res = {}
        ids = {}
        nationID = nations.INDICES[nation]
        pricesDest = _g_prices
        if pricesDest is not None:
            if IS_CLIENT or IS_WEB or IS_COMMON_ENV:
                SELL_PRICE_FACTOR = 0.5
            else:
                from server_constants import SELL_PRICE_FACTOR
        for vname, vsection in section.items():
            if vname == b'xmlns:xmlref' or len(vsection) == 0:
                continue
            ctx = (
             None, xmlPath + b'/' + vname)
            if vname in ids:
                _xml.raiseWrongXml(ctx, b'', b'vehicle type name is not unique')
            innationID = _xml.readInt(ctx, vsection, b'id', 0, 65535)
            if innationID in res:
                _xml.raiseWrongXml(ctx, b'id', b'is not unique')
            compactDescr = makeIntCompactDescrByID(b'vehicle', nationID, innationID)
            ids[vname] = innationID
            item = vehicle_items.VehicleItem(ITEM_TYPES[b'vehicle'], innationID, (b'{}:{}').format(nation, vname), compactDescr, level=_readLevel(ctx, vsection))
            tags = _readTags(ctx, vsection, b'tags', b'vehicle')
            if len(tags & VEHICLE_CLASS_TAGS) != 1:
                _xml.raiseWrongXml(ctx, b'tags', b'vehicle class tag is missing or is multiple')
            if item.level in VEHICLE_LEVELS_EARN_CRYSTAL and b'earn_crystals' not in tags and len(set(tags) & MODES_WITHOUT_CRYSTAL_EARNINGS) == 0:
                _xml.raiseWrongXml(ctx, b'tags', b'vehicle %s with level %s does not have tag earn_crystals' % (vname, item.level))
            item.tags = tags
            res[innationID] = item
            if IS_CLIENT or IS_WEB or IS_BOT:
                item.i18n = shared_readers.readUserText(vsection)
            price = _xml.readPrice(ctx, vsection, b'price')
            if b'gold' in price:
                item.tags |= frozenset((b'premium',))
            if pricesDest is not None:
                pricesDest[b'itemPrices'][compactDescr] = price
                if vsection.readBool(b'notInShop', False):
                    pricesDest[b'notInShopItems'].add(compactDescr)
                if IS_RENTALS_ENABLED and vsection.readBool(b'cannotBeBought', False):
                    pricesDest[b'vehiclesNotToBuy'].add(compactDescr)
                sellPriceFactor = vsection.readFloat(b'sellPriceFactor', SELL_PRICE_FACTOR)
                if abs(sellPriceFactor - SELL_PRICE_FACTOR) > 0.001:
                    pricesDest[b'vehicleSellPriceFactors'][compactDescr] = sellPriceFactor
                if b'gold' in price and vsection.readBool(b'sellForGold', False):
                    pricesDest[b'vehiclesToSellForGold'].add(compactDescr)
                rentPrice = _xml.readRentPrice(ctx, vsection, b'rent') if IS_RENTALS_ENABLED else {}
                pricesDest[b'vehiclesRentPrices'][compactDescr] = rentPrice

        return res


def parseVehicleCompactDescr(compactDescr):
    header, vehicleTypeID = struct.unpack(b'2B', compactDescr[:2])
    if header & EXTENDED_VEHICLE_TYPE_ID_FLAG:
        vehicleTypeID += unpackByte(compactDescr[2]) << 8
    return (header >> 4 & 15, vehicleTypeID)


__ITEM_TYPE_VEHICLE = items.ITEM_TYPES.vehicle

def getVehicleTypeCompactDescr(compactDescr):
    nationID, vehicleTypeID = parseVehicleCompactDescr(compactDescr)
    return __ITEM_TYPE_VEHICLE + (nationID << 4) + (vehicleTypeID << 8)


def makeVehicleTypeCompDescrByName(name):
    nationID, innationID = g_list.getIDsByName(name)
    return makeIntCompactDescrByID(b'vehicle', nationID, innationID)


def makeVehicleTypeByName(name):
    nationID, innationID = g_list.getIDsByName(name)
    return g_cache.vehicle(nationID, innationID)


def getItemByCompactDescr(compactDescr):
    try:
        itemTypeID, nationID, compTypeID = parseIntCompactDescr(compactDescr)
        return _itemGetters[itemTypeID](nationID, compTypeID)
    except Exception:
        LOG_CURRENT_EXCEPTION()
        LOG_ERROR(b'(compact description to XML mismatch?)', compactDescr)
        raise

    return


def isItemWithCompactDescrExist(compactDescr):
    try:
        itemTypeID, nationID, compTypeID = parseIntCompactDescr(compactDescr)
        return _itemGetters[itemTypeID](nationID, compTypeID) is not None
    except Exception:
        return False

    return


def customizationLambda(cType, compTypeID):
    if IS_UE_EDITOR:
        cItems = g_cache.customization20().itemTypes[cType]
        if cItems is None or len(cItems) == 0:
            return
        return cItems[compTypeID]
    else:
        return g_cache.customization20().itemTypes[cType][compTypeID]
        return


_itemGetters = {(ITEM_TYPES.vehicle): (lambda nationID, compTypeID: g_cache.vehicle(nationID, compTypeID)), 
   (ITEM_TYPES.shell): (lambda nationID, compTypeID: g_cache.shells(nationID)[compTypeID]), 
   (ITEM_TYPES.equipment): (lambda nationID, compTypeID: g_cache.equipments()[compTypeID]), 
   (ITEM_TYPES.optionalDevice): (lambda nationID, compTypeID: g_cache.optionalDevices()[compTypeID]), 
   (ITEM_TYPES.vehicleGun): (lambda nationID, compTypeID: g_cache.guns(nationID)[compTypeID]), 
   (ITEM_TYPES.vehicleTurret): (lambda nationID, compTypeID: g_cache.turrets(nationID)[compTypeID]), 
   (ITEM_TYPES.vehicleEngine): (lambda nationID, compTypeID: g_cache.engines(nationID)[compTypeID]), 
   (ITEM_TYPES.vehicleRadio): (lambda nationID, compTypeID: g_cache.radios(nationID)[compTypeID]), 
   (ITEM_TYPES.vehicleChassis): (lambda nationID, compTypeID: g_cache.chassis(nationID)[compTypeID]), 
   (ITEM_TYPES.vehicleFuelTank): (lambda nationID, compTypeID: g_cache.fuelTanks(nationID)[compTypeID]), 
   (ITEM_TYPES.customizationItem): customizationLambda}
VEHICLE_ITEM_TYPES = list(_itemGetters)

def isVehicleTypeCompactDescr(vehDescr):
    cdType = type(vehDescr)
    if cdType is int or cdType is long:
        return True
    return False


def getEquipmentByName(name):
    eqID = g_cache.equipmentIDs()[name]
    return g_cache.equipments()[eqID]


def getVehicleType(compactDescr):
    if isVehicleTypeCompactDescr(compactDescr):
        nationID = compactDescr >> 4 & 15
        vehicleTypeID = compactDescr >> 8 & 65535
    else:
        nationID, vehicleTypeID = parseVehicleCompactDescr(compactDescr)
    return g_cache.vehicle(nationID, vehicleTypeID)


def getVehicleClass(compactDescr):
    return getVehicleClassFromVehicleType(getVehicleType(compactDescr))


def getVehicleClassFromVehicleType(vehicleType):
    for vehClass in VEHICLE_CLASS_TAGS & vehicleType.tags:
        return vehClass

    return


def makeCompactDescrBy(*args, **kwargs):
    if b'intCD' in kwargs:
        vehDescr = VehicleDescr(typeID=parseIntCompactDescr(kwargs[b'intCD'])[1:])
    else:
        vehDescr = VehicleDescr(**kwargs)
    return vehDescr.makeCompactDescr()


def stripCustomizationFromVehicleCompactDescr(compactDescr, stripEmblems=True, stripInscriptions=True, stripCamouflages=True, keepInfinite=False):
    type, components, optionalDevicesSlots, optionalDevices, enhancements, emblemSlots, emblems, inscriptions, camouflages = _splitVehicleCompactDescr(compactDescr)
    resEmblems = {}
    if stripEmblems and emblems:
        remainedEmblems = b''
        for pos in _RANGE_4:
            if emblemSlots & 1 << pos:
                emblemInfo = _unpackIDAndDuration(emblems[:6])
                if keepInfinite and emblemInfo[2] == 0:
                    remainedEmblems += emblems[:6]
                else:
                    resEmblems[pos] = emblemInfo
                    emblemSlots &= ~(1 << pos)
                emblems = emblems[6:]

        emblems = remainedEmblems
    resInscrs = {}
    if stripInscriptions and inscriptions:
        remainedInscriptions = b''
        for pos in _RANGE_4:
            if emblemSlots & 1 << pos + 4:
                inscrInfo = _unpackIDAndDuration(inscriptions[:6]) + (unpackByte(inscriptions[6]),)
                if keepInfinite and inscrInfo[2] == 0:
                    remainedInscriptions += inscriptions[:7]
                else:
                    resInscrs[pos] = inscrInfo
                    emblemSlots &= ~(1 << pos + 4)
                inscriptions = inscriptions[7:]

        inscriptions = remainedInscriptions
    resCams = {}
    if stripCamouflages and camouflages:
        remainedCamouflages = b''
        pos = 0
        while camouflages:
            camInfo = _unpackIDAndDuration(camouflages[:6])
            if keepInfinite and camInfo[2] == 0:
                remainedCamouflages += camouflages[:6]
            else:
                resCams[pos] = camInfo
            camouflages = camouflages[6:]
            pos += 1

        camouflages = remainedCamouflages
    compactDescr = _combineVehicleCompactDescr(type, components, optionalDevicesSlots, optionalDevices, enhancements, emblemSlots, emblems, inscriptions, camouflages)
    return (
     compactDescr, resEmblems, resInscrs, resCams)


def stripPrivateInfoFromVehicleCompactDescr(compactDescr):
    type, components, optionalDevicesSlots, optionalDevices, enhancements, emblemSlots, emblems, inscriptions, camouflages = _splitVehicleCompactDescr(compactDescr)
    optionalDevices = b''
    optionalDevicesSlots = 0
    enhancements = b''
    compactDescr = _combineVehicleCompactDescr(type, components, optionalDevicesSlots, optionalDevices, enhancements, emblemSlots, emblems, inscriptions, camouflages)
    return compactDescr


def stripOptionalDeviceFromVehicleCompactDescr(compactDescr):
    vehType, components, optionalDevicesSlots, optionalDevices, enhancements, emblemSlots, emblems, inscriptions, camouflages = _splitVehicleCompactDescr(compactDescr)
    optionalDevices = b''
    optionalDevicesSlots = 0
    return _combineVehicleCompactDescr(vehType, components, optionalDevicesSlots, optionalDevices, enhancements, emblemSlots, emblems, inscriptions, camouflages)


def isShellSuitableForGun(shellCompactDescr, gunDescr):
    itemTypeID, nationID, shellTypeID = parseIntCompactDescr(shellCompactDescr)
    shellID = (
     nationID, shellTypeID)
    for shotDescr in gunDescr.shots:
        if shotDescr.shell.id == shellID:
            return True

    return False


def getEmptyAmmoForGun(gunDescr):
    ammo = []
    for shot in gunDescr.shots:
        ammo.append(shot.shell.compactDescr)
        ammo.append(0)

    if not ammo:
        ammo.append(gunDescr.shots[0].shell.compactDescr)
        ammo.append(0)
    return ammo


def getDefaultAmmoForGun(gunDescr):
    return _getAmmoForGun(gunDescr, None)


def getUniformAmmoForGun(gunDescr):
    shots = len(gunDescr.shots)
    defaultPortion = 1.0 / shots if shots else 1.0
    return _getAmmoForGun(gunDescr, defaultPortion)


def getSpecificAmmoForGun(gunDescr, ammoProperties):
    ammo = []
    usedShellKinds = set()
    maxCount = gunDescr.maxAmmo
    for shot in gunDescr.shots:
        shellKind = shot.shell.kind
        percentage = ammoProperties.get(shellKind, None)
        if percentage is not None and shellKind not in usedShellKinds:
            ammo.append(shot.shell.compactDescr)
            ammo.append(int(percentage * maxCount))
            usedShellKinds.add(shellKind)

    return ammo


def calculateCarryingTriangles(carryingPoint):
    v = carryingPoint
    topLeft = Vector2(-v.x, v.y)
    bottomLeft = Vector2(-v.x, -v.y)
    topRight = Vector2(v.x, v.y)
    bottomRight = Vector2(v.x, -v.y)
    return (
     (
      (topLeft + bottomLeft) * 0.5, topRight, bottomRight),
     (
      (topRight + bottomRight) * 0.5, bottomLeft, topLeft))


def _getAmmoForGun(gunDescr, defaultPortion=None):
    ammo = []
    maxCount = gunDescr.maxAmmo
    clipSize = gunDescr.clip[0]
    if clipSize == maxCount:
        clipSize = 1
    currCount = 0
    for shot in gunDescr.shots:
        if defaultPortion is None:
            portion = shot.defaultPortion
        else:
            portion = defaultPortion
        shotCount = int(portion * maxCount / clipSize + 0.5) * clipSize
        if currCount + shotCount > maxCount:
            shotCount = maxCount - currCount
        currCount += shotCount
        ammo.append(shot.shell.compactDescr)
        ammo.append(shotCount)

    return ammo


def getBuiltinEqsForVehicle(vehType):
    builtins = vehType.builtins
    result = []
    for e in viewvalues(g_cache.equipments()):
        if e.name not in builtins:
            continue
        priority = float(b'inf')
        for tag in e.tags:
            if b'builtin_priority' not in tag:
                continue
            try:
                priority = int(tag.split(b'builtin_priority_')[1])
            except:
                pass

            break

        result.append((priority, e.compactDescr))

    result.sort()
    amountOfEquipment = vehType.supplySlots.getAmountForType(ITEM_TYPES.equipment, items.EQUIPMENT_TYPES.regular)
    result = result[:amountOfEquipment]
    return [equipTuple[1] for equipTuple in result]


def getUnlocksSources():
    res = {}
    for nationID in xrange(len(nations.NAMES)):
        for vehicleTypeID in g_list.getList(nationID):
            vehicleType = g_cache.vehicle(nationID, vehicleTypeID)
            for descr in vehicleType.unlocksDescrs:
                cd = descr[1]
                res.setdefault(cd, set()).add(vehicleType)

    return res


def getRolesActions():
    return g_cache.roles()


def getEquipmentIdsFromAmmoIter(ammo):
    for ammoIdx in xrange(0, len(ammo), 2):
        itemTypeID, _, equipmentID = parseIntCompactDescr(ammo[ammoIdx])
        if ammo[ammoIdx + 1] <= 0 or itemTypeID != ITEM_TYPES.equipment:
            continue
        yield equipmentID

    return


def getActionsByRole(role):
    actionsByRoles = getRolesActions()
    if role in actionsByRoles:
        return actionsByRoles[role]
    LOG_ERROR((b"actionsByRoles doesn't contain role={}").format(role))
    return ()


def isRestorable(vehTypeCD, gameParams):
    if vehTypeCD in gameParams[b'items'][b'vehiclesToSellForGold']:
        return False
    vehicleTags = getVehicleType(vehTypeCD).tags
    for tag in (b'unrecoverable', CollectorVehicleConsts.COLLECTOR_VEHICLES_TAG):
        if bool(tag in vehicleTags):
            return False

    isPremium = bool(b'premium' in vehicleTags)
    notInShop = bool(vehTypeCD in gameParams[b'items'][b'notInShopItems'])
    return isPremium or notInShop


def hasAnyOfTags(vehTypeCD, tags=()):
    vehicleType = getVehicleType(vehTypeCD)
    return bool(vehicleType.tags.intersection(tags))


def makeOutfitCD(outfitData):
    from items import customizations
    outfit = b''
    if outfitData:
        camouflages = None
        camouflageID = outfitData.get(b'camouflage')
        if camouflageID:
            camouflages = [customizations.CamouflageComponent(camouflageID, appliedTo=ApplyArea.HULL | ApplyArea.TURRET | ApplyArea.GUN)]
        decals = []
        decalID = outfitData.get(b'decal')
        if decalID:
            decals.append(customizations.DecalComponent(decalID, ApplyArea.ALL))
        paints = []
        paintID = outfitData.get(b'paint')
        if paintID:
            flag = ApplyArea.CHASSIS | ApplyArea.HULL | ApplyArea.TURRET
            paints.append(customizations.PaintComponent(paintID, flag))
        styleId = outfitData.get(b'style', 0)
        outfit = customizations.CustomizationOutfit(camouflages=camouflages, decals=decals, paints=paints, styleId=styleId).makeCompDescr()
    return outfit


def getShellByName(name, nation):
    nationID = nations.INDICES.get(nation, None)
    if nationID is None:
        return
    else:
        shellID = g_cache.shellIDs(nationID).get(name, None)
        return g_cache.shells(nationID).get(shellID, None)


def _readComponents(xmlPath, reader, nationID, itemTypeID):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    descrs = {}
    ids = {}
    for name in _xml.getSubsection(xmlCtx, section, b'ids').keys():
        name = intern(name)
        componentID = _xml.readInt(xmlCtx, section, b'ids/' + name, 0, 65535)
        if componentID in descrs:
            _xml.raiseWrongXml(xmlCtx, b'ids/' + name, b'name or ID is not unique')
        ids[name] = componentID
        descrs[componentID] = vehicle_items.createInstallableItem(itemTypeID, nationID, componentID, name)

    for name, subsection in _xml.getChildren(xmlCtx, section, b'shared'):
        ctx = (
         xmlCtx, b'shared')
        if name not in ids:
            _xml.raiseWrongXml(ctx, name, b'unknown name')
        descr = descrs[ids[name]]
        if descr.status != _ITEM_STATUS.EMPTY:
            _xml.raiseWrongXml(ctx, name, b'already defined')
        reader((ctx, name), subsection, descr)
        descr.status = _ITEM_STATUS.SHARED

    ResMgr.purge(xmlPath, True)
    return (
     descrs, ids)


def _readInstallableComponents(xmlCtx, section, subsectionName, nationID, reader, localReader, cachedDescrs, cachedIDs, unlocksDescrs, parentItem=None, **kwargs):
    res = []
    for sname, subsection in _xml.getChildren(xmlCtx, section, subsectionName):
        ctx = (
         xmlCtx, subsectionName + b'/' + sname)
        id = cachedIDs.get(sname)
        if id is None:
            _xml.raiseWrongXml(ctx, b'', b'unknown name')
        descr = cachedDescrs[id]
        if VehicleType.currentReadingVeh.mode == VEHICLE_MODE.DEFAULT:
            if subsection.asString == b'shared':
                if descr.status != _ITEM_STATUS.SHARED:
                    _xml.raiseWrongXml(ctx, sname, b'the component is not shared')
                res.append(localReader(ctx, subsection, descr, unlocksDescrs, parentItem, **kwargs))
            elif descr.status != _ITEM_STATUS.EMPTY:
                if IS_UE_EDITOR:
                    descr = descr.copy()
                else:
                    _xml.raiseWrongXml(ctx, b'', b'the component is already defined somewhere')
            descr.status = _ITEM_STATUS.LOCAL
            reader(ctx, subsection, descr, unlocksDescrs, parentItem, **kwargs)
            res.append(descr)
        elif descr.status == _ITEM_STATUS.SHARED:
            res.append(localReader(ctx, subsection, descr, unlocksDescrs, parentItem, **kwargs))
        else:
            modeDescr = descr.copy()
            modeDescr.status = _ITEM_STATUS.LOCAL
            reader(ctx, subsection, modeDescr, unlocksDescrs, parentItem, **kwargs)
            res.append(modeDescr)

    if not res:
        _xml.raiseWrongXml(xmlCtx, subsectionName, b'should be at least one subsection')
    return tuple(res)


def _writeInstallableComponents(components, section, subsectionName, writer, cachedIDs, sharedSections, materialData, parentName=None):
    cachedNames = {id: name for name, id in viewitems(cachedIDs)}
    if components is not None:
        for component in components:
            item_type_id, _, item_id_within_nation = parseIntCompactDescr(component.compactDescr)
            componentName = cachedNames[item_id_within_nation]
            sharedComponentSection = None
            if sharedSections:
                sharedSection = sharedSections[item_type_id]
                sharedComponentSection = sharedSection[(b'shared/{}').format(componentName)]
            mainComponentSection = section[(b'{}/{}').format(subsectionName, componentName)]
            if mainComponentSection is None:
                _xml.raiseWrongXml(None, subsectionName, b'can not open main components section')
                return
            sectionsToWrite = [
             mainComponentSection]
            if sharedComponentSection:
                sectionsToWrite.append(sharedComponentSection)
            combinedSection = CombinedDataSection(sectionsToWrite)
            writer(component, combinedSection, sharedSections, materialData, parentName)

    return


def _writeXPhysicsDetailed(xphysicsDetailed, xphysicsXml):
    for key, chassis in xphysicsDetailed[b'chassis'].items():
        chassisXml = xphysicsXml[(b'chassis/{}').format(key)]
        _xml.rewriteTupleOfFloats(chassisXml, b'axleSteeringLockAngles', chassis.get(b'axleSteeringLockAngles'), createNew=False)
        _xml.rewriteTupleOfFloats(chassisXml, b'axleSteeringAngles', chassis.get(b'axleSteeringAngles'), createNew=False)

    return


def _writeMultiGun(item, section):
    multiGunSection = section[b'multiGun']
    if multiGunSection is None or item.multiGun is None:
        return
    children = multiGunSection.values()
    index = 0
    for child in children:
        value = item.multiGun[index]
        _xml.rewriteVector3(child, b'position', value.position)
        _xml.rewriteVector3(child, b'shotOffset', value.shotOffset, (0.0, 0.0, 0.0))
        index += 1

    return


def _readLevel(xmlCtx, section):
    level = section.readInt(b'level', MIN_VEHICLE_LEVEL)
    if not MIN_VEHICLE_LEVEL <= level <= MAX_VEHICLE_LEVEL:
        _xml.raiseWrongSection(xmlCtx, b'level')
    return level


def _readIGRType(xmlCtx, section):
    igrType = section.readInt(b'igrType', IGR_TYPE.NONE)
    if not IGR_TYPE.NONE <= igrType <= IGR_TYPE.PREMIUM:
        _xml.raiseWrongSection(xmlCtx, b'igrType')
    return igrType


def _readNations(xmlCtx, section):
    if not section.has_key(b'nations'):
        return
    else:
        values = section.readString(b'nations').split()
        result = []
        for nation in values:
            index = nations.INDICES.get(nation, None)
            if index is None:
                _xml.raiseWrongSection(xmlCtx, b'nations')
            result.append(index)

        return tuple(result)


def _readFakeGearBox(xmlCtx, section):
    res = {b'fwdgears': {b'switchSpeed': (2, 5, 15), 
                     b'switchHysteresis': (1, 2, 3), 
                     b'lowRpm': (0.2, 0.2, 0.2), 
                     b'highRpm': (0.9, 0.9, 0.9)}, 
       b'bkwdgears': {b'switchSpeed': (2, 5, 15), 
                      b'switchHysteresis': (1, 2, 3), 
                      b'lowRpm': (0.2, 0.2, 0.2), 
                      b'highRpm': (0.9, 0.9, 0.9)}}
    fakeGeadBoxSection = section[b'fakegearbox']
    if fakeGeadBoxSection is None:
        return res
    else:
        fwdGears = {}
        fwdGearsSection = fakeGeadBoxSection[b'fwdgears']
        fwdGears[b'switchSpeed'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, fwdGearsSection, b'switchSpeed')
        fwdGears[b'switchHysteresis'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, fwdGearsSection, b'switchHysteresis')
        fwdGears[b'lowRpm'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, fwdGearsSection, b'lowRpm')
        fwdGears[b'highRpm'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, fwdGearsSection, b'highRpm')
        bkwdGears = {}
        bkwdGearsSection = fakeGeadBoxSection[b'bkwdgears']
        bkwdGears[b'switchSpeed'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, bkwdGearsSection, b'switchSpeed')
        bkwdGears[b'switchHysteresis'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, bkwdGearsSection, b'switchHysteresis')
        bkwdGears[b'lowRpm'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, bkwdGearsSection, b'lowRpm')
        bkwdGears[b'highRpm'] = _xml.readTupleOfNonNegativeFloats(xmlCtx, bkwdGearsSection, b'highRpm')
        if not len(fwdGears[b'switchSpeed']) == len(fwdGears[b'switchHysteresis']) == len(fwdGears[b'lowRpm']) == len(fwdGears[b'highRpm']):
            _xml.raiseWrongSection(xmlCtx, b'fwdGears')
        if not len(bkwdGears[b'switchSpeed']) == len(bkwdGears[b'switchHysteresis']) == len(bkwdGears[b'lowRpm']) == len(bkwdGears[b'highRpm']):
            _xml.raiseWrongSection(xmlCtx, b'bkwdGears')
        res[b'fwdgears'] = fwdGears
        res[b'bkwdgears'] = bkwdGears
        return res


def _readHull(xmlCtx, section):
    item = vehicle_items.Hull()
    item.hitTesterManager = _readHitTester(xmlCtx, section, b'hitTester')
    item.materials = _readArmor(xmlCtx, section, b'armor')
    item.weight = _xml.readNonNegativeFloat(xmlCtx, section, b'weight')
    item.maxHealth = _xml.readInt(xmlCtx, section, b'maxHealth', 1)
    item.ammoBayHealth = shared_readers.readDeviceHealthParams(xmlCtx, section, b'ammoBayHealth', False)
    item.customizableVehicleAreas = _readCustomizableAreas(xmlCtx, section, b'customization')
    if not IS_CLIENT and not IS_BOT and not IS_PROCESS_REPLAY:
        item.armorHomogenization = _xml.readPositiveFloat(xmlCtx, section, b'armorHomogenization')
    v = []
    for s in _xml.getSubsection(xmlCtx, section, b'turretPositions').values():
        v.append(_xml.readVector3((xmlCtx, b'turretPositions'), s, b''))

    if not v:
        _xml.raiseWrongSection(xmlCtx, b'turretPositions')
    item.turretPositions = tuple(v)
    numTurrets = len(item.turretPositions)
    item.turretPitches = __readTurretPitches(xmlCtx, section, numTurrets)
    if IS_CLIENT or IS_UE_EDITOR:
        item.turretHardPoints = __readTurretHardPoints(section, numTurrets)
    if numTurrets == 1:
        item.variantMatch = component_constants.DEFAULT_HULL_VARIANT_MATCH
    else:
        item.variantMatch = (None,) * (1 + numTurrets)
    if not section.has_key(b'fakeTurrets'):
        item.fakeTurrets = component_constants.DEFAULT_FAKE_TURRETS
    else:
        item.fakeTurrets = {b'lobby': (_readFakeTurretIndices(xmlCtx, section, b'fakeTurrets/lobby', numTurrets)), 
           b'battle': (_readFakeTurretIndices(xmlCtx, section, b'fakeTurrets/battle', numTurrets))}
    if IS_CLIENT or IS_UE_EDITOR or IS_BOT or IS_BASEAPP:
        if section.has_key(b'emblemSlots'):
            if not IS_BASEAPP:
                item.emblemSlots, item.slotsAnchors = shared_readers.readEmblemSlots(xmlCtx, section, b'emblemSlots')
        elif section.has_key(b'customizationSlots'):
            item.emblemSlots, item.slotsAnchors = shared_readers.readCustomizationSlots(xmlCtx, section, b'customizationSlots')
    if IS_CLIENT or IS_UE_EDITOR:
        item.modelsSets = shared_readers.readModelsSets(xmlCtx, section, b'models')
        item.models = item.modelsSets[b'default']
        item.swinging = shared_readers.readSwingingSettings(xmlCtx, section, g_cache)
        item.customEffects = (
         __readExhaustEffect(xmlCtx, section),)
        item.AODecals = _readAODecals(xmlCtx, section, b'AODecals')
        if section.has_key(b'camouflage'):
            item.camouflage = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=shared_components.DEFAULT_CAMOUFLAGE)
        if section.has_key(b'hangarShadowTexture'):
            item.hangarShadowTexture = _xml.readString(xmlCtx, section, b'hangarShadowTexture')
        else:
            item.hangarShadowTexture = b''
        item.burnoutAnimation = __readBurnoutAnimation(xmlCtx, section)
        item.prefabs = shared_readers.readPrefabsSets(section[b'prefabs'], (b'custom',))
    if IS_CLIENT or IS_UE_EDITOR or IS_WEB or IS_CELLAPP or IS_PROCESS_REPLAY:
        item.primaryArmor = _readPrimaryArmor(xmlCtx, section, b'primaryArmor', item.materials)
        if IS_UE_EDITOR and hasattr(item, b'editorData'):
            item.editorData.primaryArmors = _readPrimaryArmorKinds(xmlCtx, section, b'primaryArmor')
    item.slotPrefabs = shared_readers.readSlotPrefabs(section)
    item.objectSlots = shared_readers.readObjectSlots(xmlCtx, section)
    return item


def _writeHulls(hulls, section, materialData):
    section = _xml.getSubsection(None, section, b'hull')
    item = hulls[0]
    shared_writers.writeSlotPrefabs(item.slotPrefabs, section)
    shared_writers.writeObjectSlots(item.objectSlots, section)
    _writeHitTester(item.hitTesterManager, None, section, b'hitTester')
    _writeArmor(item.materials, section, materialData.get(b'hull', None) if materialData is not None else None, item.editorData.primaryArmors)
    _xml.rewriteFloat(section, b'weight', item.weight)
    _xml.rewriteInt(section, b'maxHealth', item.maxHealth)
    __writeTurretPitches(section, item.turretPitches)
    _writeCamouflageSettings(section, b'camouflage', item.camouflage)
    shared_writers.writeModelsSets(item.modelsSets, section[b'models'])
    shared_writers.writeSwingingSettings(item.swinging, section[b'swinging'])
    __writeExhaustEffect(item.customEffects[0], section)
    _xml.rewriteString(section, b'hangarShadowTexture', item.hangarShadowTexture, defaultValue=b'')
    slots = item.emblemSlots + item.slotsAnchors
    shared_writers.writeCustomizationSlots(slots, section, b'customizationSlots')
    _writeCustomizableAreas(item.customizableVehicleAreas, section)
    _writeHullVariants(hulls, section, materialData)
    return


def __readExhaustEffect(xmlCtx, section):
    effectDescriptors = {}
    effectDescriptors[b'default'] = CustomEffectsDescriptor.getDescriptor(section, g_cache._customEffects[b'exhaust'], xmlCtx, b'exhaust/pixie')
    tagsSection = _xml.getSubsection(xmlCtx, section, b'exhaust/tags', False)
    if tagsSection:
        for key in tagsSection.keys():
            effectDescriptors[key] = CustomEffectsDescriptor.getDescriptor(tagsSection, g_cache._customEffects[b'exhaust'], xmlCtx, key)

    effect = ExhaustEffectDescriptor(section, xmlCtx, effectDescriptors, b'exhaust/nodes')
    return effect


def __writeExhaustEffect(effect, section):
    effectDescriptors = effect._ExhaustEffectDescriptor__descriptors
    defaultEffect = effectDescriptors[b'default']
    effectName = None
    for name, customEffect in viewitems(g_cache._customEffects[b'exhaust']):
        if defaultEffect == customEffect:
            effectName = name
            break

    _xml.rewriteString(section, b'exhaust/pixie', effectName)
    return


BurnoutAnimationConfig = namedtuple(b'BurnoutAnimationConfig', (
 b'accumImpulseMag',
 b'dischargeImpulseMag',
 b'timeToAccumImpulse'))

def __readBurnoutAnimation(xmlCtx, section):
    burnoutSection = _xml.getSubsection(xmlCtx, section, b'burnoutAnimation', False)
    if burnoutSection is None:
        return
    else:
        accumImpulseMag = _xml.readFloat(xmlCtx, burnoutSection, b'accumulationImpulse')
        dischargeImpulseMag = _xml.readFloat(xmlCtx, burnoutSection, b'dischargeImpulse')
        timeToAccumImpulse = _xml.readFloat(xmlCtx, burnoutSection, b'timeToAccumulationImpulse')
        return BurnoutAnimationConfig(accumImpulseMag, dischargeImpulseMag, timeToAccumImpulse)


def __readTurretPitches(xmlCtx, section, numTurrets):
    if not section.has_key(b'turretPitches'):
        return [0.0] * numTurrets
    values = []
    for s in _xml.getSubsection(xmlCtx, section, b'turretPitches').values():
        values.append(radians(_xml.readFloat((xmlCtx, b'turretPitches'), s, b'')))

    result = tuple(values)
    return result


def __writeTurretPitches(section, pitches):
    if pitches:
        if len(pitches) == 1 and pitches[0] == 0:
            if section.has_key(b'turretPitches'):
                section.deleteSection(section[b'turretPitches'])
            return
    with _xml.ListRewriter(section, b'turretPitches/turret') as listRewriter:
        for pitch, child in zip(pitches, listRewriter):
            child.writeFloat(b'', degrees(pitch))

    return


def __readTurretHardPoints(section, numTurrets):
    thpSection = section[b'turretHardPoints']
    defaultJointHP = intern(b'HP_turretJoint')
    resultSeq = None
    if thpSection is None:
        resultSeq = (defaultJointHP for x in xrange(numTurrets))
    else:
        resultSeq = (intern(node.asString) for node in thpSection.values())
    result = tuple(resultSeq)
    return result


def _readHullVariants(xmlCtx, section, defHull, chassis, turrets):
    res = []
    numTurrets = len(defHull.turretPositions)
    for variantName, vSection in section.items():
        ctx = (
         xmlCtx, variantName)
        for prevVariant in res:
            if prevVariant.variantName == variantName:
                _xml.raiseWrongXml(xmlCtx, variantName, b'duplicate variant name')

        variantBase = defHull
        if vSection.has_key(b'base'):
            variantBaseName = vSection[b'base'].asString
            for prevVariant in res:
                if prevVariant.variantName == variantBaseName:
                    variantBase = prevVariant
                    break
            else:
                _xml.raiseWrongXml(ctx, b'base', b'unknown hull variant name "%s"' % variantBaseName)

        variant = variantBase.copy()
        variant.variantName = variantName
        variantMatch = variant.variantMatch = [None] * (1 + numTurrets)
        res.append(variant)
        isNonEmptyMatch = False
        for name in vSection.keys():
            if name == b'base':
                continue
            if name == b'models':
                variant.modelsSets = shared_readers.readModelsSets(ctx, vSection, b'models')
                variant.models = variant.modelsSets[b'default']
                continue
            if name == b'exhaust':
                if IS_CLIENT:
                    variant.customEffects = (
                     __readExhaustEffect(ctx, vSection),)
                continue
            if name == b'hitTester':
                variant.hitTesterManager = _readHitTester(ctx, vSection, b'hitTester')
                continue
            if name == b'armor':
                variant.materials = _readArmor(ctx, vSection, b'armor')
                continue
            if name == b'primaryArmor':
                if IS_CLIENT or IS_PROCESS_REPLAY:
                    variant.primaryArmor = _readPrimaryArmor(ctx, vSection, b'primaryArmor', variant.materials)
                if IS_UE_EDITOR and hasattr(variant, b'editorData'):
                    variant.editorData.primaryArmors = _readPrimaryArmorKinds(ctx, vSection, b'primaryArmor')
                continue
            if name == b'armorHomogenization':
                if not IS_CLIENT and not IS_BOT:
                    variant.armorHomogenization = _xml.readPositiveFloat(ctx, vSection, b'armorHomogenization')
                continue
            if name == b'weight':
                variant.weight = _xml.readNonNegativeFloat(ctx, vSection, b'weight')
                continue
            if name == b'maxHealth':
                variant.maxHealth = _xml.readInt(ctx, vSection, b'maxHealth', 1)
                continue
            if name == b'ammoBayHealth':
                variant.ammoBayHealth = shared_readers.readDeviceHealthParams(ctx, vSection, b'ammoBayHealth', False)
                continue
            if name == b'turretPositions':
                v = []
                for s in _xml.getSubsection(ctx, vSection, b'turretPositions').values():
                    v.append(_xml.readVector3((ctx, b'turretPositions'), s, b''))

                if len(v) != numTurrets:
                    _xml.raiseWrongSection(ctx, b'turretPositions')
                variant.turretPositions = tuple(v)
                continue
            if name == b'turretHardPoints':
                if IS_CLIENT or IS_UE_EDITOR:
                    variant.turretHardPoints = __readTurretHardPoints(vSection, numTurrets)
                continue
            if name == b'emblemSlots':
                if IS_CLIENT or IS_UE_EDITOR:
                    variant.emblemSlots, variant.slotsAnchors = shared_readers.readEmblemSlots(xmlCtx, vSection, b'emblemSlots')
                continue
            if name == b'customizationSlots':
                if IS_CLIENT or IS_UE_EDITOR or IS_BOT or IS_BASEAPP:
                    variant.emblemSlots, variant.slotsAnchors = shared_readers.readCustomizationSlots(xmlCtx, vSection, b'customizationSlots')
                continue
            if name == b'camouflage':
                if IS_CLIENT or IS_UE_EDITOR:
                    variant.camouflage = shared_readers.readCamouflage(xmlCtx, vSection, b'camouflage', default=shared_components.DEFAULT_CAMOUFLAGE)
                continue
            if name == b'chassis':
                if variantMatch[0] is not None:
                    _xml.raiseWrongXml(ctx, b'chassis', b'duplicate attr "chassis"')
                itemName = vSection[b'chassis'].asString
                for descr in chassis:
                    if descr.name == itemName:
                        variantMatch[0] = descr.id[1]
                        isNonEmptyMatch = True
                        break
                else:
                    _xml.raiseWrongXml(ctx, b'chassis', b'unknown chassis "%s"' % itemName)

                continue
            if name.startswith(b'turret'):
                turretIndex = -1
                try:
                    turretIndex = int(name[len(b'turret'):])
                except:
                    pass

                if not 0 <= turretIndex < numTurrets:
                    _xml.raiseWrongXml(ctx, name, b'unsupported parameter')
                if variantMatch[1 + turretIndex] is not None:
                    _xml.raiseWrongXml(ctx, name, b'duplicate attr "%s"' % name)
                itemName = vSection[name].asString
                for descr in turrets[turretIndex]:
                    if descr.name == itemName:
                        variantMatch[1 + turretIndex] = descr.id[1]
                        isNonEmptyMatch = True
                        break
                else:
                    _xml.raiseWrongXml(ctx, name, b'unknown turret "%s"' % itemName)

                continue
            _xml.raiseWrongXml(ctx, name, b'unsupported parameter')

        if not isNonEmptyMatch:
            _xml.raiseWrongXml(xmlCtx, variantName, b'no chassis or turret match specified')

    return tuple(res)


def _writeHullVariants(hulls, section, materialData):
    if len(hulls) < 2:
        if section.has_key(b'variants'):
            section.deleteSection(b'variants')
        return
    section = _xml.getSubsection(None, section, b'variants')
    defHull = hulls[0]
    for i in range(1, len(hulls)):
        hull = hulls[i]
        subsectionName = hull.variantName
        subsection = _xml.getSubsection(None, section, subsectionName)
        if hull.models == defHull.models:
            subsection.deleteSection(b'models')
        else:
            shared_writers.writeModelsSets(hull.modelsSets, subsection[b'models'])
            _writeArmor(hull.materials, subsection, materialData.get(subsectionName, None), hull.editorData.primaryArmors)
        if hull.hitTesterManager == defHull.hitTesterManager:
            subsection.deleteSection(b'hitTester')
        else:
            _writeHitTester(hull.hitTesterManager, None, subsection, b'hitTester')
        slots = hull.emblemSlots + hull.slotsAnchors
        defSlots = defHull.emblemSlots + defHull.slotsAnchors
        shared_writers.writeCustomizationSlots(slots if slots != defSlots else None, subsection, b'customizationSlots')
        _xml.rewriteFloat(subsection, b'weight', hull.weight, defHull.weight)

    return


def _readChassis(xmlCtx, section, item, unlocksDescrs=None, _=None, isWheeledVehicle=False):
    item.tags = _readTags(xmlCtx, section, b'tags', b'vehicleChassis')
    item.level = _readLevel(xmlCtx, section)
    item.hullPosition = _xml.readVector3(xmlCtx, section, b'hullPosition')
    item.topRightCarryingPoint = _xml.readPositiveVector2(xmlCtx, section, b'topRightCarryingPoint')
    item.navmeshGirth = _xml.readPositiveFloat(xmlCtx, section, b'navmeshGirth')
    item.minPlaneNormalY = cos(radians(_xml.readPositiveFloat(xmlCtx, section, b'maxClimbAngle')))
    item.weight = _xml.readPositiveFloat(xmlCtx, section, b'weight')
    item.specificFriction = component_constants.DEFAULT_SPECIFIC_FRICTION
    item.rotationSpeed = radians(_xml.readPositiveFloat(xmlCtx, section, b'rotationSpeed'))
    item.rotationIsAroundCenter = _xml.readBool(xmlCtx, section, b'rotationIsAroundCenter')
    item.customizableVehicleAreas = _readCustomizableAreas(xmlCtx, section, b'customization')
    if section.has_key(b'rotationSpeedLimit'):
        item.rotationSpeedLimit = radians(_xml.readPositiveFloat(xmlCtx, section, b'rotationSpeedLimit'))
    item.shotDispersionFactors = (
     _xml.readNonNegativeFloat(xmlCtx, section, b'shotDispersionFactors/vehicleMovement') / component_constants.KMH_TO_MS,
     degrees(_xml.readNonNegativeFloat(xmlCtx, section, b'shotDispersionFactors/vehicleRotation')))
    v = _xml.readVector3(xmlCtx, section, b'terrainResistance').tuple()
    if not 0.0 < v[0] <= v[1] <= v[2]:
        _xml.raiseWrongSection(xmlCtx, b'terrainResistance')
    item.terrainResistance = v
    if not IS_CLIENT and not IS_BOT:
        item.armorHomogenization = component_constants.DEFAULT_ARMOR_HOMOGENIZATION
        item.bulkHealthFactor = _xml.readPositiveFloat(xmlCtx, section, b'bulkHealthFactor')
    if not isWheeledVehicle:
        item.trackPairs = _readTrackPairs(xmlCtx, section)
        mainTrackPair = item.trackPairs[component_constants.MAIN_TRACK_PAIR_IDX]
        item.hitTesterManager = mainTrackPair.hitTesterManager
        item.materials = mainTrackPair.materials
        item.healthParams = mainTrackPair.healthParams
        if not (IS_BASEAPP or IS_WEB or IS_PROCESS_REPLAY or IS_COMMON_ENV):
            item.bboxManager = createBBoxManagerForModels([trackPair.hitTesterManager for trackPair in item.trackPairs])
    else:
        item.hitTesterManager = _readHitTester(xmlCtx, section, b'hitTester')
        item.materials = _readArmor(xmlCtx, section, b'armor', optional=True)
        item.healthParams = shared_readers.readDeviceHealthParams(xmlCtx, section)
        if not (IS_BASEAPP or IS_WEB or IS_PROCESS_REPLAY or IS_COMMON_ENV):
            htManager = item.hitTesterManager
            item.bboxManager = BoundingBoxManager(htManager.modelHitTester.bbox, htManager.crashedModelHitTester.bbox if htManager.crashedModelHitTester else None)
    if IS_CLIENT or IS_UE_EDITOR or IS_BOT or IS_BASEAPP:
        if section.has_key(b'emblemSlots'):
            if not IS_BASEAPP:
                item.emblemSlots, item.slotsAnchors = shared_readers.readEmblemSlots(xmlCtx, section, b'emblemSlots')
        elif section.has_key(b'customizationSlots'):
            item.emblemSlots, item.slotsAnchors = shared_readers.readCustomizationSlots(xmlCtx, section, b'customizationSlots')
    if section.has_key(b'wheelsHealth'):
        for name, subsection in section[b'wheelsHealth'].items():
            subctx = (
             (
              xmlCtx, b'wheelsHealth'), name)
            wheelNumber = int(name[-2:]) if name[-2:].isdigit() else int(name[-1])
            item.wheelHealthParams[wheelNumber] = shared_readers.readDeviceHealthParams(subctx, subsection)

    if IS_CLIENT or IS_UE_EDITOR or IS_CELLAPP or IS_WEB or IS_BOT:
        item.carryingTriangles = calculateCarryingTriangles(item.topRightCarryingPoint)
    if IS_CLIENT or IS_UE_EDITOR or IS_CELLAPP:
        drivingWheelNames = section.readString(b'drivingWheels').split()
        if len(drivingWheelNames) != 2:
            _xml.raiseWrongSection(xmlCtx, b'drivingWheels')
        if IS_UE_EDITOR and hasattr(item, b'editorData'):
            item.editorData.frontDrivingWheelName = drivingWheelNames[0]
            item.editorData.rearDrivingWheelName = drivingWheelNames[1]
        frontWheelSize = None
        rearWheelSize = None
        if (IS_CLIENT or IS_UE_EDITOR) and _xml.readBool(xmlCtx, section, b'wheels/generalWheels', False):
            item.generalWheelsAnimatorConfig = Vehicular.GeneralWheelsAnimatorConfig(section)
            radius = item.generalWheelsAnimatorConfig.getRadius(drivingWheelNames[0])
            frontWheelSize = radius * WHEEL_SIZE_COEF
            radius = item.generalWheelsAnimatorConfig.getRadius(drivingWheelNames[1])
            rearWheelSize = radius * WHEEL_SIZE_COEF
        if frontWheelSize is None or IS_UE_EDITOR:
            wheelGroups, wheels = chassis_readers.readWheelsAndGroups(xmlCtx, section)
            for wheel in wheels:
                if wheel.nodeName == drivingWheelNames[0]:
                    frontWheelSize = wheel.radius * WHEEL_SIZE_COEF
                if wheel.nodeName == drivingWheelNames[1]:
                    rearWheelSize = wheel.radius * WHEEL_SIZE_COEF
                if frontWheelSize is not None and rearWheelSize is not None:
                    break
            else:
                _xml.raiseWrongXml(xmlCtx, b'drivingWheels', b'unknown wheel name(s)')

            item.wheels = chassis_components.WheelsConfig(wheelGroups, wheels)
        if IS_CLIENT:
            _, wheels = chassis_readers.readWheelsAndGroups(xmlCtx, section)
            for wheel in wheels:
                if wheel.materials:
                    item.wheelsArmor[wheel.nodeName] = wheel.materials.values()[0]

        item.drivingWheelsSizes = (
         frontWheelSize, rearWheelSize)
    _readPriceForItem(xmlCtx, section, item.compactDescr)
    if IS_CLIENT or IS_WEB:
        item.i18n = shared_readers.readUserText(section)
    if IS_CLIENT or IS_UE_EDITOR:
        groundGroups, groundNodes, groundNodesActivePostmortem, lodSettings = chassis_readers.readGroundNodesAndGroups(xmlCtx, section, g_cache)
        trackNodes = chassis_readers.readTrackNodes(xmlCtx, section)
        if section.has_key(b'camouflage'):
            item.camouflage = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=shared_components.DEFAULT_CAMOUFLAGE)
        item.modelsSets = shared_readers.readModelsSets(xmlCtx, section, b'models')
        item.models = item.modelsSets[b'default']
        item.traces = chassis_readers.readTraces(xmlCtx, section, item.topRightCarryingPoint[0], g_cache)
        item.tracks = chassis_readers.readTrackBasicParams(xmlCtx, section, g_cache)
        item.groundNodes = shared_components.NodesAndGroups(nodes=groundNodes, groups=groundGroups, activePostmortem=groundNodesActivePostmortem, lodSettings=lodSettings)
        item.trackNodes = shared_components.NodesAndGroups(nodes=trackNodes, groups=component_constants.EMPTY_TUPLE, activePostmortem=False, lodSettings=None)
        item.trackSplineParams = chassis_readers.readTrackSplineParams(xmlCtx, section)
        item.splineDesc = chassis_readers.readSplineConfig(xmlCtx, section, g_cache)
        item.leveredSuspension = chassis_readers.readLeveredSuspension(xmlCtx, section, g_cache)
        item.hullAimingSound = sound_readers.readHullAimingSound(xmlCtx, section, g_cache)
        item.effects = {b'lodDist': (shared_readers.readLodDist(xmlCtx, section, b'effects/lodDist', g_cache))}
        sounds = sound_readers.readWWTripleSoundConfig(section)
        if sounds.isEmpty():
            raise SoftException(b'chassis sound tags are wrong for vehicle ' + item.name)
        item.sounds = sounds
        item.physicalTracks = physicalTracksDict = {}
        physicalTracksSection = section[b'physicalTracks']
        if physicalTracksSection is not None:
            physicalTracksDict[b'left'] = shared_readers.readBuilders(xmlCtx, physicalTracksSection, b'left', Vehicular.PhysicalTrackBuilder)
            physicalTracksDict[b'right'] = shared_readers.readBuilders(xmlCtx, physicalTracksSection, b'right', Vehicular.PhysicalTrackBuilder)
        item.chassisLodDistance = shared_readers.readLodDist(xmlCtx, section, b'wheels/lodDist', g_cache)
        item.customEffects = (
         CustomEffectsDescriptor.getDescriptor(section, g_cache._customEffects[b'slip'], xmlCtx, b'effects/mud'),)
        item.AODecals = _readAODecals(xmlCtx, section, b'AODecals')
        item.prefabs = shared_readers.readPrefabsSets(section[b'prefabs'], (b'custom',))
    item.slotPrefabs = shared_readers.readSlotPrefabs(section)
    item.objectSlots = shared_readers.readObjectSlots(xmlCtx, section)
    item.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, item.compactDescr)
    return


def _writeChassis(item, section, sharedSections, materialData, parentName):
    shared_writers.writeSlotPrefabs(item.slotPrefabs, section)
    shared_writers.writeObjectSlots(item.objectSlots, section)
    _writeHitTester(item.hitTesterManager, None, section, b'hitTester')
    _xml.rewriteFloat(section, b'weight', item.weight)
    _xml.rewriteFloat(section, b'rotationSpeed', degrees(item.rotationSpeed))
    chassisMatData = materialData.get(b'chassis', None) if materialData is not None else None
    if len(item.trackPairs) != 2:
        _writeArmor(item.materials, section, chassisMatData.get(item.name, None) if chassisMatData is not None else None)
    else:
        trackPairMatData = materialData.get(b'trackPair1', None) if materialData is not None else None
        trackPairsCount = 2
        paramSections = []
        for childSectionName, childSection in section.items():
            if childSectionName == b'trackPairParams':
                paramSections.append(childSection)
                if len(paramSections) == trackPairsCount:
                    break

        for _ in xrange(0, len(paramSections) - trackPairsCount):
            paramSections.append(section.createSection(b'trackPairParams'))

        _writeArmor(item.trackPairs[0].materials, paramSections[0], chassisMatData.get(item.name, None) if chassisMatData is not None else None)
        _writeArmor(item.trackPairs[1].materials, paramSections[1], trackPairMatData.get(item.name, None) if trackPairMatData is not None else None)
    slots = item.emblemSlots + item.slotsAnchors
    shared_writers.writeCustomizationSlots(slots, section, b'customizationSlots')
    _writeCustomizableAreas(item.customizableVehicleAreas, section)
    chassis_writers.writeWheelsAndGroups(item.wheels, section, materialData, item.name)
    shared_writers.writeModelsSets(item.modelsSets, section[b'models'])
    chassis_writers.writeTraces(item.traces, section, g_cache)
    chassis_writers.writeTrackBasicParams(item.tracks, section, g_cache)
    chassis_writers.writeTrackSplineParams(item.trackSplineParams, section)
    chassis_writers.writeTrackNodes(item.trackNodes.nodes, section)
    chassis_writers.writeGroundNodes(item.groundNodes.groups, section)
    sound_writers.writeHullAimingSound(item.hullAimingSound, section, g_cache)
    shared_writers.writeLodDist(item.effects[b'lodDist'], section, b'effects/lodDist', g_cache)
    chassis_writers.writeMudEffect(item.customEffects[0], g_cache, section, b'effects/mud')
    sound_writers.writeWWTripleSoundConfig(item.sounds, section)
    _writeAODecals(item.AODecals, section, b'AODecals')
    if IS_UE_EDITOR:
        editorData = item.editorData
        drivingWheelNames = (b' ').join((editorData.frontDrivingWheelName, editorData.rearDrivingWheelName))
        _xml.rewriteString(section, b'drivingWheels', drivingWheelNames)
    if item.generalWheelsAnimatorConfig:
        item.generalWheelsAnimatorConfig.save(section.getPrioritySection(b'wheels'))
    chassis_writers.writeSplineDesc(item.splineDesc, section, g_cache)
    physicalTracksSection = None
    if section.has_key(b'physicalTracks'):
        physicalTracksSection = section[b'physicalTracks']
    elif bool(item.physicalTracks):
        physicalTracksSection = section.createSection(b'physicalTracks')
        for _ in xrange(len(item.physicalTracks[b'left'])):
            physicalTracksSection.createSection(b'left')

        for _ in xrange(len(item.physicalTracks[b'right'])):
            physicalTracksSection.createSection(b'right')

    if physicalTracksSection is not None:
        if b'left' in item.physicalTracks:
            shared_writers.writeBuilders(item.physicalTracks[b'left'], physicalTracksSection, b'left')
        if b'right' in item.physicalTracks:
            shared_writers.writeBuilders(item.physicalTracks[b'right'], physicalTracksSection, b'right')
    leveredSuspensionSection = section[b'leveredSuspension']
    if leveredSuspensionSection is not None and item.leveredSuspension is not None:
        for leverSectionName, leverSection in leveredSuspensionSection.items():
            if leverSectionName != b'lever':
                continue
            leverName = _xml.readNonEmptyString(None, leverSection, b'trackNode')
            for lever in item.leveredSuspension.levers:
                if leverName == lever.trackNodeName:
                    limits = Vector2(degrees(lever.minAngle), degrees(lever.maxAngle))
                    _xml.rewriteVector2(leverSection, b'limits', limits)

    return


def _readChassisLocals(xmlCtx, section, sharedItem, unlocksDescrs, _=None):
    hasOverride = False
    cam = None
    if IS_CLIENT or IS_UE_EDITOR:
        sharedCam = sharedItem.camouflage
        cam = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=sharedCam)
        if cam != sharedCam:
            hasOverride = True
    if not section.has_key(b'unlocks'):
        unlocks = sharedItem.unlocks
    else:
        hasOverride = True
        unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, sharedItem.compactDescr)
    if not hasOverride:
        return sharedItem
    else:
        descr = sharedItem.copy()
        descr.unlocks = unlocks
        if IS_CLIENT or IS_UE_EDITOR:
            descr.camouflage = cam
        return descr


def _readTrackPairs(xmlCtx, section):
    if not section.has_key(b'trackPairParams'):
        return tuple([
         chassis_components.TrackPair(hitTesterManager=_readHitTester(xmlCtx, section, b'hitTester'), materials=_readArmor(xmlCtx, section, b'armor', index=component_constants.MAIN_TRACK_PAIR_IDX), healthParams=shared_readers.readDeviceHealthParams(xmlCtx, section), breakMode=_readTrackBreakMode(xmlCtx, section))])
    else:
        needHitTesters = not (IS_BASEAPP or IS_WEB)
        hitTesters = {}
        trackPairsParams = {}
        for sname, subsection in section.items():
            if needHitTesters and sname == b'hitTester':
                ctx = (
                 xmlCtx, sname)
                idx = subsection.readInt(b'trackPairIdx')
                hitTesters[idx] = _readHitTester(ctx, subsection, b'')
            if sname == b'trackPairParams':
                ctx = (
                 xmlCtx, sname)
                idx = subsection.readInt(b'trackPairIdx')
                trackPairsParams[idx] = {b'materials': (_readArmor(ctx, subsection, b'armor', index=idx)), 
                   b'healthParams': (shared_readers.readDeviceHealthParams(ctx, subsection)), 
                   b'breakMode': (_readTrackBreakMode(ctx, subsection))}

        trackPairsCount = len(trackPairsParams)
        if needHitTesters and len(hitTesters) != trackPairsCount:
            _xml.raiseWrongXml(xmlCtx, b'', b'Hit testers are provided not for all track pairs')
        trackPairs = [None] * trackPairsCount
        for idx, params in trackPairsParams.items():
            trackPairs[idx] = chassis_components.TrackPair(hitTesterManager=hitTesters[idx] if needHitTesters else None, materials=params[b'materials'], healthParams=params[b'healthParams'], breakMode=params[b'breakMode'])

        return tuple(trackPairs)


def _readTrackBreakMode(xmlCtx, section):
    defaultLabel = TrackBreakMode(TrackBreakMode.STOP).name
    breakModeLabel = intern(_xml.readStringWithDefaultValue(xmlCtx, section, b'breakMode', defaultLabel))
    return TrackBreakMode[breakModeLabel]


def _readExtrasProtection(vehType, xmlCtx, section):
    res = {b'protecting': {}, b'protected': {}}
    if not section.has_key(b'extrasProtection'):
        return res
    ctx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, b'extrasProtection')
    vehExtrasDict = vehType.extrasDict
    for protectingExtra, content in subsection.items():
        protectedExtra = content.asString
        if protectingExtra not in vehExtrasDict:
            _xml.raiseWrongXml(ctx, b'', (b"Non-existent extra name '{}'").format(protectingExtra))
        if protectedExtra not in vehExtrasDict:
            _xml.raiseWrongXml(ctx, b'', (b"Non-existent extra name '{}'").format(protectedExtra))
        res[b'protecting'][protectingExtra] = protectedExtra
        res[b'protected'][protectedExtra] = protectingExtra

    return res


def _readEngine(xmlCtx, section, item, unlocksDescrs=None, _=None):
    item.tags = _readTags(xmlCtx, section, b'tags', b'vehicleEngine')
    item.level = _readLevel(xmlCtx, section)
    item.power = _xml.readPositiveFloat(xmlCtx, section, b'power') * component_constants.HP_TO_WATTS
    item.weight = _xml.readPositiveFloat(xmlCtx, section, b'weight')
    item.fireStartingChance = _xml.readFraction(xmlCtx, section, b'fireStartingChance')
    item.minFireStartingDamage = g_cache.commonConfig[b'miscParams'][b'minFireStartingDamage']
    _readPriceForItem(xmlCtx, section, item.compactDescr)
    if IS_CLIENT or IS_WEB:
        item.i18n = shared_readers.readUserText(section)
    if IS_CLIENT or IS_UE_EDITOR:
        item.rpm_min = section.readInt(b'rpm_min', 1000)
        item.rpm_max = section.readInt(b'rpm_max', 2600)
        sounds = sound_readers.readWWTripleSoundConfig(section)
        if sounds.isEmpty():
            _xml.raiseWrongXml(xmlCtx, b'', b'chassis sound tags are wrong')
        item.sounds = sounds
    item.healthParams = shared_readers.readDeviceHealthParams(xmlCtx, section)
    item.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, item.compactDescr)
    return


def _readEngineLocal(xmlCtx, section, sharedItem, unlocksDescrs, _=None):
    hasOverride = False
    if section.has_key(b'unlocks'):
        hasOverride = True
        unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, sharedItem.compactDescr)
    else:
        unlocks = sharedItem.unlocks
    if section.has_key(b'power'):
        hasOverride = True
        power = _xml.readPositiveFloat(xmlCtx, section, b'power') * component_constants.HP_TO_WATTS
    else:
        power = sharedItem.power
    if not hasOverride:
        return sharedItem
    descr = sharedItem.copy()
    descr.unlocks = unlocks
    descr.power = power
    return descr


def _readFuelTank(xmlCtx, section, item, unlocksDescrs=None, _=None):
    item.tags = _readTags(xmlCtx, section, b'tags', b'vehicleEngine')
    item.level = _readLevel(xmlCtx, section)
    item.weight = _xml.readPositiveFloat(xmlCtx, section, b'weight')
    _readPriceForItem(xmlCtx, section, item.compactDescr)
    if IS_CLIENT or IS_WEB:
        item.i18n = shared_readers.readUserText(section)
    item.healthParams = shared_readers.readDeviceHealthParams(xmlCtx, section, b'', False)
    item.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, item.compactDescr)
    return


def _readRadio(xmlCtx, section, item, unlocksDescrs=None, _=None):
    item.tags = _readTags(xmlCtx, section, b'tags', b'vehicleEngine')
    item.level = _readLevel(xmlCtx, section)
    item.weight = _xml.readNonNegativeFloat(xmlCtx, section, b'weight')
    item.distance = _xml.readNonNegativeFloat(xmlCtx, section, b'distance')
    defaults = g_cache.commonConfig[b'miscParams'][b'radarDefaults']
    item.radarRadius = _xml.readNonNegativeFloat(xmlCtx, section, b'radarRadius', defaults[b'radarRadius'])
    item.radarCooldown = _xml.readNonNegativeFloat(xmlCtx, section, b'radarCooldown', defaults[b'radarCooldown'])
    _readPriceForItem(xmlCtx, section, item.compactDescr)
    if IS_CLIENT or IS_WEB:
        item.i18n = shared_readers.readUserText(section)
    item.healthParams = shared_readers.readDeviceHealthParams(xmlCtx, section)
    item.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, item.compactDescr)
    return


def _parseSectionList(ctx, section, listItemParser, listSubSectionTag=None):
    if listSubSectionTag:
        subsection = _xml.getSubsection(ctx, section, listSubSectionTag)
        ctx = (ctx, listSubSectionTag)
    else:
        subsection = section
    res = {}
    for name, sec in subsection.items():
        named_ctx = (
         ctx, name)
        res[intern(name)] = listItemParser(named_ctx, sec)

    return res


def _parseFloatList(ctx, sec, floatList):
    return dict((pn, _xml.readFloat(ctx, sec, pn)) for pn in floatList)


def _tryParseFloatList(ctx, sec, nameList):
    return dict((pn, _xml.readFloat(ctx, sec, pn)) for pn in nameList if sec.has_key(pn))


def _parseFloatArrList(ctx, sec, floatArrList):
    return dict((pn, _xml.readTupleOfFloats(ctx, sec, pn, sz)) for pn, sz in floatArrList)


def _xphysicsParseEngine(ctx, sec):
    res = {}
    floatParamsCommon = (b'startRPM',)
    res.update(_parseFloatList(ctx, sec, floatParamsCommon))
    floatParamsDetailed = (b'engineInertia', b'idleRPM', b'idleChoker')
    res.update(_parseFloatList(ctx, sec, floatParamsDetailed))
    floatArrParamsDetailed = (
     (b'engineLoses', 2),
     (b'engineTorque', 8))
    res.update(_parseFloatArrList(ctx, sec, floatArrParamsDetailed))
    res[b'engineTorque'] = tuple(zip(res[b'engineTorque'][0::2], res[b'engineTorque'][1::2]))
    res[b'powerFactor'] = sec.readFloat(b'powerFactor', 1.0)
    res[b'rotationFactor'] = sec.readFloat(b'rotationFactor', 1.0)
    res[b'smplEnginePower'] = sec.readFloat(b'smplEnginePower', 600.0)
    res[b'smplFwMaxSpeed'] = component_constants.KMH_TO_MS * sec.readFloat(b'smplFwMaxSpeed', 55.0)
    res[b'smplBkMaxSpeed'] = component_constants.KMH_TO_MS * sec.readFloat(b'smplBkMaxSpeed', 15.0)
    return res


def _xphysicsReadSwingCompensator(ctx, sec):
    floatParams = (b'collisionExtend', b'stiffnesFactor0', b'stiffnesFactor1', b'dampingFactor', b'maxPitchDeviation', b'maxRollDeviation', b'restitution')
    res = _tryParseFloatList(ctx, sec, floatParams)
    if sec.has_key(b'enable'):
        res[b'enable'] = sec.readBool(b'enable', b'true')
    if sec.has_key(b'stabilisationCenter'):
        res[b'stabilisationCenter'] = _xml.readTupleOfFloats(ctx, sec, b'stabilisationCenter')
    return res


def _xphysicsParseGround(ctx, sec):
    floatParams = (b'dirtCumulationRate', b'dirtReleaseRate', b'dirtSideVelocity', b'maxDirt', b'sideFriction', b'fwdFriction', b'rollingFriction')
    res = _parseFloatList(ctx, sec, floatParams)
    res[b'dirtSideVelocity'] *= component_constants.KMH_TO_MS
    res[b'dirtCumulationRate'] *= component_constants.KMH_TO_MS
    res[b'hbComSideFriction'] = sec.readFloat(b'hbComSideFriction', 0.0)
    res[b'hbSideFrictionAddition'] = sec.readFloat(b'hbSideFrictionAddition', 0.0)
    res[b'rotationFactor'] = sec.readFloat(b'rotationFactor', 1.0)
    return res


def _xphysicsParseChassis(type, ctx, sec):
    res = {}
    res[b'grounds'] = _parseSectionList(ctx, sec, _xphysicsParseGround, b'grounds')
    floatParamsCommon = (b'chassisMassFraction', b'hullCOMShiftY', b'wheelRadius', b'bodyHeight', b'clearance', b'wheelStroke', b'stiffness0', b'stiffness1', b'damping', b'movementRevertSpeed', b'comSideFriction', b'wheelInertiaFactor', b'rotationBrake', b'brake', b'angVelocityFactor')
    res.update(_parseFloatList(ctx, sec, floatParamsCommon))
    res[b'movementRevertSpeed'] *= component_constants.KMH_TO_MS
    res[b'isRotationAroundCenter'] = sec.readBool(b'isRotationAroundCenter', False)
    res[b'comFrictionYOffs'] = sec.readFloat(b'comFrictionYOffs', 0.7)
    res[b'rotFritionFactor'] = sec.readFloat(b'rotFritionFactor', 0.0)
    res[b'wheelSinkageResistFactor'] = sec.readFloat(b'wheelSinkageResistFactor', 0.0)
    res[b'gimletGoalWOnSpot'] = sec.readFloat(b'gimletGoalWOnSpot', sec.readFloat(b'wPushedRot', 0.0))
    res[b'gimletGoalWOnMove'] = sec.readFloat(b'gimletGoalWOnMove', sec.readFloat(b'wPushedDiag', 0.0))
    res[b'wPushedRot'] = res[b'gimletGoalWOnSpot']
    res[b'wPushedDiag'] = res[b'gimletGoalWOnMove']
    res[b'pushStop'] = sec.readFloat(b'pushStop', 0.0)
    res[b'gimletPushOnSpotInit'] = sec.readFloat(b'gimletPushOnSpotInit', sec.readFloat(b'pushRot', 0.0))
    res[b'gimletPushOnSpotFinal'] = sec.readFloat(b'gimletPushOnSpotFinal', sec.readFloat(b'pushDiag', 0.0))
    res[b'gimletPushOnMoveInit'] = sec.readFloat(b'gimletPushOnMoveInit', res[b'gimletPushOnSpotInit'])
    res[b'gimletPushOnMoveFinal'] = sec.readFloat(b'gimletPushOnMoveFinal', res[b'gimletPushOnSpotFinal'])
    res[b'gimletCOMOffset'] = sec.readVector3(b'gimletCOMOffset', component_constants.ZERO_VECTOR3)
    gimletParams = (b'gimletVelScaleMin', b'gimletVelScaleMax', b'pushRotOnSpotFixedPeriod', b'pushRotOnMoveFixedPeriod', b'pushRotOnSpotGrowPeriod', b'pushRotOnMoveGrowPeriod')
    res.update(_tryParseFloatList(ctx, sec, gimletParams))
    res[b'chsDmgMultiplier'] = sec.readFloat(b'chsDmgMultiplier', 1.0)
    if sec.has_key(b'hullDamageByStaticFactor'):
        res[b'hullDamageByStaticFactor'] = _xml.readPositiveFloat(ctx, sec, b'hullDamageByStaticFactor')
    res[b'wPushedMediumFactor'] = sec.readFloat(b'wPushedMediumFactor', 1.0)
    res[b'wPushedSoftFactor'] = sec.readFloat(b'wPushedSoftFactor', 1.0)
    res[b'sideFrictionConstantRatio'] = sec.readFloat(b'sideFrictionConstantRatio', 0.0)
    res[b'angVelocityFactor0'] = sec.readFloat(b'angVelocityFactor0', 1.0)
    axleCount = sec.readInt(b'axleCount', 5)
    res[b'axleCount'] = axleCount
    floatArrParamsCommon = (
     (b'hullCOM', 3),
     (
      b'roadWheelPositions', axleCount),
     (
      b'stiffnessFactors', axleCount),
     (b'hullInertiaFactors', 3))
    res.update(_parseFloatArrList(ctx, sec, floatArrParamsCommon))
    floatParamsDetailed = (b'centerRotationFwdSpeed', b'rotationByLockChoker', b'fwLagRatio', b'bkLagRatio')
    res.update(_parseFloatList(ctx, sec, floatParamsDetailed))
    res[b'centerRotationFwdSpeed'] *= component_constants.KMH_TO_MS
    res[b'brokenTrackLosses'] = _readBrokenTrackLosses(ctx, sec)
    res[b'railCOMOffset'] = sec.readVector3(b'railCOMOffset', component_constants.ZERO_VECTOR3)
    return res


def _xphysicsParseWheeledChassis(type, ctx, sec):
    res = _xphysicsParseChassis(type, ctx, sec)
    res[b'isWheeledOnSpotRotation'] = _xml.readBool(ctx, sec, b'isWheeledOnSpotRotation', False)
    res[b'isWheeledOnMoveRotation'] = _xml.readBool(ctx, sec, b'isWheeledOnMoveRotation', False)
    axleCount = sec.readInt(b'axleCount', 5)
    res[b'axleSteeringAngles'], res[b'axleSteeringLockAngles'] = _readSteeringAngles(ctx, sec, axleCount, not res[b'isWheeledOnSpotRotation'])
    floatArrParams = (
     (
      b'axleSteeringSpeed', axleCount),
     (
      b'fwdFrictionOnAxisModifiers', axleCount),
     (
      b'sideFrictionOnAxisModifiers', axleCount),
     (
      b'sideFrictionConstantRatioOnAxis', axleCount),
     (
      b'sinkageResistOnAxis', axleCount))
    res.update(_parseFloatArrList(ctx, sec, floatArrParams))
    res[b'axleIsLeading'] = _xml.readTupleOfBools(ctx, sec, b'axleIsLeading', axleCount)
    res[b'axleCanBeRised'], res[b'wheelRiseHeight'], res[b'wheelRiseSpeed'] = _readAxleRiseParams(ctx, sec, axleCount, type.hasSiegeMode)
    floatParams = (b'handbrakeBrakeForce', b'noSignalBrakeForce', b'afterDeathBrakeForce', b'afterDeathMinSpeedForImpulse', b'afterDeathImpulse', b'slowTurnChocker', b'airPitchReduction', b'wheelToHullRollTransmission', b'steeringSpeedInTurnMultiplier')
    res.update(_parseFloatList(ctx, sec, floatParams))
    res[b'afterDeathMinSpeedForImpulse'] *= component_constants.KMH_TO_MS
    res[b'jumpingFactor'] = _xml.readFloat(ctx, sec, b'jumpingFactor', 0.0)
    res[b'jumpingMinForce'] = _xml.readFloat(ctx, sec, b'jumpingMinForce', 0.0)
    res[b'brokenWheelRollingFrictionModifier'] = _xml.readFloat(ctx, sec, b'brokenWheelRollingFrictionModifier', 1.0)
    res[b'brokenWheelPowerLoss'], res[b'brokenWheelSpeedLoss'], res[b'brokenWheelRotationSpeedLoss'] = _readBrokenWheelLosses(ctx, sec, res[b'axleIsLeading'], res[b'axleCanBeRised'], res[b'wheelRiseHeight'])
    res[b'burnout'] = _readBurnout(ctx, sec)
    res[b'enableRail'] = _xml.readBool(ctx, sec, b'enableRail')
    return res


def _readXPhysicsMode(xmlCtx, sec, subsectionName, type):
    subsec = sec[subsectionName]
    if subsec is None:
        return
    else:
        ctx = (
         xmlCtx, subsectionName)
        res = {}
        res[b'gravityFactor'] = subsec.readFloat(b'gravityFactor', 1.0)
        res[b'vehiclePhysicsType'] = subsec.readInt(b'vehiclePhysicsType', VEHICLE_PHYSICS_TYPE.TANK)
        res[b'fakegearbox'] = _readFakeGearBox(ctx, subsec)
        res[b'engines'] = _parseSectionList(ctx, subsec, _xphysicsParseEngine, b'engines')
        if subsec.has_key(b'swingCompensator'):
            res[b'swingCompensator'] = _xphysicsReadSwingCompensator(ctx, subsec[b'swingCompensator'])
        isTank = res[b'vehiclePhysicsType'] == VEHICLE_PHYSICS_TYPE.TANK
        readChassisFunc = _xphysicsParseChassis if isTank else _xphysicsParseWheeledChassis
        res[b'chassis'] = _parseSectionList(ctx, subsec, partial(readChassisFunc, type), b'chassis')
        return res


def _readXPhysics(xmlCtx, section, subsectionName, type):
    xsec = section[subsectionName]
    if xsec is None:
        return
    else:
        ctx = (
         xmlCtx, subsectionName)
        res = {}
        res[b'mode'] = _xml.readInt(ctx, xsec, b'mode', 1)
        res[b'detailed'] = _readXPhysicsMode(ctx, xsec, b'detailed', type)
        return res


def _xphysicsParseGroundClient(ctx, sec):
    res = {}
    res[b'rollingFriction'] = sec.readFloat(b'rollingFriction', float(b'nan'))
    if isnan(res[b'rollingFriction']):
        _xml.raiseWrongXml(ctx, b'', b"'rollingFriction' is missing")
    return res


def _xphysicsParseChassisClient(ctx, sec):
    res = {}
    res[b'grounds'] = _parseSectionList(ctx, sec, _xphysicsParseGroundClient, b'grounds')
    return res


def _xphysicsParseWheeledChassisClient(ctx, sec):
    res = _xphysicsParseChassisClient(ctx, sec)
    axleCount = sec.readInt(b'axleCount', 5)
    res[b'isWheeledOnSpotRotation'] = _xml.readBool(ctx, sec, b'isWheeledOnSpotRotation', False)
    res[b'isWheeledOnMoveRotation'] = _xml.readBool(ctx, sec, b'isWheeledOnMoveRotation', False)
    res[b'axleSteeringAngles'], res[b'axleSteeringLockAngles'] = _readSteeringAngles(ctx, sec, axleCount, not res[b'isWheeledOnSpotRotation'])
    res[b'wheelRiseSpeed'] = _xml.readFloat(ctx, sec, b'wheelRiseSpeed', 0.0)
    res[b'burnout'] = {} if sec.has_key(b'burnout') else None
    return res


def _xphysicsParseEngineClient(ctx, sec):
    res = {}
    res[b'smplEnginePower'] = sec.readFloat(b'smplEnginePower', float(b'nan'))
    res[b'smplFwMaxSpeed'] = sec.readFloat(b'smplFwMaxSpeed', float(b'nan'))
    res[b'smplBkMaxSpeed'] = sec.readFloat(b'smplBkMaxSpeed', float(b'nan'))
    if isnan(res[b'smplEnginePower']):
        _xml.raiseWrongXml(ctx, b'', b"'smplEnginePower' is missing")
    return res


def _readXPhysicsClient(xmlCtx, section, subsectionName, type):
    xsec = section[subsectionName]
    if xsec is None:
        _xml.raiseWrongXml(xmlCtx, b'', b"subsection '%s' is missing" % subsectionName)
    ctx = (xmlCtx, subsectionName)
    res = {}
    res[b'engines'] = _parseSectionList(ctx, xsec, _xphysicsParseEngineClient, b'detailed/engines')
    if type.isWheeledVehicle:
        readFunc = _xphysicsParseWheeledChassisClient
    else:
        readFunc = _xphysicsParseChassisClient
    res[b'chassis'] = _parseSectionList(ctx, xsec, readFunc, b'detailed/chassis')
    return res


def _readXPhysicsEditor(xmlCtx, section, subsectionName, type):
    xsec = section[subsectionName]
    if xsec is None:
        return
    else:
        ctx = (
         xmlCtx, subsectionName)
        res = {}
        res[b'mode'] = _xml.readInt(ctx, xsec, b'mode', 1)
        res[b'detailed'] = _readXPhysicsMode(ctx, xsec, b'detailed', type)
        res[b'engines'] = _parseSectionList(ctx, xsec, _xphysicsParseEngineClient, b'detailed/engines')
        if type.isWheeledVehicle:
            readFunc = _xphysicsParseWheeledChassisClient
        else:
            readFunc = _xphysicsParseChassisClient
        res[b'chassis'] = _parseSectionList(ctx, xsec, readFunc, b'detailed/chassis')
        if type.isWheeledVehicle and hasattr(type, b'editorData'):
            for i, name in enumerate(res[b'chassis']):
                chassis = res[b'chassis'][name]
                editorData = type.chassis[i].editorData
                editorData.axleCount = len(chassis[b'axleSteeringAngles'])
                editorData.axleSteeringAngles = list(chassis[b'axleSteeringAngles'])
                editorData.axleSteeringLockAngles = list(chassis[b'axleSteeringLockAngles'])

        return res


def _readTurret(xmlCtx, section, item, unlocksDescrs=None, _=None):
    item.tags = _readTags(xmlCtx, section, b'tags', b'vehicleTurret')
    item.level = _readLevel(xmlCtx, section)
    item.hitTesterManager = _readHitTester(xmlCtx, section, b'hitTester')
    item.gunPosition = _xml.readVector3(xmlCtx, section, b'gunPosition')
    item.gunJointPitch = radians(_xml.readFloat(xmlCtx, section, b'gunJointPitch', 0.0))
    item.customizableVehicleAreas = _readCustomizableAreas(xmlCtx, section, b'customization')
    if section.has_key(b'multiGun'):
        item.multiGun = _readMultiGun(xmlCtx, section, b'multiGun')
    item.materials = _readArmor(xmlCtx, section, b'armor')
    item.weight = _xml.readNonNegativeFloat(xmlCtx, section, b'weight')
    item.healthParams = shared_components.DeviceHealth(_xml.readInt(xmlCtx, section, b'maxHealth', 1))
    item.rotationSpeed = cachedFloat(radians(_xml.readNonNegativeFloat(xmlCtx, section, b'rotationSpeed')))
    item.turretRotatorHealth = shared_readers.readDeviceHealthParams(xmlCtx, section, b'turretRotatorHealth')
    item.surveyingDeviceHealth = shared_readers.readDeviceHealthParams(xmlCtx, section, b'surveyingDeviceHealth')
    if not IS_CLIENT and not IS_BOT and not IS_PROCESS_REPLAY:
        item.armorHomogenization = _xml.readPositiveFloat(xmlCtx, section, b'armorHomogenization')
    if section.has_key(b'invisibilityFactor'):
        item.invisibilityFactor = _xml.readNonNegativeFloat(xmlCtx, section, b'invisibilityFactor')
    else:
        item.invisibilityFactor = component_constants.DEFAULT_INVISIBILITY_FACTOR
    _readPriceForItem(xmlCtx, section, item.compactDescr)
    item.showEmblemsOnGun = section.readBool(b'showEmblemsOnGun', False)
    if IS_CLIENT or IS_WEB:
        item.i18n = shared_readers.readUserText(section)
    if IS_CLIENT or IS_UE_EDITOR or IS_WEB or IS_CELLAPP or IS_PROCESS_REPLAY:
        item.primaryArmor = _readPrimaryArmor(xmlCtx, section, b'primaryArmor', item.materials)
        if IS_UE_EDITOR and hasattr(item, b'editorData'):
            item.editorData.primaryArmors = _readPrimaryArmorKinds(xmlCtx, section, b'primaryArmor')
    if IS_CLIENT or IS_UE_EDITOR or IS_BOT or IS_BASEAPP:
        if section.has_key(b'emblemSlots'):
            if not IS_BASEAPP:
                item.emblemSlots, item.slotsAnchors = shared_readers.readEmblemSlots(xmlCtx, section, b'emblemSlots')
        elif section.has_key(b'customizationSlots'):
            item.emblemSlots, item.slotsAnchors = shared_readers.readCustomizationSlots(xmlCtx, section, b'customizationSlots')
    if IS_CLIENT or IS_UE_EDITOR:
        item.ceilless = section.readBool(b'ceilless', False)
        item.modelsSets = shared_readers.readModelsSets(xmlCtx, section, b'models')
        item.models = item.modelsSets[b'default']
        if section.has_key(b'camouflage'):
            item.camouflage = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=shared_components.DEFAULT_CAMOUFLAGE)
        item.turretRotatorSoundManual = _xml.readString(xmlCtx, section, b'wwturretRotatorSoundManual')
        item.AODecals = _readAODecals(xmlCtx, section, b'AODecals')
        commonConfig = g_cache.commonConfig
        item.turretDetachmentEffects = _readTurretDetachmentEffects(xmlCtx, section, b'turretDetachmentEffects', commonConfig[b'defaultTurretDetachmentEffects'])
        item.prefabs = shared_readers.readPrefabsSets(section[b'prefabs'], (b'custom',))
    if IS_CELLAPP or IS_UE_EDITOR:
        item.physicsShape = _xml.readTupleOfFloats(xmlCtx, section, b'physicsShape', defaultValue=[])
    v = _xml.readNonNegativeFloat(xmlCtx, section, b'circularVisionRadius')
    item.circularVisionRadius = v
    nationID = parseIntCompactDescr(item.compactDescr)[1]
    item.guns = _readInstallableComponents(xmlCtx, section, b'guns', nationID, _readGun, _readGunLocals, g_cache.guns(nationID), g_cache.gunIDs(nationID), unlocksDescrs, item.compactDescr, multiGun=item.multiGun)
    if section.has_key(b'secondaryGuns'):
        item.secondaryGuns = _readInstallableComponents(xmlCtx, section, b'secondaryGuns', nationID, _readGun, _readGunLocals, g_cache.guns(nationID), g_cache.gunIDs(nationID), unlocksDescrs, item.compactDescr, multiGun=item.multiGun)
        if IS_UE_EDITOR:
            for gunItem in item.secondaryGuns:
                gunItem.editorData.isSecondaryGun = True

    if not item.multiGun:
        pass
    item.slotPrefabs = shared_readers.readSlotPrefabs(section)
    item.objectSlots = shared_readers.readObjectSlots(xmlCtx, section)
    item.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, item.compactDescr)
    return


def _writeTurret(item, section, sharedSections, materialData, parentName):
    shared_writers.writeSlotPrefabs(item.slotPrefabs, section)
    shared_writers.writeObjectSlots(item.objectSlots, section)
    _xml.rewriteFloat(section, b'weight', item.weight)
    _xml.rewriteFloat(section, b'gunJointPitch', degrees(item.gunJointPitch), 0.0)
    _xml.rewriteBool(section, b'showEmblemsOnGun', item.showEmblemsOnGun, defaultValue=False)
    _writeHitTester(item.hitTesterManager, None, section, b'hitTester')
    _xml.rewriteString(section, b'wwturretRotatorSoundManual', item.turretRotatorSoundManual)
    _writeCamouflageSettings(section, b'camouflage', item.camouflage)
    turretMatData = materialData.get(b'turret', None) if materialData is not None else None
    turretMatData = turretMatData.get(item.name, None) if turretMatData is not None else None
    _writeArmor(item.materials, section, turretMatData, item.editorData.primaryArmors)
    slots = item.emblemSlots + item.slotsAnchors
    shared_writers.writeCustomizationSlots(slots, section, b'customizationSlots')
    _writeCustomizableAreas(item.customizableVehicleAreas, section)
    shared_writers.writeModelsSets(item.modelsSets, section[b'models'])
    _xml.rewriteTupleOfFloats(section, b'physicsShape', item.physicsShape, [])
    nationID = parseIntCompactDescr(item.compactDescr)[1]
    _writeInstallableComponents(item.guns, section, b'guns', _writeGun, g_cache.gunIDs(nationID), sharedSections, materialData=materialData.get(b'gun', None), parentName=item.name)
    _writeInstallableComponents(item.secondaryGuns, section, b'secondaryGuns', _writeGun, g_cache.gunIDs(nationID), sharedSections, materialData=materialData.get(b'secondaryGun', None), parentName=item.name)
    _writeMultiGun(item, section)
    return


def _readTurretLocals(xmlCtx, section, sharedItem, unlocksDescrs, _=None):
    hasOverride = False
    cam = None
    nationID = sharedItem.id[0]
    if not section.has_key(b'guns'):
        guns = sharedItem.guns
    else:
        hasOverride = True
        guns = _readInstallableComponents(xmlCtx, section, b'guns', nationID, _readGun, _readGunLocals, g_cache.guns(nationID), g_cache.gunIDs(nationID), unlocksDescrs, sharedItem.compactDescr, multiGun=sharedItem.multiGun)
    if not section.has_key(b'secondaryGuns'):
        secondaryGuns = sharedItem.secondaryGuns
    else:
        hasOverride = True
        secondaryGuns = _readInstallableComponents(xmlCtx, section, b'secondaryGuns', nationID, _readGun, _readGunLocals, g_cache.guns(nationID), g_cache.gunIDs(nationID), unlocksDescrs, sharedItem.compactDescr, multiGun=sharedItem.multiGun)
    if IS_CLIENT or IS_UE_EDITOR:
        sharedCam = sharedItem.camouflage
        cam = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=sharedCam)
        if cam != sharedCam:
            hasOverride = True
    if not section.has_key(b'unlocks'):
        unlocks = sharedItem.unlocks
    else:
        hasOverride = True
        unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, sharedItem.compactDescr)
    if not hasOverride:
        return sharedItem
    else:
        descr = sharedItem.copy()
        descr.guns = guns
        descr.secondaryGuns = secondaryGuns
        descr.unlocks = unlocks
        if IS_CLIENT or IS_UE_EDITOR:
            descr.camouflage = cam
        return descr


if IS_CLIENT or IS_UE_EDITOR:
    MultiGunInstance = namedtuple(b'MultiGun', (b'node', b'gunFire', b'position', b'shotOffset', b'shotPosition'))
    if IS_UE_EDITOR:
        MultiGunInstance = reflectedNamedTuple(b'MultiGun', (
         b'node', b'gunFire', b'position', b'shotOffset', b'shotPosition'))
else:
    MultiGunInstance = namedtuple(b'MultiGun', (b'position', b'shotOffset', b'shotPosition'))
MultiGun = MultiGunInstance

def _readMultiGun(xmlCtx, section, subsection):
    multiGun = []
    gun_tag_name = b'gun'
    for name, mSubsection in _xml.getChildren(xmlCtx, section, subsection):
        if name != gun_tag_name:
            _xml.raiseWrongXml(xmlCtx, (b'multiGun/{}').format(name), (b'expected {}').format(gun_tag_name))
        ctx = (
         xmlCtx, (b'multiGun/{}').format(gun_tag_name))
        gunPosition = _xml.readVector3(ctx, mSubsection, b'position')
        gunShotOffset = _xml.readVector3(ctx, mSubsection, b'shotOffset', defaultValue=Vector3(0.0, 0.0, 0.0))
        gunShotPosition = gunPosition + gunShotOffset
        if IS_CLIENT or IS_UE_EDITOR:
            gunNode = _xml.readString(ctx, mSubsection, b'gunNode')
            gunFire = _xml.readString(ctx, mSubsection, b'gunFire')
            multiGun.append(MultiGunInstance(gunNode, gunFire, gunPosition, gunShotOffset, gunShotPosition))
        else:
            multiGun.append(MultiGunInstance(gunPosition, gunShotOffset, gunShotPosition))

    return multiGun


def makeMultiExtraNameTemplate(name):
    if b'_' in name:
        return name.replace(b'_', b'{}', 1)
    return name + b'{}'


def _readExtraLocals(vehType, xmlCtx, section):
    vehExtrasDict = vehType.extrasDict
    vehExtras = list(vehType.extras)
    _, extrasDict = common_extras.readExtras(xmlCtx, section, b'extras', b'vehicle_extras', vehType=vehType)
    for extraName, extra in viewitems(extrasDict):
        oldExtra = vehExtrasDict.get(extraName)
        if oldExtra:
            extra.index = oldExtra.index
            vehExtras[oldExtra.index] = extra
        else:
            extra.index = len(vehExtras)
            vehExtras.append(extra)
        vehExtrasDict[extraName] = extra

    vehType.extras = tuple(vehExtras)
    vehType.tankmen = _selectCrewExtras(vehType.crewRoles, vehType.extrasDict)
    if section.has_key(b'deviceExtras'):
        deviceTypes = g_cache.commonConfig[b'deviceExtraIndexToTypeIndex'].copy()
        newDevicesTypes, _ = _readDeviceTypes(xmlCtx, section, b'deviceExtras', extrasDict)
        deviceTypes.update(newDevicesTypes)
        vehType.devices = frozenset(vehExtras[idx] for idx in deviceTypes)
    return


def _provideMultipleExtras(vehType):
    chassisItems = tuple()
    for chassis in vehType.chassis:
        chassisItems += chassis.wheels.wheels if vehType.isWheeledVehicle else chassis.trackPairs

    for item in chassisItems + vehType.hulls:
        for matKind, matInfo in item.materials.items():
            if matInfo.multipleExtra:
                item.materials[matKind] = matInfo._replace(extra=vehType.extrasDict[matInfo.extra])

    return


def _readGun(xmlCtx, section, item, unlocksDescrs=None, _=None, multiGun=None):
    item.tags = _readTags(xmlCtx, section, b'tags', b'vehicleGun')
    item.level = _readLevel(xmlCtx, section)
    isSecondaryGun = b'secondaryGun' in item.tags
    if section.has_key(b'rotationSpeed'):
        item.rotationSpeed = radians(_xml.readNonNegativeFloat(xmlCtx, section, b'rotationSpeed'))
    if section.has_key(b'weight'):
        item.weight = _xml.readPositiveFloat(xmlCtx, section, b'weight')
    item.reloadTime = _xml.readPositiveFloat(xmlCtx, section, b'reloadTime')
    item.aimingTime = _xml.readPositiveFloat(xmlCtx, section, b'aimingTime')
    item.forcedReloadTime = _xml.readPositiveFloat(xmlCtx, section, b'forcedReloadTime', defaultValue=0.0)
    if section.has_key(b'maxAmmo'):
        item.maxAmmo = _xml.readInt(xmlCtx, section, b'maxAmmo', 1)
    elif not isSecondaryGun:
        _xml.raiseWrongSection(xmlCtx, b'maxAmmo')
    item.invisibilityFactorAtShot = _xml.readFraction(xmlCtx, section, b'invisibilityFactorAtShot')
    item.shotOffset = _xml.readVector3(xmlCtx, section, b'shotOffset', defaultValue=Vector3(0.0, 0.0, 0.0))
    item.multiGunState = _readMultiGunState(xmlCtx, section, multiGun)
    _readPriceForItem(xmlCtx, section, item.compactDescr)
    if IS_CLIENT or IS_WEB:
        item.i18n = shared_readers.readUserText(section)
    if IS_CLIENT or IS_UE_EDITOR:
        if section.has_key(b'models'):
            item.modelsSets = shared_readers.readModelsSets(xmlCtx, section, b'models')
            item.models = item.modelsSets[b'default']
        effName = _xml.readStringOrEmpty(xmlCtx, section, b'effects')
        item.effects = g_cache.gunEffects.get(effName)
        prefabEffName = _readPrefabEffect(xmlCtx, section, b'prefabEffects', g_cache.defaultPrefabEffects.gun)
        item.prefabEffects = g_cache.prefabEffects.gun.get(prefabEffName)
        effName = _xml.readStringOrNone(xmlCtx, section, b'reloadEffect')
        if effName is not None:
            reloadEff = g_cache._gunReloadEffects.get(effName, None)
            if reloadEff is None:
                _xml.raiseWrongXml(xmlCtx, b'effects', b"unknown reload effect '%s'" % effName)
            item.reloadEffect = reloadEff
        item.impulse = _xml.readNonNegativeFloat(xmlCtx, section, b'impulse', defaultValue=0.0)
        item.recoil = gun_readers.readRecoilEffect(xmlCtx, section, g_cache)
        if section.has_key(b'camouflage'):
            item.camouflage = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=shared_components.DEFAULT_CAMOUFLAGE)
        item.animateEmblemSlots = section.readBool(b'animateEmblemSlots', True)
        if section.has_key(b'emblemSlots'):
            item.emblemSlots, item.slotsAnchors = shared_readers.readEmblemSlots(xmlCtx, section, b'emblemSlots')
        item.edgeByVisualModel = section.readBool(b'edgeByVisualModel', True)
        item.muzzleBrake = _readMuzzleBrake(xmlCtx, section)
    if IS_CLIENT or IS_UE_EDITOR or IS_BOT or IS_BASEAPP:
        if section.has_key(b'customizationSlots'):
            item.emblemSlots, item.slotsAnchors = shared_readers.readCustomizationSlots(xmlCtx, section, b'customizationSlots')
    if section.has_key(b'hitTester'):
        item.hitTesterManager = _readHitTester(xmlCtx, section, b'hitTester')
    if section.has_key(b'armor'):
        item.materials = _readArmor(xmlCtx, section, b'armor')
    if section.has_key(b'turretYawLimits'):
        item.turretYawLimits = __readRotationAngleLimits(xmlCtx, section, b'turretYawLimits')
    elif not isSecondaryGun:
        _xml.raiseWrongSection(xmlCtx, b'turretYawLimits')
    if section.has_key(b'pitchLimits'):
        item.pitchLimits = _readGunPitchLimits(xmlCtx, section[b'pitchLimits'], False)
        _validatePitchLimits(xmlCtx, b'pitchLimits', item.pitchLimits)
    elif not isSecondaryGun:
        _xml.raiseWrongSection(xmlCtx, b'pitchLimits')
    if section.has_key(b'staticTurretYaw'):
        item.staticTurretYaw = angle = _xml.readFloat(xmlCtx, section, b'staticTurretYaw')
        if angle is not None:
            item.staticTurretYaw = radians(angle)
    else:
        item.staticTurretYaw = None
    if section.has_key(b'staticPitch'):
        item.staticPitch = angle = _xml.readFloat(xmlCtx, section, b'staticPitch')
        if angle is not None:
            item.staticPitch = radians(angle)
    else:
        item.staticPitch = None
    if not isSecondaryGun:
        item.healthParams = shared_readers.readDeviceHealthParams(xmlCtx, section)
    item.shotDispersionAngle = atan(_xml.readNonNegativeFloat(xmlCtx, section, b'shotDispersionRadius') / 100.0)
    item.shotDispersionFactors = _readGunShotDispersionFactors(xmlCtx, section, b'shotDispersionFactors')
    if not section.has_key(b'autoreload'):
        item.autoreload = component_constants.DEFAULT_GUN_AUTORELOAD
    else:
        item.autoreload, item.autoreloadHasBoost = _readGunClipAutoreload(xmlCtx, section)
    if not section.has_key(b'burst'):
        item.burst = component_constants.DEFAULT_GUN_BURST
    else:
        item.burst = _readGunBurst(xmlCtx, section)
    if not section.has_key(b'clip'):
        item.clip = component_constants.DEFAULT_GUN_CLIP
    else:
        item.clip = _readGunClip(xmlCtx, section)
    if not section.has_key(b'autoShoot'):
        item.autoShoot = component_constants.DEFAULT_GUN_AUTOSHOOT
    else:
        item.autoShoot = _readAutoShootGun(xmlCtx, section)
    if not section.has_key(b'twinGun'):
        item.twinGun = component_constants.DEFAULT_GUN_TWINGUN
    else:
        item.twinGun = _readGunTwinGunParams(xmlCtx, section)
    if section.has_key(b'controllableReload'):
        item.controllableReload = _readGunControllableReload(xmlCtx, section)
    if item.burst[0] > item.clip[0] > 1:
        _xml.raiseWrongXml(xmlCtx, b'burst', b'burst/count is larger than clip/count')
    if item.autoreload != component_constants.DEFAULT_GUN_AUTORELOAD and item.clip[0] <= 1:
        _xml.raiseWrongXml(xmlCtx, b'autoreload', b"'autoreload' section is redundant for non-clip items")
    if item.autoShoot != component_constants.DEFAULT_GUN_AUTOSHOOT and item.clip[0] <= 1:
        _xml.raiseWrongXml(xmlCtx, b'autoShoot', b"'autoShoot' section is redundant for non-clip items")
    if item.controllableReload is not None and item.clip[0] <= 1:
        _xml.raiseWrongXml(xmlCtx, b'controllableReload', b"'controllableReload' section is redundant for non-clip items")
    dualGun = None
    if section.has_key(b'dualGun'):
        dualGun = _readGunDualGunParams(xmlCtx, section)
        item.dualGun = dualGun
    dualAccuracy = None
    if section.has_key(b'dualAccuracy'):
        dualAccuracy = _readGunDualAccuracyParams(xmlCtx, section)
        item.dualAccuracy = dualAccuracy
    item.shootImpulses = _readShootImpulses(xmlCtx, section)
    tags = item.tags
    if item.clip[0] == 1:
        tags -= {b'clip'}
    else:
        tags |= {b'clip'}
    if item.autoreload == component_constants.DEFAULT_GUN_AUTORELOAD:
        tags -= {b'autoreload'}
    else:
        tags |= {b'autoreload'}
    if item.autoShoot == component_constants.DEFAULT_GUN_AUTOSHOOT:
        tags -= {b'autoShoot', b'unlimitedClip'}
    else:
        tags |= {b'autoShoot'}
        if item.clip[0] != item.maxAmmo:
            tags -= {b'unlimitedClip'}
        else:
            tags |= {b'unlimitedClip'}
    if item.twinGun == component_constants.DEFAULT_GUN_TWINGUN:
        tags -= {b'twinGun'}
    else:
        tags |= {b'twinGun'}
    if dualGun is None:
        tags -= {b'dualGun'}
    else:
        tags |= {b'dualGun'}
    if dualAccuracy is None:
        tags -= {b'dualAccuracy'}
    else:
        tags |= {b'dualAccuracy'}
    if item.controllableReload is None:
        tags -= {b'controllableReload'}
    else:
        tags |= {b'controllableReload'}
    item.tags = tags
    nationID = parseIntCompactDescr(item.compactDescr)[1]
    shots = [_readShot((xmlCtx, b'shots/' + sname), subsection, nationID) for sname, subsection in _xml.getChildren(xmlCtx, section, b'shots')]
    if not shots:
        _xml.raiseWrongXml(xmlCtx, b'shots', b'no shots are specified')
    item.shots = tuple(shots)
    item.isDamageMutable = any(shot.shell.isDamageMutable for shot in item.shots)
    if IS_CLIENT or IS_WEB:
        item.effectsCaliber = _xml.readPositiveFloat(xmlCtx, section, b'effectsCaliber', shots[0].shell.effectsCaliber)
    item.prefabs = shared_readers.readPrefabsSets(section[b'prefabs'], (b'main', b'custom'))
    item.slotPrefabs = shared_readers.readSlotPrefabs(section)
    item.objectSlots = shared_readers.readObjectSlots(xmlCtx, section)
    item.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, item.compactDescr)
    if not isSecondaryGun and section.has_key(b'secondaryGun'):
        item.secondaryGunID = _readSecondaryGunID(xmlCtx, section, item.id[0])
    item.mechanicsParams = _readItemMechanicsParams(xmlCtx, section[b'mechanics'], item)
    return


if IS_UE_EDITOR:

    def __markEditorPropertyAsOverride(object, propertyName):
        if hasattr(object, b'editorData'):
            sharedPropertiesInfo = object.editorData.sharedPropertiesInfo
            if sharedPropertiesInfo is not None:
                sharedPropertiesInfo.markAsOverride(propertyName)
        return


else:

    def __markEditorPropertyAsOverride(object, propertyName):
        return


def _readGunLocals(xmlCtx, section, sharedItem, unlocksDescrs, turretCompactDescr, multiGun=None):
    hasOverride = False
    isSecondaryGun = b'secondaryGun' in sharedItem.tags
    sharedItem.customizableVehicleAreas = _readCustomizableAreas(xmlCtx, section, b'customization')
    if not section.has_key(b'turretYawLimits'):
        turretYawLimits = sharedItem.turretYawLimits
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'turretYawLimits')
        v = _xml.readVector2(xmlCtx, section, b'turretYawLimits')
        if v[0] > v[1]:
            _xml.raiseWrongSection(xmlCtx, b'turretYawLimits')
        turretYawLimits = cachedFloatTuple((radians(v[0]), radians(v[1]))) if v[0] > -179.0 or v[1] < 179.0 else None
    if section.has_key(b'pitchLimits'):
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'pitchLimits')
        pitchLimits = _readGunPitchLimits(xmlCtx, section[b'pitchLimits'], True)
    else:
        pitchLimits = sharedItem.pitchLimits
    if not section.has_key(b'shotOffset'):
        shotOffset = sharedItem.shotOffset
    else:
        hasOverride = True
        shotOffset = _xml.readVector3(xmlCtx, section, b'shotOffset')
    if multiGun is None and sharedItem.multiGun is None:
        multiGunState = sharedItem.multiGunState
    else:
        hasOverride = True
        multiGunState = _readMultiGunState(xmlCtx, section, multiGun)
    if not section.has_key(b'staticTurretYaw'):
        staticTurretYaw = sharedItem.staticTurretYaw
    else:
        hasOverride = True
        staticTurretYaw = radians(_xml.readFloat(xmlCtx, section, b'staticTurretYaw'))
    if not section.has_key(b'staticPitch'):
        staticPitch = sharedItem.staticPitch
    else:
        hasOverride = True
        staticPitch = radians(_xml.readFloat(xmlCtx, section, b'staticPitch'))
    if not section.has_key(b'rotationSpeed'):
        rotationSpeed = sharedItem.rotationSpeed
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'rotationSpeed')
        rotationSpeed = radians(_xml.readNonNegativeFloat(xmlCtx, section, b'rotationSpeed'))
    if not section.has_key(b'reloadTime'):
        reloadTime = sharedItem.reloadTime
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'reloadTime')
        reloadTime = _xml.readPositiveFloat(xmlCtx, section, b'reloadTime')
    if not section.has_key(b'aimingTime'):
        aimingTime = sharedItem.aimingTime
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'aimingTime')
        aimingTime = _xml.readPositiveFloat(xmlCtx, section, b'aimingTime')
    if not section.has_key(b'forcedReloadTime'):
        forcedReloadTime = sharedItem.forcedReloadTime
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'forcedReloadTime')
        forcedReloadTime = _xml.readPositiveFloat(xmlCtx, section, b'forcedReloadTime')
    if not section.has_key(b'maxAmmo'):
        ammo = sharedItem.maxAmmo
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'maxAmmo')
        ammo = _xml.readInt(xmlCtx, section, b'maxAmmo', 1)
    if not section.has_key(b'shotDispersionRadius'):
        shotDispAngle = sharedItem.shotDispersionAngle
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'shotDispersionRadius')
        shotDispAngle = atan(_xml.readNonNegativeFloat(xmlCtx, section, b'shotDispersionRadius') / 100.0)
    if not section.has_key(b'shotDispersionFactors'):
        shotDispFactors = sharedItem.shotDispersionFactors
    else:
        hasOverride = True
        shotDispFactors = _readGunShotDispersionFactors(xmlCtx, section, b'shotDispersionFactors')
    if not section.has_key(b'autoreload'):
        autoreload = sharedItem.autoreload
    else:
        hasOverride = True
        autoreload, autoreloadHasBoost = _readGunClipAutoreload(xmlCtx, section)
    if not section.has_key(b'autoShoot'):
        autoShoot = sharedItem.autoShoot
    else:
        hasOverride = True
        autoShoot = _readAutoShootGun(xmlCtx, section)
    if not section.has_key(b'burst'):
        burst = sharedItem.burst
    else:
        hasOverride = True
        burst = _readGunBurst(xmlCtx, section)
    if not section.has_key(b'clip'):
        clip = sharedItem.clip
    else:
        hasOverride = True
        clip = _readGunClip(xmlCtx, section)
    if not section.has_key(b'controllableReload'):
        controllableReload = sharedItem.controllableReload
    else:
        hasOverride = True
        controllableReload = _readGunControllableReload(xmlCtx, section)
    if not section.has_key(b'twinGun'):
        twinGun = sharedItem.twinGun
    else:
        hasOverride = True
        twinGun = _readGunTwinGunParams(xmlCtx, section)
    if burst[0] > clip[0] > 1:
        _xml.raiseWrongXml(xmlCtx, b'burst', b'burst/count is larger than clip/count')
    if autoreload != component_constants.DEFAULT_GUN_AUTORELOAD and clip[0] <= 1:
        _xml.raiseWrongXml(xmlCtx, b'autoreload', b"'autoreload' section is redundant for non-clip items")
    if autoShoot != component_constants.DEFAULT_GUN_AUTOSHOOT and clip[0] <= 1:
        _xml.raiseWrongXml(xmlCtx, b'autoShoot', b"'autoShoot' section is redundant for non-clip items")
    if controllableReload is not None and clip[0] <= 1:
        _xml.raiseWrongXml(xmlCtx, b'controllableReload', b"'controllableReload' section is redundant for non-clip items")
    dualGun = None
    if section.has_key(b'dualGun'):
        hasOverride = True
        dualGun = _readGunDualGunParams(xmlCtx, section)
    dualAccuracy = None
    if section.has_key(b'dualAccuracy'):
        hasOverride = True
        dualAccuracy = _readGunDualAccuracyParams(xmlCtx, section)
    shootImpulses = _readShootImpulses(xmlCtx, section)
    if shootImpulses:
        hasOverride = True
    if not section.has_key(b'invisibilityFactorAtShot'):
        invisibilityFactorAtShot = sharedItem.invisibilityFactorAtShot
    else:
        hasOverride = True
        __markEditorPropertyAsOverride(sharedItem, b'invisibilityFactorAtShot')
        invisibilityFactorAtShot = _xml.readFraction(xmlCtx, section, b'invisibilityFactorAtShot')
    if IS_CLIENT or IS_UE_EDITOR:
        if not section.has_key(b'models'):
            modelsSets = sharedItem.modelsSets
            models = sharedItem.models
            if models is None and not isSecondaryGun:
                _xml.raiseWrongSection(xmlCtx, b'models')
        else:
            hasOverride = True
            modelsSets = shared_readers.readModelsSets(xmlCtx, section, b'models')
            models = modelsSets[b'default']
        if not section.has_key(b'effects'):
            effects = sharedItem.effects
        else:
            hasOverride = True
            __markEditorPropertyAsOverride(sharedItem, b'effects')
            effName = _xml.readNonEmptyString(xmlCtx, section, b'effects')
            effects = g_cache.gunEffects.get(effName)
            if effects is None:
                _xml.raiseWrongXml(xmlCtx, b'effects', b"unknown effect '%s'" % effName)
        if not section.has_key(b'prefabEffects'):
            prefabEffects = sharedItem.prefabEffects
        else:
            hasOverride = True
            __markEditorPropertyAsOverride(sharedItem, b'prefabEffects')
            effName = _xml.readString(xmlCtx, section, b'prefabEffects')
            prefabEffects = g_cache.prefabEffects.gun.get(effName)
            if effName and prefabEffects is None:
                _xml.raiseWrongXml(xmlCtx, b'prefabEffects', b"unknown effect '%s'" % effName)
        if section.has_key(b'multiGunEffects'):
            multiGunEffects = _xml.readNonEmptyString(xmlCtx, section, b'multiGunEffects')
            effects = []
            for effName in multiGunEffects.split():
                effect = g_cache.gunEffects.get(intern(effName))
                effects.append(effect)

        if not section.has_key(b'recoil'):
            recoil = sharedItem.recoil
        else:
            hasOverride = True
            __markEditorPropertyAsOverride(sharedItem, b'recoil')
            recoil = gun_readers.readRecoilEffect(xmlCtx, section, g_cache)
        if not section.has_key(b'impulse'):
            impulse = sharedItem.impulse
        else:
            hasOverride = True
            __markEditorPropertyAsOverride(sharedItem, b'impulse')
            impulse = _xml.readNonNegativeFloat(xmlCtx, section, b'impulse')
        reloadEffect = sharedItem.reloadEffect
        if section.has_key(b'reloadEffect'):
            hasOverride = True
            effName = _xml.readStringOrNone(xmlCtx, section, b'reloadEffect')
            if effName is not None:
                reloadEffect = g_cache._gunReloadEffects.get(effName, None)
                if reloadEffect is None:
                    _xml.raiseWrongXml(xmlCtx, b'effects', b"unknown reload effect '%s'" % effName)
        sharedCam = sharedItem.camouflage
        cam = shared_readers.readCamouflage(xmlCtx, section, b'camouflage', default=sharedCam)
        if cam != sharedCam:
            hasOverride = True
        if not section.has_key(b'animateEmblemSlots'):
            animateEmblemSlots = sharedItem.animateEmblemSlots
        else:
            hasOverride = True
            animateEmblemSlots = section.readBool(b'animateEmblemSlots', True)
        if not section.has_key(b'edgeByVisualModel'):
            edgeByVisualModel = sharedItem.edgeByVisualModel
        else:
            hasOverride = True
            edgeByVisualModel = section.readBool(b'edgeByVisualModel', True)
        if section.has_key(b'drivenJoints'):
            drivenJoints = _readDrivenJoints(xmlCtx, section, b'drivenJoints')
        else:
            drivenJoints = {}
        muzzleBrake = sharedItem.muzzleBrake
        if section.has_key(b'muzzleBrake'):
            hasOverride = True
            muzzleBrake = _readMuzzleBrake(xmlCtx, section)
    slotsAnchors = tuple([])
    if IS_CLIENT or IS_UE_EDITOR or IS_BOT or IS_BASEAPP:
        if not section.has_key(b'emblemSlots') and not section.has_key(b'customizationSlots'):
            if not IS_BOT and not IS_BASEAPP:
                emblemSlots = sharedItem.emblemSlots
            slotsAnchors = sharedItem.slotsAnchors
        else:
            hasOverride = True
            __markEditorPropertyAsOverride(sharedItem, b'emblemSlots')
            __markEditorPropertyAsOverride(sharedItem, b'slotsAnchors')
            if section.has_key(b'emblemSlots'):
                if not IS_BOT and not IS_BASEAPP:
                    emblemSlots, slotsAnchors = shared_readers.readEmblemSlots(xmlCtx, section, b'emblemSlots')
            elif section.has_key(b'customizationSlots'):
                emblemSlots, slotsAnchors = shared_readers.readCustomizationSlots(xmlCtx, section, b'customizationSlots')
    if IS_BASEAPP:
        htManager = None
        materials = None
    else:
        if not section.has_key(b'hitTester'):
            htManager = sharedItem.hitTesterManager
            if htManager is None and not isSecondaryGun:
                _xml.raiseWrongSection(xmlCtx, b'hitTester')
        else:
            hasOverride = True
            htManager = _readHitTester(xmlCtx, section, b'hitTester')
        if not section.has_key(b'armor'):
            materials = sharedItem.materials
            if materials is None and not isSecondaryGun:
                _xml.raiseWrongSection(xmlCtx, b'armor')
        else:
            hasOverride = True
            materials = _readArmor(xmlCtx, section, b'armor')
    if not section.has_key(b'unlocks'):
        unlocks = sharedItem.unlocks
    else:
        hasOverride = True
        unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, sharedItem.compactDescr, turretCompactDescr)
    if not section.has_key(b'prefabs'):
        prefabs = sharedItem.prefabs
    else:
        hasOverride = True
        prefabs = shared_readers.readPrefabsSets(section[b'prefabs'], (b'main', b'custom'))
    if not section.has_key(b'secondaryGun') or isSecondaryGun:
        secondaryGunID = sharedItem.secondaryGunID
    else:
        hasOverride = True
        secondaryGunID = _readSecondaryGunID(xmlCtx, section, sharedItem.id[0])
    if not section.has_key(b'mechanics'):
        mechanicsParams = sharedItem.mechanicsParams
    else:
        hasOverride = True
        mechanicsParams = _readItemMechanicsParams(xmlCtx, section[b'mechanics'], sharedItem, copy.deepcopy(sharedItem.mechanicsParams))
    if not section.has_key(b'slotPrefabs'):
        slotPrefabs = sharedItem.slotPrefabs
    else:
        hasOverride = True
        slotPrefabs = shared_readers.readSlotPrefabs(section)
    if not section.has_key(b'objectSlots'):
        objectSlots = sharedItem.objectSlots
    else:
        hasOverride = True
        objectSlots = shared_readers.readObjectSlots(xmlCtx, section)
    shots = sharedItem.shots
    if section.has_key(b'shots'):
        hasOverride = True
        shotsCtx, shotsSection = _xml.getSubSectionWithContext(xmlCtx, section, b'shots')
        shots = tuple(_readShotLocal(shotsCtx, shotsSection, shot) for shot in shots)
    if not hasOverride:
        return sharedItem
    else:
        item = sharedItem.copy()
        item.turretYawLimits = turretYawLimits
        item.rotationSpeed = rotationSpeed
        item.reloadTime = reloadTime
        item.aimingTime = aimingTime
        item.forcedReloadTime = forcedReloadTime
        item.maxAmmo = ammo
        item.shotDispersionAngle = shotDispAngle
        item.shotDispersionFactors = shotDispFactors
        item.burst = burst
        item.unlocks = unlocks
        item.hitTesterManager = htManager
        item.materials = materials
        item.staticTurretYaw = staticTurretYaw
        item.staticPitch = staticPitch
        item.shotOffset = shotOffset
        item.multiGunState = multiGunState
        item.secondaryGunID = secondaryGunID
        item.mechanicsParams = mechanicsParams
        if IS_UE_EDITOR:
            if not isSecondaryGun and hasattr(item.editorData, b'secondaryGunName'):
                if section.has_key(b'secondaryGun'):
                    item.editorData.secondaryGunName = _xml.readString(xmlCtx, section, b'secondaryGun')
        if not isSecondaryGun:
            item.pitchLimits = copy.deepcopy(sharedItem.pitchLimits)
            item.pitchLimits.update(pitchLimits)
            _validatePitchLimits(xmlCtx, b'pitchLimits', item.pitchLimits)
        if clip is not sharedItem.clip:
            item.clip = clip
            tags = item.tags
            if clip[0] == 1:
                tags -= {b'clip'}
            else:
                tags |= {b'clip'}
            item.tags = tags
        if autoreload is not sharedItem.autoreload:
            item.autoreload = autoreload
            item.autoreloadHasBoost = autoreloadHasBoost
            tags = item.tags
            if autoreload == component_constants.DEFAULT_GUN_AUTORELOAD:
                tags -= {b'autoreload'}
            else:
                tags |= {b'autoreload'}
            item.tags = tags
        if autoShoot is not sharedItem.autoShoot:
            item.autoShoot = autoShoot
            tags = item.tags
            if autoShoot == component_constants.DEFAULT_GUN_AUTOSHOOT:
                tags -= {b'autoShoot', b'unlimitedClip'}
            else:
                tags |= {b'autoShoot'}
                if clip[0] != item.maxAmmo:
                    tags -= {b'unlimitedClip'}
                else:
                    tags |= {b'unlimitedClip'}
            item.tags = tags
        if twinGun is not sharedItem.twinGun:
            item.twinGun = twinGun
            tags = item.tags
            if twinGun == component_constants.DEFAULT_GUN_TWINGUN:
                tags -= {b'twinGun'}
            else:
                tags |= {b'twinGun'}
            item.tags = tags
        if dualGun is not None:
            item.dualGun = dualGun
            tags = item.tags
            if dualGun == component_constants.DEFAULT_GUN_DUALGUN:
                tags -= {b'dualGun'}
            else:
                tags |= {b'dualGun'}
            item.tags = tags
        if dualAccuracy is not None:
            item.dualAccuracy = dualAccuracy
            tags = item.tags
            if dualAccuracy == component_constants.DEFAULT_GUN_DUAL_ACCURACY:
                tags -= {b'dualAccuracy'}
            else:
                tags |= {b'dualAccuracy'}
            item.tags = tags
        if controllableReload is not sharedItem.controllableReload:
            item.controllableReload = controllableReload
            tags = item.tags
            if controllableReload is None:
                tags -= {b'controllableReload'}
            else:
                tags |= {b'controllableReload'}
            item.tags = tags
        if shootImpulses:
            item.shootImpulses = shootImpulses
        if IS_CLIENT or IS_UE_EDITOR:
            item.modelsSets = modelsSets
            item.models = models
            item.effects = effects
            item.prefabEffects = prefabEffects
            item.recoil = recoil
            item.impulse = impulse
            item.camouflage = cam
            item.animateEmblemSlots = animateEmblemSlots
            item.edgeByVisualModel = edgeByVisualModel
            item.emblemSlots = emblemSlots
            item.reloadEffect = reloadEffect
            item.drivenJoints = drivenJoints
            item.muzzleBrake = muzzleBrake
        if IS_CLIENT or IS_UE_EDITOR or IS_BOT or IS_BASEAPP:
            item.slotsAnchors = slotsAnchors
        item.invisibilityFactorAtShot = invisibilityFactorAtShot
        item.prefabs = prefabs
        item.slotPrefabs = slotPrefabs
        item.objectSlots = objectSlots
        item.shots = shots
        return item


def _writeGun(item, section, sharedSections, materialData, parentName):
    shared_writers.writeSlotPrefabs(item.slotPrefabs, section)
    shared_writers.writeObjectSlots(item.objectSlots, section)
    isSG = isSecondaryGunCheck(item)
    _xml.rewriteFloat(section, b'rotationSpeed', degrees(item.rotationSpeed), 0.0)
    _xml.rewriteFloat(section, b'weight', item.weight, 0.0)
    _xml.rewriteFloat(section, b'reloadTime', item.reloadTime, 0.0)
    _xml.rewriteFloat(section, b'aimingTime', item.aimingTime, 0.0)
    _xml.rewriteFloat(section, b'forcedReloadTime', item.forcedReloadTime, 0.0)
    if isSG is False:
        _xml.rewriteInt(section, b'maxAmmo', item.maxAmmo, 1)
    _xml.rewriteFloat(section, b'shotDispersionRadius', tan(item.shotDispersionAngle) * 100.0)
    _xml.rewriteFloat(section, b'invisibilityFactorAtShot', item.invisibilityFactorAtShot)
    _xml.rewriteFloat(section, b'impulse', item.impulse, 0.0)
    _xml.rewriteBool(section, b'animateEmblemSlots', item.animateEmblemSlots, True)
    _xml.rewriteBool(section, b'edgeByVisualModel', item.edgeByVisualModel, True)
    _xml.rewriteVector3(section, b'shotOffset', item.shotOffset, (0, 0, 0))
    _xml.rewriteString(section, b'muzzleBrake', item.muzzleBrake.name, component_constants.MuzzleBrakeType.NONE.name)
    if isSG is False:
        _xml.rewriteVector2(section, b'turretYawLimits', item.editorTurretYawLimits)
    _writeGunEffectName(item, section)
    _writeCamouflageSettings(section, b'camouflage', item.camouflage)
    _writeArmor(item.materials, section, materialData.get(item.name + parentName, None) if materialData is not None else None)
    slots = item.emblemSlots + item.slotsAnchors
    shared_writers.writeCustomizationSlots(slots, section, b'customizationSlots')
    if isSG is False:
        _writeCustomizableAreas(item.customizableVehicleAreas, section)
    shared_writers.writeModelsSets(item.modelsSets, section[b'models'])
    gun_writers.writeRecoilEffect(item.recoil, section[b'recoil'], g_cache)
    _writeHitTester(item.hitTesterManager, None, section, b'hitTester')
    _writeGunPitchLimits(item.pitchLimits, section[b'pitchLimits'])
    _writeDrivenJoints(item.drivenJoints, section, b'drivenJoints')
    _writeDualGun(item, section)
    if isSG is True:
        _writeSecondaryGunPrefabs(item, section)
        _writeMechanics(item, section)
    return


def _writeGunEffectName(item, section):
    effects = item.effects
    effectName = None
    if isinstance(effects, list):
        for effect in effects:
            if effectName is None:
                effectName = getEffectNameByEffect(effect)
            else:
                effectName += b' ' + getEffectNameByEffect(effect)

    else:
        effectName = getEffectNameByEffect(effects)
    if effectName is not None:
        if item.dualGun and item.dualGun is not component_constants.DEFAULT_GUN_DUALGUN:
            _xml.rewriteString(section, b'multiGunEffects', effectName)
        elif len(effectName.split(b' ')) > 1:
            _xml.rewriteString(section, b'multiGunEffects', effectName)
        else:
            _xml.rewriteString(section, b'effects', effectName)
    prefabEffectName = getPrefabEffectNameByEffect(item.prefabEffects)
    if prefabEffectName is not None:
        _xml.rewriteString(section, b'prefabEffects', prefabEffectName, g_cache.defaultPrefabEffects.gun)
    return


def _readGunPitchLimitsSiege(xmlCtx, section, subsectionName):
    subsec = section[subsectionName]
    res = {b'minPitch': (_readGunPitchConstraints(xmlCtx, subsec, b'minPitch')), 
       b'maxPitch': (_readGunPitchConstraints(xmlCtx, subsec, b'maxPitch'))}
    return res


def _readGunPitchLimits(xmlCtx, section, isLocal):
    res = {}
    if section.has_key(b'minPitch'):
        res[b'minPitch'] = _readGunPitchConstraints(xmlCtx, section, b'minPitch')
    elif not isLocal:
        _xml.raiseWrongSection(xmlCtx, b'minPitch')
    if section.has_key(b'maxPitch'):
        res[b'maxPitch'] = _readGunPitchConstraints(xmlCtx, section, b'maxPitch')
    elif not isLocal:
        _xml.raiseWrongSection(xmlCtx, b'maxPitch')
    return res


def _writeGunPitchLimits(pitchLimits, section):
    if pitchLimits is not None:
        if b'minPitch' in pitchLimits:
            _writeGunPitch(pitchLimits[b'minPitch'], section, b'minPitch')
        if b'maxPitch' in pitchLimits:
            _writeGunPitch(pitchLimits[b'maxPitch'], section, b'maxPitch')
    return


def _writeGunPitch(pitchLimit, section, subsectionName):
    points = []
    for pair in pitchLimit:
        points.append(0.5 * pair[0] / pi)
        points.append(degrees(pair[1]))

    try:
        strings = section.readString(subsectionName).split()
        oldPoints = tuple(map(float, strings))
        match = True
        for i in xrange(len(oldPoints)):
            if abs(points[i] - oldPoints[i]) > 1e-05:
                match = False
                break

        if match:
            return
    except:
        pass

    pointsStr = (b' ').join([(b'{:.5f}').format(points[i]) if i % 2 == 0 else (b'{:.2f}').format(points[i]) for i in xrange(len(points))])
    _xml.rewriteString(section, subsectionName, pointsStr)
    return


def _validatePitchLimits(xmlCtx, subsectionName, pitchLimits):
    minPitch = pitchLimits[b'minPitch']
    maxPitch = pitchLimits[b'maxPitch']
    pitchLimits[b'absolute'] = cachedFloatTuple((min([key for _, key in minPitch]), max([key for _, key in maxPitch])))
    ok = _validateMinMaxPitchLimits(minPitch, maxPitch, False) and _validateMinMaxPitchLimits(maxPitch, minPitch, True)
    if not ok:
        _xml.raiseWrongSection(xmlCtx, subsectionName)
    return


def _validateMinMaxPitchLimits(firstLimit, secondLimit, isGreater):
    ok = True
    f = 0
    s = 1
    while f < len(firstLimit):
        firstYaw = firstLimit[f][0]
        firstPitch = firstLimit[f][1]
        f += 1
        while secondLimit[s][0] < firstYaw:
            s += 1

        t = (firstYaw - secondLimit[s - 1][0]) / (secondLimit[s][0] - secondLimit[s - 1][0])
        secondPitch = secondLimit[s - 1][1] * (1 - t) + secondLimit[s][1] * t
        if firstPitch == secondPitch:
            continue
        if not (firstPitch < secondPitch) ^ isGreater:
            ok = False
            break

    return ok


def _readGunPitchConstraints(xmlCtx, section, type):
    v = _xml.readTupleOfFloats(xmlCtx, section, type)
    if len(v) & 1 != 0:
        _xml.raiseWrongSection(xmlCtx, type)
    points = [(2 * pi * v[2 * index], radians(v[2 * index + 1])) for index in xrange(len(v) // 2)]
    if points[0][0] != 0 or points[-1][0] != 2 * pi or points[0][1] != points[-1][1]:
        _xml.raiseWrongSection(xmlCtx, type)
    if len(points) <= 1:
        _xml.raiseWrongSection(xmlCtx, type)
    for index in xrange(len(points) - 1):
        if points[index][0] >= points[index + 1][0]:
            _xml.raiseWrongSection(xmlCtx, type)

    return cachedFloatTuple(points)


def _readGunClip(xmlCtx, section, type=b'clip'):
    count = _xml.readInt(xmlCtx, section, type + b'/count', 1)
    interval = 60.0 / _xml.readPositiveFloat(xmlCtx, section, type + b'/rate')
    return (count, interval if count > 1 else 0.0)


def _readGunBurst(xmlCtx, section):
    count, interval = _readGunClip(xmlCtx, section, b'burst')
    syncReloading = _xml.readBool(xmlCtx, section, b'burst/syncReloading', False)
    return (count, interval, syncReloading)


def _readAutoShootGun(xmlCtx, section):
    autoShootSection = section[b'autoShoot']
    if autoShootSection is None:
        return component_constants.DEFAULT_GUN_AUTOSHOOT
    else:
        shotDispersionPerShot = _xml.readNonNegativeFloat(xmlCtx, autoShootSection, b'shotDispersionPerShot', 0.0)
        return component_constants.AutoShoot(shotDispersionPerShot=shotDispersionPerShot, maxShotDispersion=_xml.readNonNegativeFloat(xmlCtx, autoShootSection, b'maxShotDispersion', 0.0), aimingDelay=_xml.readNonNegativeFloat(xmlCtx, autoShootSection, b'aimingDelay', 0.0), groupSize=_xml.readNonNegativeInt(xmlCtx, autoShootSection, b'groupSize', 0))


def _readGunClipAutoreload(xmlCtx, section):
    reloadTime = _xml.readTupleOfPositiveFloats(xmlCtx, section, b'autoreload/reloadTime')
    if not reloadTime:
        _xml.raiseWrongXml(xmlCtx, b'autoreload/reloadTime', b"'reloadTime' must contain at least one value")
    boostStartTime = _xml.readNonNegativeFloat(xmlCtx, section, b'autoreload/boostStartTime', 0.0)
    boostResidueTime = _xml.readNonNegativeFloat(xmlCtx, section, b'autoreload/boostResidueTime', 0.0)
    fractionName = b'autoreload/boostFraction'
    boostFraction = _xml.readFraction(xmlCtx, section, fractionName) if section.has_key(fractionName) else 1.0
    hasBoost = section.has_key(b'autoreload/boostStartTime') and section.has_key(b'autoreload/boostResidueTime') and section.has_key(b'autoreload/boostFraction')
    return (
     component_constants.Autoreload(reloadTime=reloadTime, boostStartTime=boostStartTime, boostResidueTime=boostResidueTime, boostFraction=boostFraction), hasBoost)


def _readItemMechanicsParams(xmlCtx, section, item, mechanicsParams=None):
    if mechanicsParams is None:
        mechanicsParams = {}
    if section is None:
        return mechanicsParams
    else:
        for mechanicsCls in shared_components.MechanicsParams.getSubClasses():
            if item.typeID == mechanicsCls.COMPONENT_TYPE_ID:
                params = mechanicsCls.readMechanicsParams(xmlCtx, section, readModifiers)
                if params is not None:
                    mechanicsParams[mechanicsCls.MECHANICS_NAME] = params

        return mechanicsParams


def _readSecondaryGunID(xmlCtx, section, nationID):
    secondaryGunName = _xml.readString(xmlCtx, section, b'secondaryGun')
    gunIDsCache = g_cache.gunIDs(nationID)
    if secondaryGunName not in gunIDsCache:
        _xml.raiseWrongXml(xmlCtx, b'secondaryGun', b"unknown secondary gun name: '%s'" % secondaryGunName)
    return gunIDsCache[secondaryGunName]


def _readMultiGunState(xmlCtx, section, multiGun):
    if multiGun is None:
        return
    else:
        gunIndexes = lrange(len(multiGun))
        if section.has_key(b'multiGunState'):
            stateSection = section[b'multiGunState']
            gunIndexes = lmap(int, _xml.readStringOrEmpty(xmlCtx, stateSection, b'gunIndexes').split())
        return component_constants.MultiGunState(gunIndexes=gunIndexes, multiGun=[multiGun[gunIndex] for gunIndex in gunIndexes])


def _readShells(xmlPath, nationID):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    icons = {}
    if IS_CLIENT or IS_UE_EDITOR or IS_WEB:
        for name, subsection in _xml.getChildren((None, xmlPath), section, b'icons'):
            name = intern(name)
            if icons.has_key(name):
                _xml.raiseWrongXml((None, xmlPath + b'/icons'), name, b'name is not unique')
            icons[name] = _xml.readIcon((None, xmlPath + b'/icons'), subsection, b'')

    descrs = {}
    ids = {}
    for name, subsection in section.items():
        if name in (b'icons', b'xmlns:xmlref'):
            continue
        xmlCtx = (
         None, xmlPath + b'/' + name)
        name = intern(name)
        if ids.has_key(name):
            _xml.raiseWrongXml(xmlCtx, b'', b'shell type name is not unique')
        id = _xml.readInt(xmlCtx, subsection, b'id', 0, 65535)
        if descrs.has_key(id):
            _xml.raiseWrongXml(xmlCtx, b'id', b'shell type ID is not unique')
        descrs[id] = _readShell(xmlCtx, subsection, name, nationID, id, icons)
        ids[name] = id

    section = None
    subsection = None
    ResMgr.purge(xmlPath, True)
    return (
     descrs, ids)


def _readShell(xmlCtx, section, name, nationID, shellTypeID, icons):
    shell = vehicle_items.createShell(nationID, shellTypeID, name)
    shell.caliber = _xml.readPositiveFloat(xmlCtx, section, b'caliber')
    shell.isTracer = section.readBool(b'isTracer', False)
    if shell.isTracer:
        shell.isForceTracer = section.readBool(b'isForceTracer', False)
    if IS_CLIENT or IS_WEB:
        shell.i18n = shared_components.I18nComponent(userStringKey=section.readString(b'userString'), descriptionKey=section.readString(b'description'), shortDescriptionSpecialKey=section.readString(b'shortDescriptionSpecial'), longDescriptionSpecialKey=section.readString(b'longDescriptionSpecial'))
        v = _xml.readNonEmptyString(xmlCtx, section, b'icon')
        if icons.get(v) is None:
            _xml.raiseWrongXml(xmlCtx, b'icon', b"unknown icon '%s'" % v)
        shell.icon = icons.get(v)
        shell.iconName = os.path.splitext(os.path.basename(shell.icon[0]))[0]
    _readPriceForItem(xmlCtx, section, shell.compactDescr)
    if IS_CELLAPP or IS_WEB or IS_BASEAPP or IS_CLIENT:
        shell.isGold = b'gold' in _xml.readPrice(xmlCtx, section, b'price') or section.readBool(b'improved', False)
    kind = intern(_xml.readNonEmptyString(xmlCtx, section, b'kind'))
    shellType = shell_components.createShellType(kind)
    if shellType is None:
        _xml.raiseWrongXml(xmlCtx, b'kind', b"unknown shell kind '%s'" % kind)
    shell.type = shellType
    mechanics = intern(_xml.readStringWithDefaultValue(xmlCtx, section, b'mechanics', SHELL_MECHANICS_TYPE.LEGACY))
    isModernHighExplosive = mechanics == SHELL_MECHANICS_TYPE.MODERN
    shell.armorDamage = shared_readers.readFloatPair(xmlCtx, section, b'damage/armor')
    shell.isDamageMutable = shell.armorDamage[0] != shell.armorDamage[1]
    shell.deviceDamage = shared_readers.readFloatPair(xmlCtx, section, b'damage/devices')
    if section.has_key(b'obstacles/damage'):
        shell.obstaclesDamage = _xml.readNonNegativeFloat(xmlCtx, section, b'obstacles/damage')
    if section.has_key(b'obstacles/powerReduction'):
        shell.obstaclesPowerReduction = _xml.readNonNegativeFloat(xmlCtx, section, b'obstacles/powerReduction')
    if section.has_key(b'deviceDamagePossibility/protectFromDirectHits'):
        shellType.protectFromDirectHits = readProtectedModules(xmlCtx, section, b'deviceDamagePossibility/protectFromDirectHits')
    if kind == b'HIGH_EXPLOSIVE' and section.has_key(b'deviceDamagePossibility/protectFromIndirectHits'):
        shellType.protectFromIndirectHits = readProtectedModules(xmlCtx, section, b'deviceDamagePossibility/protectFromIndirectHits')
    if kind.startswith(b'ARMOR_PIERCING'):
        shellType.normalizationAngle = radians(_xml.readNonNegativeFloat(xmlCtx, section, b'normalizationAngle'))
        shellType.ricochetAngleCos = cos(radians(_xml.readNonNegativeFloat(xmlCtx, section, b'ricochetAngle')))
        shellType.enableTraceRicochet = _xml.readBool(xmlCtx, section, b'enableTraceRicochet', component_constants.DEFAULT_ENABLE_TRACE_RICOCHET)
    elif kind == b'HOLLOW_CHARGE':
        shellType.piercingPowerLossFactorByDistance = 10.0 * _xml.readNonNegativeFloat(xmlCtx, section, b'piercingPowerLossFactorByDistance')
        shellType.ricochetAngleCos = cos(radians(_xml.readNonNegativeFloat(xmlCtx, section, b'ricochetAngle')))
        shellType.enableTraceRicochet = _xml.readBool(xmlCtx, section, b'enableTraceRicochet', component_constants.DEFAULT_ENABLE_TRACE_RICOCHET)
    if kind == b'HIGH_EXPLOSIVE':
        shellType.mechanics = mechanics
        if isModernHighExplosive:
            shellType.obstaclePenetration = _xml.readBool(xmlCtx, section, b'obstaclePenetration', component_constants.DEFAULT_MODERN_HE_OBSTACLE_PENETRATION)
            shellType.shieldPenetration = _xml.readBool(xmlCtx, section, b'shieldPenetration', component_constants.DEFAULT_MODERN_HE_SHIELD_PENETRATION)
            blastWave = _readImpactParams(xmlCtx, section, HighExplosiveImpact.BLAST_WAVE)
            shellFragments = _readImpactParams(xmlCtx, section, HighExplosiveImpact.SHELL_FRAGMENTS)
            armorSpalls = _readImpactParams(xmlCtx, section, HighExplosiveImpact.ARMOR_SPALLS)
            if not (blastWave.isActive or shellFragments.isActive or armorSpalls.isActive):
                _xml.raiseWrongXml(xmlCtx, b'', b'Modern high explosive shell must contain at least one damage mechanics: blastWave, shellFragments, armorSpalls')
            shellType.blastWave = blastWave
            shellType.shellFragments = shellFragments
            shellType.armorSpalls = armorSpalls
            shellType.maxDamage = max(max(shellFragments.armorDamage), max(shellFragments.deviceDamage), max(armorSpalls.armorDamage), max(armorSpalls.deviceDamage), max(blastWave.armorDamage), max(blastWave.deviceDamage))
        shellType.explosionRadius = cachedFloat(section.readFloat(b'explosionRadius'))
        if not isModernHighExplosive and shellType.explosionRadius <= 0.0:
            shellType.explosionRadius = cachedFloat(shell.caliber * shell.caliber / 5555.0)
        explosionSettings = (b'explosionDamageFactor', b'explosionDamageAbsorptionFactor', b'explosionEdgeDamageFactor', b'shellFragmentsDamageAbsorptionFactor')
        for f in explosionSettings:
            factor = section.readFloat(f)
            if factor <= 0:
                factor = g_cache.commonConfig[b'miscParams'][f]
            setattr(shellType, f, factor)

        if shellType.explosionEdgeDamageFactor > 1.0:
            _xml.raiseWrongXml(xmlCtx, b'explosionEdgeDamageFactor', b'explosionEdgeDamageFactor must be < 1')
    elif mechanics == SHELL_MECHANICS_TYPE.NON_PIERCING_DAMAGE:
        shellType.mechanics = mechanics
        subXmlCtx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, b'nonPiercingDamage', throwIfMissing=False)
        shellType.nonPiercingArmorDamage = _xml.readNonNegativeFloat(subXmlCtx, subsection, b'damage/armor', 0.0)
    shell.damageRandomization = _xml.readNonNegativeFloat(xmlCtx, section, b'damageRandomization', component_constants.DEFAULT_DAMAGE_RANDOMIZATION)
    shell.damageRandomizationType = _xml.readStringWithDefaultValue(xmlCtx, section, b'damageRandomizationType', RandomizationType.NORMAL)
    shell.piercingPowerRandomization = _xml.readNonNegativeFloat(xmlCtx, section, b'piercingPowerRandomization', component_constants.DEFAULT_PIERCING_POWER_RANDOMIZATION)
    shell.piercingPowerRandomizationType = _xml.readStringWithDefaultValue(xmlCtx, section, b'piercingPowerRandomizationType', RandomizationType.NORMAL)
    hasStun = section.readBool(b'hasStun', False)
    if hasStun:
        stunParams = gun_readers.readStunParams(section, xmlCtx, True)
        if stunParams.get(b'stunRadius') is not None:
            stun = shell_components.Stun(**stunParams)
        elif kind == b'HIGH_EXPLOSIVE':
            stunParams[b'stunRadius'] = shellType.explosionRadius
            stun = shell_components.Stun(**stunParams)
        else:
            _xml.raiseWrongXml(xmlCtx, b'stunRadius', b'hasStun = true, but neither explosionRadius nor stunRadius defined')
    else:
        stun = None
    shell.stun = stun
    effName = _xml.readNonEmptyString(xmlCtx, section, b'effects')
    effIdx = g_cache.shotEffectsIndexes.get(effName, component_constants.INVALID_EFFECT_INDEX)
    shell.effectsIndex = effIdx
    defaultPrefabEffName = g_cache.defaultPrefabEffects.shot.shellTypeEffects.get(kind, g_cache.defaultPrefabEffects.shot.default)
    prefabEffName = _readPrefabEffect(xmlCtx, section, b'prefabEffects', defaultPrefabEffName)
    prefabEffIdx = g_cache.prefabEffects.shot.indexes.get(prefabEffName, component_constants.INVALID_EFFECT_INDEX)
    shell.prefabEffectsIndex = prefabEffIdx
    if effIdx == component_constants.INVALID_EFFECT_INDEX and prefabEffIdx == effIdx:
        _xml.raiseWrongXml(xmlCtx, b'effects', b"unknown effects: '%s' and '%s'" % (effName, prefabEffName))
    shell.effectsCaliber = _xml.readPositiveFloat(xmlCtx, section, b'effectsCaliber', shell.caliber)
    if section.has_key(b'dynamicEffects'):
        dynamicEffects = []
        for dynamicEffect in section[b'dynamicEffects'].values():
            effName = _xml.readNonEmptyString(xmlCtx, dynamicEffect, b'name')
            minShotsCount = _xml.readIntOrNone(xmlCtx, dynamicEffect, b'minShotsCount')
            maxShotsCount = _xml.readIntOrNone(xmlCtx, dynamicEffect, b'maxShotsCount')
            dynamicEffects.append(component_constants.DynamicShotEffect(effectsIndex=g_cache.shotEffectsIndexes.get(effName), minShotsCount=minShotsCount or component_constants.ONE_INT, maxShotsCount=maxShotsCount or component_constants.DYNAMIC_SHOT_MAX_COUNT))

        shell.dynamicEffectsIndexes = tuple(sorted(dynamicEffects, key=(lambda item: item.minShotsCount)))
    if section.has_key(b'tags'):
        shell.tags = _readTags(xmlCtx, section, b'tags', b'shell')
        if INFINITE_SHELL_TAG in shell.tags and FORCE_FINITE_SHELL_TAG in shell.tags:
            _xml.raiseWrongXml(xmlCtx, b'tags', (b'incompatible tags: {}, {}').format(INFINITE_SHELL_TAG, FORCE_FINITE_SHELL_TAG))
    if section.has_key(b'secondaryAttackReason'):
        shell.secondaryAttackReason = _xml.readStringOrNone(xmlCtx, section, b'secondaryAttackReason')
    if section.has_key(b'chanceToHitByProjectileModifier'):
        shell.chanceToHitByProjectileModifier = _xml.readFloat(xmlCtx, section, b'chanceToHitByProjectileModifier')
    return shell


def _readShellLocal(xmlCtx, section, originalShell):
    kind = originalShell.kind
    originalShellType = originalShell.type
    isModernHighExplosive = originalShellType.mechanics == SHELL_MECHANICS_TYPE.MODERN
    localShell = copy.copy(originalShell)
    localShellType = copy.copy(originalShell.type)
    if section.has_key(b'damage/armor'):
        localShell.armorDamage = shared_readers.readFloatPair(xmlCtx, section, b'damage/armor')
        localShell.isDamageMutable = localShell.armorDamage[0] != localShell.armorDamage[1]
    if section.has_key(b'damage/devices'):
        localShell.deviceDamage = shared_readers.readFloatPair(xmlCtx, section, b'damage/devices')
    if section.has_key(b'obstacles/damage'):
        localShell.obstaclesDamage = _xml.readNonNegativeFloat(xmlCtx, section, b'obstacles/damage')
    if section.has_key(b'obstacles/powerReduction'):
        localShell.obstaclesPowerReduction = _xml.readNonNegativeFloat(xmlCtx, section, b'obstacles/powerReduction')
    if section.has_key(b'deviceDamagePossibility/protectFromDirectHits'):
        localShellType.protectFromDirectHits = readProtectedModules(xmlCtx, section, b'deviceDamagePossibility/protectFromDirectHits')
    if kind == b'HIGH_EXPLOSIVE' and section.has_key(b'deviceDamagePossibility/protectFromIndirectHits'):
        localShellType.protectFromIndirectHits = readProtectedModules(xmlCtx, section, b'deviceDamagePossibility/protectFromIndirectHits')
    if kind.startswith(b'ARMOR_PIERCING'):
        if section.has_key(b'normalizationAngle'):
            localShellType.normalizationAngle = radians(_xml.readNonNegativeFloat(xmlCtx, section, b'normalizationAngle'))
        if section.has_key(b'ricochetAngle'):
            localShellType.ricochetAngleCos = cos(radians(_xml.readNonNegativeFloat(xmlCtx, section, b'ricochetAngle')))
        if section.has_key(b'enableTraceRicochet'):
            localShellType.enableTraceRicochet = _xml.readBool(xmlCtx, section, b'enableTraceRicochet')
    elif kind == b'HOLLOW_CHARGE':
        if section.has_key(b'piercingPowerLossFactorByDistance'):
            localShellType.piercingPowerLossFactorByDistance = 10.0 * _xml.readNonNegativeFloat(xmlCtx, section, b'piercingPowerLossFactorByDistance')
        if section.has_key(b'ricochetAngle'):
            localShellType.ricochetAngleCos = cos(radians(_xml.readNonNegativeFloat(xmlCtx, section, b'ricochetAngle')))
        if section.has_key(b'enableTraceRicochet'):
            localShellType.enableTraceRicochet = _xml.readBool(xmlCtx, section, b'enableTraceRicochet')
    if kind == b'HIGH_EXPLOSIVE':
        if isModernHighExplosive:
            if section.has_key(b'obstaclePenetration'):
                localShellType.obstaclePenetration = _xml.readBool(xmlCtx, section, b'obstaclePenetration')
            if section.has_key(b'shieldPenetration'):
                localShellType.shieldPenetration = _xml.readBool(xmlCtx, section, b'shieldPenetration')
            if section.has_key(HighExplosiveImpact.BLAST_WAVE):
                localShellType.blastWave = _readImpactParamsLocal(xmlCtx, section, HighExplosiveImpact.BLAST_WAVE, originalShellType.blastWave)
            if section.has_key(HighExplosiveImpact.SHELL_FRAGMENTS):
                localShellType.shellFragments = _readImpactParamsLocal(xmlCtx, section, HighExplosiveImpact.SHELL_FRAGMENTS, originalShellType.shellFragments)
            if section.has_key(HighExplosiveImpact.ARMOR_SPALLS):
                localShellType.armorSpalls = _readImpactParamsLocal(xmlCtx, section, HighExplosiveImpact.ARMOR_SPALLS, originalShellType.armorSpalls)
            blastWave = localShellType.blastWave
            shellFragments = localShellType.shellFragments
            armorSpalls = localShellType.armorSpalls
            if not (blastWave.isActive or shellFragments.isActive or armorSpalls.isActive):
                _xml.raiseWrongXml(xmlCtx, b'', b'Modern high explosive shell must contain at least one damage mechanics: blastWave, shellFragments, armorSpalls')
            localShellType.maxDamage = max(max(shellFragments.armorDamage), max(shellFragments.deviceDamage), max(armorSpalls.armorDamage), max(armorSpalls.deviceDamage), max(blastWave.armorDamage), max(blastWave.deviceDamage))
        if section.has_key(b'explosionRadius'):
            localShellType.explosionRadius = cachedFloat(section.readFloat(b'explosionRadius'))
            if not isModernHighExplosive and localShellType.explosionRadius <= 0.0:
                localShellType.explosionRadius = cachedFloat(originalShell.caliber * originalShell.caliber / 5555.0)
        explosionSettings = (b'explosionDamageFactor', b'explosionDamageAbsorptionFactor', b'explosionEdgeDamageFactor', b'shellFragmentsDamageAbsorptionFactor')
        for f in explosionSettings:
            if section.has_key(f):
                factor = section.readFloat(f)
                if factor <= 0:
                    factor = g_cache.commonConfig[b'miscParams'][f]
                setattr(localShellType, f, factor)

        if localShellType.explosionEdgeDamageFactor > 1.0:
            _xml.raiseWrongXml(xmlCtx, b'explosionEdgeDamageFactor', b'explosionEdgeDamageFactor must be < 1')
    elif originalShellType.mechanics == SHELL_MECHANICS_TYPE.NON_PIERCING_DAMAGE:
        subXmlCtx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, b'nonPiercingDamage')
        if subsection and subsection.has_key(b'damage/armor'):
            localShellType.nonPiercingArmorDamage = _xml.readNonNegativeFloat(subXmlCtx, subsection, b'damage/armor')
    if section.has_key(b'damageRandomization'):
        localShell.damageRandomization = _xml.readNonNegativeFloat(xmlCtx, section, b'damageRandomization')
    if section.has_key(b'damageRandomizationType'):
        localShell.damageRandomizationType = _xml.readNonEmptyString(xmlCtx, section, b'damageRandomizationType')
    if section.has_key(b'piercingPowerRandomization'):
        localShell.piercingPowerRandomization = _xml.readNonNegativeFloat(xmlCtx, section, b'piercingPowerRandomization')
    if section.has_key(b'piercingPowerRandomizationType'):
        localShell.piercingPowerRandomizationType = _xml.readNonEmptyString(xmlCtx, section, b'piercingPowerRandomizationType')
    if section.has_key(b'hasStun'):
        hasStun = section.readBool(b'hasStun')
        if hasStun:
            stunParams = gun_readers.readStunParams(section, xmlCtx)
            if originalShell.stun is None:
                if stunParams.get(b'stunRadius') is not None:
                    stun = shell_components.Stun(**stunParams)
                elif kind == b'HIGH_EXPLOSIVE':
                    stunParams[b'stunRadius'] = localShellType.explosionRadius
                    stun = shell_components.Stun(**stunParams)
                else:
                    _xml.raiseWrongXml(xmlCtx, b'stunRadius', b'hasStun = true, but neither explosionRadius nor stunRadius defined')
            else:
                stun = copy.copy(originalShell.stun)
                for k, v in viewitems(stunParams):
                    setattr(stun, k, v)

        else:
            stun = None
        localShell.stun = stun
    if section.has_key(b'chanceToHitByProjectileModifier'):
        localShell.chanceToHitByProjectileModifier = _xml.readFloat(xmlCtx, section, b'chanceToHitByProjectileModifier')
    if section.has_key(b'effects'):
        effName = _xml.readNonEmptyString(xmlCtx, section, b'effects')
        effIdx = g_cache.shotEffectsIndexes.get(effName, component_constants.INVALID_EFFECT_INDEX)
        localShell.effectsIndex = effIdx
    localShell.type = localShellType
    return localShell


_shellKinds = (
 SHELL_TYPES.HOLLOW_CHARGE, SHELL_TYPES.HIGH_EXPLOSIVE,
 SHELL_TYPES.ARMOR_PIERCING, SHELL_TYPES.ARMOR_PIERCING_HE, SHELL_TYPES.ARMOR_PIERCING_CR, SHELL_TYPES.SMOKE)

def _readShot(xmlCtx, section, nationID):
    shellName = section.name
    shellID = g_cache.shellIDs(nationID).get(shellName)
    if shellID is None:
        _xml.raiseWrongXml(xmlCtx, b'', b'unknown shell type name')
    shellDescr = g_cache.shells(nationID)[shellID]
    defaultPortion = component_constants.ZERO_FLOAT
    if section.has_key(b'defaultPortion'):
        defaultPortion = _xml.readFraction(xmlCtx, section, b'defaultPortion')
    if IS_CLIENT or IS_WEB:
        defaultPortion = ceilTo(defaultPortion, decimals=-3, epsilon=1e-06)
    projectileSpeedFactor = g_cache.commonConfig[b'miscParams'][b'projectileSpeedFactor']
    shot = gun_components.GunShot(shellDescr, defaultPortion, shared_readers.readFloatPair(xmlCtx, section, b'piercingPower'), _xml.readPositiveFloat(xmlCtx, section, b'speed') * projectileSpeedFactor, _xml.readNonNegativeFloat(xmlCtx, section, b'gravity') * projectileSpeedFactor ** 2, _xml.readPositiveFloat(xmlCtx, section, b'maxDistance'), _xml.readFloat(xmlCtx, section, b'maxHeight', 1000000.0))
    if not IS_UE_EDITOR:
        from helpers_common import computeShotMaxDistance
        shot.maxDistance = computeShotMaxDistance(shot)
    return shot


def _readShotLocal(xmlCtx, section, originalShot):
    shellName = originalShot.shell.name
    shotCtx, shotSection = _xml.getSubSectionWithContext(xmlCtx, section, shellName, throwIfMissing=False)
    if not shotSection:
        return originalShot
    localShot = copy.copy(originalShot)
    localShot.shell = _readShellLocal(shotCtx, shotSection, originalShot.shell)
    projectileSpeedFactor = g_cache.commonConfig[b'miscParams'][b'projectileSpeedFactor']
    if shotSection.has_key(b'piercingPower'):
        localShot.piercingPower = shared_readers.readFloatPair(shotCtx, shotSection, b'piercingPower')
    if shotSection.has_key(b'speed'):
        localShot.speed = _xml.readPositiveFloat(shotCtx, shotSection, b'speed') * projectileSpeedFactor
    if shotSection.has_key(b'gravity'):
        localShot.gravity = _xml.readNonNegativeFloat(shotCtx, shotSection, b'gravity') * projectileSpeedFactor ** 2
    if shotSection.has_key(b'maxDistance'):
        maxDistance = _xml.readPositiveFloat(shotCtx, shotSection, b'maxDistance')
        localShot.maxDistance = maxDistance
        localShot.nominalMaxDistance = maxDistance
    if shotSection.has_key(b'maxHeight'):
        localShot.maxHeight = _xml.readFloat(shotCtx, shotSection, b'maxHeight', 1000000.0)
    if not IS_UE_EDITOR:
        from helpers_common import computeShotMaxDistance
        localShot.maxDistance = computeShotMaxDistance(localShot)
    return localShot


def readProtectedModules(xmlCtx, section, subsection):
    moduleKind = g_cache.moduleKind
    protectModules = set()
    allValidModules = moduleKind[ModuleKind.EXTERNAL].union(moduleKind[ModuleKind.INTERNAL], moduleKind[ModuleKind.TANKMEN])
    protectFromHits = _xml.readString(xmlCtx, section, subsection).split()
    for module in protectFromHits:
        moduleID = IDS_BY_NAMES.get(module)
        if module in moduleKind:
            protectModules = protectModules.union(moduleKind[module])
        elif moduleID not in allValidModules:
            _xml.raiseWrongXml(xmlCtx, section, b'wrong material type')
        else:
            protectModules.add(moduleID)

    return protectModules


def _defaultLocalReader(xmlCtx, section, sharedItem, unlocksDescrs, parentItem=None):
    if not section.has_key(b'unlocks'):
        return sharedItem
    descr = sharedItem.copy()
    descr.unlocks = _readUnlocks(xmlCtx, section, b'unlocks', unlocksDescrs, sharedItem.compactDescr)
    return descr


def _readGunShotDispersionFactors(xmlCtx, section, subsectionName):
    res = {b'turretRotation': (_xml.readNonNegativeFloat(xmlCtx, section, subsectionName + b'/turretRotation') / radians(1.0)), 
       b'afterShot': (_xml.readNonNegativeFloat(xmlCtx, section, subsectionName + b'/afterShot')), 
       b'whileGunDamaged': (_xml.readNonNegativeFloat(xmlCtx, section, subsectionName + b'/whileGunDamaged'))}
    name = subsectionName + b'/afterShotInBurst'
    if section.has_key(name):
        res[b'afterShotInBurst'] = _xml.readNonNegativeFloat(xmlCtx, section, name)
    else:
        res[b'afterShotInBurst'] = res[b'afterShot']
    return res


def _readArmor(xmlCtx, section, subsectionName, optional=False, index=0):
    res = {}
    if IS_BASEAPP:
        return res
    else:
        if IS_BOT:
            return res
        defMaterials = g_cache.commonConfig[b'materials']
        autoDamageKindMaterials = g_cache.commonConfig[b'_autoDamageKindMaterials']
        matKindIDsByNames = material_kinds.IDS_BY_NAMES
        section = _xml.getSubsection(xmlCtx, section, subsectionName, not optional)
        if not section and optional:
            return res
        xmlCtx = (
         xmlCtx, subsectionName)
        for matKindName, matKindSection in section.items():
            materialKind = matKindIDsByNames.get(matKindName)
            if materialKind is None:
                _xml.raiseWrongXml(xmlCtx, matKindName, b'material kind name is unknown')
            defMatInfo = defMaterials.get(materialKind)
            if defMatInfo is None:
                _xml.raiseWrongXml(xmlCtx, matKindName, b'material kind is not useable on vehicle')
            vals = defMatInfo._asdict()
            vals[b'armor'] = _xml.readNonNegativeFloat(xmlCtx, section, matKindName)
            isDevice = vals[b'extra'] is not None
            damageKind = None if materialKind in autoDamageKindMaterials else vals[b'damageKind']
            if defMatInfo.multipleExtra:
                vals[b'extra'] = defMatInfo.extra.format(index)
            ctx = (xmlCtx, matKindName)
            for paramName in matKindSection.keys():
                if paramName in _g_boolMatInfoParams:
                    vals[paramName] = _xml.readBool(ctx, matKindSection, paramName)
                elif paramName == b'vehicleDamageFactor':
                    vals[paramName] = _xml.readFraction(ctx, matKindSection, paramName)
                elif isDevice and paramName in (b'chanceToHitByProjectile', b'chanceToHitByExplosion'):
                    vals[paramName] = _xml.readFraction(ctx, matKindSection, paramName)
                elif paramName == b'damageKind':
                    damageKindName = _xml.readString(ctx, matKindSection, b'damageKind')
                    if damageKindName == b'armor':
                        damageKind = 0
                    elif damageKindName == b'device':
                        damageKind = 1
                    elif damageKindName == b'auto':
                        damageKind = None
                    else:
                        _xml.raiseWrongXml(ctx, b'damageKind', b'wrong damage kind name')
                    if damageKind is not None:
                        vals[b'damageKind'] = damageKind
                elif paramName == b'tags':
                    tags = _xml.readStringOrEmpty(xmlCtx, matKindSection, paramName)
                    vals[paramName] = frozenset(tags.split(b' '))
                else:
                    _xml.raiseWrongXml(ctx, paramName, b'unknown parameter')

            if damageKind is None:
                damageKind = 0 if vals[b'armor'] else 1
                vals[b'damageKind'] = damageKind
            res[materialKind] = shared_components.MaterialInfo(**vals)

        if IS_UE_EDITOR:
            for kind, matInfo in defMaterials.items():
                if kind not in res.keys():
                    vals = matInfo._asdict()
                    if vals[b'armor'] is None:
                        vals[b'armor'] = -1.0
                    else:
                        vals[b'armor'] = 0.0
                    if matInfo.multipleExtra:
                        vals[b'extra'] = matInfo.extra.format(index)
                    res[kind] = shared_components.MaterialInfo(**vals)

        return res


def _writeArmor(armor, section, materialData, primaryArmor=None):
    if not armor or materialData is None:
        return
    armorSection = section[b'armor'] if section.has_key(b'armor') else section.createSection(b'armor')
    for childSection in armorSection.values():
        armorSection.deleteSection(childSection)

    materials = g_cache.commonConfig[b'materials']
    if primaryArmor is not None:
        for matKind in primaryArmor:
            if matKind not in materialData:
                materialData.append(matKind)

    unknownMatKinds = []
    for matKind in materialData:
        if matKind not in material_kinds.NAMES_BY_IDS:
            LOG_ERROR((b"ignoring unknown material kind '{}'").format(matKind))
            unknownMatKinds.append(matKind)

    materialData = [matKind for matKind in materialData if matKind not in unknownMatKinds]

    def materialSortKey(materialID):
        matName = material_kinds.NAMES_BY_IDS.get(materialID)
        return (b'armor' not in matName, materialID)

    materialData = sorted(materialData, key=materialSortKey)
    exceptions = [
     b'wheel']
    for matKind in materialData:
        defMatInfo = materials.get(matKind)._asdict()
        matKindName = material_kinds.NAMES_BY_IDS.get(matKind)
        matInfo = armor[matKind]
        hasChanges = matKindName in exceptions or matInfo.vehicleDamageFactor != defMatInfo[b'vehicleDamageFactor'] or matInfo.chanceToHitByProjectile != defMatInfo[b'chanceToHitByProjectile'] or matInfo.chanceToHitByExplosion != defMatInfo[b'chanceToHitByExplosion']
        defaultArmor = defMatInfo[b'armor'] if defMatInfo[b'armor'] is not None else -1.0
        _xml.rewriteFloat(armorSection, matKindName, matInfo.armor, None if hasChanges else defaultArmor)
        _xml.rewriteFloat(armorSection, matKindName + b'/vehicleDamageFactor', matInfo.vehicleDamageFactor, defMatInfo[b'vehicleDamageFactor'])
        _xml.rewriteFloat(armorSection, matKindName + b'/chanceToHitByProjectile', matInfo.chanceToHitByProjectile, defMatInfo[b'chanceToHitByProjectile'])
        _xml.rewriteFloat(armorSection, matKindName + b'/chanceToHitByExplosion', matInfo.chanceToHitByExplosion, defMatInfo[b'chanceToHitByExplosion'])
        _xml.rewriteString(armorSection, matKindName + b'/tags', (b' ').join(matInfo.tags), (b' ').join(defMatInfo[b'tags']))

    return


_g_boolMatInfoParams = (
 b'useArmorHomogenization', b'useHitAngle', b'useAntifragmentationLining', b'mayRicochet',
 b'collideOnceOnly', b'continueTraceIfNoHit', b'checkCaliberForRicochet', b'checkCaliberForHitAngleNorm')

def _readPrimaryArmor(xmlCtx, section, subsectionName, materials):
    if not section.has_key(subsectionName):
        return (
         materials.get(1, shared_components.DEFAULT_MATERIAL_INFO).armor,
         materials.get(3, shared_components.DEFAULT_MATERIAL_INFO).armor,
         materials.get(2, shared_components.DEFAULT_MATERIAL_INFO).armor)
    else:
        armorNames = section.readString(subsectionName).split()
        if len(armorNames) != 3:
            _xml.raiseWrongSection(xmlCtx, subsectionName)
        res = []
        matKindIDsByNames = material_kinds.IDS_BY_NAMES
        for matKindName in armorNames:
            materialKind = matKindIDsByNames.get(matKindName)
            if materialKind is None:
                _xml.raiseWrongXml(xmlCtx, subsectionName, b"unknown material kind name '%s'" % matKindName)
            res.append(materials.get(materialKind, shared_components.DEFAULT_MATERIAL_INFO).armor)

        return cachedFloatTuple(res)


def _readPrimaryArmorKinds(xmlCtx, section, subsectionName):
    armorNames = section.readString(subsectionName).split()
    res = []
    for matKindName in armorNames:
        materialKind = material_kinds.IDS_BY_NAMES.get(matKindName)
        if materialKind is None:
            _xml.raiseWrongXml(xmlCtx, subsectionName, b"unknown material kind name '%s'" % matKindName)
        res.append(materialKind)

    return res


def _readDamageByStaticsChances(xmlCtx, section, subsectionName):
    section = _xml.getSubsection(xmlCtx, section, subsectionName, False)
    if section is None:
        return g_cache.commonConfig[b'damageByStaticsChances']
    else:
        xmlCtx = (
         xmlCtx, subsectionName)
        res = copy.deepcopy(g_cache.commonConfig[b'damageByStaticsChances'])
        for subName in (b'tankman', b'module'):
            subsection = _xml.getSubsection(xmlCtx, section, subName, False)
            if subsection is not None:
                res[subName] = _xml.readFraction(xmlCtx, section, subName)

        return res


def _readFakeTurretIndices(xmlCtx, section, subsectionName, numTurrets):
    res = _xml.readTupleOfInts(xmlCtx, section, subsectionName)
    for idx in res:
        if not 0 <= idx < numTurrets:
            _xml.raiseWrongSection(xmlCtx, subsectionName)

    return res


def _readCustomizableAreas(xmlCtx, section, subsectionName):
    res = {b'paint': [], b'camouflage': []}
    paintString = camouflageString = None
    customization = _xml.getSubsection(xmlCtx, section, subsectionName, throwIfMissing=False)
    if customization is not None:
        customizableVehicleAreas = _xml.getSubsection(xmlCtx, customization, b'customizableVehicleAreas')
        paintString = _xml.readStringOrNone(xmlCtx, customizableVehicleAreas, b'paint')
        camouflageString = _xml.readStringOrNone(xmlCtx, customizableVehicleAreas, b'camouflage')
        res[b'paint'] = decodeEnum(paintString, ApplyArea)
        res[b'camouflage'] = decodeEnum(camouflageString, ApplyArea)
    if IS_UE_EDITOR:
        res[b'paintString'] = paintString if paintString is not None else b''
        res[b'camouflageString'] = camouflageString if camouflageString is not None else b''
    return res


def _writeCustomizableAreas(cItems, section):
    subsectionName = b'customization'
    _xml.rewriteString(section, subsectionName + b'/customizableVehicleAreas/paint', cItems[b'paintString'])
    _xml.rewriteString(section, subsectionName + b'/customizableVehicleAreas/camouflage', cItems[b'camouflageString'])
    return


def _writeDualGun(item, section):
    if not section.has_key(b'dualGun') or item.dualGun is None or item.dualGun is component_constants.DEFAULT_GUN_DUALGUN:
        return
    subSection = section[b'dualGun']
    _xml.rewriteFloat(subSection, b'chargeTime', item.dualGun.chargeTime)
    _xml.rewriteInt(subSection, b'shootImpulse', item.dualGun.shootImpulse)
    _xml.rewriteFloat(subSection, b'reloadLockTime', item.dualGun.reloadLockTime)
    reloadTimes = Vector2(item.dualGun.reloadTimes[0], item.dualGun.reloadTimes[1])
    _xml.rewriteVector2(subSection, b'reloadTimes', reloadTimes)
    _xml.rewriteFloat(subSection, b'rateTime', item.dualGun.rateTime)
    _xml.rewriteFloat(subSection, b'chargeThreshold', item.dualGun.chargeThreshold)
    _xml.rewriteFloat(subSection, b'afterShotDelay', item.dualGun.afterShotDelay)
    _xml.rewriteFloat(subSection, b'preChargeIndication', item.dualGun.preChargeIndication)
    _xml.rewriteFloat(subSection, b'chargeCancelTime', item.dualGun.chargeCancelTime, 0.2)
    return


def _writeSecondaryGunPrefabs(item, section):
    sectionIndex = section.getFirstIndex(b'prefabs')
    section.deleteSection(b'prefabs')
    prefabs = item.prefabs
    if prefabs is None or len(prefabs) == 0:
        return
    needToWrite = False
    for k, v in prefabs.items():
        for kk, vv in v.items():
            if len(vv) > 0:
                needToWrite = True
                break

        if needToWrite is True:
            break

    if needToWrite is False:
        return
    else:
        subSection = section.insertSection(b'prefabs', sectionIndex)
        hasSets = False
        for k, v in prefabs.items():
            if k == b'default':
                for kk, vv in v.items():
                    if len(vv) > 0:
                        _xml.rewriteString(subSection, kk, vv[0])

            else:
                hasSets = True

        if hasSets is False:
            return
        setsSection = subSection.createSection(b'sets')
        for k, v in prefabs.items():
            if k == b'default':
                continue
            setSubSection = setsSection.createSection(k)
            for kk, vv in v.items():
                if len(vv) > 0:
                    _xml.rewriteString(setSubSection, kk, vv[0])

        return


def _writeMechanicsSecondaryGun(mechanic, section):
    _xml.rewriteFloat(section, b'initiationTime', mechanic.initiationTime)
    _xml.rewriteBool(section, b'dependentOnMainGun', mechanic.dependentOnMainGun)
    return


def _writeMechanics(item, section):
    section.deleteSection(b'mechanics')
    mechanics = item.mechanicsParams
    if mechanics is None or len(mechanics) == 0:
        return
    mechanicsSection = section.createSection(b'mechanics')
    for name, mechanic in mechanics.items():
        subMechanicSection = mechanicsSection.createSection(name)
        _writeMechanicsSecondaryGun(mechanic, subMechanicSection)

    return


def _readHitTester(xmlCtx, section, subsectionName, optional=False):
    if IS_BASEAPP or IS_WEB or IS_PROCESS_REPLAY or IS_COMMON_ENV:
        return
    subsection = _xml.getSubsection(xmlCtx, section, subsectionName, throwIfMissing=False) if subsectionName else section
    if subsection is None:
        if optional:
            return
        _xml.raiseWrongSection(xmlCtx, subsectionName)
        return
    else:
        try:
            htManager = HitTesterManager(subsection)
            if IS_CELLAPP or IS_UE_EDITOR:
                htManager.loadHitTesters()
            return htManager
        except Exception as x:
            LOG_CURRENT_EXCEPTION()
            _xml.raiseWrongXml(xmlCtx, subsectionName, str(x))
            return

        return


def _writeHitTester(hitTesterManager, xmlCtx, section, subsectionName):
    if not hitTesterManager:
        return
    subsection = _xml.getSubsection(xmlCtx, section, subsectionName)
    if not subsection:
        _xml.raiseWrongXml(xmlCtx, subsectionName, b"can't write hittester")
    hitTesterManager.save(subsection)
    return


def _readCrew(xmlCtx, section, subsectionName):
    section = _xml.getSubsection(xmlCtx, section, subsectionName)
    xmlCtx = (xmlCtx, subsectionName)
    res = []
    skillCounts = {}
    for skillName, subsection in section.items():
        skillName = intern(skillName)
        if skillName not in skills_constants.ROLES:
            _xml.raiseWrongXml(xmlCtx, skillName, b'wrong skill name')
        skills = (skillName,)
        for subskillName in subsection.asString.split():
            subskillName = intern(subskillName)
            if subskillName not in skills_constants.ROLES or subskillName in (skillName, b'commander'):
                _xml.raiseWrongXml(xmlCtx, skillName, b"wrong sub-skill name '%s'" % subskillName)
            skills = skills + (subskillName,)

        res.append(skills)
        for skillItemName in skills:
            skillCounts[skillItemName] = skillCounts.get(skillItemName, 0) + 1

    if len(skillCounts) != len(skills_constants.ROLES):
        _xml.raiseWrongXml(xmlCtx, b'', b'missing crew roles: ' + str(tuple(skills_constants.ROLES.difference(viewkeys(skillCounts)))))
    for role, limit in viewitems(skills_constants.ROLE_LIMITS):
        if skillCounts[role] > limit:
            _xml.raiseWrongXml(xmlCtx, b'', b'more than one %s in crew' % role)

    return tuple(res)


def _readPriceForItem(xmlCtx, section, compactDescr, prices=None):
    pricesDest = prices if prices is not None else _g_prices
    if pricesDest is not None:
        pricesDest[b'itemPrices'][compactDescr] = _xml.readPrice(xmlCtx, section, b'price')
        if section.readBool(b'notInShop', False):
            pricesDest[b'notInShopItems'].add(compactDescr)
    return


def _readPriceForOperation(xmlCtx, section, opType, opKey):
    pricesDest = _g_prices
    if pricesDest is not None:
        pricesDest[b'operationPrices'].setdefault(opType, {})[opKey] = _xml.readPrice(xmlCtx, section, b'price')
    return


def _readPriceForProgressionLvl(compactDescr, lvls):
    pricesDest = _g_prices
    if pricesDest is not None:
        itemprices = ItemsPrices()
        notInShopItems = set()
        for num, lvl in viewitems(lvls):
            if lvl is not None:
                price = lvl.get(b'price')
                notInShop = lvl.get(b'notInShop')
                if price:
                    itemprices[num] = price
                if notInShop:
                    notInShopItems.add(num)

        if itemprices:
            pricesDest[b'progressionLvlPrices'][compactDescr] = itemprices
        if notInShopItems:
            pricesDest[b'notInShopProgressionLvlItems'][compactDescr] = notInShopItems
    return


def _copyPriceForItem(sourceCompactDescr, destCompactDescr, itemNotInShop):
    pricesDest = _g_prices
    if pricesDest is not None:
        pricesDest[b'itemPrices'][destCompactDescr] = pricesDest[b'itemPrices'].getPrices(sourceCompactDescr)
        if itemNotInShop or sourceCompactDescr in pricesDest[b'notInShopItems']:
            pricesDest[b'notInShopItems'].add(destCompactDescr)
    return


def getPriceForItemDescr(itemDescr):
    pricesDest = _g_prices
    priceInfo = tuple()
    if pricesDest is not None:
        price = pricesDest[b'itemPrices'].getPrices(itemDescr)
        notInShop = itemDescr in pricesDest[b'notInShopItems']
        priceInfo = (price, notInShop)
    return priceInfo


def _readUnlocks(xmlCtx, section, subsectionName, unlocksDescrs, *requiredItems):
    if unlocksDescrs is None:
        return []
    else:
        s = section[subsectionName]
        if s is None or len(s) == 0:
            return []
        idxs = []
        for s in s.values():
            ctx = (
             xmlCtx, subsectionName + b'/' + s.name)
            itemTypeName = _itemTypeNameMap.get(s.name)
            if itemTypeName is None:
                _xml.raiseWrongXml(ctx, b'', b'unknown item type')
            itemName = s.asString
            if not itemName:
                _xml.raiseWrongXml(ctx, b'', b'item name is missing')
            xpCost = _xml.readInt(ctx, s, b'cost', 0)
            idxs.append(len(unlocksDescrs))
            unlocksDescrs.append((xpCost, itemTypeName, itemName) + requiredItems)

        return idxs


_itemTypeNameMap = {b'vehicle': b'vehicle', 
   b'chassis': b'vehicleChassis', b'turret': b'vehicleTurret', b'gun': b'vehicleGun', b'engine': b'vehicleEngine', 
   b'fuelTank': b'vehicleFuelTank', b'radio': b'vehicleRadio'}

def __readEffectsTimeLine(xmlCtx, section):
    try:
        effectsTimeLine = EffectsList.effectsFromSection(section)
    except Exception as x:
        _xml.raiseWrongXml(xmlCtx, section.name, str(x))

    return EffectsList.EffectsTimeLinePrereqs(effectsTimeLine.keyPoints, effectsTimeLine.effectsList, set())


def _readEffectGroups(xmlPath, withSubgroups=False):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    res = __readEffectGroupsFromSection(section, xmlCtx, withSubgroups)
    ResMgr.purge(xmlPath, True)
    return res


def __readEffectGroupsFromSection(section, xmlCtx, withSubgroups=False):
    res = {}
    for sname, subsection in section.items():
        if sname in (b'xmlns:xmlref',):
            continue
        sname = intern(sname)
        if withSubgroups:
            res[sname] = [__readEffectsTimeLine((xmlCtx, sname + b'/' + subgroupName), subgroupSection) for subgroupName, subgroupSection in subsection.items()]
        else:
            res[sname] = __readEffectsTimeLine((xmlCtx, sname), subsection)

    return res


def _readPrefabEffect(xmlCtx, section, subSectionName, default):
    prefabEffName = _xml.readStringOrNone(xmlCtx, section, subSectionName)
    if prefabEffName is None:
        return default
    else:
        return prefabEffName


def _readDrivenJoints(xmlCtx, section, subsectionName):

    def readOneSection(xmlCtx, section, subsectionName):
        result = []
        for sname, subsection in _xml.getChildren(xmlCtx, section, subsectionName):
            if sname == b'sets':
                continue
            ctx = (
             xmlCtx, sname)
            masterNode = _xml.readNonEmptyString(ctx, subsection, b'node')
            fulltable = []
            masterTable = [
             masterNode]
            for rowValue in subsection[b'table'].values():
                masterTable.append(radians(rowValue.asFloat))

            fulltable.append(masterTable)
            for subsectionValue in subsection[b'slaves'].values():
                slaveNode = _xml.readString(ctx, subsectionValue, b'node')
                table = [
                 slaveNode]
                for rowValue in subsectionValue[b'table'].values():
                    table.append(radians(rowValue.asFloat))

                fulltable.append(table)

            result.append(fulltable)

        return result

    drivenJoints = {}
    drivenJointsSection = _xml.getSubsection(xmlCtx, section, subsectionName)
    defaultSection = readOneSection(xmlCtx, section, subsectionName)
    if defaultSection:
        drivenJoints[b'default'] = defaultSection
    if drivenJointsSection.has_key(b'sets'):
        drivenJointsSetsSection = _xml.getSubsection(xmlCtx, drivenJointsSection, b'sets')
        for sname in drivenJointsSetsSection.keys():
            drivenJoints[sname] = readOneSection(xmlCtx, drivenJointsSetsSection, sname)

    return drivenJoints


def _writeDrivenJoints(newItems, section, subsectionName):

    def getSubsection(section, subsectionName):
        if not section.has_key(subsectionName):
            subsection = section.createSection(subsectionName)
        else:
            subsection = section[subsectionName]
        return subsection

    def createSingleSection(section, subsection):
        for i in xrange(len(section)):
            record = section[i]
            recordSection = createOrTake(subsection, i, b'master')
            slavesSection = None
            for j in xrange(len(record)):
                table = record[j]
                if j == 0:
                    tableSection = recordSection
                else:
                    slavesSection = createOrTake(recordSection, 0, b'slaves')
                    tableSection = createOrTake(slavesSection, j - 1, b'slave')
                _xml.rewriteString(tableSection, b'node', table[0])
                rowsSection = createOrTake(tableSection, 0, b'table')
                for k in xrange(1, len(table)):
                    row = degrees(table[k])
                    rowSection = createOrTake(rowsSection, k - 1, b'row')
                    rowSection.asFloat = row

                rows = rowsSection.values()
                for k in xrange(len(table) - 1, len(rows)):
                    rowsSection.deleteSection(rows[k])

            if slavesSection:
                children = slavesSection.values()
                for j in xrange(len(record) - 1, len(children)):
                    slavesSection.deleteSection(children[j])

        masters = subsection.values()
        for i in xrange(len(section), len(masters)):
            subsection.deleteSection(masters[i])

        return

    def createOrTake(section, id, subsectionName):
        if not section.has_key(subsectionName):
            return section.createSection(subsectionName)
        children = section.values()
        curMatch = 0
        for child in children:
            if child.name == subsectionName:
                if curMatch == id:
                    return child
                curMatch += 1

        return section.createSection(subsectionName)

    def equal(left, right):
        if isinstance(left, list):
            if len(left) != len(right):
                return False
            for i in xrange(len(left)):
                if not equal(left[i], right[i]):
                    return False

            return True
        if isinstance(left, float):
            return abs(left - right) < 1e-08
        else:
            return left == right

        return

    if newItems is not None and len(newItems) > 0:
        subsection = getSubsection(section, subsectionName)
        default = []
        for key, value in newItems.items():
            if key == b'default':
                createSingleSection(value, subsection)
                default = value
                continue
            if value is None or equal(value, default):
                if subsection.has_key(b'sets'):
                    setSubsection = getSubsection(subsection, b'sets')
                    if setSubsection.has_key(key):
                        setSubsection.deleteSection(key)
                continue
            setSubsection = getSubsection(subsection, b'sets')
            skinSubsection = getSubsection(setSubsection, key)
            createSingleSection(value, skinSubsection)

    if section.has_key(subsectionName):
        subsection = getSubsection(section, subsectionName)
        if len(subsection.values()) == 0:
            section.deleteSection(subsectionName)
    return


def _readRecoilEffectGroups(xmlPath):
    res = {}
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    for sname, subsection in section.items():
        if sname in (b'xmlns:xmlref',):
            continue
        sname = intern(sname)
        ctx = (xmlCtx, sname)
        res[sname] = (_xml.readNonNegativeFloat(ctx, subsection, b'backoffTime'),
         _xml.readNonNegativeFloat(ctx, subsection, b'returnTime'))

    ResMgr.purge(xmlPath, True)
    return res


def __readReloadEffect(xmlCtx, section, parentSection):
    try:
        reloadEffect = ReloadEffect.effectFromSection(section, parentSection)
        return reloadEffect
    except Exception as x:
        _xml.raiseWrongXml(xmlCtx, section.name, str(x))
        return

    return


def _readReloadEffectGroups(xmlPath):
    res = {}
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    for sname, subsection in section.items():
        if sname in (b'xmlns:xmlref',):
            continue
        sname = intern(sname)
        ctx = (xmlCtx, sname)
        res[sname] = __readReloadEffect(ctx, subsection, section)

    ResMgr.purge(xmlPath, True)
    return res


def _readVehicleRoles(xmlPath):
    res = {}
    section = ResMgr.openSection(xmlPath)
    if not section:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read roles.xml')
    xmlCtx = (None, xmlPath)
    for roleName, subsection in section.items():
        roleType = ROLE_LABEL_TO_TYPE.get(roleName)
        if roleType is None:
            _xml.raiseWrongXml(xmlCtx, roleName, b'no role with such name (roles.xml)')
        if roleType in res:
            _xml.raiseWrongXml(xmlCtx, roleName, b'duplicated role name in roles.xml')
        ctx = (
         xmlCtx, roleName)
        actions = _xml.readNonEmptyString(ctx, subsection, b'actions')
        res[roleType] = tuple(ACTION_LABEL_TO_TYPE.get(label) for label in actions.split())

    return res


def _readChassisEffectGroups(xmlPath):
    res = {}
    section = ResMgr.openSection(xmlPath)
    if not section or section[b'particles'] is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    section = section[b'particles']
    xmlCtx = (
     None, xmlPath)
    for sname, subsection in section.items():
        sname = intern(sname)
        ctx = (xmlCtx, sname)
        effects = {}
        for matkindName, matkindSection in subsection.items():
            matkindName = intern(matkindName)
            if matkindName != b'default' and matkindName not in EFFECT_MATERIALS:
                _xml.raiseWrongXml(ctx, matkindName, b'unknown material kind')
            else:
                effectNames = []
                if len(matkindSection.keys()) > 0:
                    for side in (b'left', b'right', b'leftFront', b'rightFront'):
                        sideEffectName = _xml.readNonEmptyString((ctx, matkindName), matkindSection, side)
                        effectNames.append(intern(sideEffectName))

                else:
                    effectNames = _xml.readNonEmptyString((ctx, matkindName), matkindSection, b'')
                if matkindName == b'default':
                    effects[-1] = effectNames
                else:
                    effectIndex = material_kinds.EFFECT_MATERIAL_INDEXES_BY_NAMES[matkindName]
                    effects[effectIndex] = effectNames
            res[sname] = (
             effects, set())

        matkindSection = None

    section = None
    subsection = None
    ResMgr.purge(xmlPath, True)
    return res


def _readCustomEffectGroups(xmlPath):
    res = {}
    if IS_UE_EDITOR:
        xmlPath = xmlPath + b'!jit'
    section = ResMgr.openSection(xmlPath)
    try:
        defaultEffect = None
        if section is not None:
            SelectorDescFactory.initFactory(section)
            effectsSection = section[b'effects']
            for name, subsection in effectsSection.items():
                effect = CustomEffectsDescriptor(subsection)
                res[name] = effect
                if defaultEffect is None:
                    defaultEffect = effect

            if defaultEffect is not None:
                res[b'default'] = defaultEffect
            SelectorDescFactory.releseFactory()
    except Exception:
        LOG_CURRENT_EXCEPTION()

    ResMgr.purge(xmlPath, True)
    return res


def _readShotEffectGroups(xmlPath):
    res = ({}, [])
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    for sname, subsection in section.items():
        if sname in (b'xmlns:xmlref',):
            continue
        sname = intern(sname)
        ctx = (xmlCtx, sname)
        index = len(res[1])
        descr = {b'index': index}
        descr.update(_readShotEffects(ctx, subsection))
        if IS_CLIENT or IS_UE_EDITOR:
            descr[b'prereqs'] = set()
        res[0][sname] = index
        res[1].append(descr)

    section = None
    subsection = None
    ResMgr.purge(xmlPath, True)
    return res


def _readShotEffects(xmlCtx, section):
    res = {}
    res[b'targetStickers'] = {}
    v = section.readString(b'targetStickers/armorResisted')
    if not v:
        v = None
    else:
        v = g_cache.damageStickers[b'ids'].get(v)
        if v is None:
            _xml.raiseWrongXml(xmlCtx, b'targetStickers/armorResisted', b'unknown name of sticker')
    res[b'targetStickers'][b'armorResisted'] = v
    v = section.readString(b'targetStickers/armorPierced')
    if not v:
        v = None
    else:
        v = g_cache.damageStickers[b'ids'].get(v)
        if v is None:
            _xml.raiseWrongXml(xmlCtx, b'targetStickers/armorPierced', b'unknown name of sticker')
    res[b'targetStickers'][b'armorPierced'] = v
    if section.has_key(b'shotsCount'):
        res[b'shotsCount'] = _xml.readNonNegativeInt(xmlCtx, section, b'shotsCount')
    if IS_CLIENT or IS_UE_EDITOR:
        artillery = section.has_key(b'artillery')
        if artillery and IS_CLIENT:
            artillerySection = section[b'artillery']
            artilleryID = res[b'artilleryID'] = BigWorld.PyGroundEffectManager().loadArtillery(artillerySection)
            if pdc.isEnabled():
                _auxSerializingData[ARTILLERY_DATA].append((artillerySection, artilleryID))
        airstrike = section.has_key(b'airstrike')
        if airstrike and IS_CLIENT:
            airstrikeSection = section[b'airstrike']
            airstrikeID = res[b'airstrikeID'] = BigWorld.PyGroundEffectManager().loadAirstrike(airstrikeSection)
            if pdc.isEnabled():
                _auxSerializingData[AIRSTRIKE_DATA].append((airstrikeSection, airstrikeID))
        res[b'caliber'] = _xml.readNonNegativeFloat(xmlCtx, section, b'caliber')
        res[b'targetImpulse'] = _xml.readNonNegativeFloat(xmlCtx, section, b'targetImpulse')
        res[b'targetCameraSensitivity'] = _xml.readNonNegativeFloat(xmlCtx, section, b'targetCameraSensitivity', 1.0)
        res[b'physicsParams'] = {b'shellVelocity': (_xml.readNonNegativeFloat(xmlCtx, section, b'physicsParams/shellVelocity')), 
           b'shellMass': (_xml.readNonNegativeFloat(xmlCtx, section, b'physicsParams/shellMass')), 
           b'splashRadius': (_xml.readNonNegativeFloat(xmlCtx, section, b'physicsParams/splashRadius')), 
           b'splashStrength': (_xml.readNonNegativeFloat(xmlCtx, section, b'physicsParams/splashStrength'))}
        hitPrefabs = {}
        res[b'armorHit'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'armorHit'))
        hitPrefabs[b'armorHit'] = _xml.readStringOrEmpty(xmlCtx, section, b'armorHit/prefab')
        res[b'armorCriticalHit'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'armorCriticalHit'))
        hitPrefabs[b'armorCriticalHit'] = _xml.readStringOrEmpty(xmlCtx, section, b'armorCriticalHit/prefab')
        res[b'armorResisted'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'armorResisted'))
        hitPrefabs[b'armorResisted'] = _xml.readStringOrEmpty(xmlCtx, section, b'armorResisted/prefab')
        if section.has_key(b'armorSplashHit'):
            res[b'armorSplashHit'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'armorSplashHit'))
            hitPrefabs[b'armorSplashHit'] = _xml.readStringOrEmpty(xmlCtx, section, b'armorSplashHit/prefab')
        if not artillery and not airstrike:
            model = _xml.readNonEmptyString(xmlCtx, section, b'projectile/model')
            modelOwnShot = section.readString(b'projectile/modelOwnShot', model)
            subsection = _xml.getSubsection(xmlCtx, section, b'projectile/effects')
            try:
                effects = EffectsList.EffectsList(subsection)
            except Exception as x:
                _xml.raiseWrongXml(xmlCtx, b'projectile/effects', str(x))

            res[b'projectile'] = (
             model, modelOwnShot, effects)
            if section.has_key(b'projectile/rotationSpeed'):
                res[b'projectileRotationSpeed'] = _xml.readFloat(xmlCtx, section, b'projectile/rotationSpeed', 0.0)
            if not section.has_key(b'waterParams'):
                res[b'waterParams'] = (2.0, 4.0)
            else:
                res[b'waterParams'] = (
                 _xml.readPositiveFloat(xmlCtx, section, b'waterParams/shallowWaterDepth'),
                 _xml.readPositiveFloat(xmlCtx, section, b'waterParams/rippleDiameter'))
            if section.has_key(b'armorBasicRicochet'):
                res[b'armorBasicRicochet'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'armorBasicRicochet'))
                hitPrefabs[b'armorBasicRicochet'] = _xml.readStringOrEmpty(xmlCtx, section, b'armorBasicRicochet/prefab')
            else:
                res[b'armorBasicRicochet'] = res[b'armorResisted']
            if section.has_key(b'armorRicochet'):
                res[b'armorRicochet'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'armorRicochet'))
                hitPrefabs[b'armorRicochet'] = _xml.readStringOrEmpty(xmlCtx, section, b'armorRicochet/prefab')
            else:
                res[b'armorRicochet'] = res[b'armorResisted']
            defSubEffName = EFFECT_MATERIALS[0] + b'Hit'
            res[defSubEffName] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, defSubEffName))
            for subEffName in EFFECT_MATERIALS[1:]:
                subEffName += b'Hit'
                if section.has_key(subEffName):
                    res[subEffName] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, subEffName))
                else:
                    res[subEffName] = res[defSubEffName]

            if section.has_key(b'deepWaterHit'):
                res[b'deepWaterHit'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'deepWaterHit'))
                hitPrefabs[b'deepWaterHit'] = _xml.readStringOrEmpty(xmlCtx, section, b'deepWaterHit/prefab')
            if section.has_key(b'shallowWaterHit'):
                res[b'shallowWaterHit'] = __readEffectsTimeLine(xmlCtx, _xml.getSubsection(xmlCtx, section, b'shallowWaterHit'))
                hitPrefabs[b'shallowWaterHit'] = _xml.readStringOrEmpty(xmlCtx, section, b'shallowWaterHit/prefab')
            if not res.has_key(b'deepWaterHit'):
                v = res.get(b'shallowWaterHit')
                res[b'deepWaterHit'] = v if v else res[defSubEffName]
            if not res.has_key(b'shallowWaterHit'):
                res[b'shallowWaterHit'] = res[b'deepWaterHit']
            res[b'hitPrefabs'] = hitPrefabs
    return res


def _readDamageStickers(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    ids = {}
    descrs = []
    for sname, subsection in section.items():
        sname = intern(sname)
        if sname in (b'texture', b'xmlns:xmlref'):
            continue
        if ids.has_key(sname):
            _xml.raiseWrongXml(xmlCtx, sname, b'sticker name is not unique')
        ctx = (xmlCtx, sname)
        damageSticker = {}
        stickerID = len(descrs)
        damageSticker[b'priority'] = _xml.readInt(ctx, subsection, b'priority', 1)
        if IS_CLIENT:
            stickerID = _readAndRegisterDamageStickerTextureParams(ctx, subsection, sname, False)
            for i in xrange(1, 100):
                name = b'variant%d' % i
                if not subsection.has_key(name):
                    break
                stickerID = _readAndRegisterDamageStickerTextureParams(ctx, subsection[name], sname, True)

        damageSticker[b'id'] = stickerID
        ids[sname] = stickerID
        descrs.append(damageSticker)

    res = {b'descrs': descrs, b'ids': ids}
    section = None
    subsection = None
    ResMgr.purge(xmlPath, True)
    return res


def _readAndRegisterDamageStickerTextureParams(xmlCtx, section, stickerName, raiseError):
    if not section.has_key(b'texName'):
        if raiseError:
            _xml.raiseWrongXml(xmlCtx, section.name, b'texName for damage sticker is not specified')
        return
    texAM = _xml.readNonEmptyString(xmlCtx, section, b'texName')
    texNM = _xml.readNonEmptyString(xmlCtx, section, b'bumpTexName') if section.has_key(b'bumpTexName') else b''
    texGMM = _xml.readNonEmptyString(xmlCtx, section, b'smTexName') if section.has_key(b'smTexName') else b''
    randomYaw = True
    subsection = section[b'randomYaw']
    if subsection is not None:
        randomYaw = subsection.asBool
    variation = section.readFloat(b'variation', 0.0)
    v = _xml.readPositiveVector2(xmlCtx, section, b'modelSizes')
    modelSizes = v.tuple()
    result = BigWorld.wg_registerDamageSticker(stickerName, texAM, texNM, texGMM, modelSizes, variation, randomYaw)
    if pdc.isEnabled():
        _auxSerializingData[DAMAGE_STICKERS_DATA].append((
         (
          stickerName, texAM, texNM, texGMM, modelSizes, variation, randomYaw),
         result))
    return result


def _readCommonConfig(xmlCtx, section):
    res = {}
    res[b'miscParams'] = {b'projectileSpeedFactor': (_xml.readPositiveFloat(xmlCtx, section, b'miscParams/projectileSpeedFactor')), 
       b'minFireStartingDamage': (_xml.readNonNegativeFloat(xmlCtx, section, b'miscParams/minFireStartingDamage')), 
       b'explosionDamageFactor': (_xml.readNonNegativeFloat(xmlCtx, section, b'miscParams/explosionDamageFactor')), 
       b'explosionDamageAbsorptionFactor': (_xml.readNonNegativeFloat(xmlCtx, section, b'miscParams/explosionDamageAbsorptionFactor')), 
       b'explosionEdgeDamageFactor': (_xml.readNonNegativeFloat(xmlCtx, section, b'miscParams/explosionEdgeDamageFactor')), 
       b'shellFragmentsDamageAbsorptionFactor': (_xml.readNonNegativeFloat(xmlCtx, section, b'miscParams/shellFragmentsDamageAbsorptionFactor')), 
       b'allowMortarShooting': (_xml.readBool(xmlCtx, section, b'miscParams/allowMortarShooting')), 
       b'radarDefaults': {b'radarRadius': (_xml.readNonNegativeFloat(xmlCtx, section, b'miscParams/radarDefaults/radarRadius')), 
                          b'radarCooldown': (_xml.readNonNegativeFloat(xmlCtx, section, b'miscParams/radarDefaults/radarCooldown'))}}
    res[b'damageByStaticsChances'] = {b'tankman': (_xml.readFraction(xmlCtx, section, b'damageByStaticsChances/tankman')), 
       b'module': (_xml.readFraction(xmlCtx, section, b'damageByStaticsChances/module'))}
    res[b'defaultPrefabEffects'] = prefab_effects_readers.readDefaultPrefabEffects(xmlCtx, section, b'defaultPrefabEffects')
    if IS_CLIENT or IS_UE_EDITOR:
        v = {}
        for lodName in _xml.getSubsection(xmlCtx, section, b'lodLevels').keys():
            v[lodName] = _xml.readPositiveFloat(xmlCtx, section, b'lodLevels/' + lodName)

        res[b'lodLevels'] = v
        res[b'miscParams'][b'damageStickerAlpha'] = _xml.readPositiveFloat(xmlCtx, section, b'miscParams/damageStickerAlpha')
        name = _xml.readNonEmptyString(xmlCtx, section, b'miscParams/damageStickersLodDist')
        v = res[b'lodLevels'].get(name)
        if v is None:
            _xml.raiseWrongXml(xmlCtx, b'miscParams/damageStickersLodDist', b"unknown lod level '%s'" % name)
        res[b'miscParams'][b'damageStickersLodDist'] = v
        res[b'defaultDamagedStateGroup'] = _xml.readStringWithDefaultValue(xmlCtx, section, b'damagedStateGroup', b'medium')
        res[b'defaultVehicleEffects'] = _readVehicleEffects(xmlCtx, section, b'defaultVehicleEffects')
        res[b'defaultTurretDetachmentEffects'] = _readTurretDetachmentEffects(xmlCtx, section, b'defaultTurretDetachmentEffects')
        res[b'miscParams'][b'explosionCandleVolumes'] = [float(f) for f in _xml.readString(xmlCtx, section, b'miscParams/explosionCandleVolumes').split()]
    if IS_CLIENT or IS_UE_EDITOR or IS_CELLAPP:
        res[b'extras'], res[b'extrasDict'] = common_extras.readExtras(xmlCtx, section, b'extras', b'vehicle_extras')
        res[b'materials'], res[b'_autoDamageKindMaterials'] = _readMaterials(xmlCtx, section, b'materials', res[b'extrasDict'])
        res[b'deviceExtraIndexToTypeIndex'], res[b'tankmanExtraIndexToTypeIndex'] = _readDeviceTypes(xmlCtx, section, b'deviceExtras', res[b'extrasDict'])
        res[b'_devices'] = frozenset(res[b'extras'][idx] for idx in res[b'deviceExtraIndexToTypeIndex'])
        effectVelPath = b'miscParams/collisionEffectVelocities/'
        res[b'miscParams'][b'collisionEffectVelocities'] = {b'hull': (_xml.readVector2(xmlCtx, section, effectVelPath + b'hull')), 
           b'track': (_xml.readVector2(xmlCtx, section, effectVelPath + b'track')), 
           b'waterContact': (_xml.readVector2(xmlCtx, section, effectVelPath + b'waterContact')), 
           b'ramming': (_xml.readPositiveFloat(xmlCtx, section, effectVelPath + b'ramming'))}
    elif IS_WEB or IS_PROCESS_REPLAY or IS_COMMON_ENV:
        res[b'materials'], res[b'_autoDamageKindMaterials'] = _readMaterials(xmlCtx, section, b'materials', None)
    if IS_BOT:
        res[b'extras'], res[b'extrasDict'] = common_extras.readExtras(xmlCtx, section, b'extras', b'vehicle_extras')
        res[b'deviceExtraIndexToTypeIndex'], res[b'tankmanExtraIndexToTypeIndex'] = _readDeviceTypes(xmlCtx, section, b'deviceExtras', res[b'extrasDict'])
        res[b'_devices'] = frozenset(res[b'extras'][idx] for idx in res[b'deviceExtraIndexToTypeIndex'])
    return res


def _readDeviceTypes(xmlCtx, section, subsectionName, extrasDict):
    resDevices = {}
    resTankmen = {}
    for res, kindName, typeNames in ((resDevices, b'devices', VEHICLE_DEVICE_TYPE_NAMES),
     (
      resTankmen, b'tankmen', VEHICLE_TANKMAN_TYPE_NAMES)):
        kindSectionName = subsectionName + b'/' + kindName
        for extraName, subsection in _xml.getChildren(xmlCtx, section, kindSectionName):
            i = 0
            template = makeMultiExtraNameTemplate(extraName)
            extraInstanceName = template.format(i) if subsection.has_key(b'multiple') else extraName
            while extraInstanceName in extrasDict:
                try:
                    extra = extrasDict[extraInstanceName]
                    typeName = subsection.asString
                    if hasattr(extra, b'typeName'):
                        extra.typeName = typeName
                    res[extra.index] = typeNames.index(typeName)
                except Exception as x:
                    _xml.raiseWrongXml((xmlCtx, kindSectionName), extraName, str(x))

                i += 1
                extraInstanceName = template.format(i)

    return (
     resDevices, resTankmen)


def _readMaterials(xmlCtx, section, subsectionName, extrasDict):
    materials = {}
    autoDamageKindMaterials = set()
    for materialKindName, subsection in _xml.getChildren(xmlCtx, section, subsectionName):
        ctx = (xmlCtx, subsectionName + b'/' + materialKindName)
        materialKind = material_kinds.IDS_BY_NAMES.get(materialKindName)
        if materialKind is None:
            _xml.raiseWrongXml(ctx, b'', b'material kind name is unknown')
        extra = None
        multipleExtra = _xml.readBool(ctx, subsection, b'multiple', False)
        extraName = subsection.readString(b'extra')
        if extraName:
            extra = extrasDict.get(extraName) if extrasDict is not None and not multipleExtra else extraName
            if extra is None:
                _xml.raiseWrongXml(ctx, b'', b"unknown extra '%s'" % extraName)
        extraIsNone = extra is None
        damageKind = 0
        if not extraIsNone:
            damageKindName = _xml.readString(ctx, subsection, b'damageKind')
            if damageKindName == b'armor':
                damageKind = 0
            elif damageKindName == b'device':
                damageKind = 1
            elif damageKindName == b'auto':
                damageKind = 1
                autoDamageKindMaterials.add(materialKind)
            else:
                _xml.raiseWrongXml(ctx, b'damageKind', b'wrong damage kind name')
        materials[materialKind] = shared_components.MaterialInfo(kind=materialKind, armor=None if extraIsNone else 0, extra=extra if not multipleExtra else makeMultiExtraNameTemplate(extra), multipleExtra=multipleExtra, vehicleDamageFactor=_xml.readFraction(ctx, subsection, b'vehicleDamageFactor'), useArmorHomogenization=_xml.readBool(ctx, subsection, b'useArmorHomogenization'), useHitAngle=_xml.readBool(ctx, subsection, b'useHitAngle'), useAntifragmentationLining=_xml.readBool(ctx, subsection, b'useAntifragmentationLining'), mayRicochet=_xml.readBool(ctx, subsection, b'mayRicochet'), collideOnceOnly=_xml.readBool(ctx, subsection, b'collideOnceOnly'), checkCaliberForRicochet=_xml.readBool(ctx, subsection, b'checkCaliberForRicochet'), checkCaliberForHitAngleNorm=_xml.readBool(ctx, subsection, b'checkCaliberForHitAngleNorm'), damageKind=damageKind, chanceToHitByProjectile=1.0 if extraIsNone else _xml.readFraction(ctx, subsection, b'chanceToHitByProjectile'), chanceToHitByExplosion=1.0 if extraIsNone else _xml.readFraction(ctx, subsection, b'chanceToHitByExplosion'), continueTraceIfNoHit=True if extraIsNone else _xml.readBool(ctx, subsection, b'continueTraceIfNoHit'), tags=frozenset(_xml.readStringOrEmpty(ctx, subsection, b'tags').split()))

    return (
     materials, autoDamageKindMaterials)


g_artefacts_postload = []

def addArtefactsPostloadCallback(callback):
    g_artefacts_postload.append(callback)
    return


def processPostLoadArtefacts(objsByIDs, idsByNames):
    for callback in g_artefacts_postload:
        callback(objsByIDs, idsByNames)

    del g_artefacts_postload[:]
    return


def _readArtefacts(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    objsByIDs = {}
    idsByNames = {}
    for name, subsection in section.items():
        ctx = (
         xmlCtx, name)
        if name in (b'xmlns:xmlref',):
            continue
        name = intern(name)
        if name in idsByNames:
            _xml.raiseWrongXml(xmlCtx, name, b'name is not unique')
        classPath = _xml.readNonEmptyString(ctx, subsection, b'script')
        classObj = importClass(classPath, defaultMod=b'items.artefacts')
        if classObj is None:
            _xml.raiseWrongXml(ctx, b'script', b"Can't import %s" % classPath)
        instObj = classObj()
        instObj.init(ctx, subsection)
        _readPriceForItem(ctx, subsection, instObj.compactDescr)
        id = instObj.id[1]
        if id in objsByIDs:
            _xml.raiseWrongXml(ctx, b'', b'id is not unique')
        objsByIDs[id] = instObj
        idsByNames[name] = id

    ResMgr.purge(xmlPath, True)
    processPostLoadArtefacts(objsByIDs, idsByNames)
    return (
     objsByIDs, idsByNames)


def _joinCustomizationParams(nationID, commonDescr, customDescr):
    if not IS_CLIENT:
        if b'inscriptionColors' not in customDescr:
            if b'inscriptionColors' not in commonDescr:
                raise SoftException(b'inscriptionColors is not specified for nation=%s' % (
                 nations.NAMES[nationID],))
            customDescr[b'inscriptionColors'] = commonDescr[b'inscriptionColors']
    for name in (b'inscriptionGroups', b'inscriptions', b'camouflageGroups', b'camouflages'):
        intersection = set(commonDescr[name]).intersection(viewkeys(customDescr[name]))
        if intersection:
            raise SoftException(b'there is unexpected intersection in %s, %s (%s)' % (
             name, nationID, intersection))
        customDescr[name].update(commonDescr[name])

    return customDescr


def _readCustomization(xmlPath, nationID, idsRange):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    res = {}
    if not IS_CLIENT and section.has_key(b'inscriptionColors'):
        res[b'inscriptionColors'] = _readColors(xmlCtx, section, b'inscriptionColors', NUM_INSCRIPTION_COLORS)
    pricesDest = _g_prices
    if pricesDest is None:
        priceFactors = notInShops = None
    else:
        priceFactors = pricesDest[b'inscriptionGroupPriceFactors'][nationID]
        notInShops = pricesDest[b'notInShopInscriptionGroups'][nationID]
    res[b'inscriptionGroups'], res[b'inscriptions'] = _readPlayerInscriptions(xmlCtx, section, b'inscriptions', priceFactors, notInShops, idsRange)
    camouflageGroups = {}
    if not IS_CLIENT:
        for groupName, subsection in _xml.getChildren(xmlCtx, section, b'camouflageGroups'):
            groupName = intern(groupName)
            if groupName in camouflageGroups:
                _xml.raiseWrongXml(xmlCtx, b'camouflages/' + groupName, b'camouflage group name is not unique')
            groupDescr = {b'ids': []}
            if IS_WEB:
                groupDescr[b'userString'] = i18n.makeString(subsection.readString(b'userString'))
                groupDescr[b'hasNew'] = False
            groupDescr[b'igrType'] = _readIGRType(_xml, subsection)
            camouflageGroups[groupName] = groupDescr

    if pricesDest is None:
        priceFactors = notInShops = None
    else:
        priceFactors = pricesDest[b'camouflagePriceFactors'][nationID]
        notInShops = pricesDest[b'notInShopCamouflages'][nationID]
    camouflages = {}
    if not IS_CLIENT:
        for camName, subsection in _xml.getChildren(xmlCtx, section, b'camouflages'):
            ctx = (
             xmlCtx, b'camouflages/' + camName)
            camID, camDescr = _readCamouflage(ctx, subsection, camouflages, camouflageGroups, nationID, priceFactors, notInShops, idsRange)
            camDescr[b'name'] = camName
            camouflages[camID] = camDescr

    res[b'camouflageGroups'] = camouflageGroups
    res[b'camouflages'] = camouflages
    insigniaOnGun = {}
    for _, insigniaSubsection in _xml.getChildren(xmlCtx, section, b'insigniaOnGun'):
        rank = _xml.readInt(xmlCtx, insigniaSubsection, b'id', 0)
        textureName = _xml.readNonEmptyString(xmlCtx, insigniaSubsection, b'texName')
        bumpTextureName = insigniaSubsection[b'bumpTexName']
        bumpTextureName = bumpTextureName.asString if bumpTextureName is not None else b''
        insigniaOnGun[rank] = (textureName, bumpTextureName, False)

    res[b'insigniaOnGun'] = insigniaOnGun
    tintGroups = {}
    if section.has_key(b'tintGroup'):
        for tintName, subsection in _xml.getChildren(xmlCtx, section, b'tintGroup'):
            tintColor = _xml.readVector3(xmlCtx, subsection, b'color')
            tintGroups[tintName] = tintColor

        res[b'tintGroups'] = tintGroups
    section = None
    subsection = None
    ResMgr.purge(xmlPath, True)
    return res


def _readCamouflage(xmlCtx, section, ids, groups, nationID, priceFactors, notInShops, idsRange):
    id = _xml.readInt(xmlCtx, section, b'id', *idsRange)
    if id in ids:
        _xml.raiseWrongXml(xmlCtx, b'id', b'camouflage ID is not unique')
    kind = CAMOUFLAGE_KINDS.get(section.readString(b'kind'))
    if kind is None:
        _xml.raiseWrongSection(xmlCtx, b'kind')
    groupName = intern(_xml.readNonEmptyString(xmlCtx, section, b'group'))
    groupDescr = groups.get(groupName)
    if groupDescr is None:
        _xml.raiseWrongXml(xmlCtx, b'group', b"unknown camouflage group name '%s'" % groupName)
    if priceFactors is not None:
        priceFactors[id] = _xml.readNonNegativeFloat(xmlCtx, section, b'priceFactor')
        if section.readBool(b'notInShop', False):
            notInShops.add(id)
    camouflage = {b'kind': kind, b'igrType': (groupDescr[b'igrType']), 
       b'groupName': groupName, 
       b'invisibilityFactor': (_xml.readNonNegativeFloat(xmlCtx, section, b'invisibilityFactor')), 
       b'allow': (_readNationVehiclesByNames(xmlCtx, section, b'allow', nationID)), 
       b'deny': (_readNationVehiclesByNames(xmlCtx, section, b'deny', nationID)), 
       b'requiredToken': (section.readString(b'requiredToken', b''))}
    isNew = False
    if IS_CLIENT or IS_UE_EDITOR or IS_WEB:
        camouflage[b'description'] = section.readString(b'description')
        camouflage[b'texture'] = _xml.readNonEmptyString(xmlCtx, section, b'texture')
        camouflage[b'colors'] = _readColors(xmlCtx, section, b'colors', 4)
    if IS_CLIENT or IS_UE_EDITOR:
        isNew = section.readBool(b'isNew', False)
        camouflage[b'isNew'] = isNew
        if IS_UE_EDITOR:
            camouflage[b'tiling'], camouflage[b'tilingName'] = _readCamouflageTilings(xmlCtx, section, b'tiling', nationID)
        else:
            camouflage[b'tiling'] = _readCamouflageTilings(xmlCtx, section, b'tiling', nationID)
        camouflage[b'tilingSettings'] = _readCamouflageTilingSettings(xmlCtx, section)
    groupDescr[b'ids'].append(id)
    if isNew:
        groupDescr[b'hasNew'] = True
    tags = _xml.readStringOrNone(xmlCtx, section, b'tags')
    camouflage[b'tags'] = frozenset() if tags is None else frozenset(tags.split())
    return (
     id, camouflage)


def _writeCamouflageSettings(section, sectionName, camouflage):
    defaultCamouflage = shared_components.DEFAULT_CAMOUFLAGE
    if camouflage.tiling is not None and len(camouflage.tiling) == 4:
        value = Math.Vector4(camouflage.tiling[0], camouflage.tiling[1], camouflage.tiling[2], camouflage.tiling[3])
        defaultValue = Math.Vector4(defaultCamouflage.tiling[0], defaultCamouflage.tiling[1], defaultCamouflage.tiling[2], defaultCamouflage.tiling[3])
        _xml.rewriteVector4(section, sectionName + b'/tiling', value, defaultValue)
    if camouflage.exclusionMask is not None:
        _xml.rewriteString(section, sectionName + b'/exclusionMask', camouflage.exclusionMask, defaultCamouflage.exclusionMask)
    if camouflage.density is not None and len(camouflage.density) == 2:
        value = Math.Vector2(camouflage.density[0], camouflage.density[1])
        defaultValue = Math.Vector2(defaultCamouflage.density[0], defaultCamouflage.density[1])
        _xml.rewriteVector2(section, sectionName + b'/density', value, defaultValue)
    if camouflage.aoTextureSize is not None and len(camouflage.aoTextureSize) == 2:
        value = Math.Vector2(camouflage.aoTextureSize[0], camouflage.aoTextureSize[1])
        defaultValue = Math.Vector2(defaultCamouflage.aoTextureSize[0], defaultCamouflage.aoTextureSize[1])
        _xml.rewriteVector2(section, sectionName + b'/aoTextureSize', value, defaultValue)
    camouflageSection = _xml.getSubsection(None, section, sectionName, False)
    if camouflageSection is not None and len(camouflageSection.items()) == 0:
        section.deleteSection(sectionName)
    return


def _readColors(xmlCtx, section, sectionName, requiredSize=None):
    res = []
    if not IS_CLIENT and not IS_BOT and not IS_WEB:
        for sname, subsection in _xml.getChildren(xmlCtx, section, sectionName):
            res.append(0)

    else:
        for sname, subsection in _xml.getChildren(xmlCtx, section, sectionName):
            res.append(_readColor((xmlCtx, sectionName + b'/' + sname), subsection, b''))

    if requiredSize is not None and len(res) != requiredSize:
        _xml.raiseWrongXml(xmlCtx, sectionName, b'wrong number of items; required %d' % requiredSize)
    return tuple(res)


def _readColor(xmlCtx, section, sectionName):
    rgbaTuple = _xml.readTupleOfInts(xmlCtx, section, sectionName, 4)
    for c in rgbaTuple:
        if not 0 <= c < 256:
            _xml.raiseWrongXml(_xml, b'', b'color component is out of range [0, 255]')

    return rgbaTuple[0] + (rgbaTuple[1] << 8) + (rgbaTuple[2] << 16) + (rgbaTuple[3] << 24)


def _readNationVehiclesByNames(xmlCtx, section, sectionName, defNationID):
    section = section[sectionName]
    if section is None:
        return frozenset()
    else:
        names = section.asString.split()
        if not names:
            return frozenset()
        if defNationID is not None:
            defNationNameTempl = nations.NAMES[defNationID] + b':'
        else:
            defNationNameTempl = b''
        res = set()
        for vehName in names:
            if vehName.find(b':') == -1:
                vehName = defNationNameTempl + vehName
            try:
                vehTypeCompDescr = makeVehicleTypeCompDescrByName(vehName)
            except:
                if not IS_UE_EDITOR:
                    _xml.raiseWrongXml(xmlCtx, sectionName, b"unknown vehicle name '%s'" % vehName)
                else:
                    ERROR_MSG(b'Unknown vehicle name ' + vehName + b'. The name was skipped.')
                    continue

            res.add(vehTypeCompDescr)

        return frozenset(res)


VehicleValue = namedtuple(b'VehicleValue', [b'vehicle_name', b'compact_descriptor', b'ctx', b'subsection'])

def _vehicleValues(xmlCtx, section, sectionName, defNationID):
    section = section[sectionName]
    if section is None:
        return
    else:
        ctx = (
         xmlCtx, sectionName)
        for vehName, subsection in section.items():
            if vehName.find(b':') == -1:
                vehName = nations.NAMES[defNationID] + b':' + vehName
            try:
                nationID, vehID = g_list.getIDsByName(vehName)
            except:
                if not IS_UE_EDITOR:
                    _xml.raiseWrongXml(xmlCtx, sectionName, b"unknown vehicle name '%s'" % vehName)
                else:
                    ERROR_MSG(b'Unknown vehicle name ' + vehName + b'. The name was skipped.')
                    continue

            yield VehicleValue(vehName, makeIntCompactDescrByID(b'vehicle', nationID, vehID), ctx, subsection)

        return


def _readCamouflageTilings(xmlCtx, section, sectionName, defNationID):
    res = {}
    nameMap = {}
    for v in _vehicleValues(xmlCtx, section, sectionName, defNationID):
        tiling = _xml.readTupleOfFloats(v.ctx, v.subsection, b'', 4)
        if tiling[0] <= 0 or tiling[1] <= 0:
            _xml.raiseWrongSection(v.ctx, v.vehicle_name)
        res[v.compact_descriptor] = tiling
        if IS_UE_EDITOR:
            nameMap[v.compact_descriptor] = v.vehicle_name

    if IS_UE_EDITOR:
        return (res, nameMap)
    return res


def _readCamouflageTilingSettings(xmlCtx, section):
    sectionName = b'tilingSettings'
    if not section.has_key(sectionName):
        return (CamouflageTilingType.LEGACY, None, None)
    else:
        subSection = _xml.getSubsection(xmlCtx, section, sectionName)
        return (
         _readCamouflageTilingType(xmlCtx, subSection),
         _xml.readTupleOfFloats(xmlCtx, subSection, b'factor', 2),
         _xml.readTupleOfFloats(xmlCtx, subSection, b'offset', 2))


def _readCamouflageTilingType(xmlCtx, section):
    readType = _xml.readNonEmptyString(xmlCtx, section, b'type')
    tilingType = CamouflageTilingTypeNameToType.get(readType.upper(), None)
    if tilingType is None:
        _xml.raiseWrongXml(xmlCtx, b'', (b"invalid tiling type '{}'").format(readType))
    return tilingType


def _readPlayerEmblems(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    groups = {}
    emblems = {}
    names = {}
    pricesDest = _g_prices
    for sname, subsection in _xml.getChildren(xmlCtx, section, b''):
        groupCtx = (xmlCtx, sname)
        if groups.has_key(sname):
            _xml.raiseWrongXml(groupCtx, b'', b'emblem group name is not unique')
        groupName = intern(sname)
        igrType = _readIGRType(groupCtx, subsection)
        nationsValue = _readNations(groupCtx, subsection)
        allow = _readNationVehiclesByNames(groupCtx, subsection, b'allow', None)
        deny = _readNationVehiclesByNames(groupCtx, subsection, b'deny', None)
        if pricesDest is not None:
            pricesDest[b'playerEmblemGroupPriceFactors'][groupName] = _xml.readNonNegativeFloat(groupCtx, subsection, b'priceFactor')
            if subsection.readBool(b'notInShop', False):
                pricesDest[b'notInShopPlayerEmblemGroups'].add(groupName)
            elif IS_CLIENT:
                continue
        groupUserString = None
        emblemIDs = []
        for innerName, innterSubsection in _xml.getChildren(groupCtx, subsection, b'emblems'):
            ctx = (groupCtx, innerName)
            if names.has_key(innerName):
                _xml.raiseWrongXml(ctx, b'', b'emblem name is not unique')
            emblemID = _xml.readInt(ctx, innterSubsection, b'id', 1, 65535)
            if emblems.has_key(emblemID):
                _xml.raiseWrongXml(ctx, b'', b'emblem ID is not unique')
            if IS_CLIENT or IS_WEB:
                emblemUserString = i18n.makeString(b'')
                texName = _xml.readNonEmptyString(ctx, innterSubsection, b'texName')
                bumpSubsection = innterSubsection[b'bumpTexName']
                if bumpSubsection is None:
                    bumpTexName = b''
                else:
                    bumpTexName = bumpSubsection.asString
                canBeMirrored = innterSubsection.readBool(b'mirror', False)
            else:
                emblemUserString = None
                texName = b''
                bumpTexName = b''
                canBeMirrored = False
            tags = _xml.readStringOrNone(ctx, innterSubsection, b'tags')
            tags = frozenset() if tags is None else frozenset(tags.split())
            emblemIDs.append(emblemID)
            emblems[emblemID] = (groupName, igrType, texName, bumpTexName, emblemUserString, canBeMirrored, tags)
            if innerName != b'emblem':
                names[intern(innerName)] = emblemID

        groups[groupName] = (
         emblemIDs, groupUserString, igrType, nationsValue, allow, deny)

    ResMgr.purge(xmlPath, True)
    return (
     groups, emblems, names)


def _readPlayerInscriptions(xmlCtx, section, subsectionName, priceFactors, notInShops, idsRange):
    section = _xml.getSubsection(xmlCtx, section, subsectionName)
    xmlCtx = (xmlCtx, subsectionName)
    groups = {}
    inscrs = {}
    for sname, subsection in _xml.getChildren(xmlCtx, section, b''):
        groupCtx = (
         xmlCtx, sname)
        if groups.has_key(sname):
            _xml.raiseWrongXml(groupCtx, b'', b'inscription group name is not unique')
        groupName = intern(sname)
        igrType = _readIGRType(_xml, subsection)
        allow = _readNationVehiclesByNames(_xml, subsection, b'allow', None)
        deny = _readNationVehiclesByNames(_xml, subsection, b'deny', None)
        if priceFactors is not None:
            priceFactors[groupName] = _xml.readNonNegativeFloat(groupCtx, subsection, b'priceFactor')
            if subsection.readBool(b'notInShop', False):
                notInShops.add(groupName)
            elif IS_CLIENT:
                continue
        groupUserString = None
        inscrIDs = []
        for innerName, innerSubsection in _xml.getChildren(groupCtx, subsection, b'inscriptions'):
            ctx = (groupCtx, innerName)
            if innerName != b'inscription':
                _xml.raiseWrongXml(ctx, b'', b'unknown subsection')
            inscrID = _xml.readInt(ctx, innerSubsection, b'id', *idsRange)
            if inscrs.has_key(inscrID):
                _xml.raiseWrongXml(ctx, b'', b'inscription ID is not unique')
            tags = _xml.readStringOrNone(ctx, innerSubsection, b'tags')
            tags = frozenset() if tags is None else frozenset(tags.split())
            if IS_CLIENT or IS_WEB:
                texName = _xml.readNonEmptyString(ctx, innerSubsection, b'texName')
                bumpTexName = innerSubsection.readString(b'bumpTexName', b'')
                inscrUserString = i18n.makeString(None)
                isFeatured = innerSubsection.readBool(b'isFeatured', False)
                inscrs[inscrID] = (groupName, igrType, texName, bumpTexName, inscrUserString, isFeatured, tags)
            else:
                inscrs[inscrID] = (
                 groupName, igrType, tags)
            inscrIDs.append(inscrID)

        groups[groupName] = (inscrIDs, groupUserString, igrType, allow, deny)

    return (groups, inscrs)


def _readVehicleEffects(xmlCtx, section, subsectionName, defaultEffects=None, useOverride=False):
    section = _xml.getSubsection(xmlCtx, section, subsectionName)
    cachedEffects = g_cache._vehicleEffects
    personalEffects = __readEffectGroupsFromSection(section, (xmlCtx, subsectionName), withSubgroups=True) if useOverride else None
    damagedStateGroupPath = b'damagedStateGroup'
    damagedStateGroupName = _xml.readStringOrNone(xmlCtx, section, damagedStateGroupPath)
    res = __readDamagedStateEffects(xmlCtx, damagedStateGroupName, personalEffects, cachedEffects, defaultEffects)
    res.update(__readNormalEffects(xmlCtx, section, personalEffects, cachedEffects, defaultEffects))
    res[b'explosion'] = res[b'ammoBayExplosion']
    if IS_UE_EDITOR:
        return (res, damagedStateGroupName)
    else:
        return res


def __readDamagedStateEffects(xmlCtx, damagedStateGroupName, personalEffects, cachedEffects, defaultEffects):
    res = {}
    for effectKind in _damagedStateGroupEffectKindNames:
        effect = personalEffects.get(effectKind) if personalEffects is not None and len(personalEffects) > 0 else None
        if effect is None:
            if damagedStateGroupName is not None:
                effect = cachedEffects.get(damagedStateGroupName + effectKind[0].upper() + effectKind[1:])
            elif defaultEffects is not None:
                effect = defaultEffects.get(effectKind)
            else:
                _xml.raiseWrongXml((xmlCtx, damagedStateGroupName), b'', b"subsection effect group '%s' is missing" % damagedStateGroupName)
        if effect is None:
            _xml.raiseWrongXml((xmlCtx, damagedStateGroupName), b'', b'missing effect or mismatching effect group name (%s is not found)' % effectKind)
        res[effectKind] = effect

    return res


def __readNormalEffects(xmlCtx, section, personalEffects, cachedEffects, defaultEffects):
    res = {}
    isPersonalEffects = personalEffects is not None and len(personalEffects) > 0
    for effectKind in _vehicleEffectKindNames:
        effect = personalEffects.get(effectKind) if isPersonalEffects else None
        if not effect:
            subsection = section[effectKind]
            if subsection is not None:
                effectName = subsection.asString
                if effectName:
                    effect = cachedEffects.get(effectName)
                    if effect is None:
                        _xml.raiseWrongXml((xmlCtx, section.asString), effectKind, b'missing or wrong effect name')
                else:
                    effect = []
            elif defaultEffects is not None:
                effect = defaultEffects.get(effectKind)
        if effect is not None:
            res[effectKind] = effect

    return res


def _readTurretDetachmentEffects(xmlCtx, section, subsectionName, defaultEffects=None):
    if defaultEffects is None:
        defaultEffects = {}
    res = {}
    detachmentEffectsSection = section[subsectionName]

    def getEffect(effectSection, defaultEffect, state):
        if effectSection is not None:
            effectName = effectSection.asString
            return g_cache._turretDetachmentEffects.get(effectName)
        else:
            if defaultEffect is not None:
                return defaultEffect
            return

    for detachmentState in (b'flight', b'flamingOnGround'):
        effectSection = None
        if detachmentEffectsSection is not None:
            effectSection = detachmentEffectsSection[detachmentState]
        effect = getEffect(effectSection, defaultEffects.get(detachmentState), detachmentState)
        if effect:
            res[detachmentState] = effect

    for collisionEffectType in (b'collision', b'pull'):
        collisionEffectsSection = None
        if detachmentEffectsSection is not None:
            collisionEffectsSection = detachmentEffectsSection[collisionEffectType]
        resultCollisionEffects = {}
        defaultCollisionEffects = defaultEffects.get(collisionEffectType, {})
        for effectMaterial in material_kinds.EFFECT_MATERIALS:
            effectIdx = material_kinds.EFFECT_MATERIAL_INDEXES_BY_NAMES[effectMaterial]
            effectSection = None
            if collisionEffectsSection is not None:
                effectSection = collisionEffectsSection[effectMaterial]
            effect = getEffect(effectSection, defaultCollisionEffects.get(effectIdx), effectMaterial)
            if effect:
                resultCollisionEffects[effectIdx] = effect

        res[collisionEffectType] = resultCollisionEffects

    return res


if IS_CLIENT or IS_UE_EDITOR:
    _vehicleEffectKindNames = tuple([
     426, 427, 428, 429, 430, 431, 432, 433] + [b'%sCollisionLight' % _name for _name in EFFECT_MATERIALS] + [b'%sCollisionHeavy' % _name for _name in EFFECT_MATERIALS] + [b'explosionCandle%d' % _i for _i in xrange(1, 5)] + [b'fullDestruction'] + [b'dynamicCollision'])
    _damagedStateGroupEffectKindNames = (
     b'ammoBayExplosion',
     b'ammoBayBurnOff',
     b'fuelExplosion',
     b'destruction',
     b'crewDeath',
     b'rammingDestruction',
     b'submersionDeath',
     b'flaming',
     b'instantExplosion')

def _readClientAdjustmentFactors(xmlCtx, section):
    return {b'power': (section.readFloat(b'clientAdjustmentFactors/power', 1.0)), 
       b'armour': (section.readFloat(b'clientAdjustmentFactors/armour', 1.0)), 
       b'mobility': (section.readFloat(b'clientAdjustmentFactors/mobility', 1.0)), 
       b'visibility': (section.readFloat(b'clientAdjustmentFactors/visibility', 1.0)), 
       b'camouflage': (section.readFloat(b'clientAdjustmentFactors/camouflage', 1.0)), 
       b'guns': (_readClientAdjustmentSection(xmlCtx, section, b'clientAdjustmentFactors/guns', b'caliberCorrection', b'delta', False))}


def _readSiegeModeParams(xmlCtx, section, vehType):
    subSection = section[b'siege_mode']
    if subSection is None:
        return
    else:
        res = {b'device': (_xml.readStringWithDefaultValue(xmlCtx, subSection, b'device', b'engine')), 
           b'switchOnTime': (_xml.readNonNegativeFloat(xmlCtx, subSection, b'switchOnTime', 2.0)), 
           b'switchOffTime': (_xml.readNonNegativeFloat(xmlCtx, subSection, b'switchOffTime', 2.0)), 
           b'switchCancelEnabled': (subSection.readBool(b'switchCancelEnabled', False)), 
           b'engineDamageCoeff': (_xml.readNonNegativeFloat(xmlCtx, subSection, b'engineDamageCoeff', 2.0)), 
           b'stopEngineOnSwitch': (subSection.readBool(b'stopEngineOnSwitch', True))}
        if b'autoSiege' in vehType.tags:
            res.update({b'autoSwitchOffRequiredVehicleSpeed': (component_constants.KMH_TO_MS * _xml.readNonNegativeFloat(xmlCtx, subSection, b'autoSwitchOffRequiredVehicleSpeed', 1.0)), 
               b'autoSwitchOnRequiredVehicleSpeed': (component_constants.KMH_TO_MS * _xml.readNonNegativeFloat(xmlCtx, subSection, b'autoSwitchOnRequiredVehicleSpeed', 0.1))})
        if IS_CLIENT or IS_UE_EDITOR:
            res[b'soundStateChange'] = sound_readers.readSoundSiegeModeStateChange(xmlCtx, subSection)
            res[VEHICLE_SIEGE_STATE.SWITCHING_ON] = {b'normal': (res[b'switchOnTime']), 
               b'critical': (res[b'switchOnTime'] * res[b'engineDamageCoeff']), 
               b'destroyed': (res[b'switchOnTime'] * res[b'engineDamageCoeff'])}
            res[VEHICLE_SIEGE_STATE.SWITCHING_OFF] = {b'normal': (res[b'switchOffTime']), 
               b'critical': (res[b'switchOffTime'] * res[b'engineDamageCoeff']), 
               b'destroyed': (res[b'switchOffTime'] * res[b'engineDamageCoeff'])}
        return res


def _readRocketAccelerationParams(xmlCtx, section):
    rocketCtx, rocketSection = _xml.getSubSectionWithContext(xmlCtx, section, b'rocketAcceleration')
    impulse = shared_components.readImpulseData(rocketCtx, rocketSection)
    modifiers = readModifiers(rocketCtx, _xml.getSubsection(rocketCtx, rocketSection, b'modifiers'))
    if IS_CLIENT:
        kpiCtx, kpiSection = _xml.getSubSectionWithContext(rocketCtx, rocketSection, b'kpi')
        kpi = readKpi(kpiCtx, kpiSection)
    else:
        kpi = None
    return shared_components.RocketAccelerationParams(deployTime=_xml.readNonNegativeFloat(rocketCtx, rocketSection, b'deployTime'), reloadTime=_xml.readNonNegativeFloat(rocketCtx, rocketSection, b'reloadTime'), reuseCount=_xml.readInt(rocketCtx, rocketSection, b'reuseCount', minVal=-1), duration=_xml.readNonNegativeFloat(rocketCtx, rocketSection, b'duration'), impulse=impulse, modifiers=modifiers, kpi=kpi)


def _readGunTwinGunParams(xmlCtx, section):
    subSection = section[b'twinGun']
    if subSection is None:
        return
    else:
        res = component_constants.TwinGun(afterShotDelay=_xml.readNonNegativeFloat(xmlCtx, subSection, b'afterShotDelay'), gunMarkerOffset=_xml.readNonNegativeFloat(xmlCtx, subSection, b'gunMarkerOffset', 0.0), shootImpulse=_xml.readNonNegativeInt(xmlCtx, subSection, b'shootImpulse', 0), twinGunReloadTime=_xml.readNonNegativeFloat(xmlCtx, subSection, b'twinGunReloadTime', 0.0))
        return res


def _readGunDualGunParams(xmlCtx, section):
    subSection = section[b'dualGun']
    if subSection is None:
        return
    else:
        res = component_constants.DualGun(chargeTime=_xml.readNonNegativeFloat(xmlCtx, subSection, b'chargeTime'), shootImpulse=_xml.readNonNegativeInt(xmlCtx, subSection, b'shootImpulse'), reloadLockTime=_xml.readNonNegativeFloat(xmlCtx, subSection, b'reloadLockTime'), reloadTimes=_xml.readTupleOfPositiveFloats(xmlCtx, subSection, b'reloadTimes'), rateTime=_xml.readNonNegativeFloat(xmlCtx, subSection, b'rateTime'), chargeThreshold=_xml.readNonNegativeFloat(xmlCtx, subSection, b'chargeThreshold'), afterShotDelay=_xml.readNonNegativeFloat(xmlCtx, subSection, b'afterShotDelay'), preChargeIndication=_xml.readNonNegativeFloat(xmlCtx, subSection, b'preChargeIndication'), chargeCancelTime=_xml.readNonNegativeFloat(xmlCtx, subSection, b'chargeCancelTime', 0.2))
        return res


def _readGunDualAccuracyParams(xmlCtx, section):
    subSection = section[b'dualAccuracy']
    if subSection is None:
        return
    else:
        afterShotDispersionRadius = _xml.readPositiveFloat(xmlCtx, subSection, b'afterShotDispersionRadius')
        afterShotDispersionAngle = atan(afterShotDispersionRadius / 100.0)
        res = component_constants.DualAccuracy(afterShotDispersionAngle=afterShotDispersionAngle, coolingDelay=_xml.readNonNegativeFloat(xmlCtx, subSection, b'coolingDelay'))
        return res


def _readGunControllableReload(xmlCtx, section):
    subSection = section[b'controllableReload']
    if subSection is None:
        return
    else:
        allowToReloadAfterShot = _xml.readBool(xmlCtx, subSection, b'allowToReloadAfterShot', False)
        return component_constants.ControllableReload(allowToReloadAfterShot=allowToReloadAfterShot)


def _readHullAimingParams(xmlCtx, section):
    res = {b'pitch': {b'isAvailable': (section.has_key(b'hull_aiming/pitch') != 0), 
                  b'isEnabled': (section.readBool(b'hull_aiming/pitch/isEnabled')), 
                  b'isFlexible': (section.readBool(b'hull_aiming/pitch/isFlexible')), 
                  b'wheelCorrectionCenterZ': (_xml.readFloat(xmlCtx, section, b'hull_aiming/pitch/wheelCorrectionCenterZ', 0.0)), 
                  b'wheelsCorrectionSpeed': (radians(_xml.readPositiveFloat(xmlCtx, section, b'hull_aiming/pitch/wheelsCorrectionSpeed', 0.0))), 
                  b'wheelsCorrectionAngles': {b'pitchMin': (radians(_xml.readFloat(xmlCtx, section, b'hull_aiming/pitch/wheelsCorrectionAngles/pitchMin', 0))), 
                                              b'pitchMax': (radians(_xml.readFloat(xmlCtx, section, b'hull_aiming/pitch/wheelsCorrectionAngles/pitchMax', 0)))}}, 
       b'yaw': {b'isAvailable': (section.has_key(b'hull_aiming') != 0 and not section.has_key(b'hull_aiming/yawDisabled'))}}
    return res


def __readRotationAngleLimits(xmlCtx, section, name):
    v = _xml.readVector2(xmlCtx, section, name)
    if v[0] > v[1]:
        _xml.raiseWrongSection(xmlCtx, name)
    if v[0] > -179.0 or v[1] < 179.0:
        return (radians(v[0]), radians(v[1]))
    else:
        return


def _readClientAdjustmentSection(xmlCtx, section, subsectionName, privateFactorName, publicFactorName, throwIfMissing=True):
    res = {}
    subsection = _xml.getSubsection(xmlCtx, section, subsectionName, throwIfMissing)
    if subsection is None:
        return res
    else:
        for name in subsection.keys():
            res.setdefault(name, {}).setdefault(privateFactorName, subsection.readFloat(name + b'/' + publicFactorName))

        return res


def _extractNeededPrereqs(prereqs, resourceNames):
    resourceNames = frozenset(resourceNames)
    res = []
    for name in resourceNames:
        try:
            if name not in g_cache.requestOncePrereqs:
                res.append(prereqs[name])
                g_cache.requestOncePrereqs.add(name)
        except Exception:
            if name not in g_cache.requestOncePrereqs:
                LOG_WARNING(b'Resource is not found: %s' % name)
            else:
                res.append(None)

    return res


def _readAODecals(xmlCtx, section, secname):
    res = []
    if section.has_key(secname):
        for _, subsection in _xml.getChildren(xmlCtx, section, secname):
            m = subsection.readMatrix(b'transform')
            res.append(m)

    return tuple(res)


def _writeAODecals(decalsList, section, secname):
    decalId = 0
    if section.has_key(secname):
        for _, subsection in _xml.getChildren(None, section, secname):
            _xml.rewriteMatrix(subsection, b'transform', decalsList[decalId])
            decalId += 1

    return


def _readRepaintParams(xmlCtx, section):
    res = {}
    if not section.has_key(b'refColor') or not section.has_key(b'refGloss') or not section.has_key(b'refColorMult') or not section.has_key(b'refGlossMult'):
        return res
    res[b'refColor'] = _xml.readVector3(xmlCtx, section, b'refColor')
    res[b'refGloss'] = _xml.readFloat(xmlCtx, section, b'refGloss')
    res[b'refColorMult'] = _xml.readFloat(xmlCtx, section, b'refColorMult')
    res[b'refGlossMult'] = _xml.readFloat(xmlCtx, section, b'refGlossMult')
    return res


def _readImpactParams(xmlCtx, section, paramName):
    subXmlCtx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, paramName, throwIfMissing=False)
    params = HighExplosiveImpactParams()
    if subsection is None:
        params.radius = 0.0
        params.armorDamage = (0.0, 0.0)
        params.deviceDamage = (0.0, 0.0)
        params.isActive = False
        params.hasSplash = False
        return params
    else:
        params.radius = _xml.readNonNegativeFloat(subXmlCtx, subsection, b'impactRadius', 0.0)
        params.armorDamage = shared_readers.readFloatPair(subXmlCtx, subsection, b'damage/armor')
        params.deviceDamage = shared_readers.readFloatPair(subXmlCtx, subsection, b'damage/devices')
        if paramName == HighExplosiveImpact.ARMOR_SPALLS:
            params.coneAngleCos = cos(radians(_xml.readNonNegativeFloat(subXmlCtx, subsection, b'coneAngle')))
            params.piercingSpalls = _xml.readBool(subXmlCtx, subsection, b'piercingSpalls', component_constants.DEFAULT_PIERCING_SPALLS)
        if subsection.has_key(b'damageAbsorption'):
            label = _xml.readNonEmptyString(subXmlCtx, subsection, b'damageAbsorption')
            params.damageAbsorptionType = DamageAbsorptionLabelToType.get(label)
        isActive = _xml.readBool(subXmlCtx, subsection, b'isActive', True)
        params.isActive = (any(params.armorDamage) or any(params.deviceDamage)) and isActive
        params.hasSplash = params.radius and params.isActive
        return params


def _readImpactParamsLocal(xmlCtx, section, paramName, originalParams):
    subXmlCtx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, paramName, throwIfMissing=True)
    localParams = copy.copy(originalParams)
    if subsection.has_key(b'isActive'):
        localParams.isActive = _xml.readBool(subXmlCtx, subsection, b'isActive')
    if subsection.has_key(b'impactRadius'):
        localParams.radius = _xml.readNonNegativeFloat(subXmlCtx, subsection, b'impactRadius')
    if subsection.has_key(b'damage/armor'):
        localParams.armorDamage = shared_readers.readFloatPair(subXmlCtx, subsection, b'damage/armor')
    if subsection.has_key(b'damage/devices'):
        localParams.deviceDamage = shared_readers.readFloatPair(subXmlCtx, subsection, b'damage/devices')
    if paramName == HighExplosiveImpact.ARMOR_SPALLS:
        if subsection.has_key(b'coneAngle'):
            localParams.coneAngleCos = cos(radians(_xml.readNonNegativeFloat(subXmlCtx, subsection, b'coneAngle')))
        if subsection.has_key(b'piercingSpalls'):
            localParams.piercingSpalls = _xml.readBool(subXmlCtx, subsection, b'piercingSpalls')
    if subsection.has_key(b'damageAbsorption'):
        label = _xml.readNonEmptyString(subXmlCtx, subsection, b'damageAbsorption')
        localParams.damageAbsorptionType = DamageAbsorptionLabelToType.get(label)
    localParams.isActive = (any(localParams.armorDamage) or any(localParams.deviceDamage)) and localParams.isActive
    localParams.hasSplash = localParams.radius and localParams.isActive
    return localParams


def _readBrokenTrackLosses(xmlCtx, section):
    if not section.has_key(b'brokenTrackLosses'):
        return {b'enginePowerLoss': None, 
           b'fwMaxSpeedLoss': None, 
           b'bkMaxSpeedLoss': None, 
           b'rotationSpeedLoss': None}
    else:
        ctx, subsection = _xml.getSubSectionWithContext(xmlCtx, section, b'brokenTrackLosses')

        def readLoss(paramName):
            if subsection[paramName] is None:
                return
            else:
                return _xml.readTupleOfFloats(ctx, subsection, paramName)

        return {b'enginePowerLoss': (readLoss(b'enginePowerLoss')), 
           b'fwMaxSpeedLoss': (readLoss(b'fwMaxSpeedLoss')), 
           b'bkMaxSpeedLoss': (readLoss(b'bkMaxSpeedLoss')), 
           b'rotationSpeedLoss': (readLoss(b'rotationSpeedLoss'))}


def _validateBrokenTrackLosses(xmlCtx, vehType):
    if vehType.isWheeledVehicle:
        return
    else:
        chassisPhysics = vehType.xphysics[b'detailed'][b'chassis']
        ctx = (xmlCtx, b'physics/detailed/chassis')
        for chassis in vehType.chassis:
            maxLossesCount = sum(2 for trackPair in chassis.trackPairs if trackPair.breakMode == TrackBreakMode.SLOW)
            brokenTrackLosses = chassisPhysics[chassis.name][b'brokenTrackLosses']
            chassisCtx = (
             ctx, chassis.name)
            for lossName, losses in viewitems(brokenTrackLosses):
                if losses is None:
                    brokenTrackLosses[lossName] = (0.0,) * maxLossesCount
                elif len(losses) != maxLossesCount:
                    _xml.raiseWrongXml((
                     chassisCtx, b'brokenTrackLosses'), lossName, b'%d floats expected' % maxLossesCount)

        return


def _readBrokenWheelLosses(xmlCtx, section, axleIsLeading, axleCanBeRised, wheelRiseHeight):

    def readLoss(paramName, minCount):
        if section[paramName] is None:
            return (0.0,) * minCount
        else:
            return _xml.readTupleOfFloats(xmlCtx, section, paramName, count=minCount)

    leadingAxleCount = len([v for v in axleIsLeading if v is True])
    groundedAxleCount = len([v for v in axleCanBeRised if v is False]) if wheelRiseHeight > 0.0 else len(axleCanBeRised)
    return (
     readLoss(b'brokenWheelPowerLoss', 2 * leadingAxleCount),
     readLoss(b'brokenWheelSpeedLoss', 2 * groundedAxleCount),
     readLoss(b'brokenWheelRotationSpeedLoss', 2 * groundedAxleCount))


def _readSteeringAngles(xmlCtx, section, axleCount, lockAnglesRequired=True):
    axleSteeringAngles = _xml.readTupleOfFloats(xmlCtx, section, b'axleSteeringAngles', axleCount)
    if not section.has_key(b'axleSteeringLockAngles') and not lockAnglesRequired:
        return (axleSteeringAngles, axleSteeringAngles)
    axleSteeringLockAngles = _xml.readTupleOfFloats(xmlCtx, section, b'axleSteeringLockAngles', axleCount)
    return (axleSteeringAngles, axleSteeringLockAngles)


def _readBurnout(xmlCtx, section):
    if not section.has_key(b'burnout'):
        return None
    else:
        burnoutCtx, burnoutSection = _xml.getSubSectionWithContext(xmlCtx, section, b'burnout')
        burnout = {b'preparationTime': (_xml.readPositiveFloat(burnoutCtx, burnoutSection, b'preparationTime')), 
           b'activityTime': (_xml.readPositiveFloat(burnoutCtx, burnoutSection, b'activityTime'))}
        burnoutParams = (b'engineDamageMin', b'engineDamageMax', b'warningMaxHealth', b'warningMaxHealthCritEngine', b'power', b'impulse')
        burnout.update(_parseFloatList(burnoutCtx, burnoutSection, burnoutParams))
        return burnout


def _readAxleRiseParams(xmlCtx, section, axleCount, hasSiegeMode=True):
    if not section.has_key(b'axleCanBeRised') and not hasSiegeMode:
        axleCanBeRised = (
         False,) * axleCount
    else:
        axleCanBeRised = _xml.readTupleOfBools(xmlCtx, section, b'axleCanBeRised', axleCount)
    defaultValue = None if hasSiegeMode and any(axleCanBeRised) else 0.0
    wheelRiseHeight = _xml.readFloat(xmlCtx, section, b'wheelRiseHeight', defaultValue)
    wheelRiseSpeed = _xml.readFloat(xmlCtx, section, b'wheelRiseSpeed', defaultValue)
    return (
     axleCanBeRised, wheelRiseHeight, wheelRiseSpeed)


def _readShootImpulses(xmlCtx, section):
    if not section.has_key(b'shootImpulse'):
        return component_constants.EMPTY_TUPLE
    shootImpulses = []
    subsectionCtx = (xmlCtx, b'shootImpulse')
    for subsectionName, subsection in section.items():
        if subsectionName != b'shootImpulse':
            continue
        shootImpulse = component_constants.ShootImpulse(_xml.readFloat(subsectionCtx, subsection, b'magnitude'), _xml.readString(subsectionCtx, subsection, b'applicationPoint'), _xml.readBool(subsectionCtx, subsection, b'isStillSafe', False))
        if shootImpulse.applicationPoint not in ShootImpulseApplicationPoint.ALL:
            _xml.raiseWrongXml(subsectionCtx, b'applicationPoint', (b'unknown value - {}, possible values - {}').format(shootImpulse.applicationPoint, ShootImpulseApplicationPoint.ALL))
        shootImpulses.append(shootImpulse)

    return tuple(shootImpulses)


def _readOptDevsOverrides(xmlCtx, section):
    if section is None:
        return {}
    else:
        optDevsOverrides = {}
        for optDevName, optDevSection in section.items():
            for factorName in optDevSection.keys():
                factor = LevelsFactor.readTypelessLevelsFactor(xmlCtx, optDevSection, factorName)
                optDevsOverrides.setdefault(optDevName, {})[factorName] = factor

        return optDevsOverrides


def _readPostProgressionPricesOverrides(xmlCtx, section):
    if section is None:
        return {}
    else:
        postProgressionPricesOverrides = {}
        for sname, _ in section.items():
            if sname not in POST_PROGRESSION_ALL_PRICES:
                raise SoftException(b'Price tag <%s> is incorrect. It should be explicitly declared in POST_PROGRESSION_ALL_PRICES' % sname)
            postProgressionPricesOverrides[sname] = _xml.readPostProgressionPrice(xmlCtx, section, sname)
            priceConstants = [(POST_PROGRESSION_UNLOCK_MODIFICATIONS_PRICES, ALLOWED_CURRENCIES_FOR_TREE_STEP),
             (
              POST_PROGRESSION_BUY_MODIFICATIONS_PRICES, ALLOWED_CURRENCIES_FOR_BUY_MODIFICATION_STEP),
             (
              (
               CUSTOM_ROLE_SLOT_CHANGE_PRICE,), ALLOWED_CURRENCIES_FOR_CUSTOM_ROLE_SLOT_CHANGE)]
            for names, currencies in priceConstants:
                if sname in names and not currencies.issuperset(postProgressionPricesOverrides[sname].keys()):
                    raise SoftException((b'Wrong currency for subsection: {}, ctx: {}').format(sname, xmlCtx))

        return postProgressionPricesOverrides


def _readMuzzleBrake(xmlCtx, section):
    default = component_constants.MuzzleBrakeType(component_constants.MuzzleBrakeType.NONE).name
    muzzleBrakeType = intern(_xml.readStringWithDefaultValue(xmlCtx, section, b'muzzleBrake', default))
    return component_constants.MuzzleBrakeType[muzzleBrakeType]


def _readVehicleMechanics(xmlPath):
    res = {}
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    availableRanks = frozenset([b'silver', b'gold'])
    for vehicleSection in section.values():
        vehTypeCompDescr = makeVehicleTypeCompDescrByName(vehicleSection.readString(b'vehicleType'))
        res[vehTypeCompDescr] = {}
        for mechanicName, mechanicSection in vehicleSection[b'mechanics'].items():
            priority = mechanicSection.readInt(b'priority', 0)
            rank = mechanicSection.readString(b'rank', b'')
            if rank not in availableRanks:
                _xml.raiseWrongXml(xmlPath, mechanicSection, b'invalid rank for mechanic : ' + mechanicName)
            params = []
            if mechanicSection.has_key(b'params'):
                for paramSection in _xml.getSubsection(xmlPath, mechanicSection, b'params').values():
                    params.append((
                     paramSection.readString(b'name'),
                     {b'value': (paramSection.asString), 
                        b'template': (paramSection.readString(b'template', b'')), 
                        b'kpiSign': (paramSection.readString(b'kpiSign', b'positive'))}))

            mechanicSubtypes = _readMechanicSubtypes(xmlPath, mechanicSection, mechanicName)
            res[vehTypeCompDescr][mechanicName] = {b'priority': priority, 
               b'rank': rank, 
               b'params': params, 
               b'mechanicSubtypes': mechanicSubtypes}

    ResMgr.purge(xmlPath, True)
    return res


def _readMechanicSubtypes(xmlPath, mechanicSection, mechanicName):
    if not mechanicSection.has_key(b'mechanicSubtypes'):
        return {}
    else:
        mechanicSubtypes = {}
        subtypeSection = _xml.getSubsection(xmlPath, mechanicSection, b'mechanicSubtypes')
        if subtypeSection.has_key(b'shells'):
            for shellSection in subtypeSection[b'shells'].values():
                shell = shellSection.readString(b'name')
                shellNation, shellName = shell.split(b':')
                shellDescr = getShellByName(shellName, shellNation)
                if shellDescr is None:
                    _xml.raiseWrongXml(None, xmlPath, (b'Invalid shell for mechanic {}').format(mechanicName))
                shellCD = shellDescr.compactDescr
                basicValue = shellSection.readString(b'basic')
                modifiedValue = shellSection.readString(b'modified')
                if not basicValue or not modifiedValue:
                    _xml.raiseWrongXml(None, xmlPath, (b'Empty value of basic or modified attribute for mechanic {} for shell {}').format(mechanicName, shellCD))
                basicWithTextLabel = shellSection.readBool(b'basicWithTextLabel', False)
                basicWithRichTooltip = shellSection.readBool(b'basicWithRichTooltip', True)
                modifiedWithTextLabel = shellSection.readBool(b'modifiedWithTextLabel', False)
                modifiedWithRichTooltip = shellSection.readBool(b'modifiedWithRichTooltip', True)
                mechanicSubtypes[shellCD] = {b'basic': basicValue, 
                   b'modified': modifiedValue, 
                   b'basicWithTextLabel': basicWithTextLabel, 
                   b'basicWithRichTooltip': basicWithRichTooltip, 
                   b'modifiedWithTextLabel': modifiedWithTextLabel, 
                   b'modifiedWithRichTooltip': modifiedWithRichTooltip}

        return mechanicSubtypes


def _descrByID(descrList, id):
    for descr in descrList:
        if descr.id[1] == id:
            return descr

    raise SoftException((b'ID={} not found in descriptor list - {}').format(id, descrList))
    return


def _findDescrByID(descrList, id):
    for descr in descrList:
        if descr.id[1] == id:
            return descr

    return


def _collectComponents(compactDescrs, compList):
    compactDescrs.update([x.compactDescr for x in compList])
    return


def _collectReqItemsRecursively(destSet, rootSet, reqItems):
    for compactDescr in rootSet:
        if compactDescr not in destSet:
            destSet.add(compactDescr)
            _collectReqItemsRecursively(destSet, tuple(reqItems.get(compactDescr, ())), reqItems)

    return


def _selectCrewExtras(crewRoles, extrasDict):
    res = []
    idxsInRoles = {}
    for role in crewRoles:
        role = role[0]
        if role not in (b'commander', b'driver'):
            idxInRole = idxsInRoles.get(role, 1)
            idxsInRoles[role] = idxInRole + 1
            role += str(idxInRole)
        res.append(extrasDict[role + b'Health'])

    return tuple(res)


def selectBestHull(hulls, turretIDs, chassisID):
    bestHull = hulls[0]
    bestMatchWeight = 0
    for hull in hulls[1:]:
        match = hull.variantMatch
        matchWeight = 0
        if match[0] is not None:
            if match[0] != chassisID:
                continue
            matchWeight = 100
        for turretID, turretToMatchID in zip(turretIDs, match[1:]):
            if turretToMatchID is None:
                continue
            if turretID == turretToMatchID:
                matchWeight += 1
            else:
                matchWeight = -1
                break

        if bestMatchWeight < matchWeight:
            bestMatchWeight = matchWeight
            bestHull = hull

    return bestHull


def _summPriceDiff(price, priceAdd, priceSub):
    return (
     price[0] + priceAdd[0] - priceSub[0],
     price[1] + priceAdd[1] - priceSub[1])


def _splitVehicleCompactDescr(compactDescr, vehMode=VEHICLE_MODE.DEFAULT, vehType=None, onlyComponents=False):
    header = unpackByte(compactDescr[0])
    vehTypeOffset = 0
    vehicleTypeID = unpackByte(compactDescr[1])
    if header & EXTENDED_VEHICLE_TYPE_ID_FLAG:
        vehicleTypeID += unpackByte(compactDescr[2]) << 8
        vehTypeOffset += 1
    nationID = header >> 4 & 15
    if vehType is None:
        type = g_cache.vehicle(nationID, vehicleTypeID, vehMode)
    else:
        type = vehType
    idx = 10 + vehTypeOffset + len(type.turrets) * 4
    components = compactDescr[2 + vehTypeOffset:idx]
    if onlyComponents:
        return (type, components)
    else:
        flags = unpackByte(compactDescr[idx])
        idx += 1
        count = 0
        optionalDeviceSlots = 0
        for i in xrange(0, MAX_OPTIONAL_DEVICES_SLOTS):
            if flags & 1 << i:
                count += 1
                optionalDeviceSlots |= 1 << i

        optionalDevices = compactDescr[idx:idx + count * 2]
        idx += count * 2
        if flags & 16:
            count = unpackByte(compactDescr[idx])
            enhancements = compactDescr[idx:idx + 1 + count * 6]
            idx += 1 + count * 6
        else:
            enhancements = b''
        if flags & 32:
            emblemPositions = unpackByte(compactDescr[idx])
            idx += 1
            count = 0
            for i in _RANGE_4:
                if emblemPositions & 1 << i:
                    count += 1

            emblems = compactDescr[idx:idx + count * 6]
            idx += count * 6
            count = 0
            for i in _RANGE_4:
                if emblemPositions & 1 << i + 4:
                    count += 1

            inscriptions = compactDescr[idx:idx + count * 7]
            idx += count * 7
        else:
            emblemPositions = 0
            emblems = b''
            inscriptions = b''
        if flags & 64:
            idx += 1
        if flags & 128:
            camouflages = compactDescr[idx:]
        else:
            camouflages = b''
        return (type, components, optionalDeviceSlots, optionalDevices, enhancements,
         emblemPositions, emblems, inscriptions, camouflages)


def _combineVehicleCompactDescr(type, components, optionalDeviceSlots, optionalDevices, enhancements, emblemPositions, emblems, inscriptions, camouflages):
    header = items.ITEM_TYPES.vehicle + (type.id[0] << 4)
    vehicleTypeID = type.id[1]
    flags = optionalDeviceSlots
    if enhancements:
        flags |= 16
    if emblems or inscriptions:
        flags |= 32
    if camouflages:
        flags |= 128
    vehTypeCD = packByte(vehicleTypeID & 255)
    if vehicleTypeID > 255:
        vehTypeCD += packByte(vehicleTypeID >> 8)
        header += EXTENDED_VEHICLE_TYPE_ID_FLAG
    cd = packByte(header) + vehTypeCD + components + packByte(flags) + optionalDevices
    if enhancements:
        cd += enhancements
    if emblems or inscriptions:
        cd += packByte(emblemPositions) + emblems + inscriptions
    if camouflages:
        cd += camouflages
    return cd


def _packIDAndDuration(id, startTime, durationDays):
    return struct.pack(b'<HI', id, (startTime - _CUSTOMIZATION_EPOCH) // 60 | durationDays << 24)


def _unpackIDAndDuration(cd):
    id, times = struct.unpack(b'<HI', cd)
    return (
     id,
     (times & 16777215) * 60 + _CUSTOMIZATION_EPOCH,
     times >> 24)


@_xml.cacheFloatTuples
def cachedFloatTuple(args):
    return tuple(args)


def _deduceNamesFromTankXmlPath(xmlPath):
    parts = xmlPath.split(b'/')
    return (parts[-2], os.path.splitext(parts[-1])[0])


def findAmmoIndexByCompactDescr(ammo, compactDescr):
    for idx in xrange(0, len(ammo), 2):
        if ammo[idx] == compactDescr:
            return idx

    return


def areOptDevicesLayoutsEqual(oldDevicesObjs, newDevicesCDs):
    oldDevicesCDs = [device.compactDescr if device is not None else 0 for device in oldDevicesObjs]
    newDevicesCDs = newDevicesCDs or [0] * len(oldDevicesCDs)
    return oldDevicesCDs == newDevicesCDs


def reinstallOptionalDevices(vehDescr, newDevices):
    removeOptionalDevice = vehDescr.removeOptionalDevice
    for slotIdx in xrange(len(vehDescr.optionalDevices)):
        removeOptionalDevice(slotIdx, rebuildAttrs=False)

    installOptionalDevice = vehDescr.installOptionalDevice
    for slotIdx, compactDescr in enumerate(newDevices):
        if compactDescr != 0:
            installOptionalDevice(compactDescr, slotIdx, rebuildAttrs=False)

    vehDescr.rebuildAttrs()
    return vehDescr


_EMPTY_EMBLEM = (
 None, _CUSTOMIZATION_EPOCH, 0)
_EMPTY_EMBLEMS = (_EMPTY_EMBLEM, _EMPTY_EMBLEM, _EMPTY_EMBLEM, _EMPTY_EMBLEM)
_EMPTY_INSCRIPTION = (None, _CUSTOMIZATION_EPOCH, 0, 0)
_EMPTY_INSCRIPTIONS = (_EMPTY_INSCRIPTION, _EMPTY_INSCRIPTION, _EMPTY_INSCRIPTION, _EMPTY_INSCRIPTION)
_EMPTY_CAMOUFLAGE = (None, _CUSTOMIZATION_EPOCH, 0)
_EMPTY_CAMOUFLAGES = (_EMPTY_CAMOUFLAGE, _EMPTY_CAMOUFLAGE, _EMPTY_CAMOUFLAGE)
_RANGE_4 = lrange(4)
_VEHICLE = items.ITEM_TYPES[b'vehicle']
_CHASSIS = items.ITEM_TYPES[b'vehicleChassis']
_TURRET = items.ITEM_TYPES[b'vehicleTurret']
_GUN = items.ITEM_TYPES[b'vehicleGun']
_ENGINE = items.ITEM_TYPES[b'vehicleEngine']
_FUEL_TANK = items.ITEM_TYPES[b'vehicleFuelTank']
_RADIO = items.ITEM_TYPES[b'vehicleRadio']
_TANKMAN = items.ITEM_TYPES[b'tankman']
_OPTIONALDEVICE = items.ITEM_TYPES[b'optionalDevice']
_SHELL = items.ITEM_TYPES[b'shell']
_EQUIPMENT = items.ITEM_TYPES[b'equipment']
