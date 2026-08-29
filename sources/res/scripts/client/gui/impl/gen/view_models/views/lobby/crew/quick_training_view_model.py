from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.base_crew_view_model import BaseCrewViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.info_tip_model import InfoTipModel
from gui.impl.gen.view_models.views.lobby.crew.freeXp_book_model import FreeXpBookModel
from gui.impl.gen.view_models.views.lobby.crew.learning_data_model import LearningDataModel
from gui.impl.gen.view_models.views.lobby.crew.training_book_model import TrainingBookModel

class QuickTrainingViewModel(BaseCrewViewModel):
    __slots__ = (b'onLearn', b'onCancel', b'onBuyBook', b'onTipClose', b'onCardMouseLeave', b'onFreeXpMouseEnter', b'onFreeXpSelected', b'onFreeXpUpdated', b'onFreeXpManualInput', b'onBookMouseEnter', b'onBookSelected')

    def __init__(self, properties=9, commands=15):
        super(QuickTrainingViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def freeXpData(self):
        return self._getViewModel(2)

    @staticmethod
    def getFreeXpDataType():
        return FreeXpBookModel

    @property
    def learningData(self):
        return self._getViewModel(3)

    @staticmethod
    def getLearningDataType():
        return LearningDataModel

    def getNationName(self):
        return self._getString(4)

    def setNationName(self, value):
        self._setString(4, value)
        return

    def getVehicleName(self):
        return self._getString(5)

    def setVehicleName(self, value):
        self._setString(5, value)
        return

    def getTankmanName(self):
        return self._getString(6)

    def setTankmanName(self, value):
        self._setString(6, value)
        return

    def getBooksList(self):
        return self._getArray(7)

    def setBooksList(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getBooksListType():
        return TrainingBookModel

    def getTips(self):
        return self._getArray(8)

    def setTips(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getTipsType():
        return InfoTipModel

    def _initialize(self):
        super(QuickTrainingViewModel, self)._initialize()
        self._addViewModelProperty(b'freeXpData', FreeXpBookModel())
        self._addViewModelProperty(b'learningData', LearningDataModel())
        self._addStringProperty(b'nationName', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'tankmanName', b'')
        self._addArrayProperty(b'booksList', Array())
        self._addArrayProperty(b'tips', Array())
        self.onLearn = self._addCommand(b'onLearn')
        self.onCancel = self._addCommand(b'onCancel')
        self.onBuyBook = self._addCommand(b'onBuyBook')
        self.onTipClose = self._addCommand(b'onTipClose')
        self.onCardMouseLeave = self._addCommand(b'onCardMouseLeave')
        self.onFreeXpMouseEnter = self._addCommand(b'onFreeXpMouseEnter')
        self.onFreeXpSelected = self._addCommand(b'onFreeXpSelected')
        self.onFreeXpUpdated = self._addCommand(b'onFreeXpUpdated')
        self.onFreeXpManualInput = self._addCommand(b'onFreeXpManualInput')
        self.onBookMouseEnter = self._addCommand(b'onBookMouseEnter')
        self.onBookSelected = self._addCommand(b'onBookSelected')
        return
