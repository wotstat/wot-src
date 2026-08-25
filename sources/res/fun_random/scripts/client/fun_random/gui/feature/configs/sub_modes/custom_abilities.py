from __future__ import absolute_import
import typing
from dict2model import fields, models, schemas

class FunSubModeCustomAbilityConfigModel(models.Model):
    __slots__ = (b'intCD',)

    def __init__(self, intCD):
        super(FunSubModeCustomAbilityConfigModel, self).__init__()
        self.intCD = intCD
        return


class FunSubModeCustomAbilitySlotConfigModel(models.Model):
    __slots__ = (b'command', b'tooltipAlias')

    def __init__(self, command, tooltipAlias):
        super(FunSubModeCustomAbilitySlotConfigModel, self).__init__()
        self.command = command
        self.tooltipAlias = tooltipAlias
        return


class FunSubModeCustomAbilityLayoutConfigModel(models.Model):
    __slots__ = (b'abilityIndex', b'slotIndex')

    def __init__(self, abilityIndex, slotIndex):
        super(FunSubModeCustomAbilityLayoutConfigModel, self).__init__()
        self.abilityIndex = abilityIndex
        self.slotIndex = slotIndex
        return


class FunSubModeCustomAbilitiesConfigModel(models.Model):
    __slots__ = (b'abilities', b'slots', b'layouts')

    def __init__(self, abilities=None, slots=None, layouts=None):
        super(FunSubModeCustomAbilitiesConfigModel, self).__init__()
        self.abilities = abilities if abilities is not None else []
        self.slots = slots if slots is not None else []
        self.layouts = layouts if layouts is not None else []
        return

    @property
    def exists(self):
        return bool(self.layouts)


funSubModeCustomAbilitySchema = schemas.Schema[FunSubModeCustomAbilityConfigModel](fields={b'intCD': (fields.Integer(required=True))}, modelClass=FunSubModeCustomAbilityConfigModel)
funSubModeCustomAbilitySlotSchema = schemas.Schema[FunSubModeCustomAbilitySlotConfigModel](fields={b'command': (fields.String(required=False, default=b'')), 
   b'tooltipAlias': (fields.String(required=False, default=b''))}, modelClass=FunSubModeCustomAbilitySlotConfigModel)
funSubModeCustomAbilityLayoutSchema = schemas.Schema[FunSubModeCustomAbilityLayoutConfigModel](fields={b'abilityIndex': (fields.Integer(required=True)), 
   b'slotIndex': (fields.Integer(required=True))}, modelClass=FunSubModeCustomAbilityLayoutConfigModel)
funSubModeCustomAbilitiesSchema = schemas.Schema[FunSubModeCustomAbilitiesConfigModel](fields={b'abilities': (fields.UniCapList(fieldOrSchema=funSubModeCustomAbilitySchema, required=False)), 
   b'slots': (fields.UniCapList(fieldOrSchema=funSubModeCustomAbilitySlotSchema, required=False)), 
   b'layouts': (fields.UniCapList(fieldOrSchema=funSubModeCustomAbilityLayoutSchema, required=False))}, modelClass=FunSubModeCustomAbilitiesConfigModel)
