from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class WtEventQuestModel(DailyQuestModel):
    __slots__ = ()

    def __init__(self, properties=22, commands=0):
        super(WtEventQuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getStatusLabel(self):
        return self._getString(19)

    def setStatusLabel(self, value):
        self._setString(19, value)
        return

    def getCompletedMissions(self):
        return self._getNumber(20)

    def setCompletedMissions(self, value):
        self._setNumber(20, value)
        return

    def getMaxMissions(self):
        return self._getNumber(21)

    def setMaxMissions(self, value):
        self._setNumber(21, value)
        return

    def _initialize(self):
        super(WtEventQuestModel, self)._initialize()
        self._addStringProperty(b'statusLabel', b'')
        self._addNumberProperty(b'completedMissions', 0)
        self._addNumberProperty(b'maxMissions', 0)
        return
