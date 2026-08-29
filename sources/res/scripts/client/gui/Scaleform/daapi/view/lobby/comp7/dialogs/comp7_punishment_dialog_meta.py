from gui.Scaleform.daapi.view.dialogs import I18nInfoDialogMeta
from gui.shared.events import ShowDialogEvent

class Comp7PunishmentDialogMeta(I18nInfoDialogMeta):

    def getTitle(self):
        return self._makeString((b'{}/title').format(self._key), {})

    def getMsgTitle(self):
        return self._makeString((b'{}/msgTitle').format(self._key), {})

    def getMessage(self):
        return self._makeString((b'{}/message').format(self._key), self._messageCtx)

    def getEventType(self):
        return ShowDialogEvent.SHOW_COMP7_PUNISHMENT_DIALOG
