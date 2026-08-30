from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class ProgressiveRewardAwardModel(ViewModel):
    __slots__ = (b'onCloseAction', b'onSpecialActionBtnClick', b'onDestroyEvent')

    def __init__(self, properties=8, commands=3):
        super(ProgressiveRewardAwardModel, self).__init__(properties=properties, commands=commands)
        return

    def getAwardType(self):
        return self._getString(0)

    def setAwardType(self, value):
        self._setString(0, value)
        return

    def getSteps(self):
        return self._getArray(1)

    def setSteps(self, value):
        self._setArray(1, value)
        return

    def getStepIdx(self):
        return self._getNumber(2)

    def setStepIdx(self, value):
        self._setNumber(2, value)
        return

    def getHardReset(self):
        return self._getBool(3)

    def setHardReset(self, value):
        self._setBool(3, value)
        return

    def getFadeOut(self):
        return self._getBool(4)

    def setFadeOut(self, value):
        self._setBool(4, value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    def getSpecialRewardType(self):
        return self._getString(6)

    def setSpecialRewardType(self, value):
        self._setString(6, value)
        return

    def getInitialCongratsType(self):
        return self._getString(7)

    def setInitialCongratsType(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(ProgressiveRewardAwardModel, self)._initialize()
        self._addStringProperty(b'awardType', b'')
        self._addArrayProperty(b'steps', Array())
        self._addNumberProperty(b'stepIdx', 0)
        self._addBoolProperty(b'hardReset', False)
        self._addBoolProperty(b'fadeOut', False)
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'specialRewardType', b'')
        self._addStringProperty(b'initialCongratsType', b'')
        self.onCloseAction = self._addCommand(b'onCloseAction')
        self.onSpecialActionBtnClick = self._addCommand(b'onSpecialActionBtnClick')
        self.onDestroyEvent = self._addCommand(b'onDestroyEvent')
        return
