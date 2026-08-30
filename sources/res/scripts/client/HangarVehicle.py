from __future__ import absolute_import
from gui.hangar_cameras.hangar_camera_common import CameraMovementStates, CameraDistanceModes
from ClientSelectableCameraVehicle import ClientSelectableCameraVehicle
from ClientSelectableCameraObject import ClientSelectableCameraObject
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events

class HangarVehicle(ClientSelectableCameraVehicle):
    hangarSpace = dependency.descriptor(IHangarSpace)

    def __init__(self):
        self.selectionId = b''
        self.clickSoundName = b''
        self.releaseSoundName = b''
        self.mouseOverSoundName = b''
        self.edgeMode = 0
        self.modelName = b''
        super(HangarVehicle, self).__init__()
        self.camDistState = CameraDistanceModes.CUSTOM
        return

    def onEnterWorld(self, prereqs):
        super(HangarVehicle, self).onEnterWorld(prereqs)
        self.hangarSpace.onSpaceCreate += self.__onSpaceCreated
        g_eventBus.addListener(events.HangarCustomizationEvent.CHANGE_VEHICLE_MODEL_TRANSFORM, self.__changeVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.addListener(events.HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__resetVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        self.setEnable(False)
        self.setState(CameraMovementStates.ON_OBJECT)
        return

    def onLeaveWorld(self):
        self.hangarSpace.onSpaceCreate -= self.__onSpaceCreated
        g_eventBus.removeListener(events.HangarCustomizationEvent.CHANGE_VEHICLE_MODEL_TRANSFORM, self.__changeVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        g_eventBus.removeListener(events.HangarCustomizationEvent.RESET_VEHICLE_MODEL_TRANSFORM, self.__resetVehicleModelTransform, scope=EVENT_BUS_SCOPE.LOBBY)
        super(HangarVehicle, self).onLeaveWorld()
        return

    def onMouseClick(self):
        super(HangarVehicle, self).onMouseClick()
        ClientSelectableCameraObject.switchCamera()
        return

    def __onSpaceCreated(self):
        self.setEnable(False)
        self.setState(CameraMovementStates.ON_OBJECT)
        return

    def _setStartValues(self):
        return

    def __changeVehicleModelTransform(self, event):
        ctx = event.ctx
        targetPos = ctx[b'targetPos']
        rotateYPR = ctx[b'rotateYPR']
        shadowYOffset = ctx[b'shadowYOffset']
        self._setVehicleModelTransform(targetPos, rotateYPR, shadowYOffset)
        return

    def __resetVehicleModelTransform(self, event):
        self._resetVehicleModelTransform()
        return
