class ISoundsController(object):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def start(self):
        raise NotImplementedError
        return

    def stop(self, isDisconnected=False):
        raise NotImplementedError
        return

    @property
    def system(self):
        raise NotImplementedError
        return

    def enable(self):
        raise NotImplementedError
        return

    def disable(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def setEnvForSpace(self, spaceID, newEnv):
        raise NotImplementedError
        return
