from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.SystemMessageDialogMeta import SystemMessageDialogMeta

class SystemMessageDialog(SystemMessageDialogMeta):

    def __init__(self, meta, handler, **kwargs):
        super(SystemMessageDialog, self).__init__()
        self.__meta = meta
        self.__handler = handler
        return

    def _populate(self):
        super(SystemMessageDialog, self)._populate()
        self.as_setInitDataS({b'title': (self.__meta.getTitle()), 
           b'closeBtnTitle': (self.__meta.getCancelLabel()), 
           b'settings': (self.__meta.getSettings())})
        self.as_setMessageDataS(self.__meta.getMessageObject())
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _dispose(self):
        if self.__handler:
            self.__handler(True)
        self.__meta.cleanUp()
        self.__meta = None
        self.__handler = None
        super(SystemMessageDialog, self)._dispose()
        return
