from new_year_common.settings import NyBuyToyConsts

class BuyToyConfig(object):
    __slots__ = (b'_config',)

    def __init__(self, config):
        self._config = config
        return

    def getToyCountForOnePurchase(self):
        return self._config.get(NyBuyToyConsts.TOY_COUNT_FOR_ONE_PURCHASE)
