from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.ammunition_panel_model import AmmunitionPanelModel

class ExtAmmoPanelView(AmmunitionPanelModel):
    __slots__ = (b'onSwitch',)

    def __init__(self, properties=8, commands=3):
        super(ExtAmmoPanelView, self).__init__(properties=properties, commands=commands)
        return

    def getAccelerationKeyName(self):
        return self._getString(6)

    def setAccelerationKeyName(self, value):
        self._setString(6, value)
        return

    def getAccelerationIntCD(self):
        return self._getNumber(7)

    def setAccelerationIntCD(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(ExtAmmoPanelView, self)._initialize()
        self._addStringProperty(b'accelerationKeyName', b'')
        self._addNumberProperty(b'accelerationIntCD', 0)
        self.onSwitch = self._addCommand(b'onSwitch')
        return
