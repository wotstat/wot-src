from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.reward_item_model import RewardItemModel

class NyPetRaidRewardViewModel(ViewModel):
    __slots__ = (b'onClose', b'onGoToMachine', b'onGoToLootbox', b'onGotoPet', b'onShowInHangar')

    def __init__(self, properties=4, commands=5):
        super(NyPetRaidRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def rewards(self):
        return self._getViewModel(0)

    @staticmethod
    def getRewardsType():
        return RewardItemModel

    def getIsPetAvailable(self):
        return self._getBool(1)

    def setIsPetAvailable(self, value):
        self._setBool(1, value)
        return

    def getIsMachineAvailable(self):
        return self._getBool(2)

    def setIsMachineAvailable(self, value):
        self._setBool(2, value)
        return

    def getHasVehicle(self):
        return self._getBool(3)

    def setHasVehicle(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(NyPetRaidRewardViewModel, self)._initialize()
        self._addViewModelProperty(b'rewards', UserListModel())
        self._addBoolProperty(b'isPetAvailable', True)
        self._addBoolProperty(b'isMachineAvailable', True)
        self._addBoolProperty(b'hasVehicle', False)
        self.onClose = self._addCommand(b'onClose')
        self.onGoToMachine = self._addCommand(b'onGoToMachine')
        self.onGoToLootbox = self._addCommand(b'onGoToLootbox')
        self.onGotoPet = self._addCommand(b'onGotoPet')
        self.onShowInHangar = self._addCommand(b'onShowInHangar')
        return
