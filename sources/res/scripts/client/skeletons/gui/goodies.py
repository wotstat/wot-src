from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Optional, Dict, List, Any, Tuple
    from gui.shared.money import Money
    from gui.shared.gui_items.fitting_item import FittingItem
    from gui.shared.utils.requesters.GoodiesRequester import GoodieVariable
    from gui.goodies.goodie_items import RecertificationForm, DemountKit, Booster, _PersonalDiscount, _Goodie
    from gui.shared.utils.requesters.ShopRequester import _ResourceData, _NamedGoodieData

class IBoostersStateProvider(object):

    @property
    def personalGoodies(self):
        raise NotImplementedError
        return

    def getBoosters(self, criteria=None):
        raise NotImplementedError
        return

    def getBooster(self, boosterID):
        raise NotImplementedError
        return

    def getActiveResources(self):
        raise NotImplementedError
        return

    def getActiveBoosterTypes(self):
        raise NotImplementedError
        return

    def getBoosterPriceData(self, boosterID):
        raise NotImplementedError
        return

    def isBoosterHidden(self, boosterID):
        raise NotImplementedError
        return

    def haveBooster(self, boosterID):
        raise NotImplementedError
        return

    def getClanReserves(self):
        raise NotImplementedError
        return


class IGoodiesCache(IBoostersStateProvider):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    def getItemByTargetValue(self, targetValue):
        raise NotImplementedError
        return

    def getDiscount(self, discoutID):
        raise NotImplementedError
        return

    def getDemountKit(self, demountKitID=None, currency=None):
        raise NotImplementedError
        return

    def getGoodie(self, goodieID):
        raise NotImplementedError
        return

    def getGoodieByID(self, goodieID):
        raise NotImplementedError
        return

    def getDiscounts(self, criteria=None):
        raise NotImplementedError
        return

    def getDemountKits(self, criteria=None):
        raise NotImplementedError
        return

    def getRecertificationForm(self, recertificationFormID=None, currency=None):
        raise NotImplementedError
        return

    def getRecertificationForms(self, criteria=None):
        raise NotImplementedError
        return
