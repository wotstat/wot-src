from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.mt_birthday_quest_model import MtBirthdayQuestModel

class QuestsGiverViewModel(ViewModel):
    __slots__ = (b'onTabVisited', b'onSoundClick', b'onTabActivate')
    ASSIGNMENTS = 0
    CHALLENGE = 1

    def __init__(self, properties=11, commands=3):
        super(QuestsGiverViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTimeUpdate(self):
        return self._getNumber(0)

    def setTimeUpdate(self, value):
        self._setNumber(0, value)
        return

    def getTimeNewQuest(self):
        return self._getNumber(1)

    def setTimeNewQuest(self, value):
        self._setNumber(1, value)
        return

    def getDefaultTab(self):
        return self._getNumber(2)

    def setDefaultTab(self, value):
        self._setNumber(2, value)
        return

    def getBattleTypes(self):
        return self._getArray(3)

    def setBattleTypes(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getBattleTypesType():
        return int

    def getMinLevel(self):
        return self._getNumber(4)

    def setMinLevel(self, value):
        self._setNumber(4, value)
        return

    def getMaxLevel(self):
        return self._getNumber(5)

    def setMaxLevel(self, value):
        self._setNumber(5, value)
        return

    def getAssignmentsQuests(self):
        return self._getArray(6)

    def setAssignmentsQuests(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getAssignmentsQuestsType():
        return MtBirthdayQuestModel

    def getChallengeQuests(self):
        return self._getArray(7)

    def setChallengeQuests(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getChallengeQuestsType():
        return MtBirthdayQuestModel

    def getIsQuestsError(self):
        return self._getBool(8)

    def setIsQuestsError(self, value):
        self._setBool(8, value)
        return

    def getIsQuestGiverError(self):
        return self._getBool(9)

    def setIsQuestGiverError(self, value):
        self._setBool(9, value)
        return

    def getIsSoundAnimationActive(self):
        return self._getBool(10)

    def setIsSoundAnimationActive(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(QuestsGiverViewModel, self)._initialize()
        self._addNumberProperty(b'timeUpdate', 1000000)
        self._addNumberProperty(b'timeNewQuest', 1000000)
        self._addNumberProperty(b'defaultTab', 0)
        self._addArrayProperty(b'battleTypes', Array())
        self._addNumberProperty(b'minLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addArrayProperty(b'assignmentsQuests', Array())
        self._addArrayProperty(b'challengeQuests', Array())
        self._addBoolProperty(b'isQuestsError', False)
        self._addBoolProperty(b'isQuestGiverError', False)
        self._addBoolProperty(b'isSoundAnimationActive', False)
        self.onTabVisited = self._addCommand(b'onTabVisited')
        self.onSoundClick = self._addCommand(b'onSoundClick')
        self.onTabActivate = self._addCommand(b'onTabActivate')
        return
