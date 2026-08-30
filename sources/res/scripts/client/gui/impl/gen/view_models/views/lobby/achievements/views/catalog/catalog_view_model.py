from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.achievement_card_model import AchievementCardModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.breadcrumb_model import BreadcrumbModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.details_model import DetailsModel

class CatalogViewModel(ViewModel):
    __slots__ = (b'onClose', b'onBreadcrumbClick', b'onCatalogClick', b'onCardClick', b'onStylePreview', b'onDogTagPreview', b'onPurchaseVehicleClick', b'onHintClose', b'onCardHover')

    def __init__(self, properties=6, commands=9):
        super(CatalogViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def details(self):
        return self._getViewModel(0)

    @staticmethod
    def getDetailsType():
        return DetailsModel

    def getBreadcrumbs(self):
        return self._getArray(1)

    def setBreadcrumbs(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getBreadcrumbsType():
        return BreadcrumbModel

    def getAchievementScore(self):
        return self._getNumber(2)

    def setAchievementScore(self, value):
        self._setNumber(2, value)
        return

    def getMaxAchievementsScore(self):
        return self._getNumber(3)

    def setMaxAchievementsScore(self, value):
        self._setNumber(3, value)
        return

    def getIsNeededShowHint(self):
        return self._getBool(4)

    def setIsNeededShowHint(self, value):
        self._setBool(4, value)
        return

    def getAchievementsList(self):
        return self._getArray(5)

    def setAchievementsList(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getAchievementsListType():
        return AchievementCardModel

    def _initialize(self):
        super(CatalogViewModel, self)._initialize()
        self._addViewModelProperty(b'details', DetailsModel())
        self._addArrayProperty(b'breadcrumbs', Array())
        self._addNumberProperty(b'achievementScore', 0)
        self._addNumberProperty(b'maxAchievementsScore', 0)
        self._addBoolProperty(b'isNeededShowHint', False)
        self._addArrayProperty(b'achievementsList', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onBreadcrumbClick = self._addCommand(b'onBreadcrumbClick')
        self.onCatalogClick = self._addCommand(b'onCatalogClick')
        self.onCardClick = self._addCommand(b'onCardClick')
        self.onStylePreview = self._addCommand(b'onStylePreview')
        self.onDogTagPreview = self._addCommand(b'onDogTagPreview')
        self.onPurchaseVehicleClick = self._addCommand(b'onPurchaseVehicleClick')
        self.onHintClose = self._addCommand(b'onHintClose')
        self.onCardHover = self._addCommand(b'onCardHover')
        return
