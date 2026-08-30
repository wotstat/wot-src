import typing
if typing.TYPE_CHECKING:
    from typing import Union
    from gui.impl.gen.view_models.views.lobby.account_dashboard.account_dashboard_model import AccountDashboardModel

class FeatureItem(object):

    def __init__(self, viewModel):
        self._viewModel = viewModel
        return

    def initialize(self, *args, **kwargs):
        return

    def finalize(self):
        self._viewModel = None
        return

    def createToolTipContent(self, event, contentID):
        return

    def createPopOverContent(self, event):
        return

    def _fillModel(self, model):
        raise NotImplementedError
        return

    def fill(self, ctx=None):
        if ctx is None:
            with self._viewModel.transaction() as tx:
                self._fillModel(tx)
        else:
            self._fillModel(ctx)
        return

    def getViewModel(self):
        return self._viewModel
