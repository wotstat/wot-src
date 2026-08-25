from shared_utils import CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = b'personalReserves'
    STATE_PLACE = b'STATE_personal_reserves'
    STATE_PERSONAL_RESERVES_ON = b'STATE_personal_reserves_on'
    STATE_PERSONAL_RESERVES_OFF = b'STATE_personal_reserves_off'
    ENTER_EVENT = b'personal_reserves'


PERSONAL_RESERVES_SOUND_SPACE = CommonSoundSpaceSettings(name=SOUNDS.COMMON_SOUND_SPACE, entranceStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PERSONAL_RESERVES_ON)}, exitStates={(SOUNDS.STATE_PLACE): (SOUNDS.STATE_PERSONAL_RESERVES_OFF)}, persistentSounds=(
 SOUNDS.ENTER_EVENT,), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
