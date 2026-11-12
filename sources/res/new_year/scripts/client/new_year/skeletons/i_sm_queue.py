class IStateMachineQueue(object):
    __slots__ = ()

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def lock(self):
        raise NotImplementedError
        return

    def release(self):
        raise NotImplementedError
        return

    def bind(self, personaType, animatorComponent):
        raise NotImplementedError
        return

    def unbind(self, personaType):
        raise NotImplementedError
        return

    def handleCloseUp(self, personaType, state):
        raise NotImplementedError
        return

    def handleRewards(self, personaType, rewards):
        raise NotImplementedError
        return

    def handleLoaded(self):
        raise NotImplementedError
        return
