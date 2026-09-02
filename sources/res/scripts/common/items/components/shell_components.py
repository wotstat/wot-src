import typing
from constants import SHELL_TYPES, DamageAbsorptionTypeToLabel, SHELL_MECHANICS_TYPE, StunTypes, HAS_EXPLOSION_EFFECT
from items.components import component_constants
from typing import Set, Tuple, Union

class ShellType(object):
    __slots__ = (b'name',)

    def __init__(self, name):
        super(ShellType, self).__init__()
        self.name = name
        return

    def __repr__(self):
        return (b'{}()').format(self.__class__.__name__)


class ArmorPiercingType(ShellType):
    __slots__ = (b'normalizationAngle', b'ricochetAngleCos', b'protectFromDirectHits', b'mechanics', b'guaranteedDamages', b'protectFromDestroy')

    def __init__(self, name):
        super(ArmorPiercingType, self).__init__(name)
        self.normalizationAngle = component_constants.ZERO_FLOAT
        self.ricochetAngleCos = component_constants.ZERO_FLOAT
        self.protectFromDirectHits = set()
        self.protectFromDestroy = set()
        self.mechanics = SHELL_MECHANICS_TYPE.LEGACY
        self.guaranteedDamages = component_constants.EMPTY_TUPLE
        return

    def __repr__(self):
        return (b'ArmorPiercingType(normalizationAngle={}, ricochetAngleCos={}, protectFromDirectHits = {}, protectFromDestroy = {})').format(self.normalizationAngle, self.ricochetAngleCos, self.protectFromDirectHits, self.protectFromDestroy)


class HollowChargeType(ShellType):
    __slots__ = (b'piercingPowerLossFactorByDistance', b'ricochetAngleCos', b'protectFromDirectHits', b'mechanics', b'guaranteedDamages', b'protectFromDestroy')

    def __init__(self, name):
        super(HollowChargeType, self).__init__(name)
        self.piercingPowerLossFactorByDistance = component_constants.ZERO_FLOAT
        self.ricochetAngleCos = component_constants.ZERO_FLOAT
        self.protectFromDirectHits = set()
        self.protectFromDestroy = set()
        self.mechanics = SHELL_MECHANICS_TYPE.LEGACY
        self.guaranteedDamages = component_constants.EMPTY_TUPLE
        return

    def __repr__(self):
        return (b'HollowChargeType(piercingPowerLossFactorByDistance={}, ricochetAngleCos={}, protectFromDirectHits={}, protectFromDestroy={})').format(self.piercingPowerLossFactorByDistance, self.ricochetAngleCos, self.protectFromDirectHits, self.protectFromDestroy)


class DistanceDamageFactor(object):
    __slots__ = (b'armorFactor', b'damageFactor', b'pierceFactor', b'deviceFactor', b'spallsDamageFactor', b'spallsDeviceFactor')

    def __init__(self):
        self.armorFactor = component_constants.EMPTY_TUPLE
        self.damageFactor = component_constants.EMPTY_TUPLE
        self.pierceFactor = component_constants.EMPTY_TUPLE
        self.deviceFactor = component_constants.EMPTY_TUPLE
        self.spallsDamageFactor = component_constants.EMPTY_TUPLE
        self.spallsDeviceFactor = component_constants.EMPTY_TUPLE
        return

    def __repr__(self):
        res = b'{}(' + (b', ').join(aName + b'=' + str(getattr(self, aName)) for aName in self.__slots__) + b')'
        return res.format(self.__class__.__name__)


class HighExplosiveImpactParams(object):
    __slots__ = (b'radius', b'damages', b'coneAngleCos', b'piercingSpalls', b'damageAbsorptionType', b'isActive', b'useEffectiveArmor')

    def __init__(self):
        self.radius = component_constants.ZERO_FLOAT
        self.damages = component_constants.EMPTY_TUPLE
        self.coneAngleCos = None
        self.piercingSpalls = None
        self.damageAbsorptionType = None
        self.useEffectiveArmor = False
        self.isActive = True
        return

    def __repr__(self):
        return (b'HighExplosiveImpactParams(radius={}, damages={}, coneAngleCos={}, piersingSpalls={}, damageAbsorption={}, useEffectiveArmor={})').format(self.radius, self.damages, self.coneAngleCos, self.piercingSpalls, DamageAbsorptionTypeToLabel[self.damageAbsorptionType] if self.damageAbsorptionType else None, self.useEffectiveArmor)


