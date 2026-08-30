from frameworks.wulf import ViewModel

class PostProgressionCompareModel(ViewModel):
    __slots__ = (b'onApplyAction', b'onCancelAction', b'onResetAction')

    def __init__(self, properties=2, commands=3):
        super(PostProgressionCompareModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasChanges(self):
        return self._getBool(0)

    def setHasChanges(self, value):
        self._setBool(0, value)
        return

    def getHasInitChanges(self):
        return self._getBool(1)

    def setHasInitChanges(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(PostProgressionCompareModel, self)._initialize()
        self._addBoolProperty(b'hasChanges', False)
        self._addBoolProperty(b'hasInitChanges', False)
        self.onApplyAction = self._addCommand(b'onApplyAction')
        self.onCancelAction = self._addCommand(b'onCancelAction')
        self.onResetAction = self._addCommand(b'onResetAction')
        return
