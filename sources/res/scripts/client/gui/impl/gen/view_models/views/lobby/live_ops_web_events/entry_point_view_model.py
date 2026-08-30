from gui.impl.gen.view_models.views.lobby.live_ops_web_events.entry_point_base import EntryPointBase

class EntryPointViewModel(EntryPointBase):
    __slots__ = (b'onClick',)

    def __init__(self, properties=6, commands=1):
        super(EntryPointViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFirstEntry(self):
        return self._getBool(2)

    def setIsFirstEntry(self, value):
        self._setBool(2, value)
        return

    def getIsVisited(self):
        return self._getBool(3)

    def setIsVisited(self, value):
        self._setBool(3, value)
        return

    def getIsSmall(self):
        return self._getBool(4)

    def setIsSmall(self, value):
        self._setBool(4, value)
        return

    def getIsHighQualityPreset(self):
        return self._getBool(5)

    def setIsHighQualityPreset(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(EntryPointViewModel, self)._initialize()
        self._addBoolProperty(b'isFirstEntry', False)
        self._addBoolProperty(b'isVisited', False)
        self._addBoolProperty(b'isSmall', True)
        self._addBoolProperty(b'isHighQualityPreset', True)
        self.onClick = self._addCommand(b'onClick')
        return
