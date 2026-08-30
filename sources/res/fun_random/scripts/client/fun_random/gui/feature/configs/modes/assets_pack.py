from __future__ import absolute_import
import typing
from dict2model import fields, models, schemas
from gui.impl.gen import R

class FunModeAssetsPackConfigurationModel(models.Model):
    __slots__ = (b'assetsPointer', b'hangarEventBanner', b'progressionView')

    def __init__(self, assetsPointer, hangarEventBanner, progressionView):
        super(FunModeAssetsPackConfigurationModel, self).__init__()
        self.assetsPointer = assetsPointer
        self.hangarEventBanner = hangarEventBanner
        self.progressionView = progressionView
        return

    def getIconsResRoot(self):
        return R.images.fun_random.gui.maps.icons.feature.asset_packs.modes.dyn(self.assetsPointer, R.images.fun_random.gui.maps.icons.feature.asset_packs.modes.undefined)

    def getLocalsResRoot(self):
        return R.strings.fun_random.modes.dyn(self.assetsPointer, R.strings.fun_random.modes.undefined)


class FunHangarEventBannerConfigModel(models.Model):
    __slots__ = (b'borderColor',)

    def __init__(self, borderColor):
        super(FunHangarEventBannerConfigModel, self).__init__()
        self.borderColor = borderColor
        return


class FunProgressionViewConfigModel(models.Model):
    __slots__ = (b'pointsTitleFontColors', b'pointsValueFontColor', b'stagesFontColors', b'rewardCounterFontColor')

    def __init__(self, pointsTitleFontColors, pointsValueFontColor, stagesFontColors, rewardCounterFontColor):
        super(FunProgressionViewConfigModel, self).__init__()
        self.pointsTitleFontColors = pointsTitleFontColors
        self.pointsValueFontColor = pointsValueFontColor
        self.stagesFontColors = stagesFontColors
        self.rewardCounterFontColor = rewardCounterFontColor
        return


funHangarEventBannerConfigurationSchema = schemas.Schema[FunHangarEventBannerConfigModel](fields={b'borderColor': (fields.HexColorCode(required=True))}, modelClass=FunHangarEventBannerConfigModel)
funProgressionViewConfigurationSchema = schemas.Schema[FunProgressionViewConfigModel](fields={b'pointsTitleFontColors': (fields.Dict(keyFieldOrSchema=fields.String(required=True), valueFieldOrSchema=fields.HexColorCode(required=True), required=True)), 
   b'pointsValueFontColor': (fields.HexColorCode(required=True)), 
   b'stagesFontColors': (fields.Dict(keyFieldOrSchema=fields.String(required=True), valueFieldOrSchema=fields.HexColorCode(required=True), required=True)), 
   b'rewardCounterFontColor': (fields.HexColorCode(required=True))}, modelClass=FunProgressionViewConfigModel)
funModeAssetsPackConfigurationSchema = schemas.Schema[FunModeAssetsPackConfigurationModel](fields={b'assetsPointer': (fields.String(required=True)), 
   b'hangarEventBanner': (fields.Nested(schema=funHangarEventBannerConfigurationSchema, required=True)), 
   b'progressionView': (fields.Nested(schema=funProgressionViewConfigurationSchema, required=True))}, modelClass=FunModeAssetsPackConfigurationModel)
