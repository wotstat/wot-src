import typing, BattleReplay, ResMgr, section2dict
from armor_flashlight_common.server_config import serverConfigSchema
from debug_utils import LOG_ERROR
from dict2model import models, schemas, fields, validate
from dict2model.exceptions import ValidationError
from dict2model.extensions.color import ColorModel, colorSchema
if typing.TYPE_CHECKING:
    from typing import Tuple
    from Math import Vector4
_CONFIG_PATH = b'gui/armor_flashlight_config.xml'
_DEFAULT_RESOLUTION_INDEX = 0
_config = None

class ArmorPiercingColorsSchemaModel(models.Model):
    __slots__ = (b'notPierced', b'littlePierced', b'greatPierced')

    def __init__(self, notPierced, littlePierced, greatPierced):
        super(ArmorPiercingColorsSchemaModel, self).__init__()
        self.notPierced = notPierced
        self.littlePierced = littlePierced
        self.greatPierced = greatPierced
        return

    def toFloats(self):
        return (
         self.notPierced.toFloats(), self.littlePierced.toFloats(), self.greatPierced.toFloats())

    def _reprArgs(self):
        return (b'notPierced={}, littlePierced={}, greatPierced={}').format(self.notPierced, self.littlePierced, self.greatPierced)


_armorPiercingColorsSchema = schemas.Schema(fields={b'notPierced': (fields.Nested(colorSchema)), 
   b'littlePierced': (fields.Nested(colorSchema)), 
   b'greatPierced': (fields.Nested(colorSchema))}, modelClass=ArmorPiercingColorsSchemaModel)

class ColorSchemaModel(models.Model):
    __slots__ = (b'name', b'normal', b'colorBlindness')

    def __init__(self, name, normal, colorBlindness):
        super(ColorSchemaModel, self).__init__()
        self.name = name
        self.normal = normal
        self.colorBlindness = colorBlindness
        return

    def _reprArgs(self):
        return (b'name={}, normal={}, colorBlindness={}').format(self.name, self.normal, self.colorBlindness)


_colorSchemaSchema = schemas.Schema(fields={b'name': (fields.NonEmptyString()), 
   b'normal': (fields.Nested(_armorPiercingColorsSchema)), 
   b'colorBlindness': (fields.Nested(_armorPiercingColorsSchema))}, modelClass=ColorSchemaModel)

class PatternModel(models.Model):
    __slots__ = (b'name', b'texturePath')

    def __init__(self, name, texturePath):
        super(PatternModel, self).__init__()
        self.name = name
        self.texturePath = texturePath
        return

    def _reprArgs(self):
        return (b'name={}, texturePath={}').format(self.name, self.texturePath)


_patternSchema = schemas.Schema(fields={b'name': (fields.NonEmptyString()), 
   b'texturePath': (fields.NonEmptyString())}, modelClass=PatternModel)

class DistanceConfigModel(models.Model):
    __slots__ = (b'distance', b'value')

    def __init__(self, distance, value):
        super(DistanceConfigModel, self).__init__()
        self.distance = distance
        self.value = value
        return

    def _reprArgs(self):
        return (b'distance={}, value={}').format(self.distance, self.value)

    def getTuple(self):
        return (
         self.distance, self.value)

    @staticmethod
    def sortedByDist(config):
        return sorted(config, key=(lambda x: x.distance))


_distanceConfigSchema = schemas.Schema(fields={b'distance': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=0))), 
   b'value': (fields.Float(required=True))}, modelClass=DistanceConfigModel)

class ResolutionModel(models.Model):
    __slots__ = (b'name', b'downscale')

    def __init__(self, name, downscale):
        super(ResolutionModel, self).__init__()
        self.name = name
        self.downscale = downscale
        return

    def _reprArgs(self):
        return (b'name={}, downscale={}').format(self.name, self.downscale)


_resolutionSchema = schemas.Schema(fields={b'name': (fields.NonEmptyString(required=True)), 
   b'downscale': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=1.0)))}, modelClass=ResolutionModel)

