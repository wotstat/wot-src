from enum import IntEnum
from gui.impl.gen.view_models.views.lobby.comp7.division_info_model import DivisionInfoModel
from gui.impl.gen.view_models.views.lobby.comp7.qualification_model import QualificationModel
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_base_widget_model import ModeSelectorBaseWidgetModel

class Rank(IntEnum):
    FIRST = 6
    SECOND = 5
    THIRD = 4
    FOURTH = 3
    FIFTH = 2
    SIXTH = 1


class ModeSelectorComp7WidgetModel(ModeSelectorBaseWidgetModel):
    __slots__ = (b'onOpenMeta',)

    def __init__(self, properties=9, commands=1):
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

    def getRank(self):
        return Rank(self._getNumber(3))

    def setRank(self, value):
        self._setNumber(3, value.value)
        return

    def getCurrentScore(self):
        return self._getNumber(4)

    def setCurrentScore(self, value):
        self._setNumber(4, value)
        return

    def getPrevScore(self):
        return self._getNumber(5)

    def setPrevScore(self, value):
        self._setNumber(5, value)
        return

    def getRankInactivityCount(self):
        return self._getNumber(6)

    def setRankInactivityCount(self, value):
        self._setNumber(6, value)
        return

    def getHasRankInactivityWarning(self):
        return self._getBool(7)

    def setHasRankInactivityWarning(self, value):
        self._setBool(7, value)
        return

    def getMyPosition(self):
        return self._getNumber(8)

    def setMyPosition(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(ModeSelectorComp7WidgetModel, self)._initialize()
        self._addViewModelProperty(b'divisionInfo', DivisionInfoModel())
        self._addViewModelProperty(b'qualificationModel', QualificationModel())
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'currentScore', 0)
        self._addNumberProperty(b'prevScore', 0)
        self._addNumberProperty(b'rankInactivityCount', -1)
        self._addBoolProperty(b'hasRankInactivityWarning', False)
        self._addNumberProperty(b'myPosition', -1)
        self.onOpenMeta = self._addCommand(b'onOpenMeta')
        return
