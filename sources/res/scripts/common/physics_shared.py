import BigWorld, Math, math, collections
from items import vehicles
from items.components.component_constants import KMH_TO_MS
from items.vehicles import VEHICLE_PHYSICS_TYPE, VehicleDescriptor, VehicleDescrType
from constants import IS_CLIENT, IS_EDITOR, SERVER_TICK_LENGTH
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_DEBUG, LOG_ERROR
import copy
from gun_rotation_shared import encodeRestrictedValueToUint, decodeRestrictedValueFromUint
from typing import Any
G = 9.81
GRAVITY_FACTOR = 1.25
WEIGHT_SCALE = 0.001
GRAVITY_FACTOR_SCALED = GRAVITY_FACTOR * WEIGHT_SCALE
PHYSICAL_INF = 1000000000
SUSP_COMPRESSION_MIN = 0.85
SUSP_COMPRESSION_MIN_MASS = 60.0
SUSP_COMPRESSION_MAX = 0.88
SUSP_COMPRESSION_MAX_MASS = 30.0
BODY_HEIGHT = 1.4
ROLLER_CONTACT_IGNORE_ANGLE = 25
ROLLER_HORIZONTAL_SURFACE_ANGLE = 35
SIDE_MOVEMENT_THRESHOLD = SERVER_TICK_LENGTH * 0.05
_SIMULATION_Y_BOUND = 1000.0
FREEZE_ANG_ACCEL_EPSILON = 0.35
FREEZE_ACCEL_EPSILON = 0.4
FREEZE_VEL_EPSILON = 0.15
FREEZE_ANG_VEL_EPSILON = 0.06
WIDTH_LONG = 6.2
WIDTH_VERY_LONG = 7.0
CLEARANCE_RATIO_LONG = 5.0
NUM_SPRINGS_LONG = 5
NUM_SPRINGS_NORMAL = 5
CMY_MIN = -0.15
CMY_MID = -0.2
CMY_MAX = -0.3
DYN_RATIO_MIN = 9.5
DYN_RATIO_MID = 13.0
DYN_RATIO_MAX = 21.0
CLEARANCE = 1.75
CLEARANCE_MIN = 0.55
CLEARANCE_MAX = 0.6
HARD_RATIO_MIN = 0.5
CLEARANCE_TO_LENGTH_MIN = 0.085
HARD_RATIO_MAX = 0.52
CLEARANCE_TO_LENGTH_MAX = 0.112
TRACK_LENGTH_MIN = 0.6
TRACK_LENGTH_MAX = 0.64
VEHICLE_ON_OBSTACLE_COLLISION_BOX_MIN_HEIGHT = 1.1
_LOG_INIT_PARAMS = False
RESTITUTION = 0.5
FRICTION_RATIO = 1.0
NUM_ITERATIONS = 10
NUM_ITERATIONS_ACCURATE = 40
MID_SOLVING_ITERATIONS = 4
NUM_SUBSTEPS_IN_STANDARD_MODE = 2
USE_SSE_SOLVER_IN_STANDARD_MODE = False
NUM_SUBSTEPS_IN_DETAILED_MODE = 3
USE_SSE_SOLVER_IN_DETAILED_MODE = False
NUM_SUBSTEPS = NUM_SUBSTEPS_IN_STANDARD_MODE
WARMSTARTING_VEHICLE_VEHICLE = False
WARMSTARTING_VEHICLE_STATICS = False
WARMSTARTING_THRESHOLD = 0.1
USE_PSEUDO_CONTACTS = True
ALLOWED_PENETRATION = 0.01
CONTACT_PENETRATION = 0.1
TRACKS_PENETRATION = 0.01
CONTACT_ENERGY_POW = 3.0
CONTACT_ENERGY_POW2 = 0.75
SLOPE_FRICTION_FUNC_DEF = Math.Vector3(tuple(math.pi * ang / 180.0 for ang in (34.0, 50.0, 70.0)))
SLOPE_FRICTION_FUNC_VAL = Math.Vector3(0.4, 2.0, 5.0)
SLOPE_FRICTION_MODELS_FUNC_VAL = Math.Vector3(0.4, 0.45, 0.5)
CONTACT_FRICTION_TERRAIN = 1.0
CONTACT_FRICTION_STATICS = 0.05
CONTACT_FRICTION_EXTRA = 0.3
CONTACT_FRICTION_DESTRUCTIBLES = 1.0
CONTACT_FRICTION_VEHICLES = 0.3
VEHICLE_ON_BODY_DEFAULT_FRICTION = 0.5
ROLLER_REACTION_COEFF_FOR_STATIC = 0.2
ROLLER_FRICTION_GAIN_MIN = 0.05
ROLLER_FRICTION_GAIN_MAX = 0.25
ROLLER_FRICTION_ANGLE_MIN = 20.0
ROLLER_FRICTION_ANGLE_MAX = 45.0
ANCHOR_MAX_REACTION_FACTOR = 0.5
ANCHOR_CONST_FRACTION = 0.0
ANCHOR_VEL_FACTOR = 0.0
ARENA_BOUNDS_FRICTION_HOR = 0.2
ARENA_BOUNDS_FRICTION_VERT = 1.0
_ALLOWER_RPM_EXCESS_UNBOUNDED = 1.4
_ABSOLUTE_SPEED_LIMIT = 25
g_confUpdaters = []

def _cosDeg(angle):
    return math.cos(math.radians(angle))


def _sinDeg(angle):
    return math.sin(math.radians(angle))


