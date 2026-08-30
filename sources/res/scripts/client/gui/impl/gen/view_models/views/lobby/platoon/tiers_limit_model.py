from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel
from gui.impl.gen.view_models.views.lobby.platoon.show_settings_button_model import ShowSettingsButtonModel

class TiersLimitModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(TiersLimitModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def btnResetSettings(self):
        return self._getViewModel(0)

    @staticmethod
    def getBtnResetSettingsType():
        return ButtonModel

    @property
    def btnShowSettings(self):
        return self._getViewModel(1)

    @staticmethod
    def getBtnShowSettingsType():
        return ShowSettingsButtonModel

    def getTiers(self):
        return self._getString(2)

    def setTiers(self, value):
        self._setString(2, value)
        return

    def getIsExpanded(self):
        return self._getBool(3)

    def setIsExpanded(self, value):
        self._setBool(3, value)
        return

    def getIsLight(self):
        return self._getBool(4)

    def setIsLight(self, value):
        self._setBool(4, value)
        return

    def getHasSettingsButton(self):
        return self._getBool(5)

    def setHasSettingsButton(self, value):
        self._setBool(5, value)
        return

    def getHasLookingForCaption(self):
        return self._getBool(6)

    def setHasLookingForCaption(self, value):
        self._setBool(6, value)
        return

    def getHasTiersCaption(self):
        return self._getBool(7)

    def setHasTiersCaption(self, value):
        self._setBool(7, value)
        return

    def getHasResetButton(self):
        return self._getBool(8)

    def setHasResetButton(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(TiersLimitModel, self)._initialize()
        self._addViewModelProperty(b'btnResetSettings', ButtonModel())
        self._addViewModelProperty(b'btnShowSettings', ShowSettingsButtonModel())
        self._addStringProperty(b'tiers', b'')
        self._addBoolProperty(b'isExpanded', False)
        self._addBoolProperty(b'isLight', False)
        self._addBoolProperty(b'hasSettingsButton', False)
        self._addBoolProperty(b'hasLookingForCaption', False)
        self._addBoolProperty(b'hasTiersCaption', False)
        self._addBoolProperty(b'hasResetButton', False)
        return
