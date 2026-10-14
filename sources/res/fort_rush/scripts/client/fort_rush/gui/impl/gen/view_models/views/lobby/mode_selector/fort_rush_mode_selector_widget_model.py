from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class FortRushModeSelectorWidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(FortRushModeSelectorWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentProgress(self):
        return self._getNumber(1)

    def setCurrentProgress(self, value):
        self._setNumber(1, value)
        return

    def getTotalCount(self):
        return self._getNumber(2)

    def setTotalCount(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(FortRushModeSelectorWidgetModel, self)._initialize()
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalCount', 0)
        return
