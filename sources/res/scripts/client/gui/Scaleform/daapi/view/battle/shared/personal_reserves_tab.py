import logging
from gui.Scaleform.daapi.view.meta.PersonalReservesTabMeta import PersonalReservesTabMeta
from gui.impl.battle.battle_page.full_stats.personal_reserves_tab_view import PersonalReservesTabView
_logger = logging.getLogger(__name__)

class PersonalReservesTab(PersonalReservesTabMeta):

    def __init__(self):
        super(PersonalReservesTab, self).__init__()
        _logger.debug(b'[Personal Reserves Tab] init')
        return

    def _onPopulate(self):
        _logger.debug(b'[Personal Reserves Tab] onPopulate')
        self._createInjectView()
        return

    def _makeInjectView(self):
        _logger.debug(b'[Personal Reserves Tab] makeInjectView')
        return PersonalReservesTabView()
