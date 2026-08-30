import typing
from Event import Event
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_base_view_model import ProgressionState
from gui.impl.gen.view_models.views.lobby.post_progression.post_progression_cmp_view_model import PostProgressionCmpViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.step_model import StepState
from gui.impl.lobby.veh_post_progression.post_progression_base_component import PostProgressionBaseComponentView
from gui.impl.lobby.veh_post_progression.tooltips.pair_modification_tooltip_view import CmpPairModificationTooltipView
from gui.impl.lobby.veh_post_progression.tooltips.level_tooltip_view import CmpProgressionLevelTooltipView
from gui.veh_post_progression.models.progression import PostProgressionAvailability, PostProgressionCompletion
from gui.veh_post_progression.models.progression_step import PostProgressionStepState
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.common.bonuses_model import BonusesModel
    from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel
    from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel
    from gui.veh_post_progression.models.progression import PostProgressionItem
    from gui.veh_post_progression.models.progression_step import PostProgressionStepItem
_SINGLE_STEP_STATE_MAP = {(PostProgressionStepState.RESTRICTED): (StepState.RESTRICTED), (PostProgressionStepState.LOCKED): (StepState.AVAILABLEPURCHASE), 
   (PostProgressionStepState.RECEIVED): (StepState.AVAILABLEPURCHASE), 
   (PostProgressionStepState.UNLOCKED): (StepState.AVAILABLEPURCHASE)}
_MULTI_STEP_STATE_MAP = {(PostProgressionStepState.RESTRICTED): (StepState.RESTRICTED), 
   (PostProgressionStepState.LOCKED): (StepState.RECEIVED), 
   (PostProgressionStepState.RECEIVED): (StepState.RECEIVED), 
   (PostProgressionStepState.UNLOCKED): (StepState.RECEIVED)}

class PostProgressionCmpComponentView(PostProgressionBaseComponentView):
    __slots__ = (b'onExitAction',)

    def __init__(self, layoutID=R.views.lobby.veh_post_progression.VehiclePostProgressionCmpView(), **kwargs):
        super(PostProgressionCmpComponentView, self).__init__(layoutID, PostProgressionCmpViewModel(), **kwargs)
        self.onExitAction = Event(self._eventManager)
        return

    @property
    def viewModel(self):
        return super(PostProgressionCmpComponentView, self).getViewModel()

    def invalidateVehicle(self):
        self._fillControlsModel(self.viewModel)
        return

    def createToolTipContent(self, event, contentID):
        stepId, modId = self._parseTooltipEvent(event)
        if contentID == R.views.lobby.veh_post_progression.tooltip.PairModificationTooltipView() and stepId is not None and modId is not None:
            return CmpPairModificationTooltipView(self._vehicle, stepId, modId)
        else:
            if contentID == R.views.lobby.veh_post_progression.tooltip.PostProgressionLevelTooltipView() and stepId is not None:
                return CmpProgressionLevelTooltipView(self._vehicle, stepId)
            return super(PostProgressionCmpComponentView, self).createToolTipContent(event, contentID)

    def _addListeners(self):
        super(PostProgressionCmpComponentView, self)._addListeners()
        self.viewModel.onExitAction += self.__onExitAction
        self.viewModel.compareControl.onApplyAction += self.__onApplyAction
        self.viewModel.compareControl.onCancelAction += self.__onExitAction
        self.viewModel.compareControl.onResetAction += self.__onResetAction
        return

    def _removeListeners(self):
        self.viewModel.onExitAction -= self.__onExitAction
        self.viewModel.compareControl.onApplyAction -= self.__onApplyAction
        self.viewModel.compareControl.onCancelAction -= self.__onExitAction
        self.viewModel.compareControl.onResetAction -= self.__onResetAction
        super(PostProgressionCmpComponentView, self)._removeListeners()
        return

    def _updateVehicle(self, isReset=False, *args, **kwargs):
        mainCfgView = cmp_helpers.getCmpConfiguratorMainView()
        self._vehicle = mainCfgView.getInitialVehicleData()[0] if isReset else mainCfgView.getCurrentVehicle()
        self._selectionProvider.setPostProgression(self._vehicle.postProgression.clone())
        self._notifyCustomState(needDiff=False)
        return

    def _updateViewModel(self, viewModel, availabilityReason, completion):
        super(PostProgressionCmpComponentView, self)._updateViewModel(viewModel, availabilityReason, completion)
        viewModel.setProgressionState(ProgressionState.TRANSITIONAL)
        viewModel.setProgressionAvailability(PostProgressionAvailability.AVAILABLE)
        return

    def _fillControlsModel(self, model, postProgression=None):
        compareControl = model.compareControl
        cmpMainView = cmp_helpers.getCmpConfiguratorMainView()
        currentProgressionState = cmpMainView.getCurrentVehicle().postProgression.getState(implicitCopy=False)
        initialProgressionState = cmpMainView.getBasketVehCmpData().getInvPostProgressionState()
        customProgressionState = self._selectionProvider.getCustomProgressionState()
        compareControl.setHasInitChanges(initialProgressionState != customProgressionState)
        compareControl.setHasChanges(currentProgressionState != customProgressionState)
        return

    def _fillMultiStepModel(self, stepModel, step, selectedModID):
        super(PostProgressionCmpComponentView, self)._fillMultiStepModel(stepModel, step, selectedModID)
        stepModel.setStepState(_MULTI_STEP_STATE_MAP[step.getState()])
        return

    def _fillPersistentBonuses(self, bonuses, postProgression, completion):
        pesistentKPIs = []
        for step in postProgression.iterUnorderedSteps():
            if step.stepID in self._selectionProvider.getSelectedMainSteps():
                pesistentKPIs.extend(step.action.getKpi(self._vehicle))

        self._fillBonusesArray(bonuses.getItems(), pesistentKPIs)
        return

    def _fillSingleStepModel(self, stepModel, step):
        super(PostProgressionCmpComponentView, self)._fillSingleStepModel(stepModel, step)
        stepModel.setStepState(_SINGLE_STEP_STATE_MAP[step.getState()])
        return

    def __onApplyAction(self):
        customProgressionState = self._selectionProvider.getCustomProgressionState()
        cmp_helpers.getCmpConfiguratorMainView().installPostProgression(customProgressionState)
        self.__onExitAction()
        return

    def __onExitAction(self):
        self.onExitAction()
        return

    def __onResetAction(self):
        self._updateAll(isReset=True)
        return
