from __future__ import absolute_import
import BigWorld
from Event import Event
from helpers import isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent

class ObeliskInfoStates(object):
    SHOW = b'show'
    HIT = b'hit'
    DEATH = b'death'
    HIDE = b'hide'


class LSObeliskInfoComponent(DynamicScriptComponent):

    def __init__(self):
        super(LSObeliskInfoComponent, self).__init__()
        self.onStateChange = Event()
        self.onObeliskObserved = Event()
        return

    def onDestroy(self):
        self.onStateChange.clear()
        super(LSObeliskInfoComponent, self).onDestroy()
        return

    def set_isPresent(self, _):
        if self.isPresent:
            self.onStateChange(ObeliskInfoStates.SHOW)
        else:
            self.onStateChange(ObeliskInfoStates.HIDE)
        return

    def set_observedObeliskCD(self, _):
        self.onObeliskObserved(self.observedObeliskCD)
        return

    def onDamageReceived(self):
        if self.isPresent:
            self.onStateChange(ObeliskInfoStates.HIT)
        return

    def onDeath(self):
        self.onStateChange(ObeliskInfoStates.DEATH)
        return

    @staticmethod
    def getInstance():
        if not isPlayerAvatar():
            return
        else:
            player = BigWorld.player()
            if not player or not player.arena:
                return
            return getattr(player.arena.arenaInfo, b'LSObeliskInfoComponent', None)

    def _onAvatarReady(self):
        super(LSObeliskInfoComponent, self)._onAvatarReady()
        self.onObeliskObserved(self.observedObeliskCD)
        return
