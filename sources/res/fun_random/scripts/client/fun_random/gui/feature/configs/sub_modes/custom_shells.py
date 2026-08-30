from __future__ import absolute_import
import typing
from dict2model import fields, models, schemas
from fun_random.gui.feature.fun_constants import FunCustomShellsSource

class FunSubModeCustomShellConfigModel(models.Model):
    __slots__ = (b'intCD',)

    def __init__(self, intCD):
        super(FunSubModeCustomShellConfigModel, self).__init__()
        self.intCD = intCD
        return


class FunSubModeCustomShellSlotConfigModel(models.Model):
    __slots__ = (b'command', b'imageOverride', b'tooltipOverride')

    def __init__(self, command, imageOverride, tooltipOverride):
        super(FunSubModeCustomShellSlotConfigModel, self).__init__()
        self.command = command
        self.imageOverride = imageOverride
        self.tooltipOverride = tooltipOverride
        return


class FunSubModeCustomShellLayoutConfigModel(models.Model):
    __slots__ = (b'shellSource', b'shellIndex', b'shellCount', b'slotIndex')

    def __init__(self, shellSource, shellIndex, shellCount, slotIndex):
        super(FunSubModeCustomShellLayoutConfigModel, self).__init__()
        self.shellSource = shellSource
        self.shellIndex = shellIndex
        self.shellCount = shellCount
        self.slotIndex = slotIndex
        return


class FunSubModeCustomShellsConfigModel(models.Model):
    __slots__ = (b'shells', b'slots', b'layouts')

    def __init__(self, shells=None, slots=None, layouts=None):
        super(FunSubModeCustomShellsConfigModel, self).__init__()
        self.shells = shells if shells is not None else []
        self.slots = slots if slots is not None else []
        self.layouts = layouts if layouts is not None else []
        return

    @property
    def exists(self):
        return bool(self.layouts)


funSubModeCustomShellSchema = schemas.Schema[FunSubModeCustomShellConfigModel](fields={b'intCD': (fields.Integer(required=True))}, modelClass=FunSubModeCustomShellConfigModel)
funSubModeCustomShellSlotSchema = schemas.Schema[FunSubModeCustomShellSlotConfigModel](fields={b'command': (fields.String(required=False, default=b'')), 
   b'imageOverride': (fields.String(required=False, default=b'')), 
   b'tooltipOverride': (fields.String(required=False, default=b''))}, modelClass=FunSubModeCustomShellSlotConfigModel)
funSubModeCustomShellLayoutSchema = schemas.Schema[FunSubModeCustomShellLayoutConfigModel](fields={b'shellSource': (fields.StrEnum(enumClass=FunCustomShellsSource, required=True)), 
   b'shellIndex': (fields.Integer(required=True)), 
   b'shellCount': (fields.Integer(required=False, default=0)), 
   b'slotIndex': (fields.Integer(required=True))}, modelClass=FunSubModeCustomShellLayoutConfigModel)
funSubModeCustomShellsSchema = schemas.Schema[FunSubModeCustomShellsConfigModel](fields={b'shells': (fields.UniCapList(fieldOrSchema=funSubModeCustomShellSchema, required=False)), 
   b'slots': (fields.UniCapList(fieldOrSchema=funSubModeCustomShellSlotSchema, required=False)), 
   b'layouts': (fields.UniCapList(fieldOrSchema=funSubModeCustomShellLayoutSchema, required=False))}, modelClass=FunSubModeCustomShellsConfigModel)
