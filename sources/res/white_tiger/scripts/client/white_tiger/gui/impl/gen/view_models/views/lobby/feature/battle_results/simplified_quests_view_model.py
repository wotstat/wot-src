from frameworks.wulf import ViewModel

class SimplifiedQuestsViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(SimplifiedQuestsViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getString(0)

    def setIcon(self, value):
        self._setString(0, value)
        return

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getIsCompleted(self):
        return self._getBool(2)

    def setIsCompleted(self, value):
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

    def getLastProgressValue(self):
        return self._getNumber(5)

    def setLastProgressValue(self, value):
        self._setNumber(5, value)
        return

    def getIsSpecialMission(self):
        return self._getBool(6)

    def setIsSpecialMission(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(SimplifiedQuestsViewModel, self)._initialize()
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'description', b'')
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addNumberProperty(b'lastProgressValue', 0)
        self._addBoolProperty(b'isSpecialMission', False)
        return
