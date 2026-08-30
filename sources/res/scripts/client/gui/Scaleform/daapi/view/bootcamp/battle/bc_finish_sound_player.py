import SoundGroups
from PlayerEvents import g_playerEvents
from gui.Scaleform.daapi.view.battle.shared.finish_sound_player import FinishSoundPlayer
from gui.battle_control.view_components import IViewComponentsCtrlListener
_SOUND_EVENT_OVERRIDES = {b'end_battle_last_kill': b'bc_end_battle_last_kill', 
   b'end_battle_capture_base': b'bc_end_battle_capture_base', 
   b'time_over': b'bc_end_battle_time_over'}

class BCFinishSoundPlayer(FinishSoundPlayer, IViewComponentsCtrlListener):

    def __init__(self):
        super(BCFinishSoundPlayer, self).__init__()
        self.__soundID = None
        g_playerEvents.onRoundFinished += self.__onRoundFinished
        return

    def detachedFromCtrl(self, ctrlID):
        g_playerEvents.onRoundFinished -= self.__onRoundFinished
        return

    def _playSound(self, soundID):
        self.__soundID = _SOUND_EVENT_OVERRIDES.get(soundID, soundID)
        return

    def __onRoundFinished(self, winnerTeam, reason, extraData):
        if self.__soundID:
            SoundGroups.g_instance.playSound2D(self.__soundID)
        return
