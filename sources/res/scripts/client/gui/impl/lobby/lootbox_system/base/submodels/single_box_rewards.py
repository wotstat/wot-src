import logging
from typing import TYPE_CHECKING
import Windowing
from gui.Scaleform.framework.entities.View import ViewKey
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.lobby_entry import getLobbyStateMachine
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.single_box_rewards_view_model import SingleBoxRewardsViewModel
from gui.impl.lobby.lootbox_system.base.common import SubViewImpl
from gui.impl.lobby.lootbox_system.base.submodels.common import updateAnimationState
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from gui.lootbox_system.base.bonuses_packers import packBonusModelAndTooltipData
from gui.lootbox_system.base.common import ViewID, Views
from gui.lootbox_system.base.decorators import createBackportTooltipDecorator, createTooltipContentDecorator
from gui.lootbox_system.base.sound import playVideoPauseSound, playVideoResumeSound
from gui.lootbox_system.base.utils import isShopVisible, openBoxes
from gui.lootbox_system.base.views_loaders import showItemPreview
from gui.server_events.bonuses import SimpleBonus
from gui.shared import EVENT_BUS_SCOPE, events
from helpers import dependency
from shared_utils import first
from skeletons.gui.game_control import ILootBoxSystemController
if TYPE_CHECKING:
    from typing import Dict, List
_logger = logging.getLogger(__name__)
_EXTRA_BONUSES_NAMES = (b'slots',)

