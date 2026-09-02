from frameworks.wulf import ViewModel

class SelectableRewardItemModel(ViewModel):
    __slots__ = ()
    STATE_NORMAL = b'state_normal'
    STATE_LIMITED = b'state_limited'
    STATE_RECEIVED = b'state_received'

    def __init__(self, properties=6, commands=0):
        super(SelectableRewardItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)
        return

    def getStorageCount(self):
        return self._getNumber(2)

    def setStorageCount(self, value):
        self._setNumber(2, value)
        return

    def getPackSize(self):
        return self._getNumber(3)

    def setPackSize(self, value):
        self._setNumber(3, value)
        return

    def getState(self):
        return self._getString(4)

    def setState(self, value):
        self._setString(4, value)
        return

    def getDecorator(self):
        return self._getString(5)

    def setDecorator(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(SelectableRewardItemModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'storageCount', 0)
        self._addNumberProperty(b'packSize', 1)
        self._addStringProperty(b'state', b'state_normal')
        self._addStringProperty(b'decorator', b'')
        return
