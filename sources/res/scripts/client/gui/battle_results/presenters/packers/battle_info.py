from gui.battle_results.pbs_helpers.common import getArenaNameStr, getRegularFinishResultResource
from gui.battle_results.presenters.packers.interfaces import IBattleResultsPacker
from gui.battle_results.settings import BATTLE_RESULTS_RECORD as _RECORD

class BattleInfo(IBattleResultsPacker):

    @classmethod
    def packModel(cls, model, battleResults):
        reusable, results = battleResults.reusable, battleResults.results
        model.setArenaName(getArenaNameStr(reusable))
        common = results[_RECORD.COMMON]
        model.setBattleStartTime(common[b'arenaCreateTime'])
        model.setBattleDuration(common[b'duration'])
        cls._packTeamResult(model, reusable, results)
        return

    @classmethod
    def _packTeamResult(cls, model, reusable, results):
        model.setWinStatus(cls._getWinStatus(reusable, results))
        model.setFinishReason(cls._getFinishReasonResource(reusable, results))
        return

    @classmethod
    def _getFinishReasonResource(cls, reusable, results):
        return getRegularFinishResultResource(reusable.common.finishReason, reusable.getPersonalTeamResult())

    @classmethod
    def _getWinStatus(cls, reusable, results):
        return reusable.getPersonalTeamResult()
