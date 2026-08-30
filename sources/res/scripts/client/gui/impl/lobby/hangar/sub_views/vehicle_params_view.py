from CurrentVehicle import g_currentVehicle, g_currentPreviewVehicle
from account_helpers import AccountSettings
from frameworks.wulf import ViewFlags, ViewSettings, ViewModel
from gui import GUI_SETTINGS
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_base_view_model import HighlightType
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_group_view_model import VehicleParamGroupViewModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_view_model import VehicleParamViewModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_params_view_model import VehicleParamsViewModel
from gui.impl.lobby.hangar.sub_views.veh_param_helpers import getGroupIcon, formatParameterValue, formatAdditionalParameter, getMaxValue
from gui.impl.pub import ViewImpl
from gui.shared.gui_items import KPI, VEHICLE_ATTR_TO_KPI_NAME_MAP
from gui.shared.items_cache import CACHE_SYNC_REASON
from gui.shared.items_parameters import params_helper, RELATIVE_PARAMS_WITHOUT_ABILITY
from gui.shared.items_parameters.comparator import PARAM_STATE
from gui.shared.items_parameters.param_name_helper import getVehicleParameterText
from gui.shared.items_parameters.params import HIDDEN_PARAM_DEFAULTS
from gui.shared.tooltips.contexts import HangarParamContext
from helpers import dependency
from skeletons.gui.app_loader import IAppLoader
from skeletons.gui.game_control import IIGRController
from skeletons.gui.shared import IItemsCache

