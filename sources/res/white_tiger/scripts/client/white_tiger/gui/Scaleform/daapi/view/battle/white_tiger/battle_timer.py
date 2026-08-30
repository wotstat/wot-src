import time, BigWorld
from constants import ARENA_PERIOD
from white_tiger.gui.Scaleform.daapi.view.meta.WTBattleTimerMeta import WTBattleTimerMeta
from gui.battle_control.controllers.battle_hints_ctrl import IBattleHintView
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from wt_settings import g_wt_config

class WhiteTigerBattleTimer(WTBattleTimerMeta, IBattleHintView):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(WhiteTigerBattleTimer, self).__init__()
        self.__arenaPeriod = None
        self.__periodEndTime = None
        self.currentHint = None
        self.currentHintStartTime = 0
        return

    def setPeriod(self, period):
        super(WhiteTigerBattleTimer, self).setPeriod(period)
        newEndTime = self.sessionProvider.shared.arenaPeriod.getEndTime()
        if self.__arenaPeriod == ARENA_PERIOD.BATTLE and period == ARENA_PERIOD.BATTLE:
            if self.__periodEndTime is not None:
                if newEndTime > self.__periodEndTime:
                    delta = min(newEndTime - self.__periodEndTime, newEndTime - BigWorld.serverTime())
                    self.as_showAdditionalTimeS((b'+{}').format(time.strftime(b'%M:%S', time.gmtime(delta))))
        self.__periodEndTime = newEndTime
        self.__arenaPeriod = period
        return

    def showHint(self, hint, data):
        hintName = hint.name
        if hintName == b'wtTimeRemaining_hunter' or hintName == b'wtTimeRemaining_wtLowHP_hunter':
            message = backport.text(R.strings.white_tiger.battleTimer.timeRemaining.hunter.messageText())
            self.as_showMessageS(message, isOverTime=False)
        elif hintName == b'wtTimeRemaining_boss' or hintName == b'wtTimeRemaining_wtLowHP_boss':
            message = backport.text(R.strings.white_tiger.battleTimer.timeRemaining.boss.messageText())
            self.as_showMessageS(message, isOverTime=False)
        self.currentHint = hint
        self.currentHintStartTime = time.time()
        return

    def hideHint(self, hint=None):
        if hint:
            if hint.name == b'wtTimeRemaining_hunter' or hint.name == b'wtTimeRemaining_wtLowHP_hunter' or hint.name == b'wtTimeRemaining_boss' or hint.name == b'wtTimeRemaining_wtLowHP_boss':
                self.as_hideMessageS()
                self.currentHint = None
        return

    def _populate(self):
        super(WhiteTigerBattleTimer, self)._populate()
        self.as_setPlayerTypeS(self.__isBossPlayer())
        return

    def __isBossPlayer(self):
        vInfo = self.sessionProvider.getCtx().getVehicleInfo(BigWorld.player().playerVehicleID)
        vehCD = vInfo.vehicleType.compactDescr
        return g_wt_config.isAnyTypeBoss(vehCD)
