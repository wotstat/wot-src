from helpers.thermal_vision.sound_event import SoundEvent
from helpers.thermal_vision.sound_states_switcher import SoundStatesSwitcher
from helpers.thermal_vision.rtpc_sound_event import RTPCSoundEvent
RTPC_EVENT_WARNING = RTPCSoundEvent(b'RTPC_ext_un_pyrometer_detecting', b'un_pyrometer_detecting_start_PC', b'un_pyrometer_detecting_stop_PC')
SOUND_SWITCH_ACTIVATION = SoundStatesSwitcher(b'STATE_un_pyrometer', b'STATE_un_pyrometer_on', b'STATE_un_pyrometer_off')
SOUND_EVENT_ACTIVATION = SoundEvent(b'un_pyrometer_start', b'un_pyrometer_stop')
SOUND_EVENT_ENEMY_IN_SECTOR = SoundEvent(b'un_pyrometer_NPC_in', b'un_pyrometer_NPC_out')
SOUND_EVENT_RELOADING = SoundEvent(b'ability_recharging')
RELOADING_DURATION = 3.0
SOUND_EVENT_NPC_DETECTED = SoundEvent(b'un_pyrometer_NPC_detected')
DISABLED_ERROR_MSG_KEY = b'thermalVisionOverturned'
