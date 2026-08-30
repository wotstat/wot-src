from frameworks.wulf import ViewModel

class QuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(QuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getQuestCondition(self):
        return self._getString(1)

    def setQuestCondition(self, value):
        self._setString(1, value)
        return

    def getSummary(self):
        return self._getString(2)

    def setSummary(self, value):
        self._setString(2, value)
        return

    def getQuestType(self):
        return self._getString(3)

    def setQuestType(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(QuestModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'questCondition', b'')
        self._addStringProperty(b'summary', b'')
        self._addStringProperty(b'questType', b'')
        return
