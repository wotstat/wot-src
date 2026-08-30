import typing
from enum import Enum
from frameworks.wulf import Array, ViewModel
T = typing.TypeVar(b'T')

class ProposalDisableReason(Enum):
    NONE = b'none'
    NOT_FORMED = b'notFormed'
    BUILT_IN_STYLE = b'builtInStyle'


class ProposalType(Enum):
    NONE = b'none'
    CREW = b'crew'
    OPT_DEVICES = b'optDevices'
    SHELLS = b'shells'
    CONSUMABLES = b'consumables'
    STYLES = b'styles'


class ProposalModel(ViewModel, typing.Generic[T]):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ProposalModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelected(self):
        return self._getBool(0)

    def setSelected(self, value):
        self._setBool(0, value)
        return

    def getDisableReason(self):
        return ProposalDisableReason(self._getString(1))

    def setDisableReason(self, value):
        self._setString(1, value.value)
        return

    def getPresetIndex(self):
        return self._getNumber(2)

    def setPresetIndex(self, value):
        self._setNumber(2, value)
        return

    def getPresets(self):
        return self._getArray(3)

    def setPresets(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getPresetsType():
        return T

    def _initialize(self):
        super(ProposalModel, self)._initialize()
        self._addBoolProperty(b'selected', False)
        self._addStringProperty(b'disableReason')
        self._addNumberProperty(b'presetIndex', 0)
        self._addArrayProperty(b'presets', Array())
        return
