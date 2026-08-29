from enum import Enum
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.key_type_model import KeyTypeModel

class KeyType(Enum):
    SIMPLE = b'simpleKey'
    LOCKPICK = b'lockpick'


class LootboxKeyViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(LootboxKeyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def keyType(self):
        return self._getViewModel(0)

    @staticmethod
    def getKeyTypeType():
        return KeyTypeModel

    def getKeyID(self):
        return self._getNumber(1)

    def setKeyID(self, value):
        self._setNumber(1, value)
        return

    def getCount(self):
        return self._getNumber(2)

    def setCount(self, value):
        self._setNumber(2, value)
        return

    def getIconName(self):
        return self._getString(3)

    def setIconName(self, value):
        self._setString(3, value)
        return

    def getUserName(self):
        return self._getString(4)

    def setUserName(self, value):
        self._setString(4, value)
        return

    def getOpenProbability(self):
        return self._getReal(5)

    def setOpenProbability(self, value):
        self._setReal(5, value)
        return

    def _initialize(self):
        super(LootboxKeyViewModel, self)._initialize()
        self._addViewModelProperty(b'keyType', KeyTypeModel())
        self._addNumberProperty(b'keyID', 0)
        self._addNumberProperty(b'count', 0)
        self._addStringProperty(b'iconName', b'unknown')
        self._addStringProperty(b'userName', b'unknown')
        self._addRealProperty(b'openProbability', 100.0)
        return
