from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseStorageCategoryViewMeta(BaseDAAPIComponent):

    def setActiveState(self, isActive):
        self._printOverrideError(b'setActiveState')
        return

    def playInfoSound(self):
        self._printOverrideError(b'playInfoSound')
        return

    def scrolledToBottom(self):
        self._printOverrideError(b'scrolledToBottom')
        return

    def as_showDummyScreenS(self, show):
        if self._isDAAPIInited():
            return self.flashObject.as_showDummyScreen(show)
        return

    def as_showFilterWarningS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showFilterWarning(data)
        return

    def as_getCardsDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCardsDP()
        return

    def as_scrollToItemS(self, itemIntCD):
        if self._isDAAPIInited():
            return self.flashObject.as_scrollToItem(itemIntCD)
        return
