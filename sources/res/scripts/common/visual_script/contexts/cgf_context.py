from __future__ import absolute_import
import weakref, BigWorld
from constants import IS_CELLAPP, IS_CLIENT
from visual_script.misc import ASPECT
from visual_script.slot_types import SLOT_TYPE
from visual_script.context import VScriptContext, vse_get_property, vse_event_out
from visual_script.dependency import dependencyImporter
if IS_CELLAPP:
    helpers, = dependencyImporter(b'helpers')

class GameObjectWrapper(object):

    def __init__(self, go):
        self.go = go
        return


class CGFGameObjectContext(VScriptContext):

    def __init__(self, gameObject, aspect):
        super(CGFGameObjectContext, self).__init__(aspect)
        self.gameObject = GameObjectWrapper(gameObject)
        if IS_CELLAPP:
            self.__arena = helpers.getArena(gameObject.spaceID)
        else:
            self.__arena = None
        return

    @vse_get_property(SLOT_TYPE.GAME_OBJECT, display_name=b'Self', description=b'Returns current context GameObject', aspects=[
     ASPECT.CLIENT, ASPECT.HANGAR, ASPECT.SERVER])
    def getSelf(self):
        return weakref.proxy(self.gameObject)

    @vse_get_property(SLOT_TYPE.ARENA, display_name=b'Arena', description=b'Returns current arena', aspects=[
     ASPECT.SERVER])
    def getArena(self):
        return weakref.proxy(self.__arena)

    @vse_event_out((), display_name=b'OnClick', description=b'Reacts on click on game object                      (only if go have CollisionComponent, IsSelectableComponent, VSEComponent)', aspects=[
     ASPECT.CLIENT, ASPECT.HANGAR])
    def onGameObjectClick(self):
        return

    @vse_event_out((), display_name=b'OnHoverIn', description=b'Reacts on hover over game object                      (only if go have CollisionComponent, VSEComponent)', aspects=[
     ASPECT.CLIENT, ASPECT.HANGAR])
    def onGameObjectHoverIn(self):
        return

    @vse_event_out((), display_name=b'OnHoverOut', description=b'Reacts on exit from hover over game object                      (only if go have CollisionComponent, VSEComponent)', aspects=[
     ASPECT.CLIENT, ASPECT.HANGAR])
    def onGameObjectHoverOut(self):
        return

    @vse_event_out(SLOT_TYPE.STR, display_name=b'OnTrigger', description=b'Custom triggered event', aspects=[
     ASPECT.CLIENT, ASPECT.HANGAR])
    def onTriggerEvent(self, eventName):
        return


def getCurrentAspect():
    if IS_CELLAPP:
        return ASPECT.SERVER
    if IS_CLIENT:
        from Account import PlayerAccount
        if isinstance(BigWorld.player(), PlayerAccount):
            return ASPECT.HANGAR
        return ASPECT.CLIENT
    return ASPECT.CLIENT


def createContext(go):
    aspect = getCurrentAspect()
    return CGFGameObjectContext(go, aspect)


def getPlanTags():
    from visual_script.plan_tags import PlanTags
    return PlanTags().tags
