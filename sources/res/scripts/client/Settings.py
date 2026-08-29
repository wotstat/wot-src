import BigWorld
g_instance = None
KEY_CONTROL_MODE = b'controlMode'
KEY_LOGIN_INFO = b'loginInfo'
KEY_SCREEN_SIZE = b'screenSize'
KEY_VIDEO_MODE = b'videoMode'
KEY_LOBBY_TOOLTIP_DELAY = b'lobbyTooltipDelay'
KEY_SOUND_PREFERENCES = b'soundPrefs'
KEY_REPLAY_PREFERENCES = b'replayPrefs'
APPLICATION_CLOSE_DELAY = b'closeApplicationDelay'
KEY_MESSENGER_PREFERENCES = b'messengerPrefs'
KEY_ACCOUNT_SETTINGS = b'accounts'
KEY_COMMAND_MAPPING = b'commandMapping'
KEY_SHOW_STARTUP_MOVIE = b'showStartupMovie'
KEY_VOIP_DEVICE = b'captureDevice'
KEY_ENABLE_EDGE_DETECT_AA = b'enableEdgeDetectAA'
KEY_WINDOWS_STORED_DATA = b'windowsStoredData'
KEY_FOV = b'fov'
KEY_GUI_NOTIFY_INFO = b'guiNotifyInfo'
KEY_DYNAMIC_FOV = b'dynamicFov'
KEY_DYNAMIC_FOV_ENABLED = b'dynamicFovEnabled'
IGB_HARDWARE_ACCELERATION_ENABLED = b'igbHardwareAccelerationEnabled'
INTRO_VIDEO_VERSION = b'introVideoVersion'
VIDEO_BUFFERING_TIME = b'videoBufferingTime'
KEY_BOOTCAMP_PREFERENCES = b'bootcampPrefs'
POPUPS_WINDOWS_DISABLED = b'popupsWindowsDisabled'
KEY_MAPS_TRAINING_PREFERENCES = b'mapsTraining'

class Settings(object):

    def __init__(self, scriptConfig, engineConfig, userPrefs):
        self.scriptConfig = scriptConfig
        self.engineConfig = engineConfig
        self.userPrefs = userPrefs
        return

    def save(self):
        BigWorld.savePreferences()
        return
