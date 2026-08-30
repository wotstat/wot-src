from gui.impl.gen.view_models.common.missions.conditions.condition_base_model import ConditionBaseModel

class PreformattedConditionModel(ConditionBaseModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(PreformattedConditionModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitleData(self):
        return self._getString(1)

    def setTitleData(self, value):
        self._setString(1, value)
        return

    def getDescrData(self):
        return self._getString(2)

    def setDescrData(self, value):
        self._setString(2, value)
        return

    def getIconKey(self):
        return self._getString(3)

    def setIconKey(self, value):
        self._setString(3, value)
        return

    def getCurrent(self):
        return self._getNumber(4)

    def setCurrent(self, value):
        self._setNumber(4, value)
        return

    def getTotal(self):
        return self._getNumber(5)

    def setTotal(self, value):
        self._setNumber(5, value)
        return

    def getEarned(self):
        return self._getNumber(6)

    def setEarned(self, value):
        self._setNumber(6, value)
        return

    def getProgressType(self):
        return self._getString(7)

    def setProgressType(self, value):
        self._setString(7, value)
        return

    def getSortKey(self):
        return self._getString(8)

    def setSortKey(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(PreformattedConditionModel, self)._initialize()
        self._addStringProperty(b'titleData', b'')
        self._addStringProperty(b'descrData', b'')
        self._addStringProperty(b'iconKey', b'')
        self._addNumberProperty(b'current', 0)
        self._addNumberProperty(b'total', 0)
        self._addNumberProperty(b'earned', 0)
        self._addStringProperty(b'progressType', b'')
        self._addStringProperty(b'sortKey', b'')
        return
