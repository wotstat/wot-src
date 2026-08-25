from enum import Enum
from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.yearly_rewards_card_model import YearlyRewardsCardModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_base_model import ProgressionItemBaseModel

class BannerState(Enum):
    DEFAULT = b'default'
    NOTACCRUEDREWARDS = b'notAccruedRewards'
    REWARDSSELECTIONAVAILABLE = b'rewardsSelectionAvailable'
    REWARDSRECEIVED = b'rewardsReceived'


class YearlyRewardsModel(ViewModel):
    __slots__ = (b'onGoToStylePreview', b'onGoToVehiclePreview', b'onGoToRewardsSelection', b'onIntroViewed')

    def __init__(self, properties=8, commands=4):
        super(YearlyRewardsModel, self).__init__(properties=properties, commands=commands)
        return

    def getCards(self):
        return self._getArray(0)

    def setCards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getCardsType():
        return YearlyRewardsCardModel

    def getBannerState(self):
        return BannerState(self._getString(1))

    def setBannerState(self, value):
        self._setString(1, value.value)
        return

    def getCurrentRank(self):
        return Rank(self._getNumber(2))

    def setCurrentRank(self, value):
        self._setNumber(2, value.value)
        return

    def getIsQualificationActive(self):
        return self._getBool(3)

    def setIsQualificationActive(self, value):
        self._setBool(3, value)
        return

    def getHasDataError(self):
        return self._getBool(4)

    def setHasDataError(self, value):
        self._setBool(4, value)
        return

    def getWithIntro(self):
        return self._getBool(5)

    def setWithIntro(self, value):
        self._setBool(5, value)
        return

    def getRanks(self):
        return self._getArray(6)

    def setRanks(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRanksType():
        return ProgressionItemBaseModel

    def getTopPercentage(self):
        return self._getNumber(7)

    def setTopPercentage(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(YearlyRewardsModel, self)._initialize()
        self._addArrayProperty(b'cards', Array())
        self._addStringProperty(b'bannerState')
        self._addNumberProperty(b'currentRank')
        self._addBoolProperty(b'isQualificationActive', False)
        self._addBoolProperty(b'hasDataError', False)
        self._addBoolProperty(b'withIntro', True)
        self._addArrayProperty(b'ranks', Array())
        self._addNumberProperty(b'topPercentage', 0)
        self.onGoToStylePreview = self._addCommand(b'onGoToStylePreview')
        self.onGoToVehiclePreview = self._addCommand(b'onGoToVehiclePreview')
        self.onGoToRewardsSelection = self._addCommand(b'onGoToRewardsSelection')
        self.onIntroViewed = self._addCommand(b'onIntroViewed')
        return
