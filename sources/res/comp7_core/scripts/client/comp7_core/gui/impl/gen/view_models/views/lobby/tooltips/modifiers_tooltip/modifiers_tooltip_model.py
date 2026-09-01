from frameworks.wulf import Array, ViewModel
from comp7_core.gui.impl.gen.view_models.views.lobby.tooltips.modifiers_tooltip.modifier_model import ModifierModel
from comp7_core.gui.impl.gen.view_models.views.lobby.tooltips.modifiers_tooltip.sub_mode_modifiers import SubModeModifiers

class ModifiersTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ModifiersTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getModifiersDomain(self):
        return self._getString(0)

    def setModifiersDomain(self, value):
        self._setString(0, value)
        return

    def getModifiers(self):
        return self._getArray(1)

    def setModifiers(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getModifiersType():
        return ModifierModel

    def getSubModesModifiers(self):
        return self._getArray(2)

    def setSubModesModifiers(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSubModesModifiersType():
        return SubModeModifiers

    def _initialize(self):
        super(ModifiersTooltipModel, self)._initialize()
        self._addStringProperty(b'modifiersDomain', b'')
        self._addArrayProperty(b'modifiers', Array())
        self._addArrayProperty(b'subModesModifiers', Array())
        return
