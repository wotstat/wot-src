from enum import IntEnum
from frameworks.wulf import ViewModel

class SwitcherType(IntEnum):
    DIGITAL = 0
    TEXT = 1


class ProgressionStylesBuyingPanelModel(ViewModel):
    __slots__ = (b'onChange',)

    def __init__(self, properties=8, commands=1):
        super(ProgressionStylesBuyingPanelModel, self).__init__(properties=properties, commands=commands)
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

    def getIsReady(self):
        return self._getBool(2)

    def setIsReady(self, value):
        self._setBool(2, value)
        return

    def getNumberOfBullets(self):
        return self._getNumber(3)

    def setNumberOfBullets(self, value):
        self._setNumber(3, value)
        return

    def getIsBulletsBeforeCurrentDisabled(self):
        return self._getBool(4)

    def setIsBulletsBeforeCurrentDisabled(self, value):
        self._setBool(4, value)
        return

    def getSwitcherType(self):
        return SwitcherType(self._getNumber(5))

    def setSwitcherType(self, value):
        self._setNumber(5, value.value)
        return

    def getStyleID(self):
        return self._getNumber(6)

    def setStyleID(self, value):
        self._setNumber(6, value)
        return

    def getNotificationText(self):
        return self._getString(7)

    def setNotificationText(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(ProgressionStylesBuyingPanelModel, self)._initialize()
        self._addNumberProperty(b'currentLevel', 1)
        self._addNumberProperty(b'selectedLevel', 1)
        self._addBoolProperty(b'isReady', False)
        self._addNumberProperty(b'numberOfBullets', 4)
        self._addBoolProperty(b'isBulletsBeforeCurrentDisabled', True)
        self._addNumberProperty(b'switcherType')
        self._addNumberProperty(b'styleID', 0)
        self._addStringProperty(b'notificationText', b'')
        self.onChange = self._addCommand(b'onChange')
        return
