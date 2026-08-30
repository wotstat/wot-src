from gui.impl.gen.view_models.views.lobby.tank_setup.ammunition_panel_view_model import AmmunitionPanelViewModel

class VehicleCompareAmmunitionPanelModel(AmmunitionPanelViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=8, commands=2):
        super(VehicleCompareAmmunitionPanelModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(VehicleCompareAmmunitionPanelModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        return
