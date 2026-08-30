from __future__ import absolute_import
import time, typing, BattleReplay
from PlayerEvents import g_playerEvents
from account_helpers import AccountSettings
from debug_utils import LOG_WARNING
from gui.battle_control.controllers.battle_hints.common import getLogger
from wotdecorators import condition
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.battle_hints.queues import BattleHint
_logger = getLogger(b'History')
_PREFS_NAME = b'displayHistory'

def _createEmptyHistory():
    return {b'lastDisplayTime': {}, b'totalDisplayCount': {}, b'perBattleCount': {}}


class BattleHintsHistory(object):
    __slots__ = (b'_history', b'_enabled')
    ifEnabled = condition(b'_enabled', logFunc=LOG_WARNING, logStack=False)

    def __init__(self):
        self._history = None
        self._enabled = True
        g_playerEvents.onShowBattleHint += self._update
        g_playerEvents.onDisconnected += self.destroy
        _logger.debug(b'Initialized.')
        return

    def getLastDisplayTime(self, uniqueName):
        self._load()
        if self._history is None:
            _logger.debug(b'Can not get display time for <%s>. Not loaded.', uniqueName)
            return 0.0
        else:
            return self._history[b'lastDisplayTime'].get(uniqueName, 0.0)

    def getTotalDisplayCount(self, uniqueName):
        self._load()
        if self._history is None:
            _logger.debug(b'Can not get total display count for <%s>. Not loaded.', uniqueName)
            return 0
        else:
            return self._history[b'totalDisplayCount'].get(uniqueName, 0)

    def getPerBattleCount(self, uniqueName):
        self._load()
        if self._history is None:
            _logger.debug(b'Can not get display count per battle for <%s>. Not loaded.', uniqueName)
            return 0
        else:
            return self._history[b'perBattleCount'].get(uniqueName, 0)

    def destroy(self, *_, **__):
        self._enabled = False
        g_playerEvents.onShowBattleHint -= self._update
        g_playerEvents.onDisconnected -= self.destroy
        if self._history is not None:
            displayHistory = self._history
            self._history = None
            displayHistory.pop(b'perBattleCount')
            AccountSettings.setBattleHints(_PREFS_NAME, displayHistory)
            _logger.debug(b'Destroyed display history.')
        return

    @ifEnabled
    def _load(self):
        if self._history is not None or BattleReplay.isPlaying():
            return
        loadedDisplayHistory = AccountSettings.getBattleHints(_PREFS_NAME)
        if loadedDisplayHistory is None:
            self._history = _createEmptyHistory()
            _logger.debug(b'Created display history.')
        elif isinstance(loadedDisplayHistory, dict):
            self._history = loadedDisplayHistory
            self._history[b'perBattleCount'] = {}
            _logger.debug(b'Loaded display history.')
        else:
            self._history = _createEmptyHistory()
            _logger.debug(b'Corrupted display history. Reset to empty state.')
        return

    def _update(self, battleHint):
        if battleHint.model.history is None:
            return
        else:
            self._load()
            if self._history is None:
                _logger.debug(b'Can not update <%s> display history. Not loaded.', battleHint.uniqueName)
            else:
                prevTotalDisplayCount = self._history[b'totalDisplayCount'].get(battleHint.uniqueName, 0)
                prevPerBattleCount = self._history[b'perBattleCount'].get(battleHint.uniqueName, 0)
                self._history[b'lastDisplayTime'][battleHint.uniqueName] = time.time()
                self._history[b'totalDisplayCount'][battleHint.uniqueName] = prevTotalDisplayCount + 1
                self._history[b'perBattleCount'][battleHint.uniqueName] = prevPerBattleCount + 1
                _logger.debug(b'Hint <%s> display history updated.', battleHint.uniqueName)
            return
