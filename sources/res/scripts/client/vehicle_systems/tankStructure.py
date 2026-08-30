from collections import namedtuple
from constants import VehiclePartName

class CgfTankNodes(object):
    TANK_ROOT = b'Tank.Root'


class ModelStates(object):
    UNDAMAGED = b'undamaged'
    DESTROYED = b'destroyed'
    EXPLODED = b'exploded'


ModelsSetParams = namedtuple(b'ModelsSetParams', (b'skin', b'state', b'attachments'))

class TankRenderMode(object):
    NORMAL = 0
    CRASH = 1
    SERVER_COLLISION = 2
    CLIENT_COLLISION = 3
    CRASH_COLLISION = 4
    OVERLAY_COLLISION = 5
    ARMOR_WIDTH_COLLISION = 6
    DISABLE = 7


class TankCollisionPartNames(object):
    CHASSIS = b'chassisCollision'
    HULL = b'hullCollision'
    TURRET = b'turretCollision'
    GUN = b'gunCollision'
    WHEEL = b'wheelCollision'
    ALL = (
     CHASSIS, HULL, TURRET, GUN)

    @staticmethod
    def getIdx(name):
        for idx, n in enumerate(TankCollisionPartNames.ALL):
            if n == name:
                return idx

        return


class TankPartNames(object):
    CHASSIS = VehiclePartName.CHASSIS
    HULL = VehiclePartName.HULL
    TURRET = VehiclePartName.TURRET
    GUN = VehiclePartName.GUN
    ALL = (
     CHASSIS, HULL, TURRET, GUN)

    @staticmethod
    def getIdx(name):
        for idx, n in enumerate(TankPartNames.ALL):
            if n == name:
                return idx

        return

    @staticmethod
    def getActualNodeNameByPartName(partName, isAlive=True):
        if isAlive and partName == TankPartNames.GUN:
            return TankNodeNames.GUN_INCLINATION
        return partName


class DetachedTurretPartNames(object):
    ALL = (
     TankPartNames.TURRET, TankPartNames.GUN)

    @staticmethod
    def getIdx(name):
        for idx, n in enumerate(DetachedTurretPartNames.ALL):
            if n == name:
                return idx

        return


class DetachedTurretPartIndexes(object):
    TURRET = 0
    GUN = 1
    ALL = (
     TURRET, GUN)

    @staticmethod
    def getName(idx):
        return DetachedTurretPartNames.ALL[idx]


VehiclePartsTuple = namedtuple(b'VehiclePartsTuple', TankPartNames.ALL)

class TankPartIndexes(object):
    CHASSIS = 0
    HULL = 1
    TURRET = 2
    GUN = 3
    ALL = (
     CHASSIS, HULL, TURRET, GUN)

    @staticmethod
    def getName(idx):
        if 0 <= idx < len(TankPartNames.ALL):
            return TankPartNames.ALL[idx]
        else:
            return


class TankNodeNames(object):
    TRACK_LEFT_FRONT = b'HP_Track_LFront'
    TRACK_LEFT_REAR = b'HP_Track_LRear'
    TRACK_RIGHT_FRONT = b'HP_Track_RFront'
    TRACK_RIGHT_REAR = b'HP_Track_RRear'
    TRACK_LEFT_UP_FRONT = b'HP_TrackUp_LFront'
    TRACK_LEFT_UP_REAR = b'HP_TrackUp_LRear'
    TRACK_RIGHT_UP_FRONT = b'HP_TrackUp_RFront'
    TRACK_RIGHT_UP_REAR = b'HP_TrackUp_RRear'
    GUI = b'HP_gui'
    HULL_SWINGING = b'V'
    TURRET_JOINT = b'HP_turretJoint'
    HULL_FIRE_1 = b'HP_Fire_1'
    GUN_JOINT = b'HP_gunJoint'
    GUN_INCLINATION = b'Gun'
    GUN_RECOIL = b'G'
    GUN_RECOIL_L = b'G_L'
    GUN_RECOIL_R = b'G_R'
    GUN_FIRE = b'HP_gunFire'
    TRACK_LEFT_MID = b'DM_Track_LMid'
    TRACK_RIGHT_MID = b'DM_Track_RMid'
    CHASSIS_MID_TRAIL = b'DM_Mid_Trail'


