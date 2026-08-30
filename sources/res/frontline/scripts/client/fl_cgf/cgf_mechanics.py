import BigWorld, CGF, Math
from GenericComponents import TransformComponent, AnimatorComponent, RemoveGoDelayedComponent
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import autoregister, onAddedQuery, onRemovedQuery, onProcessQuery
from constants import IS_CLIENT
from debug_utils import LOG_DEBUG
from items.vehicles import CAMOUFLAGE_KIND_INDICES
if IS_CLIENT:
    from helpers import dependency
    from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID
    from skeletons.gui.battle_session import IBattleSessionProvider
else:

    class DependencyMock(object):

        @staticmethod
        def descriptor(_):
            return


    class IBattleSessionProvider(object):
        pass


    dependency = DependencyMock()
BALOON_DEAD_PREFAB = b'content/CGFPrefabs/Frontline/Baloon_Crash.prefab'

@registerComponent
class DeadAirshipComponent(object):
    domain = CGF.DomainOption.DomainClient

    def __init__(self, velocity):
        self.velocity = velocity
        return


@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient)
class DeadAirshipManager(CGF.ComponentManager):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def activate(self):
        if self.sessionProvider:
            ctrl = self.sessionProvider.shared.feedback
            if ctrl:
                ctrl.onVehicleFeedbackReceived += self.__onVehicleFeedbackReceived
        return

    def deactivate(self):
        if self.sessionProvider:
            ctrl = self.sessionProvider.shared.feedback
            if ctrl:
                ctrl.onVehicleFeedbackReceived -= self.__onVehicleFeedbackReceived
        return

    @onProcessQuery(TransformComponent, DeadAirshipComponent, tickGroup=b'Simulation')
    def onProcessMoving(self, transform, deadAirship):
        transform.position += deadAirship.velocity * self.clock.gameDelta
        return

    def __onVehicleFeedbackReceived(self, eventID, vehicleID, _):
        if eventID != FEEDBACK_EVENT_ID.VEHICLE_DEAD:
            return
        vehicle = BigWorld.entities.get(vehicleID)
        if vehicle and vehicle.typeDescriptor.isAirCraft:
            velocity = vehicle.filter.velocity
            velocity.y = 0

            def _loadCb(go):
                go.createComponent(DeadAirshipComponent, velocity)
                LOG_DEBUG(b'[SupplyComponentManager] Baloon crashed prefab is loaded')
                return

            CGF.loadGameObject(BALOON_DEAD_PREFAB, self.spaceID, Math.Matrix(vehicle.matrix), _loadCb)
        return


@registerComponent
class SupplySpawnComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'Supply Spawn Component'
    category = b'Frontline'
    camouflagePrefabPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'camouflage prefab path', value=b'')


@registerComponent
class SupplyCamouflage(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'Supply Camouflage'
    category = b'Frontline'
    winter = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'winter sequence path', value=b'')
    summer = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'summer sequence path', value=b'')
    desert = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'desert sequence path', value=b'')

    def getSequencePath(self):
        if IS_CLIENT:
            if BigWorld.player() is None:
                return b''
            return getattr(self, CAMOUFLAGE_KIND_INDICES[BigWorld.player().arena.arenaType.vehicleCamouflageKind])
        else:
            return self.summer


@autoregister(presentInAllWorlds=True, domain=CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor, category=b'Frontline')
class EpicBattlesComponentManager(CGF.ComponentManager):

    def __init__(self, *args):
        super(EpicBattlesComponentManager, self).__init__(*args)
        self.__camouflageGOs = {}
        return

    @onAddedQuery(CGF.GameObject, SupplySpawnComponent, TransformComponent)
    def onAddedSupplyComponent(self, go, supplySpawnComponent, transform):

        def setGO(newGameObject):
            self.__camouflageGOs[go.id] = newGameObject
            return

        CGF.loadGameObject(supplySpawnComponent.camouflagePrefabPath, go.spaceID, transform.worldTransform, setGO)
        return

    @onRemovedQuery(CGF.GameObject, SupplySpawnComponent)
    def onRemovedSupplyComponent(self, go, _):
        camouflageGO = self.__camouflageGOs.pop(go.id)
        if camouflageGO:
            animComponent = camouflageGO.findComponentByType(AnimatorComponent)
            if animComponent is not None:
                duration = animComponent.getDuration()
                animComponent.unpause()
                animComponent.start()
                camouflageGO.createComponent(RemoveGoDelayedComponent, duration)
            else:
                CGF.removeGameObject(camouflageGO)
        return

    @onAddedQuery(CGF.GameObject, SupplyCamouflage)
    def onAddedCamouflageGO(self, go, camouflage):
        for camouflageGO in self.__camouflageGOs.itervalues():
            if go.id == camouflageGO.id and camouflage.getSequencePath():
                go.createComponent(AnimatorComponent, camouflage.getSequencePath(), 0, 1, 1, True, b'')
                return

        return

    @onAddedQuery(CGF.GameObject, SupplyCamouflage, AnimatorComponent)
    def onAddedCamouflageAnimator(self, go, camouflage, animComponent):
        animComponent.start()
        animComponent.pause()
        return
