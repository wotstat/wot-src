import typing, enum
MINIMUM_PLAYER_LOADING_PROGRESS_BAR_MAX_VALUE = 800
DEFAULT_LOGIN_STATUS_MIN_SHOW_TIME_SEC = 1
LOADING_VIEW_FADE_OUT_DURATION = 0.2
DEFAULT_SLIDE_DURATION = 15
DEFAULT_SLIDE_TRANSITION_DURATION = 0.4
DEFAULT_LOGIN_NEXT_SLIDE_DURATION = 8

@enum.unique
class GameLoadingStates(str, enum.Enum):
    LOADING_LOGOS = b'loading.logos'
    CLIENT_LOADING = b'client.loading'
    CLIENT_LOADING_SLIDE = b'client.loading.slide'
    CLIENT_LOADING_PROGRESS = b'client.loading.progress'
    CLIENT_LOADING_STATUS = b'client.loading.status'
    LOGIN_SCREEN = b'login.screen'
    PLAYER_LOADING = b'player.loading'
    PLAYER_LOADING_SLIDE = b'player.loading.slide'
    PLAYER_LOADING_PROGRESS = b'player.loading.progress'
    PLAYER_LOADING_STATUS = b'player.loading.status'
    IDL = b'idl'


@enum.unique
class GameLoadingStatesEvents(str, enum.Enum):
    LOGOS_SHOWN = b'logos.shown'
    CLIENT_LOADING = b'client.loading'
    LOGIN_SCREEN = b'login.screen'
    PLAYER_LOADING = b'player.loading'
    IDL = b'idl'


@enum.unique
class ContentState(enum.IntEnum):
    INVISIBLE = 0
    VISIBLE = 1

    @classmethod
    def values(cls):
        return [obj.value for obj in cls.__members__.values()]
