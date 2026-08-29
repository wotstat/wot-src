from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class ParagonsRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSelectVehicleAsReward', b'onShowVehicleInHangar')

    def __init__(self, properties=5, commands=3):
        super(ParagonsRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDescription(self):
        return self._getString(0)

    def setDescription(self, value):
        self._setString(0, value)
        return

    def getChapterLevel(self):
        return self._getNumber(1)

    def setChapterLevel(self, value):
        self._setNumber(1, value)
        return

    def getSelectedVehicle(self):
        return self._getBool(2)

    def setSelectedVehicle(self, value):
        self._setBool(2, value)
        return

    def getMainRewards(self):
        return self._getArray(3)

    def setMainRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getMainRewardsType():
        return IconBonusModel

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(ParagonsRewardsViewModel, self)._initialize()
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'chapterLevel', 0)
        self._addBoolProperty(b'selectedVehicle', False)
        self._addArrayProperty(b'mainRewards', Array())
        self._addArrayProperty(b'rewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onSelectVehicleAsReward = self._addCommand(b'onSelectVehicleAsReward')
        self.onShowVehicleInHangar = self._addCommand(b'onShowVehicleInHangar')
        return
