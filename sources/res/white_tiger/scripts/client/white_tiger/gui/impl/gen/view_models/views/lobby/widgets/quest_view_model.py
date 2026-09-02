from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class QuestViewModel(DailyQuestModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(QuestViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCompletedMissions(self):
        return self._getNumber(12)

    def setCompletedMissions(self, value):
        self._setNumber(12, value)
        return

    def getMaxMissions(self):
        return self._getNumber(13)

    def setMaxMissions(self, value):
        self._setNumber(13, value)
        return

    def getIsSpecialMission(self):
        return self._getBool(14)

    def setIsSpecialMission(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(QuestViewModel, self)._initialize()
        self._addNumberProperty(b'completedMissions', 0)
        self._addNumberProperty(b'maxMissions', 0)
        self._addBoolProperty(b'isSpecialMission', False)
        return
