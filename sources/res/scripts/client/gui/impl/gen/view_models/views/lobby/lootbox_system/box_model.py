from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.slot_model import SlotModel

class BoxModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(BoxModel, self).__init__(properties=properties, commands=commands)
        return

    def getCategory(self):
        return self._getString(0)

    def setCategory(self, value):
        self._setString(0, value)
        return

    def getCount(self):
        return self._getNumber(1)

    def setCount(self, value):
        self._setNumber(1, value)
        return

    def getCountToGuaranteed(self):
        return self._getNumber(2)

    def setCountToGuaranteed(self, value):
        self._setNumber(2, value)
        return

    def getGuaranteedLimit(self):
        return self._getNumber(3)

    def setGuaranteedLimit(self, value):
        self._setNumber(3, value)
        return

    def getSlots(self):
        return self._getArray(4)

    def setSlots(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getSlotsType():
        return SlotModel

    def _initialize(self):
        super(BoxModel, self)._initialize()
        self._addStringProperty(b'category', b'')
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'countToGuaranteed', 0)
        self._addNumberProperty(b'guaranteedLimit', 0)
        self._addArrayProperty(b'slots', Array())
        return
