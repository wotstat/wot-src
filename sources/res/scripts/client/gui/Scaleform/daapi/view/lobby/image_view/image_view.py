from __future__ import absolute_import
from gui.impl.lobby.common.sound_constants import HANGAR_FILTERED_SOUND_SPACE
from gui.Scaleform.daapi.view.meta.ImageViewMeta import ImageViewMeta
_IMAGE_ROOT_PATH = b'../maps/icons/imageView'

class ImageView(ImageViewMeta):
    _COMMON_SOUND_SPACE = HANGAR_FILTERED_SOUND_SPACE

    def __init__(self, ctx=None):
        super(ImageView, self).__init__(ctx)
        self.__image = ctx[b'img']
        return

    def _populate(self):
        super(ImageView, self)._populate()
        self.setBgPath()
        return

    def onClose(self):
        self.destroy()
        return

    def setBgPath(self):
        image = (b'').join((_IMAGE_ROOT_PATH, b'/', self.__image))
        self.flashObject.as_setBgPath(image)
        return
