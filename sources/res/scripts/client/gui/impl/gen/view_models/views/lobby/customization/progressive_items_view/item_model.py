from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.customization.progressive_items_view.item_level_info_model import ItemLevelInfoModel

class ItemModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(ItemModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def eachLevelInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getEachLevelInfoType():
        return ItemLevelInfoModel

    def getMaxLevel(self):
        return self._getNumber(1)

    def setMaxLevel(self, value):
        self._setNumber(1, value)
        return

    def getCurrentLevel(self):
        return self._getNumber(2)

    def setCurrentLevel(self, value):
        self._setNumber(2, value)
        return

    def getItemId(self):
        return self._getNumber(3)

    def setItemId(self, value):
        self._setNumber(3, value)
        return

    def getScaleFactor(self):
        return self._getString(4)

    def setScaleFactor(self, value):
        self._setString(4, value)
        return

    def getItemUserString(self):
        return self._getString(5)

    def setItemUserString(self, value):
        self._setString(5, value)
        return

    def getItemType(self):
        return self._getString(6)

    def setItemType(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(ItemModel, self)._initialize()
        self._addViewModelProperty(b'eachLevelInfo', UserListModel())
        self._addNumberProperty(b'maxLevel', -1)
        self._addNumberProperty(b'currentLevel', -1)
        self._addNumberProperty(b'itemId', 0)
        self._addStringProperty(b'scaleFactor', b'')
        self._addStringProperty(b'itemUserString', b'')
        self._addStringProperty(b'itemType', b'')
        return
