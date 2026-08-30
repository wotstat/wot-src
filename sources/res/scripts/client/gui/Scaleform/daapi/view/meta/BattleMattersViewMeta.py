from gui.Scaleform.daapi.view.meta.MissionsViewBaseMeta import MissionsViewBaseMeta

class BattleMattersViewMeta(MissionsViewBaseMeta):

    def as_showViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showView()
        return

    def as_hideViewS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideView()
        return

    def as_setPlaceIdS(self, placeId):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlaceId(placeId)
        return
