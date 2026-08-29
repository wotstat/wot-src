import logging, typing
from CurrentVehicle import g_currentPreviewVehicle
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.LobbySelectableView import LobbySelectableView
from gui.Scaleform.daapi.view.lobby.vehicle_preview.sound_constants import STYLE_PREVIEW_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.VehicleBasePreviewMeta import VehicleBasePreviewMeta
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS
from gui.hangar_cameras.hangar_camera_common import CameraRelatedEvents
from gui.impl import backport
from gui.impl.gen import R
from gui.prb_control.events_dispatcher import g_eventDispatcher
from gui.shared import EVENT_BUS_SCOPE, event_bus_handlers, event_dispatcher, events, g_eventBus
from gui.shared.formatters import text_styles
from gui.shared.gui_items.customization.c11n_items import getGroupFullNameResourceID
from helpers import dependency
from preview_selectable_logic import PreviewSelectableLogic
from skeletons.gui.game_control import IHeroTankController
from skeletons.gui.shared.utils import IHangarSpace
from uilogging.shop.loggers import ShopVehicleStylePreviewMetricsLogger, ShopVehicleStylePreviewFlowLogger
_SHOW_CLOSE_BTN = False
_SHOW_BACK_BTN = True
_logger = logging.getLogger(__name__)

class VehicleStylePreview(LobbySelectableView, VehicleBasePreviewMeta):
    __background_alpha__ = 0.0
    __metaclass__ = event_bus_handlers.EventBusListener
    __hangarSpace = dependency.descriptor(IHangarSpace)
    __heroTanksControl = dependency.descriptor(IHeroTankController)
    _COMMON_SOUND_SPACE = STYLE_PREVIEW_SOUND_SPACE

    def __init__(self, ctx=None):
        self._COMMON_SOUND_SPACE = ctx.get(b'soundSpace', self._COMMON_SOUND_SPACE)
        super(VehicleStylePreview, self).__init__(ctx)
        self.__ctx = ctx
        self._style = ctx[b'style']
        self.__backPreviewAlias = ctx.get(b'backPreviewAlias')
        self.__outfit = ctx.get(b'outfit')
        self.__vehicleCD = ctx[b'itemCD']
        self.__styleDescr = (ctx.get(b'styleDescr') or self._style.getDescription()) % {b'insertion_open': b'', 
           b'insertion_close': b''}
        self.__backCallback = ctx.get(b'backCallback', event_dispatcher.showHangar)
        self.__backBtnDescrLabel = ctx.get(b'backBtnDescrLabel', backport.text(R.strings.vehicle_preview.header.backBtn.descrLabel.personalAwards()))
        self.__topPanelData = ctx.get(b'topPanelData') or {}
        self.__selectedVehicleEntityId = None
        g_currentPreviewVehicle.selectHeroTank(ctx.get(b'isHeroTank', False))
        self.__uiMetricsLogger = ShopVehicleStylePreviewMetricsLogger(self._style.intCD)
        self.__uiFlowLogger = ShopVehicleStylePreviewFlowLogger()
        return

    def closeView(self):
        event_dispatcher.showHangar()
        return

    def onBackClick(self):
        if self.__backPreviewAlias and self.__backPreviewAlias == VIEW_ALIAS.LOBBY_STORE:
            self.__uiMetricsLogger.onViewClosed()
        self.__backCallback()
        return

    def setTopPanel(self):
        self.as_setTopPanelS(self.__topPanelData.get(b'linkage', b''))
        return

    def _populate(self):
        self.setTopPanel()
        super(VehicleStylePreview, self)._populate()
        g_currentPreviewVehicle.selectVehicle(self.__vehicleCD, style=self._style, outfit=self.__outfit)
        self.__selectedVehicleEntityId = g_currentPreviewVehicle.vehicleEntityID
        if not g_currentPreviewVehicle.isPresent() or self._style is None:
            event_dispatcher.showHangar()
        self.__hangarSpace.onSpaceCreate += self.__onHangarCreateOrRefresh
        self.addListener(CameraRelatedEvents.VEHICLE_LOADING, self.__onVehicleLoading, EVENT_BUS_SCOPE.DEFAULT)
        self.__heroTanksControl.setInteractive(False)
        self.as_setDataS(self._getData())
        self.as_setAdditionalInfoS(self._getAdditionalInfoVO())
        if self.__backPreviewAlias and self.__backPreviewAlias == VIEW_ALIAS.LOBBY_STORE:
            self.__uiFlowLogger.logOpenPreview()
            self.__uiMetricsLogger.onViewOpen()
        return

    def _dispose(self):
        self.__selectedVehicleEntityId = None
        self.removeListener(CameraRelatedEvents.VEHICLE_LOADING, self.__onVehicleLoading, EVENT_BUS_SCOPE.DEFAULT)
        g_clientUpdateManager.removeObjectCallbacks(self)
        self.__hangarSpace.onSpaceCreate -= self.__onHangarCreateOrRefresh
        self.__heroTanksControl.setInteractive(True)
        g_currentPreviewVehicle.selectNoVehicle()
        g_currentPreviewVehicle.resetAppearance()
        g_eventBus.handleEvent(events.LobbySimpleEvent(events.LobbySimpleEvent.VEHICLE_PREVIEW_HIDDEN), scope=EVENT_BUS_SCOPE.LOBBY)
        super(VehicleStylePreview, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        if alias == VEHPREVIEW_CONSTANTS.TOP_PANEL_TABS_PY_ALIAS:
            viewPy.setData(**self.__topPanelData)
            viewPy.setParentCtx(**self.__ctx)
        return

    def _createSelectableLogic(self):
        return PreviewSelectableLogic()

    def _getData(self):
        return {b'closeBtnLabel': (backport.text(R.strings.vehicle_preview.header.closeBtn.label())), 
           b'backBtnLabel': (backport.text(R.strings.vehicle_preview.header.backBtn.label())), 
           b'backBtnDescrLabel': (self.__backBtnDescrLabel), 
           b'showCloseBtn': _SHOW_CLOSE_BTN, 
           b'showBackButton': _SHOW_BACK_BTN}

    def _getAdditionalInfoVO(self):
        return {b'objectSubtitle': (text_styles.main(backport.text(getGroupFullNameResourceID(self._style.groupID)))), 
           b'objectTitle': (self._style.userName), 
           b'descriptionTitle': (backport.text(R.strings.tooltips.vehiclePreview.historicalReference.title())), 
           b'descriptionText': (self.__styleDescr)}

    def __onVehicleLoading(self, ctxEvent):
        isVehicleLoadingStarted = ctxEvent.ctx[b'started']
        if isVehicleLoadingStarted:
            _logger.debug(b'Too early VEHICLE_LOADING handler call.')
            return
        else:
            if ctxEvent.ctx[b'intCD'] != self.__vehicleCD:
                _logger.warning(b'VEHICLE_LOADING handler: incompatible "intCD" parameter.')
                return
            if ctxEvent.ctx[b'vEntityId'] != self.__selectedVehicleEntityId:
                _logger.warning(b'VEHICLE_LOADING handler: incompatible "vEntityId" parameter.')
                return
            self.removeListener(CameraRelatedEvents.VEHICLE_LOADING, self.__onVehicleLoading, EVENT_BUS_SCOPE.DEFAULT)
            self.__selectedVehicleEntityId = None
            return

    def __onHangarCreateOrRefresh(self):
        self.__handleWindowClose()
        g_eventDispatcher.loadHangar()
        return

    @event_bus_handlers.eventBusHandler(events.HideWindowEvent.HIDE_VEHICLE_PREVIEW, EVENT_BUS_SCOPE.LOBBY)
    def __handleWindowClose(self, event=None):
        if event is not None:
            if event.ctx.get(b'back', True):
                self.onBackClick()
            elif event.ctx.get(b'close', False):
                self.closeView()
        self.destroy()
        return
