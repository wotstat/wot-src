from typing import TYPE_CHECKING
from uilogging.base.logger import MetricsLogger
from uilogging.dog_tags.logging_constants import FEATURE, MIN_VIEW_TIME, DogTagActions, DogTagAchievementStates, DogTagsViewKeys
from advanced_achievements_client.getters import getAchievementByID
from wotdecorators import noexcept
if TYPE_CHECKING:
    from typing import Optional
    from uilogging.types import ParentScreenType, ItemType, InfoType

class DogTagsMetricsLoger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(DogTagsMetricsLoger, self).__init__(FEATURE)
        return

    @noexcept
    def logClick(self, item, parentScreen=None, info=None):
        self.log(action=DogTagActions.CLICK, item=item, parentScreen=parentScreen, info=info)
        return

    @noexcept
    def onViewOpen(self, item, parentScreen=None, info=None):
        self.log(action=DogTagActions.DISPLAY, item=item, parentScreen=parentScreen, info=info)
        return


class DogTagsViewLogger(DogTagsMetricsLoger):
    __slots__ = (b'_parentScreen',)

    def __init__(self, parentScreen):
        super(DogTagsViewLogger, self).__init__()
        self._parentScreen = parentScreen
        return

    def logClick(self, item, parentScreen=None, info=None):
        super(DogTagsViewLogger, self).logClick(item, parentScreen if parentScreen else self._parentScreen, info)
        return

    def onViewOpen(self, item, parentScreen=None, info=None):
        super(DogTagsViewLogger, self).onViewOpen(item, parentScreen if parentScreen else self._parentViewKey, info)
        return


class AnimatedDogTagsViewLogger(DogTagsMetricsLoger):
    __slots__ = (b'_parentScreen',)

    def __init__(self, parentScreen):
        super(AnimatedDogTagsViewLogger, self).__init__()
        self._parentScreen = parentScreen
        return

    def logClick(self, item, parentScreen=None, info=None):
        super(AnimatedDogTagsViewLogger, self).logClick(item, parentScreen if parentScreen else self._parentScreen, info)
        return

    @noexcept
    def logClickAchievement(self, item, achievementId, category):
        progress = getAchievementByID(achievementId, category).getProgress().getAsPercent()
        info = self.__getStateInfo(progress)
        super(AnimatedDogTagsViewLogger, self).logClick(item, parentScreen=DogTagsViewKeys.ANIMATED_DOG_TAG, info=info)
        return

    def onViewOpen(self, item, parentScreen=None, info=None):
        super(AnimatedDogTagsViewLogger, self).onViewOpen(item, parentScreen if parentScreen else self._parentViewKey, info)
        return

    def __getStateInfo(self, progress):
        if progress == 0:
            return DogTagAchievementStates.NO_PROGRESS
        if progress == 100:
            return DogTagAchievementStates.COMPLETED
        return DogTagAchievementStates.IN_PROGRESS


class DogTagsTooltipLogger(DogTagsMetricsLoger):
    __slots__ = (b'_parentViewKey', b'_currentViewKey')

    def __init__(self, currentViewKey, parentScreen):
        super(DogTagsTooltipLogger, self).__init__()
        self._currentViewKey = currentViewKey
        self._parentViewKey = parentScreen
        return

    def viewOpened(self):
        self.startAction(DogTagActions.VIEWED)
        return

    def viewClosed(self, info=None):
        self.stopAction(action=DogTagActions.VIEWED, item=self._currentViewKey, parentScreen=self._parentViewKey, timeLimit=MIN_VIEW_TIME, info=info)
        return

    def reset(self):
        super(DogTagsTooltipLogger, self).reset()
        self._currentViewKey = None
        self._parentViewKey = None
        return
