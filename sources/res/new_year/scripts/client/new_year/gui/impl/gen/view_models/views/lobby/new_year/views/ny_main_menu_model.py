from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.new_year_main_widget_model import NewYearMainWidgetModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.ny_main_menu_tab_model import NyMainMenuTabModel

class NyMainMenuModel(ViewModel):
    __slots__ = (b'onSwitchContent',)

    def __init__(self, properties=7, commands=1):
        super(NyMainMenuModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def widget(self):
        return self._getViewModel(0)

    @staticmethod
    def getWidgetType():
        return NewYearMainWidgetModel

    def getItemsMenu(self):
        return self._getArray(1)

    def setItemsMenu(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getItemsMenuType():
        return NyMainMenuTabModel

    def getStartIndexMenu(self):
        return self._getNumber(2)

    def setStartIndexMenu(self, value):
        self._setNumber(2, value)
        return

    def getIsExtendedAnim(self):
        return self._getBool(3)

    def setIsExtendedAnim(self, value):
        self._setBool(3, value)
        return

    def getIsOnboardingUnlock(self):
        return self._getBool(4)

    def setIsOnboardingUnlock(self, value):
        self._setBool(4, value)
        return

    def getIsPetOnboarding(self):
        return self._getBool(5)

    def setIsPetOnboarding(self, value):
        self._setBool(5, value)
        return

    def getWasLeaderboardFinished(self):
        return self._getBool(6)

    def setWasLeaderboardFinished(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(NyMainMenuModel, self)._initialize()
        self._addViewModelProperty(b'widget', NewYearMainWidgetModel())
        self._addArrayProperty(b'itemsMenu', Array())
        self._addNumberProperty(b'startIndexMenu', 0)
        self._addBoolProperty(b'isExtendedAnim', False)
        self._addBoolProperty(b'isOnboardingUnlock', True)
        self._addBoolProperty(b'isPetOnboarding', True)
        self._addBoolProperty(b'wasLeaderboardFinished', False)
        self.onSwitchContent = self._addCommand(b'onSwitchContent')
        return
