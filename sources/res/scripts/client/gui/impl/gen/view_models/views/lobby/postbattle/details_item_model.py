from frameworks.wulf import ViewModel

class DetailsItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DetailsItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getBlockIdx(self):
        return self._getNumber(1)

    def setBlockIdx(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(DetailsItemModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'blockIdx', 0)
        return
