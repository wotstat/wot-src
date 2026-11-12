from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel

class NyQuestsViewModel(ViewModel):
    __slots__ = (b'onTypeSelect', b'onStartStopPersonVoice', b'changePersonVoicesEnabled', b'onInfoClick')

    def __init__(self, properties=10, commands=4):
        super(NyQuestsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentTabIdx(self):
        return self._getNumber(0)

    def setCurrentTabIdx(self, value):
        self._setNumber(0, value)
        return

    def getFirstSeenNewBonusMissions(self):
        return self._getBool(1)

    def setFirstSeenNewBonusMissions(self, value):
        self._setBool(1, value)
        return

    def getQuests(self):
        return self._getArray(2)

    def setQuests(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getQuestsType():
        return DailyQuestModel

    def getCountDown(self):
        return self._getNumber(3)

    def setCountDown(self, value):
        self._setNumber(3, value)
        return

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

    def getPersonTextNumber(self):
        return self._getNumber(6)

    def setPersonTextNumber(self, value):
        self._setNumber(6, value)
        return

    def getIsPersonVoicesNowPlaying(self):
        return self._getBool(7)

    def setIsPersonVoicesNowPlaying(self, value):
        self._setBool(7, value)
        return

    def getIsPersonVoicesEnabled(self):
        return self._getBool(8)

    def setIsPersonVoicesEnabled(self, value):
        self._setBool(8, value)
        return

    def getBattleTypes(self):
        return self._getArray(9)

    def setBattleTypes(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getBattleTypesType():
        return unicode

    def _initialize(self):
        super(NyQuestsViewModel, self)._initialize()
        self._addNumberProperty(b'currentTabIdx', 0)
        self._addBoolProperty(b'firstSeenNewBonusMissions', False)
        self._addArrayProperty(b'quests', Array())
        self._addNumberProperty(b'countDown', 0)
        self._addNumberProperty(b'minLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addNumberProperty(b'personTextNumber', 1)
        self._addBoolProperty(b'isPersonVoicesNowPlaying', False)
        self._addBoolProperty(b'isPersonVoicesEnabled', False)
        self._addArrayProperty(b'battleTypes', Array())
        self.onTypeSelect = self._addCommand(b'onTypeSelect')
        self.onStartStopPersonVoice = self._addCommand(b'onStartStopPersonVoice')
        self.changePersonVoicesEnabled = self._addCommand(b'changePersonVoicesEnabled')
        self.onInfoClick = self._addCommand(b'onInfoClick')
        return
