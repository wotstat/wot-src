from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.widget.widget_quest_model import WidgetQuestModel

class ProgressionQuestsModel(ViewModel):
    __slots__ = (b'onMissionClick', b'onMarkAsViewed')

    def __init__(self, properties=2, commands=2):
        super(ProgressionQuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuests(self):
        return self._getArray(0)

    def setQuests(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getQuestsType():
        return WidgetQuestModel

    def getIsMissionsEnable(self):
        return self._getBool(1)

    def setIsMissionsEnable(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(ProgressionQuestsModel, self)._initialize()
        self._addArrayProperty(b'quests', Array())
        self._addBoolProperty(b'isMissionsEnable', True)
        self.onMissionClick = self._addCommand(b'onMissionClick')
        self.onMarkAsViewed = self._addCommand(b'onMarkAsViewed')
        return
