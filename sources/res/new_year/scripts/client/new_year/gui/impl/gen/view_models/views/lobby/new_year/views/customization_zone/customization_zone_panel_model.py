from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.customization_zone.customization_zone_model import CustomizationZoneModel

class CustomizationZonePanelModel(ViewModel):
    __slots__ = (b'onClick', b'onNextLevel')

    def __init__(self, properties=1, commands=2):
        super(CustomizationZonePanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getCustomizationZones(self):
        return self._getArray(0)

    def setCustomizationZones(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCustomizationZonesType():
        return CustomizationZoneModel

    def _initialize(self):
        super(CustomizationZonePanelModel, self)._initialize()
        self._addArrayProperty(b'customizationZones', Array())
        self.onClick = self._addCommand(b'onClick')
        self.onNextLevel = self._addCommand(b'onNextLevel')
        return
