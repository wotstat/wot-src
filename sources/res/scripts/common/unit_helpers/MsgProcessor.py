from __future__ import absolute_import
from debug_utils import LOG_DEBUG_DEV
from ops_pack import OpsPacker, OpsUnpacker, initOpsFormatDef

class CBM_OP:
    SET_ROUND = 0
    SET_RESULTS = 2
    SET_ENEMY_READY = 3


class ClanBattleMgrMsgProcessor(OpsUnpacker):
    _opsFormatDefs = initOpsFormatDef({(CBM_OP.SET_ROUND): (b'B', b'_setRound'), 
       (CBM_OP.SET_RESULTS): (b'b', b'_setResults'), 
       (CBM_OP.SET_ENEMY_READY): (b'B', b'_setEnemyReady')})

    def __init__(self, unit):
        self._unit = unit
        return

    def _setRound(self, isBattleRound):
        LOG_DEBUG_DEV(b'ClanBattleMgrMsgProcessor._setRound: ', isBattleRound)
        extras = self._unit._extras
        extras[b'isBattleRound'] = int(isBattleRound)
        return

    def _setResults(self, result):
        LOG_DEBUG_DEV(b'ClanBattleMgrMsgProcessor._setResults: res=', result)
        extras = self._unit._extras
        extras[b'battleResultList'].append(result)
        return

    def _setEnemyReady(self, enemyReady):
        LOG_DEBUG_DEV(b'ClanBattleMgrMsgProcessor._setEnemyReady: enemyReady=', enemyReady)
        extras = self._unit._extras
        extras[b'isEnemyReadyForBattle'] = enemyReady
        return


class ClanBattleMgrOpsPacker(OpsPacker, ClanBattleMgrMsgProcessor):
    pass
