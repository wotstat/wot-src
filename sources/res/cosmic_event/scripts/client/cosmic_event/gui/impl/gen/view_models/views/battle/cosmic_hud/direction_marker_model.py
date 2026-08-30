from enum import Enum
from cosmic_event.gui.impl.gen.view_models.views.battle.cosmic_hud.marker_model import MarkerModel

class DirectionMarkerType(Enum):
    CORAL = b'coral'
    ARTIFACT_ZONE = b'artifactZone'


class DirectionMarkerModel(MarkerModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(DirectionMarkerModel, self).__init__(properties=properties, commands=commands)
        return

    def getDistance(self):
        return self._getNumber(5)

    def setDistance(self, value):
        self._setNumber(5, value)
        return

    def getAngle(self):
        return self._getReal(6)

    def setAngle(self, value):
        self._setReal(6, value)
        return

    def getMarkerVisibility(self):
        return self._getBool(7)

    def setMarkerVisibility(self, value):
        self._setBool(7, value)
        return

    def getMarkerType(self):
        return DirectionMarkerType(self._getString(8))

    def setMarkerType(self, value):
        self._setString(8, value.value)
        return

    def getMarkerTimer(self):
        return self._getNumber(9)

    def setMarkerTimer(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(DirectionMarkerModel, self)._initialize()
        self._addNumberProperty(b'distance', 0)
        self._addRealProperty(b'angle', 0.0)
        self._addBoolProperty(b'markerVisibility', False)
        self._addStringProperty(b'markerType')
        self._addNumberProperty(b'markerTimer', 0)
        return
