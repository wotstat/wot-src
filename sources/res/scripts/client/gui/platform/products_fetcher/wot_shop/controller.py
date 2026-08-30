import logging
from gui.platform.products_fetcher.controller import ProductsFetchController
from gui.platform.products_fetcher.wot_shop.descriptors.account_limits_descriptor import AccountLimitsDescriptor
from gui.platform.products_fetcher.wot_shop.descriptors.categories_descriptor import CategoriesDescriptor
from gui.platform.products_fetcher.wot_shop.descriptors.product_descriptor import ProductDescriptor
from gui.platform.products_fetcher.wot_shop.fetch_result import WotShopFetchResult
from gui.wgcg.wot_shop.contexts import WotShopGetStorefrontProductsCtx
from skeletons.gui.platform.product_fetch_controller import IWotShopFetchController
_logger = logging.getLogger(__name__)

class WotShopFetcherController(ProductsFetchController, IWotShopFetchController):
    platformFetchCtx = WotShopGetStorefrontProductsCtx
    productDescriptor = ProductDescriptor
    accountLimitsDescriptor = AccountLimitsDescriptor
    categoriesDescriptor = CategoriesDescriptor
    dataGetKey = b'data'
    downloadRequired = False

    @property
    def _fetchResultType(self):
        return WotShopFetchResult

    def _createDescriptors(self, data):
        self._fetchResult.setProducts(map(self.productDescriptor, data[b'items']))
        self._fetchResult.setAccountLimits(map(self.accountLimitsDescriptor, data[b'account_limits']))
        self._fetchResult.setCategories(map(self.categoriesDescriptor, data[b'categories']))
        return

    def getProducts(self, showWaiting=True, **kwargs):
        self.platformParams.storefront = kwargs[b'storefront']
        return super(WotShopFetcherController, self).getProducts(showWaiting)
