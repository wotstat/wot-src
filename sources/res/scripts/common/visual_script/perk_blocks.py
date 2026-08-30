from visual_script.block import Meta, Block
from visual_script.slot_types import SLOT_TYPE
from constants import IS_EDITOR
if not IS_EDITOR:
    from items import perks
    from items.components.perks_constants import PERK_BONUS_VALUE_PRECISION
    from debug_utils import LOG_ERROR

class Perk(Meta):

    @classmethod
    def blockCategory(cls):
        return b'Perks'


class AddFactorModifierBase(Block, Perk):

    def __init__(self, *args, **kwargs):
        super(AddFactorModifierBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._vehId = self._makeDataInputSlot(b'vehId', SLOT_TYPE.INT)
        self._perkId = self._makeDataInputSlot(b'perkId', SLOT_TYPE.INT)
        self._scopeId = self._makeDataInputSlot(b'scopeId', SLOT_TYPE.INT)
        self._value = self._makeDataInputSlot(b'value', SLOT_TYPE.FLOAT)
        self._factor = self._makeDataInputSlot(b'factor', SLOT_TYPE.STR)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class RemoveFactorModifiersBase(Block, Perk):

    def __init__(self, *args, **kwargs):
        super(RemoveFactorModifiersBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._vehId = self._makeDataInputSlot(b'vehId', SLOT_TYPE.INT)
        self._perkId = self._makeDataInputSlot(b'perkId', SLOT_TYPE.INT)
        self._scopeId = self._makeDataInputSlot(b'scopeId', SLOT_TYPE.INT)
        self._factor = self._makeDataInputSlot(b'factor', SLOT_TYPE.STR)
        self._numMods = self._makeDataInputSlot(b'numMods', SLOT_TYPE.INT)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class DropAllPerkModifiersBase(Block, Perk):

    def __init__(self, *args, **kwargs):
        super(DropAllPerkModifiersBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._vehId = self._makeDataInputSlot(b'vehId', SLOT_TYPE.INT)
        self._perkId = self._makeDataInputSlot(b'perkId', SLOT_TYPE.INT)
        self._scopeId = self._makeDataInputSlot(b'scopeId', SLOT_TYPE.INT)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class VehicleInRangeLoopBase(Block, Perk):

    def __init__(self, *args, **kwargs):
        super(VehicleInRangeLoopBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._vehicle = self._makeDataInputSlot(b'vehicle', SLOT_TYPE.VEHICLE)
        self._vehTeam = self._makeDataInputSlot(b'vehTeam', SLOT_TYPE.INT)
        self._vehClass = self._makeDataInputSlot(b'vehClass', SLOT_TYPE.STR)
        self._range = self._makeDataInputSlot(b'range', SLOT_TYPE.INT)
        self._interval = self._makeDataInputSlot(b'interval', SLOT_TYPE.FLOAT)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class ModifyTerrainResistanceBase(Block):

    def __init__(self, *args, **kwargs):
        super(ModifyTerrainResistanceBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._perk = self._makeDataInputSlot(b'perk', SLOT_TYPE.PERK)
        self._firmGroundFactor = self._makeDataInputSlot(b'firmGroundFactor', SLOT_TYPE.FLOAT)
        self._mediumGroundFactor = self._makeDataInputSlot(b'mediumGroundFactor', SLOT_TYPE.FLOAT)
        self._softGroundFactor = self._makeDataInputSlot(b'softGroundFactor', SLOT_TYPE.FLOAT)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class AddDeviceHitModifierBase(Block, Perk):

    def __init__(self, *args, **kwargs):
        super(AddDeviceHitModifierBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._perk = self._makeDataInputSlot(b'perk', SLOT_TYPE.PERK)
        self._value = self._makeDataInputSlot(b'value', SLOT_TYPE.FLOAT)
        self._device = self._makeDataInputSlot(b'device', SLOT_TYPE.E_VEHICLE_DEVICE)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class AddEquipmentCooldownModifierBase(Block, Perk):

    def __init__(self, *args, **kwargs):
        super(AddEquipmentCooldownModifierBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._perk = self._makeDataInputSlot(b'perk', SLOT_TYPE.PERK)
        self._value = self._makeDataInputSlot(b'value', SLOT_TYPE.FLOAT)
        self._equipmentName = self._makeDataInputSlot(b'equipmentName', SLOT_TYPE.STR)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class RemoveEquipmentCooldownModifierBase(Block, Perk):

    def __init__(self, *args, **kwargs):
        super(RemoveEquipmentCooldownModifierBase, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._perk = self._makeDataInputSlot(b'perk', SLOT_TYPE.PERK)
        self._equipmentName = self._makeDataInputSlot(b'equipmentName', SLOT_TYPE.STR)
        self._outSlot = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        return


class PerkArgumentBase(Block):

    def __init__(self, *args, **kwargs):
        super(PerkArgumentBase, self).__init__(*args, **kwargs)
        self._perk = self._makeDataInputSlot(b'perk', SLOT_TYPE.PERK)
        self._argument = self._makeDataInputSlot(b'argument', SLOT_TYPE.STR)
        self._outSlot1 = self._makeDataOutputSlot(b'value', SLOT_TYPE.FLOAT, self._execute)
        return

    def _execute(self):
        argument = self._argument.getValue()
        perk = self._perk.getValue()
        perkId = perk.perkID
        level = perk.perkLevel
        perkItem = perks.g_cache.perks.get(perkId)
        argRecord = perkItem.defaultBlockSettings.get(argument)
        if not argRecord:
            LOG_ERROR((b'Perk item do not contain argument {}').format(argument))
            return
        value = perkItem.getArgBonusByLevel(argument, level)
        self._outSlot1.setValue(round(value, PERK_BONUS_VALUE_PRECISION))
        return
