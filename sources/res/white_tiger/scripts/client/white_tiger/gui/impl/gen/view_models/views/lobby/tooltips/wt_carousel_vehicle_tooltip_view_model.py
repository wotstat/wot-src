from gui.impl.gen import R
from frameworks.wulf import ViewModel

class WtCarouselVehicleTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(WtCarouselVehicleTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getSubtitle(self):
        return self._getString(1)

    def setSubtitle(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def getWtVehicleType(self):
        return self._getString(4)

    def setWtVehicleType(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(WtCarouselVehicleTooltipViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'subtitle', b'')
        self._addStringProperty(b'description', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'wtVehicleType', b'boss')
        return
