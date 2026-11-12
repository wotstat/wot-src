from enum import Enum
from frameworks.wulf import ViewModel

class CustomizationZone(Enum):
    UNDEFINED = b''
    FIR = b'Fir'
    TEREM = b'Terem'
    INSTALLATIONS = b'Installations'
    FAIR = b'Fair'
    SNOW_SLIDE = b'SnowSlide'
    FIREWORKS = b'Fireworks'


class CustomizationZoneTypeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(CustomizationZoneTypeModel, self).__init__(properties=properties, commands=commands)
        return

    def getValue(self):
        return CustomizationZone(self._getString(0))

    def setValue(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(CustomizationZoneTypeModel, self)._initialize()
        self._addStringProperty(b'value', CustomizationZone.UNDEFINED.value)
        return
