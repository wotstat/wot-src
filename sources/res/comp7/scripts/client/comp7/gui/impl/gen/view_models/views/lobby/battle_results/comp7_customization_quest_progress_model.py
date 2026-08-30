from frameworks.wulf import ViewModel

class Comp7CustomizationQuestProgressModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(Comp7CustomizationQuestProgressModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsCompleted(self):
        return self._getBool(0)

    def setIsCompleted(self, value):
        self._setBool(0, value)
        return

    def getCurrentProgress(self):
        return self._getNumber(1)

    def setCurrentProgress(self, value):
        self._setNumber(1, value)
        return

    def getTotalProgress(self):
        return self._getNumber(2)

    def setTotalProgress(self, value):
        self._setNumber(2, value)
        return

    def getEarned(self):
        return self._getNumber(3)

    def setEarned(self, value):
        self._setNumber(3, value)
        return

    def getDescription(self):
        return self._getString(4)

    def setDescription(self, value):
        self._setString(4, value)
        return

    def getIconKey(self):
        return self._getString(5)

    def setIconKey(self, value):
        self._setString(5, value)
        return

    def getCustomizationId(self):
        return self._getNumber(6)

    def setCustomizationId(self, value):
        self._setNumber(6, value)
        return

    def getCustomizationIconKey(self):
        return self._getString(7)

    def setCustomizationIconKey(self, value):
        self._setString(7, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(8)

    def setProgressionLevel(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(Comp7CustomizationQuestProgressModel, self)._initialize()
        self._addBoolProperty(b'isCompleted', False)
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'totalProgress', 0)
        self._addNumberProperty(b'earned', 0)
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'iconKey', b'')
        self._addNumberProperty(b'customizationId', 0)
        self._addStringProperty(b'customizationIconKey', b'')
        self._addNumberProperty(b'progressionLevel', 0)
        return
