from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ImageManagerMeta(BaseDAAPIComponent):

    def as_setImageCacheSettingsS(self, maxSize, minSize):
        if self._isDAAPIInited():
            return self.flashObject.as_setImageCacheSettings(maxSize, minSize)
        return

    def as_loadImagesS(self, sourceData):
        if self._isDAAPIInited():
            return self.flashObject.as_loadImages(sourceData)
        return

    def as_unloadImagesS(self, sourceData):
        if self._isDAAPIInited():
            return self.flashObject.as_unloadImages(sourceData)
        return