def getDefaultChassisXPhysicsCfg():
    return {b'wheelRadius': 0.4, 
       b'wheelRestitution': 0.9, 
       b'wheelPenetration': 0.02, 
       b'wheelUsePseudoContacts': True, 
       b'wheelFwdInertiaFactor': 3.0, 
       b'sideFrictionConstantRatio': 0.0, 
       b'flatSideFriction': True, 
       b'wheelDetachOnRoll': False, 
       b'trackToBeLockedDelay': 1.0, 
       b'trackGaugeFactor': 0.96, 
       b'slopeResistTerrain': (
                             1.5, _cosDeg(15.0), _sinDeg(29.0)), 
       b'slopeResistStaticObject': (
                                  1.5, _cosDeg(15.0), _sinDeg(29.0)), 
       b'slopeResistDynamicObject': (
                                   1.5, _cosDeg(15.0), _sinDeg(20.0)), 
       b'slopeGripLngTerrain': (
                              _cosDeg(27.5), 1.0, _cosDeg(32.0), 0.1), 
       b'slopeGripSdwTerrain': (
                              _cosDeg(24.5), 1.0, _cosDeg(29.0), 0.1), 
       b'slopeGripLngStaticObject': (
                                   _cosDeg(27.5), 1.0, _cosDeg(32.0), 0.1), 
       b'slopeGripSdwStaticObject': (
                                   _cosDeg(24.5), 1.0, _cosDeg(29.0), 0.1), 
       b'slopeGripLngDynamicObject': (
                                    _cosDeg(20.0), 1.0, _cosDeg(25.0), 0.1), 
       b'slopeGripSdwDynamicObject': (
                                    _cosDeg(20.0), 1.0, _cosDeg(25.0), 0.1), 
       b'stiffnessFactors': (1.0, 1.0, 1.0, 1.0, 1.0), 
       b'angVelocityFactor': 1.0, 
       b'angVelocityFactor0': 1.0, 
       b'gimletGoalWOnSpot': 1.0, 
       b'gimletGoalWOnMove': 1.0, 
       b'isRotationAroundCenter': False, 
       b'centerRotationFwdSpeed': 1.0, 
       b'movementRevertSpeed': 1.0, 
       b'fwLagRatio': 1.0, 
       b'bkLagRatio': 1.0, 
       b'rotFritionFactor': 1.0, 
       b'comFrictionYOffs': 1.0, 
       b'comSideFriction': 1.0, 
       b'pushStop': 1.0, 
       b'gimletPushOnSpotInit': 1.0, 
       b'gimletPushOnSpotFinal': 1.0, 
       b'gimletPushOnMoveInit': 1.0, 
       b'gimletPushOnMoveFinal': 1.0, 
       b'gimletVelScaleMin': 1.0, 
       b'gimletVelScaleMax': 1.0, 
       b'pushRotOnSpotFixedPeriod': 1.0, 
       b'pushRotOnMoveFixedPeriod': 1.0, 
       b'pushRotOnSpotGrowPeriod': 1.0, 
       b'pushRotOnMoveGrowPeriod': 1.0, 
       b'bodyHeight': 2.5, 
       b'hullCOMShiftY': (-0.25), 
       b'hullInertiaFactors': (1.0, 1.0, 1.0), 
       b'clearance': 0.25, 
       b'rotationByLockChoker': 1.0, 
       b'chassisMassFraction': 0.3, 
       b'wheelSinkageResistFactor': 0.2, 
       b'wheelInertiaFactor': 1.5, 
       b'stiffness0': 1.0, 
       b'stiffness1': 1.0, 
       b'damping': 0.2, 
       b'brake': 1000.0, 
       b'rotationBrake': 1000.0, 
       b'roadWheelPositions': (-2.5, -1.25, 0.0, 1.25, 2.5), 
       b'brokenTrackLosses': {b'enginePowerLoss': (0.0,), 
                              b'fwMaxSpeedLoss': (0.0,), 
                              b'bkMaxSpeedLoss': (0.0,), 
                              b'rotationSpeedLoss': (0.0,)}}


def getDeafultVehicleModelXPhysicsCfg():
    return {b'hullSize': (0.0, 0.0, 0.0), 
       b'hullBoxOffsetZ': 0.0, 
       b'turretTopPos': (0.0, 0.0, 0.0), 
       b'turretTopWidth': 0.0}


def getDefaultWheeledVehicleModelXPhysicsCfg():
    return dict(getDeafultVehicleModelXPhysicsCfg(), **{b'wheelSize': (0.0, 0.0, 0.0)})


def getDefaultWheeledChassisXPhysicsCfg():
    return dict(getDefaultChassisXPhysicsCfg(), **{b'axleSteeringLockAngles': (0.0, 0.0, 0.0, 30.0), 
       b'axleSteeringAngles': (0.0, 0.0, 0.0, 15.0), 
       b'axleSteeringSpeed': (0.0, 0.0, 0.0, 90.0), 
       b'brokenWheelPowerLoss': (0.0, 0.0, 0.0, 0.0), 
       b'brokenWheelSpeedLoss': (0.0, 0.0, 0.0, 0.0), 
       b'brokenWheelRotationSpeedLoss': (0.0, 0.0, 0.0, 0.0), 
       b'fwdFrictionOnAxisModifiers': (1.0, 1.0, 1.0, 1.0), 
       b'sideFrictionOnAxisModifiers': (1.0, 1.0, 1.0, 1.0), 
       b'sideFrictionConstantRatioOnAxis': (0.0, 0.0, 0.0, 0.0), 
       b'sinkageResistOnAxis': (0.0, 0.0, 0.0, 0.0), 
       b'axleIsLeading': (
                        True, True, True, True), 
       b'axleCanBeRised': (
                         False, True, True, False), 
       b'wheelRiseHeight': 0.2, 
       b'wheelRiseSpeed': 1.0, 
       b'enableRail': True, 
       b'handbrakeBrakeForce': 10.0, 
       b'brokenWheelRollingFrictionModifier': 1.0, 
       b'noSignalBrakeForce': 10.0, 
       b'afterDeathBrakeForce': 10.0, 
       b'afterDeathMinSpeedForImpulse': 29.0, 
       b'afterDeathImpulse': 1.0, 
       b'jumpingFactor': 30.0, 
       b'jumpingMinForce': 70.0, 
       b'slowTurnChocker': 0.5, 
       b'airPitchReduction': 0.0, 
       b'wheelToHullRollTransmission': 1.0, 
       b'steeringSpeedInTurnMultiplier': 1.0, 
       b'burnout': {b'preparationTime': 3.0, 
                    b'activityTime': 1.0, 
                    b'engineDamageMin': 100.0, 
                    b'engineDamageMax': 200.0, 
                    b'warningMaxHealth': 100.0, 
                    b'warningMaxHealthCritEngine': 50.0, 
                    b'power': 1.0, 
                    b'impulse': 0.0}, 
       b'isWheeledOnSpotRotation': False})


def getDefaultTankVehicleXPhysicsShapeCfg():
    return dict(getDefaultVehicleXPhysicsShapeCfg(), **{b'modelShape': (getDeafultVehicleModelXPhysicsCfg()), 
       b'crashedModelShape': (getDeafultVehicleModelXPhysicsCfg())})


def getDefaultWheeledVehicleXPhysicsShapeCfg():
    return dict(getDefaultVehicleXPhysicsShapeCfg(), **{b'wheelZPenetration': 0.8, 
       b'wheelXOffset': 0.0, 
       b'terrBoardAngle': 20.0, 
       b'terrFrontChamferFraction': 0.75, 
       b'modelShape': (getDefaultWheeledVehicleModelXPhysicsCfg()), 
       b'crashedModelShape': (getDefaultWheeledVehicleModelXPhysicsCfg())})


def getDefaultVehicleXPhysicsShapeCfg():
    return {b'useComplexForm': False, 
       b'isParametricShape': True, 
       b'terrAftChamferFraction': 0.5, 
       b'terrFrontChamferFraction': 0.5, 
       b'terrBoardAngle': 0.0, 
       b'tankAftChamferFraction': 0.25, 
       b'tankFrontChamferFraction': 0.25, 
       b'tankBoardAngle': 0.0, 
       b'auxClearance': 0.8}


