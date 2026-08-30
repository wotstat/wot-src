from enum import Enum
from frameworks.wulf import Map, ViewModel

class AlertType(Enum):
    NONE = b'none'
    CEASEFIRECURRENTSERVER = b'ceasefireCurrentServer'
    CEASEFIREALLSERVERS = b'ceasefireAllServers'
    MODEISUNAVAILABLE = b'modeIsUnavailable'
    MODEISFINISHED = b'modeIsFinished'


class AlertMessageModel(ViewModel):
    __slots__ = (b'onChangeServer',)

    def __init__(self, properties=2, commands=1):
        super(AlertMessageModel, self).__init__(properties=properties, commands=commands)
        return

    def getAlertType(self):
        return AlertType(self._getString(0))

    def setAlertType(self, value):
        self._setString(0, value.value)
        return

    def getBattleSchedule(self):
        return self._getMap(1)

    def setBattleSchedule(self, value):
        self._setMap(1, value)
        return

    @staticmethod
    def getBattleScheduleType():
        return (unicode, unicode)

    def _initialize(self):
        super(AlertMessageModel, self)._initialize()
        self._addStringProperty(b'alertType', AlertType.NONE.value)
        self._addMapProperty(b'battleSchedule', Map(unicode, unicode))
        self.onChangeServer = self._addCommand(b'onChangeServer')
        return
