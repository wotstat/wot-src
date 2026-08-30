from frameworks.wulf import ViewModel

class QuestDescrModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(QuestDescrModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuestName(self):
        return self._getString(0)

    def setQuestName(self, value):
        self._setString(0, value)
        return

    def getConditions(self):
        return self._getString(1)

    def setConditions(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(QuestDescrModel, self)._initialize()
        self._addStringProperty(b'questName', b'')
        self._addStringProperty(b'conditions', b'')
        return
