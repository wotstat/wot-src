from __future__ import absolute_import
import inspect, weakref, Keys
from Event import EventManager, Event
from debug_utils import LOG_WARNING
from gui import InputHandler
from gui.Scaleform.framework.entities.abstract.ContextMenuManagerMeta import ContextMenuManagerMeta
from soft_exception import SoftException
CM_BUY_COLOR = 13347959
_SEPARATOR_ID = b'separate'
_handlers = {}

def registerHandlers(*handlers):
    handlerTypes = []
    for item in handlers:
        if len(item) < 2:
            raise SoftException((b'Item {} is invalid').format(item))
        handlerType, handler = item[:2]
        if handlerType in _handlers:
            raise SoftException((b'Type of handler {} already exists').format(handlerType))
        if not inspect.isclass(handler) or AbstractContextMenuHandler not in inspect.getmro(handler):
            raise SoftException((b'Handler {} is invalid').format(handler))
        _handlers[handlerType] = handler
        handlerTypes.append(handlerType)

    return handlerTypes


def unregisterHandlers(*handlerTypes):
    for handlerType in handlerTypes:
        _handlers.pop(handlerType, None)

    return


def _getHandlerClass(handlerType):
    if handlerType in _handlers:
        return _handlers[handlerType]
    else:
        LOG_WARNING(b'Unknown context menu handler type', handlerType)
        return


class ContextMenuManager(ContextMenuManagerMeta):

    def __init__(self, app):
        super(ContextMenuManager, self).__init__()
        self.setEnvironment(app)
        self.onContextMenuHide = Event()
        self.__currentHandler = None
        return

    def getCurrentHandler(self):
        return self.__currentHandler

    def pyHide(self):
        self.as_hideS()
        return

    def show(self, menuType, args):
        self.as_showS(menuType, args)
        return

    def requestOptions(self, handlerType, ctx):
        clazz = _getHandlerClass(handlerType)
        if clazz is not None:
            self.__currentHandler = clazz(self, ctx)
            self.__currentHandler.onContextMenuHide += self.as_hideS
            InputHandler.g_instance.onKeyDown += self.__onKeyDown
            self._sendOptionsToFlash(self.__currentHandler.getOptions(ctx))
        return

    def onOptionSelect(self, optionId):
        if self.__currentHandler is not None:
            self.__currentHandler.onOptionSelect(optionId)
        return

    def onHide(self):
        if self.__isMenuActive():
            self.onContextMenuHide()
        self.__disposeHandler()
        return

    def _dispose(self):
        self.__app = None
        self.__disposeHandler()
        super(ContextMenuManager, self)._dispose()
        return

    def _sendOptionsToFlash(self, options):
        self.as_setOptionsS({b'options': options})
        return

    def _onOptionsChanged(self, options):
        self._sendOptionsToFlash(options)
        return

    def __disposeHandler(self):
        InputHandler.g_instance.onKeyDown -= self.__onKeyDown
        if self.__currentHandler is not None:
            self.__currentHandler.onContextMenuHide -= self.as_hideS
            self.__currentHandler.fini()
            self.__currentHandler = None
        return

    def __onKeyDown(self, event):
        if event.key == Keys.KEY_ESCAPE:
            self.pyHide()
        return

    def __isMenuActive(self):
        return self.__currentHandler is not None


class AbstractContextMenuHandler(object):

    def __init__(self, cmProxy, ctx=None, handlers=None):
        self._eManager = EventManager()
        self.onContextMenuHide = Event(self._eManager)
        super(AbstractContextMenuHandler, self).__init__()
        self.__cmProxy = weakref.proxy(cmProxy)
        self.__handlers = handlers or {}
        self._initFlashValues(ctx)
        return

    @property
    def app(self):
        return self.__cmProxy.app

    @property
    def cmProxy(self):
        return self.__cmProxy

    def fini(self):
        self._eManager.clear()
        self.__handlers = None
        self.__cmProxy = None
        self._clearFlashValues()
        return

    def getOptions(self, ctx=None):
        return self._generateOptions(ctx)

    def onOptionSelect(self, optionId):
        if optionId in self.__handlers:
            getattr(self, self.__handlers[optionId])()
            return
        LOG_WARNING(b'AbstractContextMenuHandler: unknown context menu option', self, self.__cmProxy, optionId)
        return

    def getCMInfo(self):
        return

    @classmethod
    def makeItem(cls, optId, optLabel=None, optInitData=None, optSubMenu=None, linkage=None, iconType=b''):
        return cls._makeItem(optId, optLabel=optLabel, optInitData=optInitData, optSubMenu=optSubMenu, linkage=linkage, iconType=iconType)

    def _dispatchChanges(self, options):
        if self.__cmProxy is not None:
            self.__cmProxy._onOptionsChanged(options)
        return

    @classmethod
    def _makeItem(cls, optId, optLabel=None, optInitData=None, optSubMenu=None, linkage=None, iconType=b''):
        return {b'id': optId, 
           b'label': optLabel, 
           b'iconType': iconType, 
           b'initData': (cls.__makeOptDataDefaults(optInitData)), 
           b'submenu': optSubMenu, 
           b'linkage': linkage}

    def _makeSeparator(self):
        return self._makeItem(_SEPARATOR_ID)

    def _generateOptions(self, ctx=None):
        raise NotImplementedError
        return

    def _initFlashValues(self, ctx):
        return

    def _clearFlashValues(self):
        return

    @staticmethod
    def __makeOptDataDefaults(optInitData):
        if optInitData is None:
            return {b'visible': True}
        else:
            if b'visible' not in optInitData or optInitData[b'visible'] is None:
                optInitData[b'visible'] = True
            return optInitData


class AbstractContextMenuCollectEventsHandler(AbstractContextMenuHandler):

    def onOptionSelect(self, optionId):
        handler = self._getContexMenuHandler()(optionId)
        if handler and callable(handler):
            handler(self)
            return
        LOG_WARNING(b'AbstractContextMenuCollectEventsHandler: unknown context menu option', self, self.cmProxy, optionId)
        return

    def _getContexMenuHandler(self):
        raise NotImplementedError
        return
