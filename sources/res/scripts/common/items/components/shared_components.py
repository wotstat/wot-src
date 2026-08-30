from __future__ import absolute_import, division
from functools import partial
import typing
from past.builtins import xrange
from future.moves import pickle
from future.utils import lmap, lzip, viewitems
from math import radians
from collections import namedtuple
from constants import IS_CLIENT, IS_WEB, IS_EDITOR, IS_BOT, HEATING_ZONES_GUN_STATE, DEBUFFS_TYPES, SIGHT_POINTER_COMMON_CONSTANTS
from debug_utils import LOG_WARNING
from items import ITEM_TYPES, _xml
from items.components import component_constants, c11n_constants, path_builder
from items.components.component_constants import KMH_TO_MS
from items.components.c11n_constants import AttachmentSize
from items.attributes_helpers import ALLOWED_STATIC_ATTRS, isclose
from py2to3.patched_future import with_metaclass
from soft_exception import SoftException
from wrapped_reflection_framework import ReflectionMetaclass, reflectedNamedTuple
if IS_CLIENT:
    from helpers import i18n
elif IS_WEB or IS_BOT:
    from web_stubs import i18n
else:

    class i18n(object):

        @classmethod
        def makeString(cls, key):
            raise SoftException(b'Unexpected call "i18n.makeString"')
            return


if typing.TYPE_CHECKING:
    from typing import Any, Dict, List, Optional, Sequence, Set
    from constants import VEHICLE_TTC_ASPECTS
    from items.vehicles import VehicleDescriptor
__all__ = (b'MaterialInfo', b'DEFAULT_MATERIAL_INFO', b'EmblemSlot', b'LodSettings', b'NodesAndGroups', b'Camouflage', b'DEFAULT_CAMOUFLAGE', b'SwingingSettings', b'I18nComponent', b'DeviceHealth', b'ModelStatesPaths', b'RocketAccelerationParams', b'ImpulseData', b'MechanicsParams', b'RechargeableNitroParams', b'ConcentrationModeParams', b'ImprovedRammingParams', b'PowerModeParams', b'BattleFuryParams', b'PillboxSiegeModeParams', b'StationaryReloadParams', b'ExtraShotClipParams', b'AccuracyStacksParams', b'SecondaryGunParams', b'SupportWeaponParams', b'ChargeableBurstParams', b'ChargeShotParams', b'OverheatStacksParams', b'TargetDesignatorParams', b'StanceDanceParams', b'TemperatureGunThermalState', b'TemperatureGunThermalStates', b'TemperatureGunParams', b'OverheatGunParams', b'HeatingZonesGunParams', b'StagedJetBoostersParams', b'LowChargeShotParams', b'PropellantGunParams', b'WheeledDashParams', b'AuxiliaryRocketLauncherParams', b'ShellSwitcherParams', b'ShellCalibrationParams', b'AutoreloaderSurgeParams', b'BustleFeedParams', b'SightPointerParams')
MaterialInfo = reflectedNamedTuple(b'MaterialInfo', (b'kind', b'armor', b'extra', b'multipleExtra', b'vehicleDamageFactor', b'useArmorHomogenization', b'useHitAngle', b'useAntifragmentationLining', b'mayRicochet', b'collideOnceOnly', b'checkCaliberForRicochet', b'checkCaliberForHitAngleNorm', b'damageKind', b'chanceToHitByProjectile', b'chanceToHitByExplosion', b'continueTraceIfNoHit', b'tags'))
DEFAULT_MATERIAL_INFO = MaterialInfo(0, 0, None, False, 0.0, False, False, False, False, False, False, False, 0, 0.0, 0.0, False, frozenset())
EmblemSlot = reflectedNamedTuple(b'EmblemSlot', (b'rayStart', b'rayEnd', b'rayUp', b'size', b'hideIfDamaged', b'type', b'isMirrored', b'isUVProportional', b'emblemId', b'slotId', b'applyToFabric', b'compatibleModels'))

class CustomizationSlotDescription(with_metaclass(ReflectionMetaclass, object)):
    __slots__ = (b'type', b'slotId', b'anchorPosition', b'anchorDirection', b'applyTo')

    def __init__(self, slotType=b'', slotId=0, anchorPosition=None, anchorDirection=None, applyTo=None, tags=None):
        super(CustomizationSlotDescription, self).__init__()
        self.type = slotType
        self.slotId = slotId
        self.anchorPosition = anchorPosition
        self.anchorDirection = anchorDirection
        self.applyTo = applyTo
        return


class ProjectionDecalSlotDescription(with_metaclass(ReflectionMetaclass, object)):
    __slots__ = (b'type', b'slotId', b'position', b'rotation', b'scale', b'scaleFactors', b'doubleSided', b'hiddenForUser', b'canBeMirroredVertically', b'showOn', b'tags', b'clipAngle', b'compatibleModels', b'itemId', b'options', b'anchorShift', b'modificationOrder')

    def __init__(self, slotType=b'', slotId=0, position=None, rotation=None, scale=None, scaleFactors=c11n_constants.DEFAULT_DECAL_SCALE_FACTORS, doubleSided=False, hiddenForUser=False, canBeMirroredVertically=False, showOn=None, tags=None, clipAngle=c11n_constants.DEFAULT_DECAL_CLIP_ANGLE, compatibleModels=(
 c11n_constants.SLOT_DEFAULT_ALLOWED_MODEL,), itemId=None, options=c11n_constants.Options.NONE, anchorShift=c11n_constants.DEFAULT_DECAL_ANCHOR_SHIFT, modificationOrder=0):
        super(ProjectionDecalSlotDescription, self).__init__()
        self.type = slotType
        self.slotId = slotId
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.scaleFactors = scaleFactors
        self.doubleSided = doubleSided
        self.hiddenForUser = hiddenForUser
        self.canBeMirroredVertically = canBeMirroredVertically
        self.showOn = showOn
        self.tags = tags or ()
        self.clipAngle = clipAngle
        self.compatibleModels = compatibleModels
        self.itemId = itemId
        self.options = options
        self.anchorShift = anchorShift
        self.modificationOrder = modificationOrder
        return


class AttachmentSlotDescription(with_metaclass(ReflectionMetaclass, object)):
    __slots__ = (b'type', b'slotId', b'position', b'rotation', b'scale', b'attachNode', b'hiddenForUser', b'enableVisTunnel', b'applyType', b'size', b'hangerId', b'hangerRotation', b'compatibleModels')

    def __init__(self, slotType=b'', slotId=0, position=None, rotation=None, scale=None, attachNode=None, hiddenForUser=False, enableVisTunnel=False, applyType=b'', size=b'', hangerId=0, hangerRotation=None, compatibleModels=(
 c11n_constants.SLOT_DEFAULT_ALLOWED_MODEL,)):
        super(AttachmentSlotDescription, self).__init__()
        self.type = slotType
        self.slotId = slotId
        self.position = position
        self.rotation = rotation
        self.scale = scale
        self.attachNode = attachNode
        self.hiddenForUser = hiddenForUser
        self.enableVisTunnel = enableVisTunnel
        self.applyType = applyType
        self.size = size
        self.hangerId = hangerId
        self.hangerRotation = hangerRotation
        self.compatibleModels = compatibleModels
        return

    @property
    def scaleFactorId(self):
        return AttachmentSize.ALL.index(self.size)


MiscSlot = reflectedNamedTuple(b'MiscSlot', (b'type', b'slotId', b'position', b'rotation', b'attachNode'))
LodSettings = namedtuple(b'LodSettings', (b'maxLodDistance', b'maxPriority'))
NodesAndGroups = reflectedNamedTuple(b'NodesAndGroups', (b'nodes', b'groups', b'activePostmortem', b'lodSettings'))
Camouflage = reflectedNamedTuple(b'Camouflage', (b'tiling', b'exclusionMask', b'density', b'aoTextureSize'))
DEFAULT_CAMOUFLAGE = Camouflage((1.0, 1.0, 0.0, 0.0), b'', (1.0, 1.0), (1, 1))
EMPTY_CAMOUFLAGE = Camouflage(None, None, None, None)
SwingingSettings = reflectedNamedTuple(b'SwingingSettings', (b'lodDist', b'sensitivityToImpulse', b'pitchParams', b'rollParams'))

class I18nString(object):
    __slots__ = (b'__value', b'__converted')

    def __init__(self, key):
        super(I18nString, self).__init__()
        self.__value = i18n.makeString(key)
        self.__converted = False
        return

    @property
    def value(self):
        if not self.__converted:
            self.__value = i18n.makeString(self.__value)
            self.__converted = True
        return self.__value


class _I18nConvertedFlags(object):
    UNDEFINED = 0
    USER_STRING = 1
    SHORT_STRING = 2
    DESCRIPTION = 4
    SHORT_DESCRIPTION_SPECIAL = 8
    LONG_DESCRIPTION_SPECIAL = 16
    SHORT_FILTER_ALERT_SPECIAL = 18
    LONG_FILTER_ALERT_SPECIAL = 20


class I18nComponent(object):
    __slots__ = (b'__userString', b'__shortString', b'__description', b'__converted', b'__shortDescriptionSpecial', b'__longDescriptionSpecial', b'__shortFilterAlertSpecial', b'__longFilterAlertSpecial')

    def __init__(self, userStringKey, descriptionKey, shortStringKey=b'', shortDescriptionSpecialKey=b'', longDescriptionSpecialKey=b'', shortFilterAlertKey=b'', longFilterAlertKey=b''):
        super(I18nComponent, self).__init__()
        self.__userString = userStringKey
        if shortStringKey:
            self.__shortString = shortStringKey
        else:
            self.__shortString = component_constants.EMPTY_STRING
        self.__description = descriptionKey
        self.__converted = _I18nConvertedFlags.UNDEFINED
        if shortDescriptionSpecialKey:
            self.__shortDescriptionSpecial = shortDescriptionSpecialKey
        else:
            self.__shortDescriptionSpecial = component_constants.EMPTY_STRING
        if longDescriptionSpecialKey:
            self.__longDescriptionSpecial = longDescriptionSpecialKey
        else:
            self.__longDescriptionSpecial = component_constants.EMPTY_STRING
        if shortFilterAlertKey:
            self.__longFilterAlertSpecial = shortFilterAlertKey
        else:
            self.__shortFilterAlertSpecial = component_constants.EMPTY_STRING
        if longFilterAlertKey:
            self.__longFilterAlertSpecial = longFilterAlertKey
        else:
            self.__longFilterAlertSpecial = component_constants.EMPTY_STRING
        return

    @property
    def userString(self):
        if self.__converted & _I18nConvertedFlags.USER_STRING == 0:
            self.__userString = i18n.makeString(self.__userString)
            self.__converted |= _I18nConvertedFlags.USER_STRING
        return self.__userString

    @property
    def shortString(self):
        if self.__shortString and self.__converted & _I18nConvertedFlags.SHORT_STRING == 0:
            self.__shortString = i18n.makeString(self.__shortString)
            self.__converted |= _I18nConvertedFlags.SHORT_STRING
        return self.__shortString or self.userString

    @property
    def description(self):
        if self.__converted & _I18nConvertedFlags.DESCRIPTION == 0:
            self.__description = i18n.makeString(self.__description)
            self.__converted |= _I18nConvertedFlags.DESCRIPTION
        return self.__description

    @property
    def shortDescriptionSpecial(self):
        if self.__converted & _I18nConvertedFlags.SHORT_DESCRIPTION_SPECIAL == 0:
            self.__shortDescriptionSpecial = i18n.makeString(self.__shortDescriptionSpecial)
            self.__converted |= _I18nConvertedFlags.SHORT_DESCRIPTION_SPECIAL
        return self.__shortDescriptionSpecial

    @property
    def longDescriptionSpecial(self):
        if self.__converted & _I18nConvertedFlags.LONG_DESCRIPTION_SPECIAL == 0:
            self.__longDescriptionSpecial = i18n.makeString(self.__longDescriptionSpecial)
            self.__converted |= _I18nConvertedFlags.LONG_DESCRIPTION_SPECIAL
        return self.__longDescriptionSpecial

    @property
    def longFilterAlertSpecial(self):
        if self.__converted & _I18nConvertedFlags.LONG_FILTER_ALERT_SPECIAL == 0:
            self.__longFilterAlertSpecial = i18n.makeString(self.__longFilterAlertSpecial)
            self.__converted |= _I18nConvertedFlags.LONG_FILTER_ALERT_SPECIAL
        return self.__longFilterAlertSpecial

    @property
    def shortFilterAlertSpecial(self):
        if self.__converted & _I18nConvertedFlags.SHORT_FILTER_ALERT_SPECIAL == 0:
            self.__shortFilterAlertSpecial = i18n.makeString(self.__shortFilterAlertSpecial)
            self.__converted |= _I18nConvertedFlags.SHORT_FILTER_ALERT_SPECIAL
        return self.__shortFilterAlertSpecial


