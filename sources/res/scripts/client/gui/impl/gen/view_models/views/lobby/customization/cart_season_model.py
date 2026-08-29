from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.customization.cart_slot_model import CartSlotModel

class CartSeasonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(CartSeasonModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def items(self):
        return self._getViewModel(0)

    @staticmethod
    def getItemsType():
        return CartSlotModel

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)
        return

    def getBonusType(self):
        return self._getString(3)

    def setBonusType(self, value):
        self._setString(3, value)
        return

    def getBonusValue(self):
        return self._getString(4)

    def setBonusValue(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(CartSeasonModel, self)._initialize()
        self._addViewModelProperty(b'items', UserListModel())
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'count', -1)
        self._addStringProperty(b'bonusType', b'')
        self._addStringProperty(b'bonusValue', b'')
        return
