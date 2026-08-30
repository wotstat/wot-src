from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank, SeasonName
from comp7.gui.impl.gen.view_models.views.lobby.division_info_model import DivisionInfoModel
from comp7.gui.impl.gen.view_models.views.lobby.qualification_model import QualificationModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class ModeSelectorComp7WidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = (b'onOpenMeta',)

    def __init__(self, properties=10, commands=1):
        super(ModeSelectorComp7WidgetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def divisionInfo(self):
        return self._getViewModel(1)

    @staticmethod
    def getDivisionInfoType():
        return DivisionInfoModel

    @property
    def qualificationModel(self):
        return self._getViewModel(2)

    @staticmethod
    def getQualificationModelType():
        return QualificationModel

    def getSeasonName(self):
        return SeasonName(self._getString(3))

    def setSeasonName(self, value):
        self._setString(3, value.value)
        return

    def getRank(self):
        return Rank(self._getNumber(4))

    def setRank(self, value):
        self._setNumber(4, value.value)
        return

    def getCurrentScore(self):
        return self._getNumber(5)

    def setCurrentScore(self, value):
        self._setNumber(5, value)
        return

    def getPrevScore(self):
        return self._getNumber(6)

    def setPrevScore(self, value):
        self._setNumber(6, value)
        return

    def getTopPercentage(self):
        return self._getNumber(7)

    def setTopPercentage(self, value):
        self._setNumber(7, value)
        return

    def getRankInactivityCount(self):
        return self._getNumber(8)

    def setRankInactivityCount(self, value):
        self._setNumber(8, value)
        return

    def getHasRankInactivity(self):
        return self._getBool(9)

    def setHasRankInactivity(self, value):
        self._setBool(9, value)
        return

    def _initialize(self):
        super(ModeSelectorComp7WidgetModel, self)._initialize()
        self._addViewModelProperty(b'divisionInfo', DivisionInfoModel())
        self._addViewModelProperty(b'qualificationModel', QualificationModel())
        self._addStringProperty(b'seasonName')
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'currentScore', 0)
        self._addNumberProperty(b'prevScore', 0)
        self._addNumberProperty(b'topPercentage', 0)
        self._addNumberProperty(b'rankInactivityCount', -1)
        self._addBoolProperty(b'hasRankInactivity', False)
        self.onOpenMeta = self._addCommand(b'onOpenMeta')
        return
