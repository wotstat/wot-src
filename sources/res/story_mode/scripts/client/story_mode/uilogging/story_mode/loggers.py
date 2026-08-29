import typing
from gui.game_loading import loading as gameLoading
from helpers import dependency
from story_mode.skeletons.story_mode_controller import IStoryModeController
from wotdecorators import noexcept
from uilogging.base.logger import MetricsLogger
from story_mode.uilogging.story_mode.consts import Features, LogActions, LogWindows, LogButtons, LogBattleResultStats
if typing.TYPE_CHECKING:
    from uilogging.types import ItemType, ItemStateType, InfoType

class BaseMetricsLogger(MetricsLogger):
    __slots__ = (b'_item',)
    _storyModeCtrl = dependency.descriptor(IStoryModeController)

    def __init__(self, item):
        feature = Features.ONBOARDING if self._storyModeCtrl.isOnboarding else Features.STORY_MODE
        super(BaseMetricsLogger, self).__init__(feature)
        self._item = item
        return


class WindowLogger(BaseMetricsLogger):
    __slots__ = (b'_isOpened',)

    def __init__(self, item):
        super(WindowLogger, self).__init__(item)
        self._isOpened = False
        return

    def logOpen(self, state=None, info=None):
        self.log(action=LogActions.OPEN, item=self._item, itemState=state, info=info)
        self._isOpened = True
        return

    def logClose(self):
        self.log(action=LogActions.CLOSE, item=self._item)
        self._isOpened = False
        return

    def logButtonShown(self, button, once=False):
        if self._isOpened:
            if once:
                self.logOnce(action=LogActions.SHOW, item=button, parentScreen=self._item)
            else:
                self.log(action=LogActions.SHOW, item=button, parentScreen=self._item)
        return

    def logClick(self, button, state=None):
        if self._isOpened:
            self.log(action=LogActions.CLICK, item=button, itemState=state, parentScreen=self._item)
        return


class WindowBehindGameLoadingLogger(WindowLogger):
    __slots__ = ()

    @noexcept
    def logGameLoadingClose(self):
        if self._isOpened and gameLoading.getLoader().isLoading:
            self.log(action=LogActions.GAME_LOADING_CLOSE, item=self._item)
        return


class MissionWindowLogger(WindowLogger):
    __slots__ = ()

    @noexcept
    def logOpen(self, missionId=None, info=None):
        super(MissionWindowLogger, self).logOpen(state=None if missionId is None else str(missionId), info=info)
        return


class PostBattleWindowLogger(MissionWindowLogger):
    __slots__ = ()

    def __init__(self):
        super(PostBattleWindowLogger, self).__init__(LogWindows.POST_BATTLE)
        return

    @noexcept
    def logOpen(self, missionId=None, win=False):
        result = LogBattleResultStats.WIN if win else LogBattleResultStats.LOST
        super(PostBattleWindowLogger, self).logOpen(missionId=missionId, info=result)
        return


class SelectMissionWindow(MissionWindowLogger):
    __slots__ = ()

    def __init__(self):
        super(SelectMissionWindow, self).__init__(LogWindows.MISSION_SELECTION)
        return

    @noexcept
    def logMissionSelectClick(self, missionId):
        self.logClick(LogButtons.SELECT, state=str(missionId))
        return

    @noexcept
    def logAutoSelect(self, missionId):
        if self._isOpened:
            self.log(LogActions.AUTO_SELECT, item=self._item, itemState=str(missionId))
        return


class SelectorCardLogger(BaseMetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(SelectorCardLogger, self).__init__(LogWindows.MODE_SELECTOR_CARD)
        return

    def logSelfClick(self):
        self.log(action=LogActions.CLICK, item=self._item)
        return

    def logInfoClick(self):
        self.log(action=LogActions.CLICK, item=LogButtons.INFO, parentScreen=self._item)
        return


class IntroVideoLogger(WindowLogger):
    __slots__ = ()

    def __init__(self):
        super(IntroVideoLogger, self).__init__(LogWindows.INTRO_VIDEO)
        return

    def logVideoStarted(self):
        if self._isOpened:
            self.log(LogActions.PLAY, item=self._item)
        return
