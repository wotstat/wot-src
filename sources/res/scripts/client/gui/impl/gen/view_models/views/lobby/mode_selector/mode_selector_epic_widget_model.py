from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class ModeSelectorEpicWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ModeSelectorEpicWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getRestRewards(self):
        return self._getNumber(2)

    def setRestRewards(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(ModeSelectorEpicWidgetModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'restRewards', 0)
        return
