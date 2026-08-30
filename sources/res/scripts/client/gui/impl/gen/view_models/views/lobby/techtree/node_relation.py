from enum import IntEnum
from frameworks.wulf import ViewModel

class LineType(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1
    H_V = 2


class NodeRelation(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(NodeRelation, self).__init__(properties=properties, commands=commands)
        return

    def getNodeInId(self):
        return self._getNumber(0)

    def setNodeInId(self, value):
        self._setNumber(0, value)
        return

    def getNodeOutId(self):
        return self._getNumber(1)

    def setNodeOutId(self, value):
        self._setNumber(1, value)
        return

    def getLineType(self):
        return LineType(self._getNumber(2))

    def setLineType(self, value):
        self._setNumber(2, value.value)
        return

    def _initialize(self):
        super(NodeRelation, self)._initialize()
        self._addNumberProperty(b'nodeInId', 0)
        self._addNumberProperty(b'nodeOutId', 0)
        self._addNumberProperty(b'lineType')
        return
