from collections import deque
from gui.shared.utils.decorators import ReprInjector
from messenger.m_constants import PROTO_TYPE, USER_TAG, GAME_ONLINE_STATUS
from messenger.proto.entities import LobbyUserEntity, ChannelEntity, MemberEntity
from messenger.proto.xmpp.gloox_constants import MESSAGE_TYPE, PRESENCE
from messenger.proto.xmpp.jid import makeClanRoomJID, makeSystemRoomJID
from messenger.proto.xmpp.xmpp_constants import XMPP_BAN_COMPONENT, XMPP_MUC_CHANNEL_TYPE, MESSAGE_LIMIT
from messenger.proto.xmpp.xmpp_items import createItem
from messenger.storage import storage_getter

@ReprInjector.withParent((b'getItem', b'item'), (b'getGOS', b'isOnline'))
class XMPPUserEntity(LobbyUserEntity):
    __slots__ = (b'_item', b'_gos')

    def __init__(self, userID, name=None, tags=None, clanInfo=None, item=None, gos=GAME_ONLINE_STATUS.UNDEFINED, scope=None):
        super(XMPPUserEntity, self).__init__(userID, name, tags, clanInfo, scope=scope)
        self._item = item or createItem(userID)
        self._gos = gos
        return

    def getResourceID(self):
        return self._item.getResources().getHighestPriorityID()

    def getClientInfo(self):
        return self._item.getClientInfo()

    def clear(self):
        self._gos = GAME_ONLINE_STATUS.UNDEFINED
        super(XMPPUserEntity, self).clear()
        return

    def getPersistentState(self):
        state = None
        if self._userID and self._item.isTrusted():
            state = (
             self._name, self._item.getItemType())
        return state

    def setPersistentState(self, state):
        result = False
        if len(state) == 2:
            self._name, itemType = state
            self._item = createItem(self._userID, itemType, trusted=False)
            result = True
        return result

    def getProtoType(self):
        return PROTO_TYPE.XMPP

    def setSharedProps(self, other):
        result = super(XMPPUserEntity, self).setSharedProps(other)
        if result and other.getProtoType() == PROTO_TYPE.XMPP:
            if USER_TAG.CACHED in self.getTags():
                self.update(name=other.getName(), item=other.getItem())
            elif USER_TAG.CACHED in other.getTags() and other.isMuted():
                self.addTags({USER_TAG.MUTED})
        if USER_TAG.filterSharedTags(self._tags):
            self._gos = other.getGOS()
        return result

    def getTags(self):
        tags = super(XMPPUserEntity, self).getTags()
        tags.update(self._item.getTags())
        return tags

    def removeTags(self, tags):
        super(XMPPUserEntity, self).removeTags(tags)
        if self._item.removeTags(tags):
            self._item = createItem(self._userID)
        return

    def getGroups(self):
        return self._item.getGroups()

    def getGOS(self):
        return self._gos

    def isOnline(self):
        return self._item.isOnline(self._gos & GAME_ONLINE_STATUS.ONLINE > 0)

    def update(self, **kwargs):
        if b'item' in kwargs:
            self._item = self._item.replace(kwargs[b'item'])
        if b'gosBit' in kwargs and USER_TAG.filterSharedTags(self._tags):
            self._gos = GAME_ONLINE_STATUS.update(self._gos, kwargs[b'gosBit'])
        self._item.update(**kwargs)
        super(XMPPUserEntity, self).update(**kwargs)
        return

    def getJID(self):
        return self._item.getJID()

    def getSubscription(self):
        return self._item.getSubscription()

    def getItemType(self):
        return self._item.getItemType()

    def getItem(self):
        return self._item


