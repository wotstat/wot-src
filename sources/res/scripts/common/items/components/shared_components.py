import math
from collections import namedtuple
from constants import IS_CLIENT, IS_WEB, IS_EDITOR, IS_BOT
from items.components import component_constants, c11n_constants
from items.components import path_builder
from items.components.c11n_constants import ApplyArea
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


__all__ = (b'MaterialInfo', b'DEFAULT_MATERIAL_INFO', b'EmblemSlot', b'LodSettings', b'NodesAndGroups', b'Camouflage', b'DEFAULT_CAMOUFLAGE', b'SwingingSettings', b'I18nComponent', b'DeviceHealth', b'ModelStatesPaths', b'RocketAccelerationParams')
MaterialInfo = reflectedNamedTuple(b'MaterialInfo', (b'kind', b'armor', b'extra', b'multipleExtra', b'vehicleDamageFactor', b'useArmorHomogenization', b'useHitAngle', b'useAntifragmentationLining', b'mayRicochet', b'collideOnceOnly', b'checkCaliberForRichet', b'checkCaliberForHitAngleNorm', b'damageKind', b'chanceToHitByProjectile', b'chanceToHitByExplosion', b'continueTraceIfNoHit'))
DEFAULT_MATERIAL_INFO = MaterialInfo(0, 0, None, False, 0.0, False, False, False, False, False, False, False, 0, 0.0, 0.0, False)
EmblemSlot = reflectedNamedTuple(b'EmblemSlot', (b'rayStart', b'rayEnd', b'rayUp', b'size', b'hideIfDamaged', b'type', b'isMirrored', b'isUVProportional', b'emblemId', b'slotId', b'applyToFabric', b'compatibleModels', b'planeProjection'))

class CustomizationSlotDescription(object):
    __metaclass__ = ReflectionMetaclass
    __slots__ = (b'type', b'slotId', b'anchorPosition', b'anchorDirection', b'applyTo')

    def __init__(self, slotType=b'', slotId=0, anchorPosition=None, anchorDirection=None, applyTo=None, tags=None):
        self.type = slotType
        self.slotId = slotId
        self.anchorPosition = anchorPosition
        self.anchorDirection = anchorDirection
        self.applyTo = applyTo
        return


class ProjectionDecalSlotDescription(object):
    __metaclass__ = ReflectionMetaclass
    __slots__ = (b'type', b'slotId', b'position', b'rotation', b'scale', b'scaleFactors', b'doubleSided', b'hiddenForUser', b'canBeMirroredVertically', b'showOn', b'tags', b'clipAngle', b'compatibleModels', b'itemId', b'options', b'anchorShift', b'modificationOrder')

    def __init__(self, slotType=b'', slotId=0, position=None, rotation=None, scale=None, scaleFactors=c11n_constants.DEFAULT_DECAL_SCALE_FACTORS, doubleSided=False, hiddenForUser=False, canBeMirroredVertically=False, showOn=None, tags=None, clipAngle=c11n_constants.DEFAULT_DECAL_CLIP_ANGLE, compatibleModels=(
 c11n_constants.SLOT_DEFAULT_ALLOWED_MODEL,), itemId=None, options=c11n_constants.Options.NONE, anchorShift=c11n_constants.DEFAULT_DECAL_ANCHOR_SHIFT, modificationOrder=0):
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
    __slots__ = (b'__userKey', b'__descriptionKey', b'__longDescriptionSpecialKey')

    def __init__(self, userStringKey, descriptionKey, longDescriptionSpecialKey=b''):
        super(I18nExposedComponent, self).__init__(userStringKey, descriptionKey, longDescriptionSpecialKey=longDescriptionSpecialKey)
        self.__userKey = userStringKey
        self.__descriptionKey = descriptionKey
        self.__longDescriptionSpecialKey = longDescriptionSpecialKey
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

class ModelStatesPaths(object):
    __slots__ = (b'__undamaged', b'__destroyed', b'__exploded')
    __metaclass__ = ReflectionMetaclass

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


class RocketAccelerationParams(object):
    ImpulseData = namedtuple(b'ImpulseData', (b'magnitude', b'applyPoint', b'duration'))
    __slots__ = (b'deployTime', b'reloadTime', b'reuseCount', b'duration', b'impulse', b'modifiers', b'kpi', b'effectsPrefab')

    def __init__(self, deployTime, reloadTime, reuseCount, duration, impulse, modifiers, kpi, effectsPrefab):
        self.deployTime = deployTime
        self.reloadTime = reloadTime
        self.reuseCount = reuseCount
        self.duration = duration
        self.impulse = impulse
        self.modifiers = modifiers
        self.kpi = kpi
        self.effectsPrefab = effectsPrefab
        return

    def __repr__(self):
        return (b'deployTime={}, reloadTime={}, reuseCount={}, duration={}, impulse={}, modifiers={}').format(self.deployTime, self.reloadTime, self.reuseCount, self.duration, self.impulse, self.modifiers)


class ThermalVisionParams(object):
    __slots__ = (b'initialReloadTime', b'reloadTime', b'duration', b'hSectorAngle', b'vSectorAngle', b'distance', b'timeToObserve', b'timeInObservation', b'useCount')

    def __init__(self, initialReloadTime, reloadTime, duration, hSectorAngle, vSectorAngle, distance, timeToObserve, timeInObservation, useCount):
        self.initialReloadTime = initialReloadTime
        self.reloadTime = reloadTime
        self.duration = duration
        self.hSectorAngle = math.radians(hSectorAngle)
        self.vSectorAngle = math.radians(vSectorAngle)
        self.distance = distance
        self.timeToObserve = timeToObserve
        self.timeInObservation = timeInObservation
        self.useCount = useCount
        return

    def __repr__(self):
        reprItems = []
        for item in self.__slots__:
            reprItems.append((b'{}={}').format(item, getattr(self, item, None)))

        return (b', ').join(reprItems)

    @staticmethod
    def makeCopy(other):
        return ThermalVisionParams(initialReloadTime=other.initialReloadTime, reloadTime=other.reloadTime, duration=other.duration, hSectorAngle=math.degrees(other.hSectorAngle), vSectorAngle=math.degrees(other.vSectorAngle), distance=other.distance, timeToObserve=other.timeToObserve, timeInObservation=other.timeInObservation, useCount=other.useCount)
