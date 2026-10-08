from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from account_helpers.AccountSettings import AccountSettings
from gui.Scaleform.daapi.view.meta.VehicleParametersMeta import VehicleParametersMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.impl import backport
from gui.shared.formatters import text_styles
from gui.shared.items_parameters import params_helper, formatters
from gui.shared.items_parameters.comparator import PARAM_STATE
from gui.shared.items_parameters.param_name_helper import getVehicleParameterText
from gui.shared.items_parameters.params_helper import VehParamsBaseGenerator, getParameters, getCommonParam, isValidEmptyValue, SimplifiedBarVO
from items import vehicles

class VehicleParameters(VehicleParametersMeta):

    def __init__(self):
        super(VehicleParameters, self).__init__()
        self._vehParamsDP = None
        self._alreadyShowed = False
        self._expandedGroups = {b'relativePower': (AccountSettings.getSettings(b'relativePower')), 
           b'relativeArmor': (AccountSettings.getSettings(b'relativeArmor')), 
           b'relativeMobility': (AccountSettings.getSettings(b'relativeMobility')), 
           b'relativeVisibility': (AccountSettings.getSettings(b'relativeVisibility')), 
           b'relativeCamouflage': (AccountSettings.getSettings(b'relativeCamouflage')), 
           b'relativeAbility': (AccountSettings.getSettings(b'relativeAbility'))}
        return

    def onParamClick(self, paramID):
        isOpened = not self._expandedGroups[paramID]
        AccountSettings.setSettings(paramID, isOpened)
        self._expandedGroups[paramID] = isOpened
        self._setDPUseAnimAndRebuild(False)
        return

    def onListScroll(self):
        self._setDPUseAnimAndRebuild(False)
        return

    def update(self, useAnim=True, *_):
        self._vehParamsDP.setGroupsToShow(self._expandedGroups)
        self._setDPUseAnimAndRebuild(useAnim)
        return

    def rebuildParams(self):
        if self._vehParamsDP is not None:
            self._vehParamsDP.rebuildList(self._getVehicleCache())
        return

    def _createDataProvider(self):
        return _VehParamsDataProvider(_VehParamsGenerator())

    def _populate(self):
        super(VehicleParameters, self)._populate()
        self._vehParamsDP = self._createDataProvider()
        self._vehParamsDP.setFlashObject(self.as_getDPS())
        return

    def _dispose(self):
        self._vehParamsDP.fini()
        self._vehParamsDP = None
        self._paramsProviderCls = None
        super(VehicleParameters, self)._dispose()
        return

    def _setDPUseAnimAndRebuild(self, useAnim):
        if self._vehParamsDP.useAnim != useAnim:
            self.as_setIsParamsAnimatedS(useAnim)
        self._vehParamsDP.setUseAnim(useAnim)
        cache = self._getVehicleCache()
        if not cache.item:
            return
        self.rebuildParams()
        return

    def _getVehicleCache(self):
        return g_currentVehicle


class VehiclePreviewParameters(VehicleParameters):

    def _createDataProvider(self):
        return VehPreviewParamsDataProvider()

    def _populate(self):
        super(VehiclePreviewParameters, self)._populate()
        self.update()
        g_currentPreviewVehicle.onComponentInstalled += self.update
        g_currentPreviewVehicle.onChanged += self.update
        g_currentPreviewVehicle.onPostProgressionChanged += self.update
        return

    def _dispose(self):
        g_currentPreviewVehicle.onComponentInstalled -= self.update
        g_currentPreviewVehicle.onChanged -= self.update
        g_currentPreviewVehicle.onPostProgressionChanged -= self.update
        super(VehiclePreviewParameters, self)._dispose()
        return

    def _getVehicleCache(self):
        return g_currentPreviewVehicle


