from gui.sounds.sounds_ctrl import SoundsController
from skeletons.gui.sounds import ISoundsController
__all__ = (b'getSoundsConfig',)

def getSoundsConfig(manager):
    ctrl = SoundsController()
    ctrl.init()
    manager.addInstance(ISoundsController, ctrl, finalizer=b'fini')
    return
