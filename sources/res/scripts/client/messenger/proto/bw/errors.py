from chat_shared import CHAT_RESPONSES
from constants import NOVICE_RESTRICTIONS_BAN_TYPE
from debug_utils import LOG_ERROR, LOG_WARNING
from gui.Scaleform.locale.MESSENGER import MESSENGER
from gui.impl import backport
from helpers import i18n
from helpers.time_utils import makeLocalServerTime
import messenger
from messenger.m_constants import MESSENGER_I18N_FILE
from messenger.proto.bw.cooldown import getOperationInCooldownMsg
from messenger.proto.interfaces import IChatError
from messenger.proto.shared_errors import makeChatBanError, makeNoviceChatBanError

class ChannelNotFound(messenger.error):

    def __init__(self, cid, *args, **kwargs):
        super(ChannelNotFound, self).__init__(*args, **kwargs)
        self.cid = cid
        return

    def __str__(self):
        return b'Not found a channel with id = %d, the first request from the server information on the channel with this id' % self.cid


class ChatActionError(IChatError):

    def __init__(self, title, message, isModal=False):
        super(ChatActionError, self).__init__()
        self._title = title
        self._message = message
        self._isModal = isModal
        return

    def getTitle(self):
        return self._title

    def getMessage(self):
        return self._message

    def isModal(self):
        return self._isModal

    @classmethod
    def _makeTitle(cls, name):
        return i18n.makeString((b'#{0:>s}:server/errors/{1:>s}/title').format(MESSENGER_I18N_FILE, name))

    @classmethod
    def _makeMessage(cls, name):
        return i18n.makeString((b'#{0:>s}:server/errors/{1:>s}/message').format(MESSENGER_I18N_FILE, name))

    @classmethod
    def create(cls, chatAction):
        actionResponse = CHAT_RESPONSES[chatAction[b'actionResponse']]
        if actionResponse is None:
            LOG_WARNING(b'__onResponse. action response index %d not found' % chatAction[b'actionResponse'])
            return
        else:
            name = actionResponse.name()
            title = cls._makeTitle(name)
            message = cls._makeMessage(name)
            auxInfo = chatAction[b'data'] if chatAction.has_key(b'data') else None
            if auxInfo is not None and isinstance(auxInfo, dict):
                for key, item in auxInfo.items():
                    if isinstance(item, basestring) and item.startswith(b'#'):
                        auxInfo[key] = i18n.makeString(item)

                try:
                    fullMessage = message % auxInfo
                except TypeError:
                    LOG_WARNING(b'__onResponse. An exception occurred during message formatting: %s %% (%s)' % (
                     message[1], auxInfo))
                    fullMessage = message

            else:
                fullMessage = message
            return ChatActionError(title, fullMessage, isModal=False)


class MemberBannedError(ChatActionError):

    @classmethod
    def create(cls, chatAction):
        banInfo = chatAction[b'data']
        banEndTime = makeLocalServerTime(banInfo.get(b'banEndTime', None))
        if banEndTime is None:
            if banEndTime in banInfo:
                del banInfo[b'banEndTime']
            bannedMessage = i18n.makeString(b'#chat:errors/bannedpermanent', **banInfo)
        else:
            banInfo[b'banEndTime'] = backport.getLongDateFormat(banEndTime) + b' ' + backport.getShortTimeFormat(banEndTime)
            bannedMessage = i18n.makeString(b'#chat:errors/banned', **banInfo)
        return MemberBannedError(cls._makeTitle(b'memberBanned'), bannedMessage, isModal=True)


class ChatBannedError(ChatActionError):

    @classmethod
    def create(cls, chatAction):
        banInfo = chatAction[b'data']
        banEndTime = makeLocalServerTime(banInfo.get(b'banEndTime', None))
        banReason = banInfo.get(b'banReason', None)
        banType = banInfo.get(b'banType', None)
        if banType == NOVICE_RESTRICTIONS_BAN_TYPE:
            bannedMessage = makeNoviceChatBanError()
        else:
            bannedMessage = makeChatBanError(banEndTime, banReason)
        return ChatBannedError(cls._makeTitle(b'chatBanned'), bannedMessage, isModal=True)


class CommandInCooldownError(ChatActionError):

    @classmethod
    def create(cls, chatAction):
        chatActionDict = dict(chatAction)
        data = chatActionDict.get(b'data', {b'command': None, b'cooldownPeriod': (-1)})
        result = None
        if data[b'command'] is not None:
            result = CommandInCooldownError(cls._makeTitle(b'commandInCooldown'), getOperationInCooldownMsg(data[b'command'], data[b'cooldownPeriod']), isModal=False)
        else:
            LOG_ERROR(b'CommandInCooldown', chatActionDict)
        return result


class I18nError(IChatError):
    __slots__ = (b'__message',)

    def __init__(self, key, **kwargs):
        super(I18nError, self).__init__()
        self.__message = i18n.makeString(key, **kwargs)
        return

    def getMessage(self):
        return self.__message


class ChannelLimitReachedError(I18nError):

    def __init__(self):
        super(ChannelLimitReachedError, self).__init__(MESSENGER.CLIENT_ERROR_CHANNEL_LIMIT_REACHED)
        return
