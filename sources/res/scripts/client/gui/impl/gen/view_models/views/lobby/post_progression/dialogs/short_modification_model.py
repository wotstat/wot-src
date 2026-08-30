from enum import Enum
from frameworks.wulf import ViewModel

class ModificationType(Enum):
    MODIFICATION = b'modification'
    PAIRMODIFICATION = b'pairModification'
    MODIFICATIONWITHFEATURE = b'modificationWithFeature'


class ShortModificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ShortModificationModel, self).__init__(properties=properties, commands=commands)
        return

    def getModificationName(self):
        return self._getString(0)

    def setModificationName(self, value):
        self._setString(0, value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getModificationType(self):
        return self._getString(2)

    def setModificationType(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ShortModificationModel, self)._initialize()
        self._addStringProperty(b'modificationName', b'')
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'modificationType', b'')
        return
