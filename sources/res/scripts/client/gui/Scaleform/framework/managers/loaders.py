from __future__ import absolute_import
import logging, typing
from future.utils import viewvalues
import BigWorld, Event, constants
from gui.Scaleform.framework import g_entitiesFactories, ViewSettings, ScopeTemplates
from gui.Scaleform.framework.entities.View import View, ViewKey
from gui.Scaleform.framework.entities.abstract.LoaderManagerMeta import LoaderManagerMeta
from gui.Scaleform.framework.entities.sf_window import SFWindow
from gui.Scaleform.framework.entities.view_impl_adaptor import ViewImplAdaptor
from gui.Scaleform.framework.entities.wulf_adapter import WulfPackageLayoutAdapter
from gui.Scaleform.framework.settings import UIFrameworkImpl
from gui.Scaleform.framework.view_overrider import ViewOverrider
from gui.impl.common.fade_manager import UseFading
from helpers import dependency, uniprof
from shared_utils import CONST_CONTAINER
from skeletons.gui.impl import IGuiLoader
from skeletons.tutorial import ITutorialLoader
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from frameworks.wulf import Window
    from gui.Scaleform.framework.ScopeTemplates import SimpleScope
_VIEW_REGION_COLOR = 3368601
_LOADING_VIEW_REGION_COLOR = 6710937
NO_IMPL_ALIAS = b'noImpl'
NO_IMPL_URL = b'development/noImpl.swf'
_logger = logging.getLogger(__name__)

class _LoadingItem(object):
    __slots__ = (b'loadParams', b'pyEntity', b'factoryIdx', b'args', b'kwargs', b'isCancelled', b'isModal', b'uid')

    def __init__(self, loadParams, uid, pyEntity, factoryIdx, isModal, args, kwargs):
        super(_LoadingItem, self).__init__()
        self.loadParams = loadParams
        self.pyEntity = pyEntity
        self.factoryIdx = factoryIdx
        self.args = args
        self.kwargs = kwargs
        self.isCancelled = False
        self.isModal = isModal
        self.uid = uid
        return

    def __repr__(self):
        return (b'{}[{}]=[loadParams={}, pyEntity={}]').format(self.__class__.__name__, hex(id(self)), self.loadParams, self.pyEntity)

    @property
    def name(self):
        return self.loadParams.viewKey.name

    @property
    def loadMode(self):
        return self.loadParams.loadMode


class ViewLoadMode(CONST_CONTAINER):
    DEFAULT = b'default'
    PRELOAD = b'preload'


class ViewLoadParams(object):
    __slots__ = (b'__viewKey', b'__loadMode', b'__parent')

    def __init__(self, viewKey, loadMode=ViewLoadMode.DEFAULT, parent=None):
        super(ViewLoadParams, self).__init__()
        self.__viewKey = viewKey
        self.__loadMode = loadMode
        self.__parent = parent
        return

    def __repr__(self):
        return (b'{}[viewKey={}, loadMode={}, parent={}]').format(self.__class__.__name__, self.__viewKey, self.loadMode, str(self.__parent))

    def __hash__(self):
        return hash((self.__viewKey, self.__loadMode, self.__parent))

    def __eq__(self, other):
        return isinstance(other, ViewLoadParams) and self.__viewKey == other.viewKey and self.__loadMode == other.loadMode and self.__parent == other.parent

    @property
    def uiImpl(self):
        return UIFrameworkImpl.UNDEFINED

    @property
    def viewKey(self):
        return self.__viewKey

    @property
    def loadMode(self):
        return self.__loadMode

    @property
    def parent(self):
        return self.__parent


class SFViewLoadParams(ViewLoadParams):
    __slots__ = (b'window',)

    def __init__(self, alias, name=None, loadMode=ViewLoadMode.DEFAULT, parent=None):
        super(SFViewLoadParams, self).__init__(ViewKey(alias, name), loadMode, parent)
        self.window = None
        return

    @property
    def uiImpl(self):
        return UIFrameworkImpl.SCALEFORM


class GuiImplViewLoadParams(ViewLoadParams):
    __slots__ = (b'__viewClass', b'__scope')

    def __init__(self, layoutID, viewClass, scope, parent=None):
        super(GuiImplViewLoadParams, self).__init__(ViewKey(layoutID, None), ViewLoadMode.DEFAULT, parent)
        self.__viewClass = viewClass
        self.__scope = scope
        return

    def __hash__(self):
        return hash((self.viewKey, self.loadMode, self.parent, self.__viewClass, self.__scope))

    def __eq__(self, other):
        return super(GuiImplViewLoadParams, self).__eq__(other) and self.__viewClass == other.viewClass and self.__scope == other.scope

    @property
    def uiImpl(self):
        return UIFrameworkImpl.GUI_IMPL

    @property
    def viewClass(self):
        return self.__viewClass

    @property
    def scope(self):
        return self.__scope


