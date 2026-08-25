from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class UnlockModuleProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(UnlockModuleProgressModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getModuleId(self):
        return self._getNumber(1)

    def setModuleId(self, value):
        self._setNumber(1, value)
        return

    def getItemTypeName(self):
        return self._getString(2)

    def setItemTypeName(self, value):
        self._setString(2, value)
        return

    def getUserName(self):
        return self._getString(3)

    def setUserName(self, value):
        self._setString(3, value)
        return

    def getIconName(self):
        return self._getString(4)

    def setIconName(self, value):
        self._setString(4, value)
        return

    def getLevel(self):
        return self._getNumber(5)

    def setLevel(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(UnlockModuleProgressModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceItemModel())
        self._addNumberProperty(b'moduleId', 0)
        self._addStringProperty(b'itemTypeName', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'iconName', b'')
        self._addNumberProperty(b'level', 0)
        return
