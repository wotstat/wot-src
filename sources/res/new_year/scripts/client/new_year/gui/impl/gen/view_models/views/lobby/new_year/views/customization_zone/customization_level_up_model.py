from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.customization_zone.customization_zone_model import CustomizationZoneModel

class CustomizationLevelUpModel(CustomizationZoneModel):
    __slots__ = (b'onLevelUp', b'onClose')

    def __init__(self, properties=11, commands=2):
        super(CustomizationLevelUpModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(CustomizationLevelUpModel, self)._initialize()
        self.onLevelUp = self._addCommand(b'onLevelUp')
        self.onClose = self._addCommand(b'onClose')
        return
