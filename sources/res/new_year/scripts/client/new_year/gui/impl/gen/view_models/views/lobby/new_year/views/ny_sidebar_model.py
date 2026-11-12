from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_sidebar_common_model import NySidebarCommonModel

class NySidebarModel(NySidebarCommonModel):
    __slots__ = (b'onSideBarBtnClick',)
    VIEW_NAME_CITY = b'city'
    VIEW_NAME_REWARDS = b'rewards'
    VIEW_NAME_COLLECTIONS = b'collections'

    def __init__(self, properties=3, commands=1):
        super(NySidebarModel, self).__init__(properties=properties, commands=commands)
        return

    def getViewName(self):
        return self._getString(2)

    def setViewName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(NySidebarModel, self)._initialize()
        self._addStringProperty(b'viewName', b'')
        self.onSideBarBtnClick = self._addCommand(b'onSideBarBtnClick')
        return
