from enum import Enum
from frameworks.wulf import ViewModel

class EntryPointCgfTooltipState(Enum):
    QUESTGIVER = b'questGiver'
    POSTOFFICE = b'postOffice'
    GOLDWAGON = b'goldWagon'
    ONPAUSE = b'onPause'


class EntryPointCgfTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(EntryPointCgfTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCgfEntryPoint(self):
        return self._getString(0)

    def setCgfEntryPoint(self, value):
        self._setString(0, value)
        return

    def getIsPaused(self):
        return self._getBool(1)

    def setIsPaused(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(EntryPointCgfTooltipModel, self)._initialize()
        self._addStringProperty(b'cgfEntryPoint', b'')
        self._addBoolProperty(b'isPaused', False)
        return