class I18nExposedComponent(I18nComponent):
    __slots__ = (b'__userKey', b'__descriptionKey', b'__longDescriptionSpecialKey', b'__name', b'__shortDescriptionSpecialKey')

    def __init__(self, userStringKey, descriptionKey, longDescriptionSpecialKey=b'', name=b'', shortDescriptionSpecialKey=b''):
        super(I18nExposedComponent, self).__init__(userStringKey, descriptionKey, longDescriptionSpecialKey=longDescriptionSpecialKey, shortDescriptionSpecialKey=shortDescriptionSpecialKey)
        self.__userKey = userStringKey
        self.__descriptionKey = descriptionKey
        self.__longDescriptionSpecialKey = longDescriptionSpecialKey
        self.__name = name
        self.__shortDescriptionSpecialKey = shortDescriptionSpecialKey
        return

    @property
    def userKey(self):
        return self.__userKey

    @property
    def descriptionKey(self):
        return self.__descriptionKey

    @property
    def longDescriptionSpecialKey(self):
        return self.__longDescriptionSpecialKey

    @property
    def name(self):
        return self.__name

    @property
    def shortDescriptionSpecialKey(self):
        return self.__shortDescriptionSpecialKey


class DeviceHealth(object):
    __slots__ = (b'maxHealth', b'repairCost', b'maxRegenHealth', b'healthRegenPerSec', b'healthBurnPerSec', b'chanceToHit', b'hysteresisHealth', b'invulnerable', b'repairSpeedLimiter', b'repairTime')

    def __init__(self, maxHealth, repairCost=component_constants.ZERO_FLOAT, maxRegenHealth=component_constants.ZERO_INT):
        super(DeviceHealth, self).__init__()
        self.repairTime = None
        self.maxHealth = maxHealth
        self.repairCost = repairCost
        self.maxRegenHealth = maxRegenHealth
        self.healthRegenPerSec = component_constants.ZERO_FLOAT
        self.hysteresisHealth = None
        self.healthBurnPerSec = component_constants.ZERO_FLOAT
        self.chanceToHit = None
        self.invulnerable = False
        self.repairSpeedLimiter = None
        return

    def __repr__(self):
        return (b'DeviceHealth(maxHealth={}, repairCost={}, maxRegenHealth={}, healthRegenPerSec={}, hysteresisHealth={})').format(self.maxHealth, self.repairCost, self.maxRegenHealth, self.healthRegenPerSec, self.hysteresisHealth)

    @property
    def maxRepairCost(self):
        return (self.maxHealth - self.maxRegenHealth) * self.repairCost


DEFAULT_DEVICE_HEALTH = DeviceHealth(1)

class ModelStatesPaths(with_metaclass(ReflectionMetaclass, object)):
    __slots__ = (b'__undamaged', b'__destroyed', b'__exploded')

    def __init__(self, undamaged, destroyed, exploded):
        super(ModelStatesPaths, self).__init__()
        self.__undamaged = tuple(path_builder.makeIndexes(undamaged))
        self.__destroyed = tuple(path_builder.makeIndexes(destroyed))
        self.__exploded = tuple(path_builder.makeIndexes(exploded))
        return

    def __repr__(self):
        return (b'ModelStatesPaths(undamaged={}, destroyed={}, exploded={})').format(self.undamaged, self.destroyed, self.exploded)

    @property
    def undamaged(self):
        return path_builder.makePath(*self.__undamaged)

    @property
    def destroyed(self):
        return path_builder.makePath(*self.__destroyed)

    @property
    def exploded(self):
        return path_builder.makePath(*self.__exploded)

    if IS_EDITOR:

        def setUndamaged(self, value):
            self.__undamaged = tuple(path_builder.makeIndexes(value))
            return

        def setDestroyed(self, value):
            self.__destroyed = tuple(path_builder.makeIndexes(value))
            return

        def setExploded(self, value):
            self.__exploded = tuple(path_builder.makeIndexes(value))
            return

    def getPathByStateName(self, stateName):
        path = getattr(self, stateName, None)
        if path is None:
            raise SoftException((b'State {} is not found').format(stateName))
        return path


ImpulseData = namedtuple(b'ImpulseData', (b'magnitude', b'applyPoint', b'duration'))

def readImpulseData(ctx, section, subsection=b'impulse'):
    impulseCtx, impulseSection = _xml.getSubSectionWithContext(ctx, section, subsection)
    impulse = ImpulseData(magnitude=_xml.readNonNegativeFloat(impulseCtx, impulseSection, b'magnitude'), applyPoint=_xml.readVector3(impulseCtx, impulseSection, b'applyPoint', component_constants.ZERO_VECTOR3), duration=_xml.readNonNegativeFloat(impulseCtx, impulseSection, b'duration'))
    return impulse


SpeedTriggerData = namedtuple(b'SpeedTriggerData', (b'enableSpeed', b'hysteresisSpeed'))
TickedImpulseData = namedtuple(b'TickedImpulseData', (b'cooldown', b'magnitudePerTick', b'applyPoint'))

def readTickedImpulseData(ctx, section, subsection=b'tickedImpulse'):
    tickedImpulseCtx, tickedImpulseSection = _xml.getSubSectionWithContext(ctx, section, subsection)
    tickedImpulse = TickedImpulseData(cooldown=_xml.readNonNegativeFloat(tickedImpulseCtx, tickedImpulseSection, b'cooldown'), magnitudePerTick=_xml.readTupleOfPositiveFloats(tickedImpulseCtx, tickedImpulseSection, b'magnitudePerTick'), applyPoint=_xml.readVector3(tickedImpulseCtx, tickedImpulseSection, b'applyPoint'))
    return tickedImpulse


def readShellCDsByName(ctx, section, subsection=b'shells'):
    from items.vehicles import getShellByName
    shellsCDs = set()
    shellsList = _xml.readStringOrEmpty(ctx, section, subsection).strip().split()
    for shellData in shellsList:
        shellNation, shellName = shellData.split(b':')
        shellDescr = getShellByName(shellName, shellNation)
        if shellDescr is None:
            _xml.raiseWrongXml(ctx, b'', (b"Unknown shell's name: {}!").format(shellData))
        shellsCDs.add(shellDescr.compactDescr)

    return shellsCDs


class RocketAccelerationParams(object):
    __slots__ = (b'deployTime', b'reloadTime', b'reuseCount', b'duration', b'impulse', b'modifiers', b'kpi')

    def __init__(self, deployTime, reloadTime, reuseCount, duration, impulse, modifiers, kpi):
        self.deployTime = deployTime
        self.reloadTime = reloadTime
        self.reuseCount = reuseCount
        self.duration = duration
        self.impulse = impulse
        self.modifiers = modifiers
        self.kpi = kpi
        return

    def __repr__(self):
        return (b'deployTime={}, reloadTime={},reuseCount={}, duration={}, impulse={}, modifiers={}').format(self.deployTime, self.reloadTime, self.reuseCount, self.duration, self.impulse, self.modifiers)


class MechanicsParams(object):
    __slots__ = (b'__origin', b'modifiers')
    MECHANICS_NAME = None
    COMPONENT_TYPE_ID = None

    def __init__(self, modifiers=None):
        self.__origin = None
        self.modifiers = modifiers
        return

    @classmethod
    def getSubClasses(cls, uniqueParamNames=None):
        if uniqueParamNames is None:
            uniqueParamNames = set()
        paramsClasses = []
        for paramsCls in cls.__subclasses__():
            if paramsCls.MECHANICS_NAME is None:
                paramsClasses.extend(paramsCls.getSubClasses(uniqueParamNames))
            elif paramsCls.MECHANICS_NAME not in uniqueParamNames:
                paramsClasses.append(paramsCls)
                uniqueParamNames.add(paramsCls.MECHANICS_NAME)

        return paramsClasses

    @classmethod
    def readMechanicsParams(cls, xmlCtx, section, readModifiers):
        if not cls.MECHANICS_NAME:
            return
        else:
            mechanicCtx, mechanicSection = _xml.getSubSectionWithContext(xmlCtx, section, cls.MECHANICS_NAME, throwIfMissing=False)
            if mechanicSection is None:
                return
            params = cls._readMechanicsParams(mechanicCtx, mechanicSection, readModifiers)
            return params

    def createMechanicsParamsOrigin(self):
        origin = self.__origin
        if origin:
            params = pickle.loads(origin)
            params.__origin = origin
            return params
        else:
            return

    def getMechanicsMiscAttributes(self):
        return self.getDefaultMechanicsMiscAttributes()

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {}

    def isActiveMechanics(self, vehicleDescriptor):
        return True

    def applyMiscAttrToMechanics(self, miscAttrs):
        for attr in self.getMechanicsMiscAttributes():
            self._applyMechanicsAttrs(attr, miscAttrs[attr])

        return

    def applyDynModifiersToMechanics(self, dynModifiers):
        modifiers = self.modifiers
        if not dynModifiers or self.modifiers is None:
            return
        for modifier in dynModifiers:
            modifierFilter = modifier[4]
            if modifierFilter == self.MECHANICS_NAME:
                modifiers.append(modifier)

        return

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect):
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        return

    def _applyMechanicsAttrs(self, attr, value):
        return

    def _saveOrigin(self):
        self.__origin = pickle.dumps(self, -1)
        return

    def __repr__(self):
        return (b'{}({})').format(self.__class__.__name__, (b', ').join((b'{}={}').format(slotName, getattr(self, slotName)) for slotName in self.__slots__ if not slotName.startswith(b'_')))


class GunMechanicsParams(MechanicsParams):
    __slots__ = (b'gunInstallationSlot',)
    COMPONENT_TYPE_ID = ITEM_TYPES.vehicleGun

    def __init__(self, modifiers=None):
        super(GunMechanicsParams, self).__init__(modifiers)
        self.gunInstallationSlot = None
        return

    def setGunInstallationSlot(self, gunInstallationSlot):
        self.gunInstallationSlot = gunInstallationSlot
        return


class RechargeableNitroParams(MechanicsParams):
    __slots__ = (b'deployTime', b'reloadTime', b'duration', b'threshold', b'cooldown', b'addMaxSpeedForwardBonus', b'addRotationSpeedBonus', b'impulse')
    MECHANICS_NAME = b'rechargeableNitro'

    def __init__(self, deployTime, reloadTime, duration, cooldown, addMaxSpeedForwardBonus, addRotationSpeedBonus, impulse, modifiers, threshold=0):
        super(RechargeableNitroParams, self).__init__(modifiers)
        self.deployTime = deployTime
        self.reloadTime = reloadTime
        self.duration = duration
        self.threshold = threshold
        self.cooldown = cooldown
        self.addMaxSpeedForwardBonus = addMaxSpeedForwardBonus
        self.addRotationSpeedBonus = addRotationSpeedBonus
        self.impulse = impulse
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        impulse = readImpulseData(ctx, section)
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        return cls(deployTime=_xml.readNonNegativeFloat(ctx, section, b'deployTime'), reloadTime=_xml.readPositiveFloat(ctx, section, b'reloadTime'), duration=_xml.readPositiveFloat(ctx, section, b'duration'), threshold=_xml.readPositiveFloat(ctx, section, b'threshold'), cooldown=_xml.readPositiveFloat(ctx, section, b'cooldown'), addMaxSpeedForwardBonus=_xml.readFloat(ctx, section, b'addMaxSpeedForwardBonus'), addRotationSpeedBonus=_xml.readFloat(ctx, section, b'addRotationSpeedBonus'), impulse=impulse, modifiers=modifiers)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'rechargeableNitro/duration': 0.0, 
           b'rechargeableNitro/reloadTime': 0.0, 
           b'rechargeableNitro/addMaxSpeedForwardBonus': 0.0, 
           b'rechargeableNitro/addRotationSpeedBonus': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'rechargeableNitro/duration':
            self.duration += value
        elif attr == b'rechargeableNitro/reloadTime':
            self.reloadTime += value
        elif attr == b'rechargeableNitro/addMaxSpeedForwardBonus':
            self.addMaxSpeedForwardBonus += value
            if self.addMaxSpeedForwardBonus or value:
                self.__applyMulModifier(b'dynAttrs/', b'vehicle/maxSpeed/forward', self.addMaxSpeedForwardBonus)
        elif attr == b'rechargeableNitro/addRotationSpeedBonus':
            self.addRotationSpeedBonus += value
            if self.addRotationSpeedBonus or value:
                self.__applyMulModifier(b'dynAttrs/', b'vehicle/rotationSpeed', self.addRotationSpeedBonus)
        return

    def __applyMulModifier(self, modifierType, modifierName, bonusValue):
        mulValue = max(0.0, 1.0 + bonusValue)
        newModifier = (b'mul', modifierType, modifierName, mulValue, b'rechargeableNitro')
        foundIndex = None
        for idx, (opCode, modType, modName, _, _) in enumerate(self.modifiers):
            if opCode == b'mul' and modType == modifierType and modName == modifierName:
                foundIndex = idx
                break

        if foundIndex is not None:
            self.modifiers[foundIndex] = newModifier
        else:
            self.modifiers.append(newModifier)
        return

    def __repr__(self):
        return (b'deployTime={}, reloadTime={}, duration={}, threshold={}, impulse={}, cooldown={}, addMaxSpeedForwardBonus={}, addRotationSpeedBonus={}, modifiers={}').format(self.deployTime, self.reloadTime, self.duration, self.threshold, self.impulse, self.cooldown, self.addMaxSpeedForwardBonus, self.addRotationSpeedBonus, self.modifiers)


