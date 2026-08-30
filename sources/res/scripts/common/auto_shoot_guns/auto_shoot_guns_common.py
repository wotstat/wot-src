PROJECTILE_INTERVAL = 0.2
BURST_ACTIVATION_MIN_TIMEOUT = 0.0
BURST_ACTIVATION_MAX_TIMEOUT = 1.0
BURST_DEACTIVATION_MIN_TIMEOUT = 0.0
BURST_DEACTIVATION_MAX_TIMEOUT = 1.0
BURST_VERIFYING_DELTA = 0.0
BURST_CONFIRMATION_DELTA = 0.5
BURST_CONFIRMATION_TIMEOUT = BURST_CONFIRMATION_DELTA * 4
CLIP_MAX_INTERVAL = PROJECTILE_INTERVAL
CLIP_MIN_RATE = 1.0 / CLIP_MAX_INTERVAL
AUTOSHOOT_MAX_INTERVAL = 1.0

class AutoShootGunState(object):
    NONE = 0
    SHOOT = 1
    DELAY_SHOOT = 2
    NOT_SHOOT = 3
    SHOOTING_STATES = (
     SHOOT, DELAY_SHOOT)
    NAMES = {NONE: b'none', 
       SHOOT: b'shoot', 
       DELAY_SHOOT: b'delay_shoot', 
       NOT_SHOOT: b'not_shoot'}


class AutoShootPredictionState(object):
    NOT_ACTIVE = 0
    ACTIVATION = 1
    ACTIVE = 2
    DEACTIVATION = 3
    COOLDOWN = 4
    ACTIVATED = (
     ACTIVE, DEACTIVATION)
    CONFIRMABLE = (
     NOT_ACTIVE, ACTIVE)
    COOLDOWNABLE = (ACTIVATION, ACTIVE, DEACTIVATION)
    DISABLEABLE = (ACTIVATION, ACTIVE)
    NAMES = {NOT_ACTIVE: b'not_active', 
       ACTIVATION: b'activation', 
       ACTIVE: b'active', 
       DEACTIVATION: b'deactivation', 
       COOLDOWN: b'cooldown'}


class SpinGunState(object):
    NOT_STARTED = 0
    SPIN_UP = 1
    SPIN_FULL = 2
    SPIN_DOWN = 3
    ACTIVE_STATES = (
     SPIN_FULL, SPIN_UP, SPIN_DOWN)
    DYNAMIC_STATES = (SPIN_UP, SPIN_DOWN)


def autoShootDynamicAttrFactors():
    factors = {b'rate/multiplier': 1.0, 
       b'isDelayShooting': False, 
       b'shotDispersionPerSecFactor': 1.0, 
       b'maxShotDispersionFactor': 1.0}
    return factors
