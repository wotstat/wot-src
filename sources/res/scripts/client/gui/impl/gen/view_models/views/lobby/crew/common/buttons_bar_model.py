from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_books_button_model import CrewBooksButtonModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_operations_button_model import CrewOperationsButtonModel
from gui.impl.gen.view_models.views.lobby.crew.common.toggle_button_model import ToggleButtonModel

class ButtonsBarModel(ViewModel):
    __slots__ = (b'onCrewBooksClick', b'onWotPlusClick')

    def __init__(self, properties=4, commands=2):
        super(ButtonsBarModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def crewOperations(self):
        return self._getViewModel(0)

    @staticmethod
    def getCrewOperationsType():
        return CrewOperationsButtonModel

    @property
    def crewBooks(self):
        return self._getViewModel(1)

    @staticmethod
    def getCrewBooksType():
        return CrewBooksButtonModel

    @property
    def wotPlus(self):
        return self._getViewModel(2)

    @staticmethod
    def getWotPlusType():
        return ToggleButtonModel

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ButtonsBarModel, self)._initialize()
        self._addViewModelProperty(b'crewOperations', CrewOperationsButtonModel())
        self._addViewModelProperty(b'crewBooks', CrewBooksButtonModel())
        self._addViewModelProperty(b'wotPlus', ToggleButtonModel())
        self._addBoolProperty(b'isVisible', True)
        self.onCrewBooksClick = self._addCommand(b'onCrewBooksClick')
        self.onWotPlusClick = self._addCommand(b'onWotPlusClick')
        return
