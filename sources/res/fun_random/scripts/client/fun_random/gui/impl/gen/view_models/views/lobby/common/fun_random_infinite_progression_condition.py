from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition

class FunRandomInfiniteProgressionCondition(FunRandomProgressionCondition):
    __slots__ = ()

    def __init__(self, properties=10, commands=0):
        super(FunRandomInfiniteProgressionCondition, self).__init__(properties=properties, commands=commands)
        return

    def getCompleteCount(self):
        return self._getNumber(8)

    def setCompleteCount(self, value):
        self._setNumber(8, value)
        return

    def getPrevCompleteCount(self):
        return self._getNumber(9)

    def setPrevCompleteCount(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(FunRandomInfiniteProgressionCondition, self)._initialize()
        self._addNumberProperty(b'completeCount', -1)
        self._addNumberProperty(b'prevCompleteCount', -1)
        return
