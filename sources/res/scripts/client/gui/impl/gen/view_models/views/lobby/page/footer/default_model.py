from frameworks.wulf import ViewModel

class DefaultModel(ViewModel):
    __slots__ = (b'onOpenGameMenu',)

    def __init__(self, properties=1, commands=1):
        super(DefaultModel, self).__init__(properties=properties, commands=commands)
        return

    def getOldStyle(self):
        return self._getBool(0)

    def setOldStyle(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(DefaultModel, self)._initialize()
        self._addBoolProperty(b'oldStyle', False)
        self.onOpenGameMenu = self._addCommand(b'onOpenGameMenu')
        return
