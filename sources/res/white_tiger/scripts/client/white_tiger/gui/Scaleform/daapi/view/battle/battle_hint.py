from __future__ import absolute_import
import logging, typing
from gui.battle_control.controllers.battle_hints.component import BattleHintComponent
from gui.battle_control.controllers.battle_hints.queues import BattleHintQueueParams
from white_tiger.gui.Scaleform.daapi.view.meta.WhiteTigerBattleHintMeta import WhiteTigerBattleHintMeta
if typing.TYPE_CHECKING:
    from hints.battle.schemas.base import CHMType
_logger = logging.getLogger(__name__)
defaultHintQueueParams = BattleHintQueueParams(name=b'default')

class WhiteTigerBattleHint(BattleHintComponent, WhiteTigerBattleHintMeta):

    def _showHint(self, model, params):
        vo = model.createVO(params)
        if vo:
            self.as_showHintS(vo)
        else:
            _logger.debug(b'Value object is empty.')
        return

    def _hideHint(self):
        self.as_hideHintS()
        return

    def _cancelFadeOut(self):
        self.as_cancelFadeOutS()
        return
