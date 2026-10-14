from __future__ import absolute_import
from future.moves import pickle
import VSE

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

    def handleScriptEventFromServer(self, eventName, params, targetAspects, eventScope):
        if self.__enabled:
            if eventScope.startswith(b'ArenaT:') and self.arena is not None:
                eventScope = b'ArenaT:' + str(self.arena.arenaUniqueID)
            VSE.passEventToVisualScript(eventName, pickle.loads(params), targetAspects, eventScope)
        return
