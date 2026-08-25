from frameworks.wulf import ViewModel

class ResearchConfirmDialogViewModel(ViewModel):
    __slots__ = (b'onAcceptClick', b'onCancelClick')

    def __init__(self, properties=3, commands=2):
        super(ResearchConfirmDialogViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getXp(self):
        return self._getNumber(0)

    def setXp(self, value):
        self._setNumber(0, value)
        return

    def getFreeXP(self):
        return self._getNumber(1)

    def setFreeXP(self, value):
        self._setNumber(1, value)
        return

    def getResearchedItemsText(self):
        return self._getString(2)

    def setResearchedItemsText(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ResearchConfirmDialogViewModel, self)._initialize()
        self._addNumberProperty(b'xp', 0)
        self._addNumberProperty(b'freeXP', 0)
        self._addStringProperty(b'researchedItemsText', b'')
        self.onAcceptClick = self._addCommand(b'onAcceptClick')
        self.onCancelClick = self._addCommand(b'onCancelClick')
        return
