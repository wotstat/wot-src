from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.books_list_component_model import BooksListComponentModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.freeXp_book_component_model import FreeXpBookComponentModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.learning_results_component_model import LearningResultsComponentModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.mentoring_license_component_model import MentoringLicenseComponentModel
from gui.impl.gen.view_models.views.lobby.crew.quick_training.tips_list_component_model import TipsListComponentModel

class QuickTrainingViewModel(BaseCrewViewModel):
    __slots__ = (b'mouseLeave', b'goToProfile')

    def __init__(self, properties=14, commands=6):
        super(QuickTrainingViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def freeXp(self):
        return self._getViewModel(2)

    @staticmethod
    def getFreeXpType():
        return FreeXpBookComponentModel

    @property
    def books(self):
        return self._getViewModel(3)

    @staticmethod
    def getBooksType():
        return BooksListComponentModel

    @property
    def learningResults(self):
        return self._getViewModel(4)

    @staticmethod
    def getLearningResultsType():
        return LearningResultsComponentModel

    @property
    def tips(self):
        return self._getViewModel(5)

    @staticmethod
    def getTipsType():
        return TipsListComponentModel

    @property
    def mentoringLicense(self):
        return self._getViewModel(6)

    @staticmethod
    def getMentoringLicenseType():
        return MentoringLicenseComponentModel

    def getNationName(self):
        return self._getString(7)

    def setNationName(self, value):
        self._setString(7, value)
        return

    def getVehicleName(self):
        return self._getString(8)

    def setVehicleName(self, value):
        self._setString(8, value)
        return

    def getTankmanName(self):
        return self._getString(9)

    def setTankmanName(self, value):
        self._setString(9, value)
        return

    def getIsWholeCrewHasPerkLimit(self):
        return self._getBool(10)

    def setIsWholeCrewHasPerkLimit(self, value):
        self._setBool(10, value)
        return

    def getIsAnyTankmanHasPerkLimit(self):
        return self._getBool(11)

    def setIsAnyTankmanHasPerkLimit(self, value):
        self._setBool(11, value)
        return

    def getIsCurrentTankmanHasPerkLimit(self):
        return self._getBool(12)

    def setIsCurrentTankmanHasPerkLimit(self, value):
        self._setBool(12, value)
        return

    def getIsCurrentTankmanHasLowEfficiency(self):
        return self._getBool(13)

    def setIsCurrentTankmanHasLowEfficiency(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(QuickTrainingViewModel, self)._initialize()
        self._addViewModelProperty(b'freeXp', FreeXpBookComponentModel())
        self._addViewModelProperty(b'books', BooksListComponentModel())
        self._addViewModelProperty(b'learningResults', LearningResultsComponentModel())
        self._addViewModelProperty(b'tips', TipsListComponentModel())
        self._addViewModelProperty(b'mentoringLicense', MentoringLicenseComponentModel())
        self._addStringProperty(b'nationName', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'tankmanName', b'')
        self._addBoolProperty(b'isWholeCrewHasPerkLimit', False)
        self._addBoolProperty(b'isAnyTankmanHasPerkLimit', False)
        self._addBoolProperty(b'isCurrentTankmanHasPerkLimit', False)
        self._addBoolProperty(b'isCurrentTankmanHasLowEfficiency', False)
        self.mouseLeave = self._addCommand(b'mouseLeave')
        self.goToProfile = self._addCommand(b'goToProfile')
        return
