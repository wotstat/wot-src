from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel

class RewardWindowContentModel(ViewModel):
    __slots__ = (b'onConfirmBtnClicked', b'onSecondBtnClicked', b'onHyperLinkClicked')

    def __init__(self, properties=3, commands=3):
        super(RewardWindowContentModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewardsList(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsListType():
        return ListModel

    def getEventName(self):
        return self._getString(1)

    def setEventName(self, value):
        self._setString(1, value)
        return

    def getShowRewards(self):
        return self._getBool(2)

    def setShowRewards(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(RewardWindowContentModel, self)._initialize()
        self._addViewModelProperty(b'rewardsList', ListModel())
        self._addStringProperty(b'eventName', b'')
        self._addBoolProperty(b'showRewards', False)
        self.onConfirmBtnClicked = self._addCommand(b'onConfirmBtnClicked')
        self.onSecondBtnClicked = self._addCommand(b'onSecondBtnClicked')
        self.onHyperLinkClicked = self._addCommand(b'onHyperLinkClicked')
        return
