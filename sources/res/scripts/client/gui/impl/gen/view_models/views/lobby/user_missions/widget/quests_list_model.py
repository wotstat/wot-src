from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel

class QuestsListModel(ViewModel):
    __slots__ = (b'onMissionClick', b'onMarkAsViewed')

    def __init__(self, properties=1, commands=2):
        super(QuestsListModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getQuestsType():
        return WidgetQuestModel

    def _initialize(self):
        super(QuestsListModel, self)._initialize()
        self._addArrayProperty(b'quests', Array())
        self.onMissionClick = self._addCommand(b'onMissionClick')
        self.onMarkAsViewed = self._addCommand(b'onMarkAsViewed')
        return
