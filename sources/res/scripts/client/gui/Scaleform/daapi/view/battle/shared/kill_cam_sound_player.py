from __future__ import absolute_import, division
import WWISE, BigWorld
from AvatarInputHandler.DynamicCameras.kill_cam_camera import CallbackPauseManager
from gui.battle_control import avatar_getter
from gui.battle_control.controllers.kill_cam_ctrl import KillCamInfoMarkerType, DistanceMarkerData
from gui.battle_control.view_components import IViewComponentsCtrlListener
from gui.shared.events import DeathCamEvent
from helpers import dependency
from math_common import decimal_round
from skeletons.gui.battle_session import IBattleSessionProvider
_TRAJECTORY_PROGRESS_DELAY = 0.1

class _DeathCamSound(object):
    DC_WW_RTPC_ext_dc_trajectory_progress = b'RTPC_ext_dc_trajectory_progress'
    DC_WW_STATE_GROUP = b'STATE_deathcam'
    DC_WW_STATE_ON = b'STATE_deathcam_on'
    DC_WW_STATE_OFF = b'STATE_deathcam_off'
    DC_MUTE_GAME_AUDIO = {True: DC_WW_STATE_ON, 
       False: DC_WW_STATE_OFF}
    DC_SIMULATED_SCENE_ENTER = b'dc_simulated_scene_enter'
    DC_SIMULATED_SCENE_EXIT = b'dc_simulated_scene_exit'
    DC_AMBIENT_START = b'dc_amb_start'
    DC_AMBIENT_STOP = b'dc_amb_stop'
    DC_TRAJECTORY_RAY = b'dc_trajectory_ray'
    DC_TRANSITION_START = b'dc_transition_start'
    DC_TRANSITION_END = b'dc_transition_end'
    DC_UI_MARKER = b'dc_ui_marker'
    DC_UI_PAUSE_ENTER = b'dc_ui_pause_enter'
    DC_UI_PAUSE_EXIT = b'dc_ui_pause_exit'
    DC_UI_EXIT = b'dc_ui_exit'
    DC_UI_MARKER_SHOW_ADDITIONAL_INFO = b'dc_ui_marker_add_info'
    DC_UI_MARKER_STATES = {True: [
            KillCamInfoMarkerType.IMPACT, KillCamInfoMarkerType.DISTANCE], 
       False: [
             KillCamInfoMarkerType.GUN, KillCamInfoMarkerType.IMPACT, KillCamInfoMarkerType.DISTANCE]}


