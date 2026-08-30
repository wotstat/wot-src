import BigWorld
from gui import GUI_SETTINGS
from gui.DialogsInterface import showDialog
from gui.Scaleform.daapi.view.dialogs import SimpleDialogMeta, I18nConfirmDialogButtons, DIALOG_BUTTON_ID
from helpers import aop
from helpers.i18n import makeString as _ms

class _PrepareLibrariesListAspect(aop.Aspect):

    def atReturn(self, cd):
        original_return_value = list(cd.returned)
        original_return_value.append(b'miniClient.swf')
        cd.change()
        return original_return_value


class PrepareLibrariesListPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.lobby_entry', b'LobbyEntry', b'_getRequiredLibraries', aspects=(
         _PrepareLibrariesListAspect,))
        return


class _OnHyperlinkClickAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        _show_continue_client_download_dialog()
        return


class _OnBrowserHyperlinkClickAspect(aop.Aspect):

    def atCall(self, cd):
        if cd.args[0] == _getContinueDownloadUrl():
            cd.avoid()
            _show_continue_client_download_dialog()
            return True
        return


class _OnFailLoadingFrameAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        if cd.args[1] and cd.args[4] == _getContinueDownloadUrl():
            cd.self.onLoadEnd(True)
        return


class OnHyperlinkClickPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.meta.MiniClientComponentMeta', b'MiniClientComponentMeta', b'onHyperlinkClick', aspects=(
         _OnHyperlinkClickAspect,))
        return


class OnSquadHyperlinkClickPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.prb_windows.SquadPromoWindow', b'SquadPromoWindow', b'onHyperlinkClick', aspects=(
         _OnHyperlinkClickAspect,))
        return


class OnBrowserHyperlinkClickPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'MTWebBrowser', b'EventListener', b'onFilterNavigation', aspects=(
         _OnBrowserHyperlinkClickAspect,))
        return


class OnFailLoadingFramePointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'MTWebBrowser', b'EventListener', b'onFailLoadingFrame', aspects=(
         _OnFailLoadingFrameAspect,))
        return


def _show_continue_client_download_dialog():
    showDialog(SimpleDialogMeta(title=_ms(b'#miniclient:continue_download_dialog/title'), message=_ms(b'#miniclient:continue_download_dialog/message'), buttons=I18nConfirmDialogButtons(focusedIndex=DIALOG_BUTTON_ID.SUBMIT, i18nKey=b'questsConfirmDialog')), (lambda proceed: BigWorld.quitAndStartLauncher() if proceed else None))
    return


def _getContinueDownloadUrl():
    return GUI_SETTINGS.baseUrls[b'webBridgeRootURL'] + b'/wot_client_url/'
