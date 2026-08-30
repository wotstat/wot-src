from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers
from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.backport import BackportTooltipWindow, createTooltipData
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared.event_dispatcher import showHangar

class NoVehiclesScreen(ViewImpl, IGlobalListener):
    __slots__ = ()

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = self._modelClazz()
        super(NoVehiclesScreen, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(NoVehiclesScreen, self).getViewModel()

    @property
    def _modeController(self):
        raise NotImplementedError
        return

    @property
    def _modelClazz(self):
        raise NotImplementedError
        return

    @property
    def _seasonStateClazz(self):
        raise NotImplementedError
        return

    @property
    def _yearStateClazz(self):
        raise NotImplementedError
        return

    @property
    def _errorReasonClazz(self):
        raise NotImplementedError
        return

    @property
    def _seasonNameClazz(self):
        raise NotImplementedError
        return

    @property
    def _calendarDayTooltipID(self):
        raise NotImplementedError
        return

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument(b'tooltipId')
            tooltipData = None
            if tooltipId == self._calendarDayTooltipID:
                tooltipData = createTooltipData(isSpecial=True, specialAlias=tooltipId, specialArgs=(None,))
            if tooltipData is not None:
                window = BackportTooltipWindow(tooltipData, self.getParentWindow())
                window.load()
                return window
        return super(NoVehiclesScreen, self).createToolTip(event)

    def onPrbEntitySwitched(self):
        if not self._modeController.isModePrbActive():
            self.destroyWindow()
        return

    def _finalize(self):
        self.__removeListeners()
        super(NoVehiclesScreen, self)._finalize()
        return

    def _onLoading(self, *args, **kwargs):
        super(NoVehiclesScreen, self)._onLoading(*args, **kwargs)
        self.__updateData()
        self.__addListeners()
        return

    def __addListeners(self):
        self.viewModel.scheduleInfo.season.pollServerTime += self.__onPollServerTime
        self.startGlobalListening()
        return

    def __removeListeners(self):
        self.viewModel.scheduleInfo.season.pollServerTime -= self.__onPollServerTime
        self.stopGlobalListening()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self._modeController.onModeConfigChanged, self.__onModeConfigChanged),
         (
          self._modeController.onStatusUpdated, self.__onStatusUpdated))

    def __onClose(self):
        showHangar()
        return

    def __onModeConfigChanged(self):
        self.__updateData()
        return

    def __onStatusUpdated(self, status):
        if comp7_core_model_helpers.isModeForcedDisabled(status, self._modeController):
            showHangar()
        else:
            self.__onPollServerTime()
        return

    def __updateData(self):
        with self.viewModel.transaction() as model:
            self.__onPollServerTime()
            levelsArr = model.getVehicleLevels()
            levelsArr.clear()
            for level in self._modeController.getModeSettings().levels:
                levelsArr.addNumber(level)

            levelsArr.invalidate()
            if self._modeController.vehicleIsAvailableForRestore():
                errorReason = self._errorReasonClazz.CAN_RECOVER_VEHICLES
            elif self._modeController.vehicleIsAvailableForBuy():
                errorReason = self._errorReasonClazz.NOT_BOUGHT_VEHICLES
            else:
                errorReason = self._errorReasonClazz.DEFAULT
            model.setErrorReason(errorReason)
        return

    def __onPollServerTime(self):
        with self.viewModel.transaction() as vm:
            comp7_core_model_helpers.setScheduleInfo(vm.scheduleInfo, self._modeController, self._calendarDayTooltipID, self._seasonStateClazz, self._yearStateClazz, self._seasonNameClazz)
        return