class ConcentrationModeParams(MechanicsParams):
    __slots__ = (b'deployTime', b'reloadTime', b'duration')
    MECHANICS_NAME = b'concentrationMode'

    def __init__(self, deployTime, reloadTime, duration, modifiers):
        super(ConcentrationModeParams, self).__init__(modifiers)
        self.deployTime = deployTime
        self.reloadTime = reloadTime
        self.duration = duration
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'concentrationModeDeployTime': 0.0, 
           b'concentrationModeReloadTime': 0.0, 
           b'concentrationModeDuration': 0.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        return cls(deployTime=_xml.readPositiveFloat(ctx, section, b'deployTime'), reloadTime=_xml.readPositiveFloat(ctx, section, b'reloadTime'), duration=_xml.readPositiveFloat(ctx, section, b'duration'), modifiers=modifiers)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'concentrationModeDeployTime':
            self.deployTime += value
        elif attr == b'concentrationModeReloadTime':
            self.reloadTime += value
        elif attr == b'concentrationModeDuration':
            self.duration += value
        return


class ImprovedRammingParams(MechanicsParams):
    __slots__ = (b'damageBonusStageSize', b'damageBonusBasicFactor', b'damageBonusChangeFactor', b'trackDamageBonusStageSize', b'trackDamageBonusBasicFactor', b'trackDamageBonusChangeFactor', b'reductionDamageBonusStageSize', b'reductionDamageBonusBasicFactor', b'reductionDamageBonusChangeFactor', b'damageValueToShowAnimation', b'effectSpeedThreshold')
    MECHANICS_NAME = b'improvedRamming'

    def __init__(self, damageBonusStageSize, damageBonusBasicFactor, damageBonusChangeFactor, trackDamageBonusStageSize, trackDamageBonusBasicFactor, trackDamageBonusChangeFactor, reductionDamageBonusStageSize, reductionDamageBonusBasicFactor, reductionDamageBonusChangeFactor, damageValueToShowAnimation, effectSpeedThreshold):
        super(ImprovedRammingParams, self).__init__()
        self.damageBonusStageSize = damageBonusStageSize
        self.damageBonusBasicFactor = damageBonusBasicFactor
        self.damageBonusChangeFactor = damageBonusChangeFactor
        self.trackDamageBonusStageSize = trackDamageBonusStageSize
        self.trackDamageBonusBasicFactor = trackDamageBonusBasicFactor
        self.trackDamageBonusChangeFactor = trackDamageBonusChangeFactor
        self.reductionDamageBonusStageSize = reductionDamageBonusStageSize
        self.reductionDamageBonusBasicFactor = reductionDamageBonusBasicFactor
        self.reductionDamageBonusChangeFactor = reductionDamageBonusChangeFactor
        self.damageValueToShowAnimation = damageValueToShowAnimation
        self.effectSpeedThreshold = effectSpeedThreshold
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'improvedRammingDamageBonus/basicFactor': 1.0, 
           b'improvedRammingTrackDamageBonus/basicFactor': 1.0, 
           b'improvedRammingDamageReductionBonus/basicFactor': 1.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        _defaultStageSize = 10.0
        _defaultDamageToAnimation = 0
        _defaultSpeedToEffect = 30
        damageBonusStageSize = _xml.readNonNegativeFloat(ctx, section, b'damageBonusStageSize', _defaultStageSize)
        damageBonusBasicFactor = _xml.readNonNegativeFloat(ctx, section, b'damageBonusBasicFactor')
        damageBonusChangeFactor = _xml.readNonNegativeFloat(ctx, section, b'damageBonusChangeFactor')
        trackDamageBonusStageSize = _xml.readNonNegativeFloat(ctx, section, b'trackDamageBonusStageSize', _defaultStageSize)
        trackDamageBonusBasicFactor = _xml.readNonNegativeFloat(ctx, section, b'trackDamageBonusBasicFactor')
        trackDamageBonusChangeFactor = _xml.readNonNegativeFloat(ctx, section, b'trackDamageBonusChangeFactor')
        reductionDamageBonusStageSize = _xml.readNonNegativeFloat(ctx, section, b'reductionDamageBonusStageSize', _defaultStageSize)
        reductionDamageBonusBasicFactor = _xml.readNonNegativeFloat(ctx, section, b'reductionDamageBonusBasicFactor')
        reductionDamageBonusChangeFactor = _xml.readNonNegativeFloat(ctx, section, b'reductionDamageBonusChangeFactor')
        damageValueToShowAnimation = _xml.readNonNegativeInt(ctx, section, b'damageValueToShowAnimation', _defaultDamageToAnimation)
        effectSpeedThreshold = _xml.readNonNegativeInt(ctx, section, b'effectSpeedThreshold', _defaultSpeedToEffect)
        return cls(damageBonusStageSize=damageBonusStageSize * component_constants.KMH_TO_MS, damageBonusBasicFactor=damageBonusBasicFactor, damageBonusChangeFactor=damageBonusChangeFactor, trackDamageBonusStageSize=trackDamageBonusStageSize * component_constants.KMH_TO_MS, trackDamageBonusBasicFactor=trackDamageBonusBasicFactor, trackDamageBonusChangeFactor=trackDamageBonusChangeFactor, reductionDamageBonusStageSize=reductionDamageBonusStageSize * component_constants.KMH_TO_MS, reductionDamageBonusBasicFactor=reductionDamageBonusBasicFactor, reductionDamageBonusChangeFactor=reductionDamageBonusChangeFactor, damageValueToShowAnimation=damageValueToShowAnimation, effectSpeedThreshold=effectSpeedThreshold * component_constants.KMH_TO_MS)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'improvedRammingDamageBonus/basicFactor':
            self.damageBonusBasicFactor *= value
        elif attr == b'improvedRammingTrackDamageBonus/basicFactor':
            self.trackDamageBonusBasicFactor *= value
        elif attr == b'improvedRammingDamageReductionBonus/basicFactor':
            self.reductionDamageBonusBasicFactor *= value
        return


class PowerModeParams(MechanicsParams):
    __slots__ = (b'modeThreshold', b'modeDuration', b'accelerationFactor', b'attenuationFactor', b'speedThreshold', b'gracePeriod', b'vehicleParams')
    MECHANICS_NAME = b'powerMode'
    DEFAULT_VEHICLE_PARAMS = {b'vehicleSpeed': 1.0, 
       b'dispersion': 1.0, 
       b'rotationSpeed': 1.0, 
       b'enginePower': 1.0}

    def __init__(self, modeThreshold, modeDuration, accelerationFactor, attenuationFactor, speedThreshold, gracePeriod, vehicleParams):
        super(PowerModeParams, self).__init__()
        self.modeThreshold = modeThreshold
        self.modeDuration = modeDuration
        self.accelerationFactor = accelerationFactor
        self.attenuationFactor = attenuationFactor
        self.speedThreshold = speedThreshold
        self.gracePeriod = gracePeriod
        self.vehicleParams = dict(PowerModeParams.DEFAULT_VEHICLE_PARAMS, **vehicleParams)
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'powerMode/modeThreshold': 0.0, 
           b'powerMode/modeDuration': 0.0, 
           b'powerMode/speedThreshold': 0.0, 
           b'powerMode/gracePeriod': 0.0, 
           b'powerMode/accelerationFactor': 1.0, 
           b'powerMode/attenuationFactor': 1.0, 
           b'powerMode/vehicleSpeed': 1.0, 
           b'powerMode/rotationSpeed': 1.0, 
           b'powerMode/enginePower': 1.0, 
           b'powerMode/dispersion': 1.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        modeThreshold = _xml.readPositiveFloat(ctx, section, b'modeThreshold')
        modeDuration = _xml.readPositiveFloat(ctx, section, b'modeDuration')
        accelerationFactor = _xml.readPositiveFloat(ctx, section, b'accelerationFactor', 1.0)
        attenuationFactor = _xml.readPositiveFloat(ctx, section, b'attenuationFactor', 1.0)
        speedThreshold = _xml.readPositiveFloat(ctx, section, b'speedThreshold', 0.0)
        gracePeriod = _xml.readPositiveFloat(ctx, section, b'gracePeriod', 0.0)
        vehicleParams = {}
        vehicleParamSection = section[b'vehicleParams']
        for paramName in vehicleParamSection.keys():
            vehicleParams[paramName] = vehicleParamSection.readFloat(paramName)

        return cls(modeThreshold=modeThreshold, modeDuration=modeDuration, accelerationFactor=accelerationFactor, attenuationFactor=attenuationFactor, speedThreshold=speedThreshold * component_constants.KMH_TO_MS, gracePeriod=gracePeriod, vehicleParams=vehicleParams)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'powerMode/modeThreshold':
            self.modeThreshold += value
        elif attr == b'powerMode/modeDuration':
            self.modeDuration += value
        elif attr == b'powerMode/speedThreshold':
            self.speedThreshold += value * component_constants.KMH_TO_MS
        elif attr == b'powerMode/gracePeriod':
            self.gracePeriod += value
        elif attr == b'powerMode/accelerationFactor':
            self.accelerationFactor *= value
        elif attr == b'powerMode/attenuationFactor':
            self.attenuationFactor *= value
        elif attr == b'powerMode/vehicleSpeed':
            self.vehicleParams[b'vehicleSpeed'] *= value
        elif attr == b'powerMode/rotationSpeed':
            self.vehicleParams[b'rotationSpeed'] *= value
        elif attr == b'powerMode/enginePower':
            self.vehicleParams[b'enginePower'] *= value
        elif attr == b'powerMode/dispersion':
            self.vehicleParams[b'dispersion'] *= value
        return


class BattleFuryParams(MechanicsParams):
    __slots__ = (b'maxLevel', b'duration', b'reloadSpdBonus', b'gainPerHit', b'gainPerKill')
    MECHANICS_NAME = b'battleFury'

    def __init__(self, maxLevel, duration, reloadSpdBonus, gainPerHit, gainPerKill):
        super(BattleFuryParams, self).__init__()
        self.maxLevel = maxLevel
        self.duration = duration
        self.reloadSpdBonus = reloadSpdBonus
        self.gainPerHit = gainPerHit
        self.gainPerKill = gainPerKill
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'battleFury/gainPerKill': 0, 
           b'battleFury/duration': 0.0, 
           b'battleFury/reloadSpdBonus': 0.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        maxLevel = _xml.readPositiveInt(ctx, section, b'maxLevel')
        duration = _xml.readPositiveFloat(ctx, section, b'duration')
        reloadSpdBonus = _xml.readNonNegativeFloat(ctx, section, b'reloadSpdBonus')
        gainPerHit = _xml.readNonNegativeInt(ctx, section, b'gainPerHit')
        gainPerKill = _xml.readNonNegativeInt(ctx, section, b'gainPerKill')
        return cls(maxLevel=maxLevel, duration=duration, reloadSpdBonus=reloadSpdBonus, gainPerHit=gainPerHit, gainPerKill=gainPerKill)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'battleFury/gainPerKill':
            self.gainPerKill += value
        elif attr == b'battleFury/duration':
            self.duration += value
        elif attr == b'battleFury/reloadSpdBonus':
            self.reloadSpdBonus += value
        return


class PillboxSiegeModeParams(MechanicsParams):
    __slots__ = (b'switchDriveToPillboxTime', b'switchSiegeToPillboxTime', b'switchPillboxToSiegeTime', b'switchPillboxToDriveTime')
    MECHANICS_NAME = b'pillboxSiegeMode'

    def __init__(self, switchDriveToPillboxTime, switchSiegeToPillboxTime, switchPillboxToSiegeTime, switchPillboxToDriveTime, modifiers):
        super(PillboxSiegeModeParams, self).__init__(modifiers)
        self.switchDriveToPillboxTime = switchDriveToPillboxTime
        self.switchSiegeToPillboxTime = switchSiegeToPillboxTime
        self.switchPillboxToSiegeTime = switchPillboxToSiegeTime
        self.switchPillboxToDriveTime = switchPillboxToDriveTime
        self.modifiers = modifiers
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'pillboxSiegeMode/switchDriveToPillboxTime': 0.0, 
           b'pillboxSiegeMode/switchSiegeToPillboxTime': 0.0, 
           b'pillboxSiegeMode/switchPillboxToSiegeTime': 0.0, 
           b'pillboxSiegeMode/switchPillboxToDriveTime': 0.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        switchDriveToPillboxTime = _xml.readNonNegativeFloat(ctx, section, b'switchDriveToPillboxTime')
        switchSiegeToPillboxTime = _xml.readNonNegativeFloat(ctx, section, b'switchSiegeToPillboxTime')
        switchPillboxToSiegeTime = _xml.readNonNegativeFloat(ctx, section, b'switchPillboxToSiegeTime')
        switchPillboxToDriveTime = _xml.readNonNegativeFloat(ctx, section, b'switchPillboxToDriveTime')
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        return cls(switchDriveToPillboxTime=switchDriveToPillboxTime, switchSiegeToPillboxTime=switchSiegeToPillboxTime, switchPillboxToSiegeTime=switchPillboxToSiegeTime, switchPillboxToDriveTime=switchPillboxToDriveTime, modifiers=modifiers)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'pillboxSiegeMode/switchDriveToPillboxTime':
            self.switchDriveToPillboxTime += value
        elif attr == b'pillboxSiegeMode/switchSiegeToPillboxTime':
            self.switchSiegeToPillboxTime += value
        elif attr == b'pillboxSiegeMode/switchPillboxToSiegeTime':
            self.switchPillboxToSiegeTime += value
        elif attr == b'pillboxSiegeMode/switchPillboxToDriveTime':
            self.switchPillboxToDriveTime += value
        return


