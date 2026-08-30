from gui.Scaleform.daapi.view.battle.classic.minimap import ClassicMinimapComponent

class PveMinimapMeta(ClassicMinimapComponent):

    def as_setShorcutLabelS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setShorcutLabel(label)
        return

    def as_showGridS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showGrid(show)
        return

    def as_setGridS(self, rows, columns):
        if self._isDAAPIInited():
            return self.flashObject.as_setGrid(rows, columns)
        return
