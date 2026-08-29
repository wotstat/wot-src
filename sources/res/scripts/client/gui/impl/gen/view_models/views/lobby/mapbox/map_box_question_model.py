from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_answers_model import MapBoxAnswersModel
from gui.impl.gen.view_models.views.lobby.mapbox.map_box_option_model import MapBoxOptionModel

class QuestionType(Enum):
    VEHICLE = b'vehicle'
    IMAGE = b'image'
    TABLE = b'table'
    INTERACTIVE_MAP = b'interactiveMap'
    TEXT = b'text'
    UNDEFINED = b'undefined'
    ALTERNATIVE = b'alternative'
    MULTIPLE_CHOICE = b'multipleChoice'


class MapBoxQuestionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(MapBoxQuestionModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def answers(self):
        return self._getViewModel(0)

    @staticmethod
    def getAnswersType():
        return MapBoxAnswersModel

    @property
    def options(self):
        return self._getViewModel(1)

    @staticmethod
    def getOptionsType():
        return MapBoxOptionModel

    def getType(self):
        return QuestionType(self._getString(2))

    def setType(self, value):
        self._setString(2, value.value)
        return

    def getImagePath(self):
        return self._getString(3)

    def setImagePath(self, value):
        self._setString(3, value)
        return

    def getPathPrefix(self):
        return self._getString(4)

    def setPathPrefix(self, value):
        self._setString(4, value)
        return

    def getShowIcons(self):
        return self._getBool(5)

    def setShowIcons(self, value):
        self._setBool(5, value)
        return

    def getQuestionId(self):
        return self._getString(6)

    def setQuestionId(self, value):
        self._setString(6, value)
        return

    def getTitleParams(self):
        return self._getArray(7)

    def setTitleParams(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getTitleParamsType():
        return unicode

    def _initialize(self):
        super(MapBoxQuestionModel, self)._initialize()
        self._addViewModelProperty(b'answers', MapBoxAnswersModel())
        self._addViewModelProperty(b'options', UserListModel())
        self._addStringProperty(b'type')
        self._addStringProperty(b'imagePath', b'')
        self._addStringProperty(b'pathPrefix', b'')
        self._addBoolProperty(b'showIcons', False)
        self._addStringProperty(b'questionId', b'')
        self._addArrayProperty(b'titleParams', Array())
        return
