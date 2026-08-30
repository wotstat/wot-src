from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from constants import Configs
from dict2model import fields, models
from dict2model.schemas import Schema

class _InterfacesModel(models.Model):
    __slots__ = (b'postbattle', b'spectatorMode')

    def __init__(self, postbattle, spectatorMode):
        super(_InterfacesModel, self).__init__()
        self.postbattle = postbattle
        self.spectatorMode = spectatorMode
        return

    def _reprArgs(self):
        return (b'postbattle={}, spectatorMode={}').format(self.postbattle, self.spectatorMode)


_interfacesSchema = Schema[_InterfacesModel](fields={b'postbattle': (fields.Boolean(required=False, default=False)), 
   b'spectatorMode': (fields.Boolean(required=False, default=False))}, modelClass=_InterfacesModel, checkUnknown=True)

class PlayerSatisfactionConfigModel(models.Model):
    __slots__ = (b'enabled', b'enabledInterfaces')

    def __init__(self, enabled, enabledInterfaces):
        super(PlayerSatisfactionConfigModel, self).__init__()
        self.enabled = enabled
        self.enabledInterfaces = enabledInterfaces
        return

    def _reprArgs(self):
        return (b'enabled={}, enabledInterfaces={}').format(self.enabled, self.enabledInterfaces)


playerSatisfactionSchema = GameParamsSchema[PlayerSatisfactionConfigModel](gameParamsKey=Configs.PLAYER_SATISFACTION_CONFIG.value, fields={b'enabled': (fields.Boolean(required=True)), 
   b'enabledInterfaces': (fields.Nested(_interfacesSchema, required=True))}, modelClass=PlayerSatisfactionConfigModel, checkUnknown=True, usedInReplay=True)
