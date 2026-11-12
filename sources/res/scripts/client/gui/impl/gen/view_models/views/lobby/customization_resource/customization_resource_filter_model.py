from gui.impl.gen.view_models.views.lobby.customization.customization_filter_model import CustomizationFilterModel

class CustomizationResourceFilterModel(CustomizationFilterModel):
    __slots__ = ()

    def __init__(self, properties=27, commands=3):
        super(CustomizationResourceFilterModel, self).__init__(properties=properties, commands=commands)
        return

    def getInventory(self):
        return self._getBool(26)

    def setInventory(self, value):
        self._setBool(26, value)
        return

    def _initialize(self):
        super(CustomizationResourceFilterModel, self)._initialize()
        self._addBoolProperty(b'inventory', False)
        return