class _VehParamsGenerator(VehParamsBaseGenerator):
    _AVERAGE_PARAMS = (b'avgDamage', b'avgPiercingPower')
    _AVERAGE_TOOLTIPS_MAP = {(TOOLTIPS_CONSTANTS.VEHICLE_ADVANCED_PARAMETERS): (TOOLTIPS_CONSTANTS.VEHICLE_AVG_PARAMETERS), 
       (TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_ADVANCED_PARAMETERS): (TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_AVG_PARAMETERS)}

    def __init__(self, tooltipType=TOOLTIPS_CONSTANTS.VEHICLE_ADVANCED_PARAMETERS):
        super(_VehParamsGenerator, self).__init__()
        self._tooltipType = tooltipType
        self.useAnim = False
        return

    def _getAdvancedFormatters(self):
        return formatters.NO_BONUS_BASE_SCHEME

    def _getExtraFormatters(self):
        return formatters.BASE_SCHEME

    def _getSimplifiedValue(self, param):
        return formatters.colorizedFormatParameter(param, formatters.NO_BONUS_SIMPLIFIED_SCHEME)

    def _makeSimpleParamBottomVO(self, param, vehIntCD):
        vehicle = self.itemsCache.items.getStockVehicle(vehIntCD)
        if param.name == b'relativeAbility':
            return self.__makeRelativeAbilityBottomVO(param, vehicle)
        stockParams = getParameters(vehicle)
        data = getCommonParam(HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_SIMPLE_BOTTOM, param.name, param.name)
        delta = 0
        state, diff = param.state
        if state == PARAM_STATE.WORSE:
            delta = -abs(diff)
        data.update({b'isEnabled': True, 
           b'tooltip': (self._tooltipType), 
           b'indicatorVO': (SimplifiedBarVO(value=param.value, delta=delta, markerValue=stockParams[param.name], useAnim=self.useAnim))})
        return data

    def _makeAdvancedParamVO(self, param, parentID, highlight):
        if param.value or isValidEmptyValue(param.name, param.value):
            data = super(_VehParamsGenerator, self)._makeAdvancedParamVO(param, parentID, highlight)
            data.update({b'titleText': (formatters.formatVehicleParamName(param.name, False)), 
               b'valueText': (formatters.colorizedFullFormatParameter(param, self._getAdvancedFormatters())), 
               b'iconSource': (formatters.getParameterSmallIconPath(param.name)), 
               b'isEnabled': False, 
               b'tooltip': (self.__getAdvancedParamTooltip(param))})
            return data
        else:
            return

    def _isExtraParamEnabled(self):
        return True

    def _makeExtraParamVO(self, param, parentID, highlight):
        if param.value:
            data, _ = super(_VehParamsGenerator, self)._makeExtraParamVO(param, parentID, highlight)
            isPositive = param.value >= 0
            title = backport.text(getVehicleParameterText(param.name, isTTC=True, isPositive=isPositive))
            data.update({b'titleText': (text_styles.leadingText(text_styles.main(title), 2)), 
               b'valueText': (formatters.colorizedFullFormatParameter(param, self._getExtraFormatters())), 
               b'isEnabled': False, 
               b'tooltip': (self.__getAdvancedParamTooltip(param, parentID)), 
               b'iconSource': (formatters.getParameterSmallIconPath(param.name))})
            return (
             data, title.count(b'\n'))
        else:
            return (None, 0)

    def _makeSimpleParamHeaderVO(self, param, isOpen, comparator):
        data = super(_VehParamsGenerator, self)._makeSimpleParamHeaderVO(param, isOpen, comparator)
        data.update({b'titleText': (formatters.formatVehicleParamName(param.name)), 
           b'valueText': (b' ' if param.name == b'relativeAbility' else self._getSimplifiedValue(param)), 
           b'isEnabled': True, 
           b'tooltip': (self._tooltipType), 
           b'isOpen': isOpen, 
           b'buffIconSrc': (formatters.getGroupPenaltyIcon(param, comparator))})
        return data

    def _makeSeparator(self, parentID):
        return {b'state': (HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_SEPARATOR), 
           b'isEnabled': False, 
           b'tooltip': b'', 
           b'parentID': parentID}

    def _makeExtraAdditionalBlock(self, paramID, parentID, tooltip):
        return {b'state': (HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_SEPARATOR), 
           b'isEnabled': False, 
           b'tooltip': tooltip, 
           b'paramID': paramID, 
           b'parentID': parentID}

    def _makeLineSeparator(self, parentID):
        return {b'state': (HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_LINE_SEPARATOR), 
           b'isEnabled': False, 
           b'tooltip': b'', 
           b'parentID': parentID}

    def __makeRelativeAbilityBottomVO(self, param, vehicle):
        data = getCommonParam(HANGAR_ALIASES.VEH_PARAM_RENDERER_STATE_ABILITY, param.name, param.name)
        abilityID = vehicle.typeDescr.ability
        if abilityID is None:
            abilityName = b''
        else:
            abilityName = vehicles.g_cache.getEquipmentByID(abilityID).userString
        data.update({b'isEnabled': True, 
           b'tooltip': (self._tooltipType), 
           b'iconSource': (RES_ICONS.MAPS_ICONS_VEHPARAMS_BG_ABILITY), 
           b'titleText': (text_styles.stats(abilityName))})
        return data

    def __getAdvancedParamTooltip(self, param, parentID=b''):
        if param.name in self._AVERAGE_PARAMS and self._tooltipType in self._AVERAGE_TOOLTIPS_MAP:
            return self._AVERAGE_TOOLTIPS_MAP[self._tooltipType]
        if parentID == b'relativeAbility':
            return TOOLTIPS_CONSTANTS.BASE_VEHICLE_PARAMETERS
        return self._tooltipType