def getDefaultVehicleXPhysicsCfg():
    return {b'mode_index': 0, 
       b'gravity': 9.81, 
       b'hullCOMShiftY': 0.0, 
       b'clearance': 0.7, 
       b'overspeedResistBaseFactor': 0.5, 
       b'allowedRPMExcessUnbounded': 1.4, 
       b'absoluteSpeedLimit': 25.0, 
       b'hasCrashedModel': False, 
       b'engine': {b'engineTorque': (
                                   (500.0, 2.0), (1000.0, 3.0), (2000.0, 2.5), (2500.0, 2.0)), 
                   b'smplEngPower': 800.0, 
                   b'smplMinRPM': 150.0, 
                   b'smplEnginePower': 1.0, 
                   b'rotationChoker': 1.0, 
                   b'smplFwMaxSpeed': 15.0, 
                   b'smplBkMaxSpeed': 10.0, 
                   b'powerFactor': 1.0, 
                   b'rotationFactor': 1.0, 
                   b'engineLoses': (0.5, 0.8), 
                   b'engineInertia': 0.02, 
                   b'idleChoker': 0.2, 
                   b'idleRPM': 800.0, 
                   b'startRPM': 1000.0}, 
       b'comFrictionYOffs': 0.7, 
       b'smplFwMaxSpeed': 10.0, 
       b'smplBkMaxSpeed': 5.5, 
       b'pushStop': 0.3, 
       b'rail': {b'railFactorInContact': 0.5}, 
       b'anchor': {b'anchorMaxReactionFactor': ANCHOR_MAX_REACTION_FACTOR, 
                   b'anchorConstFraction': ANCHOR_CONST_FRACTION, 
                   b'anchorVelFactor': ANCHOR_VEL_FACTOR}, 
       b'gimlet': {b'pushInContact': 2.5}, 
       b'gimletVelScaleMin': 1.0, 
       b'gimletVelScaleMax': 5.0, 
       b'pushRotOnSpotFixedPeriod': 0.2, 
       b'pushRotOnMoveFixedPeriod': 0.2, 
       b'pushRotOnSpotGrowPeriod': 2.0, 
       b'pushRotOnMoveGrowPeriod': 2.0, 
       b'swingCompensator': {b'enable': True, 
                             b'collisionExtend': 0.2, 
                             b'stiffnesFactor0': 1.0, 
                             b'stiffnesFactor1': 1.0, 
                             b'dampingFactor': 1.0, 
                             b'maxPitchDeviation': 0.1, 
                             b'maxRollDeviation': 0.1, 
                             b'restitution': 0.8, 
                             b'stabilisationCenter': (0.0, 0.0, 0.0)}, 
       b'powerFactor': 1.0, 
       b'angVelocityFactor': 1.0, 
       b'angVelocityFactor0': 1.0, 
       b'gimletGoalWOnSpot': 0.0, 
       b'gimletGoalWOnMove': 0.0, 
       b'rotationFactor': 1.0, 
       b'hullAiming': {b'pitch': {b'correctionCenterZ': 0.0, 
                                  b'correctionSpeed': 0.3, 
                                  b'pitchMin': (-0.2), 
                                  b'pitchMax': 0.2, 
                                  b'correctionStiffness': 30.0, 
                                  b'correctionDamping': 0.25, 
                                  b'correctionScale': 0.5}, 
                       b'yaw': {b'gimletForce': 4.0, 
                                b'stiffness': 8000.0, 
                                b'damping': 400.0, 
                                b'preciseRestitution': 0.3, 
                                b'dampingYawDist': 0.03, 
                                b'preciseYawDist': 0.03}}, 
       b'hullInertiaFactors': (1.0, 1.0, 1.8), 
       b'engineLoses': (0.5, 0.8), 
       b'enableStabilization': True, 
       b'modes': {b'siegeMode': {b'mode_index': 1, 
                                 b'engine': {b'smplEnginePower': 1.0}, 
                                 b'powerFactor': 1.0, 
                                 b'angVelocityFactor': 1.0, 
                                 b'angVelocityFactor0': 1.0, 
                                 b'gimletGoalWOnSpot': 0.0, 
                                 b'gimletGoalWOnMove': 0.0, 
                                 b'rotationFactor': 1.0}}}


def getDefaultTankXPhysicsCfg():
    return dict(getDefaultVehicleXPhysicsCfg(), **{b'vehiclePhysicsType': (VEHICLE_PHYSICS_TYPE.TANK), 
       b'shape': (getDefaultTankVehicleXPhysicsShapeCfg()), 
       b'chassis': (getDefaultChassisXPhysicsCfg())})


def getDefaultWheeledTechXPhysicsCfg():
    return dict(getDefaultVehicleXPhysicsCfg(), **{b'vehiclePhysicsType': (VEHICLE_PHYSICS_TYPE.WHEELED_TECH), 
       b'shape': (getDefaultWheeledVehicleXPhysicsShapeCfg()), 
       b'chassis': (getDefaultWheeledChassisXPhysicsCfg())})


def getAppliedGravityMultiplier(physics, typeDesc):
    baseCfg = typeDesc.type.xphysics[b'detailed']
    baseGravityFactor = baseCfg[b'gravityFactor']
    gravityMultiplier = physics.gravity / baseGravityFactor / G
    return gravityMultiplier


def init():
    updateCommonConf()
    return


def updateCommonConf():
    BigWorld.setupPhysicsParam(b'CONTACT_ENERGY_POW', CONTACT_ENERGY_POW)
    BigWorld.setupPhysicsParam(b'CONTACT_ENERGY_POW2', CONTACT_ENERGY_POW2)
    BigWorld.setupPhysicsParam(b'SLOPE_FRICTION_FUNC_DEF', SLOPE_FRICTION_FUNC_DEF)
    BigWorld.setupPhysicsParam(b'SLOPE_FRICTION_FUNC_VAL', SLOPE_FRICTION_FUNC_VAL)
    BigWorld.setupPhysicsParam(b'SLOPE_FRICTION_MODELS_FUNC_VAL', SLOPE_FRICTION_MODELS_FUNC_VAL)
    BigWorld.setupPhysicsParam(b'CONTACT_FRICTION_TERRAIN', CONTACT_FRICTION_TERRAIN)
    BigWorld.setupPhysicsParam(b'CONTACT_FRICTION_STATICS', CONTACT_FRICTION_STATICS)
    BigWorld.setupPhysicsParam(b'CONTACT_FRICTION_EXTRA', CONTACT_FRICTION_EXTRA)
    BigWorld.setupPhysicsParam(b'CONTACT_FRICTION_DESTRUCTIBLES', CONTACT_FRICTION_DESTRUCTIBLES)
    BigWorld.setupPhysicsParam(b'CONTACT_FRICTION_VEHICLES', CONTACT_FRICTION_VEHICLES)
    BigWorld.setupPhysicsParam(b'VEHICLE_ON_BODY_DEFAULT_FRICTION', VEHICLE_ON_BODY_DEFAULT_FRICTION)
    BigWorld.setupPhysicsParam(b'ROLLER_REACTION_COEFF_FOR_STATIC', ROLLER_REACTION_COEFF_FOR_STATIC)
    BigWorld.setupPhysicsParam(b'ROLLER_FRICTION_GAIN_MIN', ROLLER_FRICTION_GAIN_MIN)
    BigWorld.setupPhysicsParam(b'ROLLER_FRICTION_GAIN_MAX', ROLLER_FRICTION_GAIN_MAX)
    BigWorld.setupPhysicsParam(b'ROLLER_FRICTION_ANGLE_MIN', ROLLER_FRICTION_ANGLE_MIN)
    BigWorld.setupPhysicsParam(b'ROLLER_FRICTION_ANGLE_MAX', ROLLER_FRICTION_ANGLE_MAX)
    BigWorld.setupPhysicsParam(b'ARENA_BOUNDS_FRICTION_HOR', ARENA_BOUNDS_FRICTION_HOR)
    BigWorld.setupPhysicsParam(b'ARENA_BOUNDS_FRICTION_VERT', ARENA_BOUNDS_FRICTION_VERT)
    BigWorld.setupPhysicsParam(b'USE_PSEUDO_CONTACTS', USE_PSEUDO_CONTACTS)
    BigWorld.setupPhysicsParam(b'CONTACT_PENETRATION', CONTACT_PENETRATION)
    BigWorld.setupPhysicsParam(b'WARMSTARTING_VEHICLE_VEHICLE', WARMSTARTING_VEHICLE_VEHICLE)
    BigWorld.setupPhysicsParam(b'WARMSTARTING_VEHICLE_STATICS', WARMSTARTING_VEHICLE_STATICS)
    BigWorld.setupPhysicsParam(b'WARMSTARTING_THRESHOLD', WARMSTARTING_THRESHOLD)
    return


