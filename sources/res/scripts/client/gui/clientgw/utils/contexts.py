from gui.clientgw.base.contexts import CommonWebRequestCtx
from gui.clientgw.settings import WebRequestDataType

class SPAAccountAttributeCtx(CommonWebRequestCtx):

    def __init__(self, ctx, waitingID=b''):
        self.__attrPrefix = ctx.attr_prefix
        super(SPAAccountAttributeCtx, self).__init__(waitingID=waitingID)
        return

    def getRequestType(self):
        return WebRequestDataType.SPA_GET_ACCOUNT_ATTRIBUTE

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getRequestedAttr(self):
        return self.__attrPrefix

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return


class PlatformFetchProductListCtx(CommonWebRequestCtx):

    def __init__(self, ctx, waitingID=b''):
        self.__params = {b'storefront': (ctx.storefront), 
           b'wgid': (ctx.wgid), 
           b'language': (ctx.language), 
           b'additional_data': (ctx.additional_data), 
           b'country': (ctx.country), 
           b'response_fields': (ctx.response_fields), 
           b'response_fields_profile': (ctx.response_fields_profile), 
           b'category': (ctx.category)}
        if ctx.product_codes:
            self.__params.update(product_codes=ctx.product_codes)
        super(PlatformFetchProductListCtx, self).__init__(waitingID=waitingID)
        return

    def getRequestType(self):
        return WebRequestDataType.PLATFORM_FETCH_PRODUCT_LIST

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getParams(self):
        return self.__params

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return


class PlatformFetchProductListPersonalCtx(CommonWebRequestCtx):

    def __init__(self, ctx, waitingID=b''):
        self.__params = {b'storefront': (ctx.storefront), 
           b'language': (ctx.language), 
           b'country': (ctx.country)}
        if ctx.product_codes:
            self.__params.update(product_codes=ctx.product_codes)
        super(PlatformFetchProductListPersonalCtx, self).__init__(waitingID=waitingID)
        return

    def getRequestType(self):
        return WebRequestDataType.PLATFORM_FETCH_PRODUCT_LIST_PERSONAL

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getParams(self):
        return self.__params

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return


class PlatformGetUserSubscriptionsCtx(CommonWebRequestCtx):

    def __init__(self, ctx, waitingID=b''):
        self.__params = {b'status': (ctx.status), 
           b'product_code': (ctx.productCode)}
        super(PlatformGetUserSubscriptionsCtx, self).__init__(waitingID=waitingID)
        return

    def getRequestType(self):
        return WebRequestDataType.PLATFORM_GET_USER_SUBSCRIPTIONS

    def isAuthorizationRequired(self):
        return True

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getParams(self):
        return self.__params

    @staticmethod
    def getDataObj(incomeData):
        return incomeData

    @staticmethod
    def getDefDataObj():
        return