class VehicleParamsView(ViewImpl):
    __slots__ = (b'__vehIntCD', b'__expandedGroups', b'__params', b'__extraParams', b'__groups', b'__context', b'__comparator', b'__stockParams')
    _DEFAULT_MIN_VALUE = 0
    _N_DIGITS = 2
    _igrController = dependency.descriptor(IIGRController)
    _itemsCache = dependency.descriptor(IItemsCache)
    _appLoader = dependency.descriptor(IAppLoader)

    def __init__(self, vehIntCD=None, flags=ViewFlags.LOBBY_TOP_SUB_VIEW, layoutID=R.views.lobby.hangar.subViews.VehicleParams()):
        settings = ViewSettings(layoutID)
        settings.flags = flags
        settings.model = VehicleParamsViewModel()
        self.__vehIntCD = vehIntCD
        self.__context = HangarParamContext()
        self.__params = []
        self.__extraParams = []
        self.__expandedGroups = None
        self.__comparator = None
        self.__stockParams = None
        super(VehicleParamsView, self).__init__(settings)
        return

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument(b'tooltipId', None)
            if tooltipId == self._getTooltipID():
                paramId = event.getArgument(b'paramId', None)
                toolTipMgr = self._appLoader.getApp().getToolTipMgr()
                if toolTipMgr is not None:
                    toolTipMgr.onCreateWulfTooltip(tooltipId, (
                     paramId, self.__context, True), event.mouse.positionX, event.mouse.positionY)
                    return tooltipId
        return super(VehicleParamsView, self).createToolTip(event)

    @property
    def comparator(self):
        if self.__comparator is None:
            self.__comparator = self._getComparator()
        return self.__comparator

    @property
    def viewModel(self):
        return super(VehicleParamsView, self).getViewModel()

    @property
    def groups(self):
        return self.__groups

    @property
    def params(self):
        return self.__params

    @property
    def extraParams(self):
        return self.__extraParams

    @property
    def expandedGroups(self):
        if self.__expandedGroups is not None:
            return self.__expandedGroups
        else:
            return {b'relativePower': (AccountSettings.getSettings(b'relativePower')), 
               b'relativeArmor': (AccountSettings.getSettings(b'relativeArmor')), 
               b'relativeMobility': (AccountSettings.getSettings(b'relativeMobility')), 
               b'relativeVisibility': (AccountSettings.getSettings(b'relativeVisibility')), 
               b'relativeCamouflage': (AccountSettings.getSettings(b'relativeCamouflage'))}

    def setExpandedGroups(self, value):
        self.__expandedGroups = value
        return

    def update(self):
        if not GUI_SETTINGS.technicalInfo:
            return
        self._clearData()
        self._prepareData()
        self.__fillViewModel()
        return

    def setContext(self, context):
        self.__context = context
        return

    def _getComparator(self):
        return params_helper.idealCrewComparator(self._getVehicle())

    def _getVehicle(self):
        if self.__vehIntCD is not None:
            return self._itemsCache.items.getItemByCD(self.__vehIntCD)
        else:
            return g_currentVehicle.item

    def _onLoading(self, *args, **kwargs):
        super(VehicleParamsView, self)._onLoading()
        self.update()
        return

    def _getEvents(self):
        return (
         (
          self._igrController.onIgrTypeChanged, self._onIgrTypeChanged),
         (
          g_currentVehicle.onChanged, self._onCurrentVehicleChanged),
         (
          self._itemsCache.onSyncCompleted, self._onCacheResync),
         (
          self.viewModel.onGroupClick, self.__onGroupClick))

    def _onIgrTypeChanged(self):
        self.__fillViewModel()
        return

    def _onCurrentVehicleChanged(self):
        self.update()
        return

    def _onCacheResync(self, reason, _):
        if reason == CACHE_SYNC_REASON.SHOP_RESYNC:
            self.__fillViewModel()
            return
        return

    @property
    def _stockParams(self):
        if self.__stockParams is None:
            self.__stockParams = params_helper.getParameters(self._itemsCache.items.getStockVehicle(self._getVehicle().intCD))
        return self.__stockParams

    def _clearData(self):
        self.__groups = []
        self.__params = []
        self.__extraParams = []
        self.__comparator = None
        return

    def _getTooltipID(self):
        return TOOLTIPS_CONSTANTS.VEHICLE_ADVANCED_PARAMETERS

    def _getGroupHighlight(self, _):
        return HighlightType.NONE

    def _getGroupEnabled(self, _):
        return True

    def _getUseAnim(self):
        return True

    def _getParamEnabled(self, *_):
        return True

    def _getRoundNDigits(self):
        return self._N_DIGITS

    def _getAdvancedParamTooltip(self, _):
        return TOOLTIPS_CONSTANTS.VEHICLE_ADVANCED_PARAMETERS

    def _isExtraParamEnabled(self):
        return False

    def _isAdditionalValueEnabled(self):
        return False

    def _isAdditionalValueApproximately(self):
        return False

    def _getLocalizedName(self, param):
        if KPI.Name.hasValue(param.name):
            isPositive = param.value >= 0
            paramName = VEHICLE_ATTR_TO_KPI_NAME_MAP.get(param.name, param.name)
            name = getVehicleParameterText(paramName, isPositive=isPositive, isTTC=True)
        else:
            name = R.strings.menu.tank_params.dyn(param.name)()
        return backport.text(name)

    def _createGroupViewModel(self, groupName, comparator):
        param = comparator.getExtendedData(groupName)
        additionalValue = formatAdditionalParameter(param, isApproximately=self._isAdditionalValueApproximately())
        return {b'Id': groupName, 
           b'IsEnabled': (self._getGroupEnabled(groupName)), 
           b'Value': (formatParameterValue(param.name, param.value, param.state, allowSmartRound=False, isColorize=False, nDigits=self._getRoundNDigits())), 
           b'HighlightType': (self._getGroupHighlight(groupName)), 
           b'TooltipID': (self._getTooltipID()), 
           b'BuffIconType': (getGroupIcon(param, self.comparator)), 
           b'IsOpen': (self.__getIsOpened(groupName=groupName)), 
           b'AdditionalValue': (additionalValue if self._isAdditionalValueEnabled() else b''), 
           b'Indicator': (self._createIndicator(param))}

    def _createIndicator(self, param):
        state, delta = param.state
        if state == PARAM_STATE.WORSE:
            delta = -abs(delta)
        return {b'Value': (param.value), 
           b'Delta': delta, 
           b'MarkerValue': (self._stockParams[param.name]), 
           b'MaxValue': (getMaxValue(param.value, delta)), 
           b'MinValue': (self._DEFAULT_MIN_VALUE), 
           b'IsUseAnim': (self._getUseAnim())}

    def _createParam(self, param, groupName, highlight=HighlightType.NONE):
        if param.value is None:
            return
        else:
            return {b'Id': (param.name), 
               b'ParentID': groupName, 
               b'HighlightType': highlight, 
               b'IsEnabled': (self._getParamEnabled(param, groupName)), 
               b'Value': (formatParameterValue(param.name, param.value, param.state, allowSmartRound=False, nDigits=self._getRoundNDigits())), 
               b'TooltipID': (self._getAdvancedParamTooltip(param)), 
               b'LocalizedName': (self._getLocalizedName(param))}

    def _prepareData(self, diffParams=None, concreteGroup=None):
        diffParams = diffParams if diffParams is not None else {}
        for groupName in RELATIVE_PARAMS_WITHOUT_ABILITY:
            if concreteGroup is not None and concreteGroup != groupName:
                continue
            group = self._createGroupViewModel(groupName=groupName, comparator=self.comparator)
            self.__groups.append(group)
            if not self.__getIsOpened(groupName):
                continue
            for paramName in params_helper.PARAMS_GROUPS[groupName]:
                self.__addParam(paramName, groupName, diffParams, self.__params)

            if self._isExtraParamEnabled():
                for paramName in params_helper.EXTRA_PARAMS_GROUP[groupName]:
                    self.__addParam(paramName, groupName, diffParams, self.__extraParams, skipMissing=True)

        return

    def __addParam(self, paramName, groupName, diffParams, paramsContainer, skipMissing=False):
        param = self.comparator.getExtendedData(paramName)
        if skipMissing and (not param.value or paramName in HIDDEN_PARAM_DEFAULTS and param.value == HIDDEN_PARAM_DEFAULTS[paramName]):
            return
        highlight = diffParams.get(paramName, HighlightType.NONE)
        paramModel = self._createParam(param, groupName, highlight)
        if paramModel:
            paramsContainer.append(paramModel)
        return

    def __getIsOpened(self, groupName):
        return self.expandedGroups is None or self.expandedGroups.get(groupName, False)

    def __fillViewModel(self):
        with self.viewModel.transaction() as model:
            groups = model.getGroups()
            groups.clear()
            for group in self.__groups:
                groupID = group.get(b'Id', b'')
                groupModel = self.__convertGroupToModel(group)
                params = groupModel.getParams()
                params.clear()
                extraParams = groupModel.getExtraParams()
                extraParams.clear()
                for param in self.__params:
                    paramID = param.get(b'ParentID', b'')
                    if paramID == groupID:
                        params.addViewModel(self.__fillModel(VehicleParamViewModel(), param))

                for extraParam in self.__extraParams:
                    paramID = extraParam.get(b'ParentID', b'')
                    if paramID == groupID:
                        extraParams.addViewModel(self.__fillModel(VehicleParamViewModel(), extraParam))

                groups.addViewModel(groupModel)

            groups.invalidate()
        return

    def __fillModel(self, model, params):
        for k, v in params.iteritems():
            modelSetter = b'set' + k
            if hasattr(model, modelSetter):
                getattr(model, modelSetter)(v)

        return model

    def __convertGroupToModel(self, item):
        groupModel = self.__fillModel(VehicleParamGroupViewModel(), item)
        indicator = item.get(b'Indicator', None)
        if indicator is not None:
            self.__fillModel(groupModel.indicator, indicator)
        return groupModel

    def __onGroupClick(self, args=None):
        if not args:
            return
        else:
            groupName = args.get(b'groupName', None)
            if groupName:
                for group in self.viewModel.getGroups():
                    if groupName == group.getId():
                        isOpened = not group.getIsOpen()
                        group.setIsOpen(isOpened)
                        AccountSettings.setSettings(groupName, isOpened)

            self.viewModel.getGroups().invalidate()
            self.update()
            return


