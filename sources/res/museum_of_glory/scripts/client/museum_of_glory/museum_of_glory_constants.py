MUSEUM_OF_GLORY_CONFIG = b'museum_of_glory_config'
MUSEUM_OF_GLORY = b'MuseumOfGlorySettings'
AUDIO_GUIDE_ENABLED = b'AudioGuideEnabled'
IS_INTRO_SEEN = b'IsIntroSeen'
LAST_SEEN_INDEX = b'lastSeenIndex'
ALL_VEHS_INT_CD = b'allVehsIntCD'
NEW_CONTENT = b'newContent'
VEHS_COUNT = b'vehsCount'
ACCOUNT_DEFAULT_SETTINGS = {MUSEUM_OF_GLORY: {AUDIO_GUIDE_ENABLED: True, 
                     IS_INTRO_SEEN: False, 
                     LAST_SEEN_INDEX: 0, 
                     ALL_VEHS_INT_CD: (set()), 
                     VEHS_COUNT: 0, 
                     NEW_CONTENT: False}}
CHARACTERISTIC_FIELDS = [
 9, 10, 11, 12, 13, 14, 15, 16]

class MuseumOfGlorySoundEvents(object):
    SOUND_EVENT_PREFIX = b'h16_mt_museum_vo_guide_'
    WELCOME_SOUND_EVENT = b'h16_mt_museum_vo_guide_welcome'
    STOP_SOUND_EVENT = b'h16_mt_museum_vo_guide_stop'
    PAUSE_SOUND_EVENT = b'h16_mt_museum_vo_guide_pause'
    RESUME_SOUND_EVENT = b'h16_mt_museum_vo_guide_resume'
    EXCURSION_MUTE = b'h16_mt_museum_vo_guide_mute'
    EXCURSION_UNMUTE = b'h16_mt_museum_vo_guide_unmute'
    STATE_PLACE = b'STATE_hangar_place'
    STATE_PLACE_GARAGE = b'STATE_hangar_place_garage'
    EXCURSION_STATE = b'STATE_ext_mt_museum_excursion'
    DATES_STATE = b'STATE_ext_mt_museum_dates'
    STATES = {EXCURSION_STATE: [
                       b'STATE_ext_mt_museum_excursion_off', b'STATE_ext_mt_museum_excursion_on']}
