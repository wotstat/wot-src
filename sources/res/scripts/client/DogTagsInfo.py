import typing, BigWorld, Event
if typing.TYPE_CHECKING:
    from typing import List, Tuple

class DogTagsInfo(BigWorld.DynamicScriptComponent):

    def __init__(self):
        self.__eManager = Event.EventManager()
        self.onUsedComponentsUpdated = Event.Event(self.__eManager)
        return

    def onLeaveWorld(self, *args):
        self.__eManager.clear()
        return

    def setSlice_usedDogTagsComponents(self, changePath, oldValue):
        begin, end = changePath[0]
        newComponents = self.usedDogTagsComponents[begin:end]
        self.onUsedComponentsUpdated(newComponents)
        return
