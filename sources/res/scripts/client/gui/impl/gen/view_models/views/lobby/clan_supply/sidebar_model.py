from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.clan_supply.tab_model import TabModel

class SidebarModel(ViewModel):
    __slots__ = (b'onSideBarTabChange',)

    def __init__(self, properties=1, commands=1):
        super(SidebarModel, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getItemsType():
        return TabModel

    def _initialize(self):
        super(SidebarModel, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self.onSideBarTabChange = self._addCommand(b'onSideBarTabChange')
        return