class HighExplosiveType(ShellType):
    __slots__ = (b'explosionRadius', b'explosionDamageFactor', b'explosionDamageAbsorptionFactor', b'explosionEdgeDamageFactor', b'mechanics', b'blastWave', b'shellFragments', b'armorSpalls', b'shellFragmentsDamageAbsorptionFactor', b'obstaclePenetration', b'shieldPenetration', b'maxDamage', b'protectFromDirectHits', b'protectFromIndirectHits', b'protectFromDestroy', b'explosionDisableDamageFalloff')

    def __init__(self, name):
        super(HighExplosiveType, self).__init__(name)
        self.explosionRadius = component_constants.ZERO_FLOAT
        self.explosionDamageFactor = component_constants.ZERO_FLOAT
        self.explosionDamageAbsorptionFactor = component_constants.ZERO_FLOAT
        self.explosionEdgeDamageFactor = component_constants.ZERO_FLOAT
        self.shellFragmentsDamageAbsorptionFactor = component_constants.ZERO_FLOAT
        self.explosionDisableDamageFalloff = component_constants.ZERO_FLOAT
        self.mechanics = SHELL_MECHANICS_TYPE.LEGACY
        self.obstaclePenetration = None
        self.shieldPenetration = None
        self.blastWave = None
        self.shellFragments = None
        self.armorSpalls = None
        self.protectFromDirectHits = set()
        self.protectFromIndirectHits = set()
        self.protectFromDestroy = set()
        self.maxDamage = None
        return

    def __repr__(self):
        return (b'HighExplosiveType(explosionRadius={}, explosionDamageFactor={}, explosionDamageAbsorptionFactor={}, explosionEdgeDamageFactor={}, mechanics={}, obstaclePenetration={}, shieldPenetration={}, blastWave={}, shellFragments={}, armorSpalls={}, shellFragmentsDamageAbsorptionFactor={}, protectFromDirectHits = {}, protectFromIndirectHits = {}, protectFromDestroy = {}, explosionDisableDamageFalloff = {}, ').format(self.explosionRadius, self.explosionDamageFactor, self.explosionDamageAbsorptionFactor, self.explosionEdgeDamageFactor, self.mechanics, self.obstaclePenetration, self.shieldPenetration, self.blastWave, self.shellFragments, self.armorSpalls, self.shellFragmentsDamageAbsorptionFactor, self.protectFromDirectHits, self.protectFromIndirectHits, self.protectFromDestroy, self.explosionDisableDamageFalloff)


class SmokeType(ShellType):
    __slots__ = ()

    def __init__(self, name):
        super(SmokeType, self).__init__(name)
        return

    def __repr__(self):
        return b'SmokeType()'


class Stun(object):
    __slots__ = (b'stunRadius', b'stunDuration', b'stunType', b'stunFactor', b'guaranteedStunDuration', b'damageDurationCoeff', b'guaranteedStunEffect', b'damageEffectCoeff', b'stunInPoint')

    def __init__(self):
        super(Stun, self).__init__()
        self.stunRadius = component_constants.ZERO_FLOAT
        self.stunDuration = component_constants.ZERO_FLOAT
        self.stunType = StunTypes.DEFAULT
        self.stunInPoint = False
        self.stunFactor = component_constants.ZERO_FLOAT
        self.guaranteedStunDuration = component_constants.ZERO_FLOAT
        self.damageDurationCoeff = component_constants.ZERO_FLOAT
        self.guaranteedStunEffect = component_constants.ZERO_FLOAT
        self.damageEffectCoeff = component_constants.ZERO_FLOAT
        return

    def __repr__(self):
        return (b'Stun(radius={}, duration={}, guaranteedDuration={}, damageDurationCoeff={} guaranteedSEffect={}, damageEffectCoeff={}, stunInPoint={})').format(self.stunRadius, self.stunDuration, self.guaranteedStunDuration, self.damageDurationCoeff, self.guaranteedStunEffect, self.damageEffectCoeff, self.stunInPoint)


def createShellType(typeName):
    shellType = None
    if typeName in (
     SHELL_TYPES.ARMOR_PIERCING,
     SHELL_TYPES.ARMOR_PIERCING_HE,
     SHELL_TYPES.ARMOR_PIERCING_FSDS,
     SHELL_TYPES.ARMOR_PIERCING_CR):
        shellType = ArmorPiercingType(typeName)
    elif typeName == SHELL_TYPES.HOLLOW_CHARGE:
        shellType = HollowChargeType(typeName)
    elif typeName in HAS_EXPLOSION_EFFECT:
        shellType = HighExplosiveType(typeName)
    elif typeName == SHELL_TYPES.SMOKE:
        shellType = SmokeType(typeName)
    return shellType
