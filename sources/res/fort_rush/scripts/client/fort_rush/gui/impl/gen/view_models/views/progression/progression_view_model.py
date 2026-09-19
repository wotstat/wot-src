from frameworks.wulf import Array, ViewModel
from fort_rush.gui.impl.gen.view_models.views.progression.milestone_model import MilestoneModel
from fort_rush.gui.impl.gen.view_models.views.progression.mission_model import MissionModel

class ProgressionViewModel(ViewModel):
    __slots__ = (b'onMessageClick',)

    def __init__(self, properties=7, commands=1):
        super(ProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventStartDateTime(self):
        return self._getNumber(0)

    def setEventStartDateTime(self, value):
        self._setNumber(0, value)
        return

    def getEventEndDateTime(self):
        return self._getNumber(1)

    def setEventEndDateTime(self, value):
        self._setNumber(1, value)
        return

    def getNewMissionsDateTime(self):
        return self._getNumber(2)

    def setNewMissionsDateTime(self, value):
        self._setNumber(2, value)
        return

    def getMissions(self):
        return self._getArray(3)

    def setMissions(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getMissionsType():
        return MissionModel

    def getPreviousEventPoints(self):
        return self._getNumber(4)

    def setPreviousEventPoints(self, value):
        self._setNumber(4, value)
        return

    def getCurrentEventPoints(self):
        return self._getNumber(5)

    def setCurrentEventPoints(self, value):
        self._setNumber(5, value)
        return

    def getMilestones(self):
        return self._getArray(6)

    def setMilestones(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getMilestonesType():
        return MilestoneModel

    def _initialize(self):
        super(ProgressionViewModel, self)._initialize()
        self._addNumberProperty(b'eventStartDateTime', 0)
        self._addNumberProperty(b'eventEndDateTime', 0)
        self._addNumberProperty(b'newMissionsDateTime', 0)
        self._addArrayProperty(b'missions', Array())
        self._addNumberProperty(b'previousEventPoints', 0)
        self._addNumberProperty(b'currentEventPoints', 0)
        self._addArrayProperty(b'milestones', Array())
        self.onMessageClick = self._addCommand(b'onMessageClick')
        return
