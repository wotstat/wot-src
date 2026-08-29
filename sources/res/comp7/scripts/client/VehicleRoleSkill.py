from helpers import fixed_dict
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleRoleSkill(DynamicScriptComponent):

    def set_roleEquipmentState(self, prev):
        if self._isAvatarReady:
            self.__updateRoleEquipmentState(prev)
        return

    def _onAvatarReady(self):
        self.__updateRoleEquipmentState()
        return

    def __updateRoleEquipmentState(self, previousState=None):
        from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
        ctx = {b'state': (fixed_dict.getRoleEquipmentState(self.roleEquipmentState)), 
           b'previousState': (fixed_dict.getRoleEquipmentState(previousState) if previousState is not None else None)}
        g_eventBus.handleEvent(events.RoleSkillEvent(events.RoleSkillEvent.STATE_CHANGED, ctx), scope=EVENT_BUS_SCOPE.BATTLE)
        return
