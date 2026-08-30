from __future__ import absolute_import
import logging, typing
from functools import wraps
from gui.Scaleform.daapi.view.meta.InjectComponentMeta import InjectComponentMeta
from helpers import dependency
from skeletons.gui.impl import IGuiLoader
from frameworks.wulf import ViewStatus, ViewFlags
if typing.TYPE_CHECKING:
    from frameworks.wulf import View, Window
_logger = logging.getLogger(__name__)

def hasAliveInject(deadUnexpected=False):

    def decorator(method):

        @wraps(method)
        def wrapper(injectAdapor, *args, **kwargs):
            if injectAdapor.getInjectView() is not None:
                method(injectAdapor, *args, **kwargs)
            elif deadUnexpected:
                _logger.warning(b'unexpected call on adaptor %s without alive content', injectAdapor)
            return

        return wrapper

    return decorator


class InjectComponentAdaptor(InjectComponentMeta):
    __slots__ = (b'__injected', b'__view')
    __gui = dependency.descriptor(IGuiLoader)

    def __init__(self):
        super(InjectComponentAdaptor, self).__init__()
        self.__view = None
        return

    def registerFlashComponent(self, component, alias, *args):
        _logger.warning(b'InjectComponentAdaptor %s does not support internal components', self.getAlias())
        return

    def isFlashComponentRegistered(self, alias):
        return False

    def unregisterFlashComponent(self, alias):
        _logger.warning(b'InjectComponentAdaptor %s does not support internal components', self.getAlias())
        return

    def getInjectView(self):
        return self.__view

    @property
    def _injectView(self):
        return self.__view

    def _populate(self):
        super(InjectComponentAdaptor, self)._populate()
        self._onPopulate()
        return

    def _onPopulate(self):
        self._createInjectView()
        return

    def _dispose(self):
        self._destroyInjected()
        super(InjectComponentAdaptor, self)._dispose()
        return

    def _makeInjectView(self, *args):
        raise NotImplementedError
        return

    def _addInjectContentListeners(self):
        return

    def _removeInjectContentListeners(self):
        return

    def _createInjectView(self, *args):
        if not self._isDAAPIInited():
            _logger.warning(b'GFxValue is not created for %s', self.getAlias())
            return
        else:
            if self.__view is not None:
                _logger.error(b'View %r is already created in component %s', self.__view, self.getAlias())
                return
            self.__view = self._makeInjectView(*args)
            if self.__view is None:
                return
            if self.__view.viewFlags != ViewFlags.VIEW:
                _logger.error(b'View %r with flags %r is not supported to be injected. %r. ViewFlags.VIEW is the only supported.', self.__view, self.__view.viewFlags, self.getAlias())
                return
            self.__view.onStatusChanged += self.__onViewStatusChanged
            self._addInjectContentListeners()
            placeId = self.__view.uniqueID
            mainWindow = self.__gui.windowsManager.getMainWindow()
            mainView = mainWindow.content
            mainView.addChild(placeId, self.__view, loadImmediately=True)
            self.as_setPlaceIdS(placeId)
            return

    def _destroyInjected(self):
        if self.__view is not None:
            self._removeInjectContentListeners()
            self.__view.onStatusChanged -= self.__onViewStatusChanged
            mainWindow = self.__gui.windowsManager.getMainWindow()
            mainView = mainWindow.content
            placeId = self.__view.uniqueID
            mainView.removeChild(placeId, destroy=True)
            self.__view = None
            self.as_setPlaceIdS(0)
        return

    def __onViewStatusChanged(self, status):
        if status == ViewStatus.DESTROYED and self.__view is not None:
            _logger.info(b'Inject component was destroyed: %s (%r)', self.getAlias(), self.__view)
            self.__view = None
            self.as_setPlaceIdS(0)
        return
