from frameworks.wulf import ViewModel

class TankmanTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(TankmanTooltipViewModel, self).__init__(properties=properties, commands=commands)
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

    def getMainIcon(self):
        return self._getString(2)

    def setMainIcon(self, value):
        self._setString(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getIconsTitle(self):
        return self._getString(4)

    def setIconsTitle(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(TankmanTooltipViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'subtitle', b'')
        self._addStringProperty(b'mainIcon', b'')
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'iconsTitle', b'')
        return
