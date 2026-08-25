from constants import LOOTBOX_TOKEN_PREFIX
from frameworks.wulf import ViewSettings, WindowFlags
from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.lootbox_system.auto_open_view_model import AutoOpenViewModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator
from gui.impl.pub import ViewImpl, WindowImpl
from gui.lootbox_system.base.bonuses_helpers import REWARDS_GROUP_NAME_RES, RewardsGroup, getGoodiesFilter, getItemsFilter, getTankmenFilter, getVehiclesFilter, isBattleBooster, isCrewBook, noCompensation, isOptionalDevice, packBonusGroups
from gui.lootbox_system.base.common import LOOTBOX_COMPENSATION_TOKEN_PREFIX
from gui.lootbox_system.base.decorators import createTooltipContentDecorator
from gui.lootbox_system.base.views_loaders import showItemPreview
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache

class AutoOpenView(ViewImpl):
    __goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, ctx):
        settings = ViewSettings(R.views.mono.lootbox.auto_open(), model=AutoOpenViewModel())
        super(AutoOpenView, self).__init__(settings)
        self.__eventName = ctx.get(b'eventName')
        self.__rewards = self.__filterRewards(ctx.get(b'rewards'))
        self.__boxes = ctx.get(b'boxes')
        self.__tooltips = {}
        return

    @property
    def viewModel(self):
        return super(AutoOpenView, self).getViewModel()

    @createBackportTooltipDecorator()
    def createToolTip(self, event):
        return super(AutoOpenView, self).createToolTip(event)

    @createTooltipContentDecorator()
    def createToolTipContent(self, event, contentID):
        return super(AutoOpenView, self).createToolTipContent(event, contentID)

    def getTooltipData(self, event):
        return self.__tooltips.get(event.getArgument(b'tooltipId', 0))

    def _onLoading(self, *args, **kwargs):
        super(AutoOpenView, self)._onLoading(*args, **kwargs)
        with self.viewModel.transaction() as tx:
            tx.setEventName(self.__eventName)
            tx.setBoxesQuantity(sum(self.__boxes.values()))
        self.__updateRewards()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onPreview, self.__showPreview))

    def __updateRewards(self):
        with self.getViewModel().transaction() as tx:
            packBonusGroups(bonuses=self.__rewards, groupModels=tx.getRewardRows(), groupsLayout=self.__getGroupsLayout(), tooltipsData=self.__tooltips, packer=None, eventName=self.__eventName)
        return

    @classmethod
    def __getGroupsLayout(cls):
        layout = (
         RewardsGroup(name=REWARDS_GROUP_NAME_RES.vehicles(), bonusTypes=(b'vehicles',), bonuses={}, filterFuncs=(
          getVehiclesFilter((noCompensation,)),)),
         RewardsGroup(name=REWARDS_GROUP_NAME_RES.customizations(), bonusTypes=(b'customizations',), bonuses={}, filterFuncs=None),
         RewardsGroup(name=REWARDS_GROUP_NAME_RES.crewBooksAndCrew(), bonusTypes=(b'items', b'goodies', b'tokens', b'crewSkins'), bonuses={}, filterFuncs=(
          getItemsFilter((isCrewBook,)),
          getGoodiesFilter((
           cls.__goodiesCache.getRecertificationForm, cls.__goodiesCache.getMentoringLicense)),
          getTankmenFilter)),
         RewardsGroup(name=REWARDS_GROUP_NAME_RES.optionalDevicesAndBattleBoosters(), bonusTypes=(b'items', b'goodies'), bonuses={}, filterFuncs=(
          getItemsFilter((isOptionalDevice, isBattleBooster)),
          getGoodiesFilter((cls.__goodiesCache.getDemountKit,)))),
         RewardsGroup(name=REWARDS_GROUP_NAME_RES.other(), bonusTypes=(), bonuses={}, filterFuncs=None))
        return layout

    def __showPreview(self, ctx):
        showItemPreview(str(ctx.get(b'bonusType')), int(ctx.get(b'bonusId')), int(ctx.get(b'styleID')))
        return

    def __onClose(self):
        from gui.Scaleform.lobby_entry import getLobbyStateMachine
        lsm = getLobbyStateMachine()
        lsm.getStateFromView(self).goBack()
        return

    def __filterRewards(self, rewards):
        for tokenName in rewards.get(b'tokens', {}).keys():
            if tokenName.startswith((LOOTBOX_TOKEN_PREFIX, LOOTBOX_COMPENSATION_TOKEN_PREFIX)):
                rewards[b'tokens'].pop(tokenName, None)

        if not rewards.get(b'tokens'):
            rewards.pop(b'tokens', None)
        return rewards


class AutoOpenWindow(WindowImpl):

    def __init__(self, layer, ctx=None, *args, **kwargs):
        super(AutoOpenWindow, self).__init__(WindowFlags.WINDOW | WindowFlags.WINDOW_FULLSCREEN, content=AutoOpenView(ctx), layer=layer)
        return
