from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_books_button_model import CrewBooksButtonModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_operations_button_model import CrewOperationsButtonModel
from gui.impl.gen.view_models.views.lobby.crew.common.toggle_button_model import ToggleButtonModel

class ButtonsBarModel(ViewModel):
    __slots__ = (b'onCrewBooksClick', b'onAcceleratedTrainingClick', b'onWotPlusClick')

    def __init__(self, properties=5, commands=3):
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
    def acceleratedTraining(self):
        return self._getViewModel(2)

    @staticmethod
    def getAcceleratedTrainingType():
        return ToggleButtonModel

    @property
    def wotPlus(self):
        return self._getViewModel(3)

    @staticmethod
    def getWotPlusType():
        return ToggleButtonModel

    def getIsVisible(self):
        return self._getBool(4)

    def setIsVisible(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(ButtonsBarModel, self)._initialize()
        self._addViewModelProperty(b'crewOperations', CrewOperationsButtonModel())
        self._addViewModelProperty(b'crewBooks', CrewBooksButtonModel())
        self._addViewModelProperty(b'acceleratedTraining', ToggleButtonModel())
        self._addViewModelProperty(b'wotPlus', ToggleButtonModel())
        self._addBoolProperty(b'isVisible', True)
        self.onCrewBooksClick = self._addCommand(b'onCrewBooksClick')
        self.onAcceleratedTrainingClick = self._addCommand(b'onAcceleratedTrainingClick')
        self.onWotPlusClick = self._addCommand(b'onWotPlusClick')
        return
