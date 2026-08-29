from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RssNewsFeedMeta(BaseDAAPIComponent):

    def openBrowser(self, linkToOpen):
        self._printOverrideError(b'openBrowser')
        return

    def as_updateFeedS(self, feed):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFeed(feed)
        return
