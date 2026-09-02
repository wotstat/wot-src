from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.postbattle.events.base_event_model import BaseEventModel

class EventsStatsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(EventsStatsModel, self).__init__(properties=properties, commands=commands)
        return

    def getEvents(self):
        return self._getArray(0)

    def setEvents(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getEventsType():
        return BaseEventModel

    def getHasQuestsToShow(self):
        return self._getBool(1)

    def setHasQuestsToShow(self, value):
        self._setBool(1, value)
        return

    def getQuestsUpdateTimeLeft(self):
        return self._getNumber(2)

    def setQuestsUpdateTimeLeft(self, value):
        self._setNumber(2, value)
        return

    def getIsHunter(self):
        return self._getBool(3)

    def setIsHunter(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(EventsStatsModel, self)._initialize()
        self._addArrayProperty(b'events', Array())
        self._addBoolProperty(b'hasQuestsToShow', True)
        self._addNumberProperty(b'questsUpdateTimeLeft', 0)
        self._addBoolProperty(b'isHunter', True)
        return
