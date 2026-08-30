from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_card_model import ModeSelectorCardModel

class ModeSelectorModel(ViewModel):
    __slots__ = (b'onItemClicked', b'onShowMapSelectionClicked', b'onShowWidgetsClicked', b'onInfoClicked')

    def __init__(self, properties=5, commands=4):
        super(ModeSelectorModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsContentVisible(self):
        return self._getBool(0)

    def setIsContentVisible(self, value):
        self._setBool(0, value)
        return

    def getIsMapSelectionVisible(self):
        return self._getBool(1)

    def setIsMapSelectionVisible(self, value):
        self._setBool(1, value)
        return

    def getIsMapSelectionEnabled(self):
        return self._getBool(2)

    def setIsMapSelectionEnabled(self, value):
        self._setBool(2, value)
        return

    def getAreWidgetsVisible(self):
        return self._getBool(3)

    def setAreWidgetsVisible(self, value):
        self._setBool(3, value)
        return

    def getCardList(self):
        return self._getArray(4)

    def setCardList(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getCardListType():
        return ModeSelectorCardModel

    def _initialize(self):
        super(ModeSelectorModel, self)._initialize()
        self._addBoolProperty(b'isContentVisible', True)
        self._addBoolProperty(b'isMapSelectionVisible', False)
        self._addBoolProperty(b'isMapSelectionEnabled', False)
        self._addBoolProperty(b'areWidgetsVisible', False)
        self._addArrayProperty(b'cardList', Array())
        self.onItemClicked = self._addCommand(b'onItemClicked')
        self.onShowMapSelectionClicked = self._addCommand(b'onShowMapSelectionClicked')
        self.onShowWidgetsClicked = self._addCommand(b'onShowWidgetsClicked')
        self.onInfoClicked = self._addCommand(b'onInfoClicked')
        return
