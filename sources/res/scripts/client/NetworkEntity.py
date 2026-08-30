import CGF, BigWorld, cgf_network
from debug_utils import LOG_DEBUG_DEV
cache = dict()

class NetworkEntity(BigWorld.Entity):
    ignoreEntityGOSync = True

    def __init__(self):
        super(NetworkEntity, self).__init__()
        self.entityGameObject = None
        return

    def onEnterWorld(self, _):
        if CGF.addNetworkEntity(self.spaceID, self, self.unique_id, self.prefab_path):
            direction = (
             self.yaw, self.pitch, self.roll)
            LOG_DEBUG_DEV((b'New NetworkEntity [{}][{}] position {} rotation {} scale {}').format(self.id, self.unique_id, self.position, direction, self.scale))
        return

    def onConnected(self):
        cache[self.unique_id] = self.entityGameObject
        return

    def onLeaveWorld(self):
        if CGF.removeGameObject(cache[self.unique_id]):
            self.entityGameObject = None
            LOG_DEBUG_DEV((b'Removed NetworkEntity [{}]').format(self.id))
        return

    @property
    def gameObject(self):
        return self.entityGameObject

    @property
    def isConnected(self):
        return self.entityGameObject is not None

    def onDynamicComponentCreated(self, component):
        if not self.isConnected:
            return
        self.__processAddComponent(self.entityGameObject, component)
        return

    def onDynamicComponentDestroyed(self, component):
        if not self.isConnected:
            return
        self.__processRemoveComponent(self.entityGameObject, component)
        return

    def activateGameObject(self, id):
        cgf_network.activateGameObject(self.gameObject, id)
        return

    def activateGameObjectUnique(self, id):
        cgf_network.activateGameObjectByUniqueID(self.gameObject, id)
        return

    def deactivateGameObject(self, id):
        cgf_network.deactivateGameObject(self.gameObject, id)
        return

    def deactivateGameObjectUnique(self, id):
        cgf_network.deactivateGameObjectByUniqueID(self.gameObject, id)
        return

    def createGameObject(self, id):
        cgf_network.createGameObject(self.gameObject, id)
        return

    def removeGameObject(self, id):
        cgf_network.removeGameObject(self.gameObject, id)
        return

    def removeGameObjectUnique(self, id):
        cgf_network.removeGameObjectByUniqueID(self.gameObject, id)
        return

    @staticmethod
    def __processAddComponent(go, component):
        existing = go.findComponentByType(type(component))
        if existing is None:
            go.addComponent(component)
        return

    @staticmethod
    def __processRemoveComponent(go, component):
        existing = go.findComponentByType(type(component))
        if existing is component:
            go.removeComponent(component)
        return
