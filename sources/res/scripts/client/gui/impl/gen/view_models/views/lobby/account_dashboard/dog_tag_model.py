from frameworks.wulf import ViewModel

class DogTagModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=6, commands=1):
        super(DogTagModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsSelected(self):
        return self._getBool(0)

    def setIsSelected(self, value):
        self._setBool(0, value)
        return

    def getIsHighlighted(self):
        return self._getBool(1)

    def setIsHighlighted(self, value):
        self._setBool(1, value)
        return

    def getBackground(self):
        return self._getString(2)

    def setBackground(self, value):
        self._setString(2, value)
        return

    def getEngraving(self):
        return self._getString(3)

    def setEngraving(self, value):
        self._setString(3, value)
        return

    def getCounter(self):
        return self._getNumber(4)

    def setCounter(self, value):
        self._setNumber(4, value)
        return

    def getIsEmptyCounter(self):
        return self._getBool(5)

    def setIsEmptyCounter(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(DogTagModel, self)._initialize()
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isHighlighted', False)
        self._addStringProperty(b'background', b'')
        self._addStringProperty(b'engraving', b'')
        self._addNumberProperty(b'counter', -1)
        self._addBoolProperty(b'isEmptyCounter', False)
        self.onClick = self._addCommand(b'onClick')
        return
