from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.WindowViewMeta import WindowViewMeta

class AbstractWindowView(WindowViewMeta):

    def __init__(self, ctx=None):
        super(AbstractWindowView, self).__init__()
        return

    def _populate(self):
        super(AbstractWindowView, self)._populate()
        return

    def onTryClosing(self):
        return True
