from messenger.proto.bw import bw_chat_string_utils
from messenger.proto.events import g_messengerEvents
from messenger.proto.migration.proxy import MigrationProxy
from messenger.proto.xmpp import xmpp_string_utils
from messenger.proto.xmpp.jid import JID

class MessagesManagerProxy(MigrationProxy):
    __slots__ = ()

    def getSearchUserRoomsProcessor(self):
        raise NotImplementedError
        return

    def getUserRoomValidator(self):
        raise NotImplementedError
        return

    def createUserRoom(self, name, password=b''):
        raise NotImplementedError
        return

    def joinToUserRoom(self, roomID, name, password=b''):
        raise NotImplementedError
        return


class BWMessagesManagerProxy(MessagesManagerProxy):
    __slots__ = ()

    def getSearchUserRoomsProcessor(self):
        from messenger.proto.bw import search_processors
        return search_processors.SearchChannelsProcessor()

    def getUserRoomValidator(self):
        return bw_chat_string_utils

    def createUserRoom(self, name, password=b''):
        self._proto.channels.createChannel(name, password)
        return True

    def joinToUserRoom(self, roomID, name, password=b''):
        self._proto.channels.joinToChannel(roomID, password)
        return True


class XMPPMessagesManagerProxy(MessagesManagerProxy):
    __slots__ = ()

    def getSearchUserRoomsProcessor(self):
        from messenger.proto.xmpp import xmpp_search_processors
        return xmpp_search_processors.SearchUserRoomsProcessor()

    def getUserRoomValidator(self):
        return xmpp_string_utils

    def createUserRoom(self, name, password=b''):
        result, error = self._proto.messages.createUserRoom(name, password)
        if not result:
            g_messengerEvents.onErrorReceived(error)
        return result

    def joinToUserRoom(self, roomID, name, password=b''):
        result, error = self._proto.messages.joinToMUC(JID(roomID), password=password, name=name)
        if not result:
            g_messengerEvents.onErrorReceived(error)
        return result
