from __future__ import absolute_import
from builtins import open
from gui import GUI_SETTINGS
from gui.Scaleform.daapi.view.meta.LegalInfoWindowMeta import LegalInfoWindowMeta
from debug_utils import LOG_ERROR
from gui.impl import backport
from gui.impl.gen import R
from gui.shared import EVENT_BUS_SCOPE
from gui.shared import events

class LegalInfoWindow(LegalInfoWindowMeta):

    def __init__(self, ctx=None):
        super(LegalInfoWindow, self).__init__()
        return

    def startListening(self):
        self.addListener(events.HideWindowEvent.HIDE_LEGAL_INFO_WINDOW, self.__handleLIWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def stopListening(self):
        self.removeListener(events.HideWindowEvent.HIDE_LEGAL_INFO_WINDOW, self.__handleLIWindowHide, scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __handleLIWindowHide(self, _):
        self.destroy()
        return

    def _populate(self):
        self.startListening()
        super(LegalInfoWindow, self)._populate()
        return

    def _dispose(self):
        self.stopListening()
        super(LegalInfoWindow, self)._dispose()
        return

    def getLegalInfo(self):
        info = b''
        LICENSES_PATH = b'licenses.txt'
        try:
            f = open(LICENSES_PATH, mode=b'r', encoding=b'utf-8')
        except IOError:
            LOG_ERROR(b'cannot open %s' % LICENSES_PATH)
        else:
            info = f.read()
            info = info.format(header_1=backport.text(R.strings.menu.login.licenses.header_1()), header_2=backport.text(R.strings.menu.login.licenses.header_2()), vivoxLicense=GUI_SETTINGS.vivoxLicense.replace(b'\\n', b'\n'))
            f.close()

        self.as_setLegalInfoS(info)
        return

    def onCancelClick(self):
        self.destroy()
        return

    def onWindowClose(self):
        self.destroy()
        return
