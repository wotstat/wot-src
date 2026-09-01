from enum import Enum
from frameworks.wulf import ViewModel

class GeneratorStatusEnum(Enum):
    ACTIVE = b'active'
    LOCKED = b'locked'
    DESTROYED = b'destroyed'


class GeneratorStatusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(GeneratorStatusModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getProgress(self):
        return self._getNumber(1)

    def setProgress(self, value):
        self._setNumber(1, value)
        return

    def getGeneratorStatus(self):
        return GeneratorStatusEnum(self._getString(2))

    def setGeneratorStatus(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(GeneratorStatusModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'progress', 0)
        self._addStringProperty(b'generatorStatus', GeneratorStatusEnum.ACTIVE.value)
        return
