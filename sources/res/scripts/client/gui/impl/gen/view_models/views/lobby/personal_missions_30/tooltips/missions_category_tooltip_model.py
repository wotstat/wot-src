from gui.impl.gen.view_models.views.lobby.personal_missions_30.common.enums import MissionCategory
from frameworks.wulf import ViewModel

class MissionsCategoryTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MissionsCategoryTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return MissionCategory(self._getString(0))

    def setCategory(self, value):
        self._setString(0, value.value)
        return

    def getOperationName(self):
        return self._getString(1)

    def setOperationName(self, value):
        self._setString(1, value)
        return

    def getMinLevel(self):
        return self._getNumber(2)

    def setMinLevel(self, value):
        self._setNumber(2, value)
        return

    def getMaxLevel(self):
        return self._getNumber(3)

    def setMaxLevel(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(MissionsCategoryTooltipModel, self)._initialize()
        self._addStringProperty(b'category')
        self._addStringProperty(b'operationName', b'')
        self._addNumberProperty(b'minLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        return
