import typing
from gui.collection import loggers
from gui.impl import backport
from gui.impl.gen import R
_logger = loggers.getLocalCacheLogger()
if typing.TYPE_CHECKING:
    from typing import Dict, List

class CollectionsLocalCacheMgr(object):
    __IMG = R.images.gui.maps.icons.collections.fakeCdn.images

    def startSync(self, *args, **kwargs):
        _logger.debug(b'Sync started')
        return

    def stopSync(self, *args, **kwargs):
        _logger.debug(b'Sync stopped')
        return

    def getImagesPaths(self, imagesIDs, callback=None):
        callback(True, self.__packImages(imagesIDs))
        return

    def __packImages(self, imagesIDs):
        packed = {}
        for imageID in imagesIDs:
            group, sub, name = imageID.split(b'/')
            packed.setdefault(group, {})
            packed[group].setdefault(sub, {})
            resID = self.__IMG.dyn(group).dyn(sub).dyn(name)()
            if resID != R.invalid():
                packed[group][sub][name] = backport.image(resID)

        return packed