class DefaultResolutionByPostProcessingModel(models.Model):
    __slots__ = (b'postProcessingLevel', b'maxResolutionName')

    def __init__(self, postProcessingLevel, maxResolutionName):
        super(DefaultResolutionByPostProcessingModel, self).__init__()
        self.postProcessingLevel = postProcessingLevel
        self.maxResolutionName = maxResolutionName
        return

    def _reprArgs(self):
        return (b'postProcessingLevel={}, maxResolutionName={}').format(self.postProcessingLevel, self.maxResolutionName)


_defaultResolutionByPostProcessingSchema = schemas.Schema(fields={b'postProcessingLevel': (fields.Integer(required=True, deserializedValidators=validate.Range(minValue=0, maxValue=4))), 
   b'maxResolutionName': (fields.NonEmptyString(required=True, deserializedValidators=validate.Range(minValue=1)))}, modelClass=DefaultResolutionByPostProcessingModel)

class ConfigModel(models.Model):
    __slots__ = (b'colorSchemas', b'patterns', b'textureTilingFactor', b'alphaByDist', b'radiusByDist', b'appearanceDurationByDist', b'resolutions', b'defaultResolutionByPostProcessing', b'noiseIntensityMultiplier', b'maxSizePercentOfWindow', b'fadeoffFactorWhenNotAimed', b'borderSmoothness', b'aimingCircleAdjustment', b'smoothnessInAimingCircleAdjustment')

    def __init__(self, colorSchemas, patterns, textureTilingFactor, alphaByDist, radiusByDist, appearanceDurationByDist, resolutions, defaultResolutionByPostProcessing, noiseIntensityMultiplier, maxSizePercentOfWindow, fadeoffFactorWhenNotAimed, borderSmoothness, aimingCircleAdjustment, smoothnessInAimingCircleAdjustment):
        super(ConfigModel, self).__init__()
        self.colorSchemas = colorSchemas
        self.patterns = patterns
        self.textureTilingFactor = textureTilingFactor
        self.alphaByDist = DistanceConfigModel.sortedByDist(alphaByDist)
        self.radiusByDist = DistanceConfigModel.sortedByDist(radiusByDist)
        self.appearanceDurationByDist = DistanceConfigModel.sortedByDist(appearanceDurationByDist)
        self.resolutions = resolutions
        self.defaultResolutionByPostProcessing = defaultResolutionByPostProcessing
        self.noiseIntensityMultiplier = noiseIntensityMultiplier
        self.maxSizePercentOfWindow = maxSizePercentOfWindow
        self.fadeoffFactorWhenNotAimed = fadeoffFactorWhenNotAimed
        self.borderSmoothness = borderSmoothness
        self.aimingCircleAdjustment = aimingCircleAdjustment
        self.smoothnessInAimingCircleAdjustment = smoothnessInAimingCircleAdjustment
        return

    def getSchemaColorFloatsByIndex(self, index, isColorBlind):
        schema = self.colorSchemas[index].colorBlindness if isColorBlind else self.colorSchemas[index].normal
        return schema.toFloats()

    def getPatternByIndex(self, index):
        return self.patterns[index].texturePath

    @staticmethod
    def getDistanceConfigTupleList(config):
        return [item.getTuple() for item in config]

    def getResolutionDownscaleByIndex(self, index):
        return self.resolutions[index].downscale

    def getResolutionIndexByPostProcessing(self, postProcessingLevel):
        resolution = self._getDefaultResolutionByPostProcessing(postProcessingLevel)
        return self._getResolutionIndexByName(resolution.maxResolutionName)

    def _getDefaultResolutionByPostProcessing(self, postProcessingLevel):
        for resByPostProc in self.defaultResolutionByPostProcessing:
            if resByPostProc.postProcessingLevel == postProcessingLevel:
                return resByPostProc

        LOG_ERROR((b'No flashlight resolution provided for post processing level {}').format(postProcessingLevel))
        return self.defaultResolutionByPostProcessing[_DEFAULT_RESOLUTION_INDEX]

    def _getResolutionIndexByName(self, name):
        for index, resolution in enumerate(self.resolutions):
            if resolution.name == name:
                return index

        LOG_ERROR((b'{} resolution does not exist').format(name))
        return _DEFAULT_RESOLUTION_INDEX

    def _reprArgs(self):
        return (b'colorSchemas={}, patterns={}, textureTilingFactor={}, alphaByDist={}, radiusByDist={}, appearanceDurationByDist={}, resolutions={}, defaultResolutionByPostProcessing={}, noiseIntensityMultiplier={}, maxSizePercentOfWindow={}, fadeoffFactorWhenNotAimed={}, borderSmoothness={}, aimingCircleAdjustment={}, smoothnessInAimingCircleAdjustment={}').format(self.colorSchemas, self.patterns, self.textureTilingFactor, self.alphaByDist, self.radiusByDist, self.appearanceDurationByDist, self.resolutions, self.defaultResolutionByPostProcessing, self.noiseIntensityMultiplier, self.maxSizePercentOfWindow, self.fadeoffFactorWhenNotAimed, self.borderSmoothness, self.aimingCircleAdjustment, self.smoothnessInAimingCircleAdjustment)


