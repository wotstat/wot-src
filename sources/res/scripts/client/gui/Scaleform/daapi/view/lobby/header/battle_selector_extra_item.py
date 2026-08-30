from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.header.battle_selector_item import SelectorItem

class SelectorExtraItem(SelectorItem):

    def __init__(self, label, data, order, selectorType=None, isVisible=True):
        super(SelectorExtraItem, self).__init__(label, data, order, selectorType, isVisible, isExtra=True)
        return

    def getVO(self):
        vo = super(SelectorExtraItem, self).getVO()
        vo.update({b'mainLabel': (self.getMainLabel()), 
           b'infoLabel': (self.getInfoLabel()), 
           b'ribbonSrc': (self.getRibbonSrc())})
        return vo

    def getMainLabel(self):
        raise NotImplementedError
        return

    def getInfoLabel(self):
        raise NotImplementedError
        return

    def getRibbonSrc(self):
        raise NotImplementedError
        return

    def _update(self, state):
        raise NotImplementedError
        return