def updateConf():
    for e in BigWorld.entities.values():
        if e.className == b'Vehicle':
            initVehiclePhysicsServer(e.mover.physics, e.typeDescriptor)

    updateCommonConf()
    for updater in g_confUpdaters:
        updater()

    return


def updatePhysicsCfg(baseCfg, typeDesc, cfg):
    if typeDesc.type.xphysics[b'detailed'] != baseCfg:
        typeDesc.type.xphysics[b'detailed'].update(baseCfg)
    engName = typeDesc.engine.name
    engCfg = baseCfg[b'engines'].get(engName)
    if engCfg:
        cfg.setdefault(b'engine', {}).update(engCfg)
    chsName = typeDesc.chassis.name
    chsCfg = baseCfg[b'chassis'].get(chsName)
    if chsCfg:
        cfg.setdefault(b'chassis', {}).update(chsCfg)
    fakeGearBox = baseCfg.get(b'fakegearbox')
    if fakeGearBox is not None:
        cfg[b'fakegearbox'] = fakeGearBox
    swingCompensator = baseCfg.get(b'swingCompensator')
    if swingCompensator is not None:
        cfg.setdefault(b'swingCompensator', {}).update(swingCompensator)
    return


def applyVehDescrMiscFactors(typeDescr, mode):
    mode[b'engine'][b'smplFwMaxSpeed'] += KMH_TO_MS * typeDescr.miscAttrs[b'forwardMaxSpeedKMHTerm']
    mode[b'engine'][b'smplBkMaxSpeed'] += KMH_TO_MS * typeDescr.miscAttrs[b'backwardMaxSpeedKMHTerm']
    onStillRotationSpeedFactor = typeDescr.miscAttrs[b'onStillRotationSpeedFactor']
    onMoveRotationSpeedFactor = typeDescr.miscAttrs[b'onMoveRotationSpeedFactor']
    if not typeDescr.isWheeledVehicle:
        mode[b'chassis'][b'gimletGoalWOnSpot'] *= onStillRotationSpeedFactor
        mode[b'chassis'][b'angVelocityFactor0'] *= onStillRotationSpeedFactor
        mode[b'chassis'][b'gimletGoalWOnMove'] *= onMoveRotationSpeedFactor
        mode[b'chassis'][b'angVelocityFactor'] *= onMoveRotationSpeedFactor
    else:
        factor = mode[b'chassis'][b'axleSteeringAngles']
        mode[b'chassis'][b'axleSteeringAngles'] = tuple(fi * onMoveRotationSpeedFactor for fi in factor)
        factor = mode[b'chassis'][b'axleSteeringSpeed']
        mode[b'chassis'][b'axleSteeringSpeed'] = tuple(fi * onMoveRotationSpeedFactor for fi in factor)
        mode[b'chassis'][b'slowTurnChocker'] *= onStillRotationSpeedFactor
        mode[b'chassis'][b'centerRotationFwdSpeed'] *= typeDescr.miscAttrs[b'centerRotationFwdSpeedFactor']
    return


def configurePhysics(physics, baseCfg, typeDescr, gravityFactor, updateSiegeModeFromCfg):
    vehiclePhysicsType = typeDescr.type.xphysics[b'detailed'].get(b'vehiclePhysicsType', VEHICLE_PHYSICS_TYPE.TANK)
    isTank = vehiclePhysicsType == VEHICLE_PHYSICS_TYPE.TANK
    cfg = getDefaultTankXPhysicsCfg() if isTank else getDefaultWheeledTechXPhysicsCfg()
    if typeDescr.hasSiegeMode:
        defaultVehicleDescr = typeDescr.defaultVehicleDescr
        siegeVehicleDescr = typeDescr.siegeVehicleDescr
    else:
        defaultVehicleDescr = typeDescr
    try:
        cfg[b'fakegearbox'] = typeDescr.type.xphysics[b'detailed'][b'fakegearbox']
    except:
        cfg[b'fakegearbox'] = _DEFAULT_FAKE_GEARBOX_SETTINGS

    if baseCfg:
        updatePhysicsCfg(baseCfg, defaultVehicleDescr, cfg)
        if typeDescr.hasSiegeMode:
            if updateSiegeModeFromCfg and b'siegeMode' in baseCfg.get(b'modes', {}):
                siegeBaseCfg = baseCfg[b'modes'][b'siegeMode']
            else:
                siegeBaseCfg = siegeVehicleDescr.type.xphysics[b'detailed']
            updatePhysicsCfg(siegeBaseCfg, siegeVehicleDescr, cfg[b'modes'][b'siegeMode'])
    cfg = __buildConfigurations(cfg)
    for name, mode in cfg[b'modes'].iteritems():
        applyVehDescrMiscFactors(typeDescr, mode)
        configurePhysicsMode(mode, typeDescr, gravityFactor)

    if not physics.configure(cfg):
        LOG_ERROR(b'configureXPhysics: configure failed')
    physics.centerOfMass = Math.Vector3((
     0.0,
     cfg[b'modes'][b'normal'][b'clearance'] + cfg[b'modes'][b'normal'][b'bodyHeight'] * 0.5 + cfg[b'modes'][b'normal'][b'hullCOMShiftY'], physics.hullCOMZ))
    physics.isFrozen = False
    physics.movementSignals = 0
    physics.freezeAccelEpsilon = FREEZE_ACCEL_EPSILON
    physics.freezeAngAccelEpsilon = FREEZE_ANG_ACCEL_EPSILON
    physics.freezeVelEpsilon = FREEZE_VEL_EPSILON
    physics.freezeAngVelEpsilon = FREEZE_ANG_VEL_EPSILON
    physics.simulationYBound = _SIMULATION_Y_BOUND
    return cfg


