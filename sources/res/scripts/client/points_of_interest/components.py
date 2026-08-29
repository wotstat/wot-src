import enum, typing, BigWorld, CGF
if typing.TYPE_CHECKING:
    from points_of_interest_shared import PoiType
    from helpers.fixed_dict import StatusWithTimeInterval
    from points_of_interest.mixins import PointsOfInterestListener

@enum.unique
class PoiStateUpdateMask(enum.IntEnum):
    NONE = 0
    PROGRESS = 1
    INVADER = 2
    STATUS = 4
    ALL = PROGRESS | INVADER | STATUS


class PoiStateComponent(object):
    __slots__ = (b'id', b'type', b'_progress', b'_invader', b'_status', b'_updatedFields')

    def __init__(self, poiID, poiType, progress, invader, status):
        self.id = poiID
        self.type = poiType
        self._progress = progress
        self._invader = invader
        self._status = status
        self._updatedFields = PoiStateUpdateMask.ALL
        return

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, progress):
        self._progress = progress
        self._updatedFields |= PoiStateUpdateMask.PROGRESS
        return

    @property
    def invader(self):
        return self._invader

    @invader.setter
    def invader(self, invader):
        self._invader = invader
        self._updatedFields |= PoiStateUpdateMask.INVADER
        return

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
        self._updatedFields |= PoiStateUpdateMask.STATUS
        return

    @property
    def updatedFields(self):
        return self._updatedFields

    def resetUpdatedFields(self):
        self._updatedFields = PoiStateUpdateMask.NONE
        return


class PoiStateUIListenerComponent(object):
    __slots__ = (b'listener',)

    def __init__(self, listener):
        self.listener = listener
        return


class PoiCaptureBlockerStateComponent(object):
    __slots__ = (b'id', b'blockReasons', b'poiState')

    def __init__(self, poiID, blockReasons):
        self.id = poiID
        self.blockReasons = blockReasons
        poi = BigWorld.entities.get(poiID)
        self.poiState = CGF.ComponentLink(poi.entityGameObject, PoiStateComponent) if poi is not None else None
        return


class PoiVehicleStateComponent(object):
    __slots__ = (b'id',)

    def __init__(self, poiID):
        self.id = poiID
        return
