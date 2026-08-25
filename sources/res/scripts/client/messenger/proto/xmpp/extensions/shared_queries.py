from messenger.proto.xmpp.extensions import PyQuery
from messenger.proto.xmpp.extensions.wg_items import WgClientExtension

class MessageQuery(PyQuery):
    __slots__ = (b'_body',)

    def __init__(self, msgType, to, msgBody=b'', ext=None):
        super(MessageQuery, self).__init__(msgType, ext, to)
        self._body = msgBody
        return

    def getBody(self):
        return self._body


class PresenceQuery(PyQuery):

    def __init__(self, queryType, to=b''):
        super(PresenceQuery, self).__init__(queryType, WgClientExtension(), to)
        return

    def getStatus(self):
        return (b'', b'')

    def isMucNsUsed(self):
        return False

    def setIgrID(self, igrID):
        if self._ext:
            self._ext.setIgrID(igrID)
        return

    def setIgrRoomID(self, igrRoomID):
        if self._ext:
            self._ext.setIgrRoomID(igrRoomID)
        return

    def setGameServerHost(self, host):
        if self._ext:
            self._ext.setGameServerHost(host)
        return

    def setArenaGuiLabel(self, label):
        if self._ext:
            self._ext.setArenaGuiLabel(label)
        return
