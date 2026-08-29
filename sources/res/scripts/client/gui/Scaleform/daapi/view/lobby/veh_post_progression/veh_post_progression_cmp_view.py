from gui.Scaleform.daapi.view.meta.VehiclePostProgressionCmpViewMeta import VehiclePostProgressionCmpViewMeta
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.veh_post_progression.vo_builders.cmp_page_vos import getTitleVO, getDataVO
from helpers import dependency
from skeletons.gui.game_control import IVehicleComparisonBasket

class VehiclePostProgressionCmpView(VehiclePostProgressionCmpViewMeta):
    _PROGRESSION_INJECT_ALIAS = HANGAR_ALIASES.POST_PROGRESSION_CMP_INJECT
    __cmpBasket = dependency.descriptor(IVehicleComparisonBasket)

    def onCloseClick(self):
        self._onExit()
        return

    def _addListeners(self):
        super(VehiclePostProgressionCmpView, self)._addListeners()
        self.__cmpBasket.onParametersChange += self.__onBasketParamsChanged
        progressionInjectView = self._progressionInject.getInjectView()
        progressionInjectView.onExitAction += self.__onExitAction
        return

    def _removeListeners(self):
        self.__cmpBasket.onParametersChange -= self.__onBasketParamsChanged
        progressionInjectView = self._progressionInject.getInjectView()
        progressionInjectView.onExitAction -= self.__onExitAction
        super(VehiclePostProgressionCmpView, self)._removeListeners()
        return

    def _onExit(self):
        self.destroy()
        return

    def _onSyncCompleted(self, reason, diff):
        changedVehicles = diff.get(GUI_ITEM_TYPE.VEHICLE, {})
        if self._vehicle.intCD in changedVehicles:
            self._checkPostProgressionExists()
        return

    def _getDiffVehicle(self):
        return cmp_helpers.getCmpConfiguratorMainView().getInitialVehicleData()[0]

    def _getModVehicle(self):
        return cmp_helpers.getCmpConfiguratorMainView().getCurrentVehicleCopy()

    def _getVehicle(self):
        return cmp_helpers.getCmpConfiguratorMainView().getInitialVehicleData()[0]

    def _checkNationChange(self):
        return

    def _updateData(self, *_):
        self.as_setDataS(getDataVO(self._vehicle))
        return

    def _updateTitle(self):
        self.as_setVehicleTitleS(getTitleVO(self._vehicle))
        return

    def __onExitAction(self):
        self.as_onEscPressedS()
        return

    def __onBasketParamsChanged(self, *_):
        self._updateVehicle()
        self._progressionInject.getInjectView().invalidateVehicle()
        self._parametersView.update(useAnim=False)
        return
