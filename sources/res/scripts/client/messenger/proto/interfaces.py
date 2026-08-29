class IProtoPlugin(object):
    __slots__ = (b'__weakref__',)

    def connect(self, scope):
        return

    def disconnect(self):
        return

    def view(self, scope):
        return

    def goToReplay(self):
        return

    def setFilters(self, msgFilterChain):
        return

    def init(self):
        return

    def clear(self):
        return

    def isConnected(self):
        return False


class IProtoSettings(object):

    def update(self, data):
        return

    def clear(self):
        return

    def isEnabled(self):
        return False


class IProtoLimits(object):

    def getMessageMaxLength(self):
        raise NotImplementedError
        return

    def getBroadcastCoolDown(self):
        raise NotImplementedError
        return

    def getHistoryMaxLength(self):
        raise NotImplementedError
        return


class IBattleCommandFactory(object):

    def createByName(self, name):
        return

    def createByNameTarget(self, name, targetID):
        return

    def createByPosition(self, position, name, reloadTime=0.0):
        return

    def createByObjectiveIndex(self, idx, isAtk, actionName):
        return

    def createByBaseIndexAndName(self, pointID, commandName, baseName):
        return

    def createReloadingCommand(self, isCassetteClip, timeLeft, quantity, hasAutoShoot):
        return

    def createOverheatCantShootCommand(self, timeLeft):
        return

    def createReplyByName(self, replyID, replyType, replierID):
        return

    def createCancelReplyByName(self, replyID, replyType, replierID):
        return

    def createClearChatCommandsFromTarget(self, targetID, targetMarkerType):
        return


class IUnitCommandFactory(object):
    pass


class IEntityFindCriteria(object):

    def filter(self, entity):
        return False


class ISearchHandler(object):

    def onSearchComplete(self, result):
        return

    def onSearchFailed(self, reason):
        return

    def onExcludeFromSearch(self, entity):
        return


class ISearchProcessor(object):

    def addHandler(self, handler):
        return

    def removeHandler(self, handler):
        return

    def find(self, token, **kwargs):
        return

    def getSearchResultLimit(self):
        return 0


class IChatMessage(object):

    def getMessage(self):
        return b''


class IChatError(IChatMessage):

    def getTitle(self):
        return b''

    def isModal(self):
        return False


class IVOIPChatProvider(object):

    def getChannelParams(self):
        return (b'', b'')

    def requestCredentials(self, reset=0):
        return

    def logVivoxLogin(self):
        return


class IVOIPChatController(object):

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def isReady(self):
        raise NotImplementedError
        return

    def isPlayerSpeaking(self, accountDBID):
        raise NotImplementedError
        return

    def isVOIPEnabled(self):
        raise NotImplementedError
        return

    def isVivox(self):
        raise NotImplementedError
        return

    def isYY(self):
        raise NotImplementedError
        return

    def invalidateInitialization(self):
        raise NotImplementedError
        return

    def requestCaptureDevices(self, firstTime=False, callback=None):
        raise NotImplementedError
        return

    def isCurrentChannelEnabled(self):
        raise NotImplementedError
        return

    def enableCurrentChannel(self, enabled):
        raise NotImplementedError
        return


class IUserSearchLimits(object):

    def getMaxResultSize(self):
        raise NotImplementedError
        return

    def getRequestCooldown(self):
        raise NotImplementedError
        return
