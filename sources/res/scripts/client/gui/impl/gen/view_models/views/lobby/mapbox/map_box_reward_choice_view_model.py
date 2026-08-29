from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.mapbox.crew_book_reward_option_model import CrewBookRewardOptionModel

class MapBoxRewardChoiceViewModel(ViewModel):
    __slots__ = (b'onTakeClick', b'onCloseClick', b'onAnimationFinished')

    def __init__(self, properties=4, commands=3):
        super(MapBoxRewardChoiceViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return CrewBookRewardOptionModel

    def getRewardType(self):
        return self._getString(1)

    def setRewardType(self, value):
        self._setString(1, value)
        return

    def getIsOptionsSequence(self):
        return self._getBool(2)

    def setIsOptionsSequence(self, value):
        self._setBool(2, value)
        return

    def getSelectedGiftId(self):
        return self._getNumber(3)

    def setSelectedGiftId(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(MapBoxRewardChoiceViewModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addStringProperty(b'rewardType', b'')
        self._addBoolProperty(b'isOptionsSequence', False)
        self._addNumberProperty(b'selectedGiftId', -1)
        self.onTakeClick = self._addCommand(b'onTakeClick')
        self.onCloseClick = self._addCommand(b'onCloseClick')
        self.onAnimationFinished = self._addCommand(b'onAnimationFinished')
        return
