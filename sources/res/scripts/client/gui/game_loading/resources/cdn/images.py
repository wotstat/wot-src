import typing
from gui.game_loading import loggers
from gui.game_loading.resources.base import BaseResources
from gui.game_loading.resources.cdn.models import LocalSlideModel
from gui.game_loading.resources.cdn.cache import GameLoadingCdnCacheMgr
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.cdn.models import CdnCacheDefaultsModel
_logger = loggers.getResourcesLogger()

class CdnImagesResources(BaseResources):
    __slots__ = (b'_cdnCacheMgr',)

    def __init__(self, defaults):
        super(CdnImagesResources, self).__init__()
        self._cdnCacheMgr = GameLoadingCdnCacheMgr(defaults)
        return

    def destroy(self):
        super(CdnImagesResources, self).destroy()
        self._cdnCacheMgr.destroy()
        return

    def onConnected(self):
        self._cdnCacheMgr.onConnected()
        super(CdnImagesResources, self).onConnected()
        return

    def onDisconnected(self):
        self._cdnCacheMgr.onDisconnected()
        super(CdnImagesResources, self).onDisconnected()
        return

    def get(self):
        return self._cdnCacheMgr.nextSlide()
