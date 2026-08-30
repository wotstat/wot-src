from frameworks.wulf import ViewModel

class DogTagModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(DogTagModel, self).__init__(properties=properties, commands=commands)
        return

    def getEngravingCompId(self):
        return self._getNumber(0)

    def setEngravingCompId(self, value):
        self._setNumber(0, value)
        return

    def getBackgroundCompId(self):
        return self._getNumber(1)

    def setBackgroundCompId(self, value):
        self._setNumber(1, value)
        return

    def getIsEnabled(self):
        return self._getBool(2)

    def setIsEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsHighlighted(self):
        return self._getBool(3)

    def setIsHighlighted(self, value):
        self._setBool(3, value)
        return

    def getBackground(self):
        return self._getString(4)

    def setBackground(self, value):
        self._setString(4, value)
        return

    def getEngraving(self):
        return self._getString(5)

    def setEngraving(self, value):
        self._setString(5, value)
        return

    def getPurpose(self):
        return self._getString(6)

    def setPurpose(self, value):
        self._setString(6, value)
        return

    def getAnimation(self):
        return self._getString(7)

    def setAnimation(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(DogTagModel, self)._initialize()
        self._addNumberProperty(b'engravingCompId', 0)
        self._addNumberProperty(b'backgroundCompId', 0)
        self._addBoolProperty(b'isEnabled', True)
        self._addBoolProperty(b'isHighlighted', False)
        self._addStringProperty(b'background', b'')
        self._addStringProperty(b'engraving', b'')
        self._addStringProperty(b'purpose', b'')
        self._addStringProperty(b'animation', b'')
        return
