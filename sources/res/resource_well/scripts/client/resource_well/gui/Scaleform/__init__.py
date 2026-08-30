from __future__ import absolute_import
from gui.shared.system_factory import registerScaleformLobbyPackages

def registerResourceWellScaleform():
    registerScaleformLobbyPackages((b'resource_well.gui.Scaleform.daapi.view.lobby',))
    return
