from white_tiger.gui.Scaleform.daapi.view.battle.white_tiger.ability_widget import IComponentWidgetView
from white_tiger.gui.Scaleform.daapi.view.meta.WTMissileWidgetMeta import WTMissileWidgetMeta

class WhiteTigerMissileWidgetView(WTMissileWidgetMeta, IComponentWidgetView):

    def show(self, useAnim=False):
        self.as_showS(useAnim)
        return

    def hide(self, useAnim=False):
        self.as_hideS(useAnim)
        return

    def update(self, **kwargs):
        if b'distance' in kwargs:
            self.as_setRangeS(kwargs[b'distance'])
        if b'altitude' in kwargs:
            self.as_setAltitudeS(kwargs[b'altitude'])
        return
