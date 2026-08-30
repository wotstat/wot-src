from frameworks.wulf import ViewModel

class CollectionItemTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CollectionItemTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getIsReceived(self):
        return self._getBool(2)

    def setIsReceived(self, value):
        self._setBool(2, value)
        return

    def getImagePath(self):
        return self._getString(3)

    def setImagePath(self, value):
        self._setString(3, value)
        return

    def getIsDetailed(self):
        return self._getBool(4)

    def setIsDetailed(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(CollectionItemTooltipViewModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'isReceived', False)
        self._addStringProperty(b'imagePath', b'')
        self._addBoolProperty(b'isDetailed', False)
        return
