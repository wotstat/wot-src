from gui.Scaleform.daapi.view.meta.MissionsViewBaseMeta import MissionsViewBaseMeta

class MissionsListViewBaseMeta(MissionsViewBaseMeta):

    def openMissionDetailsView(self, id, blockId):
        self._printOverrideError(b'openMissionDetailsView')
        return

    def as_getDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getDP()
        return

    def as_scrollToItemS(self, idFieldName, itemId):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToItem(idFieldName, itemId)
        return
