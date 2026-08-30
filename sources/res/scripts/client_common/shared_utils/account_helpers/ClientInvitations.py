from __future__ import absolute_import
from collections import namedtuple
from functools import partial
from future.utils import viewvalues
import BigWorld, AccountCommands
from constants import INVITATION_STATUS
from helpers.time_utils import getCurrentTimestamp, getServerUTCTime
from debug_utils import LOG_DEBUG, LOG_ERROR, LOG_CURRENT_EXCEPTION
from shared_utils import safeCancelCallback
UniqueId = namedtuple(b'UniqueId', [b'id', b'senderID'])

class InvitationScope(object):
    AVATAR = 0
    ACCOUNT = 1


class ClientInvitations(object):

    def __init__(self, playerEvents):
        self.__proxy = None
        self.__expCbID = None
        self.__invitations = {}
        self.__playerEvents = playerEvents
        return

    def clear(self):
        self._clearExpiryCallback()
        return

    def getInvites(self):
        return self.__invitations

    def setProxy(self, proxy):
        self.__proxy = proxy
        return

    def onProxyBecomePlayer(self):
        return

    def onProxyBecomeNonPlayer(self):
        return

    def processInvitations(self, invitations, scope):
        LOG_DEBUG(b'ClientInvitations::processInvitations', invitations)
        for inv in invitations:
            senderID = inv.get(b'senderDBID', 0)
            senderVehID = inv.get(b'senderVehID', 0)
            if scope == InvitationScope.ACCOUNT:
                if senderVehID:
                    uniqueId = UniqueId(inv[b'id'], senderVehID)
                    if uniqueId in self.__invitations:
                        del self.__invitations[uniqueId]
            if (scope == InvitationScope.AVATAR or not senderID) and senderVehID:
                senderID = senderVehID
            if senderID:
                uniqueId = UniqueId(inv[b'id'], senderID)
                self.__invitations[uniqueId] = inv

        self._loadExpiryCallback()
        self.__playerEvents.onPrebattleInvitationsChanged(self.__invitations)
        return

    def sendInvitation(self, accountsToInvite, comment=b'', callback=None):
        if self.__playerEvents.isPlayerEntityChanging:
            return
        self.__proxy._doCmdIntArrStrArr(AccountCommands.CMD_INVITATION_SEND, accountsToInvite, [comment], callback)
        return

    def acceptInvitation(self, invitationID, senderID, callback=None):
        if self.__playerEvents.isPlayerEntityChanging:
            return
        proxy = partial(self._onInvitationResponseReceived, INVITATION_STATUS.ACCEPTED, invitationID, senderID, callback)
        self.__proxy._doCmdInt3(AccountCommands.CMD_INVITATION_ACCEPT, invitationID, senderID, 0, proxy)
        self.__playerEvents.onPrebattleInvitationAccepted(invitationID, senderID)
        return

    def declineInvitation(self, invitationID, senderID, callback=None):
        if self.__playerEvents.isPlayerEntityChanging:
            return
        proxy = partial(self._onInvitationResponseReceived, INVITATION_STATUS.DECLINED, invitationID, senderID, callback)
        self.__proxy._doCmdInt3(AccountCommands.CMD_INVITATION_DECLINE, invitationID, senderID, 0, proxy)
        return

    def _onInvitationResponseReceived(self, newStatus, invitationId, senderID, callback, _, code, errStr):
        if AccountCommands.isCodeValid(code):
            uniqueId = UniqueId(invitationId, senderID)
            try:
                self.__invitations[uniqueId][b'status'] = newStatus
                self.__playerEvents.onPrebattleInvitationsChanged(self.__invitations)
            except KeyError:
                LOG_ERROR(b'Unknown invitation', uniqueId, self.__invitations, callback, code, errStr)

        else:
            self.__playerEvents.onPrebattleInvitationsError(invitationId, code, errStr)
        if callback is not None:
            callback(code, errStr)
        return

    def _cancelInvitations(self, predicate):
        for inv in viewvalues(self.__invitations):
            if predicate(inv):
                inv[b'status'] = INVITATION_STATUS.ERROR

        return

    def _loadExpiryCallback(self):
        self._clearExpiryCallback()
        if self.__invitations:
            inviteId = min(self.__invitations, key=(lambda k: self.__invitations[k][b'expiresAt']))
            invite = self.__invitations[inviteId]
            expTime = max(invite[b'expiresAt'] - getServerUTCTime(), 0.0)
            self.__expCbID = BigWorld.callback(expTime, partial(self.__onInviteExpired, inviteId))
            LOG_DEBUG(b'Invite expiration callback has been loaded', inviteId, expTime)
        return

    def _clearExpiryCallback(self):
        if self.__expCbID is not None:
            safeCancelCallback(self.__expCbID)
            self.__expCbID = None
        return

    def __onInviteExpired(self, inviteId):
        try:
            del self.__invitations[inviteId]
            self.__playerEvents.onPrebattleInvitationsChanged(self.__invitations)
        except KeyError:
            LOG_ERROR(b'There is error while removing expired invite')
            LOG_CURRENT_EXCEPTION()

        self._loadExpiryCallback()
        return


class ReplayClientInvitations(ClientInvitations):

    def processInvitations(self, invitations, scope):
        for inv in invitations:
            inv[b'expiresAt'] = getCurrentTimestamp() + 86400

        super(ReplayClientInvitations, self).processInvitations(invitations, scope)
        return
