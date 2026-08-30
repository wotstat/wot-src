from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class FunRandomCustomShellSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(FunRandomCustomShellSlot, self).__init__(properties=properties, commands=commands)
        return

    def getCount(self):
        return self._getNumber(13)

    def setCount(self, value):
        self._setNumber(13, value)
        return

    def getOriginalIdx(self):
        return self._getNumber(14)

    def setOriginalIdx(self, value):
        self._setNumber(14, value)
        return

    def getImageNameOverride(self):
        return self._getString(15)

    def setImageNameOverride(self, value):
        self._setString(15, value)
        return

    def getTooltipOverride(self):
        return self._getString(16)

    def setTooltipOverride(self, value):
        self._setString(16, value)
        return

    def _initialize(self):
        super(FunRandomCustomShellSlot, self)._initialize()
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'originalIdx', 0)
        self._addStringProperty(b'imageNameOverride', b'')
        self._addStringProperty(b'tooltipOverride', b'')
        return
