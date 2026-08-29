import typing
from frameworks.wulf.view.submodel_presenter import SubModelPresenter
import logging
from gui.impl.lobby.paragons.paragons_helpers.paragons_model_helpers import fillChapterModels
from helpers import dependency
from skeletons.gui.game_control import IParagonsController
_logger = logging.getLogger(__name__)
if typing.TYPE_CHECKING:
    from typing import Dict
    from frameworks.wulf import View, ViewModel

class ChaptersPresenter(SubModelPresenter):
    __slots__ = SubModelPresenter.__slots__ + (b'__tooltipData',)
    __paragonsController = dependency.descriptor(IParagonsController)

    def __init__(self, viewModel, parentView):
        super(ChaptersPresenter, self).__init__(viewModel, parentView)
        self.__viewModel = viewModel
        self.__tooltipData = {}
        return

    @property
    def viewModel(self):
        return super(ChaptersPresenter, self).getViewModel()

    @property
    def parentViewModel(self):
        return self.parentView.getViewModel()

    def initialize(self, *args, **kwargs):
        super(ChaptersPresenter, self).initialize(*args, **kwargs)
        self.__updateChapters()
        _logger.info(b'[Paragons]: chapters presenter inited')
        return

    def finalize(self):
        _logger.info(b'[Paragons]: chapters presenter finalized')
        super(ChaptersPresenter, self).finalize()
        return

    def createToolTipContent(self, event, contentID):
        return

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(tooltipId)

    def _getEvents(self):
        return (
         (
          self.viewModel.onSelectChapter, self.__onSelectChapter),
         (
          self.__paragonsController.onSettingsChanged, self.__onServerSettingsChanged),
         (
          self.__paragonsController.onProgressPointsChanged, self.__updateChapters))

    def __onSelectChapter(self, event):
        chapterId = int(event.get(b'id', 0))
        self.__paragonsController.setChapter(chapterId, self.__selectChapterCallback)
        return

    def __selectChapterCallback(self, isSuccess, _):
        if isSuccess:
            self.__updateChapters()
        return

    def __updateChapters(self):
        with self.parentViewModel.progression.transaction() as tx:
            fillChapterModels(tx.getStages(), tooltipData=self.__tooltipData)
        return

    def __onServerSettingsChanged(self, _):
        self.__updateChapters()
        return