class VehiclePreviewParamsView(VehicleParamsView):

    def _getComparator(self):
        return params_helper.previewVehiclesComparator(self._getVehicle(), self._getVehicle())

    def _getVehicle(self):
        return g_currentPreviewVehicle.item


class VehicleSkillPreviewParamsView(VehicleParamsView):

    def __init__(self, *args, **kwargs):
        super(VehicleSkillPreviewParamsView, self).__init__(*args, **kwargs)
        self.__skillName = kwargs.get(b'skillName', b'')
        return

    def update(self):
        if not self._getVehicle():
            return
        super(VehicleSkillPreviewParamsView, self).update()
        return

    def updateForSkill(self, skillName):
        self.__skillName = skillName
        self.update()
        return

    def _getComparator(self):
        return params_helper.skillOnIdealCrewComparator(self._getVehicle(), self.__skillName)

    def _isExtraParamEnabled(self):
        return True

    def _isAdditionalValueEnabled(self):
        return True


class VehicleParamsComponent(InjectComponentAdaptor):

    def _makeInjectView(self):
        self.__view = VehicleParamsComponentView(context=HangarParamContext())
        return self.__view


class VehicleParamsComponentView(ViewImpl):

    def __init__(self, context):
        settings = ViewSettings(R.views.lobby.hangar.VehicleParamsWidget())
        settings.flags = ViewFlags.VIEW
        settings.model = ViewModel()
        super(VehicleParamsComponentView, self).__init__(settings)
        view = VehicleParamsView()
        view.setContext(context)
        self.setChildView(resourceID=R.views.lobby.hangar.subViews.VehicleParams(), view=view)
        return

    @property
    def viewModel(self):
        return super(VehicleParamsComponentView, self).getViewModel()
