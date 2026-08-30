from gui.impl.gen import R
from frameworks.wulf import ViewModel

class WtEquipmentSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(WtEquipmentSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)
        return

    def getId(self):
        return self._getNumber(1)

    def setId(self, value):
        self._setNumber(1, value)
        return

    def getTooltipId(self):
        return self._getString(2)

    def setTooltipId(self, value):
        self._setString(2, value)
        return

    def getInfiniteIcon(self):
        return self._getResource(3)

    def setInfiniteIcon(self, value):
        self._setResource(3, value)
        return

    def _initialize(self):
        super(WtEquipmentSlotModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'tooltipId', b'')
        self._addResourceProperty(b'infiniteIcon', R.invalid())
        return