class StationaryReloadParams(GunMechanicsParams):
    __slots__ = (b'preparingSpeedFactor', b'finishingSpeedFactor', b'preparingDelay', b'finishingDelay', b'fixAngles')
    MECHANICS_NAME = b'stationaryReload'

    def __init__(self, preparingSpeedFactor, finishingSpeedFactor, preparingDelay, finishingDelay, fixAngles):
        super(StationaryReloadParams, self).__init__()
        self.preparingSpeedFactor = preparingSpeedFactor
        self.finishingSpeedFactor = finishingSpeedFactor
        self.preparingDelay = preparingDelay
        self.finishingDelay = finishingDelay
        self.fixAngles = fixAngles
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'stationaryReload/preparingDelayFactor': 1.0, 
           b'stationaryReload/finishingDelayFactor': 1.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        return cls(preparingSpeedFactor=_xml.readNonNegativeFloat(ctx, section, b'preparingSpeedFactor'), finishingSpeedFactor=_xml.readNonNegativeFloat(ctx, section, b'finishingSpeedFactor'), preparingDelay=_xml.readNonNegativeFloat(ctx, section, b'preparingDelay'), finishingDelay=_xml.readNonNegativeFloat(ctx, section, b'finishingDelay'), fixAngles=tuple(map(radians, _xml.readVector2(ctx, section, b'fixAngles'))))

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'stationaryReload/preparingDelayFactor':
            self.preparingDelay *= value
            self.preparingSpeedFactor /= value
        elif attr == b'stationaryReload/finishingDelayFactor':
            self.finishingDelay *= value
            self.finishingSpeedFactor /= value
        return


class ExtraShotClipParams(GunMechanicsParams):
    __slots__ = (b'extraReloadTime',)
    MECHANICS_NAME = b'extraShotClip'

    def __init__(self, extraReloadTime):
        super(ExtraShotClipParams, self).__init__()
        self.extraReloadTime = extraReloadTime
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'gun/extraShotClip/extraReloadTime': 0.0}

    def isActiveMechanics(self, vehicleDescriptor):
        return b'clip' in vehicleDescriptor.gun.tags and vehicleDescriptor.gun.clip[0] > 1

    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect):
        factors[b'gun/extraReloadTime'] += self.extraReloadTime
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        extraReloadTime = _xml.readNonNegativeFloat(ctx, section, b'extraReloadTime', 0.0)
        return cls(extraReloadTime=extraReloadTime)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'gun/extraShotClip/extraReloadTime':
            self.extraReloadTime += value
        return


class AccuracyStacksParams(MechanicsParams):
    __slots__ = (b'levelMax', b'levelInitial', b'levelAfterShot', b'aimLevelBonus', b'aimBonusCap', b'gainMaxSpd', b'gainTime', b'stabilizeBonus')
    MECHANICS_NAME = b'accuracyStacks'

    def __init__(self, levelMax, levelInitial, levelAfterShot, aimLevelBonus, aimBonusCap, gainMaxSpd, gainTime, stabilizeBonus):
        super(AccuracyStacksParams, self).__init__()
        self.levelMax = levelMax
        self.levelInitial = levelInitial
        self.levelAfterShot = levelAfterShot
        self.aimLevelBonus = aimLevelBonus
        self.aimBonusCap = aimBonusCap
        self.gainMaxSpd = gainMaxSpd
        self.gainTime = gainTime
        self.stabilizeBonus = stabilizeBonus
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'accuracyStacks/aimLevelBonus': 0.0, 
           b'accuracyStacks/gainMaxSpd': 0.0, 
           b'accuracyStacks/gainTime': 0.0, 
           b'accuracyStacks/stabilizeBonus': 0.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        levelMax = _xml.readPositiveInt(ctx, section, b'levelMax')
        levelInitial = _xml.readNonNegativeInt(ctx, section, b'levelInitial')
        levelAfterShot = _xml.readNonNegativeInt(ctx, section, b'levelAfterShot')
        aimLevelBonus = _xml.readNonNegativeFloat(ctx, section, b'aimLevelBonus')
        aimBonusCap = _xml.readNonNegativeFloat(ctx, section, b'aimBonusCap', 0.99)
        gainMaxSpd = _xml.readNonNegativeFloat(ctx, section, b'gainMaxSpd')
        gainTime = _xml.readPositiveFloat(ctx, section, b'gainTime')
        stabilizeBonus = _xml.readNonNegativeFloat(ctx, section, b'stabilizeBonus')
        return cls(levelMax=levelMax, levelInitial=levelInitial, levelAfterShot=levelAfterShot, aimLevelBonus=aimLevelBonus, aimBonusCap=aimBonusCap, gainMaxSpd=gainMaxSpd, gainTime=gainTime, stabilizeBonus=stabilizeBonus)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'accuracyStacks/aimLevelBonus':
            self.aimLevelBonus += value
        elif attr == b'accuracyStacks/gainMaxSpd':
            self.gainMaxSpd += value
        elif attr == b'accuracyStacks/gainTime':
            self.gainTime += value
        elif attr == b'accuracyStacks/stabilizeBonus':
            self.stabilizeBonus += value
        return


class SecondaryGunParams(with_metaclass(ReflectionMetaclass, GunMechanicsParams)):
    __slots__ = (b'initiationTime', b'dependentOnMainGun')
    MECHANICS_NAME = b'secondaryGun'

    def __init__(self, initiationTime, dependentOnMainGun):
        super(SecondaryGunParams, self).__init__()
        self.initiationTime = initiationTime
        self.dependentOnMainGun = dependentOnMainGun
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return cls._generateMechanicMiscAttributes()

    def getMechanicsMiscAttributes(self):
        return self._generateMechanicMiscAttributes(self.gunInstallationSlot.gun)

    def isActiveMechanics(self, vehicleDescriptor):
        gunInstallationSlot = self.gunInstallationSlot
        return not gunInstallationSlot.isMainInstallation() and b'secondaryGun' in gunInstallationSlot.gun.tags

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        return cls(initiationTime=_xml.readNonNegativeFloat(ctx, section, b'initiationTime'), dependentOnMainGun=_xml.readBool(ctx, section, b'dependentOnMainGun'))

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'secondaryGun/initiationTime':
            self.initiationTime *= value
        return

    @staticmethod
    def _generateMechanicMiscAttributes(gunDescr=None):
        gunShotDispersionFactors = gunDescr.shotDispersionFactors if gunDescr else {}
        return {b'secondaryGun/initiationTime': 1.0, 
           b'secondaryGunReloadTimeFactor': 1.0, 
           b'secondaryGunAimingTimeFactor': 1.0, 
           b'secondaryGun/invisibilityFactorAtShot': (gunDescr.invisibilityFactorAtShot if gunDescr else 1.0), 
           b'secondaryGun/shotDispersionFactors/afterShot': (gunShotDispersionFactors.get(b'afterShot', 1.0)), 
           b'secondaryGun/shotDispersionFactors/whileGunDamaged': (gunShotDispersionFactors.get(b'whileGunDamaged', 1.0)), 
           b'secondaryGun/shotDispersionFactors/turretRotation': (gunShotDispersionFactors.get(b'turretRotation', 0.0)), 
           b'secondaryGunMultShotDispersionFactor': 1.0, 
           b'secondaryGunAdditiveShotDispersionFactor': 1.0}


class SupportWeaponParams(MechanicsParams):
    __slots__ = ()
    MECHANICS_NAME = b'supportWeapon'

    def __init__(self):
        super(SupportWeaponParams, self).__init__()
        self._saveOrigin()
        return

    def isActiveMechanics(self, vehicleDescriptor):
        mechanicsParams = vehicleDescriptor.mechanicsParams
        return SecondaryGunParams.MECHANICS_NAME in mechanicsParams and mechanicsParams[SecondaryGunParams.MECHANICS_NAME].isActiveMechanics(vehicleDescriptor)

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        return cls()


class ChargeableBurstParams(GunMechanicsParams):
    __slots__ = (b'penetrationCount', b'burstDispersionFactor')
    MECHANICS_NAME = b'chargeableBurst'

    def __init__(self, penetrationCount, burstDispersionFactor, modifiers):
        super(ChargeableBurstParams, self).__init__(modifiers)
        self.penetrationCount = penetrationCount
        self.burstDispersionFactor = burstDispersionFactor
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        penetrationCount = _xml.readNonNegativeInt(ctx, section, b'penetrationCount')
        burstDispersionFactor = _xml.readNonNegativeFloat(ctx, section, b'burstDispersionFactor')
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        return cls(penetrationCount=penetrationCount, burstDispersionFactor=burstDispersionFactor, modifiers=modifiers)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'chargeableBurst/penetrationCount': 0, 
           b'chargeableBurst/burstDispersionFactor': 1.0}

    def isActiveMechanics(self, vehicleDescriptor):
        return vehicleDescriptor.hasBurst

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'chargeableBurst/penetrationCount':
            self.penetrationCount += value
        if attr == b'chargeableBurst/burstDispersionFactor':
            self.burstDispersionFactor *= value
        return


class LowChargeShotParams(GunMechanicsParams):
    __slots__ = (b'almostFinishedTime', b'reloadTimeCoefficient')
    MECHANICS_NAME = b'lowChargeShot'

    def __init__(self, almostFinishedTime, reloadTimeCoefficient, modifiers):
        super(LowChargeShotParams, self).__init__(modifiers)
        self.almostFinishedTime = almostFinishedTime
        self.reloadTimeCoefficient = reloadTimeCoefficient
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        almostFinishedTime = _xml.readNonNegativeFloat(ctx, section, b'almostFinishedTime')
        reloadTimeCoefficient = _xml.readNonNegativeFloat(ctx, section, b'reloadTimeCoefficient')
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        return cls(almostFinishedTime=almostFinishedTime, reloadTimeCoefficient=reloadTimeCoefficient, modifiers=modifiers)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'lowChargeShot/reloadTimeCoefficient': 1.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'lowChargeShot/reloadTimeCoefficient':
            self.reloadTimeCoefficient *= value
        return


class ChargeShotParams(MechanicsParams):
    __slots__ = (b'timePerLevel', b'damageFactorsPerLevel', b'maxLevel', b'shotBlockTime')
    MECHANICS_NAME = b'chargeShot'

    def __init__(self, timePerLevel, damageFactorsPerLevel, shotBlockTime):
        super(ChargeShotParams, self).__init__()
        self.timePerLevel = timePerLevel
        self.damageFactorsPerLevel = damageFactorsPerLevel
        self.maxLevel = len(timePerLevel) - 1
        self.shotBlockTime = shotBlockTime
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        timePerLevel = list(_xml.readTupleOfNonNegativeFloats(ctx, section, b'timePerLevel'))
        damageFactorsPerLevel = list(_xml.readTupleOfNonNegativeFloats(ctx, section, b'damageFactorsPerLevel'))
        shotBlockTime = _xml.readNonNegativeFloat(ctx, section, b'shotBlockTime')
        return cls(timePerLevel, damageFactorsPerLevel, shotBlockTime)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'chargeShot/damageFactorLevel1': 0.0, 
           b'chargeShot/damageFactorLevel2': 0.0, 
           b'chargeShot/damageFactorLevel3': 0.0, 
           b'chargeShot/timeToShotBlock': 0.0, 
           b'chargeShot/shotBlockTime': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'chargeShot/damageFactorLevel1':
            self.damageFactorsPerLevel[1] += value
        elif attr == b'chargeShot/damageFactorLevel2':
            self.damageFactorsPerLevel[2] += value
        elif attr == b'chargeShot/damageFactorLevel3':
            self.damageFactorsPerLevel[3] += value
        elif attr == b'chargeShot/timeToShotBlock':
            self.timePerLevel[3] += value
        elif attr == b'chargeShot/shotBlockTime':
            self.shotBlockTime += value
        return


