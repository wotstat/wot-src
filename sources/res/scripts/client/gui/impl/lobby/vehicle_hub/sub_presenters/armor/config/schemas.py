from __future__ import absolute_import
from dict2model import schemas, fields, validate
from gui.impl.lobby.vehicle_hub.sub_presenters.armor.config.models import ArmorScaleModel, ColorListModel, TierModel, ConfigModel, TierListModel
TIER_MIN_VALUE = 1
TIER_MAX_VALUE = 11
colorListSchema = schemas.Schema(fields={b'normalArmor': (fields.UniCapList(fieldOrSchema=fields.String(required=True), required=True, deserializedValidators=validate.Length(minValue=2))), 
   b'spacedArmor': (fields.UniCapList(fieldOrSchema=fields.String(required=True), required=True, deserializedValidators=validate.Length(minValue=2))), 
   b'ricochet': (fields.String(required=True)), 
   b'noDamage': (fields.String(required=True))}, modelClass=ColorListModel)
armorScaleSchema = schemas.Schema(fields={b'min': (fields.Integer(required=True)), 
   b'max': (fields.Integer(required=True))}, modelClass=ArmorScaleModel)
tierSchema = schemas.Schema(fields={b'number': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=TIER_MIN_VALUE, maxValue=TIER_MAX_VALUE))), 
   b'normalArmor': (fields.Nested(schema=armorScaleSchema, required=True)), 
   b'spacedArmor': (fields.Nested(schema=armorScaleSchema, required=True)), 
   b'defaultVehicle': (fields.String(required=True))}, modelClass=TierModel)
tierListSchema = schemas.Schema(fields={b'tier': (fields.UniCapList(fieldOrSchema=tierSchema, required=True))}, modelClass=TierListModel)
configSchema = schemas.Schema(fields={b'tierList': (fields.Nested(schema=tierListSchema, required=True)), 
   b'colorList': (fields.Nested(schema=colorListSchema, required=True)), 
   b'blindColorList': (fields.Nested(schema=colorListSchema, required=True)), 
   b'blendingAlpha': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=0, maxValue=1)))}, modelClass=ConfigModel)
__config = None
