import logging, typing, Event
from soft_exception import SoftException
from ..py_object_binder import PyObjectEntity, getProxy, getObject
from ..py_object_wrappers import PyObjectWindowSettings
from ..py_object_wrappers import PyObjectWindow
from ..view.view import View
from ..view.view_model import ViewModel
from ..gui_constants import WindowStatus, WindowFlags, ViewStatus, ShowingStatus
_logger = logging.getLogger(__name__)
NO_WINDOW_OWNER = 0

class WindowSettings(object):
    __slots__ = (b'__proxy',)

    def __init__(self):
        super(WindowSettings, self).__init__()
        self.__proxy = PyObjectWindowSettings()
        return

    def clear(self):
        self.__proxy = None
        return

    @property
    def proxy(self):
        return self.__proxy

    @property
    def flags(self):
        return self.__proxy.flags

    @flags.setter
    def flags(self, flags):
        self.__proxy.flags = flags
        return

    @property
    def layer(self):
        return self.__proxy.layer

    @layer.setter
    def layer(self, layer):
        self.__proxy.layer = layer
        return

    @property
    def name(self):
        return self.__proxy.name

    @name.setter
    def name(self, name):
        self.__proxy.name = name
        return

    @property
    def areaID(self):
        return self.__proxy.areaID

    @areaID.setter
    def areaID(self, areaID):
        self.__proxy.areaID = areaID
        return

    @property
    def decorator(self):
        return getObject(self.__proxy.decorator)

    @decorator.setter
    def decorator(self, decorator):
        if decorator is not None and not isinstance(decorator, View):
            raise SoftException(b'Decorator should be View class or extends it')
        self.__proxy.decorator = getProxy(decorator)
        return

    @property
    def content(self):
        return getObject(self.__proxy.content)

    @content.setter
    def content(self, content):
        if content is not None and not isinstance(content, View):
            raise SoftException(b'Content should be View class or extends it')
        self.__proxy.content = getProxy(content)
        return

    @property
    def parent(self):
        return getObject(self.__proxy.parent)

    @parent.setter
    def parent(self, parent):
        if parent is not None and not isinstance(parent, Window):
            raise SoftException(b'Content should be Window class or extends it')
        self.__proxy.parent = getProxy(parent)
        return

    @property
    def ownerViewID(self):
        return self.__proxy.ownerViewID

    @ownerViewID.setter
    def ownerViewID(self, ownerViewID_):
        self.__proxy.ownerViewID = ownerViewID_ or NO_WINDOW_OWNER
        return


