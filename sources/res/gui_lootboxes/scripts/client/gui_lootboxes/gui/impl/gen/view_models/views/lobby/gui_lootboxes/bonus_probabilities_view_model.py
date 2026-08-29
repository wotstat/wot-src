from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.slot_view_model import SlotViewModel

class BonusProbabilitiesViewModel(ViewModel):
    __slots__ = (b'onClose', b'onPreview')

    def __init__(self, properties=8, commands=2):
        super(BonusProbabilitiesViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getLootboxName(self):
        return self._getString(0)

    def setLootboxName(self, value):
        self._setString(0, value)
        return

    def getLootboxID(self):
        return self._getNumber(1)

    def setLootboxID(self, value):
        self._setNumber(1, value)
        return

    def getLootboxTier(self):
        return self._getNumber(2)

    def setLootboxTier(self, value):
        self._setNumber(2, value)
        return

    def getSlots(self):
        return self._getArray(3)

    def setSlots(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getSlotsType():
        return SlotViewModel

    def getGuaranteedFrequencies(self):
        return self._getArray(4)

    def setGuaranteedFrequencies(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getGuaranteedFrequenciesType():
        return int

    def getHasLootLists(self):
        return self._getBool(5)

    def setHasLootLists(self, value):
        self._setBool(5, value)
        return

    def getRotationStage(self):
        return self._getNumber(6)

    def setRotationStage(self, value):
        self._setNumber(6, value)
        return

    def getLootLists(self):
        return self._getArray(7)

    def setLootLists(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getLootListsType():
        return SlotViewModel

    def _initialize(self):
        super(BonusProbabilitiesViewModel, self)._initialize()
        self._addStringProperty(b'lootboxName', b'')
        self._addNumberProperty(b'lootboxID', 0)
        self._addNumberProperty(b'lootboxTier', 0)
        self._addArrayProperty(b'slots', Array())
        self._addArrayProperty(b'guaranteedFrequencies', Array())
        self._addBoolProperty(b'hasLootLists', False)
        self._addNumberProperty(b'rotationStage', 0)
        self._addArrayProperty(b'lootLists', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onPreview = self._addCommand(b'onPreview')
        return
