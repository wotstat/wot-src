from gui.clans.clan_cache import g_clanCache
from messenger.proto.shared_find_criteria import MutualFriendsFindCriteria
from web.web_client_api import w2capi, w2c, W2CSchema
from web.web_client_api.social import getStatuses
from helpers import dependency
from skeletons.gui.game_control import IClanNotificationController
from skeletons.gui.web import IWebController

@w2capi(name=b'clan_management', key=b'action')
class ClansWebApi(object):
    __notificationCtrl = dependency.descriptor(IClanNotificationController)
    __webCtrl = dependency.descriptor(IWebController)

    @w2c(W2CSchema, name=b'members_online')
    def membersOnline(self, cmd):
        members = g_clanCache.clanMembers
        onlineCount = 0
        for member in members:
            if member.isOnline():
                onlineCount += 1

        return {b'action': b'members_online', b'all_members': (len(members)), 
           b'online_members': onlineCount}

    @w2c(W2CSchema, name=b'members_status')
    def membersStatus(self, cmd):
        members = g_clanCache.clanMembers
        return {b'action': b'members_status', 
           b'members_status': (getStatuses(members))}

    @w2c(W2CSchema, name=b'friends_status')
    def friendsStatus(self, cmd):
        storage = g_clanCache.usersStorage
        friends = storage.getList(MutualFriendsFindCriteria(), iterator=storage.getClanMembersIterator(False))
        return {b'action': b'friends_status', 
           b'friends_status': (getStatuses(friends))}

    @w2c(W2CSchema, name=b'set_news_counter')
    def setNewsCounter(self, cmd):
        alias = cmd.custom_parameters.get(b'alias')
        value = cmd.custom_parameters.get(b'count', 1)
        self.__notificationCtrl.setCounters(alias, value)
        return {b'action': b'set_news_counter'}

    @w2c(W2CSchema, name=b'get_news_counters')
    def getNewsCounters(self, cmd):
        aliases = cmd.custom_parameters.get(b'aliases', [])
        return {b'action': b'get_news_counters', 
           b'news_counts': (self.__notificationCtrl.getCounters(aliases))}

    @w2c(W2CSchema, name=b'get_clan_info')
    def getClanInfo(self, cmd):
        return {b'action': b'get_clan_info', 
           b'clan_info': (self.__webCtrl.getClanInfo())}
