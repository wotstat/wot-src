from frameworks.wulf import ViewModel

class CollectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(CollectionModel, self).__init__(properties=properties, commands=commands)
        return

    def getCollectionId(self):
        return self._getNumber(0)

    def setCollectionId(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)
        return

    def getIsNew(self):
        return self._getBool(3)

    def setIsNew(self, value):
        self._setBool(3, value)
        return

    def getCompletionWasShown(self):
        return self._getBool(4)

    def setCompletionWasShown(self, value):
        self._setBool(4, value)
        return

    def getItemCount(self):
        return self._getNumber(5)

    def setItemCount(self, value):
        self._setNumber(5, value)
        return

    def getMaxCount(self):
        return self._getNumber(6)

    def setMaxCount(self, value):
        self._setNumber(6, value)
        return

    def getYear(self):
        return self._getNumber(7)

    def setYear(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(CollectionModel, self)._initialize()
        self._addNumberProperty(b'collectionId', 0)
        self._addStringProperty(b'name', b'')
        self._addBoolProperty(b'isActive', False)
        self._addBoolProperty(b'isNew', False)
        self._addBoolProperty(b'completionWasShown', False)
        self._addNumberProperty(b'itemCount', 0)
        self._addNumberProperty(b'maxCount', 0)
        self._addNumberProperty(b'year', 0)
        return
