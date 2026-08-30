from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.panel.ammunition.slot_model import SlotModel

class SectionState(Enum):
    DEFAULT = b'default'
    WARNING = b'warning'


class SectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SectionModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getSlots(self):
        return self._getArray(1)

    def setSlots(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSlotsType():
        return SlotModel

    def getType(self):
        return self._getString(2)

    def setType(self, value):
        self._setString(2, value)
        return

    def getState(self):
        return SectionState(self._getString(3))

    def setState(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(SectionModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addArrayProperty(b'slots', Array())
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'state')
        return
