from constants import EMAIL_CONFIRMATION_QUEST_ID
from gui.impl.backport.backport_tooltip import createBackportTooltipContent
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.add_credentials_model import AddCredentialsModel
from gui.impl.gen.view_models.views.lobby.account_completion.tooltips.tooltip_constants import TooltipConstants
from gui.impl.lobby.account_completion.common import errors
from gui.impl.lobby.account_completion.common.base_wgnp_overlay_view import BaseWGNPOverlayView
from gui.impl.lobby.account_completion.common.field_presenters import EmailPresenter
from gui.impl.lobby.account_completion.utils.common import fillRewards, DISABLE_BUTTON_TIME
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
_WARNING_TIMEOUT = DISABLE_BUTTON_TIME

class BaseCredentialsOverlayView(BaseWGNPOverlayView):
    __slots__ = (b'_email', b'_tooltipItems')
    _REWARDS_TITLE = R.invalid()
    _eventsCache = dependency.descriptor(IEventsCache)
    _LAYOUT_DYN_ACCESSOR = R.views.lobby.account_completion.AddCredentialsView
    _VIEW_MODEL_CLASS = AddCredentialsModel

    def __init__(self):
        super(BaseCredentialsOverlayView, self).__init__()
        self._email = EmailPresenter(self.viewModel.email)
        self._tooltipItems = {}
        return

    @property
    def viewModel(self):
        return super(BaseCredentialsOverlayView, self).getViewModel()

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = event.getArgument(b'tooltipId')
            if tooltipId == TooltipConstants.REWARD:
                rewardTooltipID = event.getArgument(b'rewardTooltipID')
                if rewardTooltipID:
                    itemIndex = rewardTooltipID.split(b':').pop()
                    tooltipData = self._tooltipItems.get(itemIndex)
                    if tooltipData is not None:
                        return createBackportTooltipContent(tooltipData=tooltipData)
            return super(BaseCredentialsOverlayView, self).createToolTipContent(event, contentID)
        else:
            return

    def activate(self, initialEmail=b'', emailError=b'', *args, **kwargs):
        super(BaseCredentialsOverlayView, self).activate(*args, **kwargs)
        self._eventsCache.onSyncCompleted += self._onSyncCompleted
        self._email.onValueChanged += self._inputValueChangeHandler
        self._email.onFocusLost += self._inputFocusLostHandler
        with self.viewModel.transaction() as model:
            self._email.clear()
            self._email.setValue(initialEmail)
            if emailError:
                model.email.setErrorMessage(emailError)
        self._updateConfirmButtonAvailability()
        return

    def deactivate(self):
        self._eventsCache.onSyncCompleted -= self._onSyncCompleted
        self._email.onValueChanged -= self._inputValueChangeHandler
        self._email.onFocusLost -= self._inputFocusLostHandler
        super(BaseCredentialsOverlayView, self).deactivate()
        return

    def _onLoading(self, *args, **kwargs):
        super(BaseCredentialsOverlayView, self)._onLoading(*args, **kwargs)
        self._fillRewards(self.viewModel)
        self.viewModel.setQuestID(EMAIL_CONFIRMATION_QUEST_ID)
        self.viewModel.setRewardsTitle(self._REWARDS_TITLE)
        return

    def _doFinalize(self):
        self._email.dispose()
        self._tooltipItems = None
        super(BaseCredentialsOverlayView, self)._doFinalize()
        return

    def _inputValueChangeHandler(self):
        if not self.viewModel.getWarningCountdown():
            self._setWarning()
        self._updateConfirmButtonAvailability()
        return

    def _inputFocusLostHandler(self):
        self._updateConfirmButtonAvailability()
        return

    def _updateConfirmButtonAvailability(self):
        haveTimedWarning = self.viewModel.getWarningCountdown() and self.viewModel.getWarningText()
        self.viewModel.setIsConfirmEnabled(not haveTimedWarning and bool(self._email.value) and self._email.isValid)
        return

    def _fillRewards(self, model):
        self._tooltipItems.clear()
        fillRewards(model, tooltipItems=self._tooltipItems)
        return

    def _onSyncCompleted(self, *args):
        with self.viewModel.transaction() as model:
            self._fillRewards(model)
        return

    def _handleError(self, response):
        with self.viewModel.transaction() as model:
            emailErrorMessage = self._getEmailErrorMessage(response)
            if not emailErrorMessage:
                self._setWarning(errors.serverUnavailableTimed(), _WARNING_TIMEOUT)
            model.email.setErrorMessage(emailErrorMessage)
            model.email.setValue(self._email.value)
        return

    def _getEmailErrorMessage(self, response):
        return b''
