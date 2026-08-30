from gui.Scaleform.daapi.view.meta.NotifyCenterDialogMeta import NotifyCenterDialogMeta
from gui.notify_center import g_notifyCenterProvider

class NotifyCenterDialog(NotifyCenterDialogMeta):

    def __init__(self, ctx=None):
        super(NotifyCenterDialog, self).__init__()
        self.__notID = ctx[b'notID']
        self.__target = ctx[b'target']
        return

    def onWindowClose(self):
        self.destroy()
        return

    def doAction(self, actionID, isButtonClicked):
        g_notifyCenterProvider.doAction(self.__notID, actionID, self.__target)
        if isButtonClicked:
            self.destroy()
        return

    def _populate(self):
        super(NotifyCenterDialog, self)._populate()
        item = g_notifyCenterProvider.getNotItemByName(self.__notID, self.__target)
        self.as_setTextS(item.getBody())
        self.as_setTitleS(item.getTopic())
        self.as_setButtonsS(item.getButtonsMap())
        return

    def _dispose(self):
        self.__notID = None
        self.__target = None
        super(NotifyCenterDialogMeta, self)._dispose()
        return
