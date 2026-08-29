from frameworks.wulf import ViewSettings
from gui.impl.auxiliary.resource_well_helper import fillVehicleCounter
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.resource_well.no_serial_vehicles_confirm_model import NoSerialVehiclesConfirmModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogView
from gui.resource_well.sounds import RESOURCE_WELL_SOUND_SPACE
from gui.sounds.filters import switchHangarFilteredFilter
from helpers import dependency
from skeletons.gui.game_control import IResourceWellController

class NoSerialVehiclesConfirm(FullScreenDialogView):
    __slots__ = (b'__additionalData',)
    _COMMON_SOUND_SPACE = RESOURCE_WELL_SOUND_SPACE
    __resourceWell = dependency.descriptor(IResourceWellController)

    def __init__(self):
        settings = ViewSettings(R.views.lobby.resource_well.NoSerialVehiclesConfirm())
        settings.model = NoSerialVehiclesConfirmModel()
        super(NoSerialVehiclesConfirm, self).__init__(settings)
        self.__additionalData = {}
        return

    @property
    def viewModel(self):
        return super(NoSerialVehiclesConfirm, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(NoSerialVehiclesConfirm, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            fillVehicleCounter(vehicleCounterModel=model.vehicleCounter, resourceWell=self.__resourceWell)
            vehicle = self._itemsCache.items.getItemByCD(self.__resourceWell.getRewardVehicle())
            model.setVehicleName(vehicle.userName)
        switchHangarFilteredFilter(on=True)
        return

    def _finalize(self):
        switchHangarFilteredFilter(on=False)
        super(NoSerialVehiclesConfirm, self)._finalize()
        return

    def _addListeners(self):
        self.viewModel.confirm += self._onAccept
        self.viewModel.cancel += self.__onCancelAction
        self.viewModel.close += self.__onCancelAction
        self.__resourceWell.onNumberRequesterUpdated += self.__onNumberRequesterUpdated
        self.__resourceWell.onEventUpdated += self.__onEventStateUpdated
        return

    def _removeListeners(self):
        self.viewModel.confirm -= self._onAccept
        self.viewModel.cancel -= self.__onCancelAction
        self.viewModel.close -= self.__onCancelAction
        self.__resourceWell.onNumberRequesterUpdated -= self.__onNumberRequesterUpdated
        self.__resourceWell.onEventUpdated -= self.__onEventStateUpdated
        return

    def _getAdditionalData(self):
        return self.__additionalData

    def _setBaseParams(self, model):
        return

    def __onNumberRequesterUpdated(self):
        with self.viewModel.transaction() as model:
            fillVehicleCounter(vehicleCounterModel=model.vehicleCounter, resourceWell=self.__resourceWell)
        return

    def __onEventStateUpdated(self):
        if not self.__resourceWell.isActive():
            self._onCancel()
        return

    def __onCancelAction(self):
        self.__additionalData[b'isUserCancelAction'] = True
        self._onCancel()
        return
