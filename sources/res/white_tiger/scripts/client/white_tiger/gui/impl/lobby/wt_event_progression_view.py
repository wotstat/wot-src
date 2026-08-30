import logging, typing
from frameworks.wulf import ViewFlags, ViewSettings, ViewEvent
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import HeaderMenuVisibilityState
from gui.Scaleform.Waiting import Waiting
from gui.impl.gen import R
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_progression_view_model import WtProgressionViewModel
from white_tiger.gui.impl.lobby import wt_event_sound
from white_tiger.gui.impl.lobby.tooltips.wt_event_lootbox_tooltip_view import WtEventLootBoxTooltipView
from white_tiger.gui.impl.lobby.tooltips.wt_event_stamp_tooltip_view import WtEventStampTooltipView
from white_tiger.gui.impl.lobby.tooltips.wt_event_ticket_tooltip_view import WtEventTicketTooltipView
from white_tiger.gui.impl.lobby.tooltips.main_prize_discount_tooltip_view import MainPrizeDiscountTooltipView
from white_tiger.gui.impl.lobby.wt_progression_view import WTProgressionView
from white_tiger.gui.impl.lobby.wt_quests_view import WTQuestsView
from gui.impl.pub import ViewImpl
from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.game_control import IWhiteTigerController
from white_tiger.gui.wt_event_helpers import backportTooltipDecorator
_logger = logging.getLogger(__name__)

class WTEventProgressionView(ViewImpl):
    __slots__ = (b'questContainer', b'__isGrowingAnimation', b'__fromWelcome', b'__ctx', b'__subviews')
    __gameEventController = dependency.descriptor(IWhiteTigerController)

    def __init__(self, *args, **kwargs):
        settings = ViewSettings(layoutID=R.views.white_tiger.lobby.ProgressionView(), flags=ViewFlags.LOBBY_TOP_SUB_VIEW, model=WtProgressionViewModel())
        settings.args = args
        settings.kwargs = kwargs
        super(WTEventProgressionView, self).__init__(settings)
        self.__isGrowingAnimation = False
        self.__fromWelcome = kwargs.get(b'fromWelcome', False)
        self.__ctx = kwargs.get(b'ctx', {})
        self.__subviews = []
        return

    @property
    def viewModel(self):
        return super(WTEventProgressionView, self).getViewModel()

    @property
    def _tooltipItems(self):
        items = {}
        for subview in self.__subviews:
            subviewItems = subview.getTooltipItems()
            items.update(subviewItems)

        return items

    @backportTooltipDecorator()
    def createToolTip(self, event):
        return super(WTEventProgressionView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.white_tiger.lobby.tooltips.LootBoxTooltipView():
            return WtEventLootBoxTooltipView(isHunterLootBox=event.getArgument(b'isHunterLootBox'))
        if contentID == R.views.white_tiger.lobby.tooltips.TicketTooltipView():
            return WtEventTicketTooltipView()
        if contentID == R.views.white_tiger.lobby.tooltips.StampTooltipView():
            return WtEventStampTooltipView()
        if contentID == R.views.white_tiger.lobby.tooltips.MainPrizeDiscountTooltipView():
            discount = int(event.getArgument(b'discount'))
            return MainPrizeDiscountTooltipView(discount=discount)
        return super(WTEventProgressionView, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        for subview in self.__subviews:
            tooltipData = subview.getTooltipData(event)
            if tooltipData:
                return tooltipData

        return

    def _onLoading(self, *args, **kwargs):
        if self.__fromWelcome:
            Waiting.show(b'loadContent')
        super(WTEventProgressionView, self)._onLoading()
        self.__subviews.append(WTProgressionView(self.viewModel.progression, self))
        self.__subviews.append(WTQuestsView(self.viewModel.dailyQuests, self))
        for subview in self.__subviews:
            subview.initialize(**self.__ctx)

        self._updateModel()
        self.__addListeners()
        return

    def _updateModel(self):
        self.viewModel.setIsOutroVideoAvailable(self.__gameEventController.isOutroVideoAvailable())
        return

    def _onLoaded(self, *args, **kwargs):
        super(WTEventProgressionView, self)._onLoaded(*args, **kwargs)
        if self.__fromWelcome:
            Waiting.hide(b'loadContent')
        wt_event_sound.playProgressionViewEnter()
        g_eventBus.handleEvent(events.LobbyHeaderMenuEvent(events.LobbyHeaderMenuEvent.TOGGLE_VISIBILITY, ctx={b'state': (HeaderMenuVisibilityState.NOTHING)}), EVENT_BUS_SCOPE.LOBBY)
        return

    def _finalize(self):
        self.__removeListeners()
        for subview in self.__subviews:
            subview.finalize()
            subview.clear()

        self.__subviews = None
        wt_event_sound.playProgressionViewExit()
        if self.__isGrowingAnimation:
            wt_event_sound.playProgressBarGrowing(False)
        g_eventBus.handleEvent(events.LobbyHeaderMenuEvent(events.LobbyHeaderMenuEvent.TOGGLE_VISIBILITY, ctx={b'state': (HeaderMenuVisibilityState.ALL)}), EVENT_BUS_SCOPE.LOBBY)
        super(WTEventProgressionView, self)._finalize()
        return

    def __addListeners(self):
        self.viewModel.onClose += self.__onCloseHandler
        self.viewModel.onIntroVideoClicked += self.__onIntroVideoClicked
        self.viewModel.onOutroVideoClicked += self.__onOutroVideoClicked
        self.__gameEventController.onEventPrbChanged += self.__onEventPrbChanged
        return

    def __removeListeners(self):
        self.viewModel.onClose -= self.__onCloseHandler
        self.viewModel.onIntroVideoClicked -= self.__onIntroVideoClicked
        self.viewModel.onOutroVideoClicked -= self.__onOutroVideoClicked
        self.__gameEventController.onEventPrbChanged -= self.__onEventPrbChanged
        return

    def __onEventPrbChanged(self, isActive):
        if not isActive:
            self.destroyWindow()
        return

    def __onCloseHandler(self):
        self.destroyWindow()
        return

    def __onIntroVideoClicked(self):
        self.__gameEventController.showIntroVideo()
        return

    def __onOutroVideoClicked(self):
        self.__gameEventController.showOutroVideo()
        return
