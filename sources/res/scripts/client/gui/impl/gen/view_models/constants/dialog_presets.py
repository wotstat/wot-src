from frameworks.wulf import ViewModel

class DialogPresets(ViewModel):
    __slots__ = ()
    QUIT_GAME = b'quitGame'
    ERROR = b'error'
    WARNING = b'warning'
    INFO = b'info'
    BLUEPRINTS_CONVERSION = b'blueprintsConversion'
    MAPS_BLACKLIST = b'mapsBlacklist'
    TROPHY_DEVICE_UPGRADE = b'trophyDeviceUpgrade'
    BUY_BATTLE_PASS = b'buyBattlePass'
    CUSTOMIZATION_INSTALL_BOUND = b'customizationInstallBound'
    DEFAULT = b'default'

    def __init__(self, properties=0, commands=0):
        super(DialogPresets, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(DialogPresets, self)._initialize()
        return
