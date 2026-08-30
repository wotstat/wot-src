from frameworks.wulf import ViewModel

class DeconstructFromInventoryTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(DeconstructFromInventoryTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getEquipmentName(self):
        return self._getString(0)

    def setEquipmentName(self, value):
        self._setString(0, value)
        return

    def getEquipmentAmount(self):
        return self._getNumber(1)

    def setEquipmentAmount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(DeconstructFromInventoryTooltipModel, self)._initialize()
        self._addStringProperty(b'equipmentName', b'')
        self._addNumberProperty(b'equipmentAmount', 0)
        return
