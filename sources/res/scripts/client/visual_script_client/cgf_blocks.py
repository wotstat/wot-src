import weakref, BigWorld, logging, GenericComponents
from debug_utils import LOG_WARNING
from visual_script.block import Block
from visual_script.slot_types import SLOT_TYPE
from visual_script.misc import ASPECT, errorVScript
from visual_script.dependency import dependencyImporter
from visual_script.contexts.cgf_context import GameObjectWrapper, CGFGameObjectContext
from constants import ROCKET_ACCELERATION_STATE
from visual_script.cgf_blocks import CGFMeta
Vehicle, CGF, tankStructure, RAC = dependencyImporter(b'Vehicle', b'CGF', b'vehicle_systems.tankStructure', b'cgf_components.rocket_acceleration_component')
_logger = logging.getLogger(__name__)

class GetEntityGameObject(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(GetEntityGameObject, self).__init__(*args, **kwargs)
        self._entity = self._makeDataInputSlot(b'entity', SLOT_TYPE.ENTITY)
        self._gameObject = self._makeDataOutputSlot(b'gameObject', SLOT_TYPE.GAME_OBJECT, self._exec)
        return

    def _exec(self):
        entity = self._entity.getValue()
        gameObject = entity.entityGameObject
        goWrapper = GameObjectWrapper(gameObject)
        self._gameObject.setValue(weakref.proxy(goWrapper))
        return


class GetVehicleAppearanceGameObject(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleAppearanceGameObject, self).__init__(*args, **kwargs)
        self._object = self._makeDataInputSlot(b'gameObject', SLOT_TYPE.GAME_OBJECT)
        self._appObject = self._makeDataOutputSlot(b'appearanceObject', SLOT_TYPE.GAME_OBJECT, self._exec)
        return

    def validate(self):
        if not self._object.hasValue():
            return b'GameObject is required'
        return super(GetVehicleAppearanceGameObject, self).validate()

    def _exec(self):
        currentGO = self._object.getValue()
        hierarchy = CGF.HierarchyManager(currentGO.spaceID)
        topGO = hierarchy.getTopMostParent(currentGO)
        currentGO = hierarchy.findFirstNode(topGO, tankStructure.CgfTankNodes.TANK_ROOT)
        if currentGO is not None:
            goWrapper = GameObjectWrapper(currentGO)
            self._appObject.setValue(weakref.proxy(goWrapper))
        else:
            self._appObject.setValue(None)
        return


class GetVehicleGameObject(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(GetVehicleGameObject, self).__init__(*args, **kwargs)
        self._object = self._makeDataInputSlot(b'gameObject', SLOT_TYPE.GAME_OBJECT)
        self._vehicleObject = self._makeDataOutputSlot(b'vehicleObject', SLOT_TYPE.GAME_OBJECT, self._exec)
        return

    def validate(self):
        if not self._object.hasValue():
            return b'GameObject is required'
        return super(GetVehicleGameObject, self).validate()

    def _exec(self):
        currentGO = self._object.getValue()
        hierarchy = CGF.HierarchyManager(currentGO.spaceID)
        topGO = hierarchy.getTopMostParent(currentGO)
        if topGO.findComponentByType(Vehicle.Vehicle) is not None:
            goWrapper = GameObjectWrapper(topGO)
            self._vehicleObject.setValue(weakref.proxy(goWrapper))
        else:
            self._vehicleObject.setValue(None)
        return


class GetHangarVehicleGameObject(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(GetHangarVehicleGameObject, self).__init__(*args, **kwargs)
        self._object = self._makeDataInputSlot(b'gameObject', SLOT_TYPE.GAME_OBJECT)
        self._vehicleObject = self._makeDataOutputSlot(b'hangarVehicleObject', SLOT_TYPE.GAME_OBJECT, self._exec)
        return

    def validate(self):
        if not self._object.hasValue():
            return b'GameObject is required'
        return super(GetHangarVehicleGameObject, self).validate()

    def _exec(self):
        currentGO = self._object.getValue()
        hierarchy = CGF.HierarchyManager(currentGO.spaceID)
        topGO = hierarchy.getTopMostParent(currentGO)
        if topGO.findComponentByType(GenericComponents.EntityGOSync) is not None:
            goWrapper = GameObjectWrapper(topGO)
            self._vehicleObject.setValue(weakref.proxy(goWrapper))
        else:
            self._vehicleObject.setValue(None)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class PushVseTrigger(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(PushVseTrigger, self).__init__(*args, **kwargs)
        self._trigger = self._makeEventInputSlot(b'push_trigger', self._exec)
        self._object = self._makeDataInputSlot(b'game_object', SLOT_TYPE.GAME_OBJECT)
        self._triggerName = self._makeDataInputSlot(b'trigger_name', SLOT_TYPE.STR)
        return

    def validate(self):
        if not self._object.hasValue():
            return b'GameObject is required'
        if not self._triggerName.hasValue():
            return b'Trigger Name is required'
        return super(PushVseTrigger, self).validate()

    def _exec(self):
        go = self._object.getValue()
        if go is None or not go.isValid:
            return
        vseComponent = go.findComponentByType(GenericComponents.VSEComponent)
        if vseComponent is None:
            _logger.error(b'GameObject does not contain VSEComponent')
            return
        else:
            context = vseComponent.context
            if not isinstance(context, CGFGameObjectContext):
                _logger.error(b'%s not supported', type(context))
                return
            triggerName = self._triggerName.getValue()
            context.onTriggerEvent(triggerName)
            return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class RocketAcceleratorEvents(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(RocketAcceleratorEvents, self).__init__(*args, **kwargs)
        self._activate = self._makeEventInputSlot(b'activate', self.__activate)
        self._deactivate = self._makeEventInputSlot(b'deactivate', self.__deactivate)
        self._object = self._makeDataInputSlot(b'vehicleObject', SLOT_TYPE.GAME_OBJECT)
        self._activateOut = self._makeEventOutputSlot(b'activateOut')
        self._deactivateOut = self._makeEventOutputSlot(b'deactivateOut')
        self._failure = self._makeEventOutputSlot(b'failure')
        self._deploying = self._makeEventOutputSlot(ROCKET_ACCELERATION_STATE.toString(ROCKET_ACCELERATION_STATE.DEPLOYING))
        self._preparing = self._makeEventOutputSlot(ROCKET_ACCELERATION_STATE.toString(ROCKET_ACCELERATION_STATE.PREPARING))
        self._empty = self._makeEventOutputSlot(ROCKET_ACCELERATION_STATE.toString(ROCKET_ACCELERATION_STATE.EMPTY))
        self._ready = self._makeEventOutputSlot(ROCKET_ACCELERATION_STATE.toString(ROCKET_ACCELERATION_STATE.READY))
        self._active = self._makeEventOutputSlot(ROCKET_ACCELERATION_STATE.toString(ROCKET_ACCELERATION_STATE.ACTIVE))
        self._disabled = self._makeEventOutputSlot(ROCKET_ACCELERATION_STATE.toString(ROCKET_ACCELERATION_STATE.DISABLED))
        self._tryActivate = self._makeEventOutputSlot(b'tryActivate')
        self._duration = self._makeDataOutputSlot(b'duration', SLOT_TYPE.FLOAT, None)
        self.__switcher = {}
        self.__controllerLink = None
        return

    def __activate(self):
        go, provider, errorMsg = _extractRACComponent(self._object)
        if errorMsg:
            LOG_WARNING(b'[VScript] RocketAcceleratorEvents:', errorMsg)
            self._writeLog(errorMsg)
            self._failure.call()
            return
        self.__switcher = {(ROCKET_ACCELERATION_STATE.NOT_RUNNING): (lambda *args: None), 
           (ROCKET_ACCELERATION_STATE.DEPLOYING): (lambda status: self._deploying.call()), 
           (ROCKET_ACCELERATION_STATE.PREPARING): (lambda status: self._preparing.call()), 
           (ROCKET_ACCELERATION_STATE.READY): (lambda status: self._ready.call()), 
           (ROCKET_ACCELERATION_STATE.ACTIVE): (lambda status: self._active.call()), 
           (ROCKET_ACCELERATION_STATE.DISABLED): (lambda status: self._disabled.call()), 
           (ROCKET_ACCELERATION_STATE.EMPTY): (lambda status: self._empty.call())}
        provider.subscribe(self.__onStateChange, self.__onTryActivate)
        self.__controllerLink = CGF.ComponentLink(go, RAC.RocketAccelerationController)
        self._activateOut.call()
        return

    def __deactivate(self):
        self.__switcher = None
        if self.__controllerLink:
            controller = self.__controllerLink() if self.__controllerLink else None
            if controller:
                controller.unsubscribe(self.__onStateChange, self.__onTryActivate)
            self.__controllerLink = None
        else:
            LOG_WARNING(b'')
        self._deactivateOut.call()
        return

    def __onStateChange(self, status):
        self._duration.setValue(status.endTime - BigWorld.serverTime())
        self.__switcher.get(status.status, self.__onWrongState)(status)
        return

    def __onTryActivate(self):
        self._tryActivate.call()
        return

    def __onWrongState(self, *args, **kwargs):
        errorVScript(self, b'RocketAcceleratorEvents: Set state called with undefined value')
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


class RocketAcceleratorSettings(Block, CGFMeta):

    def __init__(self, *args, **kwargs):
        super(RocketAcceleratorSettings, self).__init__(*args, **kwargs)
        self._activate = self._makeEventInputSlot(b'in', self.__execute)
        self._object = self._makeDataInputSlot(b'vehicleObject', SLOT_TYPE.GAME_OBJECT)
        self._out = self._makeEventOutputSlot(b'out')
        self._failure = self._makeEventOutputSlot(b'failure')
        self._isPlayer = self._makeDataOutputSlot(b'isPlayer', SLOT_TYPE.BOOL, None)
        return

    def __execute(self):
        _, provider, errorMsg = _extractRACComponent(self._object)
        if errorMsg:
            LOG_WARNING(b'[VScript]: RocketAcceleratorSettings', errorMsg)
            self._failure.call()
            self._writeLog(errorMsg)
        else:
            self._isPlayer.setValue(provider.entity.isPlayerVehicle)
            self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT]


def _extractRACComponent(gameObjectLink):
    go = gameObjectLink.getValue()
    if not go.isValid:
        return (None, None, b'Input game object is not valid')
    else:
        provider = go.findComponentByType(RAC.RocketAccelerationController)
        if provider is None:
            return (None, None, b'No RocketAccelerationController can be found')
        return (go, provider, None)
