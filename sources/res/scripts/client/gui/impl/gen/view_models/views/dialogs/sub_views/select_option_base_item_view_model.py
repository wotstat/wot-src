from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_generic_tooltip_view_model import DialogTemplateGenericTooltipViewModel

class ComponentType(Enum):
    BASE = b'base'
    MONEY = b'money'
    DEMOUNT_KIT = b'demountKit'


class SelectOptionBaseItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SelectOptionBaseItemViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def tooltip(self):
        return self._getViewModel(0)

    @staticmethod
    def getTooltipType():
        return DialogTemplateGenericTooltipViewModel

    def getComponentType(self):
        return ComponentType(self._getString(1))

    def setComponentType(self, value):
        self._setString(1, value.value)
        return

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def _initialize(self):
        super(SelectOptionBaseItemViewModel, self)._initialize()
        self._addViewModelProperty(b'tooltip', DialogTemplateGenericTooltipViewModel())
        self._addStringProperty(b'componentType')
        self._addBoolProperty(b'isDisabled', False)
        self._addResourceProperty(b'icon', R.invalid())
        return
