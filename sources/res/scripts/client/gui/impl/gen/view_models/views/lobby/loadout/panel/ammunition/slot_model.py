from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.specialization import Specialization

class SlotModel(ViewModel):
    __slots__ = ()
    CONSUMABLE_ITEM_TYPE = b'consumable'
    SHELL_ITEM_TYPE = b'shell'
    EQUIPMENT_ITEM_TYPE = b'equipment'
    INSTRUCTION_ITEM_TYPE = b'instruction'

    def __init__(self, properties=5, commands=0):
        super(SlotModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def specialization(self):
        return self._getViewModel(0)

    @staticmethod
    def getSpecializationType():
        return Specialization

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getItemId(self):
        return self._getString(2)

    def setItemId(self, value):
        self._setString(2, value)
        return

    def getItemType(self):
        return self._getString(3)

    def setItemType(self, value):
        self._setString(3, value)
        return

    def getBindedKey(self):
        return self._getString(4)

    def setBindedKey(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(SlotModel, self)._initialize()
        self._addViewModelProperty(b'specialization', Specialization())
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'itemId', b'')
        self._addStringProperty(b'itemType', b'')
        self._addStringProperty(b'bindedKey', b'')
        return
