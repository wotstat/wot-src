from enum import Enum
from frameworks.wulf import ViewModel

class StatusList(Enum):
    DEFAULT = b'default'
    DISABLED = b'disabled'
    ACTIVE = b'active'
    FINISHED = b'finished'
    ANNOUNCEMENT = b'announcement'
    PAUSED = b'paused'


class ChapterStatusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(ChapterStatusModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatus(self):
        return StatusList(self._getString(0))

    def setStatus(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(ChapterStatusModel, self)._initialize()
        self._addStringProperty(b'status', StatusList.DEFAULT.value)
        return
