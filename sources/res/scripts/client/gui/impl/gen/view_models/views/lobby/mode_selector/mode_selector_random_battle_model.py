from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_normal_card_model import ModeSelectorNormalCardModel

class ModeSelectorRandomBattleModel(ModeSelectorNormalCardModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(ModeSelectorRandomBattleModel, self).__init__(properties=properties, commands=commands)
        return

    def getSettingsPopoverID(self):
        return self._getNumber(22)

    def setSettingsPopoverID(self, value):
        self._setNumber(22, value)
        return

    def getIsSettingsActive(self):
        return self._getBool(23)

    def setIsSettingsActive(self, value):
        self._setBool(23, value)
        return

    def getWithSettingsNotification(self):
        return self._getBool(24)

    def setWithSettingsNotification(self, value):
        self._setBool(24, value)
        return

    def _initialize(self):
        super(ModeSelectorRandomBattleModel, self)._initialize()
        self._addNumberProperty(b'settingsPopoverID', -1)
        self._addBoolProperty(b'isSettingsActive', False)
        self._addBoolProperty(b'withSettingsNotification', False)
        return
