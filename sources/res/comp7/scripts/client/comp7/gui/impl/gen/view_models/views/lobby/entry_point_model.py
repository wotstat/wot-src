from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank, SeasonName
from frameworks.wulf import ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.division_info_model import DivisionInfoModel
from comp7.gui.impl.gen.view_models.views.lobby.qualification_model import QualificationModel

class EntryPointModel(ViewModel):
    __slots__ = (b'onOpenMeta', b'onAnimationEnd', b'onEntryPointAnimationSeen')

    def __init__(self, properties=11, commands=3):
        super(EntryPointModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def divisionInfo(self):
        return self._getViewModel(0)

    @staticmethod
    def getDivisionInfoType():
        return DivisionInfoModel

    @property
    def qualificationModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getQualificationModelType():
        return QualificationModel

    def getSeasonName(self):
        return SeasonName(self._getString(2))

    def setSeasonName(self, value):
        self._setString(2, value.value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
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

    def getIsEntryPointAnimationSeen(self):
        return self._getBool(10)

    def setIsEntryPointAnimationSeen(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(EntryPointModel, self)._initialize()
        self._addViewModelProperty(b'divisionInfo', DivisionInfoModel())
        self._addViewModelProperty(b'qualificationModel', QualificationModel())
        self._addStringProperty(b'seasonName')
        self._addBoolProperty(b'isEnabled', False)
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'currentScore', 0)
        self._addNumberProperty(b'prevScore', 0)
        self._addNumberProperty(b'topPercentage', 0)
        self._addNumberProperty(b'rankInactivityCount', -1)
        self._addBoolProperty(b'hasRankInactivity', False)
        self._addBoolProperty(b'isEntryPointAnimationSeen', False)
        self.onOpenMeta = self._addCommand(b'onOpenMeta')
        self.onAnimationEnd = self._addCommand(b'onAnimationEnd')
        self.onEntryPointAnimationSeen = self._addCommand(b'onEntryPointAnimationSeen')
        return
