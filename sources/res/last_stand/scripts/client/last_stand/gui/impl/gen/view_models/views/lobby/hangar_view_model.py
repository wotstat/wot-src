from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class HangarViewModel(RouterModel):
    __slots__ = (b'onAboutClick', b'onViewLoaded', b'onNarrationClick')

    def __init__(self, properties=7, commands=5):
        super(HangarViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsInfoEnabled(self):
        return self._getBool(2)

    def setIsInfoEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsLootBoxEntryPointEnabled(self):
        return self._getBool(3)

    def setIsLootBoxEntryPointEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsLoadedSetup(self):
        return self._getBool(4)

    def setIsLoadedSetup(self, value):
        self._setBool(4, value)
        return

    def getSelectedStory(self):
        return self._getNumber(5)

    def setSelectedStory(self, value):
        self._setNumber(5, value)
        return

    def getShowDailyAnim(self):
        return self._getBool(6)

    def setShowDailyAnim(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(HangarViewModel, self)._initialize()
        self._addBoolProperty(b'isInfoEnabled', False)
        self._addBoolProperty(b'isLootBoxEntryPointEnabled', False)
        self._addBoolProperty(b'isLoadedSetup', False)
        self._addNumberProperty(b'selectedStory', 0)
        self._addBoolProperty(b'showDailyAnim', False)
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onNarrationClick = self._addCommand(b'onNarrationClick')
        return
