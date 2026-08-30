from gui.impl.gen.view_models.views.lobby.platoon.platoon_dropdown_model import PlatoonDropdownModel

class ExtPlatoonDropdownModel(PlatoonDropdownModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=1):
        super(ExtPlatoonDropdownModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedDifficulty(self):
        return self._getNumber(10)

    def setSelectedDifficulty(self, value):
        self._setNumber(10, value)
        return

    def _initialize(self):
        super(ExtPlatoonDropdownModel, self)._initialize()
        self._addNumberProperty(b'selectedDifficulty', 1)
        return
