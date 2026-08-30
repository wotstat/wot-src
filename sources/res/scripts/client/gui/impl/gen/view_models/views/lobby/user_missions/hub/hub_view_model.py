from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tab_model import TabModel

class HubViewModel(ViewModel):
    __slots__ = (b'onTabChange', b'onContentLayoutChanged')

    def __init__(self, properties=2, commands=2):
        super(HubViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentTabId(self):
        return self._getString(0)

    def setCurrentTabId(self, value):
        self._setString(0, value)
        return

    def getTabsList(self):
        return self._getArray(1)

    def setTabsList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getTabsListType():
        return TabModel

    def _initialize(self):
        super(HubViewModel, self)._initialize()
        self._addStringProperty(b'currentTabId', b'')
        self._addArrayProperty(b'tabsList', Array())
        self.onTabChange = self._addCommand(b'onTabChange')
        self.onContentLayoutChanged = self._addCommand(b'onContentLayoutChanged')
        return
