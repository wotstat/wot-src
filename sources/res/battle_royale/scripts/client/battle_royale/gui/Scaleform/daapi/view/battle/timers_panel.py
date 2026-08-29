import weakref, math, BigWorld
from battle_royale.gui.Scaleform.daapi.view.common.respawn_ability import RespawnAbility
from gui.Scaleform.daapi.view.meta.BattleRoyaleTimersPanelMeta import BattleRoyaleTimersPanelMeta
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import AirDropEvent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from constants import ARENA_PERIOD, ARENA_BONUS_TYPE
from gui.Scaleform.daapi.view.battle.shared.timers_common import TimerComponent, PythonTimer

def _setRespawnTime(panel, timeLeft):
    panel.as_setRespawnTimeS(timeLeft)
    return


def _setAirDropTime(panel, timeLeft):
    panel.as_setAirDropTimeS(timeLeft)
    return


class _AsTimer(TimerComponent):

    def __init__(self, panel, totalTime, viewFunc):
        super(_AsTimer, self).__init__(weakref.proxy(panel), 0, 0, totalTime, 0)
        self._viewFunc = viewFunc
        return

    def _startTick(self):
        return

    def _stopTick(self):
        return

    def _hideView(self):
        return

    def _showView(self, isBubble):
        self._viewFunc(self._viewObject, self._totalTime)
        return


class _ReplayTimer(PythonTimer):

    def __init__(self, panel, totalTime, viewFunc):
        super(_ReplayTimer, self).__init__(weakref.proxy(panel), 0, 0, totalTime, 0)
        self._viewFunc = viewFunc
        return

    def _hideView(self):
        self._viewFunc(self._viewObject, 0)
        return

    def _showView(self, isBubble):
        return

    def _setViewSnapshot(self, timeLeft):
        self._viewFunc(self._viewObject, int(math.ceil(timeLeft)))
        return


class TimersPanelPanel(BattleRoyaleTimersPanelMeta, IAbstractPeriodView):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)
    __timerCreator = property((lambda self: _ReplayTimer if self.__sessionProvider.isReplayPlaying else _AsTimer))

    def __init__(self):
        super(TimersPanelPanel, self).__init__()
        self._respawnPeriod = 0
        return

    def _populate(self):
        super(TimersPanelPanel, self)._populate()
        g_eventBus.addListener(AirDropEvent.AIR_DROP_NXT_SPAWNED, self.__onAirDropLootSpawned, scope=EVENT_BUS_SCOPE.BATTLE)
        bonusType = self.__sessionProvider.arenaVisitor.getArenaBonusType()
        isSquadMode = bonusType in ARENA_BONUS_TYPE.BATTLE_ROYALE_SQUAD_RANGE
        self._respawnPeriod = (isSquadMode or RespawnAbility()).soloRespawnPeriod if 1 else RespawnAbility().platoonRespawnPeriod
        self.as_setIsReplayS(self.__sessionProvider.isReplayPlaying)
        self._airDroptimer = self._respawnTimer = None
        if self.__sessionProvider.isReplayPlaying:
            self.setPeriod(ARENA_PERIOD.BATTLE)
        return

    def _dispose(self):
        super(TimersPanelPanel, self)._dispose()
        g_eventBus.removeListener(AirDropEvent.AIR_DROP_NXT_SPAWNED, self.__onAirDropLootSpawned, scope=EVENT_BUS_SCOPE.BATTLE)
        return

    def setPeriod(self, period):
        if period == ARENA_PERIOD.BATTLE:
            timeout = self._respawnPeriod
            periodCtrl = self.__sessionProvider.shared.arenaPeriod
            if periodCtrl:
                startTime = periodCtrl.getEndTime() - periodCtrl.getLength()
                timeout -= BigWorld.serverTime() - startTime
            self._respawnTimer = self.__timerCreator(self, timeout, _setRespawnTime)
            self._respawnTimer.show()
        return

    def __onAirDropLootSpawned(self, event):
        self._airDroptimer = self.__timerCreator(self, event.ctx[b'timeout'] - BigWorld.serverTime(), _setAirDropTime)
        self._airDroptimer.show()
        return
