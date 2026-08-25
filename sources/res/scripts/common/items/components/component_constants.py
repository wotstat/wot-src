from __future__ import absolute_import
import collections, enum
from soft_exception import SoftException
from wrapped_reflection_framework import reflectedNamedTuple
from Math import Vector3
Autoreload = collections.namedtuple(b'Autoreload', [
 b'reloadTime', b'boostStartTime', b'boostResidueTime', b'boostFraction'])
AutoShoot = collections.namedtuple(b'AutoShoot', [
 b'maxShotDispersion', b'groupSize', b'shotDispersionPerShot', b'aimingDelay'])
DualGun = reflectedNamedTuple(b'DualGun', [
 17, 18, 19, 20, 21, 22, 
 23, 24, 25])
DualAccuracy = collections.namedtuple(b'DualAccuracy', [
 b'afterShotDispersionAngle', b'coolingDelay'])
TwinGun = collections.namedtuple(b'TwinGun', [
 b'afterShotDelay', b'gunMarkerOffset', b'shootImpulse', b'twinGunReloadTime'])
MultiGunState = collections.namedtuple(b'MultiGunState', [
 b'gunIndexes', b'multiGun'])
ControllableReload = collections.namedtuple(b'ControllableReload', [
 b'allowToReloadAfterShot'])
UNDEFINED_ITEM_TYPE_ID = 0
ZERO_FLOAT = 0.0
ZERO_INT = 0
ZERO_TUPLE2 = (0.0, 0.0)
ZERO_VECTOR3 = Vector3(0.0, 0.0, 0.0)
ONE_INT = 1
EMPTY_STRING = b''
EMPTY_TUPLE = ()
EMPTY_LIST = []
INFLUENCE_ALL = 0
INFLUENCE_ALLY = 1
INFLUENCE_ENEMY = 2

class _ReadOnlyDict(dict):

    def __setitem__(self, key, value):
        raise SoftException(b'ReadOnlyDict set item attempt %s=>%s' % (key, value))
        return

    def update(self, E=None, **F):
        raise SoftException(b'ReadOnlyDict update attempt %s, %s' % (E, F))
        return


EMPTY_DICT = _ReadOnlyDict()
EMPTY_TAGS = frozenset()
LEVEL = 1
DEFAULT_ARMOR_HOMOGENIZATION = 1.0
DEFAULT_GUN_AUTORELOAD = Autoreload(reloadTime=(0.0,), boostStartTime=0.0, boostResidueTime=0.0, boostFraction=1.0)
DEFAULT_GUN_BURST = (
 1, 0.0, False)
DEFAULT_GUN_CLIP = (1, 0.0)
DEFAULT_GUN_DUALGUN = DualGun(chargeTime=4.0, shootImpulse=100.0, reloadLockTime=10.0, reloadTimes=(10, 8), rateTime=5, chargeThreshold=0.5, afterShotDelay=0.5, preChargeIndication=0.25, chargeCancelTime=0.18)
DEFAULT_GUN_DUAL_ACCURACY = DualAccuracy(afterShotDispersionAngle=1.0, coolingDelay=5.0)
DEFAULT_GUN_AUTOSHOOT = AutoShoot(maxShotDispersion=0.0, shotDispersionPerShot=0.0, aimingDelay=0.0, groupSize=1)
DEFAULT_GUN_TWINGUN = TwinGun(afterShotDelay=0.5, gunMarkerOffset=0.0, shootImpulse=0, twinGunReloadTime=0.0)
DEFAULT_FAKE_TURRETS = {b'lobby': (), b'battle': ()}
DEFAULT_HULL_VARIANT_MATCH = (None, None)
DEFAULT_PREMIUM_VEHICLE_XP_FACTOR = 0.0
DEFAULT_SPECIFIC_FRICTION = 0.6867000000000001
DEFAULT_INVISIBILITY_FACTOR = 1.0
DEFAULT_DAMAGE_RANDOMIZATION = 0.25
DEFAULT_PIERCING_POWER_RANDOMIZATION = 0.25
DEFAULT_MODERN_HE_OBSTACLE_PENETRATION = True
DEFAULT_MODERN_HE_SHIELD_PENETRATION = True
DEFAULT_PIERCING_SPALLS = True
MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_DESTRUCTIBLES = 1.0
MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS = 3.0
MODERN_HE_DAMAGE_ABSORPTION_FACTOR = 0.0
DEFAULT_ENABLE_TRACE_RICOCHET = True
KMH_TO_MS = 0.27778
MS_TO_KMH = 3.5999712
KG_TO_NEWTON = 9.81
HP_TO_WATTS = 735.5
ALLOWED_EMBLEM_SLOTS = (b'player', b'clan', b'inscription', b'insignia', b'insigniaOnGun', b'fixedEmblem', b'fixedInscription')
ALLOWED_PROJECTION_DECALS_ANCHORS = (b'projectionDecal', b'fixedProjectionDecal')
ALLOWED_MISC_SLOTS = (b'sequence',)
ALLOWED_SLOTS_ANCHORS = (b'paint', b'camouflage', b'effect', b'style')
ALLOWED_ATTACHMENT_SLOTS = (b'attachment', b'statTracker')
TANKMEN_GROUPS = (b'normalGroups', b'premiumGroups')
MAIN_TRACK_PAIR_IDX = 0
DEFAULT_TRACK_HIT_VECTOR = Vector3(0.0, 10.0, 0.0)
TrackState = collections.namedtuple(b'TrackState', [b'isBroken', b'hitPoint', b'isDebris'])
DynamicShotEffect = collections.namedtuple(b'DynamicShotEffect', [b'effectsIndex', b'minShotsCount', b'maxShotsCount'])
DYNAMIC_SHOT_MAX_COUNT = 10000
ShootImpulse = collections.namedtuple(b'ShootImpulse', [
 b'magnitude', b'applicationPoint', b'isStillSafe'])

class ObjectSlotType(object):
    ATTACHMENT = b'attachment'
    ALL = (
     ATTACHMENT,)


class MuzzleBrakeType(enum.IntEnum):
    NONE = 0
    STANDARD = 1


INVALID_EFFECT_INDEX = 255