class Window(PyObjectEntity):
    __slots__ = (b'onStatusChanged', b'__windowStatus', b'onShowingStatusChanged', b'onFocusChanged', b'onReady', b'onSizeChanged', b'onPositionChanged', b'__showingStatus', b'__isReady', b'__isShown', b'__isFocused', b'__em')

    def __init__(self, settings):
        if not settings.name:
            settings.name = self.getName()
        super(Window, self).__init__(PyObjectWindow(settings.proxy))
        self.__em = Event.EventManager()
        self.onStatusChanged = Event.Event(self.__em)
        self.__windowStatus = WindowStatus.UNDEFINED if self.proxy is None else self.proxy.windowStatus
        self.onShowingStatusChanged = Event.Event(self.__em)
        self.__showingStatus = ShowingStatus.HIDDEN
        self.__isShown = False
        self.__isFocused = False
        self.onFocusChanged = Event.Event(self.__em)
        self.onSizeChanged = Event.Event(self.__em)
        self.onPositionChanged = Event.Event(self.__em)
        self.__isReady = False
        self.onReady = Event.Event(self.__em)
        _logger.debug(b'Creating %r with %r', self, settings)
        return

    def __repr__(self):
        return (b'{}(uniqueID={}, layer={}, decorator={}, content={})').format(self.__class__.__name__, self.uniqueID, self.layer, self.decorator, self.content)

    def getName(self):
        module = self.__class__.__module__
        if module is None:
            return self.__class__.__name__
        else:
            return (b'.').join((module, self.__class__.__name__))

    @property
    def decorator(self):
        proxy = self.proxy
        if proxy is not None:
            return proxy.decorator
        else:
            return

    @property
    def content(self):
        proxy = self.proxy
        if proxy is not None:
            return proxy.content
        else:
            return

    @property
    def parent(self):
        if self.proxy is not None:
            return self.proxy.parent
        else:
            return

    @property
    def layer(self):
        if self.proxy is not None:
            return self.proxy.layer
        else:
            return -1

    @property
    def uniqueID(self):
        if self.proxy is not None:
            return self.proxy.uniqueID
        else:
            return 0

    @property
    def windowFlags(self):
        if self.proxy is not None:
            return self.proxy.windowFlags
        else:
            return WindowFlags.UNDEFINED

    @property
    def windowStatus(self):
        return self.__windowStatus

    @property
    def showingStatus(self):
        return self.__showingStatus

    @property
    def isFocused(self):
        return self.__isFocused

    @property
    def isReady(self):
        return self.__isReady

    @isReady.setter
    def isReady(self, value):
        oldIsReady = self.__isReady
        if oldIsReady and not value:
            _logger.error(b"Window's readiness cannot be reset: %r", self)
            return
        self.__isReady = value
        if not oldIsReady and value:
            self.onReady()
        return

    @property
    def position(self):
        proxy = self.proxy
        if proxy is not None:
            return self.proxy.windowPosition
        else:
            return (0.0, 0.0)

    @property
    def globalPosition(self):
        proxy = self.proxy
        if proxy is not None:
            return self.proxy.calculateGlobalPosition
        else:
            return (0.0, 0.0)

    @property
    def size(self):
        proxy = self.proxy
        if proxy is not None:
            return self.proxy.windowSize
        else:
            return (0.0, 0.0)

    @property
    def typeFlag(self):
        return self.windowFlags & WindowFlags.WINDOW_TYPE_MASK

    @property
    def stateFlag(self):
        return self.windowFlags & WindowFlags.WINDOW_STATE_MASK

    @property
    def modalityFlag(self):
        return self.windowFlags & WindowFlags.WINDOW_MODALITY_MASK

    def checkWindowFlags(self, flags):
        return self.proxy.checkWindowFlags(flags)

    def isModal(self):
        return self.proxy.isModal()

    def setDecorator(self, decorator):
        self.__detachFromDecorator()
        self.proxy.setDecorator(getProxy(decorator))
        self.__attachToDecorator()
        return

    def setContent(self, view):
        self.__detachFromContent()
        self.proxy.setContent(getProxy(view))
        self.__attachToContent()
        return

    def setParent(self, parent):
        self.proxy.setParent(getProxy(parent))
        return

    def load(self):
        _logger.info(b'Loading window: %r', self)
        self.proxy.load()
        return

    def reload(self):
        self.proxy.reload()
        return

    def destroy(self):
        _logger.debug(b'Destroying window: %r', self)
        if self.proxy is not None:
            self.proxy.destroy()
        self.__em.clear()
        return

    def setLayer(self, layerID):
        self.proxy.setLayer(layerID)
        return

    def resetLayer(self):
        self.proxy.resetLayer()
        return

    def tryFocus(self):
        self.proxy.tryFocus()
        return

    def show(self, focus=True):
        self.proxy.show(focus)
        return

    def hide(self, destroy=False):
        self.proxy.hide(destroy)
        return

    def isHidden(self):
        return self.proxy.isHidden()

    def _getDecoratorViewModel(self):
        decorator = self.decorator
        if decorator is not None:
            return decorator.getViewModel()
        else:
            return

    def _initialize(self):
        self.__attachToDecorator()
        self.__attachToContent()
        return

    def _finalize(self):
        self.__detachFromDecorator()
        self.__detachFromContent()
        return

    def _onReady(self):
        self.show()
        return

    def _onShown(self):
        _logger.debug(b'_onShown %r', self)
        return

    def _onHidden(self):
        _logger.debug(b'_onHidden %r', self)
        return

    def _onFocus(self, focused):
        _logger.debug(b'_onFocus %r %r', focused, self)
        return

    def _onDecoratorReady(self):
        return

    def _onDecoratorReleased(self):
        return

    def _onContentReady(self):
        return

    def _onContentReleased(self):
        return

    def _swapShowingStates(self, oldStatus, newStatus):
        if newStatus == ShowingStatus.SHOWN:
            if not self.__isShown:
                self.__isShown = True
                self._onShown()
        elif newStatus == ShowingStatus.HIDDEN:
            if self.__isShown:
                self.__isShown = False
                self._onHidden()
        elif newStatus == ShowingStatus.SHOWING:
            pass
        elif newStatus == ShowingStatus.HIDING:
            pass
        return

    def _cInit(self):
        self._initialize()
        return

    def _cFini(self):
        self._finalize()
        return

    def _cWindowStatusChanged(self, _, newStatus):
        self.__windowStatus = newStatus
        _logger.debug(b'Status changed to %r for %r', newStatus, self)
        self.onStatusChanged(newStatus)
        return

    def _cShowingStatusChanged(self, oldStatus, newStatus):
        oldStatus = ShowingStatus(oldStatus)
        newStatus = ShowingStatus(newStatus)
        self.__showingStatus = newStatus
        self._swapShowingStates(oldStatus, newStatus)
        self.onShowingStatusChanged(newStatus)
        return

    def _cReady(self):
        self.isReady = True
        if self.__windowStatus == WindowStatus.LOADED:
            self._onReady()
        return

    def _cFocusChanged(self, focused):
        self.__isFocused = focused
        self._onFocus(focused)
        self.onFocusChanged(focused)
        return

    def _cResized(self, width, height):
        _logger.debug(b'Size changed to %d %d for %r', width, height, self)
        self.onSizeChanged(self.uniqueID, width, height)
        return

    def _cPositionChanged(self, x, y):
        self.onPositionChanged(self.uniqueID, x, y)
        return

    def __attachToDecorator(self):
        decorator = self.decorator
        if decorator is not None:
            if decorator.viewStatus == ViewStatus.LOADED:
                self._onDecoratorReady()
            decorator.onStatusChanged += self.__onDecoratorStatusChanged
        return

    def __detachFromDecorator(self):
        decorator = self.decorator
        if decorator is not None:
            self._onDecoratorReleased()
            decorator.onStatusChanged -= self.__onDecoratorStatusChanged
        return

    def __attachToContent(self):
        content = self.content
        if content is not None:
            if content.viewStatus == ViewStatus.LOADED:
                self._onContentReady()
            content.onStatusChanged += self.__onContentStatusChanged
        return

    def __detachFromContent(self):
        content = self.content
        if content is not None:
            self._onContentReleased()
            content.onStatusChanged -= self.__onContentStatusChanged
        return

    def __onDecoratorStatusChanged(self, newStatus):
        if newStatus == ViewStatus.LOADED:
            self._onDecoratorReady()
        elif newStatus == ViewStatus.DESTROYED:
            self._onDecoratorReleased()
        return

    def __onContentStatusChanged(self, newStatus):
        if newStatus == ViewStatus.LOADED:
            self._onContentReady()
        elif newStatus == ViewStatus.DESTROYED:
            self._onContentReleased()
        return
