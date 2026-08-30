from __future__ import absolute_import
from Event import Event

class DisconnectReason(object):
    UNDEFINED = 0
    REQUEST = 1
    EVENT = 2
    KICK = 3
    ERROR = 4


class IConnectionManager(object):
    onLoggedOn = None
    onConnected = None
    onRejected = None
    onDisconnected = None
    onKickedFromServer = None
    onKickWhileLoginReceived = None
    onQueued = None
    onPeripheryRoutingGroupUpdated = None

    @property
    def serverUserName(self):
        raise NotImplementedError
        return

    @property
    def serverUserNameShort(self):
        raise NotImplementedError
        return

    @property
    def peripheryID(self):
        raise NotImplementedError
        return

    @property
    def areaID(self):
        raise NotImplementedError
        return

    @property
    def url(self):
        raise NotImplementedError
        return

    @property
    def loginName(self):
        raise NotImplementedError
        return

    @property
    def lastLoginName(self):
        raise NotImplementedError
        return

    @property
    def databaseID(self):
        raise NotImplementedError
        return

    @property
    def connectionMethod(self):
        raise NotImplementedError
        return

    @property
    def peripheryRoutingGroup(self):
        raise NotImplementedError
        return

    @property
    def availableHosts(self):
        raise NotImplementedError
        return

    def isAvailablePeriphery(self, peripheryID=None):
        raise NotImplementedError
        return

    def initiateConnection(self, params, password, serverName):
        raise NotImplementedError
        return

    def stopRetryConnection(self):
        raise NotImplementedError
        return

    def disconnect(self):
        raise NotImplementedError
        return

    def setKickedFromServer(self, reason, kickReasonType, expiryTime):
        raise NotImplementedError
        return

    def isDisconnected(self):
        raise NotImplementedError
        return

    def isStandalone(self):
        raise NotImplementedError
        return

    def isConnected(self):
        raise NotImplementedError
        return

    def checkClientServerVersions(self, clientVersion, serverVersion):
        raise NotImplementedError
        return

    def setLastLogin(self, email):
        raise NotImplementedError
        return

    def setPeripheryRoutingGroup(self, routingGroup, availableHosts):
        raise NotImplementedError
        return
