from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.feature.fun_random_maps_modifier import FunRandomMapsModifier

class FunRandomMapsSelectedMapModel(ViewModel):
    __slots__ = ()
    MINIMAP_SIZE_DEFAULT = 570
    MINIMAP_SIZE_SMALL = 332

    def __init__(self, properties=5, commands=0):
        super(FunRandomMapsSelectedMapModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getImage(self):
        return self._getResource(2)

    def setImage(self, value):
        self._setResource(2, value)
        return

    def getModifiers(self):
        return self._getArray(3)

    def setModifiers(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getModifiersType():
        return FunRandomMapsModifier

    def getPoints(self):
        return self._getArray(4)

    def setPoints(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getPointsType():
        return FunRandomMapsModifier

    def _initialize(self):
        super(FunRandomMapsSelectedMapModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'title', b'')
        self._addResourceProperty(b'image', R.invalid())
        self._addArrayProperty(b'modifiers', Array())
        self._addArrayProperty(b'points', Array())
        return
