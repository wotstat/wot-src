from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle.death_cam.hud_model import HudModel
from gui.impl.gen.view_models.views.battle.death_cam.marker_model import MarkerModel

class Phase(Enum):
    KILLER = b'killer'
    TRAJECTORY = b'trajectory'
    IMPACT = b'impact'


class CaliberRule(Enum):
    NONE = b'None'
    TWOCALIBER = b'TwoCaliber'
    THREECALIBER = b'ThreeCaliber'


class DeathReason(Enum):
    HP = b''
    IGNITION = b'ignition'
    DETONATION = b'detonation'
    CREW = b'crew'


class ShellType(Enum):
    ARMORPIERCING = b'ARMOR_PIERCING'
    ARMORPIERCINGCR = b'ARMOR_PIERCING_CR'
    ARMORPIERCINGCRPREMIUM = b'ARMOR_PIERCING_CR_PREMIUM'
    ARMORPIERCINGPREMIUM = b'ARMOR_PIERCING_PREMIUM'
    HIGHEXPLOSIVE = b'HIGH_EXPLOSIVE'
    HIGHEXPLOSIVEMODERN = b'HIGH_EXPLOSIVE_MODERN'
    HIGHEXPLOSIVEMODERNPREMIUM = b'HIGH_EXPLOSIVE_MODERN_PREMIUM'
    HIGHEXPLOSIVEPREMIUM = b'HIGH_EXPLOSIVE_PREMIUM'
    HIGHEXPLOSIVESPG = b'HIGH_EXPLOSIVE_SPG'
    HIGHEXPLOSIVESPGSTUN = b'HIGH_EXPLOSIVE_SPG_STUN'
    HOLLOWCHARGE = b'HOLLOW_CHARGE'
    HOLLOWCHARGEPREMIUM = b'HOLLOW_CHARGE_PREMIUM'


class ImpactMode(Enum):
    PENETRATION = b'penetration'
    NONPENETRATIONDAMAGE = b'nonPenetrationDamage'
    LEGACYHE = b'legacyHE'
    MODERNHE = b'modernHE'


class DeathCamHudViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=34, commands=0):
        super(DeathCamHudViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def marker(self):
        return self._getViewModel(0)

    @staticmethod
    def getMarkerType():
        return MarkerModel

    @property
    def hud(self):
        return self._getViewModel(1)

    @staticmethod
    def getHudType():
        return HudModel

    def getImpactMode(self):
        return ImpactMode(self._getString(2))

    def setImpactMode(self, value):
        self._setString(2, value.value)
        return

    def getPhase(self):
        return Phase(self._getString(3))

    def setPhase(self, value):
        self._setString(3, value.value)
        return

    def getIsAdvanced(self):
        return self._getBool(4)

    def setIsAdvanced(self, value):
        self._setBool(4, value)
        return

    def getIsKillerUnspotted(self):
        return self._getBool(5)

    def setIsKillerUnspotted(self, value):
        self._setBool(5, value)
        return

    def getIsMarkerVisible(self):
        return self._getBool(6)

    def setIsMarkerVisible(self, value):
        self._setBool(6, value)
        return

    def getPhaseDuration(self):
        return self._getNumber(7)

    def setPhaseDuration(self, value):
        self._setNumber(7, value)
        return

    def getPhaseTimePassed(self):
        return self._getNumber(8)

    def setPhaseTimePassed(self, value):
        self._setNumber(8, value)
        return

    def getIsSimplified(self):
        return self._getBool(9)

    def setIsSimplified(self, value):
        self._setBool(9, value)
        return

    def getShellType(self):
        return ShellType(self._getString(10))

    def setShellType(self, value):
        self._setString(10, value.value)
        return

    def getShellIcon(self):
        return self._getString(11)

    def setShellIcon(self, value):
        self._setString(11, value)
        return

    def getShellCaliber(self):
        return self._getNumber(12)

    def setShellCaliber(self, value):
        self._setNumber(12, value)
        return

    def getCaliberRule(self):
        return CaliberRule(self._getString(13))

    def setCaliberRule(self, value):
        self._setString(13, value.value)
        return

    def getShellDamageBasic(self):
        return self._getReal(14)

    def setShellDamageBasic(self, value):
        self._setReal(14, value)
        return

    def getShellVelocityBasic(self):
        return self._getNumber(15)

    def setShellVelocityBasic(self, value):
        self._setNumber(15, value)
        return

    def getShootDistance(self):
        return self._getNumber(16)

    def setShootDistance(self, value):
        self._setNumber(16, value)
        return

    def getShellPenetrationEffective(self):
        return self._getNumber(17)

    def setShellPenetrationEffective(self, value):
        self._setNumber(17, value)
        return

    def getShellPenetrationBasic(self):
        return self._getNumber(18)

    def setShellPenetrationBasic(self, value):
        self._setNumber(18, value)
        return

    def getArmorRelative(self):
        return self._getNumber(19)

    def setArmorRelative(self, value):
        self._setNumber(19, value)
        return

    def getArmorNominal(self):
        return self._getNumber(20)

    def setArmorNominal(self, value):
        self._setNumber(20, value)
        return

    def getShellArmorAngleGain(self):
        return self._getNumber(21)

    def setShellArmorAngleGain(self, value):
        self._setNumber(21, value)
        return

    def getAngleRicochet(self):
        return self._getNumber(22)

    def setAngleRicochet(self, value):
        self._setNumber(22, value)
        return

    def getAngleFailure(self):
        return self._getNumber(23)

    def setAngleFailure(self, value):
        self._setNumber(23, value)
        return

    def getAngleImpact(self):
        return self._getNumber(24)

    def setAngleImpact(self, value):
        self._setNumber(24, value)
        return

    def getShellDamageEffective(self):
        return self._getReal(25)

    def setShellDamageEffective(self, value):
        self._setReal(25, value)
        return

    def getShellDamageRandomizationFactor(self):
        return self._getReal(26)

    def setShellDamageRandomizationFactor(self, value):
        self._setReal(26, value)
        return

    def getDamageDistanceModifier(self):
        return self._getReal(27)

    def setDamageDistanceModifier(self, value):
        self._setReal(27, value)
        return

    def getHasDistanceFalloff(self):
        return self._getBool(28)

    def setHasDistanceFalloff(self, value):
        self._setBool(28, value)
        return

    def getShellDamageBurst(self):
        return self._getNumber(29)

    def setShellDamageBurst(self, value):
        self._setNumber(29, value)
        return

    def getShellDamageLossDistance(self):
        return self._getNumber(30)

    def setShellDamageLossDistance(self, value):
        self._setNumber(30, value)
        return

    def getShellDamageLossProtectionHe(self):
        return self._getNumber(31)

    def setShellDamageLossProtectionHe(self, value):
        self._setNumber(31, value)
        return

    def getShellDamageLossProtectionSpallLiner(self):
        return self._getNumber(32)

    def setShellDamageLossProtectionSpallLiner(self, value):
        self._setNumber(32, value)
        return

    def getDeathReason(self):
        return DeathReason(self._getString(33))

    def setDeathReason(self, value):
        self._setString(33, value.value)
        return

    def _initialize(self):
        super(DeathCamHudViewModel, self)._initialize()
        self._addViewModelProperty(b'marker', MarkerModel())
        self._addViewModelProperty(b'hud', HudModel())
        self._addStringProperty(b'impactMode')
        self._addStringProperty(b'phase')
        self._addBoolProperty(b'isAdvanced', False)
        self._addBoolProperty(b'isKillerUnspotted', False)
        self._addBoolProperty(b'isMarkerVisible', False)
        self._addNumberProperty(b'phaseDuration', 0)
        self._addNumberProperty(b'phaseTimePassed', 0)
        self._addBoolProperty(b'isSimplified', False)
        self._addStringProperty(b'shellType')
        self._addStringProperty(b'shellIcon', b'')
        self._addNumberProperty(b'shellCaliber', 0)
        self._addStringProperty(b'caliberRule')
        self._addRealProperty(b'shellDamageBasic', 0.0)
        self._addNumberProperty(b'shellVelocityBasic', 0)
        self._addNumberProperty(b'shootDistance', 0)
        self._addNumberProperty(b'shellPenetrationEffective', 0)
        self._addNumberProperty(b'shellPenetrationBasic', 0)
        self._addNumberProperty(b'armorRelative', 0)
        self._addNumberProperty(b'armorNominal', 0)
        self._addNumberProperty(b'shellArmorAngleGain', 0)
        self._addNumberProperty(b'angleRicochet', 0)
        self._addNumberProperty(b'angleFailure', 0)
        self._addNumberProperty(b'angleImpact', 0)
        self._addRealProperty(b'shellDamageEffective', 0.0)
        self._addRealProperty(b'shellDamageRandomizationFactor', 0.0)
        self._addRealProperty(b'damageDistanceModifier', 0.0)
        self._addBoolProperty(b'hasDistanceFalloff', False)
        self._addNumberProperty(b'shellDamageBurst', 0)
        self._addNumberProperty(b'shellDamageLossDistance', 0)
        self._addNumberProperty(b'shellDamageLossProtectionHe', 0)
        self._addNumberProperty(b'shellDamageLossProtectionSpallLiner', 0)
        self._addStringProperty(b'deathReason')
        return
