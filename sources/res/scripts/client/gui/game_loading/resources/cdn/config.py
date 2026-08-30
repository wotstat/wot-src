import typing
from dict2model import fields
from dict2model import schemas
from dict2model import validate
from dict2model import exceptions
from constants import MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL
from gui.game_loading import loggers
from gui.game_loading.resources.cdn.consts import SequenceOrders, SequenceCohorts, MAX_CONFIG_SEQUENCE_SLIDES_COUNT, MAX_CONFIG_SEQUENCES_COUNT, NEWBIES_BATTLES_LIMIT, NEWBIES_VEHICLE_LEVEL
from gui.game_loading.resources.consts import ImageVfxs
from gui.game_loading.resources.cdn.models import ConfigSequenceModel, ConfigModel, ConfigSlideModel, AdditionalImageModel, NewbiesCohortSettingsModel
_logger = loggers.getCdnConfigLogger()

def _validateSequenceLifeTime(model):
    if model.start >= model.finish:
        raise exceptions.ValidationError((b'Started date: {} >= finished: {}').format(model.start, model.finish))
    return


def _validateSequencesNames(model):
    sequencesNames, nameDuplicates = set(), set()
    for sequence in model.sequences:
        if sequence.name in sequencesNames:
            nameDuplicates.add(sequence.name)
        else:
            sequencesNames.add(sequence.name)

    if nameDuplicates:
        raise exceptions.ValidationError((b'Sequence name duplicates: {}').format(nameDuplicates))
    return


additionalImage = schemas.Schema(fields={b'image': (fields.Url(required=True, relative=False)), 
   b'width': (fields.Integer(required=True)), 
   b'height': (fields.Integer(required=True)), 
   b'margins': (fields.List(fields.Integer(), required=False, default=(0, 0, 0, 0))), 
   b'paddings': (fields.List(fields.Integer(), required=False, default=(0, 0, 0, 0))), 
   b'position': (fields.String(required=False, default=b'BL'))}, modelClass=AdditionalImageModel, checkUnknown=True)
slideSchema = schemas.Schema(fields={b'image': (fields.Url(required=True, relative=False)), 
   b'vfx': (fields.Enum(ImageVfxs, required=False, default=None)), 
   b'localization': (fields.Url(required=False, relative=False, default=None)), 
   b'additionalImage': (fields.Nested(schema=additionalImage, required=False)), 
   b'sound': (fields.String(required=False, default=b''))}, modelClass=ConfigSlideModel, checkUnknown=True)
sequenceSchema = schemas.Schema(fields={b'name': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   b'start': (fields.DateTime(required=True)), 
   b'finish': (fields.DateTime(required=True)), 
   b'priority': (fields.Integer(required=True, serializedValidators=validate.Range(minValue=0), deserializedValidators=validate.Range(minValue=0))), 
   b'order': (fields.Enum(SequenceOrders, required=True)), 
   b'slides': (fields.List(slideSchema, required=True, serializedValidators=validate.Length(minValue=1, maxValue=MAX_CONFIG_SEQUENCE_SLIDES_COUNT), deserializedValidators=validate.Length(minValue=1, maxValue=MAX_CONFIG_SEQUENCE_SLIDES_COUNT))), 
   b'views': (fields.Integer(required=False, default=0)), 
   b'enabled': (fields.Boolean(required=False, default=True)), 
   b'cohorts': (fields.List(fields.Enum(SequenceCohorts), required=False, default=SequenceCohorts.getDefaults, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1)))}, modelClass=ConfigSequenceModel, checkUnknown=True, deserializedValidators=_validateSequenceLifeTime)
newbiesCohortSchema = schemas.Schema(fields={b'battlesCount': (fields.Integer(required=False, default=NEWBIES_BATTLES_LIMIT, serializedValidators=validate.Range(minValue=0), deserializedValidators=validate.Range(minValue=0))), 
   b'vehicleLevel': (fields.Integer(required=False, default=NEWBIES_VEHICLE_LEVEL, serializedValidators=validate.Range(minValue=MIN_VEHICLE_LEVEL, maxValue=MAX_VEHICLE_LEVEL), deserializedValidators=validate.Range(minValue=MIN_VEHICLE_LEVEL, maxValue=MAX_VEHICLE_LEVEL)))}, modelClass=NewbiesCohortSettingsModel, checkUnknown=True)
configSchema = schemas.Schema(fields={b'enabled': (fields.Boolean(required=True)), 
   b'sequences': (fields.List(fieldOrSchema=sequenceSchema, required=True, deserializedValidators=validate.Length(minValue=1, maxValue=MAX_CONFIG_SEQUENCES_COUNT))), 
   b'newbiesCohort': (fields.Nested(schema=newbiesCohortSchema, required=False, default=NewbiesCohortSettingsModel))}, modelClass=ConfigModel, checkUnknown=True, deserializedValidators=_validateSequencesNames)

def dumpSequenceModel(model):
    return sequenceSchema.serialize(model, silent=True)


def createSequenceModel(rawData):
    return sequenceSchema.deserialize(rawData, silent=True)


def createConfigModel(rawData):
    return configSchema.deserialize(rawData, silent=True)
