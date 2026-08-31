from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ConfirmationModel(ViewModel):
    __slots__ = (b'confirm', b'cancel')

    def __init__(self, properties=2, commands=2):
        super(ConfirmationModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getEventName(self):
        return self._getString(1)

    def setEventName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(ConfirmationModel, self)._initialize()
        self._addViewModelProperty(b'price', PriceItemModel())
        self._addStringProperty(b'eventName', b'')
        self.confirm = self._addCommand(b'confirm')
        self.cancel = self._addCommand(b'cancel')
        return
