from enum import Enum
from frameworks.wulf import ViewModel

class DetailStatus(Enum):
    DONE = b'done'
    IN_PROGRESS = b'inProgress'
    NOT_RECEIVED = b'notReceived'
    DEFAULT = b'default'


class DetailModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DetailModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return DetailStatus(self._getString(0))

    def setStatus(self, value):
        self._setString(0, value.value)
        return

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getEarnedPoint(self):
        return self._getNumber(2)

    def setEarnedPoint(self, value):
        self._setNumber(2, value)
        return

    def getHasAssemblingVideo(self):
        return self._getBool(3)

    def setHasAssemblingVideo(self, value):
        self._setBool(3, value)
        return

    def getMaxPoint(self):
        return self._getNumber(4)

    def setMaxPoint(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(DetailModel, self)._initialize()
        self._addStringProperty(b'status')
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'earnedPoint', 0)
        self._addBoolProperty(b'hasAssemblingVideo', False)
        self._addNumberProperty(b'maxPoint', 0)
        return
