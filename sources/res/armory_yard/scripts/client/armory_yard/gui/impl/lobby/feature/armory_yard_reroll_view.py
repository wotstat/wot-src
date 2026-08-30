import logging
from functools import partial
from adisp import adisp_process
from account_helpers import AccountSettings
from account_helpers.AccountSettings import ArmoryYard
from armory_yard.gui.impl.lobby.feature.tooltips.task_condition_tooltip_view import TaskConditionTooltipView
from shared_utils import first
from armory_yard_constants import POST_PROGRESSION_GROUP_PREFIX
from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer, ViewModel, ViewStatus
from gui.impl import backport
from gui.impl.backport.backport_tooltip import createBackportTooltipContent
from gui.impl.dialogs.dialog_template_utils import getCurrencyTooltipAlias
from gui.impl.dialogs.dialog_template_tooltip import DialogTemplateTooltip
from gui.impl.dialogs.sub_views.top_right.money_balance import NO_WGM_TOOLTIP_DATA
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyType
from gui.impl.gui_decorators import args2params
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub.tooltip_window import SimpleTooltipContent
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder
from gui.shared.money import Currency
from armory_yard.uilogging.armory_yard.loggers import ArmoryYardLogger
from armory_yard.gui.shared.models_helpers import updateArmoryConditionQuestsModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_reroll_view_model import ArmoryYardRerollViewModel
from armory_yard.gui.impl.gen.view_models.views.lobby.feature.armory_yard_quest_sub_model import ArmoryYardQuestSubModel, QuestStatus
from armory_yard.gui.impl.lobby.feature.tooltips.armory_yard_currency_tooltip_view import ArmoryYardCurrencyTooltipView
from armory_yard.skeletons.armory_yard_reroll_controller import IArmoryYardRerollController
from armory_yard_constants import getConditionToken, State
from gui.impl.pub import WindowImpl, ViewImpl
from helpers import dependency
from skeletons.gui.game_control import IArmoryYardController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

def setIntroViewed():
    AccountSettings.setArmoryYard(ArmoryYard.ARMORY_YARD_REROLL_INTRO_VIEWED, True)
    return


def getIntroViewed():
    return AccountSettings.getArmoryYard(ArmoryYard.ARMORY_YARD_REROLL_INTRO_VIEWED)


def getLastCurrencyForReroll():
    return AccountSettings.getArmoryYard(ArmoryYard.ARMORY_YARD_REROLL_LAST_CURRENCY)


def setLastCurrencyForReroll(currency):
    AccountSettings.setArmoryYard(ArmoryYard.ARMORY_YARD_REROLL_LAST_CURRENCY, currency)
    return


def tooltipsModelsMap(model):
    return {(CurrencyType.GOLD): (DialogTemplateTooltip(viewModel=model.goldTooltip)), 
       (CurrencyType.CREDITS): (DialogTemplateTooltip(viewModel=model.creditsTooltip)), 
       (CurrencyType.CRYSTAL): (DialogTemplateTooltip(viewModel=model.crystalsTooltip)), 
       (CurrencyType.FREEXP): (DialogTemplateTooltip(viewModel=model.freeExpTooltip))}


def wgmAvailableTooltipFactory(currency):
    return createBackportTooltipContent(isSpecial=True, specialAlias=getCurrencyTooltipAlias(currency.value))


def wgmNotAvailableTooltipFactory(currency):
    params = NO_WGM_TOOLTIP_DATA.get(currency, {b'header': b'', b'body': b''})
    return SimpleTooltipContent(R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent(), header=backport.text(params[b'header']), body=backport.text(params[b'body']))


