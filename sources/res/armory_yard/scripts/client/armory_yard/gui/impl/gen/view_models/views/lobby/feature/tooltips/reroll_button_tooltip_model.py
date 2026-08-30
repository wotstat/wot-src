from frameworks.wulf import ViewModel

class RerollButtonTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RerollButtonTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getFreeRerollCount(self):
        return self._getNumber(0)

    def setFreeRerollCount(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(RerollButtonTooltipModel, self)._initialize()
        self._addNumberProperty(b'freeRerollCount', 0)
        return
