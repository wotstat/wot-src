from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.base_product_model import BaseProductModel

class PageState(IntEnum):
    CONFIRMATION = 0
    FLYBY = 1
    CONGRATULATION = 2
    ERROR = 3


class PurchaseDialogModel(ViewModel):
    __slots__ = (b'onClose', b'onConfirm', b'onMouseOver3dScene', b'onMoveSpace')

    def __init__(self, properties=4, commands=4):
        super(PurchaseDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getPageState(self):
        return PageState(self._getNumber(0))

    def setPageState(self, value):
        self._setNumber(0, value.value)
        return

    def getProduct(self):
        return self._getArray(1)

    def setProduct(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getProductType():
        return BaseProductModel

    def getHasSuitableVehicle(self):
        return self._getBool(2)

    def setHasSuitableVehicle(self, value):
        self._setBool(2, value)
        return

    def getIsPurchaseProcessing(self):
        return self._getBool(3)

    def setIsPurchaseProcessing(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(PurchaseDialogModel, self)._initialize()
        self._addNumberProperty(b'pageState', PageState.CONFIRMATION.value)
        self._addArrayProperty(b'product', Array())
        self._addBoolProperty(b'hasSuitableVehicle', False)
        self._addBoolProperty(b'isPurchaseProcessing', False)
        self.onClose = self._addCommand(b'onClose')
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onMouseOver3dScene = self._addCommand(b'onMouseOver3dScene')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        return
