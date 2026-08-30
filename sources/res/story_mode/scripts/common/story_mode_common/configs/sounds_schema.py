from __future__ import absolute_import
import typing
from dict2model import models
from dict2model.schemas import Schema
from dict2model.fields import String
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from dict2model.types import ValidatorsType
    from dict2model.fields import Field

class SoundModel(models.Model):
    __slots__ = (b'start', b'stop', b'group', b'state')

    def __init__(self, start, stop, group, state):
        super(SoundModel, self).__init__()
        self.start = start
        self.stop = stop
        self.group = group
        self.state = state
        return


_SoundModelType = typing.TypeVar(b'_SoundModelType', bound=SoundModel)

class SoundSchema(Schema[_SoundModelType]):

    def __init__(self, fields=None, modelClass=SoundModel, checkUnknown=True, serializedValidators=None, deserializedValidators=None):
        if not issubclass(modelClass, SoundModel):
            raise SoftException(b'modelClass should be a subclass of SoundModel')
        baseFields = {b'start': (String(required=False, default=b'')), 
           b'stop': (String(required=False, default=b'')), 
           b'group': (String(required=False, default=b'')), 
           b'state': (String(required=False, default=b''))}
        if fields is not None:
            baseFields.update(fields)
        super(SoundSchema, self).__init__(fields=baseFields, checkUnknown=checkUnknown, serializedValidators=serializedValidators, deserializedValidators=deserializedValidators, modelClass=modelClass)
        return


soundSchema = SoundSchema()
