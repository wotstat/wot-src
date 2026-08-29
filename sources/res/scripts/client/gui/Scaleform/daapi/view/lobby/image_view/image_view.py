from gui.Scaleform.daapi.view.meta.ImageViewMeta import ImageViewMeta
from gui.sounds.filters import switchHangarFilteredFilter
_IMAGE_ROOT_PATH = b'../maps/icons/imageView'

class ImageView(ImageViewMeta):

    def __init__(self, ctx=None):
        super(ImageView, self).__init__(ctx)
        self.__image = ctx[b'img']
        return

    def _populate(self):
        super(ImageView, self)._populate()
        self.setBgPath()
        switchHangarFilteredFilter(on=True)
        return

    def onClose(self):
        self.destroy()
        switchHangarFilteredFilter(on=False)
        return

    def setBgPath(self):
        image = (b'').join((_IMAGE_ROOT_PATH, b'/', self.__image))
        self.flashObject.as_setBgPath(image)
        return
