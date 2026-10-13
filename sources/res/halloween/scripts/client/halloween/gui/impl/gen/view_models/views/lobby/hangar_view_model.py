from halloween.gui.impl.gen.view_models.views.lobby.bestiary_model import BestiaryModel
from halloween.gui.impl.gen.view_models.views.lobby.vehicle_title_view_model import VehicleTitleViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class HangarViewModel(RouterModel):
    __slots__ = (b'onAboutClick', b'onSlide', b'onPreview', b'onWidgetsUpdate', b'onTasksClick', b'onPacksClick', b'onComparisonClick', b'onAnomaliesClick', b'onViewLoaded', b'onEnemyClick', b'onBestiaryClick')

    def __init__(self, properties=15, commands=13):
        super(HangarViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainGiftVehicle(self):
        return self._getViewModel(2)

    @staticmethod
    def getMainGiftVehicleType():
        return VehicleTitleViewModel

    @property
    def bestiaryInfo(self):
        return self._getViewModel(3)

    @staticmethod
    def getBestiaryInfoType():
        return BestiaryModel

    def getSelectedSlide(self):
        return self._getNumber(4)

    def setSelectedSlide(self, value):
        self._setNumber(4, value)
        return

    def getScrollToSlide(self):
        return self._getNumber(5)

    def setScrollToSlide(self, value):
        self._setNumber(5, value)
        return

    def getSlidesCount(self):
        return self._getNumber(6)

    def setSlidesCount(self, value):
        self._setNumber(6, value)
        return

    def getIsVehicleLocked(self):
        return self._getBool(7)

    def setIsVehicleLocked(self, value):
        self._setBool(7, value)
        return

    def getLockedMissionIndex(self):
        return self._getNumber(8)

    def setLockedMissionIndex(self, value):
        self._setNumber(8, value)
        return

    def getIsVehicleInBattle(self):
        return self._getBool(9)

    def setIsVehicleInBattle(self, value):
        self._setBool(9, value)
        return

    def getIsCompleted(self):
        return self._getBool(10)

    def setIsCompleted(self, value):
        self._setBool(10, value)
        return

    def getIsOpened(self):
        return self._getBool(11)

    def setIsOpened(self, value):
        self._setBool(11, value)
        return

    def getIsInfoPageEnabled(self):
        return self._getBool(12)

    def setIsInfoPageEnabled(self, value):
        self._setBool(12, value)
        return

    def getAreAnomaliesUnlocked(self):
        return self._getBool(13)

    def setAreAnomaliesUnlocked(self, value):
        self._setBool(13, value)
        return

    def getHasNewAnomaly(self):
        return self._getBool(14)

    def setHasNewAnomaly(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(HangarViewModel, self)._initialize()
        self._addViewModelProperty(b'mainGiftVehicle', VehicleTitleViewModel())
        self._addViewModelProperty(b'bestiaryInfo', BestiaryModel())
        self._addNumberProperty(b'selectedSlide', 0)
        self._addNumberProperty(b'scrollToSlide', 0)
        self._addNumberProperty(b'slidesCount', 0)
        self._addBoolProperty(b'isVehicleLocked', False)
        self._addNumberProperty(b'lockedMissionIndex', 0)
        self._addBoolProperty(b'isVehicleInBattle', False)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isOpened', False)
        self._addBoolProperty(b'isInfoPageEnabled', False)
        self._addBoolProperty(b'areAnomaliesUnlocked', False)
        self._addBoolProperty(b'hasNewAnomaly', False)
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onSlide = self._addCommand(b'onSlide')
        self.onPreview = self._addCommand(b'onPreview')
        self.onWidgetsUpdate = self._addCommand(b'onWidgetsUpdate')
        self.onTasksClick = self._addCommand(b'onTasksClick')
        self.onPacksClick = self._addCommand(b'onPacksClick')
        self.onComparisonClick = self._addCommand(b'onComparisonClick')
        self.onAnomaliesClick = self._addCommand(b'onAnomaliesClick')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onEnemyClick = self._addCommand(b'onEnemyClick')
        self.onBestiaryClick = self._addCommand(b'onBestiaryClick')
        return
