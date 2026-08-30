import random, BigWorld
from PlayerEvents import g_playerEvents
from constants import QUEUE_TYPE
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.maps_training.maps_training_queue_model import MapsTrainingQueueModel
from gui.prb_control import prbEntityProperty
from helpers import dependency
from helpers.time_utils import getCurrentTimestamp
from skeletons.gui.game_control import IMapsTrainingController
from skeletons.gui.shared import IItemsCache
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, events
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.lobby.maps_training.maps_training_base_view import MapsTrainingBaseView

class MapsTrainingQueueView(MapsTrainingBaseView):
    __slots__ = (b'__timerCallback', b'__queueCallback', b'__createTime', b'__tipNum', b'__status')
    mapsTrainingController = dependency.descriptor(IMapsTrainingController)
    itemsCache = dependency.descriptor(IItemsCache)
    _REQUEST_QUEUE_INFO_TIMEOUT = 5
    _TIPS_OF_ALL = 21
    _QUEUE_INFO_PARAMS_COUNT = 2
    _WAIT_TIME_AVG = 15
    _WAIT_TIME_LONG = 180

    def __init__(self, *args, **kwargs):
        super(MapsTrainingQueueView, self).__init__(viewResource=R.views.mono.maps_training.maps_training_queue(), viewModel=MapsTrainingQueueModel())
        self.__timerCallback = None
        self.__queueCallback = None
        self.__createTime = kwargs[b'ctx'].get(b'createTime', getCurrentTimestamp())
        self.__tipNum = random.randint(1, self._TIPS_OF_ALL)
        self.__status = MapsTrainingQueueModel.DELAY_DEFAULT
        return

    @prbEntityProperty
    def prbEntity(self):
        return

    def _onLoading(self, *args, **kwargs):
        super(MapsTrainingQueueView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as model:
            model.setTime(b'0:00')
            model.setDescrTip(R.strings.maps_training.queue.tip.num(self.__tipNum)())
        self.__requestQueueInfo()
        return

    def _initialize(self, *args, **kwargs):
        super(MapsTrainingQueueView, self)._initialize(*args, **kwargs)
        self.__updateTimer()
        return

    def _finalize(self):
        self.__stopUpdateScreen()
        super(MapsTrainingQueueView, self)._finalize()
        return

    def _addListeners(self):
        super(MapsTrainingQueueView, self)._addListeners()
        self.viewModel.onQuit += self.__onQuitButtonClick
        self.viewModel.onMenu += self.__onMenu
        self.viewModel.onShowPrevTip += self.__onShowPrevTipClick
        self.viewModel.onShowNextTip += self.__onShowNextTipClick
        g_playerEvents.onArenaCreated += self.__onArenaCreated
        return

    def _removeListeners(self):
        super(MapsTrainingQueueView, self)._removeListeners()
        self.viewModel.onQuit -= self.__onQuitButtonClick
        self.viewModel.onMenu -= self.__onMenu
        self.viewModel.onShowPrevTip -= self.__onShowPrevTipClick
        self.viewModel.onShowNextTip -= self.__onShowNextTipClick
        g_playerEvents.onArenaCreated -= self.__onArenaCreated
        return

    def __requestQueueInfo(self):
        player = BigWorld.player()
        if player is not None and hasattr(player, b'requestQueueInfo'):
            player.requestQueueInfo(QUEUE_TYPE.MAPS_TRAINING)
            self.__queueCallback = BigWorld.callback(self._REQUEST_QUEUE_INFO_TIMEOUT, self.__requestQueueInfo)
        else:
            self.__queueCallback = None
        return

    def __updateTimer(self):
        self.__timerCallback = BigWorld.callback(1, self.__updateTimer)
        elapsedTime = getCurrentTimestamp() - self.__createTime
        if elapsedTime > self._WAIT_TIME_LONG:
            self.__status = MapsTrainingQueueModel.DELAY_LONG
        elif elapsedTime > self._WAIT_TIME_AVG:
            self.__status = MapsTrainingQueueModel.DELAY_NORMAL
        timeStr = b'%d:%02d'
        if self.__status != MapsTrainingQueueModel.DELAY_DEFAULT:
            timeStr += b'*'
        self.viewModel.setDelayStatus(self.__status)
        self.viewModel.setTime(timeStr % divmod(elapsedTime, 60))
        return

    def __onArenaCreated(self):
        self.__stopUpdateScreen()
        return

    def __stopUpdateScreen(self):
        if self.__timerCallback is not None:
            BigWorld.cancelCallback(self.__timerCallback)
            self.__timerCallback = None
        if self.__queueCallback is not None:
            BigWorld.cancelCallback(self.__queueCallback)
            self.__queueCallback = None
        return

    def __onQuitButtonClick(self):
        self.prbEntity.exitFromQueue()
        return

    @staticmethod
    def __onMenu():
        g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(VIEW_ALIAS.LOBBY_MENU)), scope=EVENT_BUS_SCOPE.LOBBY)
        return

    def __onShowPrevTipClick(self):
        self.__tipNum -= 1
        if self.__tipNum == 0:
            self.__tipNum = self._TIPS_OF_ALL
        self.viewModel.setDescrTip(R.strings.maps_training.queue.tip.num(self.__tipNum)())
        return

    def __onShowNextTipClick(self):
        self.__tipNum += 1
        if self.__tipNum > self._TIPS_OF_ALL:
            self.__tipNum = 1
        self.viewModel.setDescrTip(R.strings.maps_training.queue.tip.num(self.__tipNum)())
        return
