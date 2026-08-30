from typing import TYPE_CHECKING
from gui.impl import backport
from constants import IS_DEVELOPMENT
from frameworks.wulf import ViewSettings
from goodies.goodie_constants import GOODIE_VARIETY
from gui import SystemMessages
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.goodies import IGoodiesCache
from gui.impl.backport.backport_tooltip import createBackportTooltipContent
from gui.impl.auxiliary.tooltips.compensation_tooltip import VehicleCompensationTooltipContent
from gui.impl.gen import R
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_types import LootBoxCompensationTooltipTypes
from gui.impl.gen.view_models.views.loot_box_vehicle_compensation_tooltip_model import LootBoxVehicleCompensationTooltipModel
from gui.impl.lobby.crew.tooltips.mentoring_license_tooltip import MentoringLicenseTooltip
from gui.impl.lobby.battle_pass.tooltips.battle_pass_coin_tooltip_view import BattlePassCoinTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_taler_tooltip import BattlePassTalerTooltip
from gui.impl.lobby.lootbox_system.base.tooltips.box_tooltip import BoxTooltip, BoxCompensationTooltip
from gui.impl.lobby.lootbox_system.base.tooltips.guaranteed_reward_info_tooltip import GuaranteedRewardInfoTooltip
from gui.impl.lobby.lootbox_system.base.tooltips.random_national_bonus_tooltip_view import RandomNationalBonusTooltipView
from gui.impl.lobby.lootbox_system.base.tooltips.statistics_category_tooltip import StatisticsCategoryTooltipView
from gui.impl.lobby.personal_reserves.quest_booster_tooltip import QuestBoosterTooltip
from helpers import dependency
if TYPE_CHECKING:
    from typing import Optional
    from gui.impl.backport import TooltipData

def onNotImplementedCall(callName, taskID):
    message = (b'"{}" is not implemented, will done in "{}"').format(callName, taskID)
    if IS_DEVELOPMENT:
        SystemMessages.pushMessage(message, type=SystemMessages.SM_TYPE.Error)
    return


def createBackportTooltipDecorator():

    def decorator(func):

        def wrapper(self, event):
            if event.contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
                tooltipData = self.getTooltipData(event)
                if tooltipData is None:
                    return
                window = backport.BackportTooltipWindow(tooltipData, self.getParentWindow(), event)
                if window is None:
                    return
                window.load()
                return window
            else:
                return func(self, event)

        return wrapper

    return decorator


def createTooltipContentDecorator():

    def decorator(func):

        def wrapper(self, event, contentID):
            goodiesCache = dependency.instance(IGoodiesCache)
            statisticBonusesCategory = event.getArgument(b'bonusesCategory')
            if statisticBonusesCategory == GOODIE_VARIETY.RECERTIFICATION_FORM_NAME and contentID == R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent():
                form = goodiesCache.getRecertificationForm(currency=b'credits')
                return createBackportTooltipContent(isSpecial=True, specialAlias=TOOLTIPS_CONSTANTS.EPIC_BATTLE_RECERTIFICATION_FORM_TOOLTIP, specialArgs=[
                 form.intCD])
            else:
                if contentID == R.views.lobby.crew.tooltips.MentoringLicenseTooltip():
                    license = goodiesCache.getMentoringLicense(currency=b'gold')
                    return MentoringLicenseTooltip(license.inventoryCount)
                if contentID == R.views.mono.lootbox.tooltips.guaranteed_reward_info():
                    return GuaranteedRewardInfoTooltip(event.getArgument(b'category'), event.getArgument(b'eventName'))
                if contentID == R.views.mono.lootbox.tooltips.box_tooltip():
                    return BoxTooltip(event.getArgument(b'boxCategory'), event.getArgument(b'eventName'))
                if contentID == R.views.mono.lootbox.tooltips.statistics_category():
                    return StatisticsCategoryTooltipView(statisticBonusesCategory, event.getArgument(b'eventName'))
                if contentID == R.views.mono.battle_pass.tooltips.bpcoin():
                    return BattlePassCoinTooltipView()
                if contentID == R.views.mono.battle_pass.tooltips.bptaler():
                    return BattlePassTalerTooltip()
                tooltipData = getattr(self, b'getTooltipData', (lambda _: None))(event)
                if tooltipData is not None:
                    if contentID == R.views.lobby.awards.tooltips.RewardCompensationTooltip():
                        compTooltipData = {b'iconBefore': (event.getArgument(b'iconBefore', b'')), b'labelBefore': (event.getArgument(b'labelBefore', b'')), 
                           b'iconAfter': (event.getArgument(b'iconAfter', b'')), 
                           b'labelAfter': (event.getArgument(b'labelAfter', b'')), 
                           b'bonusName': (event.getArgument(b'bonusName', b'')), 
                           b'countBefore': (event.getArgument(b'countBefore', 1)), 
                           b'tooltipType': (LootBoxCompensationTooltipTypes.VEHICLE)}
                        compTooltipData.update(tooltipData.specialArgs)
                        settings = ViewSettings(R.views.lobby.awards.tooltips.RewardCompensationTooltip(), model=LootBoxVehicleCompensationTooltipModel(), kwargs=compTooltipData)
                        return VehicleCompensationTooltipContent(settings)
                    if contentID == R.views.mono.lootbox.tooltips.random_national_bonus():
                        return RandomNationalBonusTooltipView(*tooltipData.specialArgs)
                if contentID == R.views.mono.lootbox.tooltips.box_compensation():
                    if tooltipData is None:
                        return
                    return BoxCompensationTooltip(*tooltipData.specialArgs)
                if contentID == R.views.lobby.personal_reserves.QuestBoosterTooltip():
                    return QuestBoosterTooltip(*tooltipData.specialArgs)
                return func(self, event, contentID)

        return wrapper

    return decorator
