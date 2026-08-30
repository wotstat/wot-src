import logging
from typing import TYPE_CHECKING
from uilogging.base.logger import MetricsLogger
from uilogging.constants import LogLevels
from uilogging.seniority_awards.constants import SeniorityAwardsLogActions, SeniorityAwardsLogKeys, SeniorityAwardsLogButtons, SeniorityAwardsLogSpaces, SeniorityAwardsFeatures
from wotdecorators import noexcept
if TYPE_CHECKING:
    from uilogging.types import ParentScreenType
_logger = logging.getLogger(__name__)

class SeniorityAwardsMetricsLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(SeniorityAwardsMetricsLogger, self).__init__(SeniorityAwardsFeatures.FEATURE)
        return


class VehicleSelectionErrorNotificationsLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(VehicleSelectionErrorNotificationsLogger, self).__init__(SeniorityAwardsFeatures.VEHICLE_SELECTION_FEATURE)
        return

    @noexcept
    def handleTimeoutError(self):
        self.log(action=SeniorityAwardsLogActions.DISPLAYED, item=SeniorityAwardsLogKeys.TIMEOUT_NOTIFICATION_ERROR, parentScreen=SeniorityAwardsLogSpaces.HANGAR, loglevel=LogLevels.WARNING)
        return

    @noexcept
    def handleMultipleTokensError(self):
        self.log(action=SeniorityAwardsLogActions.DISPLAYED, item=SeniorityAwardsLogKeys.MULTIPLE_TOKENS_NOTIFICATION_ERROR, parentScreen=SeniorityAwardsLogSpaces.HANGAR, loglevel=LogLevels.WARNING)
        return


class VehicleSelectionNotificationLogger(SeniorityAwardsMetricsLogger):
    __slots__ = ()

    @noexcept
    def handleClickAction(self):
        self.log(action=SeniorityAwardsLogActions.CLICK, item=SeniorityAwardsLogButtons.SELECT_BUTTON, parentScreen=SeniorityAwardsLogKeys.VEHICLE_SELECTION_NOTIFICATION, info=SeniorityAwardsLogSpaces.NOTIFICATION_CENTER)
        return

    @noexcept
    def handleDisplayedAction(self):
        self.log(action=SeniorityAwardsLogActions.DISPLAYED, item=SeniorityAwardsLogKeys.VEHICLE_SELECTION_NOTIFICATION, parentScreen=SeniorityAwardsLogSpaces.NOTIFICATION_CENTER)
        return


class RewardNotificationLogger(SeniorityAwardsMetricsLogger):
    __slots__ = ()

    @noexcept
    def handleClickAction(self, displaySpace):
        self.log(action=SeniorityAwardsLogActions.CLICK, item=SeniorityAwardsLogButtons.CLAIM_BUTTON, parentScreen=SeniorityAwardsLogKeys.REWARD_NOTIFICATION, info=displaySpace)
        return

    @noexcept
    def handleDisplayedAction(self, parentScreen, limitedUICompleted, isNeedBullet):
        additionalInfo = b''
        if not limitedUICompleted:
            additionalInfo += b'limited_ui'
        if isNeedBullet:
            additionalInfo += b';bullet' if additionalInfo else b'bullet'
        self.log(action=SeniorityAwardsLogActions.DISPLAYED, item=SeniorityAwardsLogKeys.REWARD_NOTIFICATION, parentScreen=parentScreen, info=additionalInfo or None)
        return


class CoinsNotificationLogger(SeniorityAwardsMetricsLogger):
    __slots__ = ()

    @noexcept
    def handleClickAction(self, displaySpace):
        self.log(action=SeniorityAwardsLogActions.CLICK, item=SeniorityAwardsLogButtons.SHOP_BUTTON, parentScreen=SeniorityAwardsLogKeys.COINS_NOTIFICATION, info=displaySpace)
        return

    @noexcept
    def handleDisplayedAction(self, parentScreen):
        self.log(action=SeniorityAwardsLogActions.DISPLAYED, item=SeniorityAwardsLogKeys.COINS_NOTIFICATION, parentScreen=parentScreen)
        return
