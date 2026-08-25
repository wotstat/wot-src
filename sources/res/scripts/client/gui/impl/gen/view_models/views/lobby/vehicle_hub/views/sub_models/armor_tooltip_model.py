from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.armor_layer_model import ArmorLayerModel

class ArmorTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ArmorTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getArmorLayers(self):
        return self._getArray(0)

    def setArmorLayers(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getArmorLayersType():
        return ArmorLayerModel

    def getSelectedMode(self):
        return self._getString(1)

    def setSelectedMode(self, value):
        self._setString(1, value)
        return

    def getDccType(self):
        return self._getString(2)

    def setDccType(self, value):
        self._setString(2, value)
        return

    def getDccValue(self):
        return self._getNumber(3)

    def setDccValue(self, value):
        self._setNumber(3, value)
        return

    def getDccColor(self):
        return self._getString(4)

    def setDccColor(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(ArmorTooltipModel, self)._initialize()
        self._addArrayProperty(b'armorLayers', Array())
        self._addStringProperty(b'selectedMode', b'')
        self._addStringProperty(b'dccType', b'')
        self._addNumberProperty(b'dccValue', 0)
        self._addStringProperty(b'dccColor', b'')
        return
