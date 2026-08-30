from __future__ import absolute_import
import typing
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.battle_control.controllers.battle_hints.common import getLogger
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams
if typing.TYPE_CHECKING:
    from hints.battle.schemas.base import CHMType
    from gui.battle_control.controllers.battle_hints.controller import BattleHintsController
_logger = getLogger(b'Component')

class IBattleHintView(object):

    def showHint(self, model, params):
        return

    def hideHint(self, hint=None):
        return


class BattleHintComponent(IBattleHintView):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, battleHintsQueueParams=None, *args, **kwargs):
        self.__battleHintsQueueParams = battleHintsQueueParams
        if self.__battleHintsQueueParams is None:
            self.__battleHintsQueueParams = BattleHintQueueParams(name=(b'{}_{}').format(self.__class__.__name__, id(self)))
        super(BattleHintComponent, self).__init__(*args, **kwargs)
        _logger.debug(b'Initialized with queue params %s.', self.__battleHintsQueueParams)
        return

    def getBattleHintsQueueParams(self):
        return self.__battleHintsQueueParams

    def showHint(self, model, params=None):
        self._showHint(model, params)
        return

    def hideHint(self):
        self._hideHint()
        return

    def cancelFadeOut(self):
        self._cancelFadeOut()
        return

    def onFadeOutFinished(self):
        battleHints = self.__sessionProvider.dynamic.battleHints
        if not battleHints:
            _logger.warning(b'No battle hint controller on fade out finished event.')
            return
        battleHints.onFadeOutFinished(self)
        return

    def _showHint(self, model, params):
        raise NotImplementedError
        return

    def _hideHint(self):
        raise NotImplementedError
        return

    def _cancelFadeOut(self):
        return
