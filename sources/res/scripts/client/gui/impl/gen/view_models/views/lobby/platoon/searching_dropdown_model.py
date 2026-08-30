from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class SearchingDropdownModel(ViewModel):
    __slots__ = (b'onOutsideClick',)

    def __init__(self, properties=7, commands=1):
        super(SearchingDropdownModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def cancelSearch(self):
        return self._getViewModel(0)

    @staticmethod
    def getCancelSearchType():
        return ButtonModel

    def getBackgroundImage(self):
        return self._getString(1)

    def setBackgroundImage(self, value):
        self._setString(1, value)
        return

    def getSeekers(self):
        return self._getNumber(2)

    def setSeekers(self, value):
        self._setNumber(2, value)
        return

    def getSearchStartTime(self):
        return self._getNumber(3)

    def setSearchStartTime(self, value):
        self._setNumber(3, value)
        return

    def getEstimatedTime(self):
        return self._getString(4)

    def setEstimatedTime(self, value):
        self._setString(4, value)
        return

    def getHasXpBonus(self):
        return self._getBool(5)

    def setHasXpBonus(self, value):
        self._setBool(5, value)
        return

    def getHasCreditsBonus(self):
        return self._getBool(6)

    def setHasCreditsBonus(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(SearchingDropdownModel, self)._initialize()
        self._addViewModelProperty(b'cancelSearch', ButtonModel())
        self._addStringProperty(b'backgroundImage', b'')
        self._addNumberProperty(b'seekers', 0)
        self._addNumberProperty(b'searchStartTime', 0)
        self._addStringProperty(b'estimatedTime', b'')
        self._addBoolProperty(b'hasXpBonus', False)
        self._addBoolProperty(b'hasCreditsBonus', False)
        self.onOutsideClick = self._addCommand(b'onOutsideClick')
        return
