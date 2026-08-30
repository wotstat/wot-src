from __future__ import absolute_import
import typing
from dict2model import models

class ColorListModel(models.Model):
    __slots__ = (b'normalArmor', b'spacedArmor', b'ricochet', b'noDamage')

    def __init__(self, normalArmor, spacedArmor, ricochet, noDamage):
        super(ColorListModel, self).__init__()
        self.normalArmor = normalArmor
        self.spacedArmor = spacedArmor
        self.ricochet = ricochet
        self.noDamage = noDamage
        return

    def __repr__(self):
        return (b'<ColorListModel(normalArmor={}, spacedArmor={}, ricochet={}, no_damage={})>').format(self.normalArmor, self.spacedArmor, self.ricochet, self.noDamage)


class ArmorScaleModel(models.Model):
    __slots__ = (b'min', b'max')

    def __init__(self, min, max):
        super(ArmorScaleModel, self).__init__()
        self.min = min
        self.max = max
        return

    def __repr__(self):
        return (b'<ArmorScaleModel(min={}, max={})>').format(self.min, self.max)


class TierModel(models.Model):
    __slots__ = (b'number', b'normalArmor', b'spacedArmor', b'defaultVehicle')

    def __init__(self, number, normalArmor, spacedArmor, defaultVehicle):
        super(TierModel, self).__init__()
        self.number = number
        self.normalArmor = normalArmor
        self.spacedArmor = spacedArmor
        self.defaultVehicle = defaultVehicle
        return

    def __repr__(self):
        return (b'<TierModel(number={}, normalArmor={}, spacedArmor={}, defaultVehicle={})>').format(self.number, self.normalArmor, self.spacedArmor, self.defaultVehicle)


class TierListModel(models.Model):
    __slots__ = (b'tier',)

    def __init__(self, tier):
        super(TierListModel, self).__init__()
        self.tier = tier
        return

    def __repr__(self):
        return (b'<TierListModel(tier={})>').format(self.tier)

    def getTierModel(self, tier):
        return next(m for m in self.tier if m.number == tier)


class ConfigModel(models.Model):
    __slots__ = (b'tierList', b'colorList', b'blindColorList', b'blendingAlpha')

    def __init__(self, tierList, colorList, blindColorList, blendingAlpha):
        super(ConfigModel, self).__init__()
        self.tierList = tierList
        self.colorList = colorList
        self.blindColorList = blindColorList
        self.blendingAlpha = blendingAlpha
        return

    def getActualColorList(self, isColorBlind):
        if isColorBlind:
            return self.blindColorList
        return self.colorList

    def _reprArgs(self):
        return (b'tierList={}, colorList={}, blindColorList={}, blendingAlpha={}').format(self.tierList, self.colorList, self.blindColorList, self.blendingAlpha)
