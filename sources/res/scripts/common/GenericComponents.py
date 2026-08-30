import enum

class TransformComponent:

    def __init__(self, matrix):
        return


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
        if health < maxHealth * self.__redHealth / 100:
            return EHealthGradation.RED_ZONE
        if health < maxHealth * self.__yellowHealth / 100:
            return EHealthGradation.YELLOW_ZONE
        return EHealthGradation.GREEN_ZONE
