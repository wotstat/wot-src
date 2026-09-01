from __future__ import absolute_import
from gui.shared.events import HasCtxEvent

class WhiteTigerEvent(HasCtxEvent):
    SHOW_SPAWN_POINTS = b'game/showSpawnPoints'
    HIDE_SPAWN_POINTS = b'game/hideSpawnPoints'
