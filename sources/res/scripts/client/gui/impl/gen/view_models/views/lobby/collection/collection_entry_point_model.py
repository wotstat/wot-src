from enum import Enum
from frameworks.wulf import ViewModel

class CollectionState(Enum):
    COMPLETED = b'completed'
    DISABLED = b'disabled'
    ACTIVE = b'active'


class CollectionEntryPointModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(CollectionEntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return CollectionState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getNewReceivedItems(self):
        return self._getNumber(1)

    def setNewReceivedItems(self, value):
        self._setNumber(1, value)
        return

    def getFinishDateStamp(self):
        return self._getNumber(2)

    def setFinishDateStamp(self, value):
        self._setNumber(2, value)
        return

    def getCollectionName(self):
        return self._getString(3)

    def setCollectionName(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(CollectionEntryPointModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'newReceivedItems', 0)
        self._addNumberProperty(b'finishDateStamp', 0)
        self._addStringProperty(b'collectionName', b'')
        self.onClick = self._addCommand(b'onClick')
        return
