from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.wrappers.user_list_model import UserListModel
from portal.gui.impl.gen.view_models.views.battle.portal_widget_camp import PortalWidgetCamp

class WidgetState(Enum):
    PREBATTLE = b'preBattle'
    DEFAULT = b'default'
    SUPERBOSSFIGHT = b'superBossFight'
    AFTERBATTLE = b'afterBattle'


class PortalHudWidgetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(PortalHudWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def camps(self):
        return self._getViewModel(0)

    @staticmethod
    def getCampsType():
        return PortalWidgetCamp

    def getCampsCount(self):
        return self._getNumber(1)

    def setCampsCount(self, value):
        self._setNumber(1, value)
        return

    def getCapturedCamps(self):
        return self._getNumber(2)

    def setCapturedCamps(self, value):
        self._setNumber(2, value)
        return

    def getCanBeCapturedCamps(self):
        return self._getNumber(3)

    def setCanBeCapturedCamps(self, value):
        self._setNumber(3, value)
        return

    def getState(self):
        return WidgetState(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)
        return

    def getBossMaxHealth(self):
        return self._getNumber(5)

    def setBossMaxHealth(self, value):
        self._setNumber(5, value)
        return

    def getBossCurrentHealth(self):
        return self._getNumber(6)

    def setBossCurrentHealth(self, value):
        self._setNumber(6, value)
        return

    def getBossLastDamage(self):
        return self._getNumber(7)

    def setBossLastDamage(self, value):
        self._setNumber(7, value)
        return

    def getSuperBossMaxHealth(self):
        return self._getNumber(8)

    def setSuperBossMaxHealth(self, value):
        self._setNumber(8, value)
        return

    def getSuperBossCurrentHealth(self):
        return self._getNumber(9)

    def setSuperBossCurrentHealth(self, value):
        self._setNumber(9, value)
        return

    def getSuperBossLastDamage(self):
        return self._getNumber(10)

    def setSuperBossLastDamage(self, value):
        self._setNumber(10, value)
        return

    def getVehicleName(self):
        return self._getString(11)

    def setVehicleName(self, value):
        self._setString(11, value)
        return

    def getVehicleClassTag(self):
        return self._getString(12)

    def setVehicleClassTag(self, value):
        self._setString(12, value)
        return

    def _initialize(self):
        super(PortalHudWidgetViewModel, self)._initialize()
        self._addViewModelProperty(b'camps', UserListModel())
        self._addNumberProperty(b'campsCount', 0)
        self._addNumberProperty(b'capturedCamps', 0)
        self._addNumberProperty(b'canBeCapturedCamps', 0)
        self._addStringProperty(b'state')
        self._addNumberProperty(b'bossMaxHealth', 0)
        self._addNumberProperty(b'bossCurrentHealth', 0)
        self._addNumberProperty(b'bossLastDamage', 0)
        self._addNumberProperty(b'superBossMaxHealth', 0)
        self._addNumberProperty(b'superBossCurrentHealth', 0)
        self._addNumberProperty(b'superBossLastDamage', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleClassTag', b'')
        return
