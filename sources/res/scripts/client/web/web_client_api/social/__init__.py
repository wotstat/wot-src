import BigWorld
from gui.clans.clan_cache import g_clanCache
from gui.shared.view_helpers import UsersInfoHelper
from helpers import isPlayerAccount
from messenger.m_constants import USER_TAG
from messenger.proto.shared_find_criteria import MutualFriendsFindCriteria
from messenger.storage import MessengerStorageDescriptor, UsersStorage
from web.web_client_api import w2capi, w2c, W2CSchema, Field
from web.web_client_api.common import SPA_ID_TYPES
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext

class _OnlineStatus(object):
    OFFLINE = 0
    ONLINE = 1
    BUSY = 2


def getStatuses(users):
    statuses = {}
    for user in users:
        if user.isOnline():
            if USER_TAG.PRESENCE_DND in user.getTags():
                status = _OnlineStatus.BUSY
            else:
                status = _OnlineStatus.ONLINE
        else:
            status = _OnlineStatus.OFFLINE
        statuses[user.getID()] = status

    return statuses


class _PlayerStatusSchema(W2CSchema):
    player_id = Field(required=True, type=SPA_ID_TYPES)


@w2capi(name=b'social', key=b'action')
class SocialWebApi(object):
    lobbyContext = dependency.descriptor(ILobbyContext)
    usersStorage = MessengerStorageDescriptor(UsersStorage)

    def __init__(self):
        super(SocialWebApi, self).__init__()
        self.__usersInfoHelper = UsersInfoHelper()
        return

    @w2c(W2CSchema, name=b'friends_status')
    def friendsStatus(self, cmd):
        storage = self.usersStorage
        friends = storage.getList(MutualFriendsFindCriteria())
        return {b'action': b'friends_status', 
           b'friends_status': (getStatuses(friends))}

    @w2c(_PlayerStatusSchema, name=b'player_status')
    def isPlayerOnline(self, cmd, ctx):
        callback = ctx.get(b'callback')
        playerId = cmd.player_id

        def isAvailable():
            player = self.__usersInfoHelper.getContact(playerId)
            return {b'is_online': (player.isOnline() if player is not None else False)}

        def onNamesReceivedCallback():
            callback(isAvailable())
            self.__usersInfoHelper.onNamesReceived -= onNamesReceivedCallback
            return

        if not bool(self.__usersInfoHelper.getUserName(playerId)):
            self.__usersInfoHelper.onNamesReceived += onNamesReceivedCallback
            self.__usersInfoHelper.syncUsersInfo()
        else:
            return isAvailable()
        return

    @w2c(W2CSchema, name=b'get_player_info')
    def getPlayerInfo(self, _):
        if not isPlayerAccount():
            return {}
        name = BigWorld.player().name
        clanInfo = g_clanCache.clanInfo
        if clanInfo and len(clanInfo) > 1:
            clanAbbrev = clanInfo[1]
        else:
            clanAbbrev = b''
        return {b'fullName': (self.lobbyContext.getPlayerFullName(name, clanInfo=clanInfo)), 
           b'userName': name, 
           b'clanAbbrev': clanAbbrev}
