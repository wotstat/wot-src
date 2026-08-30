import logging
from gui.Scaleform.daapi.view.meta.InfoBattleContextHintMeta import InfoBattleContextHintMeta
from gui.impl.battle.battle_page.battle_context_hints.info_battle_context_hint_view import InfoBattleContextHintView
_logger = logging.getLogger(__name__)

class InfoHintInjectComponent(InfoBattleContextHintMeta):

    def _onPopulate(self):
        _logger.debug(b'[BATTLE_CONTEXT_INTS] InfoHintInjectComponent._onPopulate')
        self._createInjectView(InfoBattleContextHintView)
        return

    def showHint(self, *args):
        _logger.debug(b'[BATTLE_CONTEXT_INTS] InfoHintInjectComponent.showHint')
        self.setVisibility(True)
        return

    def hideHint(self):
        self.setVisibility(False)
        _logger.debug(b'[BATTLE_CONTEXT_INTS] InfoHintInjectComponent.hideHint')
        return

    def setVisibility(self, visible):
        self.as_setVisibilityS(visible)
        return
