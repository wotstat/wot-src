from frameworks.wulf import ViewFlags, ViewSettings, WindowFlags, WindowLayer
from gui.shared.view_helpers.blur_manager import CachedBlur
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.subscription.subscription_daily_quests_intro_model import SubscriptionDailyQuestsIntroModel
from gui.impl.pub import ViewImpl, WindowImpl
from account_helpers import AccountSettings
from account_helpers.AccountSettings import SUBSCRIPTION_DAILY_QUESTS_INTRO_SHOWN

class SubscriptionDailyQuestsIntro(ViewImpl):
    __slots__ = ()

    def __init__(self):
        settings = ViewSettings(R.views.lobby.subscription.SubscriptionDailyQuestsIntro())
        settings.flags = ViewFlags.LOBBY_TOP_SUB_VIEW
        settings.model = SubscriptionDailyQuestsIntroModel()
        super(SubscriptionDailyQuestsIntro, self).__init__(settings)
        return

    @property
    def viewModel(self):
        return super(SubscriptionDailyQuestsIntro, self).getViewModel()

    def _initialize(self, *args, **kwargs):
        AccountSettings.setSettings(SUBSCRIPTION_DAILY_QUESTS_INTRO_SHOWN, True)
        self.viewModel.onClose += self._onClose
        return

    def _finalize(self):
        self.viewModel.onClose -= self._onClose
        return

    def _onClose(self):
        self.destroyWindow()
        return


class SubscriptionDailyQuestsIntroWindow(WindowImpl):
    __slots__ = (b'__blur',)

    def __init__(self, parent=None):
        super(SubscriptionDailyQuestsIntroWindow, self).__init__(WindowFlags.WINDOW, content=SubscriptionDailyQuestsIntro(), parent=parent)
        self.__blur = CachedBlur(enabled=True, ownLayer=WindowLayer.TOP_SUB_VIEW)
        return

    def _finalize(self):
        self.__blur.fini()
        super(SubscriptionDailyQuestsIntroWindow, self)._finalize()
        return
