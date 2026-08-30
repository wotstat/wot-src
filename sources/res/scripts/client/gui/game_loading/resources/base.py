import typing
from gui.game_loading import loggers
if typing.TYPE_CHECKING:
    from gui.game_loading.resources.models import BaseResourceModel
_logger = loggers.getResourcesLogger()

class BaseResources(object):
    __slots__ = ()

    def destroy(self, *args, **kwargs):
        self.onDisconnected()
        _logger.debug(b'%s destroyed.', self)
        return

    def onConnected(self, *args, **kwargs):
        _logger.debug(b'%s on connected called.', self)
        return

    def onDisconnected(self, *args, **kwargs):
        _logger.debug(b'%s on disconnected called.', self)
        return

    def reset(self, *args, **kwargs):
        _logger.debug(b'%s restarted.', self)
        return

    def get(self, *args, **kwargs):
        raise NotImplementedError
        return

    def __repr__(self):
        return (b'<Resources:{}>').format(self.__class__.__name__)
