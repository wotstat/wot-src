from visual_script import ASPECT
from visual_script.block import Block, Meta
from visual_script.dependency import dependencyImporter
from visual_script.slot_types import SLOT_TYPE
utils, dependency, cameras, hangar_camera_manager, CGF, game_control, lock_overlays, InputHandler, Keys = dependencyImporter(b'skeletons.gui.shared.utils', b'helpers.dependency', b'AvatarInputHandler.cameras', b'cgf_components.hangar_camera_manager', b'CGF', b'skeletons.gui.game_control', b'gui.shared.lock_overlays', b'gui.InputHandler', b'Keys')

class CameraMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 6750207

    @classmethod
    def blockCategory(cls):
        return b'Camera'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/camera'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR, ASPECT.CLIENT]


class GetCamera(Block, CameraMeta):
    hangarSpace = dependency.descriptor(utils.IHangarSpace)

    def __init__(self, *args, **kwargs):
        super(GetCamera, self).__init__(*args, **kwargs)
        self._position = self._makeDataOutputSlot(b'position', SLOT_TYPE.VECTOR3, self._getPosition)
        self._direction = self._makeDataOutputSlot(b'direction', SLOT_TYPE.VECTOR3, self._getDirection)
        return

    def _getPosition(self):
        _, position = cameras.getWorldRayAndPosition()
        self._position.setValue(position)
        return

    def _getDirection(self):
        direction, _ = cameras.getWorldRayAndPosition()
        direction.normalise()
        self._direction.setValue(direction)
        return


class SwitchCamera(Block, CameraMeta):

    def __init__(self, *args, **kwargs):
        super(SwitchCamera, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._cameraName = self._makeDataInputSlot(b'cameraName', SLOT_TYPE.STR)
        self._spaceId = self._makeDataInputSlot(b'spaceId', SLOT_TYPE.INT)
        self._instantly = self._makeDataInputSlot(b'instantly', SLOT_TYPE.BOOL)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        cameraName = self._cameraName.getValue()
        spaceId = self._spaceId.getValue()
        cameraManager = CGF.getSystem(spaceId, hangar_camera_manager.HangarCameraSystem)
        if cameraManager:
            cameraManager.switchByCameraName(cameraName, self._instantly.getValue())
        self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class ActivateCameraWithOverlay(Block, CameraMeta):
    overlay = dependency.descriptor(game_control.IOverlayController)

    def __init__(self, *args, **kwargs):
        super(ActivateCameraWithOverlay, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._cameraName = self._makeDataInputSlot(b'cameraName', SLOT_TYPE.STR)
        self._spaceId = self._makeDataInputSlot(b'spaceId', SLOT_TYPE.INT)
        self._out = self._makeEventOutputSlot(b'out')
        self._onCancel = self._makeEventOutputSlot(b'onCancel')
        return

    def onStartScript(self):
        InputHandler.g_instance.onKeyDown += self._handleKeyEvent
        return

    def onFinishScript(self):
        InputHandler.g_instance.onKeyDown -= self._handleKeyEvent
        return

    def _handleKeyEvent(self, event):
        if event.key == Keys.KEY_ESCAPE:
            self._onCancel.call()
        return

    def _execute(self):
        cameraName = self._cameraName.getValue()
        spaceId = self._spaceId.getValue()
        cameraManager = CGF.getSystem(spaceId, hangar_camera_manager.HangarCameraSystem)
        if cameraManager:
            cameraManager.activateCamera(cameraName)
        self.overlay.setOverlayState(True)
        lock_overlays.lockNotificationManager(lock=True)
        self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class DeactivateCameraWithOverlay(Block, CameraMeta):
    overlay = dependency.descriptor(game_control.IOverlayController)

    def __init__(self, *args, **kwargs):
        super(DeactivateCameraWithOverlay, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._spaceId = self._makeDataInputSlot(b'spaceId', SLOT_TYPE.INT)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        spaceId = self._spaceId.getValue()
        cameraManager = CGF.getSystem(spaceId, hangar_camera_manager.HangarCameraSystem)
        if cameraManager:
            cameraManager.switchToTank()
        self.overlay.setOverlayState(False)
        lock_overlays.lockNotificationManager(lock=False)
        self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class OnCameraSwitched(Block, CameraMeta):

    def __init__(self, *args, **kwargs):
        super(OnCameraSwitched, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._initialize)
        self._spaceID = self._makeDataInputSlot(b'spaceID', SLOT_TYPE.INT)
        self._out = self._makeEventOutputSlot(b'out')
        self._cameraName = self._makeDataOutputSlot(b'cameraName', SLOT_TYPE.STR, None)
        return

    def _initialize(self):
        cameraManager = CGF.getSystem(self._spaceID.getValue(), hangar_camera_manager.HangarCameraSystem)
        if cameraManager:
            cameraManager.onCameraSwitched += self._onCameraSwitched
        return

    def _onCameraSwitched(self, cameraName):
        self._cameraName.setValue(cameraName)
        self._out.call()
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class GetCameraName(Block, CameraMeta):

    def __init__(self, *args, **kwargs):
        super(GetCameraName, self).__init__(*args, **kwargs)
        self._spaceId = self._makeDataInputSlot(b'spaceId', SLOT_TYPE.INT)
        self._cameraName = self._makeDataOutputSlot(b'cameraName', SLOT_TYPE.STR, self._execute)
        return

    def _execute(self):
        spaceId = self._spaceId.getValue()
        cameraManager = CGF.getSystem(spaceId, hangar_camera_manager.HangarCameraSystem)
        if cameraManager:
            self._cameraName.setValue(cameraManager.getCurrentCameraName())
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]