class SingleBoxRewards(SubViewImpl):
    __lootBoxes = dependency.descriptor(ILootBoxSystemController)

    def __init__(self, viewModel, parentView):
        super(SingleBoxRewards, self).__init__(viewModel, parentView)
        self.__isReopen = False
        self.__category = b''
        self.__openCount = 0
        self.__bonuses = []
        self.__extraBonuses = []
        self.__tooltipItems = {}
        self.__isVideoPlaying = False
        self.__eventName = b''
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(SingleBoxRewards, self).createToolTip(event)

    @createTooltipContentDecorator()
    def createToolTipContent(self, event, contentID):
        return super(SingleBoxRewards, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        return self.__tooltipItems.get(event.getArgument(b'tooltipId', 0))

    def initialize(self, *args, **kwargs):
        super(SingleBoxRewards, self).initialize(*args, **kwargs)
        self.__isReopen = kwargs.get(b'isReopen', False)
        self.__category = kwargs.get(b'category', b'')
        self.__openCount = kwargs.get(b'count', 0)
        self.__updateBonusesData(first(kwargs.get(b'bonuses', []), []))
        self.__eventName = kwargs.get(b'eventName', b'')
        with self.viewModel.transaction() as vmTx:
            self.__setWindowAccessible(model=vmTx)
            self.__updateData(model=vmTx)
            self.__updateCounters(model=vmTx)
            self.__updateBonuses(model=vmTx)
            self.__updateAnimationState(model=vmTx)
        Windowing.addWindowAccessibilitynHandler(self.__onWindowAccessibilityChanged)
        return

    def finalize(self):
        Windowing.removeWindowAccessibilityHandler(self.__onWindowAccessibilityChanged)
        super(SingleBoxRewards, self).finalize()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onOpen, self.__openNext),
         (
          self.viewModel.onGoBack, self.__goBack),
         (
          self.viewModel.onPreview, self.__showPreview),
         (
          self.viewModel.onBuyBoxes, self.__openShop),
         (
          self.viewModel.onAnimationStateChanged, self.__updateAnimationState),
         (
          self.viewModel.onVideoPlaying, self.__setVideoPlaying),
         (
          self.viewModel.onClose, self.__goBack),
         (
          self.__lootBoxes.onBoxesCountChanged, self.__updateCounters),
         (
          self.__lootBoxes.onBoxesUpdated, self.__updateCounters))

    def __setVideoPlaying(self, ctx=None):
        isPlaying = ctx.get(b'isPlaying')
        self.__isVideoPlaying = isPlaying
        return

    def _getListeners(self):
        return (
         (
          events.LootBoxSystemEvent.OPENING_ERROR, self.__onErrorBack, EVENT_BUS_SCOPE.LOBBY),)

    @replaceNoneKwargsModel
    def __setWindowAccessible(self, model=None):
        isWindowAccessible = Windowing.isWindowAccessible()
        model.setIsWindowAccessible(isWindowAccessible)
        return

    def __onWindowAccessibilityChanged(self, _):
        isWindowAccessible = Windowing.isWindowAccessible()
        if self.__isVideoPlaying:
            self.__setWindowAccessible()
            if isWindowAccessible:
                playVideoResumeSound(self.__eventName)
            else:
                playVideoPauseSound(self.__eventName)
        return

    @replaceNoneKwargsModel
    def __updateData(self, model=None):
        model.setEventName(self.__eventName)
        model.setBoxCategory(self.__category)
        model.setIsReopen(self.__isReopen)
        model.setIsShopVisible(isShopVisible(self.__eventName))
        return

    @replaceNoneKwargsModel
    def __updateCounters(self, model=None):
        model.setBoxesCount(self.__lootBoxes.getBoxesCount(self.__eventName, self.__category))
        model.setBoxesCountToGuaranteed(self.__lootBoxes.getBoxesCountToGuaranteed(self.__category))
        return

    @replaceNoneKwargsModel
    def __updateBonuses(self, model=None):
        model.bonuses.clearItems()
        model.extraBonuses.clearItems()
        packBonusModelAndTooltipData(self.__bonuses, model.bonuses, tooltipData=self.__tooltipItems, merge=False, eventName=self.__eventName, showLootboxCompensation=True)
        packBonusModelAndTooltipData(self.__extraBonuses, model.extraBonuses, tooltipData=self.__tooltipItems, merge=False, eventName=self.__eventName)
        model.bonuses.invalidate()
        model.extraBonuses.invalidate()
        return

    @replaceNoneKwargsModel
    def __updateAnimationState(self, ctx=None, model=None):
        updateAnimationState(model, ctx, self.__eventName)
        return

    def __openNext(self, ctx=None):
        category = ctx.get(b'category') if ctx is not None else b''

        def processResult(bonuses):
            self.viewModel.setIsAwaitingResponse(False)
            self.viewModel.setBoxCategory(self.__category)
            self.__updateCounters()
            self.__updateBonusesData(first(bonuses))
            self.__updateBonuses()
            self.__updateStateContext(bonuses)
            return

        self.__isReopen = False
        self.viewModel.setIsAwaitingResponse(True)
        if category:
            self.__category = category
        openBoxes(self.__eventName, self.__category, self.__openCount, processResult)
        return

    def __goBack(self):
        Views.load(ViewID.MAIN, eventName=self.__eventName)
        return

    def __onErrorBack(self, *_):
        self.viewModel.setIsAwaitingResponse(False)
        Views.load(ViewID.MAIN, eventName=self.__eventName)
        return

    def __showPreview(self, ctx):
        showItemPreview(str(ctx.get(b'bonusType')), int(ctx.get(b'bonusId')), int(ctx.get(b'styleID')))
        return

    def __openShop(self):
        Views.load(ViewID.SHOP, eventName=self.__eventName)
        return

    def __updateBonusesData(self, bonuses):
        self.__extraBonuses = []
        if len(bonuses) == 1:
            self.__bonuses = bonuses
            return
        self.__bonuses = []
        for bonus in bonuses:
            if bonus.getName() in _EXTRA_BONUSES_NAMES:
                self.__extraBonuses.append(bonus)
            else:
                self.__bonuses.append(bonus)

        return

    def __updateStateContext(self, bonuses):
        lsm = getLobbyStateMachine()
        lsm.getStateByViewKey(ViewKey(VIEW_ALIAS.LOOT_BOXES_MAIN_VIEW)).updateCachedCtx({b'bonuses': bonuses})
        return
