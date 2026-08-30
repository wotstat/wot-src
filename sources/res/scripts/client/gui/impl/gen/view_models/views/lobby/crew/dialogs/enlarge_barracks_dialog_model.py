from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.stepper_view_model import StepperViewModel

class EnlargeBarracksDialogModel(DialogTemplateViewModel):
    __slots__ = (b'onBunksCountChange',)

    def __init__(self, properties=10, commands=3):
        super(EnlargeBarracksDialogModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def stepper(self):
        return self._getViewModel(6)

    @staticmethod
    def getStepperType():
        return StepperViewModel

    @property
    def currency(self):
        return self._getViewModel(7)

    @staticmethod
    def getCurrencyType():
        return CurrencyViewModel

    def getFreeBunksCount(self):
        return self._getNumber(8)

    def setFreeBunksCount(self, value):
        self._setNumber(8, value)
        return

    def getAllBunksCount(self):
        return self._getNumber(9)

    def setAllBunksCount(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(EnlargeBarracksDialogModel, self)._initialize()
        self._addViewModelProperty(b'stepper', StepperViewModel())
        self._addViewModelProperty(b'currency', CurrencyViewModel())
        self._addNumberProperty(b'freeBunksCount', 0)
        self._addNumberProperty(b'allBunksCount', 0)
        self.onBunksCountChange = self._addCommand(b'onBunksCountChange')
        return
