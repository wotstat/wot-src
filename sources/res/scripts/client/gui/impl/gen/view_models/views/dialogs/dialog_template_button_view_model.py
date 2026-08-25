from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel

class ButtonType(Enum):
    MAIN = b'main'
    PRIMARY = b'primary'
    PRIMARY_GREEN = b'primaryGreen'
    PRIMARY_RED = b'primaryRed'
    SECONDARY = b'secondary'
    GHOST = b'ghost'


class DialogTemplateButtonViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DialogTemplateButtonViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tooltip(self):
        return self._getViewModel(0)

    @staticmethod
    def getTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getButtonID(self):
        return self._getString(1)

    def setButtonID(self, value):
        self._setString(1, value)
        return

    def getLabel(self):
        return self._getResource(2)

    def setLabel(self, value):
        self._setResource(2, value)
        return

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)
        return

    def getType(self):
        return ButtonType(self._getString(4))

    def setType(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(DialogTemplateButtonViewModel, self)._initialize()
        self._addViewModelProperty(b'tooltip', DialogTemplateGenericTooltipViewModel())
        self._addStringProperty(b'buttonID', b'')
        self._addResourceProperty(b'label', R.invalid())
        self._addBoolProperty(b'isDisabled', False)
        self._addStringProperty(b'type')
        return
