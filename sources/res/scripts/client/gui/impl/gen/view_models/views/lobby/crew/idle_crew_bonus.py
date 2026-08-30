from enum import Enum
from frameworks.wulf import ViewModel

class IdleCrewBonusEnum(Enum):
    DISABLED = b'Disabled'
    ENABLED = b'Enabled'
    ACTIVEONCURRENTVEHICLE = b'ActiveOnCurrentVehicle'
    INCOMPATIBLEWITHCURRENTVEHICLE = b'IncompatibleWithCurrentVehicle'
    ACTIVEONANOTHERVEHICLE = b'ActiveOnAnotherVehicle'
    POSTPROGRESSIONREACHED = b'PostProgressionReached'
    INVISIBLE = b'Invisible'


class IdleCrewBonus(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(IdleCrewBonus, self).__init__(properties=properties, commands=commands)
        return

    def getIdleCrewBonus(self):
        return IdleCrewBonusEnum(self._getString(0))

    def setIdleCrewBonus(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(IdleCrewBonus, self)._initialize()
        self._addStringProperty(b'IdleCrewBonus')
        return
