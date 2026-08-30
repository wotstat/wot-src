import SoundGroups, WWISE
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from web.web_client_api import w2c, w2capi, W2CSchema, Field

class _SoundSchema(W2CSchema):
    sound_id = Field(required=True, type=basestring)


class _SoundStateSchema(W2CSchema):
    state_name = Field(required=True, type=basestring)
    state_value = Field(required=True, type=basestring)


class _HangarSoundSchema(W2CSchema):
    mute = Field(required=True, type=bool)


@w2capi()
class SoundWebApi(object):
    _ENTER_EXIT_SOUND_MAPPING = {b'eb_ambient_progress_page_enter': b'eb_ambient_progress_page_exit', 
       b'main_unit_enter': b'main_unit_exit', 
       b'clans_quests_enter': b'clans_quests_exit', 
       b'fa_enter': b'fa_exit', 
       b'ads_enter': b'ads_exit', 
       b'global_map_enter': b'global_map_exit', 
       b'craft_machine_enter': b'craft_machine_exit', 
       b'clans_battles_global_map_enter': b'clans_battles_global_map_exit', 
       b'clans_winner_reward_enter': b'clans_winner_reward_exit', 
       b'gui_cq_progress_bar_start': b'gui_cq_progress_bar_stop', 
       b'gui_cq_progression_start': b'gui_cq_progression_stop'}

    def __init__(self):
        super(SoundWebApi, self).__init__()
        self.__exitSounds = set()
        return

    @w2c(_SoundSchema, b'sound', finiHandlerName=b'_soundFini')
    def sound(self, cmd):
        appLoader = dependency.instance(IAppLoader)
        app = appLoader.getApp()
        if app and app.soundManager:
            app.soundManager.playEffectSound(cmd.sound_id)
            self.__exitSounds.discard(cmd.sound_id)
            exitSound = self._ENTER_EXIT_SOUND_MAPPING.get(cmd.sound_id)
            if exitSound:
                self.__exitSounds.add(exitSound)
        return

    def _soundFini(self):
        for exitSound in self.__exitSounds:
            WWISE.WW_eventGlobal(exitSound)

        self.__exitSounds.clear()
        return


@w2capi()
class SoundStateWebApi(object):
    _ON_EXIT_STATES = {b'STATE_overlay_hangar_general': b'STATE_overlay_hangar_general_off', 
       b'STATE_video_overlay': b'STATE_video_overlay_off', 
       b'STATE_clans_craft': b'STATE_clans_craft_progress_off', 
       b'STATE_gamemode_progress_page': b'STATE_gamemode_progress_page_off'}

    def __init__(self):
        super(SoundStateWebApi, self).__init__()
        self.__setStates = set()
        return

    @w2c(_SoundStateSchema, b'sound_state', finiHandlerName=b'_soundStateFini')
    def setSoundState(self, cmd):
        WWISE.WW_setState(str(cmd.state_name), str(cmd.state_value))
        self.__setStates.add(str(cmd.state_name))
        return

    def _soundStateFini(self):
        for stateName, stateValue in self._ON_EXIT_STATES.iteritems():
            if stateName in self.__setStates:
                WWISE.WW_setState(stateName, stateValue)

        self.__setStates.clear()
        return


@w2capi()
class HangarSoundWebApi(object):

    @w2c(_HangarSoundSchema, b'hangar_sound', finiHandlerName=b'_hangarSoundFini')
    def hangarSound(self, cmd):
        if cmd.mute:
            SoundGroups.g_instance.playSound2D(b'ue_master_mute')
        else:
            SoundGroups.g_instance.playSound2D(b'ue_master_unmute')
        return

    def _hangarSoundFini(self):
        SoundGroups.g_instance.playSound2D(b'ue_master_unmute')
        return
