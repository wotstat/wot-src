from __future__ import absolute_import
from dict2model import fields, models, schemas

class GameModeConfigurationModel(models.Model):
    __slots__ = (b'regularDevices', b'regularBoosters', b'regularShells', b'regularConsumables')

    def __init__(self, regularDevices, regularBoosters, regularShells, regularConsumables):
        super(GameModeConfigurationModel, self).__init__()
        self.regularDevices = regularDevices
        self.regularBoosters = regularBoosters
        self.regularShells = regularShells
        self.regularConsumables = regularConsumables
        return


gameModeConfigurationSchema = schemas.Schema[GameModeConfigurationModel](fields={b'regularDevices': (fields.Boolean(required=True)), 
   b'regularBoosters': (fields.Boolean(required=True)), 
   b'regularShells': (fields.Boolean(required=True)), 
   b'regularConsumables': (fields.Boolean(required=True))}, modelClass=GameModeConfigurationModel)