class _PreviewVehParamsGenerator(_VehParamsGenerator):

    def __init__(self, tooltipType=None):
        super(_PreviewVehParamsGenerator, self).__init__(tooltipType or TOOLTIPS_CONSTANTS.VEHICLE_PREVIEW_ADVANCED_PARAMETERS)
        return

    def _getSimplifiedValue(self, param):
        return formatters.simplifiedDeltaParameter(param)

    def _getAdvancedFormatters(self):
        return formatters.BASE_SCHEME

    def _makeSimpleParamBottomVO(self, param, vehIntCD):
        vo = super(_PreviewVehParamsGenerator, self)._makeSimpleParamBottomVO(param, vehIntCD)
        if param.name == b'relativeAbility':
            return vo
        delta = param.state[1]
        value = param.value
        if delta > 0:
            value -= delta
        vo[b'indicatorVO'].update({b'value': value, b'delta': delta})
        return vo


class _ProgressionVehParamsGenerator(_PreviewVehParamsGenerator):

    def _getSimplifiedValue(self, param):
        return formatters.simplifiedDeltaParameter(param, isApproximately=True)


class _VehParamsDataProvider(SortableDAAPIDataProvider):

    def __init__(self, paramsGenerator):
        super(_VehParamsDataProvider, self).__init__()
        self._list = []
        self._useAnim = False
        self._cache = None
        self._expandedGroups = {}
        self._paramsGenerator = paramsGenerator
        return

    def setGroupsToShow(self, groups):
        self._expandedGroups = groups
        return

    @property
    def collection(self):
        return self._list

    def emptyItem(self):
        return

    def clear(self):
        self._list = []
        return

    def fini(self):
        self.clear()
        self.destroy()
        return

    def setUseAnim(self, useAnim):
        self._paramsGenerator.useAnim = useAnim
        return

    @property
    def useAnim(self):
        return self._paramsGenerator.useAnim

    def rebuildList(self, cache):
        self.buildList(cache)
        self.refresh()
        return

    def refreshItem(self, cache):
        self.buildList(cache)
        return False

    def refreshRandomItems(self, indexes, items):
        self.flashObject.invalidateItems(indexes, items)
        return

    def refreshSingleItem(self, index, item):
        self.flashObject.invalidateItem(index, item)
        return

    def buildList(self, cache):
        self.clear()
        self._cache = cache
        if self._cache.isPresent():
            self._buildSimplifiedList()
        return

    def _getComparator(self):
        return params_helper.idealCrewComparator(self._cache.item)

    def _getDiffComparator(self):
        return

    def _getSimplifiedValue(self, param):
        return formatters.colorizedFormatParameter(param, formatters.NO_BONUS_SIMPLIFIED_SCHEME)

    def _buildSimplifiedList(self):
        diffParams = self._paramsGenerator.processDiffParams(self._getDiffComparator(), self._expandedGroups)
        self._list = self._paramsGenerator.getFormattedParams(self._getComparator(), self._expandedGroups, self._cache.item.intCD, diffParams)
        return


class VehPreviewParamsDataProvider(_VehParamsDataProvider):

    def __init__(self, tooltipType=None):
        super(VehPreviewParamsDataProvider, self).__init__(_PreviewVehParamsGenerator(tooltipType))
        return

    def _getComparator(self):
        return params_helper.previewVehiclesComparator(self._cache.item, self._cache.defaultItem)


class VehPostProgressionDataProvider(_VehParamsDataProvider):

    def __init__(self, tooltipType=None):
        super(VehPostProgressionDataProvider, self).__init__(_ProgressionVehParamsGenerator(tooltipType))
        return

    def _getComparator(self):
        return params_helper.postProgressionVehiclesComparator(self._cache.item, self._cache.defaultItem)

    def _getDiffComparator(self):
        return params_helper.vehiclesComparator(self._cache.diffItem, self._cache.defaultItem)


class TankSetupParamsDataProvider(VehPreviewParamsDataProvider):

    def _getComparator(self):
        return params_helper.tankSetupVehiclesComparator(self._cache.item, self._cache.defaultItem)
