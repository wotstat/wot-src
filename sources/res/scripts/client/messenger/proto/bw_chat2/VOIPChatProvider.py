from debug_utils import LOG_WARNING, LOG_NOTE
from messenger.proto.bw_chat2 import errors, provider as bw2_provider
from messenger.proto.events import g_messengerEvents
from messenger.proto.interfaces import IVOIPChatProvider
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS, messageArgs
from messenger_common_chat2 import MESSENGER_LIMITS as _LIMITS
_EMPTY_CHANNELS_PARAMS = (b'', b'')

class VOIPChatProvider(bw2_provider.ResponseDictHandler, IVOIPChatProvider):

    def __init__(self, provider):
        super(VOIPChatProvider, self).__init__(provider)
        self.__channelParams = _EMPTY_CHANNELS_PARAMS
        return

    def clear(self):
        self.__channelParams = _EMPTY_CHANNELS_PARAMS
        super(VOIPChatProvider, self).clear()
        return

    def leave(self):
        self.__channelParams = _EMPTY_CHANNELS_PARAMS
        return

    def getChannelParams(self):
        return self.__channelParams

    def requestCredentials(self, reset=0):
        provider = self.provider()
        actionID = _ACTIONS.GET_VOIP_CREDENTIALS
        if reset:
            provider.clearActionCoolDown(actionID)
        success, reqID = provider.doAction(actionID, messageArgs(int32Arg1=reset), True)
        if reqID:
            self.pushRq(reqID, actionID)
        if success:
            provider.setActionCoolDown(actionID, _LIMITS.VOIP_CREDENTIALS_REQUEST_COOLDOWN_SEC)
        return

    def logVivoxLogin(self):
        self.provider().doAction(_ACTIONS.LOG_VIVOX_LOGIN)
        return

    def registerHandlers(self):
        register = self.provider().registerHandler
        register(_ACTIONS.ENTER_VOIP_CHANNEL, self.__onChannelAvailable)
        register(_ACTIONS.LEAVE_VOIP_CHANNEL, self.__onChannelLost)
        super(VOIPChatProvider, self).registerHandlers()
        return

    def unregisterHandlers(self):
        unregister = self.provider().unregisterHandler
        unregister(_ACTIONS.ENTER_VOIP_CHANNEL, self.__onChannelAvailable)
        unregister(_ACTIONS.LEAVE_VOIP_CHANNEL, self.__onChannelLost)
        super(VOIPChatProvider, self).unregisterHandlers()
        return

    def _onResponseSuccess(self, ids, args):
        actionID = super(VOIPChatProvider, self)._onResponseSuccess(ids, args)
        if actionID == _ACTIONS.GET_VOIP_CREDENTIALS:
            g_messengerEvents.voip.onCredentialReceived(args[b'strArg1'], args[b'strArg2'])
        return

    def _onResponseFailure(self, ids, args):
        actionID = super(VOIPChatProvider, self)._onResponseFailure(ids, args)
        if actionID is None:
            return
        else:
            error, logOnly = errors.createVOIPError(args, actionID)
            if error:
                if logOnly:
                    LOG_NOTE(error)
                else:
                    g_messengerEvents.onErrorReceived(error)
            else:
                LOG_WARNING(b'Error is not resolved on the client to display in GUI', actionID, ids, args)
            return

    def __onChannelAvailable(self, _, args):
        url = args[b'strArg1']
        pwd = args[b'strArg2']
        isRejoin = args[b'int32Arg1']
        if not url or not pwd or self.__channelParams[0] == url:
            return
        self.__channelParams = (
         url, pwd)
        g_messengerEvents.voip.onChannelAvailable(url, pwd, isRejoin)
        return

    def __onChannelLost(self, ids, args):
        g_messengerEvents.voip.onChannelLost()
        self.__channelParams = _EMPTY_CHANNELS_PARAMS
        return
