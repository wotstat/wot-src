from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.rewards_info.ny_collections_rewards_model import NyCollectionsRewardsModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.rewards_info.ny_level_model import NyLevelModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.rewards_info.ny_levels_rewards_model import NyLevelsRewardsModel

class NyProgressViewModel(ViewModel):
    __slots__ = (b'onClose', b'onGotoStore', b'onSelectVehicleDiscount', b'onShowAnimationEnd')

    def __init__(self, properties=6, commands=4):
        super(NyProgressViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def levelsRewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getLevelsRewardsType():
        return NyLevelsRewardsModel

    @property
    def collectionsRewards(self):
        return self._getViewModel(1)

    @staticmethod
    def getCollectionsRewardsType():
        return NyCollectionsRewardsModel

    def getIsLevelsRewardsOpened(self):
        return self._getBool(2)

    def setIsLevelsRewardsOpened(self, value):
        self._setBool(2, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(3)

    def setProgressionLevel(self, value):
        self._setNumber(3, value)
        return

    def getProgressionPoints(self):
        return self._getNumber(4)

    def setProgressionPoints(self, value):
        self._setNumber(4, value)
        return

    def getProgressionLevels(self):
        return self._getArray(5)

    def setProgressionLevels(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getProgressionLevelsType():
        return NyLevelModel

    def _initialize(self):
        super(NyProgressViewModel, self)._initialize()
        self._addViewModelProperty(b'levelsRewards', NyLevelsRewardsModel())
        self._addViewModelProperty(b'collectionsRewards', NyCollectionsRewardsModel())
        self._addBoolProperty(b'isLevelsRewardsOpened', False)
        self._addNumberProperty(b'progressionLevel', 1)
        self._addNumberProperty(b'progressionPoints', 0)
        self._addArrayProperty(b'progressionLevels', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onGotoStore = self._addCommand(b'onGotoStore')
        self.onSelectVehicleDiscount = self._addCommand(b'onSelectVehicleDiscount')
        self.onShowAnimationEnd = self._addCommand(b'onShowAnimationEnd')
        return
