import BigWorld, math
from Math import Vector2, Vector3
import logging, SoundGroups
from CombatSelectedArea import CombatSelectedArea
from aih_constants import CTRL_MODE_NAME
from AvatarInputHandler.MapCaseMode import MapCaseControlMode, _AreaStrikeSelector, _VehiclesSelector, _ArenaBoundsAreaStrikeSelector
from gui.battle_control import avatar_getter
_logger = logging.getLogger(__name__)

class HyperionMapCaseControlMode(MapCaseControlMode):
    MODE_NAME = CTRL_MODE_NAME.MAP_CASE_HYPERION
    _WT_HYPERION_OVERLAY_SOUND_ID = {True: b'ev_white_tiger_waiting_overlay_ambient', 
       False: b'ev_white_tiger_waiting_overlay_ambient_stop'}
    _WT_HYPERION_OVERLAY_STATE_GROUP = b'STATE_white_tiger_gameplay_waiting'
    _WT_HYPERION_OVERLAY_STATE = {True: b'STATE_white_tiger_gameplay_waiting_on', 
       False: b'STATE_white_tiger_gameplay_waiting_off'}

    def enable(self, **args):
        super(HyperionMapCaseControlMode, self).enable(**args)
        self.__playSound(True)
        return

    def disable(self):
        wasEnabled = self.isEnabled
        super(HyperionMapCaseControlMode, self).disable()
        if wasEnabled:
            self.__playSound(False)
        return

    def __playSound(self, start):
        soundEventName = self._WT_HYPERION_OVERLAY_SOUND_ID.get(start)
        SoundGroups.g_instance.playSound2D(soundEventName)
        self.__setSoundState(start)
        return

    def __setSoundState(self, setState):
        stateName = self._WT_HYPERION_OVERLAY_STATE.get(setState)
        SoundGroups.g_instance.setState(self._WT_HYPERION_OVERLAY_STATE_GROUP, stateName)
        return


class HyperionStrikeSelector(_AreaStrikeSelector, _VehiclesSelector):

    def __init__(self, position, equipment):
        self._radius = 75.0
        _AreaStrikeSelector.__init__(self, position, equipment)
        _VehiclesSelector.__init__(self, self.__intersected, selectPlayer=True)
        return

    def destroy(self):
        _VehiclesSelector.destroy(self)
        _AreaStrikeSelector.destroy(self)
        return

    def tick(self):
        self.highlightVehicles()
        return

    def _getAreaSize(self):
        return 2.0 * Vector2(self._radius, self._radius)

    def _createArea(self, equipment, position, direction):
        visualPath = equipment.aimCircleVisual
        area = CombatSelectedArea()
        area.setup(position, direction, self._getAreaSize(), visualPath, color=None, marker=None)
        return area

    def __intersected(self, vehicles):
        for v in vehicles:
            if self.area.pointInsideCircle(v.position, self._radius):
                yield v

        return


class CloneSelector(_ArenaBoundsAreaStrikeSelector):

    def __init__(self, position, equipment):
        super(CloneSelector, self).__init__(position, equipment)
        self.area.enableWaterCollision(True)
        self.__useVehPosition = equipment.useVehPosition
        self.__playerVeh = avatar_getter.getPlayerVehicle()
        self.__updateDirection()
        return

    def processHover(self, position, force=False):
        if self.__useVehPosition:
            position = self.__playerVeh.position
            self.area.relocate(position, self.direction)
            self.writeStateToReplay()
        else:
            super(CloneSelector, self).processHover(position, force)
        self.__updateDirection()
        return

    def __updateDirection(self):
        attachedV = BigWorld.player().getVehicleAttached()
        if attachedV is not None:
            self.direction = Vector3(math.sin(attachedV.yaw), 0, math.cos(attachedV.yaw))
        return
