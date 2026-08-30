from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel

class CrewBooksPurchaseDialogModel(DialogTemplateViewModel):
    __slots__ = (b'onStepperChanged',)

    def __init__(self, properties=10, commands=3):
        super(CrewBooksPurchaseDialogModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def bookPrice(self):
        return self._getViewModel(6)

    @staticmethod
    def getBookPriceType():
        return CurrencyViewModel

    def getBookName(self):
        return self._getString(7)

    def setBookName(self, value):
        self._setString(7, value)
        return

    def getIsBookPersonal(self):
        return self._getBool(8)

    def setIsBookPersonal(self, value):
        self._setBool(8, value)
        return

    def getExperience(self):
        return self._getNumber(9)

    def setExperience(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(CrewBooksPurchaseDialogModel, self)._initialize()
        self._addViewModelProperty(b'bookPrice', CurrencyViewModel())
        self._addStringProperty(b'bookName', b'')
        self._addBoolProperty(b'isBookPersonal', False)
        self._addNumberProperty(b'experience', 0)
        self.onStepperChanged = self._addCommand(b'onStepperChanged')
        return
