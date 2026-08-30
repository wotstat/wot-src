from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_grid_model import PostProgressionGridModel

class ProgressionAvailability(Enum):
    AVAILABLE = b'available'
    UNAVAILABLEELITE = b'unavailableElite'
    UNAVAILABLEPURCHASE = b'unavailablePurchase'
    UNAVAILABLERENT = b'unavailableRent'
    UNAVAILABLERENTOVER = b'unavailableRentOver'
    UNAVAILABLEBATTLE = b'unavailableBattle'
    UNAVAILABLEFORMATION = b'unavailableFormation'
    UNAVAILABLEBREAKER = b'unavailableBreaker'
    UNAVAILABLEBROKEN = b'unavailableBroken'


class ProgressionState(Enum):
    INITIAL = b'initial'
    TRANSITIONAL = b'transitional'
    FINAL = b'final'


class PostProgressionBaseViewModel(ViewModel):
    __slots__ = (b'onViewRendered',)

    def __init__(self, properties=5, commands=1):
        super(PostProgressionBaseViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def grid(self):
        return self._getViewModel(0)

    @staticmethod
    def getGridType():
        return PostProgressionGridModel

    @property
    def persistentBonuses(self):
        return self._getViewModel(1)

    @staticmethod
    def getPersistentBonusesType():
        return BonusesModel

    def getProgressionAvailability(self):
        return ProgressionAvailability(self._getString(2))

    def setProgressionAvailability(self, value):
        self._setString(2, value.value)
        return

    def getProgressionState(self):
        return ProgressionState(self._getString(3))

    def setProgressionState(self, value):
        self._setString(3, value.value)
        return

    def getVehicleRole(self):
        return self._getString(4)

    def setVehicleRole(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(PostProgressionBaseViewModel, self)._initialize()
        self._addViewModelProperty(b'grid', PostProgressionGridModel())
        self._addViewModelProperty(b'persistentBonuses', BonusesModel())
        self._addStringProperty(b'progressionAvailability')
        self._addStringProperty(b'progressionState')
        self._addStringProperty(b'vehicleRole', b'')
        self.onViewRendered = self._addCommand(b'onViewRendered')
        return
