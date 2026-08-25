from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.ammunition_panel_model import AmmunitionPanelModel

class ExtAmmoPanelView(AmmunitionPanelModel):
    __slots__ = (b'onSwitch',)

    def __init__(self, properties=6, commands=3):
        super(ExtAmmoPanelView, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ExtAmmoPanelView, self)._initialize()
        self.onSwitch = self._addCommand(b'onSwitch')
        return
