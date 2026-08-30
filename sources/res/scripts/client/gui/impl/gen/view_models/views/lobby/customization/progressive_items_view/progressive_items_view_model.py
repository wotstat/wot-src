from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_view.item_model import ItemModel
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_view.progression_cases_tutorial_model import ProgressionCasesTutorialModel

class ProgressiveItemsViewModel(ViewModel):
    __slots__ = (b'onSelectItem', b'playSounds')

    def __init__(self, properties=7, commands=2):
        super(ProgressiveItemsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progressiveItems(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressiveItemsType():
        return ItemModel

    @property
    def tutorial(self):
        return self._getViewModel(1)

    @staticmethod
    def getTutorialType():
        return ProgressionCasesTutorialModel

    def getTankLevel(self):
        return self._getString(2)

    def setTankLevel(self, value):
        self._setString(2, value)
        return

    def getTankType(self):
        return self._getResource(3)

    def setTankType(self, value):
        self._setResource(3, value)
        return

    def getTankName(self):
        return self._getString(4)

    def setTankName(self, value):
        self._setString(4, value)
        return

    def getIsRendererPipelineDeferred(self):
        return self._getBool(5)

    def setIsRendererPipelineDeferred(self, value):
        self._setBool(5, value)
        return

    def getItemToScroll(self):
        return self._getNumber(6)

    def setItemToScroll(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(ProgressiveItemsViewModel, self)._initialize()
        self._addViewModelProperty(b'progressiveItems', UserListModel())
        self._addViewModelProperty(b'tutorial', ProgressionCasesTutorialModel())
        self._addStringProperty(b'tankLevel', b'')
        self._addResourceProperty(b'tankType', R.invalid())
        self._addStringProperty(b'tankName', b'')
        self._addBoolProperty(b'isRendererPipelineDeferred', False)
        self._addNumberProperty(b'itemToScroll', 0)
        self.onSelectItem = self._addCommand(b'onSelectItem')
        self.playSounds = self._addCommand(b'playSounds')
        return
