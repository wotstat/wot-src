from enum import Enum
import SoundGroups
from shared_utils import CONST_CONTAINER
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews
from sound_gui_manager import CommonSoundSpaceSettings

class MetaViewSounds(Enum):
    ENTER_EVENT = b'comp_7_progression_enter'
    EXIT_EVENT = b'comp_7_progression_exit'
    ENTER_TAB_EVENTS = {(MetaRootViews.YEARLYSTATISTICS): b'comp_7_season_statistics_screen_appear', 
       (MetaRootViews.SHOP): b'comp_7_shop_enter'}
    EXIT_TAB_EVENTS = {(MetaRootViews.SHOP): b'comp_7_progression_enter'}


class FlybySounds(Enum):
    START = b'comp_7_shop_purchase_anim_start'
    STOP = b'comp_7_shop_purchase_anim_stop'


class VehicleVideoSounds(CONST_CONTAINER):
    START = b'comp_7_video_reward_style_start'
    PAUSE = b'comp_7_video_reward_style_pause'
    RESUME = b'comp_7_video_reward_style_resume'
    END = b'comp_7_video_reward_style_stop'


def getComp7MetaSoundSpace():
    return CommonSoundSpaceSettings(name=b'comp7_meta_view', entranceStates={}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=MetaViewSounds.ENTER_EVENT.value, exitEvent=MetaViewSounds.EXIT_EVENT.value)


def playComp7MetaViewTabSound(tabId, prevTabId=None):
    sounds = (MetaViewSounds.EXIT_TAB_EVENTS.value.get(prevTabId), MetaViewSounds.ENTER_TAB_EVENTS.value.get(tabId))
    for soundName in sounds:
        if soundName is not None:
            SoundGroups.g_instance.playSound2D(soundName)

    return


def playSound(eventName):
    SoundGroups.g_instance.playSound2D(eventName)
    return
