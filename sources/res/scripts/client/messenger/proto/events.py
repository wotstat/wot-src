import Event

class _ChannelsSharedEvents(object):
    __slots__ = (b'__eventManager', b'onChannelInited', b'onPlayerEnterChannelByAction', b'onChannelDestroyed', b'onConnectingToSecureChannel', b'onChannelInfoUpdated', b'onConnectStateChanged', b'onMessageReceived', b'onHistoryReceived', b'onCommandReceived')

    def __init__(self):
        super(_ChannelsSharedEvents, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onChannelInited = Event.Event(self.__eventManager)
        self.onPlayerEnterChannelByAction = Event.Event(self.__eventManager)
        self.onChannelDestroyed = Event.Event(self.__eventManager)
        self.onConnectingToSecureChannel = Event.Event(self.__eventManager)
        self.onChannelInfoUpdated = Event.Event(self.__eventManager)
        self.onConnectStateChanged = Event.Event(self.__eventManager)
        self.onMessageReceived = Event.Event(self.__eventManager)
        self.onHistoryReceived = Event.Event(self.__eventManager)
        self.onCommandReceived = Event.Event(self.__eventManager)
        return

    def clear(self):
        self.__eventManager.clear()
        return


class ChannelEvents(object):
    __slots__ = (b'onConnectStateChanged', b'onChannelInfoUpdated', b'onMembersListChanged', b'onMemberStatusChanged', b'__eventManager')

    def __init__(self):
        super(ChannelEvents, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onConnectStateChanged = Event.Event(self.__eventManager)
        self.onChannelInfoUpdated = Event.Event(self.__eventManager)
        self.onMembersListChanged = Event.Event(self.__eventManager)
        self.onMemberStatusChanged = Event.Event(self.__eventManager)
        return

    def clear(self):
        self.__eventManager.clear()
        return


class MemberEvents(object):
    __slots__ = (b'onMemberStatusChanged', b'__eventManager')

    def __init__(self):
        super(MemberEvents, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onMemberStatusChanged = Event.Event(self.__eventManager)
        return

    def clear(self):
        self.__eventManager.clear()
        return


class _VOIPSharedEvents(object):
    __slots__ = (b'__eventManager', b'onCredentialReceived', b'onChannelAvailable', b'onChannelLost', b'onChannelEntered', b'onChannelLeft', b'onVoiceChatInitSucceeded', b'onVoiceChatInitFailed', b'onPlayerSpeaking')

    def __init__(self):
        super(_VOIPSharedEvents, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onCredentialReceived = Event.Event()
        self.onChannelAvailable = Event.Event(self.__eventManager)
        self.onChannelLost = Event.Event(self.__eventManager)
        self.onChannelEntered = Event.Event(self.__eventManager)
        self.onChannelLeft = Event.Event(self.__eventManager)
        self.onVoiceChatInitSucceeded = Event.Event(self.__eventManager)
        self.onVoiceChatInitFailed = Event.Event(self.__eventManager)
        self.onPlayerSpeaking = Event.Event(self.__eventManager)
        return

    def clear(self):
        self.__eventManager.clear()
        return


class _UsersSharedEvents(object):
    __slots__ = (b'__eventManager', b'onUsersListReceived', b'onFriendsReceived', b'onIgnoredReceived', b'onMutedReceived', b'onUserActionReceived', b'onBattleUserActionReceived', b'onUserStatusUpdated', b'onEmptyGroupsChanged', b'onClanMembersListChanged', b'onFindUsersComplete', b'onFindUsersFailed', b'onNotesListReceived', b'onFriendshipRequestsAdded', b'onFriendshipRequestsUpdated')

    def __init__(self):
        super(_UsersSharedEvents, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onFriendsReceived = Event.Event()
        self.onIgnoredReceived = Event.Event()
        self.onMutedReceived = Event.Event()
        self.onUsersListReceived = Event.Event()
        self.onUserActionReceived = Event.Event(self.__eventManager)
        self.onBattleUserActionReceived = Event.Event(self.__eventManager)
        self.onEmptyGroupsChanged = Event.Event(self.__eventManager)
        self.onUserStatusUpdated = Event.Event(self.__eventManager)
        self.onClanMembersListChanged = Event.Event(self.__eventManager)
        self.onFindUsersComplete = Event.Event(self.__eventManager)
        self.onFindUsersFailed = Event.Event(self.__eventManager)
        self.onFriendshipRequestsAdded = Event.Event(self.__eventManager)
        self.onFriendshipRequestsUpdated = Event.Event(self.__eventManager)
        self.onNotesListReceived = Event.Event(self.__eventManager)
        return

    def clear(self):
        self.__eventManager.clear()
        return


class _ServiceChannelEvents(object):
    __slots__ = (b'__eventManager', b'onServerMessageReceived', b'onCustomMessageDataReceived', b'onClientMessageReceived', b'onChatMessageReceived')

    def __init__(self):
        super(_ServiceChannelEvents, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onServerMessageReceived = Event.Event(self.__eventManager)
        self.onCustomMessageDataReceived = Event.Event(self.__eventManager)
        self.onClientMessageReceived = Event.Event(self.__eventManager)
        self.onChatMessageReceived = Event.Event(self.__eventManager)
        return

    def clear(self):
        self.__eventManager.clear()
        return


class _ShadowEvents(object):
    __slots__ = (b'__eventManager', b'onActionDone', b'onActionFailed')

    def __init__(self):
        super(_ShadowEvents, self).__init__()
        self.__eventManager = Event.EventManager()
        self.onActionDone = Event.Event(self.__eventManager)
        self.onActionFailed = Event.Event(self.__eventManager)
        return

    def clear(self):
        self.__eventManager.clear()
        return


class _MessengerEvents(object):
    __slots__ = (b'__channels', b'__users', b'__serviceChannel', b'__voip', b'__shadow', b'onErrorReceived', b'onCustomMessage', b'onPluginConnected', b'onPluginDisconnected', b'onPluginConnectFailed', b'onLockPopUpMessages', b'onUnlockPopUpMessages')

    def __init__(self):
        super(_MessengerEvents, self).__init__()
        self.__channels = _ChannelsSharedEvents()
        self.__users = _UsersSharedEvents()
        self.__serviceChannel = _ServiceChannelEvents()
        self.__voip = _VOIPSharedEvents()
        self.__shadow = _ShadowEvents()
        self.onErrorReceived = Event.Event()
        self.onCustomMessage = Event.Event()
        self.onPluginConnected = Event.Event()
        self.onPluginDisconnected = Event.Event()
        self.onPluginConnectFailed = Event.Event()
        self.onLockPopUpMessages = Event.Event()
        self.onUnlockPopUpMessages = Event.Event()
        return

    @property
    def channels(self):
        return self.__channels

    @property
    def users(self):
        return self.__users

    @property
    def serviceChannel(self):
        return self.__serviceChannel

    @property
    def voip(self):
        return self.__voip

    @property
    def shadow(self):
        return self.__shadow

    def clear(self):
        self.__channels.clear()
        self.__users.clear()
        self.__serviceChannel.clear()
        self.__voip.clear()
        self.__shadow.clear()
        self.onErrorReceived.clear()
        self.onCustomMessage.clear()
        return


g_messengerEvents = _MessengerEvents()
