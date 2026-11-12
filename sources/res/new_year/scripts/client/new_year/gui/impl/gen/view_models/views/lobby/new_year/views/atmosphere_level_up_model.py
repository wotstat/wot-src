from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class AtmosphereLevelUpModel(ViewModel):
    __slots__ = (b'onClose', b'onGotoStore', b'onGotoQuests', b'onSelectVehicleDiscount')

    def __init__(self, properties=7, commands=4):
        super(AtmosphereLevelUpModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    @property
    def hugeRewards(self):
        return self._getViewModel(1)

    @staticmethod
    def getHugeRewardsType():
        return RewardItemModel

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def getCollection(self):
        return self._getString(3)

    def setCollection(self, value):
        self._setString(3, value)
        return

    def getIsViewReady(self):
        return self._getBool(4)

    def setIsViewReady(self, value):
        self._setBool(4, value)
        return

    def getIsDeferredGraphics(self):
        return self._getBool(5)

    def setIsDeferredGraphics(self, value):
        self._setBool(5, value)
        return

    def getIsMachineEnabled(self):
        return self._getBool(6)

    def setIsMachineEnabled(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(AtmosphereLevelUpModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addViewModelProperty(b'hugeRewards', UserListModel())
        self._addNumberProperty(b'level', 0)
        self._addStringProperty(b'collection', b'')
        self._addBoolProperty(b'isViewReady', False)
        self._addBoolProperty(b'isDeferredGraphics', False)
        self._addBoolProperty(b'isMachineEnabled', False)
        self.onClose = self._addCommand(b'onClose')
        self.onGotoStore = self._addCommand(b'onGotoStore')
        self.onGotoQuests = self._addCommand(b'onGotoQuests')
        self.onSelectVehicleDiscount = self._addCommand(b'onSelectVehicleDiscount')
        return