class OverheatStacksParams(MechanicsParams):
    __slots__ = (b'levelMax', b'levelInc', b'levelDec', b'aimLevelBonus', b'dmgLevelBonus', b'gainMaxSpd', b'gainTime', b'delayTimerDuration', b'heatingTime', b'coolingTime', b'dmgBonus', b'aimBonus')
    MECHANICS_NAME = b'overheatStacks'

    def __init__(self, heatingTime, coolingTime, dmgBonus, aimBonus, gainMaxSpd, delayTimerDuration):
        super(OverheatStacksParams, self).__init__()
        self.levelMax = 255
        self.gainTime = 1.0
        self.gainMaxSpd = gainMaxSpd
        self.delayTimerDuration = delayTimerDuration
        self.heatingTime = heatingTime
        self.coolingTime = coolingTime
        self.dmgBonus = dmgBonus
        self.aimBonus = aimBonus
        self.configure()
        self._saveOrigin()
        return

    def configure(self):
        self.levelInc = self.levelMax * self.gainTime / self.heatingTime
        self.levelDec = self.levelMax * self.gainTime / self.coolingTime
        self.dmgLevelBonus = (self.dmgBonus - 1) / self.levelMax
        self.aimLevelBonus = (self.aimBonus - 1) / self.levelMax
        self.aimLevelBonus = self.__clampAimLevelBonus(self.aimLevelBonus)
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'overheatStacks/dmgBonusFactor': 1.0, 
           b'overheatStacks/aimBonusFactor': 1.0, 
           b'overheatStacks/gainMaxSpd': 0.0, 
           b'overheatStacks/totalTime': 0.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, _):
        heatingTime = _xml.readNonNegativeInt(ctx, section, b'heatingTime', 0)
        coolingTime = _xml.readNonNegativeInt(ctx, section, b'coolingTime', 0)
        dmgBonus = _xml.readNonNegativeFloat(ctx, section, b'dmgBonus', 0.0)
        aimBonus = _xml.readNonNegativeFloat(ctx, section, b'aimBonus', 0.0)
        gainMaxSpd = _xml.readNonNegativeFloat(ctx, section, b'gainMaxSpd', 0.0)
        delayTimerDuration = _xml.readNonNegativeFloat(ctx, section, b'delayTimerDuration', 0.0)
        return cls(heatingTime, coolingTime, dmgBonus, aimBonus, gainMaxSpd, delayTimerDuration)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'overheatStacks/dmgBonusFactor':
            self.dmgBonus = max(0.0, self.dmgBonus + value - 1.0)
        elif attr == b'overheatStacks/aimBonusFactor':
            self.aimBonus = max(0.0, self.aimBonus + value - 1.0)
        elif attr == b'overheatStacks/gainMaxSpd':
            self.gainMaxSpd = max(0.0, self.gainMaxSpd + value)
        elif attr == b'overheatStacks/totalTime':
            self.heatingTime = max(1.0, self.heatingTime + value)
        return

    def applyMiscAttrToMechanics(self, miscAttrs):
        super(OverheatStacksParams, self).applyMiscAttrToMechanics(miscAttrs)
        self.configure()
        return

    @staticmethod
    def __clampAimLevelBonus(aimLevelBonus):
        res = min(0.99, max(0.0, aimLevelBonus))
        if res != aimLevelBonus:
            LOG_WARNING(b'[OverheatStacksParams] aimLevelBonus out of bounds (clamped, unclamped)', res, aimLevelBonus)
        return res


class TargetDesignatorParams(MechanicsParams):
    __slots__ = MechanicsParams.__slots__ + (b'damageIncomeFactor', b'cooldownTime', b'deployTime', b'spottedMarkedTime', b'unspottedMarkedTime')
    MECHANICS_NAME = b'targetDesignator'

    def __init__(self, damageIncomeFactor, cooldownTime, deployTime, spottedMarkedTime, unspottedMarkedTime):
        super(TargetDesignatorParams, self).__init__()
        self.damageIncomeFactor = damageIncomeFactor
        self.cooldownTime = cooldownTime
        self.deployTime = deployTime
        self.spottedMarkedTime = spottedMarkedTime
        self.unspottedMarkedTime = unspottedMarkedTime
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, _):
        readFloat = partial(_xml.readNonNegativeFloat, ctx, section)
        return cls(readFloat(b'damageIncomeFactor', 1.0), readFloat(b'cooldownTime', 1.0), readFloat(b'deployTime', 0.0), readFloat(b'spottedMarkedTime', 1.0), readFloat(b'unspottedMarkedTime', 1.0))

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'targetDesignator/spottedMarkedTime': 0.0, 
           b'targetDesignator/cooldownTime': 0.0, 
           b'targetDesignator/deployTime': 0.0, 
           b'targetDesignator/damageIncome': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'targetDesignator/spottedMarkedTime':
            self.spottedMarkedTime = max(0, self.spottedMarkedTime + value)
        elif attr == b'targetDesignator/cooldownTime':
            self.cooldownTime = max(0, self.cooldownTime + value)
        elif attr == b'targetDesignator/deployTime':
            self.deployTime = max(0.0, self.deployTime + value)
        elif attr == b'targetDesignator/damageIncome':
            self.damageIncomeFactor = max(1.0, self.damageIncomeFactor + value)
        return


class AutoreloaderSurgeParams(MechanicsParams):
    __slots__ = (b'maxCharges', b'startCharges', b'chargeTimeSRegular', b'chargeTimeSFullClip', b'reloadTime')
    MECHANICS_NAME = b'autoreloaderSurge'

    def __init__(self, maxCharges, startCharges, chargeTimeSRegular, chargeTimeSFullClip, reloadTime):
        super(AutoreloaderSurgeParams, self).__init__()
        self.maxCharges = maxCharges
        self.startCharges = startCharges
        self.chargeTimeSRegular = chargeTimeSRegular
        self.chargeTimeSFullClip = chargeTimeSFullClip
        self.reloadTime = reloadTime
        self._saveOrigin()
        return

    _MIN_CHARGES = 2
    _MAX_CHARGES = 4

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        maxCharges = _xml.readNonNegativeInt(ctx, section, b'maxCharges')
        if not cls._MIN_CHARGES <= maxCharges <= cls._MAX_CHARGES:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] maxCharges must be in range [{}, {}], got {}').format(cls.MECHANICS_NAME, cls._MIN_CHARGES, cls._MAX_CHARGES, maxCharges))
        startCharges = _xml.readNonNegativeInt(ctx, section, b'startCharges')
        chargeTimeSRegular = _xml.readNonNegativeFloat(ctx, section, b'chargeTimeSRegular')
        chargeTimeSFullClip = _xml.readNonNegativeFloat(ctx, section, b'chargeTimeSFullClip')
        reloadTime = _xml.readNonNegativeFloat(ctx, section, b'reloadTime')
        return cls(maxCharges=maxCharges, startCharges=startCharges, chargeTimeSRegular=chargeTimeSRegular, chargeTimeSFullClip=chargeTimeSFullClip, reloadTime=reloadTime)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'autoreloaderSurge/maxCharges': 0, 
           b'autoreloaderSurge/startCharges': 0, 
           b'autoreloaderSurge/chargeTimeSRegular': 0.0, 
           b'autoreloaderSurge/chargeTimeSFullClip': 0.0, 
           b'autoreloaderSurge/reloadTime': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'autoreloaderSurge/maxCharges':
            self.maxCharges += value
        elif attr == b'autoreloaderSurge/startCharges':
            self.startCharges += value
        elif attr == b'autoreloaderSurge/chargeTimeSRegular':
            self.chargeTimeSRegular += value
        elif attr == b'autoreloaderSurge/chargeTimeSFullClip':
            self.chargeTimeSFullClip += value
        elif attr == b'autoreloaderSurge/reloadTime':
            self.reloadTime += value
        return


class StanceDanceParams(MechanicsParams):
    __slots__ = (b'timeSwitchStance', b'maxEnergy', b'gainFightEnergyPoints', b'gainTurboEnergyPoints', b'gainEnergyTime', b'gainTurboEnergyBonusPoints', b'gainTurboEnergySpdLimitKmh', b'passiveFightEnergyBonusPerHit', b'passiveTurboFwdSpdBonusKmh', b'passiveTurboBkwdSpdBonusKmh', b'passiveTurboEnginePowerBonus', b'passiveTurboAccuracyDebuff', b'passiveTurboAimSpeedDebuff', b'passiveTurboStabilizeDebuff', b'passiveTurboAfterShotDispersionDebuff', b'activeFightCost', b'activeFightDuration', b'activeFightAccuracyBonus', b'activeFightAimSpeedBonus', b'activeFightStabilizeBonus', b'activeFightAfterShotDispersionBonus', b'activeFightReloadSpdBonus', b'activeTurboCost', b'activeTurboDuration', b'activeTurboFwdSpdBonusKmh', b'activeTurboBkwdSpdBonusKmh', b'activeTurboEnginePowerBonus', b'activeTurboRotationSpeedDebuff', b'activeTurboRammingDmgBonus', b'impulse')
    MECHANICS_NAME = b'stanceDance'

    def __init__(self, timeSwitchStance, maxEnergy, gainFightEnergyPoints, gainTurboEnergyPoints, gainEnergyTime, gainTurboEnergyBonusPoints, gainTurboEnergySpdLimitKmh, passiveFightEnergyBonusPerHit, passiveTurboFwdSpdBonusKmh, passiveTurboBkwdSpdBonusKmh, passiveTurboEnginePowerBonus, passiveTurboAccuracyDebuff, passiveTurboAimSpeedDebuff, passiveTurboStabilizeDebuff, passiveTurboAfterShotDispersionDebuff, activeFightCost, activeFightDuration, activeFightAccuracyBonus, activeFightAimSpeedBonus, activeFightStabilizeBonus, activeFightAfterShotDispersionBonus, activeFightReloadSpdBonus, activeTurboCost, activeTurboDuration, activeTurboFwdSpdBonusKmh, activeTurboBkwdSpdBonusKmh, activeTurboEnginePowerBonus, activeTurboRotationSpeedDebuff, activeTurboRammingDmgBonus, impulse):
        super(StanceDanceParams, self).__init__()
        self.timeSwitchStance = timeSwitchStance
        self.maxEnergy = maxEnergy
        self.gainFightEnergyPoints = gainFightEnergyPoints
        self.gainTurboEnergyPoints = gainTurboEnergyPoints
        self.gainEnergyTime = gainEnergyTime
        self.gainTurboEnergyBonusPoints = gainTurboEnergyBonusPoints
        self.gainTurboEnergySpdLimitKmh = gainTurboEnergySpdLimitKmh
        self.passiveFightEnergyBonusPerHit = passiveFightEnergyBonusPerHit
        self.passiveTurboFwdSpdBonusKmh = passiveTurboFwdSpdBonusKmh
        self.passiveTurboBkwdSpdBonusKmh = passiveTurboBkwdSpdBonusKmh
        self.passiveTurboEnginePowerBonus = passiveTurboEnginePowerBonus
        self.passiveTurboAccuracyDebuff = passiveTurboAccuracyDebuff
        self.passiveTurboAimSpeedDebuff = passiveTurboAimSpeedDebuff
        self.passiveTurboStabilizeDebuff = passiveTurboStabilizeDebuff
        self.passiveTurboAfterShotDispersionDebuff = passiveTurboAfterShotDispersionDebuff
        self.activeFightCost = activeFightCost
        self.activeFightDuration = activeFightDuration
        self.activeFightAccuracyBonus = activeFightAccuracyBonus
        self.activeFightAimSpeedBonus = activeFightAimSpeedBonus
        self.activeFightStabilizeBonus = activeFightStabilizeBonus
        self.activeFightAfterShotDispersionBonus = activeFightAfterShotDispersionBonus
        self.activeFightReloadSpdBonus = activeFightReloadSpdBonus
        self.activeTurboCost = activeTurboCost
        self.activeTurboDuration = activeTurboDuration
        self.activeTurboFwdSpdBonusKmh = activeTurboFwdSpdBonusKmh
        self.activeTurboBkwdSpdBonusKmh = activeTurboBkwdSpdBonusKmh
        self.activeTurboEnginePowerBonus = activeTurboEnginePowerBonus
        self.activeTurboRotationSpeedDebuff = activeTurboRotationSpeedDebuff
        self.activeTurboRammingDmgBonus = activeTurboRammingDmgBonus
        self.impulse = impulse
        self.modifiers = {}
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        timeSwitchStance = _xml.readNonNegativeFloat(ctx, section, b'timeSwitchStance')
        maxEnergy = _xml.readNonNegativeFloat(ctx, section, b'maxEnergy')
        gainFightEnergyPoints = _xml.readNonNegativeFloat(ctx, section, b'gainFightEnergyPoints')
        gainTurboEnergyPoints = _xml.readNonNegativeFloat(ctx, section, b'gainTurboEnergyPoints')
        gainEnergyTime = _xml.readNonNegativeFloat(ctx, section, b'gainEnergyTime')
        gainTurboEnergyBonusPoints = _xml.readNonNegativeFloat(ctx, section, b'gainTurboEnergyBonusPoints')
        gainTurboEnergySpdLimitKmh = _xml.readNonNegativeFloat(ctx, section, b'gainTurboEnergySpdLimitKmh')
        passiveFightEnergyBonusPerHit = _xml.readNonNegativeFloat(ctx, section, b'passiveFightEnergyBonusPerHit')
        passiveTurboFwdSpdBonusKmh = _xml.readNonNegativeFloat(ctx, section, b'passiveTurboFwdSpdBonusKmh')
        passiveTurboBkwdSpdBonusKmh = _xml.readNonNegativeFloat(ctx, section, b'passiveTurboBkwdSpdBonusKmh')
        passiveTurboEnginePowerBonus = _xml.readNonNegativeFloat(ctx, section, b'passiveTurboEnginePowerBonus')
        passiveTurboAccuracyDebuff = _xml.readNonNegativeFloat(ctx, section, b'passiveTurboAccuracyDebuff')
        passiveTurboAimSpeedDebuff = _xml.readNonNegativeFloat(ctx, section, b'passiveTurboAimSpeedDebuff')
        passiveTurboStabilizeDebuff = _xml.readNonNegativeFloat(ctx, section, b'passiveTurboStabilizeDebuff')
        passiveTurboAfterShotDispersionDebuff = _xml.readNonNegativeFloat(ctx, section, b'passiveTurboAfterShotDispersionDebuff')
        activeFightCost = _xml.readNonNegativeFloat(ctx, section, b'activeFightCost')
        activeFightDuration = _xml.readNonNegativeFloat(ctx, section, b'activeFightDuration')
        activeFightAccuracyBonus = _xml.readNonNegativeFloat(ctx, section, b'activeFightAccuracyBonus')
        activeFightAimSpeedBonus = _xml.readNonNegativeFloat(ctx, section, b'activeFightAimSpeedBonus')
        activeFightStabilizeBonus = _xml.readNonNegativeFloat(ctx, section, b'activeFightStabilizeBonus')
        activeFightAfterShotDispersionBonus = _xml.readNonNegativeFloat(ctx, section, b'activeFightAfterShotDispersionBonus')
        activeFightReloadSpdBonus = _xml.readNonNegativeFloat(ctx, section, b'activeFightReloadSpdBonus')
        activeTurboCost = _xml.readNonNegativeFloat(ctx, section, b'activeTurboCost')
        activeTurboDuration = _xml.readNonNegativeFloat(ctx, section, b'activeTurboDuration')
        activeTurboFwdSpdBonusKmh = _xml.readNonNegativeFloat(ctx, section, b'activeTurboFwdSpdBonusKmh')
        activeTurboBkwdSpdBonusKmh = _xml.readNonNegativeFloat(ctx, section, b'activeTurboBkwdSpdBonusKmh')
        activeTurboEnginePowerBonus = _xml.readNonNegativeFloat(ctx, section, b'activeTurboEnginePowerBonus')
        activeTurboRotationSpeedDebuff = _xml.readNonNegativeFloat(ctx, section, b'activeTurboRotationSpeedDebuff')
        activeTurboRammingDmgBonus = _xml.readNonNegativeFloat(ctx, section, b'activeTurboRammingDmgBonus')
        impulse = readImpulseData(ctx, section)
        return cls(timeSwitchStance=timeSwitchStance, maxEnergy=maxEnergy, gainFightEnergyPoints=gainFightEnergyPoints, gainTurboEnergyPoints=gainTurboEnergyPoints, gainEnergyTime=gainEnergyTime, gainTurboEnergyBonusPoints=gainTurboEnergyBonusPoints, gainTurboEnergySpdLimitKmh=gainTurboEnergySpdLimitKmh, passiveFightEnergyBonusPerHit=passiveFightEnergyBonusPerHit, passiveTurboFwdSpdBonusKmh=passiveTurboFwdSpdBonusKmh, passiveTurboBkwdSpdBonusKmh=passiveTurboBkwdSpdBonusKmh, passiveTurboEnginePowerBonus=passiveTurboEnginePowerBonus, passiveTurboAccuracyDebuff=passiveTurboAccuracyDebuff, passiveTurboAimSpeedDebuff=passiveTurboAimSpeedDebuff, passiveTurboStabilizeDebuff=passiveTurboStabilizeDebuff, passiveTurboAfterShotDispersionDebuff=passiveTurboAfterShotDispersionDebuff, activeFightCost=activeFightCost, activeFightDuration=activeFightDuration, activeFightAccuracyBonus=activeFightAccuracyBonus, activeFightAimSpeedBonus=activeFightAimSpeedBonus, activeFightStabilizeBonus=activeFightStabilizeBonus, activeFightAfterShotDispersionBonus=activeFightAfterShotDispersionBonus, activeFightReloadSpdBonus=activeFightReloadSpdBonus, activeTurboCost=activeTurboCost, activeTurboDuration=activeTurboDuration, activeTurboFwdSpdBonusKmh=activeTurboFwdSpdBonusKmh, activeTurboBkwdSpdBonusKmh=activeTurboBkwdSpdBonusKmh, activeTurboEnginePowerBonus=activeTurboEnginePowerBonus, activeTurboRotationSpeedDebuff=activeTurboRotationSpeedDebuff, activeTurboRammingDmgBonus=activeTurboRammingDmgBonus, impulse=impulse)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'stanceDance/gainFightEnergyPoints': 0.0, 
           b'stanceDance/gainFightEnergyPointsFactor': 1.0, 
           b'stanceDance/gainTurboEnergyPoints': 0.0, 
           b'stanceDance/gainTurboEnergyPointsFactor': 1.0, 
           b'stanceDance/activeFightDuration': 0.0, 
           b'stanceDance/activeTurboDuration': 0.0, 
           b'stanceDance/timeSwitchStance': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'stanceDance/gainFightEnergyPoints':
            self.gainFightEnergyPoints += value
        elif attr == b'stanceDance/gainFightEnergyPointsFactor':
            self.gainFightEnergyPoints *= value
        elif attr == b'stanceDance/gainTurboEnergyPoints':
            self.gainTurboEnergyPoints += value
        elif attr == b'stanceDance/gainTurboEnergyPointsFactor':
            self.gainTurboEnergyPoints *= value
        elif attr == b'stanceDance/activeFightDuration':
            self.activeFightDuration += value
        elif attr == b'stanceDance/activeTurboDuration':
            self.activeTurboDuration += value
        elif attr == b'stanceDance/timeSwitchStance':
            self.timeSwitchStance += value
        return