def __computeModelShape(cfg, modelShapeCfg, typeDesc, boundingBoxes):
    bmin, bmax, _ = boundingBoxes[b'chassis']
    sizeX = bmax[0] - bmin[0]
    bminHull, bmaxHull, _ = boundingBoxes[b'hull']
    if typeDesc.type.useHullZSize:
        sizeZ = bmaxHull[2] - bminHull[2]
    else:
        sizeZ = bmax[2] - bmin[2]
    if typeDesc.type.useHullZOffset:
        offsZ = (bmaxHull[2] + bminHull[2]) * 0.5
    else:
        offsZ = (bmin[2] + bmax[2]) * 0.5
    modelShapeCfg[b'hullSize'] = Math.Vector3((sizeX, cfg[b'bodyHeight'], sizeZ))
    modelShapeCfg[b'hullBoxOffsetZ'] = offsZ
    if typeDesc.isWheeledVehicle:
        wheelBbMin, wheelBbMax, _ = typeDesc.chassis.wheels.wheels[0].hitTester.bbox
        wheelSize = wheelBbMax - wheelBbMin
        modelShapeCfg[b'wheelSize'] = wheelSize
    turretMin, turretMax, _ = boundingBoxes[b'turret']
    _, gunMax, _ = boundingBoxes[b'gun']
    hullPos = typeDesc.chassis.hullPosition
    turretPos = typeDesc.hull.turretPositions[0]
    topPos = hullPos + turretPos
    turretTopOffset = max(turretMax[1], typeDesc.turret.gunPosition[1] + gunMax[1])
    topPos.y += turretTopOffset - cfg[b'clearance'] - cfg[b'bodyHeight']
    topPos.y = max(0.1, topPos.y * 0.8)
    topPos.y += cfg[b'bodyHeight'] * 0.5
    modelShapeCfg[b'turretTopPos'] = topPos
    modelShapeCfg[b'turretTopWidth'] = max(sizeX * 0.25, (turretMax[0] - turretMin[0]) * 0.7)
    return


def configureModelShapePhysics(cfg, typeDesc):
    chassisDescr = typeDesc.chassis
    normalBBoxes = {b'chassis': (chassisDescr.bboxManager.normalBBox)}
    crashedBBoxes = {b'chassis': (chassisDescr.bboxManager.crashedBBox)}
    isCrashedModelValid = crashedBBoxes[b'chassis'] is not None
    htManagers = [
     (
      b'hull', typeDesc.hull.hitTesterManager),
     (
      b'turret', typeDesc.turret.hitTesterManager),
     (
      b'gun', typeDesc.gun.hitTesterManager)]
    if typeDesc.isWheeledVehicle:
        htManagers.append((b'wheel', chassisDescr.wheels.wheels[0].hitTesterManager))
    for name, htManager in htManagers:
        normalBBoxes[name] = htManager.modelHitTester.bbox
        if htManager.crashedModelHitTester:
            crashedBBoxes[name] = htManager.crashedModelHitTester.bbox
        else:
            isCrashedModelValid = False

    cfg[b'hasCrashedModel'] = isCrashedModelValid
    __computeModelShape(cfg, cfg[b'shape'][b'modelShape'], typeDesc, normalBBoxes)
    if isCrashedModelValid:
        __computeModelShape(cfg, cfg[b'shape'][b'crashedModelShape'], typeDesc, crashedBBoxes)
    return


def updatePhysics(physics, typeDesc, isSoftUpdate=False, gravityMultiplier=1.0):
    baseCfg = typeDesc.type.xphysics[b'detailed']
    gravityFactor = baseCfg[b'gravityFactor'] * gravityMultiplier
    updateSiegeModeFromCfg = False
    vehiclePhysicsType = typeDesc.type.xphysics[b'detailed'].get(b'vehiclePhysicsType', VEHICLE_PHYSICS_TYPE.TANK)
    isTank = vehiclePhysicsType == VEHICLE_PHYSICS_TYPE.TANK
    cfg = copy.deepcopy(getDefaultTankXPhysicsCfg() if isTank else getDefaultWheeledTechXPhysicsCfg())
    if typeDesc.hasSiegeMode:
        defaultVehicleDescr = typeDesc.defaultVehicleDescr
        siegeVehicleDescr = typeDesc.siegeVehicleDescr
    else:
        defaultVehicleDescr = typeDesc
    try:
        cfg[b'fakegearbox'] = typeDesc.type.xphysics[b'detailed'][b'fakegearbox']
    except:
        cfg[b'fakegearbox'] = _DEFAULT_FAKE_GEARBOX_SETTINGS

    updatePhysicsCfg(baseCfg, defaultVehicleDescr, cfg)
    if typeDesc.hasSiegeMode:
        if updateSiegeModeFromCfg and b'modes' in baseCfg and b'siegeMode' in baseCfg[b'modes']:
            siegeBaseCfg = baseCfg[b'modes'][b'siegeMode']
        else:
            siegeBaseCfg = siegeVehicleDescr.type.xphysics[b'detailed']
        updatePhysicsCfg(siegeBaseCfg, siegeVehicleDescr, cfg[b'modes'][b'siegeMode'])
    cfg = __buildConfigurations(cfg)
    for name, mode in cfg[b'modes'].iteritems():
        if isSoftUpdate:
            applyVehDescrMiscFactors(typeDesc, mode)
        configurePhysicsMode(mode, typeDesc, gravityFactor)

    if not isSoftUpdate:
        oldMatrix = Math.Matrix(physics.matrix)
        inversedMatrix = Math.Matrix(oldMatrix)
        inversedMatrix.invert()
        oldCoM = physics.centerOfMass
        newCoM = Math.Vector3((
         0.0,
         cfg[b'modes'][b'normal'][b'clearance'] + cfg[b'modes'][b'normal'][b'bodyHeight'] * 0.5 + cfg[b'modes'][b'normal'][b'hullCOMShiftY'], physics.hullCOMZ))
        compression = inversedMatrix.applyPoint(physics.currentCenterOfMass).y / oldCoM.y
        dy = (newCoM.y - oldCoM.y) * compression
        physics.centerOfMass = newCoM
        newMatrix = Math.Matrix()
        newMatrix.setTranslate(oldMatrix.applyToAxis(1) * dy)
        newMatrix.preMultiply(oldMatrix)
        physics.matrix = newMatrix
    physics.isFrozen = False
    physics.updateSettings(cfg)
    return cfg


