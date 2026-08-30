import logging
from account_helpers import AccountSettings
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.marathon.marathon_reward_view_model import MarathonRewardViewModel
from gui.impl.lobby.marathon.marathon_reward_sounds import MarathonVideos, onVideoStart, onVideoDone
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow
from gui.server_events.events_dispatcher import showMissionsMarathon
from gui.shared.event_dispatcher import selectVehicleInHangar
_logger = logging.getLogger(__name__)

class MarathonRewardView(ViewImpl):
    __slots__ = (b'__congratsSourceId', b'__videoShownKey')

    def __init__(self, *args, **kwargs):
        self.__congratsSourceId = 0
        self.__videoShownKey = b''
        settings = ViewSettings(R.views.lobby.marathon.marathon_reward_view.MarathonRewardView())
        settings.model = MarathonRewardViewModel()
        settings.args = args
        settings.kwargs = kwargs
        super(MarathonRewardView, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(MarathonRewardView, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        super(MarathonRewardView, self)._initialize()
        if args:
            specialRewardData = args[0]
            self.__congratsSourceId = specialRewardData.congratsSourceId
            self.__videoShownKey = specialRewardData.videoShownKey
            with self.viewModel.transaction() as model:
                model.setIsGoToVehicleBtnEnabled(specialRewardData.goToVehicleBtn)
                model.setVideoSource(specialRewardData.sourceName)
                model.setVehicleLvl(specialRewardData.vehicleLvl)
                model.setVehicleName(specialRewardData.vehicleName)
                model.setVehicleType(specialRewardData.vehicleType)
                model.setVehicleIsElite(specialRewardData.vehicleIsElite)
            self.viewModel.onGoToVehicleBtnClick += self.__onGoToVehicle
            self.viewModel.onViewRewardsBtnClick += self.__onViewRewards
            self.viewModel.onCloseBtnClick += self.__onCloseWindow
            self.viewModel.onVideoStarted += self.__onVideoStarted
            self.viewModel.onVideoStopped += self.__onVideoStopped
        else:
            _logger.error(b'__specialRewardData is not specified!')
            self.__onCloseWindow()
        return

    def _finalize(self):
        self.viewModel.onGoToVehicleBtnClick -= self.__onGoToVehicle
        self.viewModel.onViewRewardsBtnClick -= self.__onViewRewards
        self.viewModel.onCloseBtnClick -= self.__onCloseWindow
        self.viewModel.onVideoStarted -= self.__onVideoStarted
        self.viewModel.onVideoStopped -= self.__onVideoStopped
        onVideoDone()
        AccountSettings.setUIFlag(self.__videoShownKey, True)
        return

    def __onGoToVehicle(self, _=None):
        self.destroyWindow()
        selectVehicleInHangar(self.__congratsSourceId)
        return

    def __onViewRewards(self, _=None):
        showMissionsMarathon()
        self.destroyWindow()
        return

    def __onCloseWindow(self, _=None):
        self.destroyWindow()
        return

    def __onVideoStarted(self, _=None):
        onVideoStart(MarathonVideos.VEHICLE, self.viewModel.getVideoSource())
        return

    def __onVideoStopped(self, _=None):
        onVideoDone()
        return


class MarathonRewardViewWindow(LobbyWindow):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(MarathonRewardViewWindow, self).__init__(content=MarathonRewardView(*args, **kwargs), wndFlags=WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, decorator=None)
        return
