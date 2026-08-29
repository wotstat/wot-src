from gui.impl.pub import ViewImpl
from uilogging.crew.loggers import CrewPersonalCaseTabLogger

class BasePersonalCaseView(ViewImpl):
    __slots__ = (b'uiLogger',)

    def __init__(self, settings, **kwargs):
        self.uiLogger = CrewPersonalCaseTabLogger(self, kwargs.get(b'parentView'), settings.layoutID, kwargs.get(b'parentViewKey'))
        super(BasePersonalCaseView, self).__init__(settings)
        return

    def _onLoading(self, *args, **kwargs):
        self.uiLogger.initialize()
        super(BasePersonalCaseView, self)._onLoading(*args, **kwargs)
        return

    def _finalize(self):
        self.uiLogger.finalize()
        super(BasePersonalCaseView, self)._finalize()
        return
