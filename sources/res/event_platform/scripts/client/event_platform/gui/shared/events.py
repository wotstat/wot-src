from __future__ import absolute_import
from gui.shared.event_bus import SharedEvent

class RespawnFrameworkEvent(SharedEvent):
    VEHICLES_LOADED = b'respawnFramework/respawnVehiclesLoaded'
    POSTMORTEM_ENTERED = b'respawnFramework/postmortemEntered'
    POSTMORTEM_LEFT = b'respawnFramework/postmortemLeft'
