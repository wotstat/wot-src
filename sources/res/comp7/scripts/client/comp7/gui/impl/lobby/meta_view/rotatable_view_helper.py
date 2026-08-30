import CGF
from enum import Enum
from ClientSelectableCameraObject import ClientSelectableCameraObject
from cgf_components.hangar_camera_manager import HangarCameraSystem
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from helpers import dependency
from skeletons.gui.shared.utils import IHangarSpace

class Comp7Cameras(Enum):
    DEFAULT = b'Tank'
    SHOP = b'Comp7ShopCamera'
    PURCHASE = b'PreShopCameraStart'
    PRE_FLYBY = b'PreStartShopCamera'


class RotatableViewHelper(object):
    __hangarSpace = dependency.descriptor(IHangarSpace)

    def getCameraManager(self):
        spaceID = self.__hangarSpace.spaceID
        if spaceID is not None:
            return CGF.getSystem(spaceID, HangarCameraSystem)
        else:
            return

    def getCameraEvents(self, viewModel):
        cameraEvents = [
         (
          viewModel.onMoveSpace, self.__onMoveSpace),
         (
          viewModel.onMouseOver3dScene, self.__onMouseOver3dScene)]
        return cameraEvents

    def switchCamera(self, cameraName, instantly):
        cameraManager = self.getCameraManager()
        if cameraManager is not None and cameraManager.getCurrentCameraName() != cameraName:
            cameraManager.switchByCameraName(cameraName, instantly)
            ClientSelectableCameraObject.deselectAll()
            if self.__hangarSpace.spaceInited:
                self.__hangarSpace.space.getVehicleEntity().onSelect(True)
        return

    def resetCamera(self, duration=0):
        cameraManager = self.getCameraManager()
        if cameraManager is not None:
            cameraManager.resetCameraTarget(duration)
        return

    @staticmethod
    def __onMoveSpace(args=None):
        if args is None:
            return
        else:
            dx = args.get(b'dx')
            dy = args.get(b'dy')
            dz = args.get(b'dz')
            g_eventBus.handleEvent(CameraRelatedEvents(CameraRelatedEvents.LOBBY_VIEW_MOUSE_MOVE, ctx={b'dx': dx, b'dy': dy, b'dz': dz}), EVENT_BUS_SCOPE.GLOBAL)
            return

    @staticmethod
    def __onMouseOver3dScene(args):
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.NOTIFY_CURSOR_OVER_3DSCENE, ctx={b'isOver3dScene': (bool(args.get(b'isOver3dScene')))}))
        return
