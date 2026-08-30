from __future__ import absolute_import
import sys, weakref, typing
from typing import Optional, Dict, Tuple, Union
import BattleReplay
from PlayerEvents import g_playerEvents
from debug_utils import LOG_DEBUG
from gui.battle_control.view_components import ViewComponentsController
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.battle_hints import replay
from gui.battle_control.controllers.battle_hints.common import getLogger
from gui.battle_control.controllers.battle_hints.queues import BattleHintsQueuesMgr
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent
from gui.battle_control.controllers.battle_hints.history import BattleHintsHistory
from hints.battle import manager as battleHintsModelsMgr
from shared_utils import findFirst
from ids_generators import SequenceIDGenerator
from wotdecorators import condition
if typing.TYPE_CHECKING:
    from hints.battle.schemas.base import CHMType
    from gui.battle_control.controllers.battle_hints.queues import BattleHintsQueue, BattleHint
    BHComponentTypes = Optional[Union[weakref.ProxyType[BattleHintComponent], BattleHintComponent]]
_logger = getLogger(b'Controller')

class BattleHintsController(ViewComponentsController):
    __slots__ = (b'_modelsMgr', b'_queuesMgr', b'_history', b'_maxPriorityOffset', b'_components', b'__weakref__', b'_replayController', b'_closeOnRoundFinished', b'_started')
    ifStarted = condition(b'_started', logFunc=LOG_DEBUG, logStack=False)

    def __init__(self, closeOnRoundFinished=True):
        super(BattleHintsController, self).__init__()
        self._closeOnRoundFinished = closeOnRoundFinished
        self._started = False
        self._modelsMgr = battleHintsModelsMgr.get()
        self._queuesMgr = BattleHintsQueuesMgr()
        self._history = BattleHintsHistory()
        self._maxPriorityOffset = SequenceIDGenerator(lowBound=0, highBound=sys.maxsize)
        self._components = {}
        self._replayController = None
        _logger.debug(b'Initialized.')
        return

    def getControllerID(self):
        return BATTLE_CTRL_ID.BATTLE_HINTS

    def clearViewComponents(self):
        super(BattleHintsController, self).clearViewComponents()
        self._components.clear()
        _logger.debug(b'Views cleared.')
        return

    def startControl(self, *args):
        self._started = True
        self._replayController = replay.getReplayController(weakref.proxy(self))
        if self._closeOnRoundFinished:
            g_playerEvents.onRoundFinished += self._onRoundFinished
        _logger.debug(b'Started.')
        return

    def stopControl(self):
        self._stop()
        if self._replayController is not None:
            self._replayController.fini()
            self._replayController = None
        _logger.debug(b'Stopped.')
        return

    @ifStarted
    def showHint(self, hintName, params=None, immediately=False):
        hint, queue = self._prepare(hintName, params=params)
        if hint and queue and hint.canBeShown():
            if immediately:
                hint.setMaxPriority(self._maxPriorityOffset.nextSequenceID)
            queue.add(hint)
        return

    @ifStarted
    def hideHint(self, hintName):
        hint, queue = self._prepare(hintName)
        if hint and queue:
            queue.hide(hint)
        return

    @ifStarted
    def removeHint(self, hintName, hide=False):
        hint, queue = self._prepare(hintName)
        if hint and queue:
            queue.remove(hint)
            if hide:
                queue.hide(hint)
        return

    @ifStarted
    def onFadeOutFinished(self, component):
        queue = self._queuesMgr.get(component.getBattleHintsQueueParams())
        if queue:
            queue.onFadeOutFinished()
        return

    def getComponent(self, alias):
        if alias in self._components:
            component = self._components[alias]
            _logger.debug(b'Getting component <%s> by alias <%s> from cache.', component, alias)
        else:
            component = self._findComponent(alias)
            if component is None:
                _logger.debug(b'Can not find component by alias <%s>.', alias)
                return
            if not isinstance(component, BattleHintComponent):
                _logger.error(b'Unsupported component <%s> type.', alias)
                component = None
            self._components[alias] = component
            _logger.debug(b'Adding component %s by alias <%s> to cache.', component, alias)
        return component

    def checkHintInQueue(self, hintName):
        model = self._getModel(hintName)
        if not model:
            return False
        else:
            alias = model.props.component
            component = self.getComponent(alias)
            if not component:
                return False
            queueParams = component.getBattleHintsQueueParams()
            queue = self._queuesMgr.get(queueParams)
            return [hint for hint in queue._queue if hint.uniqueName == hintName] or queue._displayed is not None and queue._displayed.uniqueName == hintName

    def _onRoundFinished(self, *_, **__):
        self._stop()
        return

    def _stop(self):
        self._started = False
        self._modelsMgr = None
        self._queuesMgr.destroy()
        self._history.destroy()
        self._maxPriorityOffset.clear()
        self.clearViewComponents()
        if self._closeOnRoundFinished:
            g_playerEvents.onRoundFinished -= self._onRoundFinished
        _logger.debug(b'Stopped.')
        return

    def _prepare(self, hintName, params=None):
        if BattleReplay.isPlaying():
            _logger.debug(b'Hints are not showed by controller during the replay.')
            return (None, None)
        else:
            model = self._getModel(hintName)
            if not model:
                return (None, None)
            alias = model.props.component
            component = self.getComponent(alias)
            if not component:
                return (None, None)
            queueParams = component.getBattleHintsQueueParams()
            return (queueParams.createHint(model, component, self._history, params), self._queuesMgr.get(queueParams))

    def _getModel(self, hintName):
        if not self._modelsMgr:
            _logger.warning(b'Models manager not initialized.')
            return None
        else:
            model = self._modelsMgr.get(hintName)
            if not model:
                _logger.error(b'Unknown hint <%s>.', hintName)
                return None
            if not model.validate():
                _logger.debug(b'Not suitable hint <%s> or hint is disabled.', hintName)
                return None
            return model

    def _findComponent(self, alias):
        return findFirst((lambda comp: comp.getAlias() == alias), self._viewComponents, default=None)
