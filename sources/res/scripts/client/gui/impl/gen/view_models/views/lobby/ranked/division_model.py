from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.ranked.rank_model import RankModel

class DivisionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(DivisionModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def ranks(self):
        return self._getViewModel(0)

    @staticmethod
    def getRanksType():
        return RankModel

    def getDivisionID(self):
        return self._getNumber(1)

    def setDivisionID(self, value):
        self._setNumber(1, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(2)

    def setVehicleLevel(self, value):
        self._setNumber(2, value)
        return

    def getFirstRank(self):
        return self._getNumber(3)

    def setFirstRank(self, value):
        self._setNumber(3, value)
        return

    def getLastRank(self):
        return self._getNumber(4)

    def setLastRank(self, value):
        self._setNumber(4, value)
        return

    def getIsSingleReward(self):
        return self._getBool(5)

    def setIsSingleReward(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(DivisionModel, self)._initialize()
        self._addViewModelProperty(b'ranks', UserListModel())
        self._addNumberProperty(b'divisionID', 0)
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addNumberProperty(b'firstRank', 0)
        self._addNumberProperty(b'lastRank', 0)
        self._addBoolProperty(b'isSingleReward', True)
        return
