import logging
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from portal.gui.impl.battle.portal_hud_widget_view import PortalHudWidgetView
from gui.battle_control.controllers.arena_load_ctrl import IArenaLoadCtrlListener
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
_logger = logging.getLogger(__name__)

class PortalHudWidget(InjectComponentAdaptor, IArenaLoadCtrlListener, IAbstractPeriodView):

    def __init__(self):
        super(PortalHudWidget, self).__init__()
        _logger.debug(b'[Portal HudWidget] _makeInjectView')
        return

    def _onPopulate(self):
        _logger.debug(b'[Portal HudWidget] _onPopulate')
        self._createInjectView()
        return

    def _makeInjectView(self):
        _logger.debug(b'[Portal HudWidget] _makeInjectView')
        return PortalHudWidgetView()

    def arenaLoadCompleted(self):
        return

    def setPeriod(self, period):
        self.getInjectView().setPeriod(period)
        return

    def showHint(self, hint, data=None):
        self.getInjectView().showHint(hint, data)
        return

    def hideHint(self, hint=None):
        _logger.warning(b'hideHint should not be used.')
        return
