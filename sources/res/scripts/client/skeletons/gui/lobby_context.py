import typing
if typing.TYPE_CHECKING:
    from Event import Event
    from helpers.server_settings import ServerSettings

class ILobbyContext(object):
    onServerSettingsChanged = None

    @property
    def collectUiStats(self):
        raise NotImplementedError
        return

    @property
    def needLogUXEvents(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def onAccountBecomePlayer(self):
        raise NotImplementedError
        return

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError
        return

    def getArenaUniqueIDByClientID(self, clientArenaID):
        raise NotImplementedError
        return

    def getClientIDByArenaUniqueID(self, arenaUniqueID):
        raise NotImplementedError
        return

    def setCredentials(self, login, token):
        raise NotImplementedError
        return

    def getCredentials(self):
        raise NotImplementedError
        return

    def isAccountComplete(self):
        raise NotImplementedError
        return

    def setAccountComplete(self, isComplete):
        raise NotImplementedError
        return

    def getBattlesCount(self):
        raise NotImplementedError
        return

    def update(self, diff):
        raise NotImplementedError
        return

    def updateBattlesCount(self, battlesCount, epicBattlesCount):
        raise NotImplementedError
        return

    def updateGuiCtx(self, ctx):
        raise NotImplementedError
        return

    def getGuiCtx(self):
        raise NotImplementedError
        return

    def getServerSettings(self):
        raise NotImplementedError
        return

    def setServerSettings(self, serverSettings):
        raise NotImplementedError
        return

    def getPlayerFullName(self, pName, clanInfo=None, clanAbbrev=None, regionCode=None, pDBID=None):
        raise NotImplementedError
        return

    def getClanAbbrev(self, clanInfo):
        raise NotImplementedError
        return

    def getRegionCode(self, dbID):
        raise NotImplementedError
        return

    def isAnotherPeriphery(self, peripheryID):
        raise NotImplementedError
        return

    def isPeripheryAvailable(self, peripheryID, itemsCache=None):
        raise NotImplementedError
        return

    def getPeripheryName(self, peripheryID, checkAnother=True, useShortName=False):
        raise NotImplementedError
        return

    def addHeaderNavigationConfirmator(self, confirmator):
        raise NotImplementedError
        return

    def deleteHeaderNavigationConfirmator(self, confirmator):
        raise NotImplementedError
        return

    def isHeaderNavigationPossible(self, callback=None, alias=None):
        raise NotImplementedError
        return

    def addFightButtonConfirmator(self, confirmator):
        raise NotImplementedError
        return

    def deleteFightButtonConfirmator(self, confirmator):
        raise NotImplementedError
        return

    def isFightButtonPressPossible(self, callback=None):
        raise NotImplementedError
        return

    def addPlatoonCreationConfirmator(self, confirmator):
        raise NotImplementedError
        return

    def deletePlatoonCreationConfirmator(self, confirmator):
        raise NotImplementedError
        return

    def isPlatoonCreationPossible(self, callback=None):
        raise NotImplementedError
        return
