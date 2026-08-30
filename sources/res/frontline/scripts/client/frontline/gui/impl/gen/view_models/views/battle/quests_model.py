from frameworks.wulf import ViewModel

class QuestsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(QuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getDescription(self):
        return self._getString(0)

    def setDescription(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getProgressGoal(self):
        return self._getNumber(2)

    def setProgressGoal(self, value):
        self._setNumber(2, value)
        return

    def getProgressValue(self):
        return self._getNumber(3)

    def setProgressValue(self, value):
        self._setNumber(3, value)
        return

    def getIsCompleted(self):
        return self._getBool(4)

    def setIsCompleted(self, value):
        self._setBool(4, value)
        return

    def getIsObserver(self):
        return self._getBool(5)

    def setIsObserver(self, value):
        self._setBool(5, value)
        return

    def getBlockDescription(self):
        return self._getString(6)

    def setBlockDescription(self, value):
        self._setString(6, value)
        return

    def getDirectionName(self):
        return self._getString(7)

    def setDirectionName(self, value):
        self._setString(7, value)
        return

    def getButtonKey(self):
        return self._getString(8)

    def setButtonKey(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(QuestsModel, self)._initialize()
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'progressGoal', 1)
        self._addNumberProperty(b'progressValue', 0)
        self._addBoolProperty(b'isCompleted', False)
        self._addBoolProperty(b'isObserver', False)
        self._addStringProperty(b'blockDescription', b'')
        self._addStringProperty(b'directionName', b'')
        self._addStringProperty(b'buttonKey', b'')
        return
