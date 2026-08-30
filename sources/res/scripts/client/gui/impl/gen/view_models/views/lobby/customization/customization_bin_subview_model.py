from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.customization.cart_season_model import CartSeasonModel

class CustomizationBinSubviewModel(ViewModel):
    __slots__ = (b'onCloseAction', b'onSelectItem', b'onTutorialClose')

    def __init__(self, properties=5, commands=3):
        super(CustomizationBinSubviewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsShown(self):
        return self._getBool(0)

    def setIsShown(self, value):
        self._setBool(0, value)
        return

    def getIsAnySelected(self):
        return self._getBool(1)

    def setIsAnySelected(self, value):
        self._setBool(1, value)
        return

    def getIsRendererPipelineDeferred(self):
        return self._getBool(2)

    def setIsRendererPipelineDeferred(self, value):
        self._setBool(2, value)
        return

    def getSelectedSeason(self):
        return self._getString(3)

    def setSelectedSeason(self, value):
        self._setString(3, value)
        return

    def getSeasons(self):
        return self._getArray(4)

    def setSeasons(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getSeasonsType():
        return CartSeasonModel

    def _initialize(self):
        super(CustomizationBinSubviewModel, self)._initialize()
        self._addBoolProperty(b'isShown', False)
        self._addBoolProperty(b'isAnySelected', False)
        self._addBoolProperty(b'isRendererPipelineDeferred', False)
        self._addStringProperty(b'selectedSeason', b'')
        self._addArrayProperty(b'seasons', Array())
        self.onCloseAction = self._addCommand(b'onCloseAction')
        self.onSelectItem = self._addCommand(b'onSelectItem')
        self.onTutorialClose = self._addCommand(b'onTutorialClose')
        return
