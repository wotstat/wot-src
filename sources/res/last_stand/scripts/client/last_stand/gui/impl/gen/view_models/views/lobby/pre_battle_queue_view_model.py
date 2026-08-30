from last_stand.gui.impl.gen.view_models.views.lobby.vehicle_info_block_model import VehicleInfoBlockModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel
from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel

class PreBattleQueueViewModel(SelectableViewModel):
    __slots__ = (b'onExitBattle', b'onEscape')

    def __init__(self, properties=4, commands=4):
        super(PreBattleQueueViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def selectedVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getSelectedVehicleType():
        return VehicleInfoBlockModel

    @property
    def selectedDifficulty(self):
        return self._getViewModel(1)

    @staticmethod
    def getSelectedDifficultyType():
        return DifficultyItemModel

    def getIsExitButtonAvailable(self):
        return self._getBool(2)

    def setIsExitButtonAvailable(self, value):
        self._setBool(2, value)
        return

    def getTimerStartTime(self):
        return self._getNumber(3)

    def setTimerStartTime(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(PreBattleQueueViewModel, self)._initialize()
        self._addViewModelProperty(b'selectedVehicle', VehicleInfoBlockModel())
        self._addViewModelProperty(b'selectedDifficulty', DifficultyItemModel())
        self._addBoolProperty(b'isExitButtonAvailable', False)
        self._addNumberProperty(b'timerStartTime', 0)
        self.onExitBattle = self._addCommand(b'onExitBattle')
        self.onEscape = self._addCommand(b'onEscape')
        return
