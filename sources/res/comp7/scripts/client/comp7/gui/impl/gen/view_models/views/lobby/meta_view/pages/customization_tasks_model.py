from frameworks.wulf import ViewModel

class CustomizationTasksModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(CustomizationTasksModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconKey(self):
        return self._getString(0)

    def setIconKey(self, value):
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

    def getDelta(self):
        return self._getNumber(3)

    def setDelta(self, value):
        self._setNumber(3, value)
        return

    def getMaxProgress(self):
        return self._getNumber(4)

    def setMaxProgress(self, value):
        self._setNumber(4, value)
        return

    def getCustomizationId(self):
        return self._getNumber(5)

    def setCustomizationId(self, value):
        self._setNumber(5, value)
        return

    def getProgressionLevel(self):
        return self._getNumber(6)

    def setProgressionLevel(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(CustomizationTasksModel, self)._initialize()
        self._addStringProperty(b'iconKey', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'currentProgress', 0)
        self._addNumberProperty(b'delta', 0)
        self._addNumberProperty(b'maxProgress', 0)
        self._addNumberProperty(b'customizationId', 0)
        self._addNumberProperty(b'progressionLevel', 0)
        return
