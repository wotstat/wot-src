import random, types, time
from string import Template
from helpers import dependency
from ids_generators import SequenceIDGenerator
from messenger import g_settings
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_CHANNEL_TYPE
from skeletons.connection_mgr import IConnectionManager
from soft_exception import SoftException
from constants import STANDALONE_CLUSTER_ID

class BareJID(object):
    __slots__ = (b'_node', b'_domain')

    def __init__(self, jid=None):
        super(BareJID, self).__init__()
        self.setJID(jid)
        return

    def setJID(self, jid):
        tail = b''
        if not jid:
            self._node, self._domain = (b'', b'')
        elif isinstance(jid, types.StringTypes):
            if jid.find(b'@') + 1:
                self._node, jid = jid.split(b'@', 1)
                self._node = self._node.lower()
            else:
                self._node = b''
            if jid.find(b'/') + 1:
                self._domain, tail = jid.split(b'/', 1)
            else:
                self._domain = jid
            self._domain = self._domain.lower()
        elif isinstance(jid, BareJID):
            self._node, self._domain, tail = jid.getNode(), jid.getDomain(), jid.getResource()
        else:
            raise SoftException(b'JID can be specified as string or as instance of JID class.')
        return tail

    def getBareJID(self):
        return self

    def getNode(self):
        return self._node

    def setNode(self, node):
        if node is None:
            self._node = b''
        if isinstance(node, types.StringTypes):
            self._node = node.lower()
        else:
            self._node = node
        return

    def getDomain(self):
        return self._domain

    def setDomain(self, domain):
        if not domain:
            raise SoftException(b'Domain no empty')
        self._domain = domain.lower()
        return

    def getResource(self):
        return b''

    def setResource(self, resource):
        return

    def __str__(self):
        if self._node:
            jid = (b'{0}@{1}').format(self._node, self._domain)
        else:
            jid = self._domain
        return jid

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.__str__() == str(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __nonzero__(self):
        return self.__str__() != b''

    def __hash__(self):
        return hash(self.__str__())

    def __getstate__(self):
        return str(self)

    def __setstate__(self, state):
        self.setJID(state)
        return


class JID(BareJID):
    __slots__ = (b'_resource',)

    def setJID(self, jid):
        self._resource = super(JID, self).setJID(jid)
        return

    def getBareJID(self):
        return BareJID(self)

    def getResource(self):
        return self._resource

    def setResource(self, resource):
        self._resource = resource or b''
        return

    def __str__(self):
        jid = super(JID, self).__str__()
        if self._resource:
            jid = (b'{0}/{1}').format(jid, self._resource)
        return jid


class _DatabaseIDGetter(object):

    def getDatabaseID(self):
        value = getattr(self, b'_node')
        if value:
            try:
                result = long(value)
            except ValueError:
                result = 0

        else:
            result = 0
        return result


class ContactBareJID(BareJID, _DatabaseIDGetter):

    def __hash__(self):
        return self.getDatabaseID()


class ContactJID(JID, _DatabaseIDGetter):

    def getBareJID(self):
        return ContactBareJID(self)

    def __hash__(self):
        return self.getDatabaseID()


def makeContactJID(dbID):
    jid = ContactBareJID()
    jid.setNode(long(dbID))
    jid.setDomain(g_settings.server.XMPP.domain)
    return jid


_counter = SequenceIDGenerator()

def makeUserRoomJID(room=b''):
    jid = JID()
    service = g_settings.server.XMPP.getChannelByType(XMPP_MUC_CHANNEL_TYPE.USERS)
    if not service or not service[b'hostname']:
        return jid
    if not room:
        room = (b'user_room_{:08X}_{:08X}_{:04X}').format(long(time.time()) & 4294967295L, random.randrange(1, 4294967295L), _counter.next())
    jid.setNode(room)
    jid.setDomain(service[b'hostname'])
    return jid


def makeSystemRoomJID(room=b'', channelType=XMPP_MUC_CHANNEL_TYPE.STANDARD):
    jid = JID()
    service = g_settings.server.XMPP.getChannelByType(channelType)
    if not service or not service[b'hostname']:
        return jid
    room = room or _getSystemChannelNameFormatter(service)
    if not room:
        return jid
    jid.setNode(room)
    jid.setDomain(service[b'hostname'])
    return jid


@dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
def _getSystemChannelNameFormatter(service, connectionMgr=None):
    if connectionMgr is not None:
        peripheryID = connectionMgr.peripheryID
    else:
        peripheryID = STANDALONE_CLUSTER_ID
    chanTemplate = Template(service[b'format'])
    if chanTemplate:
        return chanTemplate.safe_substitute(peripheryID=peripheryID, userString=service[b'userString'], hostname=service[b'hostname'], type=service[b'type'])
    else:
        return


def makeClanRoomJID(clandDbId, channelType=XMPP_MUC_CHANNEL_TYPE.CLANS):
    jid = JID()
    service = g_settings.server.XMPP.getChannelByType(channelType)
    if not service or not service[b'hostname']:
        return jid
    clanTemplate = Template(service[b'format'])
    room = clanTemplate.safe_substitute(clanDBID=clandDbId)
    if not room:
        return jid
    jid.setNode(room)
    jid.setDomain(service[b'hostname'])
    return jid
