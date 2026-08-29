from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class Type(Enum):
    RANDOM = b'random'
    COMP7 = b'comp7'


class PlatoonDropdownModel(ViewModel):
    __slots__ = (b'onOutsideClick',)

    def __init__(self, properties=8, commands=1):
        super(PlatoonDropdownModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def btnFind(self):
        return self._getViewModel(0)

    @staticmethod
    def getBtnFindType():
        return ButtonModel

    @property
    def btnCreate(self):
        return self._getViewModel(1)

    @staticmethod
    def getBtnCreateType():
        return ButtonModel

    @property
    def btnCreateForTwo(self):
        return self._getViewModel(2)

    @staticmethod
    def getBtnCreateForTwoType():
        return ButtonModel

    def getType(self):
        return Type(self._getString(3))

    def setType(self, value):
        self._setString(3, value.value)
        return

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

    def getIsRibbonVisible(self):
        return self._getBool(6)

    def setIsRibbonVisible(self, value):
        self._setBool(6, value)
        return

    def getBackgroundImage(self):
        return self._getString(7)

    def setBackgroundImage(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(PlatoonDropdownModel, self)._initialize()
        self._addViewModelProperty(b'btnFind', ButtonModel())
        self._addViewModelProperty(b'btnCreate', ButtonModel())
        self._addViewModelProperty(b'btnCreateForTwo', ButtonModel())
        self._addStringProperty(b'type')
        self._addStringProperty(b'battleType', b'')
        self._addBoolProperty(b'isSettingsVisible', False)
        self._addBoolProperty(b'isRibbonVisible', False)
        self._addStringProperty(b'backgroundImage', b'')
        self.onOutsideClick = self._addCommand(b'onOutsideClick')
        return
