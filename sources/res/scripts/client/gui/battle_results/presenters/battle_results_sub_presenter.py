import typing
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
from helpers import dependency
from skeletons.gui.battle_results import IBattleResultsService
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from typing import Union, Type, Optional, Any
    from frameworks.wulf import View, ViewEvent, Window, ViewModel, Array
    BattleResultsComponentModelType = typing.TypeVar(b'BattleResultsComponentModelType', bound=ViewModel)
    TooltipModelType = typing.TypeVar(b'TooltipModelType', bound=ViewModel)

class UnexpectedViewModelException(SoftException):
    pass


class BattleResultsSubPresenter(SubModelPresenter):
    _battleResults = dependency.descriptor(IBattleResultsService)

    def __init__(self, viewModel, parentView):
        viewModelType = self.getViewModelType()
        if hasattr(viewModelType, b'__origin__'):
            viewModelType = viewModelType.__origin__
        if not isinstance(viewModel, viewModelType):
            raise UnexpectedViewModelException((b'Expected an instance of {}, got {}').format(self.getViewModelType(), viewModel.__class__))
        super(BattleResultsSubPresenter, self).__init__(viewModel, parentView)
        self._subPresenters = []
        return

    @classmethod
    def getViewModelType(cls):
        raise NotImplementedError
        return

    def initialize(self, *args, **kwargs):
        super(BattleResultsSubPresenter, self).initialize(*args, **kwargs)
        for subPresenter in self._subPresenters:
            subPresenter.initialize(*args, **kwargs)

        return

    def finalize(self):
        for subPresenter in self._subPresenters:
            subPresenter.finalize()

        self._subPresenters = []
        super(BattleResultsSubPresenter, self).finalize()
        return

    def addSubPresenter(self, subPacker):
        self._subPresenters.append(subPacker)
        return

    def removeSubPacker(self, subPacker):
        self._subPresenters.remove(subPacker)
        return

    def getBattleResults(self):
        statsController = self._battleResults.getStatsCtrl(self.parentView.arenaUniqueID)
        return statsController.getResults()

    def packBattleResults(self, battleResults):
        for subPresenter in self._subPresenters:
            subPresenter.packBattleResults(battleResults)

        return

    def createToolTipContent(self, event, contentID):
        for subPresenter in self._subPresenters:
            content = subPresenter.createToolTipContent(event, contentID)
            if content is not None:
                return content

        return super(BattleResultsSubPresenter, self).createToolTipContent(event, contentID)

    def createContextMenu(self, event):
        for subPresenter in self._subPresenters:
            window = subPresenter.createContextMenu(event)
            if window is not None:
                return window

        return super(BattleResultsSubPresenter, self).createContextMenu(event)
