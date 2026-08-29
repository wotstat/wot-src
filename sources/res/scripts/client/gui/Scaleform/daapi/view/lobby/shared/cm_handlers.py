import inspect
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.impl import backport
from gui.impl.gen import R

def _makeMenuLabel(label, data):
    return backport.text(R.strings.menu.cst_item_ctx_menu.dyn(data.pop(b'label', label))(), **data.pop(b'labelCtx', {}))


class CMLabel(object):
    INFORMATION = b'information'
    STATS = b'showVehicleStatistics'
    SELL = b'sell'
    REMOVE = b'remove'
    SALE_OPTION = b'saleOption'
    BUY = b'buy'
    BUY_MORE = b'buyMore'
    EXCHANGE = b'exchange'
    ADD_TO_COMPARE = b'addToCompare'
    SHOW_IN_HANGAR = b'showInHangar'
    PREVIEW = b'preview'
    RESTORE = b'restore'
    ACTIVATE = b'activate'
    PREVIEW_CUSTOMIZATION = b'previewCustomization'
    CONVERT_BLUEPRINT = b'convertBlueprint'
    CONVERT_BLUEPRINT_MAX = b'convertBlueprintMax'
    SHOW_BLUEPRINT = b'showBlueprint'
    NATION_CHANGE = b'nationChange'
    UPGRADE = b'upgrade'
    GO_TO_COLLECTION = b'goToCollection'
    DECONSTRUCT = b'deconstruct'


def option(order, label):

    def optionDecorator(method):

        def wrapper(self):
            method(self)
            return

        wrapper.cm = {b'order': order, b'label': label, 
           b'name': (method.__name__)}
        return wrapper

    return optionDecorator


class StorageOptionCustomData(object):

    def __init__(self, label, enabled=True, visible=True, isNew=False, textColor=None, labelCtx=None):
        self.label = label
        self.enabled = enabled
        self.visible = visible
        self.isNew = isNew
        self.textColor = textColor
        self.labelCtx = labelCtx
        return

    def asDict(self):
        return {key: value for key, value in inspect.getmembers(self, (lambda m: not inspect.ismethod(m))) if not (key.startswith(b'_') or key.startswith(b'__')) and value is not None}


class ContextMenu(AbstractContextMenuHandler):

    def __init__(self, cmProxy=None, ctx=None):
        self.__handlerMethods = sorted([method for method in (member.__func__ for _, member in inspect.getmembers(self, inspect.ismethod)) if getattr(method, b'cm', None) is not None], key=(lambda m: m.cm[b'order']))
        super(ContextMenu, self).__init__(cmProxy, ctx, {handler.cm[b'label']: handler.cm[b'name'] for handler in self.__handlerMethods})
        return

    def _initFlashValues(self, ctx):
        self._id = int(ctx.id)
        return

    def _generateOptions(self, ctx=None):
        return [self._makeOption(method.cm[b'label'], self._getOptionCustomData(method.cm[b'label']).asDict()) for method in self.__handlerMethods if self._isVisible(method.cm[b'label'])]

    def _makeOption(self, label, data):
        return self._makeItem(optId=label, optLabel=_makeMenuLabel(label, data), optInitData=data or None)

    def _getOptionCustomData(self, label):
        return StorageOptionCustomData(label)

    def _isVisible(self, label):
        return True
