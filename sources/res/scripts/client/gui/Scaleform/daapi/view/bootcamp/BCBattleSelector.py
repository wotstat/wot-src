import logging
from gui.Scaleform.daapi.view.lobby.header.BattleTypeSelectPopover import BattleTypeSelectPopover
_logger = logging.getLogger(__name__)

class BCBattleSelector(BattleTypeSelectPopover):

    def as_updateS(self, items, extraItems, isShowDemonstrator, demonstratorEnabled):
        _logger.debug(b'BCBattleSelector, %s', items)
        for battleTypeItem in items:
            if battleTypeItem[b'data'] != b'random':
                battleTypeItem[b'disabled'] = True

        super(BCBattleSelector, self).as_updateS(items, extraItems, isShowDemonstrator, demonstratorEnabled)
        return
