from gui.impl.gen.view_models.views.battle_royale.battle_results.personal.personal_results_model import PersonalResultsModel
from gui.impl.gen.view_models.views.lobby.battle_royale.battle_result_view.battle_pass_progress import BattlePassProgress

class BattleResultsTabModel(PersonalResultsModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(BattleResultsTabModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battlePassProgress(self):
        return self._getViewModel(4)

    @staticmethod
    def getBattlePassProgressType():
        return BattlePassProgress

    def getPlace(self):
        return self._getNumber(5)

    def setPlace(self, value):
        self._setNumber(5, value)
        return

    def getHasPremium(self):
        return self._getBool(6)

    def setHasPremium(self, value):
        self._setBool(6, value)
        return

    def getVehicleType(self):
        return self._getString(7)

    def setVehicleType(self, value):
        self._setString(7, value)
        return

    def getVehicleName(self):
        return self._getString(8)

    def setVehicleName(self, value):
        self._setString(8, value)
        return

    def getQuestCompleted(self):
        return self._getNumber(9)

    def setQuestCompleted(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(BattleResultsTabModel, self)._initialize()
        self._addViewModelProperty(b'battlePassProgress', BattlePassProgress())
        self._addNumberProperty(b'place', 0)
        self._addBoolProperty(b'hasPremium', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addNumberProperty(b'questCompleted', 0)
        return