class LoaderManager(LoaderManagerMeta):
    uiLoader = dependency.descriptor(IGuiLoader)
    __tutorialLoader = dependency.descriptor(ITutorialLoader)

    def __init__(self, app):
        super(LoaderManager, self).__init__()
        self.__eManager = Event.EventManager()
        self.onViewLoadInit = Event.Event(self.__eManager)
        self.onViewLoaded = Event.Event(self.__eManager)
        self.onViewLoadError = Event.Event(self.__eManager)
        self.onViewLoadCanceled = Event.Event(self.__eManager)
        self.__app = app
        self.__loadingItems = {}
        return

    def __repr__(self):
        return (b'{}[{}]=[loadingItems=[{}]]').format(self.__class__.__name__, hex(id(self)), self.__loadingItems)

    def loadView(self, loadParams, *args, **kwargs):
        override = g_viewOverrider.getOverrideData(loadParams, *args, **kwargs)
        if override:
            self.cancelLoading(loadParams.viewKey)
            return self.__doLoadGuiImplView(override.loadParams, override.getFadeCtx(), *override.args, **override.kwargs)
        if loadParams.uiImpl == UIFrameworkImpl.GUI_IMPL:
            return self.__doLoadGuiImplView(loadParams, {}, *args, **kwargs)
        if loadParams.uiImpl == UIFrameworkImpl.SCALEFORM:
            return self.__doLoadSFView(loadParams, *args, **kwargs)
        raise SoftException((b'View can not be loaded. UI implementation "{}" is not handled').format(loadParams.uiImpl))
        return

    def cancelLoading(self, key):
        if key.name is None:
            _logger.error(b'View loading can not be canceled by key %r', key)
            return
        else:
            if key in self.__loadingItems:
                item = self.__loadingItems.pop(key)
                item.pyEntity.onDispose -= self.__handleViewDispose
                item.isCancelled = True
                self.as_cancelLoadViewS(key.name)
                self.onViewLoadCanceled(key, item)
                if item.uid != -1 and not isinstance(item.pyEntity, WulfPackageLayoutAdapter):
                    uniprof.exitFromRegion((b'Loading {} {}').format(key.name, item.uid))
                    BigWorld.notify(BigWorld.EventType.VIEW_LOADED, key.alias, item.uid, key.name)
                if not item.pyEntity.isDisposed():
                    item.pyEntity.destroy()
            return

    def getViewLoadingItem(self, key):
        return self.__loadingItems.get(key, None)

    def isViewLoading(self, key):
        return key in self.__loadingItems

    def viewLoaded(self, alias, viewName, view):
        viewKey = ViewKey(alias, viewName)
        if viewKey in self.__loadingItems:
            item = self.__loadingItems.pop(viewKey)
            uniprof.exitFromRegion((b'Loading {} {}').format(viewKey.name, item.uid))
            BigWorld.notify(BigWorld.EventType.VIEW_LOADED, viewKey.alias, item.uid, viewKey.name)
            if item.isCancelled or item.pyEntity.isDisposed():
                self.onViewLoadCanceled(viewKey, item)
            else:
                pyEntity = g_entitiesFactories.initialize(item.pyEntity, view, item.factoryIdx, extra={b'name': (item.name)})
                item.pyEntity.onDispose -= self.__handleViewDispose
                if pyEntity is not None:
                    pyEntity.getParentWindow().setViewLoaded()
                    self.onViewLoaded(pyEntity, item.loadParams)
                else:
                    msg = (b'An error occurred before view initialization. View {} will be destroyed.').format(item.pyEntity)
                    _logger.error(msg)
                    if not item.pyEntity.isDisposed():
                        item.pyEntity.destroy()
                    self.onViewLoadError(viewKey, msg, item)
        else:
            _logger.error(b'View loading for key has no associated data: %r', viewKey)
        return

    def viewLoadCanceled(self, alias, viewName):
        viewKey = ViewKey(alias, viewName)
        if viewKey in self.__loadingItems:
            _logger.warning(b'View loading for key %r has been canceled on FE side: %r.', viewKey, self.__loadingItems[viewKey])
            self.cancelLoading(viewKey)
        return

    def viewLoadError(self, alias, viewName, text):
        viewKey = ViewKey(alias, viewName)
        msg = (b'Error occurred during view {0} loading. Error:{1}').format(viewKey, text)
        _logger.error(msg)
        if viewKey in self.__loadingItems:
            item = self.__loadingItems.pop(viewKey)
            if item.isCancelled:
                self.onViewLoadCanceled(viewKey, item)
            else:
                self.onViewLoadError(viewKey, msg, item)
                if item is not None:
                    settings = item.pyEntity.settings
                    if constants.IS_DEVELOPMENT and settings.url != NO_IMPL_URL:
                        g_entitiesFactories.addSettings(ViewSettings(NO_IMPL_ALIAS, View, NO_IMPL_URL, settings.layer, None, ScopeTemplates.DEFAULT_SCOPE, False))
                        _logger.warning(b'Try to load noImpl swf...')
                        self.__doLoadSFView(SFViewLoadParams(NO_IMPL_ALIAS, item.name))
            uniprof.exitFromRegion((b'Loading {} {}').format(viewKey.name, item.uid))
            BigWorld.notify(BigWorld.EventType.VIEW_LOADED, viewKey.alias, item.uid, viewKey.name)
        else:
            _logger.warning(b'View loading for name has no associated data: %s', viewName)
        return

    def viewInitializationError(self, alias, viewName):
        viewKey = ViewKey(alias, viewName)
        msg = (b"View '{0}' does not implement net.wg.infrastructure.interfaces.IView").format(viewKey)
        _logger.error(msg)
        item = None
        if viewKey in self.__loadingItems:
            item = self.__loadingItems.pop(viewKey)
            pyEntity = item.pyEntity
            pyEntity.destroy()
            uniprof.exitFromRegion((b'Loading {} {}').format(viewKey.name, item.uid))
            BigWorld.notify(BigWorld.EventType.VIEW_LOADED, viewKey.alias, item.uid, viewKey.name)
        self.onViewLoadError(viewKey, msg, item)
        return

    def isModalViewLoading(self):
        for item in viewvalues(self.__loadingItems):
            if item.isModal:
                return True

        return False

    def _dispose(self):
        self.__app = None
        self.__loadingItems.clear()
        self.__eManager.clear()
        super(LoaderManager, self)._dispose()
        return

    def __handleViewDispose(self, view):
        self.cancelLoading(view.key)
        return

    def __handleViewLoaded(self, view):
        viewKey = view.key
        if viewKey not in self.__loadingItems:
            _logger.warning(b'View is already loaded or is not found: %r', viewKey)
            return
        item = self.__loadingItems.pop(viewKey)
        pyEntity = item.pyEntity
        pyEntity.onCreated -= self.__handleViewLoaded
        pyEntity.onDispose -= self.__handleViewDispose
        if item.isCancelled:
            self.onViewLoadCanceled(viewKey, item)
        else:
            self.onViewLoaded(pyEntity, item.loadParams)
        return

    def __doLoadSFView(self, loadParams, *args, **kwargs):
        key = loadParams.viewKey
        viewTutorialID = self.__tutorialLoader.gui.getViewTutorialID(key.name)
        window = loadParams.window
        if window is None:
            window = SFWindow(loadParams, fireEvent=False)
            window.load()
        uid = window.uniqueID
        name = (b'{} {}').format(key.name, uid)
        uniprof.enterToRegion(b'Scaleform ' + name, _VIEW_REGION_COLOR)
        BigWorld.notify(BigWorld.EventType.VIEW_CREATED, key.alias, uid, key.name)
        uniprof.enterToRegion(b'Loading ' + name, _LOADING_VIEW_REGION_COLOR)
        BigWorld.notify(BigWorld.EventType.LOADING_VIEW, key.alias, uid, key.name)
        pyEntity = None
        if key in self.__loadingItems:
            item = self.__loadingItems[key]
            item.isCancelled = False
            if not item.pyEntity.isDisposed():
                pyEntity = item.pyEntity
        if pyEntity is not None:
            pyEntity.onDispose += self.__handleViewDispose
            pyEntity.setParentWindow(window)
            window.setContent(pyEntity)
            viewDict = {b'config': (pyEntity.settings.getDAAPIObject()), 
               b'alias': (key.alias), 
               b'name': (key.name), 
               b'viewTutorialId': viewTutorialID}
            self.as_loadViewS(viewDict)
        else:
            pyEntity, factoryIdx = g_entitiesFactories.factory(key.alias, *args, **kwargs)
            if pyEntity is None:
                _logger.warning(b'PyEntity for alias %s is None', key.alias)
                window.destroy()
                uniprof.exitFromRegion(b'Loading ' + name)
                BigWorld.notify(BigWorld.EventType.LOAD_FAILED, key.alias, uid, key.name)
                uniprof.exitFromRegion(b'Scaleform ' + name)
                BigWorld.notify(BigWorld.EventType.VIEW_DESTROYED, key.alias, uid, key.name)
                return
            closeRegions = False
            pyEntity.setUniqueName(key.name)
            pyEntity.setEnvironment(self.__app)
            pyEntity.onDispose += self.__handleViewDispose
            if isinstance(pyEntity, WulfPackageLayoutAdapter):
                closeRegions = True
            pyEntity.setParentWindow(window)
            window.setContent(pyEntity)
            config = pyEntity.settings.getDAAPIObject()
            self.__loadingItems[key] = _LoadingItem(loadParams, uid, pyEntity, factoryIdx, args, kwargs, config.get(b'isModal', False))
            self.onViewLoadInit(pyEntity)
            if isinstance(pyEntity, WulfPackageLayoutAdapter):
                pyEntity.onWulfViewLoaded += self.__onWulfViewLoaded
                pyEntity.onWulfViewLoadError += self.__onWulfViewLoadError
                pyEntity.load()
            else:
                viewDict = {b'config': config, 
                   b'alias': (key.alias), 
                   b'name': (key.name), 
                   b'viewTutorialId': viewTutorialID}
                self.as_loadViewS(viewDict)
            if closeRegions:
                uniprof.exitFromRegion(b'Loading ' + name)
                BigWorld.notify(BigWorld.EventType.VIEW_LOADED, key.alias, uid, key.name)
                uniprof.exitFromRegion(b'Scaleform ' + name)
                BigWorld.notify(BigWorld.EventType.VIEW_DESTROYED, key.alias, uid, key.name)
        return pyEntity

    def __onWulfViewLoaded(self, pyEntity):
        pyEntity.onWulfViewLoaded -= self.__onWulfViewLoaded
        pyEntity.onWulfViewLoadError -= self.__onWulfViewLoadError
        viewKey = pyEntity.key
        if viewKey not in self.__loadingItems:
            _logger.error(b'View loading for key has no associated data: %r', viewKey)
            return
        else:
            item = self.__loadingItems.pop(viewKey)
            if item.isCancelled or item.pyEntity.isDisposed():
                self.onViewLoadCanceled(viewKey, item)
                return
            item.pyEntity.onDispose -= self.__handleViewDispose
            if pyEntity is not None:
                self.onViewLoaded(pyEntity, item.loadParams)
                return
            _logger.error(b'An error occurred before view initialization. View %r will be destroyed.', item.pyEntity)
            if not item.pyEntity.isDisposed():
                item.pyEntity.destroy()
            self.onViewLoadError(viewKey, b'An error occurred before view initialization', item)
            return

    def __onWulfViewLoadError(self, pyEntity):
        pyEntity.onWulfViewLoaded -= self.__onWulfViewLoaded
        pyEntity.onWulfViewLoadError -= self.__onWulfViewLoadError
        viewKey = pyEntity.key
        _logger.error(b'Error occurred during view %s loading.', viewKey)
        if viewKey not in self.__loadingItems:
            _logger.warning(b'View loading for name has no associated data: %s', viewKey.name)
            return
        item = self.__loadingItems.pop(viewKey)
        if item.isCancelled:
            self.onViewLoadCanceled(viewKey, item)
        else:
            self.onViewLoadError(viewKey, b'Error occurred during view loading', item)
        return

    def __doLoadGuiImplView(self, loadParams, fadeParams, *args, **kwargs):
        key = loadParams.viewKey
        if key in self.__loadingItems:
            raise SoftException((b'This case in not implemented: {}').format(loadParams))
        layoutID = loadParams.viewKey.alias
        viewClass = loadParams.viewClass
        scope = loadParams.scope
        parent = loadParams.parent
        view = viewClass(layoutID, *args, **kwargs)
        adaptor = ViewImplAdaptor()
        adaptor.setView(view, parent)
        adaptor.setCurrentScope(scope)
        if adaptor.isLoaded():
            raise SoftException((b'Synchronous loading does not supported: {}').format(loadParams))
        adaptor.onDispose += self.__handleViewDispose
        adaptor.onCreated += self.__handleViewLoaded
        self.__loadingItems[adaptor.key] = _LoadingItem(loadParams, -1, adaptor, -1, False, args, kwargs)
        self.onViewLoadInit(adaptor)
        if fadeParams:

            @UseFading(**fadeParams)
            def wrapper(adaptor):
                if adaptor.isWindowValid():
                    adaptor.loadView()
                return

            wrapper(adaptor)
        else:
            adaptor.loadView()
        return adaptor


g_viewOverrider = ViewOverrider()
