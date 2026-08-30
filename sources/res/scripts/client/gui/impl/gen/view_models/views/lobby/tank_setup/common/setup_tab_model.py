from frameworks.wulf import ViewModel

class SetupTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SetupTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getNewItemsCount(self):
        return self._getNumber(1)

    def setNewItemsCount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(SetupTabModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'newItemsCount', 0)
        return
