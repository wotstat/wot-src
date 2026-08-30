from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.GoodieInfoMeta import GoodieInfoMeta
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache

class GoodieInfoWindow(GoodieInfoMeta):
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, ctx=None):
        super(GoodieInfoWindow, self).__init__()
        self.goodieID = ctx.get(b'goodieID')
        return

    def onCancelClick(self):
        self.destroy()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _populate(self):
        super(GoodieInfoWindow, self)._populate()
        goodie = self.goodiesCache.getGoodie(self.goodieID)
        self.as_setInfoS({b'windowTitle': (goodie.userName), 
           b'name': (goodie.userName), 
           b'icon': (goodie.iconInfo), 
           b'description': (goodie.longDescription)})
        return
