from gui.shared import g_eventBus, EVENT_BUS_SCOPE
from gui.shared.events import HasCtxEvent
from script_component.DynamicScriptComponent import DynamicScriptComponent

class WTCloneInfoEvent(HasCtxEvent):
    CLONE_VEHICLE_INFOS_UPDATED = b'wt/cloneVehicleIDsUpdated'


class WTTeamInfoComponent(DynamicScriptComponent):

    def set_cloneVehicleInfos(self, prev):
        g_eventBus.handleEvent(WTCloneInfoEvent(WTCloneInfoEvent.CLONE_VEHICLE_INFOS_UPDATED, ctx={b'cloneVehicleInfo': (self.cloneVehicleInfos)}), scope=EVENT_BUS_SCOPE.BATTLE)
        return
