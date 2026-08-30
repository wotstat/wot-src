from collections import namedtuple
from constants import IGR_TYPE, ARENA_GUI_TYPE_LABEL
from gui.shared.utils.decorators import ReprInjector
from helpers import time_utils
from messenger import g_settings
from messenger.proto.entities import ClanInfo
from messenger.proto.xmpp.gloox_constants import CHAT_STATE
from messenger.proto.xmpp.xmpp_constants import XMPP_BAN_COMPONENT
from messenger.proto.xmpp.xmpp_constants import ANY_ITEM_LITERAL
XMPPChannelData = namedtuple(b'XMPPChannelData', (b'name',))

class ChatMessage(object):
    __slots__ = (b'uuid', b'accountDBID', b'accountName', b'body', b'state', b'sentAt', b'requestID', b'isFinalInHistory', b'accountAffiliation', b'accountRole')

    def __init__(self, dbID=0L, name=b'', body=b'', sentAt=0, affiliation=b'none', role=b'none'):
        super(ChatMessage, self).__init__()
        self.uuid = b''
        self.accountDBID = dbID
        self.accountName = name
        self.accountAffiliation = affiliation
        self.accountRole = role
        self.body = body
        self.state = CHAT_STATE.UNDEFINED
        self.sentAt = sentAt
        self.requestID = b''
        self.isFinalInHistory = False
        return

    def isHistory(self):
        return len(self.requestID) > 0


ClientInfo = namedtuple(b'ClientInfo', (b'igrID', b'igrRoomID', b'gameHost', b'arenaLabel'))
_BanInfoItem = namedtuple(b'_BanInfoItem', (b'source', b'setter', b'expiresAt', b'reason', b'components', b'game', b'banType'))

@ReprInjector.simple((b'_items', b'items'))
class BanInfo(object):
    __slots__ = (b'_items',)

    def __init__(self, items):
        super(BanInfo, self).__init__()
        self._items = items
        return

    def getFirstActiveItem(self, game=None, components=None):
        now = time_utils.getCurrentLocalServerTimestamp()
        for item in sorted(self._items, key=(lambda item: item.expiresAt)):
            if game is not None and item.game not in (game, ANY_ITEM_LITERAL):
                continue
            if components is not None and components & item.components == 0:
                continue
            if not item.expiresAt or item.expiresAt > now:
                return item

        return

    def isBanned(self, game=None, components=None):
        return self.getFirstActiveItem(game=game, components=components) is not None

    @staticmethod
    def getCurrentGame():
        return g_settings.server.XMPP.resource


ExtsInfo = namedtuple(b'ExtsInfo', (b'dbID', b'nickname', b'client', b'clan', b'ban'))
MucInfo = namedtuple(b'MucInfo', (b'affiliation', b'role', b'statuses'))

def makeClientInfo(*args):
    if len(args) < 4:
        return None
    else:
        igrID, igrRoomID, gameHost, arenaLabel = args[:4]
        if igrID and igrID.isdigit():
            igrID = int(igrID)
        else:
            igrID = IGR_TYPE.NONE
        if igrRoomID and igrRoomID.isdigit():
            igrRoomID = long(igrRoomID)
        else:
            igrRoomID = 0
        if arenaLabel and arenaLabel not in ARENA_GUI_TYPE_LABEL.LABELS.values():
            arenaLabel = b''
        return ClientInfo(igrID, igrRoomID, gameHost, arenaLabel)


def makeClanInfo(*args):
    if len(args) < 2:
        return
    else:
        dbID, abbrev = args[:2]
        if dbID and dbID.isdigit():
            dbID = long(dbID)
        else:
            dbID = 0
        info = None
        if dbID and abbrev:
            info = ClanInfo(dbID, abbrev, 0)
        return info


def makeBanInfo(*args):
    items = []
    for item in args:
        if len(item) < 6:
            continue
        source, setter, expiresAt, reason, components, game = item[:6]
        banType = item[6] if len(item) >= 7 else None
        if source.isdigit():
            source = int(source)
        else:
            source = 0
        if expiresAt.isdigit():
            expiresAt = time_utils.getTimestampFromUTC(time_utils.getTimeStructInUTC(float(expiresAt)))
        else:
            expiresAt = 0
        items.append(_BanInfoItem(source, setter, expiresAt, reason, XMPP_BAN_COMPONENT.fromString(components), game, banType))

    if items:
        info = BanInfo(items)
    else:
        info = None
    return info


def makeMucInfo(info):
    if not info:
        return None
    else:
        if b'affiliation' in info:
            affiliation = info[b'affiliation']
        else:
            affiliation = b''
        if b'role' in info:
            role = info[b'role']
        else:
            role = b''
        if b'status_codes' in info:

            def __convert(code):
                if code.isdigit():
                    return int(code)
                return 0

            statuses = map(__convert, info[b'status_codes'])
        else:
            statuses = ()
        return MucInfo(affiliation, role, statuses)
