from gui.app_loader import settings, decorators
from gui.app_loader.decorators import app_getter, def_lobby, def_battle, sf_lobby, sf_battle
__all__ = (b'getAppLoaderConfig', b'decorators', b'settings', b'app_getter', b'def_lobby', b'def_battle', b'sf_lobby', b'sf_battle')

def getAppLoaderConfig(manager):
    from gui.app_loader.loader import AppLoader
    from skeletons.gui.app_loader import IAppLoader
    manager.addInstance(IAppLoader, AppLoader(), finalizer=b'fini')
    return
