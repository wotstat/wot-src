from frameworks.wulf import ViewModel

class SelectableRewardTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SelectableRewardTabModel, self).__init__(properties=properties, commands=commands)
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

    def getLimit(self):
        return self._getNumber(2)

    def setLimit(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(SelectableRewardTabModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'limit', 0)
        return