class _XMPPChannelEntity(ChannelEntity):
    __slots__ = (b'_jid', b'_name', b'_isStored', b'_shownMessageIDs')

    def __init__(self, jid, name=b''):
        super(_XMPPChannelEntity, self).__init__(None)
        self._jid = jid
        self._name = name
        self._isStored = False
        self._history = deque([], MESSAGE_LIMIT.HISTORY_MAX_LEN)
        self._shownMessageIDs = deque(self.shownMessagesStorage.getMessages(jid), MESSAGE_LIMIT.HISTORY_MAX_LEN)
        self.shownMessagesStorage.onRestoredFromCache += self._onShownMessagesRestoredFromCache
        self._onShownMessagesRestoredFromCache(None)
        return

    @storage_getter(b'shownMessages')
    def shownMessagesStorage(self):
        return

    def getID(self):
        return self._jid

    def getProtoType(self):
        return PROTO_TYPE.XMPP

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name
        return

    def getFullName(self):
        return self.getName()

    def getMessageType(self):
        raise NotImplementedError
        return

    def getBanComponent(self):
        raise NotImplementedError
        return

    def getPersistentState(self):
        state = None
        if self._isStored:
            state = (
             self.getMessageType(), self._name)
        return state

    def setPersistentState(self, state):
        if len(state) == 2:
            msgType, name = state
            if self.getMessageType() == msgType:
                self._name = name
                self._isStored = True
        else:
            self._isStored = False
        return self._isStored

    def setStored(self, flag):
        self._isStored = flag
        return

    def setJoined(self, isJoined):
        self._isJoined = isJoined
        self.onConnectStateChanged(self)
        return

    def addMember(self, member):
        self.addMembers((member,))
        return

    def removeMember(self, jid):
        self.removeMembers((jid,))
        return

    def clear(self):
        self._isStored = False
        self._shownMessageIDs.clear()
        self.shownMessagesStorage.onRestoredFromCache -= self._onShownMessagesRestoredFromCache
        super(_XMPPChannelEntity, self).clear()
        return

    def setMessageShown(self, message):
        self._shownMessageIDs.append(message.uuid)
        self.shownMessagesStorage.setMessages(self._jid, list(self._shownMessageIDs))
        return

    def isMessageShown(self, message):
        return message.uuid in self._shownMessageIDs

    def _onShownMessagesRestoredFromCache(self, _):
        self._shownMessageIDs.extend(self.shownMessagesStorage.getMessages(self._jid))
        return


class XMPPChatChannelEntity(_XMPPChannelEntity):
    __slots__ = (b'_contactDBID',)

    def __init__(self, jid, name=b''):
        super(XMPPChatChannelEntity, self).__init__(jid, name)
        self._contactDBID = 0
        return

    def isPrivate(self):
        return True

    def getMessageType(self):
        return MESSAGE_TYPE.CHAT

    def getBanComponent(self):
        return XMPP_BAN_COMPONENT.PRIVATE

    def getPersistentState(self):
        state = None
        if self._isStored:
            state = (
             self.getMessageType(), self._name, self._contactDBID)
        return state

    def setPersistentState(self, state):
        if len(state) == 3:
            msgType, name, contactDBID = state
            if self.getMessageType() == msgType:
                self._name = name
                self._contactDBID = contactDBID
                self._isStored = True
        else:
            self._isStored = False
        return self._isStored

    def addMembers(self, members):
        return

    def removeMembers(self, ids):
        return

    def setUser(self, jid, nickname, presence=PRESENCE.AVAILABLE):
        super(XMPPChatChannelEntity, self).addMembers((
         XMPPChatSessionGameMember(jid, nickname, presence),))
        return

    def setContact(self, jid, presence, dbID=0):
        if dbID:
            self._contactDBID = dbID
        if self._contactDBID and jid.getDatabaseID() == self._contactDBID:
            member = XMPPChatSessionGameMember(jid, self.getName(), presence)
        else:
            member = XMPPChatSessionNonGameMember(jid, self.getName(), self._contactDBID, presence)
        super(XMPPChatChannelEntity, self).addMembers((member,))
        return


