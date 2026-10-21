from frameworks.wulf import ViewSettings
from portal.gui.impl.gen.view_models.views.lobby.tooltips.progress_token_tooltip_model import ProgressTokenTooltipModel
from gui.impl.pub import ViewImpl
from gui.impl.gen import R

class ProgressTokenTooltip(ViewImpl):
    __slots__ = (b'_isToken', b'_isCompleted', b'_currentPoints', b'_nextLevelPoints')

    def __init__(self, isToken, isComplete, currentPoints, nextLevelPoints):
        settings = ViewSettings(R.views.portal.lobby.tooltips.ProgressTokenTooltip())
        settings.model = ProgressTokenTooltipModel()
        self._isToken = isToken
        self._isCompleted = isComplete
        self._currentPoints = currentPoints
        self._nextLevelPoints = nextLevelPoints
        super(ProgressTokenTooltip, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(ProgressTokenTooltip, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(ProgressTokenTooltip, self)._onLoading(*args, **kwargs)
        self.__updateData()
        return

    def __updateData(self):
        with self.viewModel.transaction() as vm:
            self.__fillModel(vm)
        return

    def __fillModel(self, model):
        model.setIsTokenTooltip(self._isToken)
        model.setInProgress(True)
        model.setIsCompleted(self._isCompleted)
        model.setCurrentPoints(self._currentPoints)
        model.setNextLevelPoints(self._nextLevelPoints)
        return
