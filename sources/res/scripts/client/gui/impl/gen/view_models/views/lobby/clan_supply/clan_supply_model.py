from enum import IntEnum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.progression_model import ProgressionModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quests_model import QuestsModel
from gui.impl.gen.view_models.views.lobby.clan_supply.sidebar_model import SidebarModel

class ClanSupplyViews(IntEnum):
    PROGRESSION = 0
    QUESTS = 1


class ClanSupplyModel(ViewModel):
    __slots__ = (b'onClose', b'onInfoPageOpen')

    def __init__(self, properties=5, commands=2):
        super(ClanSupplyModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def sidebar(self):
        return self._getViewModel(0)

    @staticmethod
    def getSidebarType():
        return SidebarModel

    @property
    def progressionModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getProgressionModelType():
        return ProgressionModel

    @property
    def questsModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getQuestsModelType():
        return QuestsModel

    def getPageViewId(self):
        return ClanSupplyViews(self._getNumber(3))

    def setPageViewId(self, value):
        self._setNumber(3, value.value)
        return

    def getCurrencyValue(self):
        return self._getNumber(4)

    def setCurrencyValue(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ClanSupplyModel, self)._initialize()
        self._addViewModelProperty(b'sidebar', SidebarModel())
        self._addViewModelProperty(b'progressionModel', ProgressionModel())
        self._addViewModelProperty(b'questsModel', QuestsModel())
        self._addNumberProperty(b'pageViewId')
        self._addNumberProperty(b'currencyValue', 0)
        self.onClose = self._addCommand(b'onClose')
        self.onInfoPageOpen = self._addCommand(b'onInfoPageOpen')
        return
