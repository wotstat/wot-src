from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.tooltips.quest_descr_model import QuestDescrModel

class QuestConditionsTooltipModel(ViewModel):
    __slots__ = ()
    MAX_QUESTS = 3

    def __init__(self, properties=2, commands=0):
        super(QuestConditionsTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getQuestsType():
        return QuestDescrModel

    def getTotalQuests(self):
        return self._getNumber(1)

    def setTotalQuests(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(QuestConditionsTooltipModel, self)._initialize()
        self._addArrayProperty(b'quests', Array())
        self._addNumberProperty(b'totalQuests', 0)
        return
