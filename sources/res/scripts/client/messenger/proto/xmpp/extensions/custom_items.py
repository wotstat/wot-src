from debug_utils import LOG_CURRENT_EXCEPTION
from shared_utils import findFirst
from messenger.proto.xmpp.extensions import PyExtension, SimpleExtension, PyHandler
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.wrappers import makeClanInfo, makeClientInfo, makeBanInfo, ExtsInfo

class SharedExtension(PyExtension):

    def __init__(self, includeNS=True):
        super(SharedExtension, self).__init__(_TAG.EXTENSION)
        if includeNS:
            self.setXmlNs(_NS.EXTENSION)
        return

    @classmethod
    def getDefaultData(cls):
        return {}

    def getTag(self):
        tag = b''
        if self._children:
            tag = super(SharedExtension, self).getTag()
        return tag

    def parseTag(self, pyGlooxTag):
        info = self.getDefaultData()
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'nickname')))
        if tag:
            info[b'name'] = tag.getCData()
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'userid')))
        if tag:
            info[b'dbID'] = long(tag.getCData())
        clanDBID, clanAbbrev = (0, b'')
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'clanid')))
        if tag:
            clanDBID = tag.getCData()
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'clantag')))
        if tag:
            clanAbbrev = tag.getCData()
        if clanDBID and clanAbbrev:
            info[b'clanInfo'] = makeClanInfo(clanDBID, clanAbbrev)
        return info


class ClientExtension(PyExtension):

    def __init__(self):
        super(ClientExtension, self).__init__(_TAG.EXT_CLIENT)
        self.setXmlNs(_NS.EXT_CLIENT)
        return

    def setIgrID(self, igrID):
        if igrID:
            self.setChild(SimpleExtension(b'igr-id', igrID))
        return

    def setIgrRoomID(self, igrRoomID):
        if igrRoomID:
            self.setChild(SimpleExtension(b'igr-room-id', igrRoomID))
        return

    def setGameServerHost(self, host):
        if host:
            self.setChild(SimpleExtension(b'game-host', host))
        return

    def setArenaGuiLabel(self, label):
        if label:
            self.setChild(SimpleExtension(b'arena-label', label))
        return

    @classmethod
    def getDefaultData(cls):
        return

    def getTag(self):
        tag = b''
        if self._children:
            tag = super(ClientExtension, self).getTag()
        return tag

    def parseTag(self, pyGlooxTag):
        igrID, igrRoomID, gameHost, arenaLabel = (0, 0, b'', b'')
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'igr-id')))
        if tag:
            igrID = tag.getCData()
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'igr-room-id')))
        if tag:
            igrRoomID = tag.getCData()
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'game-host')))
        if tag:
            gameHost = tag.getCData()
        tag = findFirst(None, pyGlooxTag.filterXPath(self.getXPath(suffix=b'arena-label')))
        if tag:
            arenaLabel = tag.getCData()
        return makeClientInfo(igrID, igrRoomID, gameHost, arenaLabel)


class ExtClientHandler(PyHandler):

    def __init__(self):
        super(ExtClientHandler, self).__init__(ClientExtension())
        return

    def getFilterString(self):
        return self._ext.getXPath()


def makeExtInfoFromPresence(info):
    if b'userId' in info:
        try:
            dbID = long(info[b'userId'])
        except TypeError:
            LOG_CURRENT_EXCEPTION()
            dbID = 0

    else:
        dbID = 0
    if b'nickname' in info:
        nickname = info[b'nickname']
    else:
        nickname = b''
    if b'extsClientTag' in info:
        clientInfo = ExtClientHandler().handleTag(info[b'extsClientTag'])
    else:
        clientInfo = None
    if b'clanInfo' in info:
        clanInfo = makeClanInfo(*info[b'clanInfo'])
    else:
        clanInfo = None
    if b'banInfo' in info:
        banInfo = makeBanInfo(*info[b'banInfo'])
    else:
        banInfo = None
    return ExtsInfo(dbID, nickname, clientInfo, clanInfo, banInfo)
