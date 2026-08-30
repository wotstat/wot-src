from gui.impl.gen.view_models.views.lobby.platoon.button_model import ButtonModel

class ButtonSwitchReadyModel(ButtonModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=1):
        super(ButtonSwitchReadyModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsRed(self):
        return self._getBool(6)

    def setIsRed(self, value):
        self._setBool(6, value)
        return

    def getTooltipHeader(self):
        return self._getString(7)

    def setTooltipHeader(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(ButtonSwitchReadyModel, self)._initialize()
        self._addBoolProperty(b'isRed', False)
        self._addStringProperty(b'tooltipHeader', b'')
        return
