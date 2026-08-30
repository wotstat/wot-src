from frameworks.wulf import ViewModel

class PremiumQuestsModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=2, commands=1):
        super(PremiumQuestsModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEnabled(self):
        return self._getBool(0)

    def setIsEnabled(self, value):
        self._setBool(0, value)
        return

    def getCompletedMissionsCount(self):
        return self._getNumber(1)

    def setCompletedMissionsCount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(PremiumQuestsModel, self)._initialize()
        self._addBoolProperty(b'isEnabled', True)
        self._addNumberProperty(b'completedMissionsCount', -1)
        self.onClick = self._addCommand(b'onClick')
        return