class ArmoryYardRerollView(ViewImpl):
    __slots__ = (b'__currentQuests', b'__tooltipData', b'__questsToSelect', b'__onLoadedCallback', b'__moneyBalanceTooltips', b'__uiLogger')
    __armoryYardCtrl = dependency.descriptor(IArmoryYardController)
    __eventsCache = dependency.descriptor(IEventsCache)
    __itemsCache = dependency.descriptor(IItemsCache)
    __rerollController = dependency.descriptor(IArmoryYardRerollController)

    def __init__(self, layoutID, quests, questsToSelect=None, onLoadedCallback=None):
        settings = ViewSettings(layoutID)
        settings.model = ArmoryYardRerollViewModel()
        super(ArmoryYardRerollView, self).__init__(settings)
        self.__currentQuests = quests
        self.__tooltipData = {}
        self.__questsToSelect = questsToSelect or []
        self.__onLoadedCallback = onLoadedCallback
        self.__uiLogger = ArmoryYardLogger()
        self.__moneyBalanceTooltips = self._initTooltips()
        return

    @property
    def viewModel(self):
        return super(ArmoryYardRerollView, self).getViewModel()

    def _getCallbacks(self):
        return (
         (
          b'stats', self.__onStatsChanged),)

    def _onLoading(self, *args, **kwargs):
        super(ArmoryYardRerollView, self)._onLoading(*args, **kwargs)
        self._update()
        self.__setStats(self.viewModel)
        self.__setLastCurrencyPrice()
        return

    def _onLoaded(self, *args, **kwargs):
        super(ArmoryYardRerollView, self)._onLoaded(*args, **kwargs)
        if self.__onLoadedCallback is not None:
            self.__onLoadedCallback()
        parentView = self.getParentWindowContent()
        if parentView:
            parentView.setHoldClose()
        return

    def _finalize(self):
        self.__currentQuests = {}
        self.__tooltipData = {}
        self.__questsToSelect = []
        self.__onLoadedCallback = None
        for tooltip in self.__moneyBalanceTooltips.values():
            tooltip.dispose()

        super(ArmoryYardRerollView, self)._finalize()
        return

    def _initTooltips(self):
        model = self.viewModel.moneyBalance
        currenciesList = self.__rerollController.getRerollCurrencies()
        return {CurrencyType(currency): tooltipsModelsMap(model)[CurrencyType(currency)] for currency in currenciesList}

    def __setStats(self, model):
        isWGMAvailable = self.__itemsCache.items.stats.mayConsumeWalletResources
        self._updateMoneyBalanceModel(model.moneyBalance)
        for currency, tooltip in self.__moneyBalanceTooltips.items():
            tooltip.isBackportTooltip = isWGMAvailable
            tooltip.tooltipFactory = partial(wgmAvailableTooltipFactory if isWGMAvailable else wgmNotAvailableTooltipFactory, currency)

        return

    def _updateMoneyBalanceModel(self, model):
        isWGMAvailable = self.__itemsCache.items.stats.mayConsumeWalletResources
        model.setIsWGMAvailable(isWGMAvailable)
        currenciesList = self.__rerollController.getRerollCurrencies()
        if Currency.CREDITS in currenciesList:
            model.setCredits(int(self.__itemsCache.items.stats.money.getSignValue(Currency.CREDITS)))
        if Currency.GOLD in currenciesList:
            model.setGold(int(self.__itemsCache.items.stats.money.getSignValue(Currency.GOLD)))
        if Currency.CRYSTAL in currenciesList:
            model.setCrystals(int(self.__itemsCache.items.stats.money.getSignValue(Currency.CRYSTAL)))
        if Currency.FREE_XP in currenciesList:
            model.setFreeExp(self.__itemsCache.items.stats.freeXP)
        return

    def _getEvents(self):
        return ((self.__armoryYardCtrl.serverSettings.onUpdated, self.__onUpdate),
         (
          self.__armoryYardCtrl.serverSettings.seasonProvider.onUpdated, self.__onUpdate),
         (
          self.__rerollController.onFreeRerollTokensUpdated, self.__onFreeRerollTokensUpdated),
         (
          self.__rerollController.onQuestConditionUpdated, self.__onUpdate),
         (
          self.__rerollController.onQuestConditionsReset, self.__onUpdate),
         (
          self.__eventsCache.onSyncCompleted, self.__onUpdate),
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onConfirm, self.__onConfirm),
         (
          self.viewModel.onReroll, self.__onReroll))

    def _update(self):
        with self.viewModel.transaction() as vm:
            vm.setIsIntroScreenVisited(getIntroViewed())
            vm.setIsPostProgression(self.__armoryYardCtrl.isPostProgressionState)
            vm.setIsPostProgressionFinished(self.__armoryYardCtrl.isFinalQuestCompleted)
            self.__currentQuests = self.getUpdatedCurrentQuests()
            questSubModel = vm.currentQuest
            if self.__currentQuests:
                questID = first(self.__currentQuests).getTokenQuestID()
                vm.setIsPostProgressionQuest(questID.startswith(POST_PROGRESSION_GROUP_PREFIX))
                self.__updateQuestModel(questSubModel, self.__currentQuests, first(self.__currentQuests).getMainID())
                self.__updateProgressionTime(vm)
                self.__updatePrices(vm)
                if self.__questsToSelect:
                    self.__fillSuggestedQuests(self.__questsToSelect)
        if not getIntroViewed():
            setIntroViewed()
        return

    def getUpdatedCurrentQuests(self):
        currentQuests = []
        for quest in self.__currentQuests:
            newQuest = self.__eventsCache.getQuestByID(quest.getID())
            if newQuest:
                currentQuests.append(newQuest)

        return currentQuests

    def __onFreeRerollTokensUpdated(self):
        self.viewModel.setFreeRerollCount(self.__rerollController.getFreeRerollsCount(first(self.__currentQuests).getGroupID()))
        return

    def __updatePrices(self, vm):
        vm.setFreeRerollCount(self.__rerollController.getFreeRerollsCount(first(self.__currentQuests).getGroupID()))
        vm.setRerollCountdown(self.__rerollController.getFreeRerollCountdown())
        BuyPriceModelBuilder.clearPriceModel(vm.price)
        BuyPriceModelBuilder.fillPriceModel(vm.price, self.__rerollController.getRerollPrices(), checkBalanceAvailability=True)
        return

    def __updateQuestModel(self, questSubModel, quests, conditionQuestID):
        questsModel = questSubModel.getQuests()
        questsModel.clear()
        questsCompleted, tokenQuestID = updateArmoryConditionQuestsModel(questsModel, quests, self.__tooltipData, 0, not self.__armoryYardCtrl.isPostProgressionState)
        questsModel.invalidate()
        questSubModel.setTokenQuestID(tokenQuestID or first(self.__currentQuests).getTokenQuestID())
        questSubModel.setConditionID(conditionQuestID)
        if self.__armoryYardCtrl.getState() == State.PURCHASESTAGE:
            questSubModel.setStatus(QuestStatus.LOCKED)
        elif questsCompleted:
            questSubModel.setStatus(QuestStatus.DONE)
        else:
            questSubModel.setStatus(QuestStatus.ACTIVE)
        return

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(ArmoryYardRerollView, self).createToolTip(event)

    def createToolTipContent(self, event, contentID):
        if contentID == R.views.armory_yard.lobby.feature.tooltips.ArmoryYardCurrencyTooltipView():
            return ArmoryYardCurrencyTooltipView(event.getArgument(b'currency'))
        else:
            if contentID == R.views.dialogs.common.DialogTemplateGenericTooltip():
                currency = event.getArgument(b'currency')
                factory = self.__moneyBalanceTooltips.get(CurrencyType(currency))
                if factory and factory.tooltipFactory is not None:
                    return factory.tooltipFactory()
            if contentID == R.views.armory_yard.lobby.feature.tooltips.RerollDescriptionTooltipView():
                return ViewImpl(ViewSettings(contentID, model=ViewModel()))
            if contentID == R.views.armory_yard.lobby.feature.tooltips.TaskConditionTooltipView():
                return TaskConditionTooltipView(event.getArgument(b'vehicleLevels'), event.getArgument(b'vehicleTypes'), event.getArgument(b'battleTypes'), event.getArgument(b'vehicleNations'))
            return super(ArmoryYardRerollView, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipData.get(int(tooltipId))

    def getParentWindowContent(self):
        if self.getParentWindow():
            return self.getParentWindow().parent.content
        return

    def __closeView(self):
        parentView = self.getParentWindowContent()
        if parentView:
            parentView.unHoldClose()
        self.destroyWindow()
        return

    def __onClose(self):
        replacedTokenQuestID = self.__rerollController.getReplacedTokenQuestID()
        if replacedTokenQuestID is not None and self.__currentQuests and replacedTokenQuestID == first(self.__currentQuests).getTokenQuestID():
            _logger.error(b'User must accept reroll')
        else:
            self.__closeView()
        return

    @adisp_process
    @args2params(int)
    def __onConfirm(self, conditionQuestID):
        if self.__currentQuests:
            questID = first(self.__currentQuests).getTokenQuestID()
            result = yield self.__rerollController.acceptReroll(conditionQuestID, questID)
            if not result:
                _logger.error(b'Cannot accept reroll')
            if self.viewStatus not in (ViewStatus.DESTROYING, ViewStatus.DESTROYED):
                self.__closeView()
        return

    @adisp_process
    @args2params(str)
    def __onReroll(self, currency):
        result = False
        questSnapshot = self.__uiLogger.getQuestSnapshot(self.viewModel.currentQuest)
        tokenQuestID = first(self.__currentQuests).getTokenQuestID()
        if self.__rerollController.getFreeRerollsCount(first(self.__currentQuests).getGroupID()) > 0:
            result = yield self.__rerollController.rerollQuest(tokenQuestID)
            currency = None
        elif currency:
            setLastCurrencyForReroll(currency)
            result = yield self.__rerollController.rerollQuest(tokenQuestID, currency)
        if not result.success:
            self.viewModel.setIsPaymentError(True)
        else:
            self.__uiLogger.logRerollQuest(questSnapshot, currency)
            self.__fillSuggestedQuests(result.auxData)
        return

    def __fillSuggestedQuests(self, suggestedConditions):
        with self.viewModel.transaction() as vm:
            arrayQuestsModel = vm.getSuggestedQuests()
            arrayQuestsModel.clear()
            for condition in suggestedConditions:
                quests = self.__rerollController.getConditionQuestsByID(getConditionToken(condition))
                questSubModel = ArmoryYardQuestSubModel()
                self.__updateQuestModel(questSubModel, quests, condition)
                arrayQuestsModel.addViewModel(questSubModel)

            arrayQuestsModel.invalidate()
        return

    def __onUpdate(self, *_):
        if not self.__rerollController.isRerollEnabled() or not self.__currentQuests or self.__armoryYardCtrl.isPaused:
            self.__closeView()
        else:
            self._update()
        return

    def __updateProgressionTime(self, vm):
        startProgressionTime, endSeasonTime = self.__armoryYardCtrl.getProgressionTimes()
        vm.setToTimestamp(endSeasonTime)
        vm.setFromTimestamp(startProgressionTime)
        return

    def __onStatsChanged(self, _):
        with self.viewModel.transaction() as vm:
            self.__updatePrices(vm)
            self.__setStats(vm)
        return

    def __setLastCurrencyPrice(self):
        lastCurrency = getLastCurrencyForReroll()
        if not (lastCurrency and self.__itemsCache.items.stats.mayConsumeWalletResources):
            return
        rerollCost = self.__rerollController.getRerollCost(lastCurrency)
        if lastCurrency == Currency.FREE_XP:
            balance = self.__itemsCache.items.stats.freeXP
        else:
            balance = self.__itemsCache.items.stats.money.get(lastCurrency)
        if rerollCost and balance >= rerollCost:
            self.viewModel.price.setPriceID(lastCurrency)
        else:
            setLastCurrencyForReroll(b'')
        return


class ArmoryYardRerollViewWindow(WindowImpl):
    __slots__ = (b'questId', b'questsToSelect', b'onLoadedCallback')

    def __init__(self, quests, questsToSelect=None, parent=None, onLoadedCallback=None):
        super(ArmoryYardRerollViewWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=ArmoryYardRerollView(layoutID=R.views.armory_yard.lobby.feature.ArmoryYardRerollView(), quests=quests, questsToSelect=questsToSelect, onLoadedCallback=onLoadedCallback), layer=WindowLayer.FULLSCREEN_WINDOW, parent=parent)
        return
