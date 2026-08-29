from enum import Enum
from frameworks.wulf import ViewModel

class HintIDs(Enum):
    BLUEPRINTSCONVERT = b'BlueprintsTechtreeConvertButtonHint'
    TECHTREEACTION = b'TechTreeActionStartNodeHint'


class CustomTechTreeHint(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CustomTechTreeHint, self).__init__(properties=properties, commands=commands)
        return

    def getHintID(self):
        return HintIDs(self._getString(0))

    def setHintID(self, value):
        self._setString(0, value.value)
        return

    def getHintText(self):
        return self._getString(1)

    def setHintText(self, value):
        self._setString(1, value)
        return

    def getNodeID(self):
        return self._getNumber(2)

    def setNodeID(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(CustomTechTreeHint, self)._initialize()
        self._addStringProperty(b'hintID')
        self._addStringProperty(b'hintText', b'')
        self._addNumberProperty(b'nodeID', -1)
        return
