from frameworks.wulf import ViewSettings, WindowFlags, WindowLayer
from gui.battle_pass.battle_pass_decorators import createBackportTooltipDecorator, createTooltipContentDecorator
from gui.impl.lobby.frontline import RegisteredFrontlineTooltips
from gui.server_events.bonuses import getNonQuestBonuses, mergeBonuses, splitBonuses
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.frontline.awards_view_model import AwardsViewModel
from gui.impl.gen.view_models.views.lobby.frontline.reward_item_model import RewardItemModel
from gui.impl.pub import ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow
from gui.shared.missions.packers.bonus import ItemBonusUIPacker, BonusUIPacker, getDefaultBonusPackersMap
from gui.shared.gui_items import GUI_ITEM_TYPE
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from uilogging.epic_battle.constants import EpicBattleLogKeys
from uilogging.epic_battle.loggers import EpicBattleTooltipLogger
MAIN_REWARDS_LIMIT = 4

class AwardsView(ViewImpl):
    __slots__ = (b'__tooltipItems', b'__onCloseCallback', b'__onAnimationEndedCallback', b'__isAnimationEnded', b'__uiEpicBattleLogger')

    def __init__(self, bonuses, onCloseCallback=None, onAnimationEnded=None):
        settings = ViewSettings(R.views.lobby.frontline.AwardsView())
        settings.model = AwardsViewModel()
        settings.kwargs = {b'bonuses': bonuses}
        super(AwardsView, self).__init__(settings)
        self.__isAnimationEnded = False
        self.__tooltipItems = {}
        self.__onCloseCallback = onCloseCallback
        self.__onAnimationEndedCallback = onAnimationEnded
        self.__uiEpicBattleLogger = EpicBattleTooltipLogger()
        return

    @property
    def viewModel(self):
        return super(AwardsView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(AwardsView, self).createToolTip(event)

    @createTooltipContentDecorator()
    def createToolTipContent(self, event, contentID):
        if contentID in RegisteredFrontlineTooltips.REGISTERED_SIMPLE_TOOLTIPS:
            view = RegisteredFrontlineTooltips.REGISTERED_SIMPLE_TOOLTIPS.get(contentID)
            return view()
        else:
            if contentID in RegisteredFrontlineTooltips.REGISTERED_TOOLTIPS:
                view = RegisteredFrontlineTooltips.REGISTERED_TOOLTIPS.get(contentID)
                return view(event)
            return

    def getTooltipData(self, event):
        tooltipId = event.getArgument(b'tooltipId')
        if tooltipId is None:
            return
        else:
            return self.__tooltipItems.get(tooltipId)

    def _initialize(self, *args, **kwargs):
        super(AwardsView, self)._initialize(*args, **kwargs)
        self.__uiEpicBattleLogger.initialize(EpicBattleLogKeys.AWARDS_VIEW.value)
        self.viewModel.onAnimationEnded += self.__onAnimationEnded
        return

    def _finalize(self):
        super(AwardsView, self)._finalize()
        self.__uiEpicBattleLogger.reset()
        self.viewModel.onAnimationEnded -= self.__onAnimationEnded
        self.__safeCall(self.__onCloseCallback)
        return

    def _onLoading(self, bonuses, *args, **kwargs):
        rewards = composeBonuses(bonuses)
        if not rewards:
            return
        packBonusModelAndTooltipData(rewards, self.viewModel.mainRewards, self.viewModel.additionalRewards, self.__tooltipItems)
        return

    def __onAnimationEnded(self):
        if not self.__isAnimationEnded:
            self.__safeCall(self.__onAnimationEndedCallback)
            self.__isAnimationEnded = True
        return

    @staticmethod
    def __safeCall(callback, *args, **kwargs):
        if callable(callback):
            callback(*args, **kwargs)
        return


class AwardsWindow(LobbyNotificationWindow):
    __slots__ = (b'__params',)
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)

    def __init__(self, bonuses, onCloseCallback=None, onAnimationEndedCallback=None):
        self.__params = dict(bonuses=bonuses, onCloseCallback=onCloseCallback, onAnimationEndedCallback=onAnimationEndedCallback)
        super(AwardsWindow, self).__init__(wndFlags=WindowFlags.SERVICE_WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=AwardsView(bonuses, onCloseCallback, onAnimationEndedCallback), layer=WindowLayer.TOP_WINDOW)
        return

    def isParamsEqual(self, *args, **kwargs):
        return all(pValue in args or kwargs.get(pName) == pValue for pName, pValue in self.__params.iteritems())

    def _finalize(self):
        super(AwardsWindow, self)._finalize()
        self.__epicController.onGameModeStatusTick()
        return


def composeBonuses(rewards, ctx=None):
    bonuses = []
    for reward in rewards:
        for key, value in reward.iteritems():
            bonuses.extend(getNonQuestBonuses(key, value, ctx))

    bonuses = mergeBonuses(bonuses)
    bonuses = splitBonuses(bonuses)
    return bonuses


class FrontlineItemBonusUIPacker(ItemBonusUIPacker):

    @classmethod
    def _packSingleBonus(cls, bonus, item, count):
        model = super(FrontlineItemBonusUIPacker, cls)._packSingleBonus(bonus, item, count)
        model.setUserName(item.userName)
        iconName = item.getGUIEmblemID()
        if item.itemTypeID == GUI_ITEM_TYPE.BATTLE_BOOSTER:
            iconName += b'BattleBooster'
        model.setUserName(item.userName)
        model.setBigIcon(iconName)
        return model

    @classmethod
    def _getBonusModel(cls):
        return RewardItemModel()


def getFrontlineBonusPacker():
    mapping = getDefaultBonusPackersMap()
    mapping[b'items'] = FrontlineItemBonusUIPacker()
    return BonusUIPacker(mapping)


def packBonusModelAndTooltipData(bonuses, bonusModelsListMain, bonusModelsListAdditional, tooltipData=None):
    itemsForModel = []
    packer = getFrontlineBonusPacker()
    for bonus in bonuses:
        if bonus.isShowInGUI():
            bonusList = packer.pack(bonus)
            bonusTooltipList = []
            bonusContentIdList = []
            if bonusList and tooltipData is not None:
                bonusTooltipList = packer.getToolTip(bonus)
                bonusContentIdList = packer.getContentId(bonus)
            for bonusIndex, item in enumerate(bonusList):
                bonusTooltipData, bonusContentIdData = (None, None)
                if bonusTooltipList:
                    bonusTooltipData = bonusTooltipList[bonusIndex]
                if bonusContentIdList:
                    bonusContentIdData = str(bonusContentIdList[bonusIndex])
                itemsForModel.append((item, bonusTooltipData, bonusContentIdData))

    sortedItems = sorted(itemsForModel, key=(lambda item: item[0].getLabel()))
    for idx, data in enumerate(sortedItems):
        item, bonusTooltipData, bonusContentIdData = data
        if idx < MAIN_REWARDS_LIMIT:
            item.setIndex(idx)
            bonusModelsListMain.addViewModel(item)
        else:
            item.setIndex(idx - MAIN_REWARDS_LIMIT)
            bonusModelsListAdditional.addViewModel(item)
        tooltipIdx = str(idx)
        item.setTooltipId(tooltipIdx)
        if bonusTooltipList:
            tooltipData[tooltipIdx] = bonusTooltipData
        if bonusContentIdList:
            item.setTooltipContentId(bonusContentIdData)

    return