class KillCamSoundPlayer(CallbackPauseManager, IViewComponentsCtrlListener):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        CallbackPauseManager.__init__(self)
        self.__transitionDuration = 0.0
        killCamCtrl = self.sessionProvider.shared.killCamCtrl
        if killCamCtrl:
            killCamCtrl.onKillCamModeStateChanged += self.__onKillCamStateChange
            killCamCtrl.onMarkerDisplayChanged += self.__onMarkerDisplayChanged
            killCamCtrl.onKillCamInterrupted += self.__onKillCamInterrupted
            killCamCtrl.onKillCamModeEffectsPlaced += self.__onKillCamModeEffectsPlaced
        return

    @property
    def __isSimplifiedDC(self):
        avatar = BigWorld.player()
        if avatar:
            return avatar.isSimpleDeathCam()
        return False

    def detachedFromCtrl(self, ctrlID):
        super(KillCamSoundPlayer, self).detachedFromCtrl(ctrlID)
        CallbackPauseManager.destroy(self)
        self.__muteGameAudio(False)
        killCamCtrl = self.sessionProvider.shared.killCamCtrl
        if killCamCtrl:
            killCamCtrl.onKillCamModeStateChanged -= self.__onKillCamStateChange
            killCamCtrl.onMarkerDisplayChanged -= self.__onMarkerDisplayChanged
            killCamCtrl.onKillCamInterrupted -= self.__onKillCamInterrupted
            killCamCtrl.onKillCamModeEffectsPlaced -= self.__onKillCamModeEffectsPlaced
        return

    def __onKillCamInterrupted(self):
        self.__playSoundNotification(_DeathCamSound.DC_UI_EXIT)
        self.clearCallbacks()
        return

    def __muteGameAudio(self, mute):
        WWISE.WW_setState(_DeathCamSound.DC_WW_STATE_GROUP, _DeathCamSound.DC_MUTE_GAME_AUDIO[mute])
        return

    def __playSoundNotification(self, notificationName=None, position=None):
        soundNotifications = avatar_getter.getSoundNotifications()
        if soundNotifications and hasattr(soundNotifications, b'play'):
            soundNotifications.play(notificationName, None, None, position)
        return

    def __onKillCamModeEffectsPlaced(self, isSpotted):
        if isSpotted:
            self.__playSoundNotification(_DeathCamSound.DC_TRAJECTORY_RAY)
        return

    def __trajectoryProgress(self, configMovementDuration):
        durationPercentage = decimal_round(self.__transitionDuration * 100.0 / configMovementDuration, 1)
        WWISE.WW_setRTCPGlobal(_DeathCamSound.DC_WW_RTPC_ext_dc_trajectory_progress, durationPercentage)
        self.__transitionDuration += _TRAJECTORY_PROGRESS_DELAY
        if durationPercentage >= 100.0:
            self.__stopTrajectoryProgress()
            return None
        else:
            return _TRAJECTORY_PROGRESS_DELAY

    def __onCamMovementStart(self, configMovementDuration):
        self.__startTrajectoryProgress(configMovementDuration)
        self.__playSoundNotification(_DeathCamSound.DC_TRANSITION_START)
        return

    def __startTrajectoryProgress(self, configMovementDuration):
        self.__transitionDuration = 0.0
        self.__resetRTPCTrajectoryProgress()
        self.delayCallback(_TRAJECTORY_PROGRESS_DELAY, self.__trajectoryProgress, configMovementDuration)
        return

    def __stopTrajectoryProgress(self):
        if self.hasDelayedCallback(self.__trajectoryProgress):
            self.stopCallback(self.__trajectoryProgress)
        self.__onFollowTrajectoryEnd()
        return

    def __onFollowTrajectoryEnd(self):
        self.__playSoundNotification(_DeathCamSound.DC_TRANSITION_END)
        return

    def __playBlackFadeIn(self, leaveKillCam):
        if leaveKillCam:
            self.clearCallbacks()
            self.__playSoundNotification(_DeathCamSound.DC_AMBIENT_STOP)
            self.__playSoundNotification(_DeathCamSound.DC_SIMULATED_SCENE_EXIT)
        else:
            self.__muteGameAudio(True)
        return

    def __resetRTPCTrajectoryProgress(self):
        WWISE.WW_setRTCPGlobal(_DeathCamSound.DC_WW_RTPC_ext_dc_trajectory_progress, 0.0)
        return

    def __playBlackFadeOut(self, leaveKillCam):
        if leaveKillCam:
            self.__muteGameAudio(False)
        else:
            self.__playSoundNotification(_DeathCamSound.DC_SIMULATED_SCENE_ENTER)
            self.__playSoundNotification(_DeathCamSound.DC_AMBIENT_START)
        return

    def __onMarkerDisplayChanged(self, markerState, ctx):
        if markerState == KillCamInfoMarkerType.DISTANCE:
            markerData = ctx[b'markerData']
            if markerData.isAttackerSpotted:
                cameraDuration = ctx[b'configMovementDuration']
                self.__onCamMovementStart(cameraDuration)
        if markerState in _DeathCamSound.DC_UI_MARKER_STATES[self.__isSimplifiedDC]:
            self.__playSoundNotification(_DeathCamSound.DC_UI_MARKER)
        return

    def __onKillCamStateChange(self, killCamState, _):
        if killCamState is DeathCamEvent.State.PAUSE:
            self.pauseCallbacks()
            self.__playSoundNotification(_DeathCamSound.DC_UI_PAUSE_ENTER)
            if not self.__isSimplifiedDC:
                self.__playSoundNotification(_DeathCamSound.DC_UI_MARKER_SHOW_ADDITIONAL_INFO)
        elif killCamState is DeathCamEvent.State.RESUME:
            self.resumeCallbacks()
            self.__playSoundNotification(_DeathCamSound.DC_UI_PAUSE_EXIT)
        elif killCamState is DeathCamEvent.State.PREPARING:
            self.__playBlackFadeIn(leaveKillCam=False)
        elif killCamState is DeathCamEvent.State.STARTING:
            self.__playBlackFadeOut(leaveKillCam=False)
        elif killCamState is DeathCamEvent.State.ENDING:
            self.__playBlackFadeIn(leaveKillCam=True)
        elif killCamState is DeathCamEvent.State.FINISHED:
            self.__playBlackFadeOut(leaveKillCam=True)
        return
