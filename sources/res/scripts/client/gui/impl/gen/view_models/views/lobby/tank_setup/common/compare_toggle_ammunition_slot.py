from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class CompareToggleAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(CompareToggleAmmunitionSlot, self).__init__(properties=properties, commands=commands)
        return

    def getIsSelected(self):
        return self._getBool(13)

    def setIsSelected(self, value):
        self._setBool(13, value)
        return

    def getIsLocked(self):
        return self._getBool(14)

    def setIsLocked(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(CompareToggleAmmunitionSlot, self)._initialize()
        self._addBoolProperty(b'isSelected', False)
        self._addBoolProperty(b'isLocked', False)
        return