class TankSoundObjectsIndexes(object):
    CHASSIS = 0
    ENGINE = 1
    GUN = 2
    HIT = 3
    COUNT = 4


UNDAMAGED_SKELETON = VehiclePartsTuple(chassis=[
 (b'Tank', b''),
 (
  TankNodeNames.HULL_SWINGING, b'Tank'),
 (
  TankNodeNames.GUI, b''),
 (
  TankNodeNames.TRACK_LEFT_FRONT, b''),
 (
  TankNodeNames.TRACK_LEFT_REAR, b''),
 (
  TankNodeNames.TRACK_RIGHT_FRONT, b''),
 (
  TankNodeNames.TRACK_RIGHT_REAR, b'')], hull=[
 (b'HP_Fire_1', b''),
 (
  TankNodeNames.TRACK_LEFT_UP_FRONT, b''),
 (
  TankNodeNames.TRACK_LEFT_UP_REAR, b''),
 (
  TankNodeNames.TRACK_RIGHT_UP_FRONT, b''),
 (
  TankNodeNames.TRACK_RIGHT_UP_REAR, b'')], turret=[
 (b'HP_gunJoint', b'')], gun=[
 (
  TankNodeNames.GUN_INCLINATION, b''),
 (
  TankNodeNames.GUN_RECOIL, TankNodeNames.GUN_INCLINATION),
 (
  b'HP_gunFire', TankNodeNames.GUN_RECOIL)])
CRASHED_SKELETON = VehiclePartsTuple(chassis=[
 (b'Tank', b''),
 (b'V', b'Tank'),
 (b'HP_gui', b'')], hull=[
 (b'HP_Fire_1', b'')], turret=[
 (b'HP_gunJoint', b'')], gun=[])

class ColliderTypes(object):
    DYNAMIC_FLAG = 1
    TANK_FLAG = 2
    HANGAR_FLAG = 4
    PLAYER_FLAG = 8
    DYNAMIC_COLLIDER = DYNAMIC_FLAG
    VEHICLE_COLLIDER = DYNAMIC_FLAG | TANK_FLAG
    PLATOON_VEHICLE_COLLIDER = TANK_FLAG | HANGAR_FLAG
    PLAYER_VEHICLE_COLLIDER = DYNAMIC_FLAG | TANK_FLAG | PLAYER_FLAG
    HANGAR_VEHICLE_COLLIDER = DYNAMIC_FLAG | TANK_FLAG | HANGAR_FLAG
    HANGAR_PLAYER_VEHICLE_COLLIDER = DYNAMIC_FLAG | TANK_FLAG | HANGAR_FLAG | PLAYER_FLAG


def getCrashedSkeleton(vehicleDesc):
    turretJointNode = (
     vehicleDesc.hull.turretHardPoints[0], b'')
    result = VehiclePartsTuple(chassis=CRASHED_SKELETON.chassis, hull=CRASHED_SKELETON.hull + [turretJointNode], turret=CRASHED_SKELETON.turret, gun=CRASHED_SKELETON.gun)
    return result


def getPartModelsFromDesc(vehicleDesc, modelsSetParams):
    skinName = modelsSetParams.skin
    paths = []
    for partName in TankPartNames.ALL:
        part = getattr(vehicleDesc, partName)
        if skinName in part.modelsSets:
            skin = part.modelsSets[skinName]
        else:
            skin = part.models
        path = skin.getPathByStateName(modelsSetParams.state)
        paths.append(path)

    return VehiclePartsTuple(*paths)


def getCollisionModelsFromDesc(vehicleDesc, state):
    paths = []
    for partName in TankPartNames.ALL:
        part = getattr(vehicleDesc, partName)
        if state == TankRenderMode.CLIENT_COLLISION:
            paths.append(part.hitTesterManager.edClientBspModel)
        elif state in (TankRenderMode.SERVER_COLLISION, TankRenderMode.ARMOR_WIDTH_COLLISION):
            paths.append(part.hitTesterManager.edServerBspModel)
        elif state == TankRenderMode.CRASH_COLLISION:
            if part.hitTesterManager.edCrashBspModel != b'':
                paths.append(part.hitTesterManager.edCrashBspModel)
            else:
                paths.append(part.hitTesterManager.edClientBspModel)

    return VehiclePartsTuple(*paths)
