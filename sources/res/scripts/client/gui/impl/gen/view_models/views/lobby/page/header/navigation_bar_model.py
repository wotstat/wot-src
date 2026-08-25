from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.page.header.navigation_bar_info_button import NavigationBarInfoButton

class NavigationBarModel(ViewModel):
    __slots__ = (b'onNavigate', b'onInfoAction')
    BACK_NAVIGATION = b'back'
    GARAGE_NAVIGATION = b'garage'

    def __init__(self, properties=4, commands=2):
        super(NavigationBarModel, self).__init__(properties=properties, commands=commands)
        return

    def getPageTitle(self):
        return self._getString(0)

    def setPageTitle(self, value):
        self._setString(0, value)
        return

    def getBackNavigationDescription(self):
        return self._getString(1)

    def setBackNavigationDescription(self, value):
        self._setString(1, value)
        return

    def getBackNavigationAllowed(self):
        return self._getBool(2)

    def setBackNavigationAllowed(self, value):
        self._setBool(2, value)
        return

    def getInfoButtons(self):
        return self._getArray(3)

    def setInfoButtons(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getInfoButtonsType():
        return NavigationBarInfoButton

    def _initialize(self):
        super(NavigationBarModel, self)._initialize()
        self._addStringProperty(b'pageTitle', b'')
        self._addStringProperty(b'backNavigationDescription', b'')
        self._addBoolProperty(b'backNavigationAllowed', False)
        self._addArrayProperty(b'infoButtons', Array())
        self.onNavigate = self._addCommand(b'onNavigate')
        self.onInfoAction = self._addCommand(b'onInfoAction')
        return
