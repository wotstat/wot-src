import BigWorld
from AvatarInputHandler import MapCaseMode
from Math import Vector2
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from portal.sounds.sound_constants import PortalUISound
from portal.sounds.sound_helpers import play2DSound

class PortalStrikeSelector(MapCaseMode._ArcadeBomberStrikeSelector):
    pass


class SentryGunPortalSelector(MapCaseMode._ArcadeBomberStrikeSelector):
    __OBSTACLES_CLASS_NAMES = (b'Vehicle',)
    __DEFAULT_BOUNDING_RADIUS = 8
    __BOUNDING_OFFSET = 2

    def __init__(self, position, equipment):
        MapCaseMode._ArcadeBomberStrikeSelector.__init__(self, position, equipment)
        self.__checkIntersectObstacle()
        return

    def processSelection(self, position, reset=False):
        if not reset and self.isIntersectObstacle():
            play2DSound(PortalUISound.NOT_APPLY_SOUND)
            return False
        return MapCaseMode._ArcadeBomberStrikeSelector.processSelection(self, position, reset)

    def tick(self):
        super(SentryGunPortalSelector, self).tick()
        self.__checkIntersectObstacle()
        return

    def isIntersectObstacle(self):
        obstacles = [e for e in BigWorld.entities.values() if e.__class__.__name__ in self.__OBSTACLES_CLASS_NAMES]
        return any(self.__obstacleIntersected(obstacles))

    def __obstacleIntersected(self, obstacles):
        for obstacle in obstacles:
            obstacleBoundingRadius = self.__DEFAULT_BOUNDING_RADIUS
            if hasattr(obstacle, b'typeDescriptor') and hasattr(obstacle.typeDescriptor.hull, b'hitTester'):
                hitTester = obstacle.typeDescriptor.hull.hitTester
                if hasattr(hitTester, b'bbox') and hitTester.bbox is not None:
                    hullBboxMin, hullBboxMax, _ = hitTester.bbox
                    obstacleBoundingRadius = Vector2(hullBboxMax.x - hullBboxMin.x, hullBboxMax.z - hullBboxMin.z).length
            if abs(self.area.position.y - obstacle.position.y > 50):
                continue
            if self.area.pointInsideCircle(obstacle.position, obstacleBoundingRadius + self.__BOUNDING_OFFSET):
                yield obstacle

        return

    def __checkIntersectObstacle(self):
        if self.isIntersectObstacle():
            self.area.setColor(int(4290649856L))
        else:
            self.area.setColor(int(4287615196L))
        return


class _PortalMinesSensor(object):
    _sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, intersectChecker):
        self.__intersectChecker = intersectChecker
        return

    def destroy(self):
        self.__intersectChecker = None
        return

    def isIntersectMine(self):
        allyMines = [e for e in BigWorld.entities.values() if (e.__class__.__name__ == b'BasicMine' or e.__class__.__name__ == b'PortalMine') and self._sessionProvider.getArenaDP().isAlly(e.ownerVehicleID)]
        return any(self.__intersectChecker(allyMines))


class MinefieldPortalSelector(MapCaseMode._ArcadeBomberStrikeSelector, _PortalMinesSensor):

    def __init__(self, position, equipment):
        MapCaseMode._ArcadeBomberStrikeSelector.__init__(self, position, equipment)
        _PortalMinesSensor.__init__(self, self.__minesIntersected)
        self.__checkIntersectMines()
        return

    def destroy(self):
        MapCaseMode._ArcadeBomberStrikeSelector.destroy(self)
        _PortalMinesSensor.destroy(self)
        return

    def processSelection(self, position, reset=False):
        if not reset and self.isIntersectMine():
            play2DSound(PortalUISound.NOT_APPLY_SOUND)
            ctrl = self._sessionProvider.shared.messages
            if ctrl is not None:
                ctrl.showVehicleError(b'minefieldIsIntersected')
            return False
        return MapCaseMode._ArcadeBomberStrikeSelector.processSelection(self, position, reset)

    def tick(self):
        super(MinefieldPortalSelector, self).tick()
        self.__checkIntersectMines()
        return

    def __minesIntersected(self, mines):
        for m in mines:
            if self.area.pointInside(m.position):
                yield m

        return

    def __checkIntersectMines(self):
        if self.isIntersectMine():
            self.area.setColor(int(4290649856L))
        else:
            self.area.setColor(int(4287615196L))
        return


class PortalVehicleTrapSelector(MapCaseMode._ArenaBoundsAreaStrikeSelector):
    pass
