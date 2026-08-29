from gui.impl.dialogs.dialog_template import DialogTemplateView
from gui.impl.lobby.crew.crew_sounds import CREW_SOUND_OVERLAY_SPACE
from gui.impl.pub.dialog_window import DialogButtons
from uilogging.crew.loggers import CrewDialogLogger
from uilogging.crew.logging_constants import CrewNavigationButtons

class BaseCrewDialogTemplateView(DialogTemplateView):
    __slots__ = (b'_isClosed', b'_uiLogger')
    _COMMON_SOUND_SPACE = CREW_SOUND_OVERLAY_SPACE

    def __init__(self, layoutID=None, uniqueID=None, *args, **kwargs):
        super(BaseCrewDialogTemplateView, self).__init__(layoutID, uniqueID, *args, **kwargs)
        self._isClosed = False
        self._uiLogger = CrewDialogLogger(self, kwargs.get(b'loggingKey'), kwargs.get(b'parentViewKey'), kwargs.get(b'loggingAdditionalInfo'))
        return

    def _onLoading(self, *args, **kwargs):
        self._uiLogger.initialize()
        super(BaseCrewDialogTemplateView, self)._onLoading(*args, **kwargs)
        return

    def _finalize(self):
        self._uiLogger.finalize()
        super(BaseCrewDialogTemplateView, self)._finalize()
        return

    def _closeClickHandler(self, args=None):
        self._isClosed = True
        self._uiLogger.logClose(args.get(b'reason') if isinstance(args, dict) else None)
        super(BaseCrewDialogTemplateView, self)._closeClickHandler(args)
        return

    def _setResult(self, result):
        if result == DialogButtons.SUBMIT:
            self._uiLogger.logNavigationButtonClick(CrewNavigationButtons.SUBMIT)
        elif result == DialogButtons.CANCEL and not self._isClosed:
            self._uiLogger.logNavigationButtonClick(CrewNavigationButtons.CANCEL)
        super(BaseCrewDialogTemplateView, self)._setResult(result)
        return
