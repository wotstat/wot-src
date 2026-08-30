from frameworks.wulf import ViewModel

class StrongholdMainWidgetModel(ViewModel):
    __slots__ = (b'onOpenStrongholdEventProgression',)

    def __init__(self, properties=3, commands=1):
        super(StrongholdMainWidgetModel, self).__init__(properties=properties, commands=commands)
        return

    def getProgressionLevel(self):
        return self._getNumber(0)

    def setProgressionLevel(self, value):
        self._setNumber(0, value)
        return

    def getIsInClan(self):
        return self._getBool(1)

    def setIsInClan(self, value):
        self._setBool(1, value)
        return

    def getIsActive(self):
        return self._getBool(2)

    def setIsActive(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(StrongholdMainWidgetModel, self)._initialize()
        self._addNumberProperty(b'progressionLevel', 0)
        self._addBoolProperty(b'isInClan', False)
        self._addBoolProperty(b'isActive', False)
        self.onOpenStrongholdEventProgression = self._addCommand(b'onOpenStrongholdEventProgression')
        return
