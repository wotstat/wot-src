import cPickle, VSE

class VisualScriptController(object):

    def __init__(self):
        self.__enabled = False
        return

    def onBecomePlayer(self):
        self.__enabled = True
        return

    def onBecomeNonPlayer(self):
        self.__enabled = False
        return

    def handleKey(self, isDown, key, mods):
        return

    def handleScriptEventFromServer(self, eventName, planName, params, targetAspects, eventScope):
        if self.__enabled:
            if eventScope.startswith(b'ArenaT:') and self.arena is not None:
                eventScope = b'ArenaT:' + str(self.arena.arenaUniqueID)
            VSE.passEventToVisualScript(eventName, planName, cPickle.loads(params), targetAspects, eventScope)
        return
