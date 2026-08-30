from enum import Enum
from frameworks.wulf import Array, ViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.detailed_stat_model import DetailedStatModel

class StatEnum(Enum):
    MISSIONS = b'missions'
    ASSIST = b'assist'
    KILLS = b'kills'
    DAMAGE = b'damage'
    ARMOR_USE = b'armorUse'


class BattleResultStatTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BattleResultStatTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getStat(self):
        return StatEnum(self._getString(0))

    def setStat(self, value):
        self._setString(0, value.value)
        return

    def getDetailedStats(self):
        return self._getArray(1)

    def setDetailedStats(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getDetailedStatsType():
        return DetailedStatModel

    def getInfoList(self):
        return self._getArray(2)

    def setInfoList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getInfoListType():
        return unicode

    def _initialize(self):
        super(BattleResultStatTooltipModel, self)._initialize()
        self._addStringProperty(b'stat')
        self._addArrayProperty(b'detailedStats', Array())
        self._addArrayProperty(b'infoList', Array())
        return
