from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel

class PostProgressionWidgetModel(ComponentBaseModel):
    __slots__ = (b'onWidgetClick',)

    def __init__(self, properties=5, commands=1):
        super(PostProgressionWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getProgressCurrent(self):
        return self._getNumber(2)

    def setProgressCurrent(self, value):
        self._setNumber(2, value)
        return

    def getProgressMax(self):
        return self._getNumber(3)

    def setProgressMax(self, value):
        self._setNumber(3, value)
        return

    def getHasWarning(self):
        return self._getBool(4)

    def setHasWarning(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(PostProgressionWidgetModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'progressCurrent', 0)
        self._addNumberProperty(b'progressMax', 0)
        self._addBoolProperty(b'hasWarning', False)
        self.onWidgetClick = self._addCommand(b'onWidgetClick')
        return
