from gui import makeHtmlString
from gui.Scaleform.daapi.view.dialogs import IDialogMeta
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.locale.DIALOGS import DIALOGS
from helpers import i18n
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS

class FreeXPInfoBaseMeta(IDialogMeta):

    def getTitle(self):
        return b''

    def getSubmitLbl(self):
        return b''

    def getTextInfo(self):
        return b''

    def getViewScopeType(self):
        return ScopeTemplates.DEFAULT_SCOPE

    def getEventType(self):
        return VIEW_ALIAS.FREE_X_P_INFO_WINDOW


class FreeXPInfoMeta(FreeXPInfoBaseMeta):

    def getTitle(self):
        return i18n.makeString(DIALOGS.FREEXPINFO_TITLE)

    def getSubmitLbl(self):
        return i18n.makeString(DIALOGS.FREEXPINFO_SUBMITBTNLBL)

    def getTextInfo(self):
        text = {}
        msgFormatted = makeHtmlString(b'html_templates:lobby/dialogs', b'freeXPInfo', {})
        text[b'body'] = msgFormatted
        return text