class DebuffsParams(MechanicsParams):
    __slots__ = MechanicsParams.__slots__ + (b'debuffs',)
    MECHANICS_NAME = b'reactiveDebuffs'

    def __init__(self, debuffs):
        super(DebuffsParams, self).__init__()
        self.debuffs = debuffs
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        debuffs = {}
        for debuff in section.keys():
            debuffIdx = DEBUFFS_TYPES.getIdx(debuff)
            debuffs[debuffIdx] = readModifiers(ctx, section[debuff])

        return cls(debuffs)


TemperatureGunThermalState = namedtuple(b'TemperatureGunThermalState', [b'temperature', b'modifiers'])

class TemperatureGunThermalStates(object):
    __slots__ = (b'states', b'thermalStateHysteresis')
    _MAX_THERMAL_STATES = 10

    def __init__(self, states, thermalStateHysteresis):
        self.states = states
        self.thermalStateHysteresis = thermalStateHysteresis
        return

    def __eq__(self, other):
        if isinstance(other, TemperatureGunThermalStates):
            return self.states == other.states and self.thermalStateHysteresis == other.thermalStateHysteresis
        return False

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return hash((self.states, self.thermalStateHysteresis))

    @classmethod
    def readThermalStates(cls, ctx, section, readModifiers, mechanicName):
        thermalStateHysteresis = _xml.readPositiveFloat(ctx, section, b'thermalStateHysteresis')
        states = []
        if not section.has_key(b'thermalStates'):
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section <thermalStates> is missing!').format(mechanicName))
        for tag, subsection in section[b'thermalStates'].items():
            if tag == b'state':
                maxTemperature = _xml.readPositiveFloat(ctx, subsection, b'maxTemperature')
                modifiers = readModifiers(ctx, _xml.getSubsection(ctx, subsection, b'modifiers'))
                state = TemperatureGunThermalState(temperature=maxTemperature, modifiers=modifiers)
                states.append(state)

        if not states:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section thermalStates should not be empty!').format(mechanicName))
        if len(states) > cls._MAX_THERMAL_STATES:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section thermalStates should not have number of states > {}!').format(mechanicName, cls._MAX_THERMAL_STATES))
        states.sort(key=(lambda thermalState: thermalState.temperature))
        temperatureRanges = [0] + [state.temperature for state in states]
        minTempDiff = min(temperatureRanges[i + 1] - temperatureRanges[i] for i in xrange(len(temperatureRanges) - 1))
        if minTempDiff < thermalStateHysteresis:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] <thermalStateHysteresis> must be within all temperature states!').format(mechanicName))
        return cls(states=states, thermalStateHysteresis=thermalStateHysteresis)


class TemperatureGunParams(GunMechanicsParams):
    __slots__ = (b'thermalStates', b'heatingPerShot', b'coolingDelay', b'coolingPerSec')
    MECHANICS_NAME = b'temperatureGun'

    def __init__(self, thermalStates, heatingPerShot, coolingDelay, coolingPerSec):
        super(TemperatureGunParams, self).__init__()
        self.thermalStates = thermalStates
        self.heatingPerShot = heatingPerShot
        self.coolingDelay = coolingDelay
        self.coolingPerSec = coolingPerSec
        self._saveOrigin()
        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'temperatureGun/heatingPerShot': 0.0, 
           b'temperatureGun/coolingDelay': 0.0, 
           b'temperatureGun/coolingPerSec': 1.0}

    @property
    def maxTemperature(self):
        return self.thermalStates.states[-1].temperature

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        heatingPerShot = _xml.readPositiveFloat(ctx, section, b'heatingPerShot')
        coolingDelay = _xml.readPositiveFloat(ctx, section, b'coolingDelay')
        coolingPerSec = _xml.readPositiveFloat(ctx, section, b'coolingPerSec')
        thermalStates = TemperatureGunThermalStates.readThermalStates(ctx, section, readModifiers, cls.MECHANICS_NAME)
        return cls(thermalStates=thermalStates, heatingPerShot=heatingPerShot, coolingDelay=coolingDelay, coolingPerSec=coolingPerSec)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'temperatureGun/heatingPerShot':
            self.heatingPerShot += value
        elif attr == b'temperatureGun/coolingDelay':
            self.coolingDelay += value
        elif attr == b'temperatureGun/coolingPerSec':
            self.coolingPerSec *= value
        return


class OverheatGunParams(GunMechanicsParams):
    __slots__ = (b'coolingPerSecFactor', b'tempOverheatOnThreshold', b'tempOverheatOffThreshold', b'tempOverheatWarnThreshold')
    MECHANICS_NAME = b'overheatGun'

    def __init__(self, coolingPerSecFactor, tempOverheatOnThreshold, tempOverheatOffThreshold, tempOverheatWarnThreshold):
        super(OverheatGunParams, self).__init__()
        self.coolingPerSecFactor = coolingPerSecFactor
        self.tempOverheatOnThreshold = tempOverheatOnThreshold
        self.tempOverheatOffThreshold = tempOverheatOffThreshold
        self.tempOverheatWarnThreshold = tempOverheatWarnThreshold
        self._saveOrigin()
        return

    def isActiveMechanics(self, vehicleDescriptor):
        mechanicsParams = vehicleDescriptor.mechanicsParams
        return TemperatureGunParams.MECHANICS_NAME in mechanicsParams and mechanicsParams[TemperatureGunParams.MECHANICS_NAME].isActiveMechanics(vehicleDescriptor)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'overheatGun/coolingPerSecFactor': 1.0, 
           b'overheatGun/tempOverheatOnThreshold': 1.0, 
           b'overheatGun/tempOverheatOffThreshold': 1.0, 
           b'overheatGun/tempOverheatWarnThreshold': 1.0}

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        coolingPerSecFactor = _xml.readPositiveFloat(ctx, section, b'coolingPerSecFactor')
        tempOverheatOnThreshold = _xml.readPositiveFloat(ctx, section, b'tempOverheatOnThreshold')
        tempOverheatOffThreshold = _xml.readNonNegativeFloat(ctx, section, b'tempOverheatOffThreshold')
        tempOverheatWarnThreshold = _xml.readPositiveFloat(ctx, section, b'tempOverheatWarnThreshold', defaultValue=tempOverheatOnThreshold)
        if tempOverheatOffThreshold > tempOverheatOnThreshold:
            _xml.raiseWrongXml(ctx, b'', (b'[OverheatGunParams] tempOverheatOffThreshold={} should not be > tempOverheatOnThreshold={}!').format(tempOverheatOffThreshold, tempOverheatOnThreshold))
        return cls(coolingPerSecFactor=coolingPerSecFactor, tempOverheatOnThreshold=tempOverheatOnThreshold, tempOverheatOffThreshold=tempOverheatOffThreshold, tempOverheatWarnThreshold=tempOverheatWarnThreshold)

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'overheatGun/coolingPerSecFactor':
            self.coolingPerSecFactor *= value
        elif attr == b'overheatGun/tempOverheatOnThreshold':
            self.tempOverheatOnThreshold *= value
        elif attr == b'overheatGun/tempOverheatOffThreshold':
            self.tempOverheatOffThreshold *= value
        elif attr == b'overheatGun/tempOverheatWarnThreshold':
            self.tempOverheatWarnThreshold *= value
        return


class HeatingZonesGunParams(GunMechanicsParams):
    __slots__ = (b'zones',)
    MECHANICS_NAME = b'heatingZonesGun'
    ZONE_STATE = HEATING_ZONES_GUN_STATE

    def __init__(self, zones):
        super(HeatingZonesGunParams, self).__init__()
        self.zones = zones
        self._saveOrigin()
        return

    def isActiveMechanics(self, vehicleDescriptor):
        mechanicsParams = vehicleDescriptor.mechanicsParams
        return TemperatureGunParams.MECHANICS_NAME in mechanicsParams and mechanicsParams[TemperatureGunParams.MECHANICS_NAME].isActiveMechanics(vehicleDescriptor)

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        zonesValues = lmap(float, _xml.readNonEmptyString(ctx, section, b'zones').split())
        if any(zoneValue < 0.0 for zoneValue in zonesValues):
            _xml.raiseWrongXml(ctx, b'', (b"[{}] Invalid zones values: all zones values should be non negative '{}'").format(cls.__name__, zonesValues))
        zonesCount = len(zonesValues)
        statesCount = len(cls.ZONE_STATE.ALL)
        if zonesCount != statesCount:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Invalid zones count: expected: {}, got: {}').format(cls.__name__, statesCount, zonesCount))
        if any(zonesValues[idx] > zonesValues[idx + 1] for idx in xrange(zonesCount - 1)):
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Invalid zones: zone value should be not less than previous one').format(cls.__name__, zonesValues))
        return cls(lzip(cls.ZONE_STATE.ALL, zonesValues))


