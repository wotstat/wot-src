from __future__ import absolute_import, division
import copy, BattleReplay, typing
from math_common import decimal_round
from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID, LS_BATTLE_HINTS_QUEUE_ID
from last_stand.gui.scaleform.daapi.view.meta.BattleHintMeta import BattleHintMeta
from last_stand.gui.scaleform.daapi.view.meta.BattleHintProgressDefenceMeta import BattleHintProgressDefenceMeta
from last_stand.gui.scaleform.daapi.view.meta.BattleHintProgressConvoyMeta import BattleHintProgressConvoyMeta
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class BattleHint(BattleHintComponent, BattleHintMeta):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(BattleHint, self).__init__(battleHintsQueueParams=LS_BATTLE_HINTS_QUEUE_ID)
        return

    @property
    def lsBattleGuiCtrl(self):
        return self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.LS_BATTLE_GUI_CTRL)

    def _populate(self):
        super(BattleHint, self)._populate()
        if self.lsBattleGuiCtrl:
            self.lsBattleGuiCtrl.onBattleGoalChanged += self._onBattleGoalChanged
        return

    def _dispose(self):
        super(BattleHint, self)._dispose()
        if self.lsBattleGuiCtrl:
            self.lsBattleGuiCtrl.onBattleGoalChanged -= self._onBattleGoalChanged
        if BattleReplay.g_replayCtrl.isPlaying:
            self._hideHint()
        return

    def _showHint(self, model, params):
        vo = model.createVO(params)
        if vo:
            self.as_showHintS(vo)
        return

    def _hideHint(self):
        self.as_hideHintS()
        return

    def _cancelFadeOut(self):
        self.as_cancelFadeOutS()
        return

    def _onBattleGoalChanged(self, goalName):
        self.as_clearPinnableHintS()
        return


class ProgressBarMixin(BattleHint):
    DEAD_ENEMY_STATUS_POSTFIX = b'_dead'
    DEFAULT_ENEMY_STATUS = {b'role': b'unknown', b'isDead': False}
    STATUS_SORTING_ORDER = [4, 5, 6, 7, 8, 9, 10, 11, 
     12, 13, 14, 15, 16, 17, 18, 
     19, 
     20, 21, 22, 23, 1]

    def _getEnemiesInfo(self):
        if self.lsBattleGuiCtrl:
            return self.lsBattleGuiCtrl.getEnemiesInfo()
        return {}

    def _formatEnemiesStatus(self, enemiesStatus):
        enemiesStatusFull = copy.deepcopy(enemiesStatus)
        missingStatusCount = self._getEnemiesInfo().get(b'totalEnemies', 0) - len(enemiesStatusFull)
        if missingStatusCount > 0:
            enemiesStatusFull.extend([self.DEFAULT_ENEMY_STATUS] * missingStatusCount)
        enemiesStatusFull = sorted(enemiesStatusFull, key=(lambda status: (
         status[b'isDead'], self.STATUS_SORTING_ORDER.index(status[b'role']))))
        return [status[b'role'] + self.DEAD_ENEMY_STATUS_POSTFIX if status[b'isDead'] else status[b'role'] for status in enemiesStatusFull]


