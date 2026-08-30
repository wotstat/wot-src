from __future__ import absolute_import
from armor_inspector_common.models import ArmorInspectorConfigModel
from game_params_common.schema import GameParamsSchema
from dict2model import fields
armorInspectorConfigSchema = GameParamsSchema[ArmorInspectorConfigModel](gameParamsKey=b'armor_inspector_config', fields={b'enabled': (fields.Boolean(required=True)), 
   b'linkButtonURL': (fields.String(required=False, default=None)), 
   b'disabledVehicle': (fields.UniCapList(fieldOrSchema=fields.String(required=True), required=False, default=list))}, modelClass=ArmorInspectorConfigModel)
