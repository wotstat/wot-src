import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Dict
    from Event import Event
    from comp7.gui.game_control.comp7_weekly_quests_controller import _Comp7WeeklyQuests
    from gui.ranked_battles.ranked_models import Rank

class IComp7ShopController(IGameController):
    onDataUpdated = None
    onShopStateChanged = None

    @property
    def isShopEnabled(self):
        raise NotImplementedError
        return

    def getProducts(self):
        raise NotImplementedError
        return

    def buyProduct(self, productCode):
        raise NotImplementedError
        return

    def hasNewProducts(self, rank):
        raise NotImplementedError
        return

    def hasNewDiscounts(self, rank):
        raise NotImplementedError
        return

    def validateCachedProducts(self):
        raise NotImplementedError
        return


class IComp7WeeklyQuestsController(IGameController):
    onWeeklyQuestsUpdated = None

    def getQuests(self):
        raise NotImplementedError
        return
