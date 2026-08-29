from gui.Scaleform.daapi.view.meta.FreeXPInfoWindowMeta import FreeXPInfoWindowMeta
__author__ = b'd_savitski'

class FreeXPInfoWindow(FreeXPInfoWindowMeta):

    def __init__(self, ctx=None):
        super(FreeXPInfoWindow, self).__init__()
        self.meta = ctx.get(b'meta')
        self.handler = ctx.get(b'handler')
        return

    def _populate(self):
        super(FreeXPInfoWindow, self)._populate()
        self.as_setTitleS(self.meta.getTitle())
        self.as_setSubmitLabelS(self.meta.getSubmitLbl())
        self.as_setTextS(self.meta.getTextInfo())
        return

    def onWindowClose(self):
        self.handler(True)
        self.destroy()
        return

    def onSubmitButton(self):
        self.onWindowClose()
        return

    def onCancelButton(self):
        self.onWindowClose()
        return

    def _dispose(self):
        super(FreeXPInfoWindow, self)._dispose()
        self.handler = None
        return