class StagedJetBoostersParams(MechanicsParams):
    __slots__ = (b'deployTime', b'reloadTime', b'reuseCount', b'duration', b'impulse', b'impulseSpeedLimits', b'modifiers', b'customRotationPoints')
    MECHANICS_NAME = b'stagedJetBoosters'

    def __init__(self, deployTime, reloadTime, reuseCount, duration, impulse, impulseSpeedLimits, modifiers, customRotationPoints):
        super(StagedJetBoostersParams, self).__init__(modifiers)
        self.deployTime = deployTime
        self.reloadTime = reloadTime
        self.reuseCount = reuseCount
        self.duration = duration
        self.impulse = impulse
        self.impulseSpeedLimits = impulseSpeedLimits
        self.modifiers = modifiers
        self.customRotationPoints = customRotationPoints
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        impulse = None
        if section.has_key(b'impulse'):
            impulse = readImpulseData(ctx, section)
        speedLimits = None
        if section.has_key(b'impulseSpeedLimits'):
            speedLimits = _xml.readVector2(ctx, section, b'impulseSpeedLimits')
            speedLimits *= KMH_TO_MS
        return cls(deployTime=_xml.readNonNegativeFloat(ctx, section, b'deployTime'), reloadTime=_xml.readNonNegativeFloat(ctx, section, b'reloadTime'), reuseCount=_xml.readInt(ctx, section, b'reuseCount', minVal=-1), duration=_xml.readNonNegativeFloat(ctx, section, b'duration'), impulse=impulse, impulseSpeedLimits=speedLimits, modifiers=modifiers, customRotationPoints=cls._readCustomRotationPoints(ctx, section))

    @classmethod
    def _readCustomRotationPoints(cls, ctx, section):
        if not section.has_key(b'customRotationPoints'):
            return None
        else:

            def readPoints(ctx, section, subsectionName):
                subCtx, subSection = _xml.getSubSectionWithContext(ctx, section, subsectionName)
                return {b'speed': (_xml.readFloat(subCtx, subSection, b'speed') * KMH_TO_MS), 
                   b'leftPoint': (_xml.readVector3(subCtx, subSection, b'leftPoint')), 
                   b'rightPoint': (_xml.readVector3(subCtx, subSection, b'rightPoint'))}

            pointsCtx, pointsSection = _xml.getSubSectionWithContext(ctx, section, b'customRotationPoints')
            return {b'min': (readPoints(pointsCtx, pointsSection, b'minSpeedPoints')), 
               b'max': (readPoints(pointsCtx, pointsSection, b'maxSpeedPoints')), 
               b'changeRailDirection': (_xml.readBool(pointsCtx, pointsSection, b'changeRailDirection'))}

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'stagedJetBoosters/deployTime': 0.0, 
           b'stagedJetBoosters/reloadTime': 0.0, 
           b'stagedJetBoosters/reuseCount': 0.0, 
           b'stagedJetBoosters/duration': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'stagedJetBoosters/deployTime':
            self.deployTime += value
        elif attr == b'stagedJetBoosters/reloadTime':
            self.reloadTime += value
        elif attr == b'stagedJetBoosters/reuseCount':
            self.reuseCount += value
        elif attr == b'stagedJetBoosters/duration':
            self.duration += value
        return


PropellantGunStage = namedtuple(b'PropellantGunStage', [
 b'maxCharge', b'modifiers', b'isOvercharge', b'damageFactorLimits'])

class PropellantGunDamageFactors(object):
    __slots__ = (b'minFactor', b'maxFactor')

    def __init__(self, minFactor, maxFactor):
        self.minFactor = minFactor
        self.maxFactor = maxFactor
        return

    def __eq__(self, other):
        return isclose(self.minFactor, other.minFactor) and isclose(self.maxFactor, other.maxFactor)

    def __ne__(self, other):
        return not self == other

    __hash__ = None


class PropellantGunParams(GunMechanicsParams):
    __slots__ = (b'chargeStages', b'chargingPerSec', b'chargeSpendingAfterShot', b'forbiddenShells', b'shouldPauseOnReload', b'chargeDelay', b'dischargingPerSec', b'overchargeSwitchCooldown')
    MECHANICS_NAME = b'propellantAfterburnerGun'
    _MAX_STAGES = 10

    def __init__(self, chargeStages, chargingPerSec, chargeSpendingAfterShot, forbiddenShells, shouldPauseOnReload, chargeDelay, dischargingPerSec, overchargeSwitchCooldown):
        super(PropellantGunParams, self).__init__()
        self.chargeStages = chargeStages
        self.chargingPerSec = chargingPerSec
        self.chargeSpendingAfterShot = chargeSpendingAfterShot
        self.forbiddenShells = forbiddenShells
        self.shouldPauseOnReload = shouldPauseOnReload
        self.chargeDelay = chargeDelay
        self.dischargingPerSec = dischargingPerSec
        self.overchargeSwitchCooldown = overchargeSwitchCooldown
        self._saveOrigin()
        return

    @property
    def maxCharge(self):
        maxCharge = 0.0
        for chargeState in self.chargeStages:
            if chargeState.isOvercharge:
                break
            maxCharge = chargeState.maxCharge

        return maxCharge

    @property
    def maxOvercharge(self):
        if self.chargeStages[-1].isOvercharge:
            return self.chargeStages[-1].maxCharge
        else:
            return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'propellantGun/chargingPerSec': 1.0, 
           b'propellantGun/dischargingPerSec': 1.0, 
           b'propellantGun/chargeSpendingAfterShot': 1.0, 
           b'propellantGun/damageMinFactor': 0.0, 
           b'propellantGun/damageMaxFactor': 0.0, 
           b'propellantGun/overchargeDamageMinFactor': 0.0, 
           b'propellantGun/overchargeDamageMaxFactor': 0.0, 
           b'propellantGun/chargeDelay': 0.0}

    def applyDynModifiersToMechanics(self, dynModifiers):
        if not dynModifiers:
            return
        regularFilter = self.MECHANICS_NAME + b'Regular'
        overchargeFilter = self.MECHANICS_NAME + b'Overcharge'
        regularModifiers = []
        overchargeModifiers = []
        for modifier in dynModifiers:
            modifierFilter = modifier[4]
            if modifierFilter == regularFilter:
                regularModifiers.append(modifier)
            elif modifierFilter == overchargeFilter:
                overchargeModifiers.append(modifier)

        for chargeState in self.chargeStages:
            chargeState.modifiers.extend(overchargeModifiers if chargeState.isOvercharge else regularModifiers)

        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        chargingPerSec = _xml.readPositiveFloat(ctx, section, b'chargingPerSec')
        dischargingPerSec = _xml.readPositiveFloat(ctx, section, b'dischargingPerSec')
        chargeSpendingAfterShot = _xml.readPositiveFloat(ctx, section, b'chargeSpendingAfterShot')
        shouldPauseOnReload = _xml.readBool(ctx, section, b'shouldPauseOnReload', True)
        chargeDelay = _xml.readNonNegativeFloat(ctx, section, b'chargeDelay')
        overchargeSwitchCooldown = _xml.readNonNegativeFloat(ctx, section, b'overchargeSwitchCooldown')
        forbiddenShells = readShellCDsByName(ctx, section, b'forbiddenShells')
        chargeStages = cls._readChargeStages(ctx, section, readModifiers)
        return cls(chargeStages=chargeStages, chargingPerSec=chargingPerSec, chargeSpendingAfterShot=chargeSpendingAfterShot, forbiddenShells=forbiddenShells, shouldPauseOnReload=shouldPauseOnReload, chargeDelay=chargeDelay, dischargingPerSec=dischargingPerSec, overchargeSwitchCooldown=overchargeSwitchCooldown)

    @classmethod
    def _readChargeStages(cls, ctx, section, readModifiers):
        if not section.has_key(b'chargeStages'):
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section <chargeStages> is missing!').format(cls.MECHANICS_NAME))
        stages = []
        overchargeStagesCount = 0
        maxCharges = set()
        for tag, subsection in section[b'chargeStages'].items():
            if tag != b'stage':
                _xml.raiseWrongXml(ctx, b'', (b'[{}] Unexpected section <{}>!').format(tag, cls.MECHANICS_NAME))
            maxCharge = _xml.readPositiveFloat(ctx, subsection, b'maxCharge')
            if maxCharge in maxCharges:
                _xml.raiseWrongXml(ctx, b'', (b'[{}] Max charge is duplicated: {}!').format(cls.MECHANICS_NAME, maxCharge))
            modifiers = readModifiers(ctx, _xml.getSubsection(ctx, subsection, b'modifiers'))
            isOvercharge = _xml.readBool(ctx, subsection, b'isOvercharge', False)
            damageFactorLimits = _xml.readTupleOfPositiveFloats(ctx, subsection, b'damageFactorLimits')
            if len(damageFactorLimits) != 2:
                _xml.raiseWrongXml(ctx, b'', (b"[{}] Expected 2 values for 'damageFactorLimits' field: {}!").format(cls.MECHANICS_NAME, damageFactorLimits))
            stages.append(PropellantGunStage(maxCharge=maxCharge, modifiers=modifiers, isOvercharge=isOvercharge, damageFactorLimits=PropellantGunDamageFactors(*damageFactorLimits)))
            maxCharges.add(maxCharge)
            if isOvercharge:
                overchargeStagesCount += 1

        if not stages:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section chargeStages should not be empty!').format(cls.MECHANICS_NAME))
        if len(stages) > cls._MAX_STAGES:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section chargeStages should not have number of stages > {}!').format(cls.MECHANICS_NAME, cls._MAX_STAGES))
        stages.sort(key=(lambda chargeStage: chargeStage.maxCharge))
        if any(state.isOvercharge for state in stages[:len(stages) - overchargeStagesCount]):
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Overcharge stages should be continuous: {}').format(cls.MECHANICS_NAME, stages))
        return stages

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'propellantGun/chargingPerSec':
            self.chargingPerSec *= value
        elif attr == b'propellantGun/dischargingPerSec':
            self.dischargingPerSec *= value
        elif attr == b'propellantGun/chargeSpendingAfterShot':
            self.chargeSpendingAfterShot *= value
        elif attr == b'propellantGun/damageMinFactor':
            self.__applyDamageFactor(b'minFactor', value, False)
        elif attr == b'propellantGun/damageMaxFactor':
            self.__applyDamageFactor(b'maxFactor', value, False)
        elif attr == b'propellantGun/overchargeDamageMinFactor':
            self.__applyDamageFactor(b'minFactor', value, True)
        elif attr == b'propellantGun/overchargeDamageMaxFactor':
            self.__applyDamageFactor(b'maxFactor', value, True)
        elif attr == b'propellantGun/chargeDelay':
            self.chargeDelay += value
        return

    def __applyDamageFactor(self, factorType, value, isOvercharge):
        for chargeState in self.chargeStages:
            if chargeState.isOvercharge == isOvercharge:
                setattr(chargeState.damageFactorLimits, factorType, max(getattr(chargeState.damageFactorLimits, factorType) + value, 0.0))

        return


class WheeledDashParams(MechanicsParams):
    __slots__ = (b'deployTime', b'reloadTime', b'duration', b'speedTrigger', b'speedReloadTimeFactor', b'tickedImpulse')
    MECHANICS_NAME = b'wheeledDash'

    def __init__(self, deployTime, reloadTime, duration, modifiers, speedTrigger, speedReloadTimeFactor, tickedImpulse):
        super(WheeledDashParams, self).__init__(modifiers)
        self.deployTime = deployTime
        self.reloadTime = reloadTime
        self.duration = duration
        self.speedTrigger = speedTrigger
        self.speedReloadTimeFactor = speedReloadTimeFactor
        self.tickedImpulse = tickedImpulse
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        speedTrigger, speedReloadTimeFactor = cls.readReloadTimeBoostData(ctx, section)
        return cls(deployTime=_xml.readPositiveFloat(ctx, section, b'deployTime'), reloadTime=_xml.readPositiveFloat(ctx, section, b'reloadTime'), duration=_xml.readPositiveFloat(ctx, section, b'duration'), modifiers=modifiers, speedTrigger=speedTrigger, speedReloadTimeFactor=speedReloadTimeFactor, tickedImpulse=readTickedImpulseData(ctx, section))

    @classmethod
    def readReloadTimeBoostData(cls, ctx, section, subsection=b'reloadTimeBoost'):
        reloadTimeBoostCtx, reloadTimeBoostSection = _xml.getSubSectionWithContext(ctx, section, subsection)
        speedTrigger = SpeedTriggerData(enableSpeed=_xml.readNonNegativeFloat(reloadTimeBoostCtx, reloadTimeBoostSection, b'minSpeed'), hysteresisSpeed=_xml.readNonNegativeFloat(reloadTimeBoostCtx, reloadTimeBoostSection, b'hysteresisSpeed'))
        speedReloadTimeFactor = _xml.readNonNegativeFloat(reloadTimeBoostCtx, reloadTimeBoostSection, b'reloadTimeFactor')
        return (speedTrigger, speedReloadTimeFactor)

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'wheeledDash/deployTime': 0.0, 
           b'wheeledDash/reloadTime': 0.0, 
           b'wheeledDash/duration': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'wheeledDash/deployTime':
            self.deployTime += value
        elif attr == b'wheeledDash/reloadTime':
            self.reloadTime += value
        elif attr == b'wheeledDash/duration':
            self.duration += value
        return


