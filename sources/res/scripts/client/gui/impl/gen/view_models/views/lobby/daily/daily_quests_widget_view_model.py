from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.daily.widget_quest_model import WidgetQuestModel

class DailyQuestsWidgetViewModel(ViewModel):
    __slots__ = (b'onQuestClick', b'onDisappear')

    def __init__(self, properties=6, commands=2):
        super(DailyQuestsWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getQuestsType():
        return WidgetQuestModel

    def getPremiumQuests(self):
        return self._getArray(1)

    def setPremiumQuests(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getPremiumQuestsType():
        return WidgetQuestModel

    def getSerialEnterQuests(self):
        return self._getArray(2)

    def setSerialEnterQuests(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSerialEnterQuestsType():
        return WidgetQuestModel

    def getCountdown(self):
        return self._getNumber(3)

    def setCountdown(self, value):
        self._setNumber(3, value)
        return

    def getVisible(self):
        return self._getBool(4)

    def setVisible(self, value):
        self._setBool(4, value)
        return

    def getIndicateCompleteQuests(self):
        return self._getArray(5)

    def setIndicateCompleteQuests(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getIndicateCompleteQuestsType():
        return bool

    def _initialize(self):
        super(DailyQuestsWidgetViewModel, self)._initialize()
        self._addArrayProperty(b'quests', Array())
        self._addArrayProperty(b'premiumQuests', Array())
        self._addArrayProperty(b'serialEnterQuests', Array())
        self._addNumberProperty(b'countdown', 0)
        self._addBoolProperty(b'visible', False)
        self._addArrayProperty(b'indicateCompleteQuests', Array())
        self.onQuestClick = self._addCommand(b'onQuestClick')
        self.onDisappear = self._addCommand(b'onDisappear')
        return
