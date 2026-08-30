from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NationChangeTankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(NationChangeTankmanModel, self).__init__(properties=properties, commands=commands)
        return

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)
        return

    def getInvID(self):
        return self._getNumber(1)

    def setInvID(self, value):
        self._setNumber(1, value)
        return

    def getIsSimpleTooltip(self):
        return self._getBool(2)

    def setIsSimpleTooltip(self, value):
        self._setBool(2, value)
        return

    def getSimpleTooltipHeader(self):
        return self._getString(3)

    def setSimpleTooltipHeader(self, value):
        self._setString(3, value)
        return

    def getSimpleTooltipBody(self):
        return self._getString(4)

    def setSimpleTooltipBody(self, value):
        self._setString(4, value)
        return

    def getIsDog(self):
        return self._getBool(5)

    def setIsDog(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(NationChangeTankmanModel, self)._initialize()
        self._addResourceProperty(b'image', R.invalid())
        self._addNumberProperty(b'invID', 0)
        self._addBoolProperty(b'isSimpleTooltip', False)
        self._addStringProperty(b'simpleTooltipHeader', b'')
        self._addStringProperty(b'simpleTooltipBody', b'')
        self._addBoolProperty(b'isDog', False)
        return
