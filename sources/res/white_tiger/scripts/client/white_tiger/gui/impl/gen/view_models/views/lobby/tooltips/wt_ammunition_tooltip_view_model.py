from frameworks.wulf import ViewModel

class WtAmmunitionTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(WtAmmunitionTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconName(self):
        return self._getString(0)

    def setIconName(self, value):
        self._setString(0, value)
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

    def getSubtitle(self):
        return self._getString(3)

    def setSubtitle(self, value):
        self._setString(3, value)
        return

    def getText(self):
        return self._getString(4)

    def setText(self, value):
        self._setString(4, value)
        return

    def getAdditionalInfoText(self):
        return self._getString(5)

    def setAdditionalInfoText(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(WtAmmunitionTooltipViewModel, self)._initialize()
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'subtitle', b'')
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'additionalInfoText', b'')
        return
