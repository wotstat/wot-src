from gui.Scaleform.locale.MESSENGER import MESSENGER as I18N_MESSENGER
from gui.impl import backport
from helpers import i18n
from messenger.m_constants import CLIENT_ERROR_NAMES, CLIENT_ACTION_NAMES, CLIENT_ERROR_ID
from messenger.proto.interfaces import IChatError

class I18nErrorID(object):
    __slots__ = (b'errorID',)

    def __init__(self, errorID):
        super(I18nErrorID, self).__init__()
        self.errorID = errorID
        return

    def __repr__(self):
        return (b'{0}').format(self.getName())

    def getName(self):
        if self.errorID in CLIENT_ERROR_NAMES:
            errorName = CLIENT_ERROR_NAMES[self.errorID]
        else:
            errorName = (b'CLIENT_ERROR_{0}').format(self.errorID)
        return errorName

    def getI18nKey(self):
        return I18N_MESSENGER.client_error_shared(self.getName())


class I18nActionID(object):
    __slots__ = (b'actionID',)

    def __init__(self, actionID):
        super(I18nActionID, self).__init__()
        self.actionID = actionID
        return

    def __repr__(self):
        return (b'{0}').format(self.getName())

    def getName(self):
        if self.actionID in CLIENT_ACTION_NAMES:
            actionName = CLIENT_ACTION_NAMES[self.actionID]
        else:
            actionName = (b'CLIENT_ACTION_{0}').format(self.actionID)
        return actionName

    def getI18nName(self):
        name = self.getName()
        key = I18N_MESSENGER.client_action(name)
        if key:
            name = i18n.makeString(key)
        return name


class ClientError(IChatError):
    __slots__ = (b'_error', b'_kwargs')

    def __init__(self, errorID, **kwargs):
        self._error = self.createError(errorID)
        self._kwargs = kwargs
        return

    def __repr__(self):
        return (b'{0}(error={1})').format(self.__class__.__name__, self._error)

    def createError(self, errorID):
        return I18nErrorID(errorID)

    def getErrorID(self):
        return self._error.errorID

    def getErrorName(self):
        return self._error.getName()

    def getMessage(self):
        key = self._error.getI18nKey()
        if key:
            result = i18n.makeString(key, **self._kwargs)
        else:
            result = self._error.getName()
            if self._kwargs:
                result = (b'{0}/{1}').format(result, self._kwargs)
        return result


class ClientActionError(ClientError):
    __slots__ = (b'_action',)

    def __init__(self, actionID, errorID=None, **kwargs):
        super(ClientActionError, self).__init__((errorID or CLIENT_ERROR_ID.GENERIC), **kwargs)
        self._action = self.createAction(actionID)
        return

    def __repr__(self):
        return (b'{0}(action={1}, error={2})').format(self.__class__.__name__, self._action, self._error)

    def createAction(self, actionID):
        return I18nActionID(actionID)

    def getActionID(self):
        return self._action.actionID

    def getMessage(self):
        if b'actionName' not in self._kwargs:
            self._kwargs[b'actionName'] = self._action.getI18nName()
        return super(ClientActionError, self).getMessage()


class ChatCoolDownError(ClientActionError):

    def __init__(self, actionID, coolDown=None):
        if coolDown:
            kwargs = {b'floatArg1': coolDown}
        else:
            kwargs = {}
        super(ChatCoolDownError, self).__init__(actionID, CLIENT_ERROR_ID.COOLDOWN, **kwargs)
        return

    def getMessage(self):
        actionName = self._action.getI18nName()
        if self._kwargs:
            msg = i18n.makeString(I18N_MESSENGER.CLIENT_ERROR_ACTION_IN_COOLDOWN, actionName=actionName, **self._kwargs)
        else:
            msg = i18n.makeString(I18N_MESSENGER.CLIENT_ERROR_ACTION_IN_COOLDOWN_WO_PERIOD, actionName=actionName)
        return msg


class ChatBanError(IChatError):
    __slots__ = (b'_endTime', b'_reason')

    def __init__(self, endTime, reason):
        super(ChatBanError, self).__init__()
        self._endTime = endTime
        self._reason = reason
        return

    def getTitle(self):
        return i18n.makeString(I18N_MESSENGER.SERVER_ERRORS_CHATBANNED_TITLE)

    def getMessage(self):
        if self._endTime:
            banEndTime = backport.getLongDateFormat(self._endTime) + b' ' + backport.getShortTimeFormat(self._endTime)
            msg = i18n.makeString(b'#chat:errors/chatbanned', banEndTime=banEndTime, banReason=self._reason)
        else:
            msg = i18n.makeString(b'#chat:errors/chatbannedpermanent', banReason=self._reason)
        return msg

    def isModal(self):
        return True
