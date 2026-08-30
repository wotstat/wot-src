import typing
from game_params_common.schema import GameParamsSchema
from dict2model import models, fields, validate, schemas, exceptions
from story_mode_common.story_mode_constants import PRIORITY

class QuotumsModel(models.Model):
    __slots__ = (b'quotums',)

    def __init__(self, quotums):
        super(QuotumsModel, self).__init__()
        self.quotums = quotums
        return


class QuotumModel(models.Model):
    __slots__ = (b'priority', b'quotum')

    def __init__(self, priority, quotum):
        super(QuotumModel, self).__init__()
        self.priority = priority
        self.quotum = quotum
        return


def validatePriorityies(model):
    priorities, duplicates = set(), set()
    for q in model.quotums:
        if q.priority not in priorities:
            priorities.add(q.priority)
        else:
            duplicates.add(q.priority)

    if duplicates:
        raise exceptions.ValidationError((b'Priority duplicates: {}').format(duplicates))
    return


quotumSchema = schemas.Schema[QuotumModel](fields={b'priority': (fields.IntEnum(PRIORITY, required=True, deserializedValidators=validate.Range(minValue=0))), 
   b'quotum': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=0)))}, modelClass=QuotumModel, checkUnknown=True)
quotumsSchema = GameParamsSchema(gameParamsKey=b'story_mode_battle_mgr_quotums', fields={b'quotums': (fields.UniCapList(fieldOrSchema=quotumSchema, required=True, deserializedValidators=validate.Length(minValue=3)))}, modelClass=QuotumsModel, checkUnknown=True, deserializedValidators=[
 validatePriorityies], usedInReplay=True)
