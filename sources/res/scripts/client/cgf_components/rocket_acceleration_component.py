import logging
from functools import partial
import CGF, BigWorld
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent
from cgf_script.managers_registrator import autoregister, onAddedQuery, onRemovedQuery, tickGroup
from GameplayDebug import DebugTextComponent
from constants import IS_CLIENT, IS_DEVELOPMENT
from constants import ROCKET_ACCELERATION_STATE
from GenericComponents import VSEComponent
if IS_CLIENT:
    from RocketAccelerationController import RocketAccelerationController
else:

    class RocketAccelerationController(object):
        pass


_logger = logging.getLogger(__name__)

class SoundEvents(object):
    ROCKET_ACCELERATION_READY = b'ev_rocket_accel_ready'
    ROCKET_ACCELERATION_ACTIVE_PC = b'ev_rocket_accel_start_PC'
    ROCKET_ACCELERATION_ACTIVE_NPC = b'ev_rocket_accel_start_NPC'
    ROCKET_ACCELERATION_STOP_PC = b'ev_rocket_accel_stop_PC'
    ROCKET_ACCELERATION_STOP_NPC = b'ev_rocket_accel_stop_NPC'
    ROCKET_ACCELERATION_DISABLE = b'ev_rocket_accel_disable'
    ROCKET_ACCELERATION_EMPTY = b'ev_rocket_accel_empty'


@registerComponent
class RocketAccelerationTerrainEffect(object):
    editorTitle = b'Rocket Accelerator Terrain Effect'
    category = b'Rocket Accelerator'
    domain = CGF.DomainOption.DomainClient
    snow = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Snow', value=CGF.GameObject)
    sand = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Sand', value=CGF.GameObject)
    ground = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Ground', value=CGF.GameObject)
    stone = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Stone', value=CGF.GameObject)


@registerComponent
class RocketAccelerationStateListener(object):
    editorTitle = b'Rocket Accelerator State Listener'
    category = b'Rocket Accelerator'
    domain = CGF.DomainOption.DomainClient
    vseComponent = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'VS Plan', value=VSEComponent)
    start = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Start Object', value=CGF.GameObject)
    idle = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Idle Object', value=CGF.GameObject)
    end = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Stop Object', value=CGF.GameObject)
    sound_l = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Left Sound', value=CGF.GameObject)
    sound_r = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Right Sound', value=CGF.GameObject)
    startDuration = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Start Duration', value=0.2)
    endDuration = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'End Duration', value=0.2)
    soundReady = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Ready sound', value=SoundEvents.ROCKET_ACCELERATION_READY)
    soundActivePC = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Active PC sound', value=SoundEvents.ROCKET_ACCELERATION_ACTIVE_PC)
    soundActiveNPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Active NPC sound', value=SoundEvents.ROCKET_ACCELERATION_ACTIVE_NPC)
    soundStopPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Stop PC sound', value=SoundEvents.ROCKET_ACCELERATION_STOP_PC)
    soundStopNPC = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Stop NPC sound', value=SoundEvents.ROCKET_ACCELERATION_STOP_NPC)
    soundDisable = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Disable sound', value=SoundEvents.ROCKET_ACCELERATION_DISABLE)
    soundEmpty = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Empty sound', value=SoundEvents.ROCKET_ACCELERATION_EMPTY)


@autoregister(presentInAllWorlds=True)
class RocketAccelerationManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, RocketAccelerationStateListener)
    def onListenerAdded(self, go, listener):
        hierarchy = CGF.HierarchyManager(go.spaceID)
        root = hierarchy.getTopMostParent(go)
        provider = root.findComponentByType(RocketAccelerationController)
        if provider is None:
            _logger.error(b'Failed to find RocketAccelerationController')
            return
        else:
            plan = listener.vseComponent()
            if plan is not None:
                plan.start()
                return
            _logger.error(b'RAM: Failed to setup visual script plan')
            return

    @onRemovedQuery(RocketAccelerationStateListener)
    def onListenerRemoved(self, listener):
        plan = listener.vseComponent()
        if plan is not None:
            plan.stop()
        return

    @onRemovedQuery(RocketAccelerationController)
    def onProviderRemoved(self, provider):
        provider.cleanup()
        return


if IS_DEVELOPMENT:

    @autoregister(presentInAllWorlds=True)
    class RocketAccelerationManagerDebug(CGF.ComponentManager):

        def __init__(self):
            super(RocketAccelerationManagerDebug, self).__init__()
            self.__texts = {}
            self.__listeners = {}
            return

        @onAddedQuery(CGF.GameObject, RocketAccelerationStateListener)
        def onListenerAdded(self, go, listener):
            hierarchy = CGF.HierarchyManager(go.spaceID)
            root = hierarchy.getTopMostParent(go)
            provider = root.findComponentByType(RocketAccelerationController)
            self.__setupDebugStateHandling(go, provider)
            return

        @onRemovedQuery(CGF.GameObject, RocketAccelerationStateListener)
        def onListenerRemoved(self, go, listener):
            hierarchy = CGF.HierarchyManager(go.spaceID)
            root = hierarchy.getTopMostParent(go)
            self.__texts.pop(root, None)
            callback = self.__listeners.pop(go, None)
            provider = root.findComponentByType(RocketAccelerationController)
            if provider is not None:
                provider.unsubscribe(callback)
            return

        @onRemovedQuery(RocketAccelerationController)
        def onProviderRemoved(self, provider):
            provider.cleanup()
            return

        @tickGroup(b'Simulation', 0.3)
        def update(self):
            for updater in self.__texts.values():
                updater()

            return

        def onStateUpdate(self, root, link, status):
            self.__updateState(root, link, ROCKET_ACCELERATION_STATE.toString(status.status).upper(), status)
            return

        def __updateState(self, root, link, value, status):
            if status.timeLeft > 0.0:
                self.__updateTextWithDuration(link, value, status.reuseCount, status.endTime)
                self.__texts[root] = partial(self.__updateTextWithDuration, link, value, status.reuseCount, status.endTime)
            else:
                self.__updateText(link, value, status.reuseCount)
                self.__texts.pop(root, None)
            return

        def __updateText(self, link, value, count):
            text = link()
            if text is not None:
                text.setText((b'[RAM][{}][{}]').format(value, count), (0, 0, 0), (1.0, 1.0, 1.0, 1.0))
            return

        def __updateTextWithDuration(self, link, value, count, end):
            duration = max(0, end - BigWorld.serverTime())
            text = link()
            if text is not None:
                text.setText((b'[RAM][{}][{}][{:.2f}]').format(value, count, duration), (0, 0, 0), (1.0, 1.0, 1.0, 1.0))
            return

        def __setupDebugStateHandling(self, root, provider):
            if root.findComponentByType(DebugTextComponent) is None:
                root.createComponent(DebugTextComponent, b'', (0, 0, 0), (1.0, 1.0, 1.0, 1.0))
            self.__listeners[root] = partial(self.onStateUpdate, root, CGF.ComponentLink(root, DebugTextComponent))
            if provider is not None:
                provider.subscribe(self.__listeners[root])
            return
