import Event

class TriggersController(object):

    def __init__(self):
        self.__enabled = False
        self.onTrigger = Event.Event()
        return

    def onBecomePlayer(self):
        self.__enabled = True
        return

    def onBecomeNonPlayer(self):
        self.__enabled = False
        return

    def externalTrigger(self, eventId, extra):
        if not self.__enabled:
            return
        self.onTrigger(eventId, extra)
        return

    def handleKey(self, isDown, key, mods):
        return
