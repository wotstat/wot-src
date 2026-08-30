from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.shared.event_bus import EVENT_BUS_SCOPE
from helpers import aop
from gui.shared import events, g_eventBus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class _OnCreateSquadClickAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.SQUAD_PROMO_WINDOW)), EVENT_BUS_SCOPE.LOBBY)
        return


class OnCreateSquadClickPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.header.LobbyHeader', b'LobbyHeader', b'showSquad', aspects=(
         _OnCreateSquadClickAspect,))
        return
