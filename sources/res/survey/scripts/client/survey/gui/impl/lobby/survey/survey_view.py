import BigWorld
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.impl.gen import R
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.shared.utils import getPlayerDatabaseID
from gui.shared.view_helpers.blur_manager import CachedBlur
from survey.gui.impl.gen.view_models.views.lobby.survey.survey_view_model import SurveyViewModel
from SurveyConstants import SURVEY_ANSWERS

class SurveyView(ViewImpl):
    __slots__ = (b'__arenaID', b'__timeout', b'__callbackID')

    def __init__(self, arenaID, timeout):
        self.__arenaID = arenaID
        self.__timeout = timeout
        self.__callbackID = None
        settings = ViewSettings(R.views.survey.lobby.survey.SurveyView())
        settings.model = SurveyViewModel()
        super(SurveyView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(SurveyView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(SurveyView, self)._initialize(*args, **kwargs)
        self.__callbackID = BigWorld.callback(self.__timeout, self.__surveyMissed)
        return

    def _finalize(self):
        self.__cancelCallback()
        super(SurveyView, self)._finalize()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onExit, self.__onWindowClose),
         (
          self.viewModel.onAccept, self.__onAccept))

    def __onWindowClose(self):
        self.__sendSurveyResult(SURVEY_ANSWERS.CANCELED)
        return

    def __onAccept(self, answer):
        self.__sendSurveyResult(answer[b'result'])
        return

    def __surveyMissed(self):
        self.__callbackID = None
        self.destroyWindow()
        return

    def __sendSurveyResult(self, result):
        self.__cancelCallback()
        dbID = getPlayerDatabaseID()
        if dbID != 0:
            BigWorld.player().AccountSurveyComponent.sendSurveyResult(dbID, self.__arenaID, result)
        self.destroyWindow()
        return

    def __cancelCallback(self):
        if self.__callbackID is not None:
            BigWorld.cancelCallback(self.__callbackID)
            self.__callbackID = None
        return


class SurveyViewWindow(LobbyWindow):
    __slots__ = (b'__blur',)

    def __init__(self, arenaID, timeout):
        super(SurveyViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=SurveyView(arenaID, timeout), layer=WindowLayer.OVERLAY)
        self.__blur = CachedBlur(enabled=True, ownLayer=self.layer)
        return

    def _finalize(self):
        self.__blur.fini()
        super(SurveyViewWindow, self)._finalize()
        return
