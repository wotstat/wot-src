from enum import Enum
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class State(Enum):
    DOORS_AVAILABLE = b'doorsAvailable'
    FIRST_ENTRY = b'firstEntry'
    POST_EVENT = b'postEvent'


class AvailableDoorsViewModel(NotificationBaseModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=7, commands=1):
        super(AvailableDoorsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return State(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getBackgroundPlugin(self):
        return self._getString(2)

    def setBackgroundPlugin(self, value):
        self._setString(2, value)
        return

    def getDescriptionPlugin(self):
        return self._getString(3)

    def setDescriptionPlugin(self, value):
        self._setString(3, value)
        return

    def getEventEndDate(self):
        return self._getNumber(4)

    def setEventEndDate(self, value):
        self._setNumber(4, value)
        return

    def getIsButtonDisabled(self):
        return self._getBool(5)

    def setIsButtonDisabled(self, value):
        self._setBool(5, value)
        return

    def getRewardImagePath(self):
        return self._getString(6)

    def setRewardImagePath(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(AvailableDoorsViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addStringProperty(b'backgroundPlugin', b'')
        self._addStringProperty(b'descriptionPlugin', b'')
        self._addNumberProperty(b'eventEndDate', 0)
        self._addBoolProperty(b'isButtonDisabled', False)
        self._addStringProperty(b'rewardImagePath', b'')
        self.onClick = self._addCommand(b'onClick')
        return
