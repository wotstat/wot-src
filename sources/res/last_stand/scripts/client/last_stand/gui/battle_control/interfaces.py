from __future__ import absolute_import
from gui.battle_control.arena_info.interfaces import IArenaLoadController

class ILSVOIPController(IArenaLoadController):
    __slots__ = ()

    @property
    def isVoipSupported(self):
        raise NotImplementedError
        return

    @property
    def isVoipEnabled(self):
        raise NotImplementedError
        return

    @property
    def isTeamChannelAvailable(self):
        raise NotImplementedError
        return

    @property
    def isJoined(self):
        raise NotImplementedError
        return

    @property
    def isTeamVoipEnabled(self):
        raise NotImplementedError
        return

    def toggleChannelConnection(self):
        raise NotImplementedError
        return
