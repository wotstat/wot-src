from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class WTBossTeleportViewMeta(BaseDAAPIComponent):

    def onTeleportPointClick(self, id):
        self._printOverrideError(b'onTeleportPointClick')
        return

    def onCancel(self):
        self._printOverrideError(b'onCancel')
        return
