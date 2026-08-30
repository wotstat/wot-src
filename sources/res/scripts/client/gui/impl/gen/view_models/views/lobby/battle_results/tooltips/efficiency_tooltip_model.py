from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.battle_results.tooltips.efficiency_item_model import EfficiencyItemModel

class EfficiencyTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(EfficiencyTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(0)

    def setTitle(self, value):
        self._setResource(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getDescription(self):
        return self._getResource(2)

    def setDescription(self, value):
        self._setResource(2, value)
        return

    def getDetails(self):
        return self._getArray(3)

    def setDetails(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getDetailsType():
        return EfficiencyItemModel

    def getStatuses(self):
        return self._getArray(4)

    def setStatuses(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getStatusesType():
        return int

    def _initialize(self):
        super(EfficiencyTooltipModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'icon', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addArrayProperty(b'details', Array())
        self._addArrayProperty(b'statuses', Array())
        return
