from collections import namedtuple
import time as _time, types
from chat_shared import SYS_MESSAGE_IMPORTANCE
_ChannelData = namedtuple(b'_ChannelData', [
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11, 
 12, 
 13, 
 14])

class ChannelDataWrapper(_ChannelData):

    def __new__(cls, id=0, channelName=b'Unknown', owner=-1, ownerName=b'', isReadOnly=False, isSystem=False, isSecured=False, greeting=b'', flags=0, notifyFlags=0, **kwargs):
        return _ChannelData.__new__(cls, id, unicode(channelName, b'utf-8', errors=b'ignore'), owner, unicode(ownerName, b'utf-8', errors=b'ignore'), isReadOnly, isSystem, isSecured, greeting, flags, notifyFlags)


_ChatActionData = namedtuple(b'_ChatActionData', (b' ').join([
 19, 
 20, 
 21, 
 22, 
 23, 
 24, 
 25, 
 26, 
 27, 
 13]))

class ChatActionWrapper(_ChatActionData):

    def __new__(cls, action=-1, channel=0, actionResponse=-1, group=0, originator=-1, originatorNickName=b'Unknown', requestID=-1, data=None, time=_time.time(), sentTime=_time.time(), flags=0, **kwargs):
        result = _ChatActionData.__new__(cls, action, channel, actionResponse, group, originator, unicode(originatorNickName, b'utf-8', errors=b'ignore'), requestID, time, sentTime, flags)
        result.data = unicode(data, b'utf-8', errors=b'ignore') if isinstance(data, types.StringTypes) else data
        return result


_ServiceChannelData = namedtuple(b'_ServiceChannelData', (b' ').join([
 31, 
 32, 
 33, 
 34, 
 35, 
 36, 
 27, 
 37, 
 38, 
 39, 
 40]))

class ServiceChannelMessage(_ServiceChannelData):

    @staticmethod
    def __new__(cls, messageID=-1, user_id=-1, type=-1, importance=SYS_MESSAGE_IMPORTANCE.normal.index(), active=True, personal=False, sentTime=_time.time(), started_at=None, finished_at=None, created_at=None, data=None, **kwargs):
        return _ServiceChannelData.__new__(cls, messageID, user_id, type, importance, active, personal, sentTime, started_at, finished_at, created_at, data)

    @property
    def isHighImportance(self):
        return self.importance == SYS_MESSAGE_IMPORTANCE.high.index()

    @classmethod
    def fromChatAction(cls, chatAction, personal=False):
        kwargs = dict(chatAction[b'data']) if chatAction.has_key(b'data') else {}
        kwargs[b'personal'] = personal
        kwargs[b'sentTime'] = chatAction[b'sentTime']
        return ServiceChannelMessage.__new__(cls, **kwargs)
