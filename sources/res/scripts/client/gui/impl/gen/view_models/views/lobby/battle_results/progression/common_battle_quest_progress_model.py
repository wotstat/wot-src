from gui.impl.gen.view_models.common.missions.quest_model import QuestModel

class CommonBattleQuestProgressModel(QuestModel):
    __slots__ = ()

    def __init__(self, properties=19, commands=0):
        super(CommonBattleQuestProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(11)

    def setIcon(self, value):
        self._setString(11, value)
        return

    def getGuiDisabled(self):
        return self._getBool(12)

    def setGuiDisabled(self, value):
        self._setBool(12, value)
        return

    def getHidden(self):
        return self._getBool(13)

    def setHidden(self, value):
        self._setBool(13, value)
        return

    def getAvailable(self):
        return self._getBool(14)

    def setAvailable(self, value):
        self._setBool(14, value)
        return

    def getCurrentCompletionCount(self):
        return self._getNumber(15)

    def setCurrentCompletionCount(self, value):
        self._setNumber(15, value)
        return

    def getMaxCompletionCount(self):
        return self._getNumber(16)

    def setMaxCompletionCount(self, value):
        self._setNumber(16, value)
        return

    def getDefaultMaxCompletionCount(self):
        return self._getNumber(17)

    def setDefaultMaxCompletionCount(self, value):
        self._setNumber(17, value)
        return

    def getNavigationEnabled(self):
        return self._getBool(18)

    def setNavigationEnabled(self, value):
        self._setBool(18, value)
        return

    def _initialize(self):
        super(CommonBattleQuestProgressModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addBoolProperty(b'guiDisabled', False)
        self._addBoolProperty(b'hidden', False)
        self._addBoolProperty(b'available', False)
        self._addNumberProperty(b'currentCompletionCount', 0)
        self._addNumberProperty(b'maxCompletionCount', 1)
        self._addNumberProperty(b'defaultMaxCompletionCount', 1)
        self._addBoolProperty(b'navigationEnabled', False)
        return
