import typing
from collections import namedtuple
from frameworks.wulf import ViewModel
if typing.TYPE_CHECKING:
    from gui.battle_results.reusable import _ReusableInfo
    BattleResultsModelType = typing.TypeVar(b'BattleResultsModelType', bound=ViewModel)
    TooltipModelType = typing.TypeVar(b'TooltipModelType', bound=ViewModel)
BattleResults = namedtuple(b'BattleResults', (b'results', b'reusable'))

class IBattleResultStatsCtrl(object):
    CTRL_IMPL_TYPE_GAMEFACE = 0
    CTRL_IMPL_TYPE_FLASH = 1

    def clear(self):
        raise NotImplementedError
        return

    @property
    def ctrlImplType(self):
        return self.CTRL_IMPL_TYPE_FLASH

    def setResults(self, results, reusable):
        raise NotImplementedError
        return

    def getResults(self):
        return

    def getVO(self):
        raise NotImplementedError
        return

    def onResultsPosted(self, arenaUniqueID):
        raise NotImplementedError
        return

    @staticmethod
    def onShowResults(arenaUniqueID):
        raise NotImplementedError
        return

    @classmethod
    def representativeArenaBonusType(cls):
        return
