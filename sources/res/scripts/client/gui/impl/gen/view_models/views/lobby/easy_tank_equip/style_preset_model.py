from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.preset_model import PresetModel

class StylePresetModel(PresetModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(StylePresetModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(5)

    def setName(self, value):
        self._setString(5, value)
        return

    def getImage(self):
        return self._getString(6)

    def setImage(self, value):
        self._setString(6, value)
        return

    def getRentDuration(self):
        return self._getNumber(7)

    def setRentDuration(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(StylePresetModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'image', b'')
        self._addNumberProperty(b'rentDuration', 0)
        return
