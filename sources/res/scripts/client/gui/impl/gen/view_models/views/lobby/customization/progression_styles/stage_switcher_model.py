from enum import IntEnum
from frameworks.wulf import ViewModel

class SwitcherType(IntEnum):
    DIGITAL = 0
    TEXT = 1


class StageSwitcherModel(ViewModel):
    __slots__ = (b'onChange',)

    def __init__(self, properties=6, commands=1):
        super(StageSwitcherModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentLevel(self):
        return self._getNumber(0)

    def setCurrentLevel(self, value):
        self._setNumber(0, value)
        return

    def getSelectedLevel(self):
        return self._getNumber(1)

    def setSelectedLevel(self, value):
        self._setNumber(1, value)
        return

    def getNumberOfBullets(self):
        return self._getNumber(2)

    def setNumberOfBullets(self, value):
        self._setNumber(2, value)
        return

    def getIsBulletsBeforeCurrentDisabled(self):
        return self._getBool(3)

    def setIsBulletsBeforeCurrentDisabled(self, value):
        self._setBool(3, value)
        return

    def getSwitcherType(self):
        return SwitcherType(self._getNumber(4))

    def setSwitcherType(self, value):
        self._setNumber(4, value.value)
        return

    def getStyleID(self):
        return self._getNumber(5)

    def setStyleID(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(StageSwitcherModel, self)._initialize()
        self._addNumberProperty(b'currentLevel', 0)
        self._addNumberProperty(b'selectedLevel', 0)
        self._addNumberProperty(b'numberOfBullets', 4)
        self._addBoolProperty(b'isBulletsBeforeCurrentDisabled', True)
        self._addNumberProperty(b'switcherType')
        self._addNumberProperty(b'styleID', 0)
        self.onChange = self._addCommand(b'onChange')
        return