def _validateUniqueNames(items, itemType):
    names = set()
    for item in items:
        if item.name in names:
            raise ValidationError((b'{} name is not unique: {}.').format(itemType, item.name))
        names.add(item.name)

    return


def _validateColorSchemasNames(config):
    _validateUniqueNames(config.colorSchemas, b'Color Schema')
    return


def _validatePatternsNames(config):
    _validateUniqueNames(config.patterns, b'Pattern')
    return


def _validateResolutionNames(config):
    _validateUniqueNames(config.resolutions, b'Resolution')
    return


def _validateMaxResolutionNames(config):
    validNames = set(resolution.name for resolution in config.resolutions)
    for resolutionByPostProcessing in config.defaultResolutionByPostProcessing:
        name = resolutionByPostProcessing.maxResolutionName
        if name not in validNames:
            raise ValidationError((b'maxResolutionName {} is not present is resolutions list.').format(name))

    return


_configSchema = schemas.Schema(fields={b'colorSchemas': (fields.UniCapList(_colorSchemaSchema, deserializedValidators=validate.Length(minValue=1))), 
   b'patterns': (fields.UniCapList(_patternSchema, deserializedValidators=validate.Length(minValue=1))), 
   b'textureTilingFactor': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=0.01))), 
   b'alphaByDist': (fields.UniCapList(_distanceConfigSchema, deserializedValidators=validate.Length(minValue=1))), 
   b'radiusByDist': (fields.UniCapList(_distanceConfigSchema, deserializedValidators=validate.Length(minValue=1))), 
   b'appearanceDurationByDist': (fields.UniCapList(_distanceConfigSchema, deserializedValidators=validate.Length(minValue=1))), 
   b'resolutions': (fields.UniCapList(_resolutionSchema, deserializedValidators=validate.Length(minValue=1))), 
   b'defaultResolutionByPostProcessing': (fields.UniCapList(_defaultResolutionByPostProcessingSchema, deserializedValidators=validate.Length(minValue=5, maxValue=5))), 
   b'noiseIntensityMultiplier': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=0.01))), 
   b'maxSizePercentOfWindow': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=0.1, maxValue=100.0))), 
   b'fadeoffFactorWhenNotAimed': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=0.01))), 
   b'borderSmoothness': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=0.0, maxValue=1.0))), 
   b'aimingCircleAdjustment': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=0.01))), 
   b'smoothnessInAimingCircleAdjustment': (fields.Float(required=True, deserializedValidators=validate.Range(minValue=1.0)))}, modelClass=ConfigModel, deserializedValidators=[
 _validateColorSchemasNames, _validatePatternsNames, _validateResolutionNames, _validateMaxResolutionNames])

def getConfig():
    global _config
    if _config:
        return _config
    root = ResMgr.openSection(_CONFIG_PATH)
    rawData = section2dict.parse(root)
    _config = _configSchema.deserialize(rawData)
    return _config


def isFeatureEnabled():
    serverConfig = serverConfigSchema.getModel()
    if serverConfig is not None:
        return serverConfig.enabled
    else:
        return BattleReplay.isPlaying()
