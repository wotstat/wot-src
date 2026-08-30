from frameworks.wulf import ViewModel

class FunRandomModifiersPanelModel(ViewModel):
    __slots__ = (b'onWidgetClick',)

    def __init__(self, properties=1, commands=1):
        super(FunRandomModifiersPanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsPanelClicked(self):
        return self._getBool(0)

    def setIsPanelClicked(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(FunRandomModifiersPanelModel, self)._initialize()
        self._addBoolProperty(b'isPanelClicked', False)
        self.onWidgetClick = self._addCommand(b'onWidgetClick')
        return
