from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.tooltips.portal_shell_stat import PortalShellStat

class ShellTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ShellTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(0)

    def setName(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return self._getString(1)

    def setType(self, value):
        self._setString(1, value)
        return

    def getCaliber(self):
        return self._getNumber(2)

    def setCaliber(self, value):
        self._setNumber(2, value)
        return

    def getStats(self):
        return self._getArray(3)

    def setStats(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getStatsType():
        return PortalShellStat

    def _initialize(self):
        super(ShellTooltipModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'caliber', 0)
        self._addArrayProperty(b'stats', Array())
        return
