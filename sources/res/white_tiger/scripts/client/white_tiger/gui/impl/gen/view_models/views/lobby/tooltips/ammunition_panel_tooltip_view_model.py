from frameworks.wulf import ViewModel
from gui.impl.gen import R

class AmmunitionPanelTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(AmmunitionPanelTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)
        return

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def getAnimation(self):
        return self._getString(3)

    def setAnimation(self, value):
        self._setString(3, value)
        return

    def getSubtitle(self):
        return self._getString(4)

    def setSubtitle(self, value):
        self._setString(4, value)
        return

    def getText(self):
        return self._getString(5)

    def setText(self, value):
        self._setString(5, value)
        return

    def getAdditionalInfoText(self):
        return self._getString(6)

    def setAdditionalInfoText(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(AmmunitionPanelTooltipViewModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'animation', b'')
        self._addStringProperty(b'subtitle', b'')
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'additionalInfoText', b'')
        return
