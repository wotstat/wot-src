import logging, typing
from constants import OFFER_TOKEN_PREFIX
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getMissionInfoData
from gui.battle_pass.battle_pass_bonuses_packers import TmanTemplateBonusPacker
from gui.impl import backport
from gui.impl.backport import BackportTooltipWindow
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.player_subscriptions.main_reward_model import MainRewardModel
from gui.impl.lobby.tooltips.additional_rewards_tooltip import AdditionalRewardsTooltip
from gui.impl.pub import ViewImpl
from gui.server_events.bonuses import getTutorialBonuses, splitBonuses
from gui.shared.event_dispatcher import showOfferGiftsWindow
from gui.shared.missions.packers.bonus import getDefaultBonusPackersMap, TokenBonusUIPacker
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.offers import IOffersDataProvider
if typing.TYPE_CHECKING:
    from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_reward_view_model import SubscriptionRewardViewModel
    from gui.shared.missions.packers.bonus import BaseBonusUIPacker
    from frameworks.wulf import Array
_logger = logging.getLogger(__name__)
BASE_EVENT_NAME = b'base'
MAIN_REWARD_PREFIX = b'mainReward_'

class PlayerSubscriptionRewardWindowView(ViewImpl):
    _offersProvider = dependency.descriptor(IOffersDataProvider)
    _BONUSES_ORDER = (
     b'dossier', b'customizations', b'premium_plus', Currency.GOLD, b'vehicles', b'items', b'crewBooks')

    def __init__(self, settings, ctx=None):
        super(PlayerSubscriptionRewardWindowView, self).__init__(settings, ctx)
        if ctx is not None:
            self._eventName = ctx.get(b'eventName', BASE_EVENT_NAME)
            self._quest = ctx.get(b'quest', None)
            self._vehicles = ctx.get(b'bonusVehicles', {})
        else:
            self._quest = None
            self._vehicles = {}
        self._tooltips = {}
        return

    @property
    def viewModel(self):
        return self.getViewModel()

    def createToolTip(self, event):
        if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
            tooltipId = int(event.getArgument(b'tooltipId'))
            window = BackportTooltipWindow(self._tooltips[tooltipId], self.getParentWindow()) if tooltipId is not None and tooltipId in self._tooltips else None
            if window is not None:
                window.load()
            return window
        if event.contentID == R.views.lobby.tooltips.AdditionalRewardsTooltip():
            showCount = event.getArgument(b'showCount')
            if showCount is None:
                return
            packedBonuses = self.viewModel.getRewards()[int(showCount):]
            window = DecoratedTooltipWindow(AdditionalRewardsTooltip(packedBonuses), useDecorator=False)
            window.load()
            window.move(event.mouse.positionX, event.mouse.positionY)
            return window
        else:
            return super(PlayerSubscriptionRewardWindowView, self).createToolTip(event)

    def _initialize(self, *args, **kwargs):
        super(PlayerSubscriptionRewardWindowView, self)._initialize(*args, **kwargs)
        self._setTitles()
        self._setMainRewards()
        self._initRewardsList()
        return

    def _setTitles(self):
        res = R.strings.ingame_gui.rewardWindow.dyn(self._eventName, None)
        if res:
            title = backport.text(res.dyn(b'headerText')())
            desc = backport.text(res.dyn(b'descText')())
            self.viewModel.setSubscriptionTitle(title)
            self.viewModel.setDescText(desc)
            offer = self.__getOffer()
            self.viewModel.setHasSelectiveRewards(offer is not None)
        return

    def _setMainRewards(self):
        stringResources = R.strings.ingame_gui.rewardWindow.dyn(self._eventName, None)
        index = 1
        with self.viewModel.transaction() as tx:
            mainRewardsModel = tx.getMainRewards()
            while True:
                imgName = (b'').join((self._eventName, b'_', MAIN_REWARD_PREFIX, str(index)))
                descr = stringResources.dyn(MAIN_REWARD_PREFIX + str(index))
                if descr:
                    model = MainRewardModel()
                    model.setImage(imgName)
                    model.setDescription(backport.text(descr()))
                    mainRewardsModel.addViewModel(model)
                    index += 1
                else:
                    break

        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onCloseButtonClick, self.__onCloseButtonClick),
         (
          self.viewModel.onChooseButtonClick, self.__onChoseButtonClick))

    def _initRewardsList(self):
        with self.getViewModel().transaction() as tx:
            rewardsList = tx.getRewards()
            bonuses = self._getBonuses()
            packerMap = self.__getPackerMap()
            for index, bonus in enumerate(bonuses):
                packer = packerMap.get(bonus.getName())
                if packer:
                    tooltipsData = packer.getToolTip(bonus)
                    for bonusIdx, bonusModel in enumerate(packer.pack(bonus)):
                        bonusModel.setTooltipId(str(index))
                        tooltip = tooltipsData[bonusIdx]
                        rewardsList.addViewModel(bonusModel)
                        self._tooltips[index] = tooltip

        return

    def _getBonuses(self):
        if self._quest is not None:
            allBonuses = getMissionInfoData(self._quest).getSubstituteBonuses()
            bonuses = [bonus for bonus in allBonuses if bonus.getName() != b'vehicles']
            vehBonus = getTutorialBonuses(b'vehicles', self._vehicles)
            bonuses.extend(vehBonus)
            bonuses = splitBonuses(bonuses)
            bonuses.sort(key=self.__keySortOrder)
            return bonuses
        else:
            return []

    def __onCloseButtonClick(self):
        self.destroyWindow()
        return

    def __onChoseButtonClick(self):
        offer = self.__getOffer()
        if offer:
            showOfferGiftsWindow(offer.id)
        else:
            self.destroyWindow()
        return

    def __getOffer(self):
        bonuses = self._quest.getBonuses(b'tokens')
        for bonus in bonuses:
            for tID in bonus.getTokens():
                if tID.startswith(OFFER_TOKEN_PREFIX):
                    for offer in self._offersProvider.getAvailableOffers(onlyVisible=True):
                        if offer.token == tID:
                            return offer

        return

    def __keySortOrder(self, bonus):
        if bonus.getName() in self._BONUSES_ORDER:
            return self._BONUSES_ORDER.index(bonus.getName())
        return len(self._BONUSES_ORDER)

    def __getPackerMap(self):
        packer = getDefaultBonusPackersMap()
        packer[b'tokens'] = PSTokenBonusUIPacker()
        packer[b'tmanToken'] = TmanTemplateBonusPacker()
        return packer


class PSTokenBonusUIPacker(TokenBonusUIPacker):

    @classmethod
    def __packBattleBonusX5Token(cls, model, bonus, *args):
        model.setValue(str(bonus.getCount()))
        model.setName(b'bonus_battle_task')
        return model
