import enum, typing
MINIMUM_PLAYER_LOADING_PROGRESS_BAR_MAX_VALUE = 800
DEFAULT_LOGIN_STATUS_MIN_SHOW_TIME_SEC = 1
LOADING_VIEW_FADE_OUT_DURATION = 0.2
DEFAULT_SLIDE_DURATION = 15
DEFAULT_SLIDE_TRANSITION_DURATION = 0.4
DEFAULT_LOGIN_NEXT_SLIDE_DURATION = 8
DEFAULT_WAITING_TIMEOUT = 10.0

@enum.unique
class GameLoadingStates(str, enum.Enum):
    CLIENT_INIT = b'client.init'
    CLIENT_INIT_LOGOS = b'client.init.logos'
    CLIENT_INIT_LOADING = b'client.init.loading'
    CLIENT_INIT_LOADING_SLIDE = b'client.loading.slide'
    CLIENT_INIT_LOADING_PROGRESS = b'client.loading.progress'
    CLIENT_INIT_LOADING_STATUS = b'client.loading.status'
    CLIENT_INIT_LOADING_STUB = b'client.loading.stub'
    LOGIN_SCREEN = b'login.screen'
    PLAYER_LOADING = b'player.loading'
    PLAYER_LOADING_SLIDE = b'player.loading.slide'
    PLAYER_LOADING_PROGRESS = b'player.loading.progress'
    PLAYER_LOADING_STATUS = b'player.loading.status'
    IDLE = b'idle'


@enum.unique
class GameLoadingStatesEvents(str, enum.Enum):
    LOGOS_SHOWN = b'logos.shown'
    CLIENT_LOADING = b'client.loading'
    LOGIN_SCREEN = b'login.screen'
    PLAYER_LOADING = b'player.loading'
    IDLE = b'idle'


@enum.unique
class ContentState(enum.IntEnum):
    INVISIBLE = 0
    VISIBLE = 1

    @classmethod
    def values(cls):
        return [obj.value for obj in cls.__members__.values()]


@enum.unique
class TickingMode(enum.IntEnum):
    MANUAL = 0
    SELF_TICKING = 1
    BOTH = 2
