import BigWorld, CGF
from constants import IS_EDITOR
if IS_EDITOR:

    class Vehicle(object):
        pass


_portalManagers = {}

def registerPortalManager(domain):

    def registrator(cls):
        CGF.registerManager(cls, False, domain)
        _portalManagers[cls.__name__] = (cls, domain)
        return cls

    return registrator


def portalManagers():
    return _portalManagers


SENTRY_GUN_LABEL_PREFIX = b'sentryGunPortal_'

def isSentryGunVehicle(vehicle):
    return vehicle.label and vehicle.label.startswith(SENTRY_GUN_LABEL_PREFIX)


CAMP_LABEL_PREFIX = b'camp_'

def isCampVehicle(vehicle):
    return vehicle.label and vehicle.label.startswith(CAMP_LABEL_PREFIX)


ASSISTANT_LABEL = b'super_boss_assistant'

def isAssistantVehicle(vehicle):
    return vehicle.label and vehicle.label.startswith(ASSISTANT_LABEL)


WAVE_LABEL_PREFIX = b'wave'

def isWaveVehicle(vehicle):
    return vehicle.label and vehicle.label.startswith(WAVE_LABEL_PREFIX)


SUPER_BOSS_LABEL = b'portal_super_boss'
MAIN_BOSS_LABEL = b'portal_main_boss'

def isMainBoss(vehicle):
    return vehicle.label == MAIN_BOSS_LABEL


def isSuperBoss(vehicle):
    return vehicle.label == SUPER_BOSS_LABEL


def isLowPreset():
    presetIndex = BigWorld.detectGraphicsPresetFromSystemSettings()
    lowPresetIndex = BigWorld.getSystemPerformancePresetIdFromName(b'LOW')
    return presetIndex >= lowPresetIndex
