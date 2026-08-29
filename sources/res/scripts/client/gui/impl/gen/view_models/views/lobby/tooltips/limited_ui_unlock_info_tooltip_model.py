from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tooltips.condition_group import ConditionGroup

class LimitedUiUnlockInfoTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(LimitedUiUnlockInfoTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getConditionGroups(self):
        return self._getArray(0)

    def setConditionGroups(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getConditionGroupsType():
        return ConditionGroup

    def getFooterTitleText(self):
        return self._getResource(1)

    def setFooterTitleText(self, value):
        self._setResource(1, value)
        return

    def getFooterText(self):
        return self._getResource(2)

    def setFooterText(self, value):
        self._setResource(2, value)
        return

    def _initialize(self):
        super(LimitedUiUnlockInfoTooltipModel, self)._initialize()
        self._addArrayProperty(b'conditionGroups', Array())
        self._addResourceProperty(b'footerTitleText', R.invalid())
        self._addResourceProperty(b'footerText', R.invalid())
        return
