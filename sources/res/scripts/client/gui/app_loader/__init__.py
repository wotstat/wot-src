from gui.app_loader import settings
from gui.app_loader.decorators import app_getter
from gui.app_loader.decorators import def_lobby
from gui.app_loader.decorators import def_battle
from gui.app_loader.decorators import sf_lobby
from gui.app_loader.decorators import sf_battle
__all__ = (b'getAppLoaderConfig', b'decorators', b'settings', b'app_getter', b'def_lobby', b'def_battle', b'sf_lobby', b'sf_battle')

def getAppLoaderConfig(manager):
    from gui.app_loader.loader import AppLoader
    from skeletons.gui.app_loader import IAppLoader
    manager.addInstance(IAppLoader, AppLoader(), finalizer=b'fini')
    return
