from gui.impl.gen.view_models.views.lobby.tank_setup.common.ammunition_items_section import AmmunitionItemsSection

class AmmunitionShellsSection(AmmunitionItemsSection):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(AmmunitionShellsSection, self).__init__(properties=properties, commands=commands)
        return

    def getInstalledCount(self):
        return self._getNumber(6)

    def setInstalledCount(self, value):
        self._setNumber(6, value)
        return

    def getMaxCount(self):
        return self._getNumber(7)

    def setMaxCount(self, value):
        self._setNumber(7, value)
        return

    def getIsWarning(self):
        return self._getBool(8)

    def setIsWarning(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(AmmunitionShellsSection, self)._initialize()
        self._addNumberProperty(b'installedCount', 0)
        self._addNumberProperty(b'maxCount', 0)
        self._addBoolProperty(b'isWarning', False)
        return
