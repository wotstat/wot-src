from Event import Event
from script_component.ScriptComponent import ScriptComponent

class StoryModeAvatarComponent(ScriptComponent):
    onSMAbilityWrongPoint = Event()
    onPositionValidChanged = Event()

    def set_wrongApplicationPoint(self, _):
        self.onSMAbilityWrongPoint(self.wrongApplicationPoint)
        return

    def set_isPositionValid(self, prevValue):
        self.onPositionValidChanged()
        return

    def checkPositionForEquipment(self, equipmentId, position):
        self.cell.checkPositionForEquipment(equipmentId, position)
        return
