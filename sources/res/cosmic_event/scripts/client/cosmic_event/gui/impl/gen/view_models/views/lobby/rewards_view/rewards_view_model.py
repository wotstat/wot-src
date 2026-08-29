from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class RewardsViewModel(ViewModel):
    __slots__ = (b'onCloseButtonClick', b'onContinueButtonClick')

    def __init__(self, properties=6, commands=2):
        super(RewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSubtitle(self):
        return self._getResource(0)

    def setSubtitle(self, value):
        self._setResource(0, value)
        return

    def getTitle(self):
        return self._getResource(1)

    def setTitle(self, value):
        self._setResource(1, value)
        return

    def getInfoText(self):
        return self._getResource(2)

    def setInfoText(self, value):
        self._setResource(2, value)
        return

    def getDisplayRewardsCount(self):
        return self._getBool(3)

    def setDisplayRewardsCount(self, value):
        self._setBool(3, value)
        return

    def getProgressionStage(self):
        return self._getNumber(4)

    def setProgressionStage(self, value):
        self._setNumber(4, value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(RewardsViewModel, self)._initialize()
        self._addResourceProperty(b'subtitle', R.invalid())
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'infoText', R.invalid())
        self._addBoolProperty(b'displayRewardsCount', False)
        self._addNumberProperty(b'progressionStage', 0)
        self._addArrayProperty(b'rewards', Array())
        self.onCloseButtonClick = self._addCommand(b'onCloseButtonClick')
        self.onContinueButtonClick = self._addCommand(b'onContinueButtonClick')
        return
