class IPrbControlLoader(object):
    __slots__ = ()

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def getDispatcher(self):
        raise NotImplementedError
        return

    def getInvitesManager(self):
        raise NotImplementedError
        return

    def getAutoInvitesNotifier(self):
        raise NotImplementedError
        return

    def getPeripheriesHandler(self):
        raise NotImplementedError
        return

    def getStorage(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def setEnabled(self, enabled):
        raise NotImplementedError
        return

    def onAccountShowGUI(self, ctx):
        raise NotImplementedError
        return

    def onAvatarBecomePlayer(self):
        raise NotImplementedError
        return

    def onDisconnected(self):
        raise NotImplementedError
        return
