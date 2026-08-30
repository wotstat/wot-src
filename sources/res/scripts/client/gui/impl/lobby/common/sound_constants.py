from sound_gui_manager import CommonSoundSpaceSettings
from gui.sounds.filters import States, StatesGroup
FIELD_POST_SOUND_SETTINGS = CommonSoundSpaceSettings(name=b'field_post', entranceStates={b'STATE_hangar_place': b'STATE_hangar_place_garage', 
   (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_ON)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
SUBVIEW_SOUND_SPACE = CommonSoundSpaceSettings(name=b'sub_view', entranceStates={b'STATE_hangar_place': b'STATE_hangar_place_garage', 
   (StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_ON)}, exitStates={}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
BROWSER_VIEW_SOUND_SPACES = {(FIELD_POST_SOUND_SETTINGS.name): FIELD_POST_SOUND_SETTINGS, 
   (SUBVIEW_SOUND_SPACE.name): SUBVIEW_SOUND_SPACE}
HANGAR_FILTERED_SOUND_SPACE = CommonSoundSpaceSettings(name=b'filterHangar', entranceStates={(StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_ON)}, exitStates={(StatesGroup.HANGAR_FILTERED): (States.HANGAR_FILTERED_OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
