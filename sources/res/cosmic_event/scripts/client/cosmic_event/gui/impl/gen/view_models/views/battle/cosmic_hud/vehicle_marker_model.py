from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.marker_model import MarkerModel

class VehicleMarkerModel(MarkerModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(VehicleMarkerModel, self).__init__(properties=properties, commands=commands)
        return

    def getPlayerName(self):
        return self._getString(5)

    def setPlayerName(self, value):
        self._setString(5, value)
        return

    def getIsLootResearching(self):
        return self._getBool(6)

    def setIsLootResearching(self, value):
        self._setBool(6, value)
        return

    def getLootTimer(self):
        return self._getNumber(7)

    def setLootTimer(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(VehicleMarkerModel, self)._initialize()
        self._addStringProperty(b'playerName', b'')
        self._addBoolProperty(b'isLootResearching', False)
        self._addNumberProperty(b'lootTimer', 0)
        return
