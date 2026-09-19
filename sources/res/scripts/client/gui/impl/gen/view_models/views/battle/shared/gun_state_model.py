from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle.shared.timer_model import TimerModel

class GunType(Enum):
    SIMPLE = b'simple'
    AUTORELOAD = b'autoReload'
    DUALGUN = b'dualGun'
    CONTROLLABLE = b'controllable'


class ReloadStatus(Enum):
    READY = b'ready'
    RELOADING = b'reloading'
    EMPTY = b'empty'


class ReloadType(Enum):
    STANDARD = b'standard'
    CASSETTECLIP = b'cassetteClip'
    AUTOLOADERCLIP = b'autoLoaderClip'
    EXTRASHOTCLIP = b'extraShotClip'
    CONTROLLABLERELOAD = b'controllableReload'
    UNLIMITEDCLIP = b'unlimitedClip'
    SHELLCALIBRATIONCLIP = b'shellCalibrationClip'


class GunStateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(GunStateModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def reloadTimer(self):
        return self._getViewModel(0)

    @staticmethod
    def getReloadTimerType():
        return TimerModel

    def getGunType(self):
        return GunType(self._getString(1))

    def setGunType(self, value):
        self._setString(1, value.value)
        return

    def getReloadStatus(self):
        return ReloadStatus(self._getString(2))

    def setReloadStatus(self, value):
        self._setString(2, value.value)
        return

    def getReloadMechanicType(self):
        return ReloadType(self._getString(3))

    def setReloadMechanicType(self, value):
        self._setString(3, value.value)
        return

    def getCurrentShellQuantity(self):
        return self._getNumber(4)

    def setCurrentShellQuantity(self, value):
        self._setNumber(4, value)
        return

    def getIsShotAvailable(self):
        return self._getBool(5)

    def setIsShotAvailable(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(GunStateModel, self)._initialize()
        self._addViewModelProperty(b'reloadTimer', TimerModel())
        self._addStringProperty(b'gunType', GunType.SIMPLE.value)
        self._addStringProperty(b'reloadStatus', ReloadStatus.READY.value)
        self._addStringProperty(b'reloadMechanicType', ReloadType.STANDARD.value)
        self._addNumberProperty(b'currentShellQuantity', -1)
        self._addBoolProperty(b'isShotAvailable', False)
        return
