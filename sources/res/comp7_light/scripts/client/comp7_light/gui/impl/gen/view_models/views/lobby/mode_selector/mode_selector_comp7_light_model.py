from comp7_light.gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_comp7_light_widget_model import ModeSelectorComp7LightWidgetModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorComp7LightModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=23, commands=0):
        super(ModeSelectorComp7LightModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def widget(self):
        return self._getViewModel(22)

    @staticmethod
    def getWidgetType():
        return ModeSelectorComp7LightWidgetModel

    def _initialize(self):
        super(ModeSelectorComp7LightModel, self)._initialize()
        self._addViewModelProperty(b'widget', ModeSelectorComp7LightWidgetModel())
        return
