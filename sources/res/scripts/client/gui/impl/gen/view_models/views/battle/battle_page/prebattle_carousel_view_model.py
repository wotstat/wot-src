from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.battle.battle_page.prebattle_vehicle_model import PrebattleVehicleModel

class PrebattleCarouselViewModel(ViewModel):
    __slots__ = (b'onVehicleClick', b'onVehicleSelect', b'onApplyFavoritesFilter', b'onApplyRentedFilter', b'onClearFilters', b'onSetDualRow')

    def __init__(self, properties=6, commands=6):
        super(PrebattleCarouselViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def vehicles(self):
        return self._getViewModel(0)

    @staticmethod
    def getVehiclesType():
        return PrebattleVehicleModel

    def getIsLoading(self):
        return self._getBool(1)

    def setIsLoading(self, value):
        self._setBool(1, value)
        return

    def getRentedFilter(self):
        return self._getBool(2)

    def setRentedFilter(self, value):
        self._setBool(2, value)
        return

    def getFavoritesFilter(self):
        return self._getBool(3)

    def setFavoritesFilter(self, value):
        self._setBool(3, value)
        return

    def getIsDualRow(self):
        return self._getBool(4)

    def setIsDualRow(self, value):
        self._setBool(4, value)
        return

    def getIsPopoverOpen(self):
        return self._getBool(5)

    def setIsPopoverOpen(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(PrebattleCarouselViewModel, self)._initialize()
        self._addViewModelProperty(b'vehicles', UserListModel())
        self._addBoolProperty(b'isLoading', False)
        self._addBoolProperty(b'rentedFilter', False)
        self._addBoolProperty(b'favoritesFilter', False)
        self._addBoolProperty(b'isDualRow', False)
        self._addBoolProperty(b'isPopoverOpen', False)
        self.onVehicleClick = self._addCommand(b'onVehicleClick')
        self.onVehicleSelect = self._addCommand(b'onVehicleSelect')
        self.onApplyFavoritesFilter = self._addCommand(b'onApplyFavoritesFilter')
        self.onApplyRentedFilter = self._addCommand(b'onApplyRentedFilter')
        self.onClearFilters = self._addCommand(b'onClearFilters')
        self.onSetDualRow = self._addCommand(b'onSetDualRow')
        return
