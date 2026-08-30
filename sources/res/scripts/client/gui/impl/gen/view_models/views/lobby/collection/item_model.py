from enum import Enum
from frameworks.wulf import ViewModel

class ItemState(Enum):
    NEW = b'new'
    RECEIVED = b'received'
    UNRECEIVED = b'unreceived'


class ItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getItemId(self):
        return self._getNumber(0)

    def setItemId(self, value):
        self._setNumber(0, value)
        return

    def getState(self):
        return ItemState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getReceivedImagePath(self):
        return self._getString(2)

    def setReceivedImagePath(self, value):
        self._setString(2, value)
        return

    def getUnreceivedImagePath(self):
        return self._getString(3)

    def setUnreceivedImagePath(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(ItemModel, self)._initialize()
        self._addNumberProperty(b'itemId', 0)
        self._addStringProperty(b'state')
        self._addStringProperty(b'receivedImagePath', b'')
        self._addStringProperty(b'unreceivedImagePath', b'')
        return
