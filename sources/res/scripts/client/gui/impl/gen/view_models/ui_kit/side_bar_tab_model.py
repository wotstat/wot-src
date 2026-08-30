from frameworks.wulf import ViewModel

class SideBarTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(SideBarTabModel, self).__init__(properties=properties, commands=commands)
        return

    def getAlias(self):
        return self._getString(0)

    def setAlias(self, value):
        self._setString(0, value)
        return

    def getTooltipHeader(self):
        return self._getString(1)

    def setTooltipHeader(self, value):
        self._setString(1, value)
        return

    def getTooltipBody(self):
        return self._getString(2)

    def setTooltipBody(self, value):
        self._setString(2, value)
        return

    def getLinkage(self):
        return self._getString(3)

    def setLinkage(self, value):
        self._setString(3, value)
        return

    def getIcon(self):
        return self._getString(4)

    def setIcon(self, value):
        self._setString(4, value)
        return

    def getEnabled(self):
        return self._getBool(5)

    def setEnabled(self, value):
        self._setBool(5, value)
        return

    def getUnseenCount(self):
        return self._getNumber(6)

    def setUnseenCount(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(SideBarTabModel, self)._initialize()
        self._addStringProperty(b'alias', b'')
        self._addStringProperty(b'tooltipHeader', b'')
        self._addStringProperty(b'tooltipBody', b'')
        self._addStringProperty(b'linkage', b'')
        self._addStringProperty(b'icon', b'')
        self._addBoolProperty(b'enabled', True)
        self._addNumberProperty(b'unseenCount', 0)
        return
