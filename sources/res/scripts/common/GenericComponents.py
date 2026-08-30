from __future__ import absolute_import
import enum
COMPOSITION_ROOT_SLOT_NAME = b'compositionRootSlot'

class EHealthGradation(enum.Enum):
    RED_ZONE = b'RED_ZONE'
    YELLOW_ZONE = b'YELLOW_ZONE'
    GREEN_ZONE = b'GREEN_ZONE'


class HealthGradationComponent:

    def __init__(self, redHealth, yellowHealth):
        self.__redHealth = redHealth
        self.__yellowHealth = yellowHealth
        return

    def getHealthZone(self, health, maxHealth):
        if health < maxHealth * self.__redHealth // 100:
            return EHealthGradation.RED_ZONE
        if health < maxHealth * self.__yellowHealth // 100:
            return EHealthGradation.YELLOW_ZONE
        return EHealthGradation.GREEN_ZONE


class CyclicActivatorComponent(object):
    pass


class VSEComponent(object):
    pass


class StateSwitcherComponent(object):
    NONE_STATE = 0
    NORMAL_STATE = 1
    DAMAGED_STATE = 2
    CRITICAL_STATE = 3
