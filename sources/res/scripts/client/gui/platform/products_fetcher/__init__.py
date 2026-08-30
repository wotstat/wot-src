import typing
from gui.platform.products_fetcher.subscriptions.subscriptions_controller import SubscriptionProductsFetchController
from gui.platform.products_fetcher.user_subscriptions.controller import UserSubscriptionsFetchController
from gui.platform.products_fetcher.wot_shop.controller import WotShopFetcherController
from skeletons.gui.platform.product_fetch_controller import ISubscriptionProductsFetchController, IUserSubscriptionsFetchController, IWotShopFetchController
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = (b'getProductFetchControllers',)

def getProductFetchControllers(manager):
    subscriptionsFetchController = SubscriptionProductsFetchController()
    subscriptionsFetchController.init()
    manager.addInstance(ISubscriptionProductsFetchController, subscriptionsFetchController, finalizer=b'fini')
    userSubscriptionsFetchController = UserSubscriptionsFetchController()
    userSubscriptionsFetchController.init()
    manager.addInstance(IUserSubscriptionsFetchController, userSubscriptionsFetchController, finalizer=b'fini')
    wotShopController = WotShopFetcherController()
    wotShopController.init()
    manager.addInstance(IWotShopFetchController, wotShopController, finalizer=b'fini')
    return
