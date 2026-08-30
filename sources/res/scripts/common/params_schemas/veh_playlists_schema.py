from __future__ import absolute_import
from game_params_common.schema import GameParamsSchema
from constants import Configs
from dict2model import models, fields as d2mfields

class VehPlaylistsConfigModel(models.Model):
    __slots__ = (b'isVehPlaylistsEnabled',)

    def __init__(self, isVehPlaylistsEnabled):
        super(VehPlaylistsConfigModel, self).__init__()
        self.isVehPlaylistsEnabled = isVehPlaylistsEnabled
        return


vehPlaylistsConfigSchema = GameParamsSchema[VehPlaylistsConfigModel](gameParamsKey=Configs.VEH_PLAYLISTS_CONFIG.value, fields={b'isVehPlaylistsEnabled': (d2mfields.Boolean())}, modelClass=VehPlaylistsConfigModel, checkUnknown=True)
