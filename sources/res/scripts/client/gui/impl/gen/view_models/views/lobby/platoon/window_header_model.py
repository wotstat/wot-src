from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.bonus_model import BonusModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel
from gui.impl.gen.view_models.views.lobby.platoon.mute_all_toggle_model import MuteAllToggleModel
from gui.impl.gen.view_models.views.lobby.platoon.no_bonus_placeholder_model import NoBonusPlaceholderModel

class WindowHeaderModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(WindowHeaderModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def noBonusPlaceholder(self):
        return self._getViewModel(0)

    @staticmethod
    def getNoBonusPlaceholderType():
        return NoBonusPlaceholderModel

    @property
    def btnLeavePlatoon(self):
        return self._getViewModel(1)

    @staticmethod
    def getBtnLeavePlatoonType():
        return ButtonModel

    @property
    def btnMuteAll(self):
        return self._getViewModel(2)

    @staticmethod
    def getBtnMuteAllType():
        return MuteAllToggleModel

    def getBackgroundImage(self):
        return self._getString(3)

    def setBackgroundImage(self, value):
        self._setString(3, value)
        return

    def getShowNoBonusPlaceholder(self):
        return self._getBool(4)

    def setShowNoBonusPlaceholder(self, value):
        self._setBool(4, value)
        return

    def getShowInfoIcon(self):
        return self._getBool(5)

    def setShowInfoIcon(self, value):
        self._setBool(5, value)
        return

    def getBonuses(self):
        return self._getArray(6)

    def setBonuses(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(WindowHeaderModel, self)._initialize()
        self._addViewModelProperty(b'noBonusPlaceholder', NoBonusPlaceholderModel())
        self._addViewModelProperty(b'btnLeavePlatoon', ButtonModel())
        self._addViewModelProperty(b'btnMuteAll', MuteAllToggleModel())
        self._addStringProperty(b'backgroundImage', b'')
        self._addBoolProperty(b'showNoBonusPlaceholder', False)
        self._addBoolProperty(b'showInfoIcon', False)
        self._addArrayProperty(b'bonuses', Array())
        return
