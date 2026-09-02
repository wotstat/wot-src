from frameworks.wulf import ViewModel

class BaseQuestModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(BaseQuestModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getAnimationId(self):
        return self._getString(1)

    def setAnimationId(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getDescription(self):
        return self._getString(3)

    def setDescription(self, value):
        self._setString(3, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(4)

    def setCurrentProgress(self, value):
        self._setNumber(4, value)
        return

    def getTotalProgress(self):
        return self._getNumber(5)

    def setTotalProgress(self, value):
        self._setNumber(5, value)
        return

    def getEarned(self):
        return self._getNumber(6)

    def setEarned(self, value):
        self._setNumber(6, value)
        return

    def getIsCompleted(self):
        return self._getBool(7)

    def setIsCompleted(self, value):
        self._setBool(7, value)
        return

    def getIsLocked(self):
        return self._getBool(8)

    def setIsLocked(self, value):
        self._setBool(8, value)
        return

    def getAnimateCompletion(self):
        return self._getBool(9)

    def setAnimateCompletion(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(BaseQuestModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'animationId', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addNumberProperty(b'earned', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isLocked', False)
        self._addBoolProperty(b'animateCompletion', False)
        return
