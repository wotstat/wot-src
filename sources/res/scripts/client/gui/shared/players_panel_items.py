import logging
from enum import Enum
import BigWorld
_logger = logging.getLogger(__name__)

class PlayersPanelItems(Enum):
    DEFAULT = 0
    CAMP = 1
    CAPTURED_BOMB = 3
    FREE_BOMB = 4


class IComponent(object):
    __slots__ = ()

    def getType(self):
        raise NotImplementedError
        return

    def setValuesOnCreate(self, entity):
        raise NotImplementedError
        return

    def setValuesOnDestroy(self, entity):
        raise NotImplementedError
        return


class Camp(IComponent):
    __slots__ = (b'__campUdo', b'__isAlive', b'__campId')

    def __init__(self, *args, **kwargs):
        self.__campUdo = b''
        self.__isAlive = True
        self.__campId = 0
        return

    @property
    def campUdo(self):
        return self.__campUdo

    @property
    def isAlive(self):
        return self.__isAlive

    @property
    def campId(self):
        return self.__campId

    def getType(self):
        return PlayersPanelItems.CAMP.name

    def setValuesOnCreate(self, entity):
        wtUdo = entity.dynamicComponents.get(b'wtUdo')
        wtIndex = entity.dynamicComponents.get(b'wtIndex')
        if wtUdo is None or wtIndex is None:
            _logger.error(b'Some component is not found to get camp properties')
            return False
        else:
            self.__campUdo = wtUdo.guid
            self.__isAlive = True
            self.__campId = wtIndex.index
            return True

    def setValuesOnDestroy(self, entity):
        self.__isAlive = False
        return True


class _BaseTimer(IComponent):
    __slots__ = (b'_subtype', b'_timerID', b'_endTime', b'_leftTime', b'_totalTime')

    def __init__(self, subtype, *args, **kwargs):
        self._subtype = subtype
        self._timerID = 0
        self._endTime = 0
        self._leftTime = 0
        self._totalTime = 0
        return

    def getType(self):
        return self._subtype

    @property
    def timerID(self):
        return self._timerID

    @property
    def endTime(self):
        return self._endTime

    @property
    def leftTime(self):
        return self._leftTime

    @property
    def totalTime(self):
        return self._totalTime

    def setValuesOnCreate(self, entity):
        return False

    def setValuesOnDestroy(self, entity):
        self._timerID = entity.id
        self._endTime = BigWorld.serverTime()
        self._leftTime = 0
        return True


class BombTimer(_BaseTimer):
    __slots__ = (b'_isPaused', b'_factor', b'_timerGUID')

    def __init__(self, subtype, *args, **kwargs):
        super(BombTimer, self).__init__(subtype, *args, **kwargs)
        self._factor = 1.0
        self._isPaused = False
        self._timerGUID = 0
        return

    @property
    def isPaused(self):
        return self._isPaused

    @property
    def timerGUID(self):
        return self._timerGUID

    @property
    def factor(self):
        return self._factor

    def setValuesOnCreate(self, entity):
        stressTimer = entity.dynamicComponents.get(b'stressTimer')
        if stressTimer is None:
            return False
        else:
            self._timerID = entity.id
            self._endTime = stressTimer.timerInfo.endTime
            self._leftTime = int(round(stressTimer.timeToDelete))
            self._factor = stressTimer.factor
            self._totalTime = stressTimer.lifetime
            self._isPaused = stressTimer.isPaused
            self._timerGUID = stressTimer.getGuiID
            return True

    def setValuesOnDestroy(self, entity):
        super(BombTimer, self).setValuesOnDestroy(entity)
        return True


_ITEMS_BY_TYPE = {(PlayersPanelItems.CAMP.name): Camp, 
   (PlayersPanelItems.CAPTURED_BOMB.name): BombTimer, 
   (PlayersPanelItems.FREE_BOMB.name): BombTimer}
_PROCESS_REPLAY_TYPES = (
 PlayersPanelItems.CAPTURED_BOMB.name,)

def getGuiItemType(itemSubtype):
    itemType = _ITEMS_BY_TYPE.get(itemSubtype)
    if itemType is None:
        _logger.error(b'Unknown type of the item for the players panel')
        return
    else:
        return itemType(itemSubtype)


def isProcessReplayNeeded(itemSubtype):
    return itemSubtype in _PROCESS_REPLAY_TYPES