def configurePhysicsMode(cfg, typeDesc, gravityFactor):
    cfg[b'angVelocityFactor'] = cfg[b'chassis'][b'angVelocityFactor']
    cfg[b'angVelocityFactor0'] = cfg[b'chassis'][b'angVelocityFactor0']
    cfg[b'axleCount'] = cfg[b'chassis'][b'axleCount']
    if cfg[b'vehiclePhysicsType'] == VEHICLE_PHYSICS_TYPE.WHEELED_TECH:
        for key in (b'axleSteeringLockAngles', b'axleSteeringAngles', b'axleSteeringSpeed', b'fwdFrictionOnAxisModifiers', b'sideFrictionOnAxisModifiers', b'sideFrictionConstantRatioOnAxis', b'sinkageResistOnAxis', b'axleIsLeading', b'axleCanBeRised', b'wheelRiseHeight', b'wheelRiseSpeed', b'enableRail', b'handbrakeBrakeForce', b'brokenWheelRollingFrictionModifier', b'noSignalBrakeForce', b'afterDeathBrakeForce', b'afterDeathMinSpeedForImpulse', b'afterDeathImpulse', b'jumpingFactor', b'jumpingMinForce', b'slowTurnChocker', b'airPitchReduction', b'wheelToHullRollTransmission', b'steeringSpeedInTurnMultiplier', b'isWheeledOnSpotRotation'):
            cfg[key] = cfg[b'chassis'][key]

    cfg[b'gimletGoalWOnSpot'] = cfg[b'chassis'][b'gimletGoalWOnSpot']
    cfg[b'gimletGoalWOnMove'] = cfg[b'chassis'][b'gimletGoalWOnMove']
    cfg[b'isRotationAroundCenter'] = cfg[b'chassis'][b'isRotationAroundCenter']
    cfg[b'centerRotationFwdSpeed'] = cfg[b'chassis'][b'centerRotationFwdSpeed']
    cfg[b'movementRevertSpeed'] = cfg[b'chassis'][b'movementRevertSpeed']
    cfg[b'fwLagRatio'] = cfg[b'chassis'][b'fwLagRatio']
    cfg[b'bkLagRatio'] = cfg[b'chassis'][b'bkLagRatio']
    cfg[b'rotFritionFactor'] = cfg[b'chassis'][b'rotFritionFactor']
    cfg[b'comFrictionYOffs'] = cfg[b'chassis'][b'comFrictionYOffs']
    cfg[b'comSideFriction'] = cfg[b'chassis'][b'comSideFriction']
    cfg[b'pushStop'] = cfg[b'chassis'][b'pushStop']
    cfg[b'gimletPushOnSpotInit'] = cfg[b'chassis'][b'gimletPushOnSpotInit']
    cfg[b'gimletPushOnSpotFinal'] = cfg[b'chassis'][b'gimletPushOnSpotFinal']
    cfg[b'gimletPushOnMoveInit'] = cfg[b'chassis'][b'gimletPushOnMoveInit']
    cfg[b'gimletPushOnMoveFinal'] = cfg[b'chassis'][b'gimletPushOnMoveFinal']
    cfg[b'gimletVelScaleMin'] = cfg[b'chassis'][b'gimletVelScaleMin']
    cfg[b'gimletVelScaleMax'] = cfg[b'chassis'][b'gimletVelScaleMax']
    cfg[b'pushRotOnSpotFixedPeriod'] = cfg[b'chassis'][b'pushRotOnSpotFixedPeriod']
    cfg[b'pushRotOnMoveFixedPeriod'] = cfg[b'chassis'][b'pushRotOnMoveFixedPeriod']
    cfg[b'pushRotOnSpotGrowPeriod'] = cfg[b'chassis'][b'pushRotOnSpotGrowPeriod']
    cfg[b'pushRotOnMoveGrowPeriod'] = cfg[b'chassis'][b'pushRotOnMoveGrowPeriod']
    cfg[b'smplFwMaxSpeed'] = cfg[b'engine'][b'smplFwMaxSpeed']
    cfg[b'smplBkMaxSpeed'] = cfg[b'engine'][b'smplBkMaxSpeed']
    cfg[b'powerFactor'] = cfg[b'engine'][b'powerFactor']
    cfg[b'rotationFactor'] = cfg[b'engine'][b'rotationFactor']
    cfg[b'bodyHeight'] = cfg[b'chassis'][b'bodyHeight']
    cfg[b'hullCOMShiftY'] = cfg[b'chassis'][b'hullCOMShiftY']
    cfg[b'hullInertiaFactors'] = cfg[b'chassis'][b'hullInertiaFactors']
    cfg[b'clearance'] = cfg[b'chassis'][b'clearance']
    cfg[b'fullMass'] = typeDesc.physics[b'weight'] * WEIGHT_SCALE
    selfDrivenMaxSpeed = max(cfg[b'smplFwMaxSpeed'], cfg[b'smplBkMaxSpeed'])
    speedLimit = min(cfg[b'absoluteSpeedLimit'], selfDrivenMaxSpeed * cfg[b'allowedRPMExcessUnbounded'])
    cfg[b'allowedRPMExcess'] = max(1.0, speedLimit / selfDrivenMaxSpeed)
    cfg[b'overspeedResistFactor'] = cfg[b'overspeedResistBaseFactor'] / selfDrivenMaxSpeed
    cfg[b'useComplexForm'] = typeDesc.type.name == b'sweden:S11_Strv_103B'
    configureModelShapePhysics(cfg, typeDesc)
    if typeDesc.isWheeledVehicle:
        cfg[b'shape'][b'wheelXOffset'] = max(abs(wheel.position.x) for wheel in typeDesc.chassis.wheels.wheels)
    cfg[b'shape'][b'useComplexForm'] = typeDesc.type.name == b'sweden:S11_Strv_103B'
    cfg[b'gravity'] = cfg[b'gravity'] * gravityFactor
    cfg[b'engine'][b'engineTorque'] = tuple((arg, val * gravityFactor) for arg, val in cfg[b'engine'][b'engineTorque'])
    cfg[b'pushHB'] = cfg.get(b'gimletPushOnSpotFinal', 0.0)
    cfg[b'engine'][b'smplEngJoinRatio'] = 0.020000000000000004 / cfg[b'chassis'][b'wheelRadius']
    applyRotationAndPowerFactors(cfg)
    cfg[b'siegeModeAvailable'] = typeDesc.hasSiegeMode
    cfg[b'isWheeledVehicle'] = typeDesc.isWheeledVehicle
    hullAimingParams = typeDesc.type.hullAimingParams
    hullAimingParamsPitch = hullAimingParams[b'pitch']
    hullAimingPitchCfg = cfg[b'hullAiming'][b'pitch']
    hullAimingPitchCfg[b'correctionCenterZ'] = hullAimingParamsPitch[b'wheelCorrectionCenterZ']
    hullAimingPitchCfg[b'correctionSpeed'] = hullAimingParamsPitch[b'wheelsCorrectionSpeed']
    hullAimingPitchCfg[b'pitchMin'] = -hullAimingParamsPitch[b'wheelsCorrectionAngles'][b'pitchMax']
    hullAimingPitchCfg[b'pitchMax'] = -hullAimingParamsPitch[b'wheelsCorrectionAngles'][b'pitchMin']
    cfg[b'enableStabilization'] = cfg[b'swingCompensator'][b'enable']
    cfg[b'gimlet'][b'wPushedRot'] = cfg[b'wPushedRot']
    cfg[b'gimlet'][b'wPushedDiag'] = cfg[b'wPushedDiag']
    cfg[b'gimlet'][b'wPushedHB'] = cfg[b'wPushedHB']
    cfg[b'gimlet'][b'pushHB'] = cfg[b'pushHB']
    cfg[b'gimlet'][b'pushStop'] = cfg[b'pushStop']
    cfg[b'gimlet'][b'gimletPushOnSpotInit'] = cfg[b'gimletPushOnSpotInit']
    cfg[b'gimlet'][b'gimletPushOnSpotFinal'] = cfg[b'gimletPushOnSpotFinal']
    cfg[b'gimlet'][b'gimletPushOnMoveInit'] = cfg[b'gimletPushOnMoveInit']
    cfg[b'gimlet'][b'gimletPushOnMoveFinal'] = cfg[b'gimletPushOnMoveFinal']
    cfg[b'gimlet'][b'gimletVelScaleMin'] = cfg[b'gimletVelScaleMin']
    cfg[b'gimlet'][b'gimletVelScaleMax'] = cfg[b'gimletVelScaleMax']
    cfg[b'gimlet'][b'pushRotOnSpotFixedPeriod'] = cfg[b'pushRotOnSpotFixedPeriod']
    cfg[b'gimlet'][b'pushRotOnMoveFixedPeriod'] = cfg[b'pushRotOnMoveFixedPeriod']
    cfg[b'gimlet'][b'pushRotOnSpotGrowPeriod'] = cfg[b'pushRotOnSpotGrowPeriod']
    cfg[b'gimlet'][b'pushRotOnMoveGrowPeriod'] = cfg[b'pushRotOnMoveGrowPeriod']
    cfg[b'engine'][b'rotationByLockChoker'] = cfg[b'chassis'][b'rotationByLockChoker']
    del cfg[b'chassis'][b'rotationByLockChoker']
    cfg[b'engine'][b'engVelMax'] = cfg[b'smplFwMaxSpeed'] / cfg[b'chassis'][b'wheelRadius'] / cfg[b'engine'][b'smplEngJoinRatio']
    cfg[b'engine'][b'engVelBkMax'] = cfg[b'smplBkMaxSpeed'] / cfg[b'chassis'][b'wheelRadius'] / cfg[b'engine'][b'smplEngJoinRatio']
    cfg[b'engine'][b'engVelRot'] = cfg[b'smplRotSpeed'] / cfg[b'chassis'][b'wheelRadius'] / cfg[b'engine'][b'smplEngJoinRatio']
    cfg[b'chassis'][b'chassisMass'] = cfg[b'fullMass'] * cfg[b'chassis'][b'chassisMassFraction']
    cfg[b'chassis'][b'hullAiming'] = cfg[b'hullAiming']
    return


