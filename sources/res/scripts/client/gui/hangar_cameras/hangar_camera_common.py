from enum import Enum
from gui.shared.events import HasCtxEvent

class CameraMovementStates(object):
    ON_OBJECT = 0
    MOVING_TO_OBJECT = 1
    FROM_OBJECT = 2


class CameraDistanceModes(Enum):
    DEFAULT = 0
    CUSTOM = 1


class CameraRelatedEvents(HasCtxEvent):
    CAMERA_ENTITY_UPDATED = b'CameraEntityUpdate'
    IDLE_CAMERA = b'IdleCamera'
    VEHICLE_LOADING = b'VehicleLoading'
    LOBBY_VIEW_MOUSE_MOVE = b'MouseMove'
    FORCE_DISABLE_IDLE_PARALAX_MOVEMENT = b'cameraRelatedEvents/forceDisableIdleParalaxMovement'
    FORCE_DISABLE_CAMERA_MOVEMENT = b'cameraRelatedEvents/forceDisableCameraMovement'
