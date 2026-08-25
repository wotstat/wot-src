from frameworks.wulf import ViewModel

class CollectionEntryPointViewModel(ViewModel):
    __slots__ = (b'openCollection',)

    def __init__(self, properties=5, commands=1):
        super(CollectionEntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCollectionItemCount(self):
        return self._getNumber(0)

    def setCollectionItemCount(self, value):
        self._setNumber(0, value)
        return

    def getNewCollectionItemCount(self):
        return self._getNumber(1)

    def setNewCollectionItemCount(self, value):
        self._setNumber(1, value)
        return

    def getMaxCollectionItemCount(self):
        return self._getNumber(2)

    def setMaxCollectionItemCount(self, value):
        self._setNumber(2, value)
        return

    def getIsFirstEnter(self):
        return self._getBool(3)

    def setIsFirstEnter(self, value):
        self._setBool(3, value)
        return

    def getIsCollectionsEnabled(self):
        return self._getBool(4)

    def setIsCollectionsEnabled(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(CollectionEntryPointViewModel, self)._initialize()
        self._addNumberProperty(b'collectionItemCount', 0)
        self._addNumberProperty(b'newCollectionItemCount', 0)
        self._addNumberProperty(b'maxCollectionItemCount', 0)
        self._addBoolProperty(b'isFirstEnter', False)
        self._addBoolProperty(b'isCollectionsEnabled', False)
        self.openCollection = self._addCommand(b'openCollection')
        return
