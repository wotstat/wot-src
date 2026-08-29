import CGF
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from gui.ClientUpdateManager import g_clientUpdateManager
from trigger_vse_component import TriggerVSEComponent
import Event

@registerComponent
class TokenComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    tokenName = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Token Name', value=b'')
    count = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Count', value=0)

    def __init__(self):
        super(TokenComponent, self).__init__()
        self.triggerEvent = Event.Event()
        return


class TokenManager(CGF.ComponentManager):
    __itemsCache = dependency.descriptor(IItemsCache)
    queryToken = CGF.QueryConfig(TokenComponent)

    def activate(self):
        g_clientUpdateManager.addCallback(b'tokens', self.__onTokensUpdate)
        return

    def deactivate(self):
        g_clientUpdateManager.removeObjectCallbacks(self, True)
        return

    @onAddedQuery(TokenComponent)
    def onAddedTokenCount(self, token):
        token.count = self.__itemsCache.items.tokens.getTokenCount(token.tokenName)
        return

    @onAddedQuery(TokenComponent, TriggerVSEComponent)
    def onAddedToken(self, token, trigger):
        token.count = self.__itemsCache.items.tokens.getTokenCount(token.tokenName)
        if token.tokenName == trigger.eventName:
            token.triggerEvent += trigger.triggerEvent
            self.syncTriggerVSE(token)
        return

    @onRemovedQuery(TokenComponent, TriggerVSEComponent)
    def onRemovedToken(self, token, trigger):
        if token.tokenName == trigger.eventName:
            token.triggerEvent -= trigger.triggerEvent
        return

    def __onTokensUpdate(self, diff):
        for token in self.queryToken:
            token.count = self.__itemsCache.items.tokens.getTokenCount(token.tokenName)
            if token.tokenName in diff.keys():
                self.syncTriggerVSE(token)

        return

    def syncTriggerVSE(self, componentToken):
        componentToken.triggerEvent(componentToken.tokenName)
        return
