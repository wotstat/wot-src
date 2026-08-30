from __future__ import absolute_import
from collections import namedtuple
WotShopPrice = namedtuple(b'WotShopPrice', (b'currency', b'value'))

class IWotShopPurchaseController(object):

    def purchaseProduct(self, storefront, productCode, productPrice):
        raise NotImplementedError
        return
