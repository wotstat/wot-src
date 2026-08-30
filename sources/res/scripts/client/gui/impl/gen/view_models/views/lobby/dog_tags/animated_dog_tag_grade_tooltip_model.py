from frameworks.wulf import ViewModel

class AnimatedDogTagGradeTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(AnimatedDogTagGradeTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getEngravingId(self):
        return self._getNumber(0)

    def setEngravingId(self, value):
        self._setNumber(0, value)
        return

    def getBackgroundId(self):
        return self._getNumber(1)

    def setBackgroundId(self, value):
        self._setNumber(1, value)
        return

    def getStage(self):
        return self._getNumber(2)

    def setStage(self, value):
        self._setNumber(2, value)
        return

    def getRequiredItemsCount(self):
        return self._getNumber(3)

    def setRequiredItemsCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(AnimatedDogTagGradeTooltipModel, self)._initialize()
        self._addNumberProperty(b'engravingId', 0)
        self._addNumberProperty(b'backgroundId', 0)
        self._addNumberProperty(b'stage', 0)
        self._addNumberProperty(b'requiredItemsCount', 0)
        return
