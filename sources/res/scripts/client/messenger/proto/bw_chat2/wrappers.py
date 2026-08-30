from collections import namedtuple
import types, cPickle
from gui.shared.utils import transport
from helpers.time_utils import makeLocalServerTime
from messenger.proto.entities import SharedUserEntity, ClanInfo
from messenger_common_chat2 import messageArgs

class _MessageVO(object):
    __slots__ = (b'sentAt', b'accountDBID', b'avatarSessionID', b'vehicleID', b'text', b'accountName')

    def __init__(self, floatArg1=0, strArg1=b'', **kwargs):
        super(_MessageVO, self).__init__()
        self.accountDBID = 0
        self.avatarSessionID = b''
        self.vehicleID = 0
        self.text = strArg1
        if not isinstance(strArg1, types.UnicodeType):
            self.text = unicode(strArg1, b'utf-8', errors=b'ignore')
        self.sentAt = 0
        if floatArg1 > 0:
            self.sentAt = makeLocalServerTime(floatArg1)
        self.accountName = None
        return


class ArenaMessageVO(_MessageVO):
    __slots__ = (b'isCommonChannel',)

    def __init__(self, floatArg1=0, int32Arg1=False, int64Arg1=0, strArg1=b'', **kwargs):
        super(ArenaMessageVO, self).__init__(floatArg1, strArg1, **kwargs)
        self.vehicleID = int64Arg1
        self.isCommonChannel = bool(int32Arg1)
        return


class UnitMessageVO(_MessageVO):

    def __init__(self, floatArg1=0, int64Arg1=0, strArg1=b'', strArg2=b'', **kwargs):
        super(UnitMessageVO, self).__init__(floatArg1, strArg1, **kwargs)
        self.accountDBID = int64Arg1
        self.accountName = strArg2
        if not isinstance(strArg2, types.UnicodeType):
            self.accountName = unicode(strArg2, b'utf-8', errors=b'ignore')
        return


def UnitHistoryIterator(value):
    value = dict(value)
    if b'strArg1' in value:
        history = transport.z_loads(value[b'strArg1'])
    else:
        history = []
    for sendAt, accountDBID, accountName, messageText in history:
        yield UnitMessageVO(sendAt, accountDBID, messageText, accountName)

    return


def ArenaHistoryIterator(value):
    value = dict(value)
    if b'strArg1' in value:
        history = transport.z_loads(value[b'strArg1'])
    else:
        history = []
    for sendAt, isCommonChannel, vehicleID, messageText in history:
        yield ArenaMessageVO(sendAt, isCommonChannel, vehicleID, messageText)

    return


def SearchResultIterator(value):
    value = dict(value)
    if b'strArg1' in value:
        result = cPickle.loads(value[b'strArg1'])
    else:
        result = []
    for name, dbID, clanAbbrev in result:
        if not name:
            continue
        yield SharedUserEntity(long(dbID), name=name, clanInfo=ClanInfo(abbrev=clanAbbrev))

    return


class IDataFactory(object):

    def broadcastArgs(self, text, *args):
        raise NotImplementedError
        return

    def historyIter(self, args):
        raise NotImplementedError
        return

    def messageVO(self, args):
        raise NotImplementedError
        return


class ArenaDataFactory(IDataFactory):

    def broadcastArgs(self, text, *args):
        return messageArgs(strArg1=text, int32Arg1=args[0] if args else 0)

    def historyIter(self, args):
        return ArenaHistoryIterator(args)

    def messageVO(self, args):
        return ArenaMessageVO(**args)


class UnitDataFactory(IDataFactory):

    def broadcastArgs(self, text, *args):
        return messageArgs(strArg1=text)

    def historyIter(self, args):
        return UnitHistoryIterator(args)

    def messageVO(self, args):
        return UnitMessageVO(**args)


class CHAT_TYPE(object):
    UNIT = 1
    ARENA = 2


ChannelProtoData = namedtuple(b'ChannelProtoData', (b'chatType', b'settings'))
