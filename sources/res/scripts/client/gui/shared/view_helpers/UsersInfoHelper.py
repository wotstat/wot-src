from __future__ import absolute_import
import logging
from collections import defaultdict
from Event import Event
from constants import IGR_TYPE
from debug_utils import LOG_DEBUG
from gui.shared import formatters as shared_fmts
from gui.shared.view_helpers.UsersInfoController import UsersInfoController
from helpers import dependency
from messenger import g_settings
from messenger.m_constants import USER_GUI_TYPE, UserEntityScope, USER_TAG
from messenger.proto import proto_getter, PROTO_TYPE
from messenger.proto.entities import SharedUserEntity
from messenger.storage import MessengerStorageDescriptor, UsersStorage
from skeletons.gui.lobby_context import ILobbyContext
_logger = logging.getLogger(__name__)

class UsersInfoHelper(object):
    lobbyContext = dependency.descriptor(ILobbyContext)
    _rqCtrl = UsersInfoController()
    usersStorage = MessengerStorageDescriptor(UsersStorage)

    def __init__(self):
        self._invalid = defaultdict(set)
        self.__callback = None
        self.onNamesReceived = Event()
        return

    def __del__(self):
        self._invalid.clear()
        return

    @classmethod
    def clear(cls):
        LOG_DEBUG(b'Users info helper stop')
        cls._rqCtrl.stopProcessing()
        return

    @classmethod
    def fini(cls):
        cls.clear()
        cls._rqCtrl.fini()
        return

    def onUserNamesReceived(self, names):
        self.onNamesReceived()
        return

    def onUserRatingsReceived(self, ratings):
        return

    def onUserClanAbbrevsReceived(self, abbrevs):
        return

    @proto_getter(PROTO_TYPE.XMPP)
    def proto(self):
        return

    def getContact(self, userID, scope=UserEntityScope.LOBBY):
        user = self.usersStorage.getUser(userID, scope=scope)
        if not user:
            user = SharedUserEntity(userID)
            self.usersStorage.addUser(user)
        return user

    def getUserName(self, userID, scope=UserEntityScope.LOBBY):
        user = self.getContact(userID, scope=scope)
        if not user.hasValidName():
            self._invalid[b'names'].add(userID)
            if self.proto.isConnected():
                return b''
        return user.getName()

    def getUserClanAbbrev(self, userDbID):
        return self.getContact(userDbID).getClanAbbrev()

    def getUserRegionCode(self, userDbID):
        return self.lobbyContext.getRegionCode(userDbID)

    def getUserRating(self, userDbID):
        user = self.getContact(userDbID)
        if not user.hasValidRating():
            self._invalid[b'ratings'].add(userDbID)
        return user.getGlobalRating()

    def buildGuiUserData(self, user):
        userDbID = user.getID()
        colorGetter = g_settings.getColorScheme(b'rosters').getColors
        return {b'userName': (self.getGuiUserName(userDbID)), 
           b'clanAbbrev': (self.getUserClanAbbrev(userDbID)), 
           b'region': (self.getUserRegionCode(userDbID)), 
           b'tags': (user.getTags() if user else []), 
           b'dbID': userDbID, 
           b'colors': (colorGetter(user.getGuiType() if user else USER_GUI_TYPE.OTHER))}

    def getGuiUserData(self, userDbID):
        user = self.getContact(userDbID)
        return self.buildGuiUserData(user)

    def getGuiUserDataWithStatus(self, userDbID):
        user = self.getContact(userDbID)
        return (user.hasValidName() and user.hasValidRating(), self.buildGuiUserData(user))

    def getGuiUserName(self, userID, formatter=(lambda v: v), scope=UserEntityScope.LOBBY):
        userName = self.getUserName(userID, scope=scope)
        if userName:
            return formatter(userName)
        return b''

    def getGuiUserRating(self, userDbID, formatter=(lambda v: v)):
        userRating = self.getUserRating(userDbID)
        if userRating != b'0':
            return formatter(shared_fmts.getGlobalRatingFmt(userRating))
        return b'-1'

    def getUserTags(self, userID, igrType):
        contact = self.usersStorage.getUser(userID, scope=UserEntityScope.BATTLE)
        if contact is not None:
            userTags = contact.getTags()
        else:
            userTags = set()
        if igrType == IGR_TYPE.BASE:
            userTags.add(USER_TAG.IGR_BASE)
        elif igrType == IGR_TYPE.PREMIUM:
            userTags.add(USER_TAG.IGR_PREMIUM)
        return userTags

    def syncUsersInfo(self):
        if self._invalid[b'names']:
            self._rqCtrl.requestNicknames(list(self._invalid[b'names']), (lambda names, _: self.onUserNamesReceived(names)))
        if self._invalid[b'ratings']:
            self._rqCtrl.requestGlobalRatings(list(self._invalid[b'ratings']), self.onUserRatingsReceived)
        self._invalid.clear()
        return
