from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel

class EventViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(EventViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getRewards(self):
        return self._getArray(0)

    def setRewards(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def getEventId(self):
        return self._getNumber(1)

    def setEventId(self, value):
        self._setNumber(1, value)
        return

    def getEventType(self):
        return self._getString(2)

    def setEventType(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(EventViewModel, self)._initialize()
        self._addArrayProperty(b'rewards', Array())
        self._addNumberProperty(b'eventId', 0)
        self._addStringProperty(b'eventType', b'')
        self.onClose = self._addCommand(b'onClose')
        return
