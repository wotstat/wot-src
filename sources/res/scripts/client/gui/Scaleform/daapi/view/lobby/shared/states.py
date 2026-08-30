from __future__ import absolute_import
from frameworks_common.state_machine import StateFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey
from gui.lobby_state_machine.states import SFViewLobbyState, SubScopeTopLayerState

def registerStates(machine):
    machine.addState(BrowserLobbyTopState())
    return


def registerTransitions(machine):
    browser = machine.getStateByCls(BrowserLobbyTopState)
    machine.addNavigationTransitionFromParent(browser)
    return


@SubScopeTopLayerState.parentOf
class BrowserLobbyTopState(SFViewLobbyState):
    STATE_ID = b'browser'
    VIEW_KEY = ViewKey(VIEW_ALIAS.BROWSER_LOBBY_TOP_SUB)

    def __init__(self, flags=StateFlags.UNDEFINED):
        super(BrowserLobbyTopState, self).__init__(flags=flags)
        self.__cachedParams = {}
        return

    @classmethod
    def goTo(cls, ctx):
        super(BrowserLobbyTopState, cls).goTo(ctx=ctx)
        return

    def serializeParams(self):
        return self.__cachedParams

    def _onEntered(self, event):
        self.__cachedParams = event.params
        super(BrowserLobbyTopState, self)._onEntered(event)
        return

    def _getViewLoadCtx(self, event):
        ctx = event.params.get(b'ctx')
        return {b'ctx': {b'url': (ctx.get(b'url')), 
                    b'allowRightClick': (ctx.get(b'allowRightClick', False)), 
                    b'callbackOnLoad': (ctx.get(b'callbackOnLoad')), 
                    b'callbackOnClose': (ctx.get(b'callbackOnClose')), 
                    b'webHandlers': (ctx.get(b'webHandlers')), 
                    b'forcedSkipEscape': (ctx.get(b'forcedSkipEscape')), 
                    b'browserParams': (ctx.get(b'browserParams', {})), 
                    b'hiddenLayers': (ctx.get(b'hiddenLayers', ()))}}
