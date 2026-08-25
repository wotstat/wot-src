import typing
from dict2model import fields, schemas, validate
from gui.collection.resources.cdn.models import ConfigModel, Group, ImageModel, Sub
if typing.TYPE_CHECKING:
    from typing import Dict, Optional
imageSchema = schemas.Schema(fields={b'group': (fields.StrEnum(Group, required=True)), 
   b'sub': (fields.StrEnum(Sub, required=True)), 
   b'name': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   b'url': (fields.Url(required=True, relative=False))}, modelClass=ImageModel, checkUnknown=True)
configSchema = schemas.Schema(fields={b'images': (fields.List(fieldOrSchema=imageSchema, required=True))}, modelClass=ConfigModel, checkUnknown=True)

def createConfigModel(rawData):
    return configSchema.deserialize(rawData, silent=True)
