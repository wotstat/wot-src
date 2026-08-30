from __future__ import absolute_import
import Event
from script_component.DynamicScriptComponent import DynamicScriptComponent

class WTRespawnTimeInfo(DynamicScriptComponent):

    def __init__(self, *_, **__):
        super(WTRespawnTimeInfo, self).__init__(*_, **__)
        self.onTeamLivesUpdated = Event.SafeEvent()
        self.onRespawnInfoUpdated = Event.Event()
        return

    def onDestroy(self):
        self.onTeamLivesUpdated.clear()
        super(WTRespawnTimeInfo, self).onDestroy()
        return

    def _onAvatarReady(self):
        self.onTeamLivesUpdated()
        self.onRespawnInfoUpdated(self.__getRespawnInfoIDs())
        return

    def set_respawnInfo(self, prev):
        self.onRespawnInfoUpdated(self.__getRespawnInfoIDs())
        return

    def getRespawnInfo(self, vehicleID):
        for entry in self.respawnInfo:
            if entry[b'vehicleID'] != vehicleID:
                continue
            return (
             entry.spawnTime, entry.delay)

        return (0.0, 0.0)

    def __getRespawnInfoIDs(self):
        if self.respawnInfo is None:
            return []
        else:
            return [entry[b'vehicleID'] for entry in self.respawnInfo]