class DefenceProgressBarBattleHint(ProgressBarMixin, BattleHintProgressDefenceMeta):

    def _populate(self):
        super(DefenceProgressBarBattleHint, self)._populate()
        if self.lsBattleGuiCtrl:
            self.lsBattleGuiCtrl.onEnemiesInfoChanged += self._onEnemiesInfoChanged
            self.lsBattleGuiCtrl.onHealthBreakpointsChanged += self._onHealthBreakpointsChanged
            self.lsBattleGuiCtrl.onEnemiesStatusChanged += self._onEnemiesStatusChanged
        if self.guiSessionProvider.isReplayPlaying:
            self.as_handleAsReplayS()
        return

    def _dispose(self):
        if self.lsBattleGuiCtrl:
            self.lsBattleGuiCtrl.onEnemiesInfoChanged -= self._onEnemiesInfoChanged
            self.lsBattleGuiCtrl.onHealthBreakpointsChanged -= self._onHealthBreakpointsChanged
            self.lsBattleGuiCtrl.onEnemiesStatusChanged -= self._onEnemiesStatusChanged
        super(DefenceProgressBarBattleHint, self)._dispose()
        return

    def _hideHint(self):
        super(DefenceProgressBarBattleHint, self)._hideHint()
        self._updateProgressBar(self._getEnemiesInfo())
        return

    def _normalizeProgressValue(self, currentValue, maxValue):
        if maxValue > 0:
            return decimal_round(float(maxValue - currentValue) / float(maxValue), 2) * 100
        return 0

    def _updateProgressBar(self, enemiesInfo):
        enemiesAlive = enemiesInfo.get(b'aliveEnemies', 0)
        currentHealth = enemiesInfo.get(b'currentHealth', 0)
        totalHealth = enemiesInfo.get(b'totalHealth', 0)
        lostHealth = max(0, totalHealth - currentHealth)
        normalizedProgressValue = self._normalizeProgressValue(lostHealth, totalHealth)
        self.as_updateProgressS(enemiesAlive, normalizedProgressValue, currentHealth)
        return

    def _onEnemiesInfoChanged(self, enemiesInfo):
        self._updateProgressBar(enemiesInfo)
        return

    def _onHealthBreakpointsChanged(self, healthBreakpoints):
        self.as_updateHealthPointsS(healthBreakpoints)
        return

    def _onEnemiesStatusChanged(self, enemiesStatus):
        enemiesStatusList = self._formatEnemiesStatus(enemiesStatus)
        self.as_updateVehiclesS(enemiesStatusList)
        return


class ConvoyProgressBarBattleHint(ProgressBarMixin, BattleHintProgressConvoyMeta):

    def __init__(self):
        super(ConvoyProgressBarBattleHint, self).__init__()
        self._convoyDistanceIndicator = None
        self._convoyHealth = None
        self._convoyStatus = None
        return

    def _populate(self):
        super(ConvoyProgressBarBattleHint, self)._populate()
        if self.lsBattleGuiCtrl:
            self.lsBattleGuiCtrl.onConvoyStatusChanged += self._onConvoyStatusChanged
            self.lsBattleGuiCtrl.onConvoyDistanceIndicatorChanged += self._onConvoyDistanceIndicatorChanged
            self.lsBattleGuiCtrl.onConvoyHealthChanged += self._onConvoyHealthChanged
            self.lsBattleGuiCtrl.onEnemiesStatusChanged += self._onEnemiesStatusChanged
        if self.guiSessionProvider.isReplayPlaying:
            self.as_handleAsReplayS()
        return

    def _dispose(self):
        if self.lsBattleGuiCtrl:
            self.lsBattleGuiCtrl.onConvoyStatusChanged -= self._onConvoyStatusChanged
            self.lsBattleGuiCtrl.onConvoyDistanceIndicatorChanged -= self._onConvoyDistanceIndicatorChanged
            self.lsBattleGuiCtrl.onConvoyHealthChanged -= self._onConvoyHealthChanged
            self.lsBattleGuiCtrl.onEnemiesStatusChanged -= self._onEnemiesStatusChanged
        super(ConvoyProgressBarBattleHint, self)._dispose()
        return

    def _onConvoyHealthChanged(self, health):
        self._convoyHealth = health
        if (self._convoyStatus and self._convoyDistanceIndicator) is not None:
            self.as_updateProgressS(self.lsBattleGuiCtrl.MAX_UI_CONVOY_PROGRESS, self._convoyDistanceIndicator, self._convoyHealth)
        return

    def _onConvoyDistanceIndicatorChanged(self, distanceIndicator):
        self._convoyDistanceIndicator = distanceIndicator
        if (self._convoyStatus and self._convoyHealth) is not None:
            self.as_updateProgressS(self.lsBattleGuiCtrl.MAX_UI_CONVOY_PROGRESS, self._convoyDistanceIndicator, self._convoyHealth)
        return

    def _onConvoyStatusChanged(self, convoyStatus):
        if convoyStatus:
            self._convoyStatus = convoyStatus
            self.as_setConvoyVehiclesStatusS([not vehicleInfo[b'isDead'] for vehicleInfo in convoyStatus])
        return

    def _onEnemiesStatusChanged(self, enemiesStatus):
        enemiesStatusList = self._formatEnemiesStatus(enemiesStatus)
        self.as_updateVehiclesS(enemiesStatusList)
        return
