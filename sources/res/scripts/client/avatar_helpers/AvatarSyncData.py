import AccountCommands

class AvatarSyncData(object):

    def __init__(self):
        self.__isSynchronized = False
        self.__subscribers = []
        self.__avatar = None
        return

    def setAvatar(self, avatar):
        self.__avatar = avatar
        return

    def onAvatarBecomePlayer(self):
        self.__isSynchronized = self.__avatar.isSynchronized()
        if not self.__isSynchronized:
            self.__avatar._doCmdStr(AccountCommands.CMD_GET_AVATAR_SYNC, b'', self.__onSyncResponse)
        return

    def onAvatarBecomeNonPlayer(self):
        return

    def waitForSync(self, callback):
        if self.__isSynchronized:
            callback(AccountCommands.RES_CACHE)
        if callback is not None:
            self.__subscribers.append(callback)
        return

    def __onSyncResponse(self, syncID, resultID, ext=None):
        ext = ext or {}
        self.__isSynchronized = True
        subscribers = self.__subscribers
        self.__subscribers = []
        for callback in subscribers:
            callback(resultID)

        return
