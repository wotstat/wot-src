from __future__ import absolute_import
import typing
from typing import Optional, List, Type, Union
from extension_utils import ResMgr
import section2dict
from dict2model import models, fields, schemas, validate, exceptions
from debug_utils import LOG_ERROR
if typing.TYPE_CHECKING:
    from items.vehicles import VehicleDescriptor
FILTERS_PATH = b'scripts/item_defs/vehicle_filters.xml'

class BaseModel(models.Model):

    def isVehicleMatch(self, descr):
        raise NotImplementedError()
        return


class BaseIncludeExcludeModel(BaseModel):
    __slots__ = (b'include', b'exclude')

    def __init__(self, include=None, exclude=None):
        super(BaseIncludeExcludeModel, self).__init__()
        self.include = include
        self.exclude = exclude
        return


class BaseValueInIncludeExcludeModel(BaseIncludeExcludeModel):

    def _isValueIn(self, value):
        if self.include and value not in self.include:
            return False
        if self.exclude and value in self.exclude:
            return False
        return True


class BaseValuesInIncludeExcludeModel(BaseIncludeExcludeModel):

    def _isValuesIn(self, values):
        if self.include and not set(self.include).issubset(values):
            return False
        if self.exclude and not set(self.exclude).isdisjoint(values):
            return False
        return True


class BaseBooleanModel(BaseModel):
    __slots__ = (b'value',)

    def __init__(self, value=None):
        super(BaseBooleanModel, self).__init__()
        self.value = value
        return

    def _isValue(self, value):
        return value is self.value


class VehNamesModel(BaseValueInIncludeExcludeModel):

    def isVehicleMatch(self, descr):
        return self._isValueIn(descr.type.name)


class VehClassesModel(BaseValueInIncludeExcludeModel):

    def isVehicleMatch(self, descr):
        return self._isValueIn(descr.type.getVehicleClass())


class LevelModel(BaseValueInIncludeExcludeModel):

    def isVehicleMatch(self, descr):
        return self._isValueIn(str(descr.type.level))


class TagsModel(BaseValuesInIncludeExcludeModel):

    def isVehicleMatch(self, descr):
        return self._isValuesIn(descr.type.tags)


class GunTagsModel(BaseValuesInIncludeExcludeModel):

    def isVehicleMatch(self, descr):
        return self._isValuesIn(descr.gun.tags)


class BurstModel(BaseBooleanModel):

    def isVehicleMatch(self, descr):
        return self._isValue(descr.hasBurst)


class FilterValuesModel(models.Model):
    __slots__ = (b'vehNames', b'vehClasses', b'level', b'tags', b'gunTags', b'burst')

    def __init__(self, vehNames=None, vehClasses=None, level=None, tags=None, gunTags=None, burst=None):
        super(FilterValuesModel, self).__init__()
        self.vehNames = vehNames
        self.vehClasses = vehClasses
        self.level = level
        self.tags = tags
        self.gunTags = gunTags
        self.burst = burst
        return

    def isVehicleMatch(self, vehDesc):
        for attrName in self.__slots__:
            valueModel = getattr(self, attrName)
            if valueModel is None:
                continue
            if not valueModel.isVehicleMatch(vehDesc):
                return False

        return True


class FilterModel(models.Model):
    __slots__ = (b'name', b'values')

    def __init__(self, name, values):
        super(FilterModel, self).__init__()
        self.name = name
        self.values = values
        return

    def isVehicleMatch(self, vehDesc):
        return self.values.isVehicleMatch(vehDesc)


class VehicleFiltersModel(models.Model):
    __slots__ = (b'filters', b'_filterByNames')

    def __init__(self, filters):
        super(VehicleFiltersModel, self).__init__()
        self.filters = filters
        self._filterByNames = {f.name: f for f in self.filters}
        return

    def getFilterNames(self):
        return list(self._filterByNames)

    def getFilter(self, filterName):
        return self._filterByNames.get(filterName)

    def isVehicleMatchByFilter(self, filterName, vehDesc):
        vehFilter = self.getFilter(filterName)
        if vehFilter is None:
            LOG_ERROR((b'No vehicle filter "{}" found.').format(filterName))
            return False
        else:
            res = vehFilter.isVehicleMatch(vehDesc)
            return res


class BooleanSchema(schemas.Schema):

    def __init__(self, modelClass):
        super(BooleanSchema, self).__init__(fields={b'value': (fields.Boolean(required=True))}, modelClass=modelClass)
        return


class IncludeExcludeSchema(schemas.Schema):

    def __init__(self, modelClass):
        super(IncludeExcludeSchema, self).__init__(fields={b'include': (fields.ListFromString(required=False, field=fields.String(deserializedValidators=validate.Length(minValue=1)), default=list)), 
           b'exclude': (fields.ListFromString(required=False, field=fields.String(deserializedValidators=validate.Length(minValue=1)), default=list))}, modelClass=modelClass, deserializedValidators=checkIncludeExcludeValue)
        return


def checkIncludeExcludeValue(model):
    if not (model.include and model.exclude):
        return
    if not set(model.include).isdisjoint(model.exclude):
        raise exceptions.ValidationError(b'Include and exclude filters must not overlap.')
    return


filterValuesSchema = schemas.Schema(fields={b'vehNames': (fields.Nested(required=False, schema=IncludeExcludeSchema(modelClass=VehNamesModel))), 
   b'vehClasses': (fields.Nested(required=False, schema=IncludeExcludeSchema(modelClass=VehClassesModel))), 
   b'level': (fields.Nested(required=False, schema=IncludeExcludeSchema(modelClass=LevelModel))), 
   b'tags': (fields.Nested(required=False, schema=IncludeExcludeSchema(modelClass=TagsModel))), 
   b'gunTags': (fields.Nested(required=False, schema=IncludeExcludeSchema(modelClass=GunTagsModel))), 
   b'burst': (fields.Nested(required=False, schema=BooleanSchema(modelClass=BurstModel)))}, modelClass=FilterValuesModel)
filterSchema = schemas.Schema(fields={b'name': (fields.String(required=True, deserializedValidators=validate.Length(minValue=1))), 
   b'values': (fields.Nested(required=True, schema=filterValuesSchema))}, modelClass=FilterModel)
vehicleFiltersSchema = schemas.Schema(fields={b'filters': (fields.UniCapList(required=False, fieldOrSchema=filterSchema, default=list))}, modelClass=VehicleFiltersModel)
_g_filters = None

def init():
    global _g_filters
    root = ResMgr.openSection(FILTERS_PATH)
    rawData = section2dict.parse(root)
    _g_filters = vehicleFiltersSchema.deserialize(rawData)
    return


def getVehicleFilters():
    if _g_filters is None:
        init()
    return _g_filters
