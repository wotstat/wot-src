from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_container_tab_model import FrontlineContainerTabModel

class FrontlineContainerViewModel(ViewModel):
    __slots__ = (b'onTabChange', b'onClose', b'onInfo')

    def __init__(self, properties=2, commands=3):
        super(FrontlineContainerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentTabId(self):
        return self._getNumber(0)

    def setCurrentTabId(self, value):
        self._setNumber(0, value)
        return

    def getTabs(self):
        return self._getArray(1)

    def setTabs(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getTabsType():
        return FrontlineContainerTabModel

    def _initialize(self):
        super(FrontlineContainerViewModel, self)._initialize()
        self._addNumberProperty(b'currentTabId', 0)
        self._addArrayProperty(b'tabs', Array())
        self.onTabChange = self._addCommand(b'onTabChange')
        self.onClose = self._addCommand(b'onClose')
        self.onInfo = self._addCommand(b'onInfo')
        return
