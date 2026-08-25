from skeletons.gui.web import IWebController
from gui.wgcg.wot_shop.controller import IWotShopController
__all__ = (b'getWebServicesConfig',)

def getWebServicesConfig(manager):
    from gui.wgcg.web_controller import WebController
    from gui.wgcg.wot_shop.controller import WotShopController
    ctrl = WebController()
    ctrl.init()
    manager.addInstance(IWebController, ctrl, finalizer=b'fini')
    manager.addInstance(IWotShopController, WotShopController(), finalizer=b'fini')
    return
