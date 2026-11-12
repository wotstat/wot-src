from frameworks.wulf import ViewModel

class NyProgressWidgetModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NyProgressWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getLevel(self):
        return self._getNumber(0)

    def setLevel(self, value):
        self._setNumber(0, value)
        return

    def getProgress(self):
        return self._getNumber(1)

    def setProgress(self, value):
        self._setNumber(1, value)
        return

    def getIsPlaceEntrance(self):
        return self._getBool(2)

    def setIsPlaceEntrance(self, value):
        self._setBool(2, value)
        return

    def getRewardsCount(self):
        return self._getNumber(3)

    def setRewardsCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(NyProgressWidgetModel, self)._initialize()
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'progress', 0)
        self._addBoolProperty(b'isPlaceEntrance', False)
        self._addNumberProperty(b'rewardsCount', 0)
        return
