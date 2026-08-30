from collections import namedtuple
from Event import Event, EventManager
from frameworks.wulf import ViewSettings
from gui.impl.pub import ViewImpl
from gui.Scaleform.daapi.view.meta.GFHeaderWidgetMeta import GFHeaderWidgetMeta
from gui.impl.gen.view_models.views.lobby.hangar.header_widget_view_model import HeaderWidgetViewModel
GFWidgetAliases = namedtuple(b'GFWidgetAliases', [b'flashLinkage', b'registerAlias'])

class GFHeaderWidget(GFHeaderWidgetMeta):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(GFHeaderWidget, self).__init__()
        return

    def _makeInjectView(self):
        raise NotImplementedError(b'The method must return a View inherited from GFHeaderWidgetView')
        return

    def _onPopulate(self):
        super(GFHeaderWidget, self)._onPopulate()
        self._addViewListeners()
        return

    def _dispose(self):
        self._removeViewListeners()
        super(GFHeaderWidget, self)._dispose()
        return

    def _addViewListeners(self):
        view = self.getInjectView()
        if view:
            view.onChangeLayout += self._onChangeLayout
        return

    def _removeViewListeners(self):
        view = self.getInjectView()
        if view:
            view.onChangeLayout -= self._onChangeLayout
        return

    def _onChangeLayout(self, top, right, left):
        self.as_updateMarginsS(top, right, left)
        return


class GFHeaderWidgetView(ViewImpl):
    __slots__ = (b'_eManager', b'onChangeLayout')

    def __init__(self, layoutID, model, *args, **kwargs):
        super(GFHeaderWidgetView, self).__init__(ViewSettings(layoutID=layoutID, model=model))
        self._eManager = EventManager()
        self.onChangeLayout = Event(self._eManager)
        return

    def _getEvents(self):
        return ((self.getViewModel().onChangeLayout, self._onChangeLayout),)

    def _finalize(self):
        self._eManager.clear()
        super(GFHeaderWidgetView, self)._finalize()
        return

    def _onChangeLayout(self, args):
        top = args.get(HeaderWidgetViewModel.ARG_TOP, 0)
        right = args.get(HeaderWidgetViewModel.ARG_RIGHT, 0)
        left = args.get(HeaderWidgetViewModel.ARG_LEFT, 0)
        self.onChangeLayout(top, right, left)
        return
