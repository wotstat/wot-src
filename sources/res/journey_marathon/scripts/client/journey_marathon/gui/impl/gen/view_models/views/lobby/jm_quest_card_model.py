from frameworks.wulf import ViewModel

class JmQuestCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(JmQuestCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(2)

    def setCurrentProgress(self, value):
        self._setNumber(2, value)
        return

    def getTotalProgress(self):
        return self._getNumber(3)

    def setTotalProgress(self, value):
        self._setNumber(3, value)
        return

    def getEarnedProgress(self):
        return self._getNumber(4)

    def setEarnedProgress(self, value):
        self._setNumber(4, value)
        return

    def getReward(self):
        return self._getNumber(5)

    def setReward(self, value):
        self._setNumber(5, value)
        return

    def getIconKey(self):
        return self._getString(6)

    def setIconKey(self, value):
        self._setString(6, value)
        return

    def getIsCompleted(self):
        return self._getBool(7)

    def setIsCompleted(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(JmQuestCardModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addNumberProperty(b'earnedProgress', 0)
        self._addNumberProperty(b'reward', 0)
        self._addStringProperty(b'iconKey', b'')
        self._addBoolProperty(b'isCompleted', False)
        return
