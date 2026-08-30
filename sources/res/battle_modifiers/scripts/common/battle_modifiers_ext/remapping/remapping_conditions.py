from __future__ import absolute_import
from future.utils import viewitems
from typing import Dict, FrozenSet, TYPE_CHECKING
from battle_modifiers_ext.constants_ext import GunCaliber, ShellCaliber, ShellKind, RemappingConditionNames
from nations import NAMES
if TYPE_CHECKING:
    from battle_modifiers_common import ModifiersContext

class IRemappingCondition(object):
    __slots__ = ()

    @classmethod
    def getName(cls):
        raise NotImplementedError
        return

    def __call__(self, ctx):
        raise NotImplementedError
        return


class _BaseCondition(IRemappingCondition):
    __slots__ = (b'_remappingName', b'_remapping')
    _CONDITION_NAME = b'baseCondition'

    def __init__(self, remappingName, remapping):
        self._remappingName = remappingName
        self._remapping = remapping
        return

    def __call__(self, ctx):
        currentParam = self._getParam(ctx)
        if not self._remapping:
            return currentParam
        for sources, target in viewitems(self._remapping):
            if currentParam in sources:
                return target

        return b''

    @classmethod
    def getName(cls):
        return cls._CONDITION_NAME

    def _getParam(self, ctx):
        raise NotImplementedError
        return


class _RemappingNameCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.REMAPPING_NAME

    def _getParam(self, ctx):
        return self._remappingName


class _NationCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.NATION

    def _getParam(self, ctx):
        return NAMES[ctx.modificationCtx[b'vehType'].id[0]]


class _OutfitCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.OUTFIT

    def _getParam(self, ctx):
        outfit = ctx.modificationCtx[b'outfit']
        if outfit != b'default':
            return outfit
        return b''


class _GunNameCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.GUN_NAME

    def _getParam(self, ctx):
        return ctx.modificationCtx[b'gun'].name


class _GunCaliberCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.GUN_CALIBER

    def _getParam(self, ctx):
        return GunCaliber.get(ctx.modificationCtx[b'gun'].effectsCaliber)


class _ShellKindCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.SHELL_KIND

    def _getParam(self, ctx):
        return ShellKind.get(ctx.modificationCtx[b'shell'], withGold=False)


class _ShellShotsCountCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.SHELL_SHOTS_COUNT

    def _getParam(self, ctx):
        shotsCount = ctx.modificationCtx[b'shotsCount']
        if shotsCount > 0:
            return str(shotsCount)
        return b''


class _ShellCaliberCondition(_BaseCondition):
    __slots__ = ()
    _CONDITION_NAME = RemappingConditionNames.SHELL_CALIBER

    def _getParam(self, ctx):
        return ShellCaliber.get(ctx.modificationCtx[b'gun'].shots[0].shell.effectsCaliber)


_CONDITIONS_FACTORY = {(RemappingConditionNames.REMAPPING_NAME): _RemappingNameCondition, 
   (RemappingConditionNames.NATION): _NationCondition, 
   (RemappingConditionNames.OUTFIT): _OutfitCondition, 
   (RemappingConditionNames.GUN_CALIBER): _GunCaliberCondition, 
   (RemappingConditionNames.GUN_NAME): _GunNameCondition, 
   (RemappingConditionNames.SHELL_KIND): _ShellKindCondition, 
   (RemappingConditionNames.SHELL_SHOTS_COUNT): _ShellShotsCountCondition, 
   (RemappingConditionNames.SHELL_CALIBER): _ShellCaliberCondition}

def getConditionClass(conditionName):
    return _CONDITIONS_FACTORY.get(conditionName)
