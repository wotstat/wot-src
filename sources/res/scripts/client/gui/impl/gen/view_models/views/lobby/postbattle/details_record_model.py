from frameworks.wulf import Array
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.postbattle.currency_model import CurrencyModel
from gui.impl.gen.view_models.views.lobby.postbattle.details_item_model import DetailsItemModel

class DetailsRecordModel(DetailsItemModel):
    __slots__ = ()
    EARNED = b'earned'
    EARNED_RECORD = b'earned_record'
    SUBGROUP_TOTAL = b'subgroupTotal'
    TOTAL = b'total'
    ALTERNATIVE_TOTAL = b'alternativeTotal'

    def __init__(self, properties=6, commands=0):
        super(DetailsRecordModel, self).__init__(properties=properties, commands=commands)
        return

    def getStringID(self):
        return self._getResource(2)

    def setStringID(self, value):
        self._setResource(2, value)
        return

    def getTooltipStringID(self):
        return self._getResource(3)

    def setTooltipStringID(self, value):
        self._setResource(3, value)
        return

    def getTags(self):
        return self._getArray(4)

    def setTags(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getTagsType():
        return unicode

    def getCurrencies(self):
        return self._getArray(5)

    def setCurrencies(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getCurrenciesType():
        return CurrencyModel

    def _initialize(self):
        super(DetailsRecordModel, self)._initialize()
        self._addResourceProperty(b'stringID', R.invalid())
        self._addResourceProperty(b'tooltipStringID', R.invalid())
        self._addArrayProperty(b'tags', Array())
        self._addArrayProperty(b'currencies', Array())
        return
