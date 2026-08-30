from gui.Scaleform.daapi.view.lobby.rally.AbstractRallyWindow import AbstractRallyWindow

class BaseRallyMainWindowMeta(AbstractRallyWindow):

    def onBackClick(self):
        self._printOverrideError(b'onBackClick')
        return

    def getClientID(self):
        self._printOverrideError(b'getClientID')
        return
