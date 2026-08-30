from enum import Enum
from frameworks.wulf import ViewModel

class Characteristic(Enum):
    CREW = b'crew'
    MASS = b'mass'
    ARMOR = b'armor'
    CALIBER = b'caliber'
    SPEED = b'speed'
    WEAPON = b'weapon'
    COMBATCREW = b'combatCrew'
    POWER = b'power'


class MuseumVehicleCharacteristics(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MuseumVehicleCharacteristics, self).__init__(properties=properties, commands=commands)
        return

    def getKey(self):
        return Characteristic(self._getString(0))

    def setKey(self, value):
        self._setString(0, value.value)
        return

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(MuseumVehicleCharacteristics, self)._initialize()
        self._addStringProperty(b'key')
        self._addStringProperty(b'value', b'')
        return
