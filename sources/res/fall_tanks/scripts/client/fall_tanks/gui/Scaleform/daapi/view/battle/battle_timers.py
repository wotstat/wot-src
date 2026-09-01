from __future__ import absolute_import
from constants import ARENA_PERIOD
from gui.Scaleform.daapi.view.battle.shared.battle_timers import PreBattleTimer, BattleTimer

class FallTanksPreBattleTimer(PreBattleTimer):

    def _onHideAll(self, speed):
        super(FallTanksPreBattleTimer, self)._onHideAll(speed)
        self.as_setWinConditionTextS(b'')
        self.as_setMessageS(b'')
        return


class FallTanksBattleTimer(BattleTimer):

    def __init__(self):
        super(FallTanksBattleTimer, self).__init__()
        self.__period = ARENA_PERIOD.IDLE
        return

    def setPeriod(self, period):
        self.__period = period
        return

    def hideTotalTime(self):
        return

    def _sendTime(self, totalTime):
        if self.__period == ARENA_PERIOD.BATTLE:
            totalTime = self.getRoundLength() - totalTime
        super(FallTanksBattleTimer, self)._sendTime(totalTime)
        return
