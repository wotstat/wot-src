from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.setup_tab_model import SetupTabModel

class SetupTabsModel(ViewModel):
    __slots__ = (b'onTabChanged',)

    def __init__(self, properties=2, commands=1):
        super(SetupTabsModel, self).__init__(properties=properties, commands=commands)
        return

    def getTabs(self):
        return self._getArray(0)

    def setTabs(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getTabsType():
        return SetupTabModel

    def getSelectedTabName(self):
        return self._getString(1)

    def setSelectedTabName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(SetupTabsModel, self)._initialize()
        self._addArrayProperty(b'tabs', Array())
        self._addStringProperty(b'selectedTabName', b'')
        self.onTabChanged = self._addCommand(b'onTabChanged')
        return
