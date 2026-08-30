import BigWorld
from constants import SPA_ATTRS
from gui.clientgw.base.contexts import CommonWebRequestCtx
from gui.clientgw.settings import WebRequestDataType

class ShopRequestCtx(CommonWebRequestCtx):
    __slots__ = (b'__userCountry',)

    def __init__(self, waitingID=b'', userCountry=b''):
        super(ShopRequestCtx, self).__init__(waitingID)
        self.__userCountry = userCountry
        return

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getCountryCode(self):
        country = BigWorld.player().spaFlags.getFlag(SPA_ATTRS.USER_COUNTRY) or self.__userCountry
        return country.upper()

    @staticmethod
    def getDataObj(incomeData):
        return incomeData


class ShopInventoryEntitlementsCtx(ShopRequestCtx):
    __slots__ = (b'__entitlementCodes',)

    def __init__(self, entitlementCodes=(), waitingID=b''):
        super(ShopInventoryEntitlementsCtx, self).__init__(waitingID)
        self.__entitlementCodes = entitlementCodes
        return

    def getRequestType(self):
        return WebRequestDataType.SHOP_INVENTORY_ENTITLEMENTS

    def getEntitlementCodes(self):
        return self.__entitlementCodes


class ShopStorefrontProductsCtx(ShopRequestCtx):
    __slots__ = (b'__storefront',)

    def __init__(self, storefront=b'', waitingID=b'', userCountry=b''):
        super(ShopStorefrontProductsCtx, self).__init__(waitingID, userCountry)
        self.__storefront = storefront
        self.__userCountry = userCountry
        return

    def getRequestType(self):
        return WebRequestDataType.SHOP_GET_STOREFRONT_PRODUCTS

    def getStorefront(self):
        return self.__storefront


class ShopBuyStorefrontProductCtx(ShopStorefrontProductsCtx):
    __slots__ = (b'__storefront', b'__productCode', b'__amount', b'__prices')

    def __init__(self, storefront=b'', productCode=b'', amount=1, prices=None, waitingID=b'', userCountry=b''):
        super(ShopBuyStorefrontProductCtx, self).__init__(storefront, waitingID, userCountry)
        self.__storefront = storefront
        self.__productCode = productCode
        self.__amount = amount
        self.__prices = prices
        return

    def getRequestType(self):
        return WebRequestDataType.SHOP_BUY_STOREFRONT_PRODUCTS

    def getProductCode(self):
        return self.__productCode

    def getData(self):
        return {b'prices': (self.__prices), 
           b'amount': (self.__amount)}
