from enum import IntEnum
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.ny_currency_panel_model import NyCurrencyPanelModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.city.ny_city_view_model import NyCityViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_leaderboard_model import NyLeaderboardModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.new_year_info_view_model import NewYearInfoViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_back_button_model import NyBackButtonModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_main_menu_model import NyMainMenuModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_progress_widget_model import NyProgressWidgetModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.ny_sidebar_model import NySidebarModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_model import NyPetModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.quests.ny_quests_view_model import NyQuestsViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.surprise_machine.ny_surprise_machine_model import NySurpriseMachineModel

class MainViews(IntEnum):
    CITY = 0
    PET = 1
    LEADERS = 2
    MACHINE = 3
    QUESTS = 4
    INFO = 5


class SwitchStates(IntEnum):
    DONE = 0
    DEFAULT = 1
    TO_GLADE_WITH_INTRO = 2
    WITH_SWITCHING_OBJS = 3


class MainViewModel(ViewModel):
    __slots__ = (b'onClose', b'onFadeInDone', b'onMouseOver3dScene', b'onMoveSpace', b'onRewardInfo')

    def __init__(self, properties=15, commands=5):
        super(MainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def backButton(self):
        return self._getViewModel(0)

    @staticmethod
    def getBackButtonType():
        return NyBackButtonModel

    @property
    def mainMenu(self):
        return self._getViewModel(1)

    @staticmethod
    def getMainMenuType():
        return NyMainMenuModel

    @property
    def sidebar(self):
        return self._getViewModel(2)

    @staticmethod
    def getSidebarType():
        return NySidebarModel

    @property
    def currencyPanel(self):
        return self._getViewModel(3)

    @staticmethod
    def getCurrencyPanelType():
        return NyCurrencyPanelModel

    @property
    def progressWidgetModel(self):
        return self._getViewModel(4)

    @staticmethod
    def getProgressWidgetModelType():
        return NyProgressWidgetModel

    @property
    def cityModel(self):
        return self._getViewModel(5)

    @staticmethod
    def getCityModelType():
        return NyCityViewModel

    @property
    def surpriseMachineModel(self):
        return self._getViewModel(6)

    @staticmethod
    def getSurpriseMachineModelType():
        return NySurpriseMachineModel

    @property
    def petModel(self):
        return self._getViewModel(7)

    @staticmethod
    def getPetModelType():
        return NyPetModel

    @property
    def infoModel(self):
        return self._getViewModel(8)

    @staticmethod
    def getInfoModelType():
        return NewYearInfoViewModel

    @property
    def leaderboardModel(self):
        return self._getViewModel(9)

    @staticmethod
    def getLeaderboardModelType():
        return NyLeaderboardModel

    @property
    def questsModel(self):
        return self._getViewModel(10)

    @staticmethod
    def getQuestsModelType():
        return NyQuestsViewModel

    def getViewType(self):
        return MainViews(self._getNumber(11))

    def setViewType(self, value):
        self._setNumber(11, value.value)
        return

    def getSwitchState(self):
        return SwitchStates(self._getNumber(12))

    def setSwitchState(self, value):
        self._setNumber(12, value.value)
        return

    def getIsAnimatedShow(self):
        return self._getBool(13)

    def setIsAnimatedShow(self, value):
        self._setBool(13, value)
        return

    def getIsControlsLocked(self):
        return self._getBool(14)

    def setIsControlsLocked(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(MainViewModel, self)._initialize()
        self._addViewModelProperty(b'backButton', NyBackButtonModel())
        self._addViewModelProperty(b'mainMenu', NyMainMenuModel())
        self._addViewModelProperty(b'sidebar', NySidebarModel())
        self._addViewModelProperty(b'currencyPanel', NyCurrencyPanelModel())
        self._addViewModelProperty(b'progressWidgetModel', NyProgressWidgetModel())
        self._addViewModelProperty(b'cityModel', NyCityViewModel())
        self._addViewModelProperty(b'surpriseMachineModel', NySurpriseMachineModel())
        self._addViewModelProperty(b'petModel', NyPetModel())
        self._addViewModelProperty(b'infoModel', NewYearInfoViewModel())
        self._addViewModelProperty(b'leaderboardModel', NyLeaderboardModel())
        self._addViewModelProperty(b'questsModel', NyQuestsViewModel())
        self._addNumberProperty(b'viewType')
        self._addNumberProperty(b'switchState')
        self._addBoolProperty(b'isAnimatedShow', True)
        self._addBoolProperty(b'isControlsLocked', False)
        self.onClose = self._addCommand(b'onClose')
        self.onFadeInDone = self._addCommand(b'onFadeInDone')
        self.onMouseOver3dScene = self._addCommand(b'onMouseOver3dScene')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onRewardInfo = self._addCommand(b'onRewardInfo')
        return
