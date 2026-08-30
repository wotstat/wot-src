from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_question_model import MapBoxQuestionModel

class MapBoxSurveyViewModel(ViewModel):
    __slots__ = (b'onClose', b'onAnswerQuestion', b'onShowPreviousPage', b'onShowNextPage', b'onReady')

    def __init__(self, properties=7, commands=5):
        super(MapBoxSurveyViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def question(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestionType():
        return MapBoxQuestionModel

    def getMapId(self):
        return self._getString(1)

    def setMapId(self, value):
        self._setString(1, value)
        return

    def getSurveyGroup(self):
        return self._getString(2)

    def setSurveyGroup(self, value):
        self._setString(2, value)
        return

    def getCurrentPage(self):
        return self._getNumber(3)

    def setCurrentPage(self, value):
        self._setNumber(3, value)
        return

    def getTotalPagesCount(self):
        return self._getNumber(4)

    def setTotalPagesCount(self, value):
        self._setNumber(4, value)
        return

    def getIsSurveyFinish(self):
        return self._getBool(5)

    def setIsSurveyFinish(self, value):
        self._setBool(5, value)
        return

    def getCanContinue(self):
        return self._getBool(6)

    def setCanContinue(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(MapBoxSurveyViewModel, self)._initialize()
        self._addViewModelProperty(b'question', MapBoxQuestionModel())
        self._addStringProperty(b'mapId', b'')
        self._addStringProperty(b'surveyGroup', b'')
        self._addNumberProperty(b'currentPage', 0)
        self._addNumberProperty(b'totalPagesCount', 0)
        self._addBoolProperty(b'isSurveyFinish', False)
        self._addBoolProperty(b'canContinue', False)
        self.onClose = self._addCommand(b'onClose')
        self.onAnswerQuestion = self._addCommand(b'onAnswerQuestion')
        self.onShowPreviousPage = self._addCommand(b'onShowPreviousPage')
        self.onShowNextPage = self._addCommand(b'onShowNextPage')
        self.onReady = self._addCommand(b'onReady')
        return