class XMPPMucChannelEntity(_XMPPChannelEntity):
    __slots__ = (b'_password', b'_isSystem', b'_isLazy', b'_isClan', b'_channelType')

    def __init__(self, jid, name=b'', password=b'', isSystem=False, isLazy=False, channelType=XMPP_MUC_CHANNEL_TYPE.UNKNOWN):
        super(XMPPMucChannelEntity, self).__init__(jid, name)
        self._password = password or b''
        self._isSystem = isSystem
        self._isLazy = isLazy
        self._channelType = channelType
        return

    def isSystem(self):
        return self._isSystem

    def isLazy(self):
        return self._isLazy

    def isAlwaysShow(self):
        if self._channelType == XMPP_MUC_CHANNEL_TYPE.STANDARD:
            return True
        return False

    def isClan(self):
        return self._channelType == XMPP_MUC_CHANNEL_TYPE.CLANS

    def getMessageType(self):
        return MESSAGE_TYPE.GROUPCHAT

    def getBanComponent(self):
        return XMPP_BAN_COMPONENT.USER

    def getPassword(self):
        return self._password

    def setPassword(self, password):
        self._password = password
        return

    def getPersistentState(self):
        state = None
        if self._isSystem and self._isLazy:
            return
        else:
            if self._isStored:
                state = (
                 self.getMessageType(), self._name, self._password)
            return state

    def setPersistentState(self, state):
        if len(state) == 3:
            msgType, name, password = state
            if self.getMessageType() == msgType:
                self._name = name
                self._password = password
                self._isStored = True
        else:
            self._isStored = False
        return self._isStored

    def getMember(self, memberID):
        member = None
        if memberID in self._members:
            member = self._members[memberID]
        return member

    def addMembers(self, members):
        isChanged = False
        for member in members:
            if member is None:
                continue
            memberID = member.getDatabaseID()
            if memberID in self._members:
                self._members[memberID].clear()
            isChanged = True
            self._members[memberID] = member
            member.onMemberStatusChanged += self._onMemberStatusChanged

        if isChanged:
            self.onMembersListChanged()
        return


class XmppSystemChannelEntity(XMPPMucChannelEntity):

    def __init__(self, mucChannelType=XMPP_MUC_CHANNEL_TYPE.UNKNOWN, name=b''):
        jid = makeSystemRoomJID(channelType=mucChannelType)
        channelName = name or jid.getDomain()
        super(XmppSystemChannelEntity, self).__init__(jid, name=channelName, isLazy=True, isSystem=True, channelType=mucChannelType)
        return


class XmppClanChannelEntity(XMPPMucChannelEntity):

    def __init__(self, dbID=0, clanTag=b''):
        jid = makeClanRoomJID(dbID, channelType=XMPP_MUC_CHANNEL_TYPE.CLANS)
        channelName = (b'[{}]').format(clanTag)
        super(XmppClanChannelEntity, self).__init__(jid, name=channelName, isSystem=True, isLazy=False, channelType=XMPP_MUC_CHANNEL_TYPE.CLANS)
        return


class _XMPPMemberEntity(MemberEntity):
    __slots__ = (b'_dbID',)

    def __init__(self, jid, nickName, dbID=0, presence=PRESENCE.AVAILABLE):
        super(_XMPPMemberEntity, self).__init__(jid, nickName, presence)
        self._dbID = dbID
        return

    def getProtoType(self):
        return PROTO_TYPE.XMPP

    def getDatabaseID(self):
        return self._dbID

    def isOnline(self):
        return self.getStatus() not in PRESENCE.OFFLINE

    def clear(self):
        self._memberID = None
        self._dbID = 0
        super(_XMPPMemberEntity, self).clear()
        return


class XMPPChatSessionGameMember(_XMPPMemberEntity):

    def __init__(self, jid, nickName, presence=PRESENCE.AVAILABLE):
        super(XMPPChatSessionGameMember, self).__init__(jid, nickName, presence=presence)
        return

    def getDatabaseID(self):
        return self._memberID.getDatabaseID()


class XMPPChatSessionNonGameMember(_XMPPMemberEntity):
    pass


class XMPPMUCOccupant(_XMPPMemberEntity):
    __slots__ = (b'_affiliation', b'_role')

    def __init__(self, jid, nickName, dbID=0, presence=PRESENCE.AVAILABLE, info=None):
        super(XMPPMUCOccupant, self).__init__(jid, nickName, dbID, presence)
        if info is not None:
            self._affiliation = info.affiliation
            self._role = info.role
        else:
            self._affiliation = b'none'
            self._role = b'none'
        return
