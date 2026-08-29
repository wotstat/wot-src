import logging
from frameworks.wulf import ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.advanced_tooltip_view_model import AdvancedTooltipViewModel
from gui.impl.pub import ViewImpl
_logger = logging.getLogger(__name__)

class AdvancedTooltipView(ViewImpl):
    __slots__ = (b'_movie', b'_header', b'_description')

    def __init__(self, movie, header, description):
        settings = ViewSettings(R.views.lobby.crew.tooltips.AdvancedTooltipView(), model=AdvancedTooltipViewModel())
        super(AdvancedTooltipView, self).__init__(settings)
        self._movie = movie
        self._header = header
        self._description = description
        return

    def onError(self, args):
        errorFilePath = str(args.get(b'errorFilePath', b''))
        _logger.error(b'Reward video error: %s', errorFilePath)
        self.destroyWindow()
        return

    @property
    def viewModel(self):
        return super(AdvancedTooltipView, self).getViewModel()

    def _onLoading(self, *args, **kwargs):
        super(AdvancedTooltipView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            tx.setMovie(self._movie)
            tx.setHeader(self._header)
            tx.setDescription(self._description)
        return

    def _getEvents(self):
        return ((self.viewModel.onError, self.onError),)
