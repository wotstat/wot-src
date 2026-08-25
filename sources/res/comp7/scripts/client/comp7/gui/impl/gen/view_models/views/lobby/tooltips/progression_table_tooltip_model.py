from comp7.gui.impl.gen.view_models.views.lobby.enums import SeasonName
from frameworks.wulf import Array
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.progression_base_model import ProgressionBaseModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_item_model import ProgressionItemModel

class ProgressionTableTooltipModel(ProgressionBaseModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(ProgressionTableTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getSeasonName(self):
        return SeasonName(self._getString(2))

    def setSeasonName(self, value):
        self._setString(2, value.value)
        return

    def getCurrentScore(self):
        return self._getNumber(3)

    def setCurrentScore(self, value):
        self._setNumber(3, value)
        return

    def getRankInactivityCount(self):
        return self._getNumber(4)

    def setRankInactivityCount(self, value):
        self._setNumber(4, value)
        return

    def getRankInactivityPointsCount(self):
        return self._getNumber(5)

    def setRankInactivityPointsCount(self, value):
        self._setNumber(5, value)
        return

    def getEarnedRankInactivityPerBattle(self):
        return self._getNumber(6)

    def setEarnedRankInactivityPerBattle(self, value):
        self._setNumber(6, value)
        return

    def getItems(self):
        return self._getArray(7)

    def setItems(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getItemsType():
        return ProgressionItemModel

    def _initialize(self):
        super(ProgressionTableTooltipModel, self)._initialize()
        self._addStringProperty(b'seasonName')
        self._addNumberProperty(b'currentScore', 0)
        self._addNumberProperty(b'rankInactivityCount', -1)
        self._addNumberProperty(b'rankInactivityPointsCount', 0)
        self._addNumberProperty(b'earnedRankInactivityPerBattle', 0)
        self._addArrayProperty(b'items', Array())
        return
