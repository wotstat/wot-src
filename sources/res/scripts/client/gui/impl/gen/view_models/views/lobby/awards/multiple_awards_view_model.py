from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.awards.reward_model import RewardModel

class MultipleAwardsViewModel(ViewModel):
    __slots__ = (b'showHangar', b'makeChoice', b'onClose')

    def __init__(self, properties=9, commands=3):
        super(MultipleAwardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardModel

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def getTitleIcon(self):
        return self._getString(2)

    def setTitleIcon(self, value):
        self._setString(2, value)
        return

    def getSubTitle(self):
        return self._getString(3)

    def setSubTitle(self, value):
        self._setString(3, value)
        return

    def getIsRibbonGold(self):
        return self._getBool(4)

    def setIsRibbonGold(self, value):
        self._setBool(4, value)
        return

    def getIsLightVisible(self):
        return self._getBool(5)

    def setIsLightVisible(self, value):
        self._setBool(5, value)
        return

    def getHasVehicleToView(self):
        return self._getBool(6)

    def setHasVehicleToView(self, value):
        self._setBool(6, value)
        return

    def getHasRewardsOnChoice(self):
        return self._getBool(7)

    def setHasRewardsOnChoice(self, value):
        self._setBool(7, value)
        return

    def getMainItemsCount(self):
        return self._getNumber(8)

    def setMainItemsCount(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(MultipleAwardsViewModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'titleIcon', b'')
        self._addStringProperty(b'subTitle', b'')
        self._addBoolProperty(b'isRibbonGold', False)
        self._addBoolProperty(b'isLightVisible', False)
        self._addBoolProperty(b'hasVehicleToView', False)
        self._addBoolProperty(b'hasRewardsOnChoice', False)
        self._addNumberProperty(b'mainItemsCount', 0)
        self.showHangar = self._addCommand(b'showHangar')
        self.makeChoice = self._addCommand(b'makeChoice')
        self.onClose = self._addCommand(b'onClose')
        return
