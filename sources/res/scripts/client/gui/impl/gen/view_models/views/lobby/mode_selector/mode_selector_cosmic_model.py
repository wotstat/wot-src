from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_cosmic_widget_model import ModeSelectorCosmicWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorCosmicModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=0):
        super(ModeSelectorCosmicModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def widget(self):
        return self._getViewModel(21)

    @staticmethod
    def getWidgetType():
        return ModeSelectorCosmicWidgetModel

    def getIsSuspended(self):
        return self._getBool(22)

    def setIsSuspended(self, value):
        self._setBool(22, value)
        return

    def _initialize(self):
        super(ModeSelectorCosmicModel, self)._initialize()
        self._addViewModelProperty(b'widget', ModeSelectorCosmicWidgetModel())
        self._addBoolProperty(b'isSuspended', False)
        return
