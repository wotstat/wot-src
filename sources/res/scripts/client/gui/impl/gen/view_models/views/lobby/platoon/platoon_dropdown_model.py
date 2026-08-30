from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class PlatoonDropdownModel(ViewModel):
    __slots__ = (b'onOutsideClick',)

    def __init__(self, properties=10, commands=1):
        super(PlatoonDropdownModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def findPlatoon(self):
        return self._getViewModel(0)

    @staticmethod
    def getFindPlatoonType():
        return ButtonModel

    @property
    def createPlatoon(self):
        return self._getViewModel(1)

    @staticmethod
    def getCreatePlatoonType():
        return ButtonModel

    @property
    def createPlatoonForTwo(self):
        return self._getViewModel(2)

    @staticmethod
    def getCreatePlatoonForTwoType():
        return ButtonModel

    @property
    def createPlatoonForSeven(self):
        return self._getViewModel(3)

    @staticmethod
    def getCreatePlatoonForSevenType():
        return ButtonModel

    def getBattleType(self):
        return self._getString(4)

    def setBattleType(self, value):
        self._setString(4, value)
        return

    def getIsSettingsVisible(self):
        return self._getBool(5)

    def setIsSettingsVisible(self, value):
        self._setBool(5, value)
        return

    def getHasXpBonus(self):
        return self._getBool(6)

    def setHasXpBonus(self, value):
        self._setBool(6, value)
        return

    def getHasCreditsBonus(self):
        return self._getBool(7)

    def setHasCreditsBonus(self, value):
        self._setBool(7, value)
        return

    def getIsRibbonVisible(self):
        return self._getBool(8)

    def setIsRibbonVisible(self, value):
        self._setBool(8, value)
        return

    def getBackgroundImage(self):
        return self._getString(9)

    def setBackgroundImage(self, value):
        self._setString(9, value)
        return

    def _initialize(self):
        super(PlatoonDropdownModel, self)._initialize()
        self._addViewModelProperty(b'findPlatoon', ButtonModel())
        self._addViewModelProperty(b'createPlatoon', ButtonModel())
        self._addViewModelProperty(b'createPlatoonForTwo', ButtonModel())
        self._addViewModelProperty(b'createPlatoonForSeven', ButtonModel())
        self._addStringProperty(b'battleType', b'')
        self._addBoolProperty(b'isSettingsVisible', False)
        self._addBoolProperty(b'hasXpBonus', False)
        self._addBoolProperty(b'hasCreditsBonus', False)
        self._addBoolProperty(b'isRibbonVisible', False)
        self._addStringProperty(b'backgroundImage', b'')
        self.onOutsideClick = self._addCommand(b'onOutsideClick')
        return