def applyRotationAndPowerFactors(cfg):
    try:
        cfg[b'engine'][b'smplEnginePower'] = cfg[b'engine'][b'smplEnginePower'] * cfg[b'powerFactor']
        cfg[b'angVelocityFactor'] = cfg[b'angVelocityFactor'] * cfg[b'rotationFactor']
        arm = cfg[b'shape'][b'modelShape'][b'hullSize'][0]
        cfg[b'smplRotSpeed'] = arm * cfg[b'angVelocityFactor0'] * cfg[b'rotationFactor']
        cfg[b'gimletGoalWOnSpot'] = cfg[b'gimletGoalWOnSpot'] * cfg[b'rotationFactor']
        cfg[b'gimletGoalWOnMove'] = cfg[b'gimletGoalWOnMove'] * cfg[b'rotationFactor']
        cfg[b'wPushedRot'] = cfg[b'gimletGoalWOnSpot']
        cfg[b'wPushedHB'] = cfg[b'wPushedRot'] * 0.98
        cfg[b'wPushedDiag'] = cfg[b'gimletGoalWOnMove']
    except:
        LOG_CURRENT_EXCEPTION()

    return


def initVehiclePhysicsServer(physics, typeDesc):
    baseCfg = typeDesc.type.xphysics[b'detailed']
    gravityFactor = baseCfg[b'gravityFactor']
    configurePhysics(physics, baseCfg, typeDesc, gravityFactor, False)
    return


def initVehiclePhysicsForced(physics, typeDesc, forcedCfg):
    baseCfg = forcedCfg
    gravityFactor = forcedCfg[b'gravityFactor']
    configurePhysics(physics, baseCfg, typeDesc, gravityFactor, True)
    return


def initVehiclePhysicsEditor(physics, typeDesc):
    initVehiclePhysicsServer(physics, typeDesc)
    initVehiclePhysicsClient(physics, typeDesc)
    return


def initVehiclePhysicsClient(physics, typeDesc):
    physDescr = typeDesc.physics
    hullMin, hullMax, _ = typeDesc.hull.hitTester.bbox
    hullCenter = (hullMin + hullMax) * 0.5
    hullY = hullCenter.y + typeDesc.chassis.hullPosition.y
    hullHeight = hullMax.y - hullMin.y
    bmin, bmax, _ = typeDesc.chassis.hitTester.bbox
    chassisCenter = (bmin + bmax) * 0.5
    blen = bmax[2] - bmin[2]
    width = bmax[0] - bmin[0]
    height = bmax[1] - bmin[1]
    if blen == 0.0 and width == 0.0 and height == 0.0:
        LOG_ERROR(b'Invalid bounding box for', typeDesc.name)
        blen = width = height = 1.0
    srcEnginePower = physDescr[b'enginePower']
    srcMass = physDescr[b'weight']
    fullMass = physDescr[b'weight'] * WEIGHT_SCALE
    clearance = (typeDesc.chassis.hullPosition.y + hullMin.y) * CLEARANCE
    clearance = _clamp(CLEARANCE_MIN * height, clearance, CLEARANCE_MAX * height)
    suspCompression = _computeSuspCompression(fullMass)
    carringSpringLength = clearance / suspCompression
    cmShift = _computeCenterOfMassShift(srcMass, srcEnginePower)
    if not IS_EDITOR:
        physics.centerOfMass = Math.Vector3((0.0, hullY + cmShift * hullHeight, 0.0))
    chassisMaxY = bmax[1]
    hullPosY = typeDesc.chassis.hullPosition[1]
    hullMaxY = hullPosY + hullMax[1]
    turretPosY = typeDesc.hull.turretPositions[0][1]
    turretMaxY = hullPosY + turretPosY + typeDesc.turret.hitTester.bbox[1][1]
    commonBoxMaxY = max(chassisMaxY, hullMaxY, turretMaxY)
    gunPosY = hullPosY + turretPosY + typeDesc.turret.gunPosition[1]
    hullUpperBound = typeDesc.chassis.hullPosition.y + hullMax.y
    boxHeight = min(commonBoxMaxY, gunPosY, hullUpperBound * BODY_HEIGHT) - clearance
    boxHeight = max(chassisMaxY * 0.7, boxHeight, VEHICLE_ON_OBSTACLE_COLLISION_BOX_MIN_HEIGHT)
    globalBoxY = clearance + boxHeight / 2
    boxCenter = Math.Vector3(chassisCenter)
    boxCenter[1] = globalBoxY - physics.centerOfMass.y
    physics.removeAllDamperSprings()
    if clearance != 0.0:
        clearanceRatio = width / clearance
    else:
        LOG_ERROR(b'Clearance is null')
        clearanceRatio = CLEARANCE_RATIO_LONG
    if width < WIDTH_VERY_LONG and (width < WIDTH_LONG or clearanceRatio < CLEARANCE_RATIO_LONG):
        carrierSpringPairs = NUM_SPRINGS_NORMAL
    else:
        carrierSpringPairs = NUM_SPRINGS_LONG
    length = carringSpringLength
    hullAimingLength = carringSpringLength
    trackLen = _computeTrackLength(clearance, blen)
    indent = boxHeight / 2
    hardRatio = _computeHardRatio(clearance, blen)
    if (IS_CLIENT or IS_EDITOR) and typeDesc.isPitchHullAimingAvailable:
        springExtendMultiplier = 2.0
        hardRatio = 0
        hullAngleMin = typeDesc.type.hullAimingParams[b'pitch'][b'wheelsCorrectionAngles'][b'pitchMin']
        hullAngleMax = typeDesc.type.hullAimingParams[b'pitch'][b'wheelsCorrectionAngles'][b'pitchMax']
        backSpringLength = blen * math.sin(abs(hullAngleMax)) * springExtendMultiplier
        frontSpringLength = blen * math.sin(abs(hullAngleMin)) * springExtendMultiplier
        hullAimingLength = max(backSpringLength, frontSpringLength)
    if (IS_CLIENT or IS_EDITOR) and typeDesc.hasSiegeMode and typeDesc.isPitchHullAimingAvailable:
        springsLengthList = tuple(length for _ in xrange(0, carrierSpringPairs))
        hullAimingSpringsLengthList = tuple(hullAimingLength for _ in xrange(0, carrierSpringPairs))
        for descriptor in [typeDesc.defaultVehicleDescr, typeDesc.siegeVehicleDescr]:
            if descriptor.chassis.suspensionSpringsLength is not None:
                break
            hullAimingEnabled = descriptor.type.hullAimingParams[b'pitch'][b'isEnabled']
            descriptor.chassis.suspensionSpringsLength = {b'left': (hullAimingSpringsLengthList if hullAimingEnabled else springsLengthList), 
               b'right': (hullAimingSpringsLengthList if hullAimingEnabled else springsLengthList)}

    stepZ = trackLen / (carrierSpringPairs - 1)
    begZ = -trackLen * 0.5
    leftX = -width * 0.45
    rightX = width * 0.45
    y = -boxHeight / 2 + boxCenter.y
    for i in xrange(0, carrierSpringPairs):
        mountPoint = Math.Vector3((leftX, y, begZ + i * stepZ))
        physics.addDamperSpring((
         mountPoint,
         length,
         indent,
         True,
         hardRatio))
        mountPoint = Math.Vector3((rightX, y, begZ + i * stepZ))
        physics.addDamperSpring((
         mountPoint,
         length,
         indent,
         False,
         hardRatio))

    if _LOG_INIT_PARAMS:
        LOG_DEBUG(b'initVehiclePhysics: clearance %f' % (clearance / height))
        LOG_DEBUG(b'initVehiclePhysics: clearanceRatio %f' % (clearance / blen))
        LOG_DEBUG(b'initVehiclePhysics: cmShift %f' % cmShift)
        LOG_DEBUG(b'initVehiclePhysics: suspCompression: %f' % suspCompression)
    return


