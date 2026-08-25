from frameworks.wulf import ViewModel

class TabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TabModel, self).__init__(properties=properties, commands=commands)
        return

    def getCollectionName(self):
        return self._getString(0)

    def setCollectionName(self, value):
        self._setString(0, value)
        return

    def getHasNewItems(self):
        return self._getBool(1)

    def setHasNewItems(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(TabModel, self)._initialize()
        self._addStringProperty(b'collectionName', b'')
        self._addBoolProperty(b'hasNewItems', False)
        return
