from frameworks.wulf import ViewModel

class WidgetQuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(WidgetQuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getCompleted(self):
        return self._getBool(2)

    def setCompleted(self, value):
        self._setBool(2, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(3)

    def setCurrentProgress(self, value):
        self._setNumber(3, value)
        return

    def getTotalProgress(self):
        return self._getNumber(4)

    def setTotalProgress(self, value):
        self._setNumber(4, value)
        return

    def getHasPremium(self):
        return self._getBool(5)

    def setHasPremium(self, value):
        self._setBool(5, value)
        return

    def getIsPremium(self):
        return self._getBool(6)

    def setIsPremium(self, value):
        self._setBool(6, value)
        return

    def getEarned(self):
        return self._getNumber(7)

    def setEarned(self, value):
        self._setNumber(7, value)
        return

    def getDescription(self):
        return self._getString(8)

    def setDescription(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(WidgetQuestModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'icon', b'')
        self._addBoolProperty(b'completed', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addBoolProperty(b'hasPremium', False)
        self._addBoolProperty(b'isPremium', False)
        self._addNumberProperty(b'earned', 0)
        self._addStringProperty(b'description', b'')
        return