def computeBarrelLocalPoint(vehDescr, turretYaw, gunPitch):
    maxGunZ = vehDescr.gun.hitTester.bbox[1][2]
    m = Math.Matrix()
    m.setRotateX(gunPitch)
    pt = m.applyVector((0.0, 0.0, maxGunZ)) + vehDescr.activeGunShotPosition
    m.setRotateY(turretYaw)
    pt = m.applyVector(pt)
    pt += vehDescr.hull.turretPositions[vehDescr.activeTurretPosition]
    pt += vehDescr.chassis.hullPosition
    return pt


def linearInterpolate(arg, argMin, argMax, valMin, valMax):
    argRange = argMax - argMin
    narg = (arg - argMin) / argRange
    narg = _clamp(0.0, narg, 1.0)
    valRange = valMax - valMin
    val = narg * valRange + valMin
    return val


def _computeCenterOfMassShift(mass, enginePower):
    dr = enginePower / mass
    cmy = _powerCurve(dr, DYN_RATIO_MIN, DYN_RATIO_MID, DYN_RATIO_MAX, CMY_MIN, CMY_MID, CMY_MAX)
    return cmy


def _computeSuspCompression(mass):
    suspCompression = linearInterpolate(mass, SUSP_COMPRESSION_MIN_MASS, SUSP_COMPRESSION_MAX_MASS, SUSP_COMPRESSION_MIN, SUSP_COMPRESSION_MAX)
    return suspCompression


def _computeTrackLength(clearance, length):
    r = clearance / length
    lenRatio = linearInterpolate(r, CLEARANCE_TO_LENGTH_MIN, CLEARANCE_TO_LENGTH_MAX, TRACK_LENGTH_MAX, TRACK_LENGTH_MIN)
    return lenRatio * length


def _computeHardRatio(clearance, length):
    r = clearance / length
    return linearInterpolate(r, CLEARANCE_TO_LENGTH_MIN, CLEARANCE_TO_LENGTH_MAX, HARD_RATIO_MIN, HARD_RATIO_MAX)


def _powerCurve(arg, argMin, argMid, argMax, valMin, valMid, valMax):
    argRange = argMax - argMin
    narg = (arg - argMin) / argRange
    narg = _clamp(0.0, narg, 1.0)
    nargMid = (argMid - argMin) / argRange
    valRange = valMax - valMin
    nvalMid = (valMid - valMin) / valRange
    pow = math.log(nvalMid, nargMid)
    nval = math.pow(narg, pow)
    val = nval * valRange + valMin
    return val


def _clamp(minBound, arg, maxBound):
    if arg < minBound:
        return minBound
    if arg > maxBound:
        return maxBound
    return arg


TRACK_SCROLL_LIMITS = (-15.0, 30.0)

def encodeTrackScrolling(leftScroll, rightScroll):
    return encodeRestrictedValueToUint(leftScroll, 8, *TRACK_SCROLL_LIMITS) | encodeRestrictedValueToUint(rightScroll, 8, *TRACK_SCROLL_LIMITS) << 8


def decodeTrackScrolling(code):
    return (
     decodeRestrictedValueFromUint((code & 255), 8, *TRACK_SCROLL_LIMITS),
     decodeRestrictedValueFromUint((code >> 8), 8, *TRACK_SCROLL_LIMITS))


def __deepUpdate(orig_dict, new_dict):
    if orig_dict is new_dict:
        return
    for key, val in new_dict.iteritems():
        if isinstance(val, collections.Mapping):
            tmp = __deepUpdate(orig_dict.get(key, {}), val)
            orig_dict[key] = tmp
        else:
            orig_dict[key] = new_dict[key]

    return orig_dict


def __buildConfigurations(configuration):
    configurations = {b'normal': configuration}
    modes = configuration.get(b'modes')
    if modes is not None:
        del configurations[b'normal'][b'modes']
        for key, value in modes.iteritems():
            basic = copy.deepcopy(configuration)
            modified = __deepUpdate(basic, value)
            configurations[key] = modified

    return {b'vehiclePhysicsType': (configuration[b'vehiclePhysicsType']), b'modes': configurations}


def getShootTimeCorrection(roundTripTime):
    return min(0.3, roundTripTime + SERVER_TICK_LENGTH * 0.5)


_DEFAULT_FAKE_GEARBOX_SETTINGS = {b'fwdgears': {b'switchSpeed': (2, 5, 15), 
                 b'switchHysteresis': (1, 2, 3), 
                 b'lowRpm': (0.2, 0.2, 0.2), 
                 b'highRpm': (0.9, 0.9, 0.9)}, 
   b'bkwdgears': {b'switchSpeed': (2, 5, 15), 
                  b'switchHysteresis': (1, 2, 3), 
                  b'lowRpm': (0.2, 0.2, 0.2), 
                  b'highRpm': (0.9, 0.9, 0.9)}}
