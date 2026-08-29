from frameworks.wulf import ViewFlags, ViewSettings
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.tooltips.task_condition_tooltip_view_model import TaskConditionTooltipViewModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class TaskConditionTooltipView(ViewImpl):
    __slots__ = (b'__vehicleLevels', b'__vehicleTypes', b'__battleTypes', b'__vehicleNations')

    def __init__(self, vehicleLevels, vehicleTypes, battleTypes, vehicleNations):
        settings = ViewSettings(R.views.armory_yard.lobby.feature.tooltips.TaskConditionTooltipView())
        settings.flags = ViewFlags.VIEW
        settings.model = TaskConditionTooltipViewModel()
        self.__vehicleLevels = vehicleLevels
        self.__vehicleTypes = vehicleTypes
        self.__vehicleNations = vehicleNations
        self.__battleTypes = battleTypes
        super(TaskConditionTooltipView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(TaskConditionTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(TaskConditionTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            self.__updateModel(model)
        return

    def __updateModel(self, model):
        model.setLevels(str(self.__vehicleLevels))
        array = model.getVehicleTypes()
        for item in self.__vehicleTypes.split(b','):
            array.addString(item)

        array.invalidate()
        array = model.getVehicleNations()
        for item in self.__vehicleNations.split(b','):
            array.addString(item)

        array.invalidate()
        array = model.getBattleTypes()
        battleTypes = self.__battleTypes.split(b',')
        for battleType in battleTypes:
            array.addNumber(int(battleType))

        array.invalidate()
        return
