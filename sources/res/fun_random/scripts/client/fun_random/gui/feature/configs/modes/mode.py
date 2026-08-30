from __future__ import absolute_import
import typing
from dict2model import fields, models, schemas
from fun_random.gui.feature.configs.modes.assets_pack import funModeAssetsPackConfigurationSchema
if typing.TYPE_CHECKING:
    from fun_random.gui.feature.configs.modes.assets_pack import FunModeAssetsPackConfigurationModel

class FunModeConfigurationModel(models.Model):
    __slots__ = (b'assetsPack',)

    def __init__(self, assetsPack):
        super(FunModeConfigurationModel, self).__init__()
        self.assetsPack = assetsPack
        return


class FunModeCompositeConfigurationModel(models.Model):
    __slots__ = (b'mode',)

    def __init__(self, mode):
        super(FunModeCompositeConfigurationModel, self).__init__()
        self.mode = mode
        return


funModeConfigurationSchema = schemas.Schema[FunModeConfigurationModel](fields={b'assetsPack': (fields.Nested(schema=funModeAssetsPackConfigurationSchema, required=True))}, modelClass=FunModeConfigurationModel)
funModeCompositeConfigurationSchema = schemas.Schema[FunModeCompositeConfigurationModel](fields={b'mode': (fields.Nested(schema=funModeConfigurationSchema, required=True))}, modelClass=FunModeCompositeConfigurationModel)
