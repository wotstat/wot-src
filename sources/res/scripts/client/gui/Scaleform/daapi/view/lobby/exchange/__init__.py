from frameworks.wulf import WindowLayer
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from gui.shared.events import ShowDialogEvent
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.exchange.ConfirmExchangeDialog import ConfirmExchangeDialog
    from gui.Scaleform.daapi.view.lobby.exchange.ExchangeWindow import ExchangeWindow
    from gui.Scaleform.daapi.view.lobby.exchange.ExchangeXPWindow import ExchangeXPWindow
    from gui.Scaleform.daapi.view.lobby.exchange.detailed_exchange_xp_dialog import ExchangeXPWindowDialog
    return (
     GroupedViewSettings(VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG, ConfirmExchangeDialog, b'confirmExchangeDialog.swf', WindowLayer.WINDOW, b'confirmExchangeDialog', None, ScopeTemplates.LOBBY_SUB_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG_MODAL, ConfirmExchangeDialog, b'confirmExchangeDialog.swf', WindowLayer.TOP_WINDOW, b'confirmExchangeDialog', None, ScopeTemplates.LOBBY_SUB_SCOPE, isModal=True),
     GroupedViewSettings(VIEW_ALIAS.EXCHANGE_WINDOW, ExchangeWindow, b'exchangeWindow.swf', WindowLayer.WINDOW, b'exchangeWindow', None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.EXCHANGE_WINDOW_MODAL, ExchangeWindow, b'exchangeWindow.swf', WindowLayer.TOP_WINDOW, b'exchangeWindow', None, ScopeTemplates.DEFAULT_SCOPE, isModal=True, canDrag=False),
     GroupedViewSettings(VIEW_ALIAS.EXCHANGE_XP_WINDOW, ExchangeXPWindow, b'exchangeXPWindow.swf', WindowLayer.WINDOW, b'exchangeXPWindow', None, ScopeTemplates.DEFAULT_SCOPE),
     GroupedViewSettings(VIEW_ALIAS.EXCHANGE_XP_WINDOW_DIALOG_MODAL, ExchangeXPWindowDialog, b'exchangeXPWindow.swf', WindowLayer.TOP_WINDOW, b'exchangeXPWindow', None, ScopeTemplates.LOBBY_SUB_SCOPE, isModal=True),
     GroupedViewSettings(VIEW_ALIAS.CONFIRM_EXCHANGE_BERTHS_DIALOG, ConfirmExchangeDialog, b'confirmExchangeDialog.swf', WindowLayer.FULLSCREEN_WINDOW, b'confirmExchangeDialog', None, ScopeTemplates.LOBBY_SUB_SCOPE))


def getBusinessHandlers():
    return (
     _ExchangeDialogBusinessHandler(),
     _ExchangeViewsBusinessHandler(),
     _ExchangeDialogModalBusinessHandler(),
     _DetailedExchangeXPDialogBusinessHandler(),
     _ExchangeBerthsDialogBusinessHandler())


class _ExchangeDialogBusinessHandler(PackageBusinessHandler):
    _ALIAS = VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG
    _EVENT = ShowDialogEvent.SHOW_EXCHANGE_DIALOG
    _LAYER = WindowLayer.WINDOW

    def __init__(self):
        listeners = (
         (
          self._EVENT, self._exchangeDialogHandler),)
        super(_ExchangeDialogBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.DEFAULT)
        return

    def _exchangeDialogHandler(self, event):
        name = b'exchange' + event.meta.getType()
        self.__loadOrUpdateDialog(name, self._ALIAS, event.meta, event.handler)
        return

    def __loadOrUpdateDialog(self, name, alias, meta, handler):
        window = self.findViewByName(self._LAYER, name)
        if window is not None:
            window.updateDialog(meta, handler)
            self.bringViewToFront(name)
        else:
            self.loadViewWithDefName(alias, name, None, meta, handler)
        return


class _ExchangeDialogModalBusinessHandler(_ExchangeDialogBusinessHandler):
    _ALIAS = VIEW_ALIAS.CONFIRM_EXCHANGE_DIALOG_MODAL
    _EVENT = ShowDialogEvent.SHOW_EXCHANGE_DIALOG_MODAL
    _LAYER = WindowLayer.TOP_WINDOW


class _ExchangeViewsBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.EXCHANGE_WINDOW, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.EXCHANGE_WINDOW_MODAL, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.EXCHANGE_XP_WINDOW, self.loadViewByCtxEvent))
        super(_ExchangeViewsBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
        return


class _DetailedExchangeXPDialogBusinessHandler(_ExchangeDialogBusinessHandler):
    _ALIAS = VIEW_ALIAS.EXCHANGE_XP_WINDOW_DIALOG_MODAL
    _EVENT = ShowDialogEvent.SHOW_DETAILED_EXCHANGE_XP_DIALOG
    _LAYER = WindowLayer.TOP_WINDOW


class _ExchangeBerthsDialogBusinessHandler(_ExchangeDialogBusinessHandler):
    _ALIAS = VIEW_ALIAS.CONFIRM_EXCHANGE_BERTHS_DIALOG
    _EVENT = ShowDialogEvent.SHOW_EXCHANGE_BERTHS_DIALOG
    _LAYER = WindowLayer.FULLSCREEN_WINDOW

    def _exchangeDialogHandler(self, event):
        name = b'exchange' + event.meta.getType()
        window = self.findViewByName(self._LAYER, name)
        parent = event.parent if event.parent else None
        if window is not None:
            window.updateDialog(event.meta, event.handler)
            self.bringViewToFront(name)
        else:
            self.loadViewWithDefName(self._ALIAS, name, parent, event.meta, event.handler)
        return
