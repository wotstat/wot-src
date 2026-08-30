from frameworks.wulf import Array, ViewModel

class ProgressiveRewardViewModel(ViewModel):
    __slots__ = (b'onCloseAction', b'onDestroyEvent')

    def __init__(self, properties=4, commands=2):
        super(ProgressiveRewardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSteps(self):
        return self._getArray(0)

    def setSteps(self, value):
        self._setArray(0, value)
        return

    def getStepIdx(self):
        return self._getNumber(1)

    def setStepIdx(self, value):
        self._setNumber(1, value)
        return

    def getHardReset(self):
        return self._getBool(2)

    def setHardReset(self, value):
        self._setBool(2, value)
        return

    def getFadeOut(self):
        return self._getBool(3)

    def setFadeOut(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ProgressiveRewardViewModel, self)._initialize()
        self._addArrayProperty(b'steps', Array())
        self._addNumberProperty(b'stepIdx', 0)
        self._addBoolProperty(b'hardReset', False)
        self._addBoolProperty(b'fadeOut', False)
        self.onCloseAction = self._addCommand(b'onCloseAction')
        self.onDestroyEvent = self._addCommand(b'onDestroyEvent')
        return
