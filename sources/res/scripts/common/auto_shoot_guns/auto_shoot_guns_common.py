from __future__ import absolute_import
from constants import SERVER_TICK_LENGTH
DISCRETE_SHOOTING_THRESHOLD = 0.25
BURST_VERIFYING_DELTA = 0.0
BURST_CONFIRMATION_DELTA = 0.5
BURST_CONFIRMATION_TIMEOUT = BURST_CONFIRMATION_DELTA * 4
PROJECTILE_LOG_FREQUENCY_LIMIT = 10
ASSIST_LOG_FREQUENCY_TIMEOUT = 1.0
COMBAT_ACTIONS_DELAY = 1.0

class PROJECTILE_INTERVAL_SETTINGS:
    PROJECTILE_INTERVAL_LIMITS = [
     8, 16]
    DEFAULT_PROJECTILE_INTERVAL = SERVER_TICK_LENGTH


class AutoShootGunState(object):
    NONE = 0
    CONTINUOUS_SHOOTING = 1
    DISCRETE_SHOOTING = 2
    DELAY_SHOOT = 3
    NOT_SHOOT = 4
    SHOOTING_STATES = (
     CONTINUOUS_SHOOTING, DISCRETE_SHOOTING)
    NAMES = {NONE: b'none', 
       CONTINUOUS_SHOOTING: b'continuous_shooting', 
       DISCRETE_SHOOTING: b'discrete_shooting', 
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


def autoShootDynamicAttrFactors():
    factors = {b'shotIntervalMultFactor': 1.0, 
       b'isDelayShooting': False, 
       b'maxShotDispersionFactor': 1.0, 
       b'projectileIntervalFactor': 1.0, 
       b'shotDispersionPerShotFactor': 1.0}
    return factors
