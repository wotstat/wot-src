from gui.Scaleform import MENU
from gui.Scaleform.daapi.view.meta.BoosterInfoMeta import BoosterInfoMeta
from gui.Scaleform.framework.entities.View import View
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.goodies import IGoodiesCache

class BoosterInfoWindow(BoosterInfoMeta):
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, ctx=None):
        super(BoosterInfoWindow, self).__init__()
        self.boosterID = ctx.get(b'boosterID')
        return

    def onCancelClick(self):
        self.destroy()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _populate(self):
        super(View, self)._populate()
        booster = self.goodiesCache.getBooster(self.boosterID)
        self.as_setBoosterInfoS({b'windowTitle': (_ms(MENU.BOOSTERS_COMMON_NAME)), 
           b'name': (booster.userName), 
           b'icon': (booster.icon), 
           b'parameters': [
                         {b'value': ((b'{}\n').format(booster.getFormattedValue())), 
                            b'type': ((b'{}\n').format(_ms(MENU.BOOSTERS_COMMON_EFFECT_VALUE)))},
                         {b'value': (booster.getEffectTimeStr(hoursOnly=True)), 
                            b'type': (_ms(MENU.BOOSTERS_COMMON_EFFECT_TIME))}]})
        return
