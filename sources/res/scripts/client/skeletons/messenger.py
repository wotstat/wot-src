class IMessengerEntry(object):

    @property
    def protos(self):
        raise NotImplementedError
        return

    @property
    def storage(self):
        raise NotImplementedError
        return

    @property
    def gui(self):
        raise NotImplementedError
        return

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def onAccountShowGUI(self):
        raise NotImplementedError
        return

    def onAvatarInitGUI(self):
        raise NotImplementedError
        return

    def onAvatarShowGUI(self):
        raise NotImplementedError
        return
