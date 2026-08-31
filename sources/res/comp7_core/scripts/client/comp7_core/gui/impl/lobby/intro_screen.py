from __future__ import absolute_import
import logging, typing
from comp7_core.gui.impl.lobby.comp7_core_helpers import comp7_core_model_helpers
from frameworks.wulf import ViewSettings, ViewFlags
from gui.impl.backport import BackportTooltipWindow
from gui.impl.backport.backport_tooltip import createTooltipData
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.prb_control.entities.listener import IGlobalListener
from gui.shared import event_dispatcher
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore
_logger = logging.getLogger(__name__)

class IntroScreen(ViewImpl, IGlobalListener):
    __slots__ = ()
    __settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self, layoutID):
        settings = ViewSettings(layoutID)
        settings.flags = ViewFlags.LOBBY_SUB_VIEW
        settings.model = self._modelClazz()
        super(IntroScreen, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(IntroScreen, self).getViewModel()

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
        return super(IntroScreen, self).createToolTip(event)

    def onPrbEntitySwitched(self):
        if not self._modeController.isModePrbActive():
            self.destroyWindow()
        return

    def _finalize(self):
        self.__removeListeners()
        return

    def _onLoading(self, *_, **__):
        self.__addListeners()
        self._updateData()
        return

    def _updateData(self):
        with self.viewModel.transaction() as vm:
            comp7_core_model_helpers.setScheduleInfo(vm.scheduleInfo, self._modeController, self._calendarDayTooltipID, self._seasonStateClazz, self._yearStateClazz, self._seasonNameClazz)
            levelsArr = vm.getVehicleLevels()
            levelsArr.clear()
            modeSettings = self._modeController.getModeSettings()
            if not modeSettings:
                return
            for level in modeSettings.levels:
                levelsArr.addNumber(level)

            levelsArr.invalidate()
        return

    def __addListeners(self):
        self.viewModel.onClose += self.__onClose
        self.viewModel.scheduleInfo.season.pollServerTime += self.__onPollServerTime
        self._modeController.onStatusUpdated += self.__onStatusUpdated
        self.startGlobalListening()
        return

    def __removeListeners(self):
        self.viewModel.onClose -= self.__onClose
        self.viewModel.scheduleInfo.season.pollServerTime -= self.__onPollServerTime
        self._modeController.onStatusUpdated -= self.__onStatusUpdated
        self.stopGlobalListening()
        return

    def __onStatusUpdated(self, status):
        if comp7_core_model_helpers.isModeForcedDisabled(status, self._modeController):
            self.destroyWindow()
        else:
            self._updateData()
        return

    def __onClose(self):
        event_dispatcher.showHangar()
        self.destroyWindow()
        return

    def __onPollServerTime(self):
        self._updateData()
        return
