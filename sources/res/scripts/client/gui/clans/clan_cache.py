from collections import namedtuple
import typing, BigWorld
from Event import Event
from account_helpers import getAccountDatabaseID
from adisp import adisp_async, adisp_process
from constants import CLAN_MEMBER_FLAGS
from debug_utils import LOG_ERROR
from helpers import dependency
from helpers import html
from gui.clans.formatters import getClanRoleString
from gui.shared.utils import code2str
from messenger.ext import passCensor
from messenger.storage import MessengerStorageDescriptor, UsersStorage
from shared_utils import CONST_CONTAINER
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from gui.clans.cache_providers.base_provider import IBaseProvider

class ProviderNames(CONST_CONTAINER):
    STRONGHOLD = b'STRONGHOLD'
    MISSIONS = b'MISSIONS'
    STRONGHOLD_EVENT = b'STRONGHOLD_EVENT'
    CLAN_SUPPLY = b'CLAN_SUPPLY'


class ClanInfo(namedtuple(b'ClanInfo', [
 20, 21, 22, 23, 
 24])):

    def getClanName(self):
        return self.clanName

    def getClanAbbrev(self):
        return self.clanAbbrev

    def getMembersFlags(self):
        return self.memberFlags

    def getJoiningTime(self):
        return self.enteringTime


class _ClanCache(object):
    itemsCache = dependency.descriptor(IItemsCache)
    usersStorage = MessengerStorageDescriptor(UsersStorage)

    def __init__(self):
        self.__waitForSync = False
        self.__clanMembersLen = None
        self.__clanMotto = b''
        self.__clanDescription = b''
        self.__providers = {}
        self.onSyncStarted = Event()
        self.onSyncCompleted = Event()
        return

    def init(self):
        from gui.clans.cache_providers.stronghold_provider import ClientStrongholdProvider
        from gui.clans.cache_providers.missions_provider import ClientMissionsProvider
        from gui.clans.cache_providers.stronghold_event_provider import StrongholdEventProvider
        from gui.clans.cache_providers.clan_supply_provider import ClanSupplyProvider
        for name, clazz, args in (
         (
          ProviderNames.STRONGHOLD, ClientStrongholdProvider, ()),
         (
          ProviderNames.MISSIONS, ClientMissionsProvider, ()),
         (
          ProviderNames.STRONGHOLD_EVENT, StrongholdEventProvider, (self,)),
         (
          ProviderNames.CLAN_SUPPLY, ClanSupplyProvider, ())):
            self.__registerProvider(name, clazz, args)

        return

    def fini(self):
        self.onSyncStarted.clear()
        self.onSyncCompleted.clear()
        self.__stopProviders(withClear=True)
        self.__providers.clear()
        return

    def onAccountShowGUI(self):
        self.__startProviders()
        return

    def onAvatarBecomePlayer(self):
        self.__stopProviders()
        return

    def onDisconnected(self):
        self.__stopProviders(withClear=True)
        return

    def clear(self):
        self.__stopProviders()
        return

    @property
    def clanDBID(self):
        return self.itemsCache.items.stats.clanDBID

    @property
    def isInClan(self):
        return self.clanDBID is not None and self.clanDBID != 0

    @property
    def clanMembers(self):
        members = set()
        if self.isInClan:
            members = set(self.usersStorage.getClanMembersIterator(False))
        return members

    @property
    def clanInfo(self):
        info = self.itemsCache.items.stats.clanInfo
        if info and len(info) > 1:
            return info
        else:
            return (None, None, -1, 0, 0)

    @property
    def clanName(self):
        return passCensor(self.clanInfo[0])

    @property
    def clanAbbrev(self):
        return self.clanInfo[1]

    @property
    def clanMotto(self):
        return self.__clanMotto

    @property
    def clanDescription(self):
        return self.__clanDescription

    @property
    def clanTag(self):
        result = self.clanAbbrev
        if result:
            return b'[%s]' % result
        return result

    @property
    def clanCommanderName(self):
        for member in self.clanMembers:
            if member.getClanRole() == CLAN_MEMBER_FLAGS.LEADER:
                return member.getName()

        return

    @property
    def clanRole(self):
        user = self.usersStorage.getUser(getAccountDatabaseID())
        if user:
            role = user.getClanRole()
        else:
            role = 0
        return role

    @property
    def isClanLeader(self):
        return self.clanRole == CLAN_MEMBER_FLAGS.LEADER

    @property
    def strongholdProvider(self):
        return self.__providers.get(ProviderNames.STRONGHOLD)

    @property
    def strongholdEventProvider(self):
        return self.__providers.get(ProviderNames.STRONGHOLD_EVENT)

    @property
    def clanSupplyProvider(self):
        return self.__providers.get(ProviderNames.CLAN_SUPPLY)

    @adisp_async
    def getFileFromServer(self, clanId, fileType, callback):
        if not BigWorld.player().serverSettings[b'file_server'].has_key(fileType):
            LOG_ERROR(b"Invalid server's file type: %s" % fileType)
            self._valueResponse(0, (None, None), callback)
            return
        else:
            clanEmblems = BigWorld.player().serverSettings[b'file_server'][fileType]
            BigWorld.player().customFilesCache.get(clanEmblems[b'url_template'] % clanId, (lambda url, file: self._valueResponse(0, (url, file), callback)), True)
            return

    @adisp_async
    @adisp_process
    def getClanEmblemTextureID(self, clanDBID, isBig, textureID, callback):
        import imghdr
        if clanDBID is not None and clanDBID != 0:
            _, clanEmblemFile = yield self.getFileFromServer(clanDBID, b'clan_emblems_small' if not isBig else b'clan_emblems_big')
            if clanEmblemFile and imghdr.what(None, clanEmblemFile) is not None:
                BigWorld.wg_addTempScaleformTexture(textureID, clanEmblemFile)
                callback(textureID)
                return
        callback(None)
        return

    def getClanRoleUserString(self):
        position = self.clanInfo[3]
        return getClanRoleString(position)

    def onClanInfoReceived(self, clanDBID, clanName, clanAbbrev, clanMotto, clanDescription):
        self.__clanMotto = passCensor(html.escape(clanMotto))
        self.__clanDescription = passCensor(html.escape(clanDescription))
        return

    def _valueResponse(self, resID, value, callback):
        if resID < 0:
            LOG_ERROR(b'[class %s] There is error while getting data from cache: %s[%d]' % (
             self.__class__.__name__, code2str(resID), resID))
            return callback(value)
        callback(value)
        return

    def __registerProvider(self, providerName, providerClazz, args):
        self.__providers[providerName] = providerClazz(*args)
        return

    def __startProviders(self):
        for provider in self.__providers.values():
            provider.start()

        return

    def __stopProviders(self, withClear=False):
        for provider in self.__providers.values():
            provider.stop(withClear=withClear)

        return

    def __me_onClanMembersListChanged(self):
        clanMembersLen = len(self.clanMembers)
        if self.__clanMembersLen is not None and clanMembersLen != self.__clanMembersLen:
            self.__clanMembersLen = clanMembersLen
        return


g_clanCache = _ClanCache()
