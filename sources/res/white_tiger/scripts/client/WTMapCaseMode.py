from __future__ import absolute_import
import logging
from aih_constants import CTRL_MODE_NAME
from AvatarInputHandler.DynamicCameras.camera_switcher import SwitchToPlaces
import BigWorld, SoundGroups
from AvatarInputHandler.MapCaseMode import MapCaseControlMode
_logger = logging.getLogger(__name__)

class HyperionMapCaseControlMode(MapCaseControlMode):
    MODE_NAME = CTRL_MODE_NAME.MAP_CASE
    _WT_HYPERION_OVERLAY_SOUND_ID = {True: b'ev_white_tiger_waiting_overlay_ambient', 
       False: b'ev_white_tiger_waiting_overlay_ambient_stop'}
    _WT_HYPERION_OVERLAY_STATE_GROUP = b'STATE_white_tiger_gameplay_waiting'
    _WT_HYPERION_OVERLAY_STATE = {True: b'STATE_white_tiger_gameplay_waiting_on', 
       False: b'STATE_white_tiger_gameplay_waiting_off'}

    def _enableCamera(self, arcadeState):
        self.camera.enable(BigWorld.player().position, False, switchToPos=1.0, switchToPlace=SwitchToPlaces.TO_RELATIVE_POS)
        return

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