class AuxiliaryRocketLauncherParams(GunMechanicsParams):
    MECHANICS_NAME = b'auxiliaryRocketLauncher'

    def __init__(self):
        super(AuxiliaryRocketLauncherParams, self).__init__()
        self._saveOrigin()
        return

    def isActiveMechanics(self, vehicleDescriptor):
        mechanicsParams = vehicleDescriptor.mechanicsParams
        return SecondaryGunParams.MECHANICS_NAME in mechanicsParams and mechanicsParams[SecondaryGunParams.MECHANICS_NAME].isActiveMechanics(vehicleDescriptor)

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        return cls()


class ShellSwitcherParams(GunMechanicsParams):
    __slots__ = (b'modifiedShells',)
    MECHANICS_NAME = b'shellParamsSwitcher'

    def __init__(self, modifiedShells):
        super(ShellSwitcherParams, self).__init__()
        self.modifiedShells = modifiedShells
        self._saveOrigin()
        return

    def isActiveMechanics(self, vehicleDescriptor):
        return vehicleDescriptor.hasSiegeMode

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        modifiedShells = readShellCDsByName(ctx, section, b'modifiedShells')
        if not modifiedShells:
            raise SoftException((b'[{}] Empty modifiedShells!').format(cls.MECHANICS_NAME))
        return cls(modifiedShells=tuple(modifiedShells))


class ShellCalibrationBonus(object):
    __slots__ = (b'dmgBonus', b'modifiers')

    def __init__(self, damageCoefficient, modifiers):
        self.dmgBonus = damageCoefficient
        self.modifiers = modifiers
        return

    def __eq__(self, other):
        if isinstance(other, ShellCalibrationBonus):
            return self.modifiers == other.modifiers and isclose(self.dmgBonus, other.dmgBonus)
        return False

    def __ne__(self, other):
        return not self == other

    __hash__ = None


class ShellCalibrationParams(GunMechanicsParams):
    __slots__ = (b'penBonuses', b'nonPenBonuses', b'forbiddenShells')
    MECHANICS_NAME = b'shellCalibration'

    def __init__(self, penBonuses, nonPenBonuses, forbiddenShells):
        super(ShellCalibrationParams, self).__init__()
        self.penBonuses = penBonuses
        self.nonPenBonuses = nonPenBonuses
        self.forbiddenShells = forbiddenShells
        self._saveOrigin()
        return

    def isActiveMechanics(self, vehicleDescriptor):
        return b'clip' in vehicleDescriptor.gun.tags and vehicleDescriptor.gun.clip[0] > 1

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        params = {}
        for condition in (b'penetration', b'nonPenetration'):
            condCtx, condSection = _xml.getSubSectionWithContext(ctx, section, condition)
            dmgFactor = _xml.readNonNegativeFloat(condCtx, condSection, b'damageCoefficient', 0.0)
            condMods = None
            if condSection[b'modifiers'] is not None:
                condMods = readModifiers(condCtx, _xml.getSubsection(condCtx, condSection, b'modifiers'))
            params[condition] = ShellCalibrationBonus(dmgFactor, condMods)

        forbiddenShells = readShellCDsByName(ctx, section, b'forbiddenShells')
        return cls(penBonuses=params[b'penetration'], nonPenBonuses=params[b'nonPenetration'], forbiddenShells=forbiddenShells)

    def applyDynModifiersToMechanics(self, dynModifiers):
        if not dynModifiers:
            return
        penFilter = self.MECHANICS_NAME + b'Penetration'
        nonPenFilter = self.MECHANICS_NAME + b'NonPenetration'
        penModifiers = self.penBonuses.modifiers
        nonPenModifiers = self.nonPenBonuses.modifiers
        for modifier in dynModifiers:
            modifierFilter = modifier[4]
            if modifierFilter == penFilter:
                penModifiers.append(modifier)
            elif modifierFilter == nonPenFilter:
                nonPenModifiers.append(modifier)

        return

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'shellCalibration/penetrationDamageCoefficient': 0.0, 
           b'shellCalibration/nonPenetrationDamageCoefficient': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'shellCalibration/penetrationDamageCoefficient':
            self.penBonuses.dmgBonus += value
        elif attr == b'shellCalibration/nonPenetrationDamageCoefficient':
            self.nonPenBonuses.dmgBonus += value
        return


class CrestMovingParams(MechanicsParams):
    MECHANICS_NAME = b'crestMoving'


class BustleFeedParams(MechanicsParams):
    __slots__ = (b'activationTime', b'deactivationTime', b'modifiers', b'bustleShotReloadFactor', b'bustleShotDamageBonusShell0', b'bustleShotDamageBonusShell1', b'bustleShotsIndices', b'animationTime')
    MECHANICS_NAME = b'bustleFeed'

    def __init__(self, activationTime, deactivationTime, modifiers, bustleShotReloadFactor, bustleShotDamageBonusShell0, bustleShotDamageBonusShell1):
        super(BustleFeedParams, self).__init__(modifiers)
        self.activationTime = activationTime
        self.deactivationTime = deactivationTime
        self.animationTime = 2.5
        self.bustleShotReloadFactor = bustleShotReloadFactor
        self.bustleShotDamageBonusShell0 = bustleShotDamageBonusShell0
        self.bustleShotDamageBonusShell1 = bustleShotDamageBonusShell1
        self.bustleShotsIndices = {0, 1}
        self._saveOrigin()
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        modifiers = readModifiers(ctx, _xml.getSubsection(ctx, section, b'modifiers'))
        return cls(activationTime=_xml.readNonNegativeFloat(ctx, section, b'activationTime'), deactivationTime=_xml.readNonNegativeFloat(ctx, section, b'deactivationTime'), modifiers=modifiers, bustleShotReloadFactor=_xml.readPositiveFloat(ctx, section, b'bustleShotReloadFactor'), bustleShotDamageBonusShell0=_xml.readPositiveFloat(ctx, section, b'bustleShotDamageBonusShell0'), bustleShotDamageBonusShell1=_xml.readPositiveFloat(ctx, section, b'bustleShotDamageBonusShell1'))

    def getBustleShotDamageBonusShell(self, idx):
        if idx == 0:
            return self.bustleShotDamageBonusShell0
        if idx == 1:
            return self.bustleShotDamageBonusShell1
        return 0

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'bustleFeed/bustleShotDamageBonusShell0': 0.0, 
           b'bustleFeed/bustleShotDamageBonusShell1': 0.0, 
           b'bustleFeed/bustleShotReloadFactor': 1.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'bustleFeed/bustleShotDamageBonusShell0':
            self.bustleShotDamageBonusShell0 += value
        if attr == b'bustleFeed/bustleShotDamageBonusShell1':
            self.bustleShotDamageBonusShell1 += value
        if attr == b'bustleFeed/bustleShotReloadFactor':
            self.bustleShotReloadFactor *= value
        return


SightPointerAbilityStage = typing.NamedTuple(b'SightPointerAbilityStage', (
 (
  b'id', int),
 (
  b'duration', float),
 (
  b'angle', float),
 (
  b'visionModifiers', typing.List[typing.Tuple[str, str, str, float, str]]),
 (
  b'vehicleModifiers', typing.List[typing.Tuple[str, str, str, float, str]])))

class SightPointerParams(MechanicsParams):
    __slots__ = (b'initialDeployTime', b'reloadTime', b'activeStages', b'selfReveal', b'selfRevealVisionTime', b'sightPointerStages')
    MECHANICS_NAME = b'sightPointer'
    _MAX_STAGES = 10
    _MIN_DURATION = 1

    def __init__(self, initialDeployTime, reloadTime, activeStages, selfReveal, selfRevealVisionTime, sightPointerStages):
        super(SightPointerParams, self).__init__()
        self.initialDeployTime = initialDeployTime
        self.reloadTime = reloadTime
        self.activeStages = activeStages
        self.selfReveal = selfReveal
        self.selfRevealVisionTime = selfRevealVisionTime
        self.sightPointerStages = sightPointerStages
        self._saveOrigin()
        return

    @property
    def duration(self):
        duration = 0.0
        for stage in self.sightPointerStages:
            if stage.id < self.activeStages:
                duration += stage.duration

        return duration

    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        return {b'sightPointer/initialDeployTime': 0.0, 
           b'sightPointer/reloadTime': 0.0, 
           b'sightPointer/activeStages': 0.0, 
           b'sightPointer/selfRevealVisionTime': 0.0}

    def _applyMechanicsAttrs(self, attr, value):
        if attr == b'sightPointer/initialDeployTime':
            self.initialDeployTime += value
        elif attr == b'sightPointer/reloadTime':
            self.reloadTime += value
        elif attr == b'sightPointer/activeStages':
            self.activeStages += int(value)
        elif attr == b'sightPointer/selfRevealVisionTime':
            self.selfRevealVisionTime += value
        return

    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        initialDeployTime = _xml.readNonNegativeFloat(ctx, section, b'initialDeployTime')
        reloadTime = _xml.readPositiveFloat(ctx, section, b'reloadTime')
        activeStages = _xml.readPositiveInt(ctx, section, b'activeStages')
        selfReveal = _xml.readBool(ctx, section, b'selfReveal')
        selfRevealVisionTime = _xml.readNonNegativeFloat(ctx, section, b'selfRevealVisionTime')
        sightPointerStages = cls._readStages(ctx, section, readModifiers)
        if initialDeployTime < SIGHT_POINTER_COMMON_CONSTANTS.ANIMATION_DELAY:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] <initialDeployTime> should be more or equal than animation time').format(cls.MECHANICS_NAME))
        initialDeployTime -= SIGHT_POINTER_COMMON_CONSTANTS.ANIMATION_DELAY
        if reloadTime < SIGHT_POINTER_COMMON_CONSTANTS.ANIMATION_DELAY:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] <reloadTime> should be more or equal than animation time').format(cls.MECHANICS_NAME))
        reloadTime -= SIGHT_POINTER_COMMON_CONSTANTS.ANIMATION_DELAY
        if activeStages > len(sightPointerStages):
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section <sightPointerStages> stages is less than current activeStages!').format(cls.MECHANICS_NAME))
        return cls(initialDeployTime=initialDeployTime, reloadTime=reloadTime, activeStages=activeStages, selfReveal=selfReveal, selfRevealVisionTime=selfRevealVisionTime, sightPointerStages=sightPointerStages)

    @classmethod
    def _readStages(cls, ctx, section, readModifiers):
        if not section.has_key(b'sightPointerStages'):
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section <sightPointerStages> is missing!').format(cls.MECHANICS_NAME))
        stages = []
        stagesIDs = set()
        for tag, subsection in viewitems(section[b'sightPointerStages']):
            if tag != b'stage':
                _xml.raiseWrongXml(ctx, b'', (b'[{}] Unexpected section <{}>!').format(cls.MECHANICS_NAME, tag))
            stageIdx = _xml.readInt(ctx, subsection, b'id')
            if stageIdx in stagesIDs:
                _xml.raiseWrongXml(ctx, b'', (b'[{}] duplicated id:{} in <sightPointerStages>,!').format(cls.MECHANICS_NAME, stageIdx))
            stagesIDs.add(stageIdx)
            duration = _xml.readNonNegativeFloat(ctx, subsection, b'duration')
            if duration < cls._MIN_DURATION:
                _xml.raiseWrongXml(ctx, b'', (b'[{}] section <duration> should be >= {}!').format(cls.MECHANICS_NAME, cls._MIN_DURATION))
            angle = _xml.readNonNegativeFloat(ctx, subsection, b'angle')
            visionModifiers = readModifiers(ctx, _xml.getSubsection(ctx, subsection, b'vision_modifiers'))
            vehicleModifiers = readModifiers(ctx, _xml.getSubsection(ctx, subsection, b'vehicle_modifiers'))
            stages.append(SightPointerAbilityStage(id=stageIdx, duration=duration, angle=angle, visionModifiers=visionModifiers, vehicleModifiers=vehicleModifiers))

        if not stages:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section sightPointerStages should not be empty!').format(cls.MECHANICS_NAME))
        if len(stages) > cls._MAX_STAGES:
            _xml.raiseWrongXml(ctx, b'', (b'[{}] Section sightPointerStages should not have number of stages > {}!').format(cls.MECHANICS_NAME, cls._MAX_STAGES))
        stages.sort(key=(lambda stage: stage.id))
        return stages


def addMechanicsParamsAttrs(attrsSet):
    for paramsCls in MechanicsParams.getSubClasses():
        attrsSet.update(paramsCls.getDefaultMechanicsMiscAttributes())

    return


addMechanicsParamsAttrs(ALLOWED_STATIC_ATTRS)
MECHANIC_NAME_TO_IDX = {mechanicParams.MECHANICS_NAME: index for index, mechanicParams in enumerate(MechanicsParams.getSubClasses())}
ObjectSlot = reflectedNamedTuple(b'ObjectSlot', (b'name', b'type', b'position', b'rotation'))
