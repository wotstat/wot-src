import json, logging, typing
from gui.impl.gen.view_models.common.ui_logger_model import UiLoggerModel
from skeletons.gui.impl import IGuiLoader
from helpers import dependency
from skeletons.ui_logging import IUILoggingCore, IUILoggingListener
from wotdecorators import noexcept
_logger = logging.getLogger(__name__)

class UILoggingListener(IUILoggingListener):
    _core = dependency.descriptor(IUILoggingCore)
    __slots__ = (b'__model',)

    def __init__(self):
        super(UILoggingListener, self).__init__()
        guiLoader = dependency.instance(IGuiLoader)
        self.__model = typing.cast(UiLoggerModel, guiLoader.uiLogger.getModel())
        self.__model.log += self._log
        return

    def fini(self):
        if self.__model is not None:
            self.__model.log -= self._log
            _logger.debug(b'UIGFLoggingListener unsubscribed from model.')
        self.__model = None
        _logger.debug(b'UIGFLoggingListener destroyed.')
        return

    @noexcept
    def _log(self, args):
        self._core.log(feature=args[b'feature'], group=args[b'group'], action=args[b'action'], loglevel=args[b'logLevel'], **json.loads(args[b'params']))
        return
