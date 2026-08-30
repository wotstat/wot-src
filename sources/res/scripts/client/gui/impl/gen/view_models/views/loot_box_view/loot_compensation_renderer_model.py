from gui.impl.gen.view_models.views.loot_box_view.loot_animated_renderer_model import LootAnimatedRendererModel

class LootCompensationRendererModel(LootAnimatedRendererModel):
    __slots__ = ()

    def __init__(self, properties=25, commands=0):
        super(LootCompensationRendererModel, self).__init__(properties=properties, commands=commands)
        return

    def getIconFrom(self):
        return self._getString(16)

    def setIconFrom(self, value):
        self._setString(16, value)
        return

    def getLabelBeforeStr(self):
        return self._getString(17)

    def setLabelBeforeStr(self, value):
        self._setString(17, value)
        return

    def getIconBefore(self):
        return self._getString(18)

    def setIconBefore(self, value):
        self._setString(18, value)
        return

    def getIconAfter(self):
        return self._getString(19)

    def setIconAfter(self, value):
        self._setString(19, value)
        return

    def getLabelBefore(self):
        return self._getString(20)

    def setLabelBefore(self, value):
        self._setString(20, value)
        return

    def getLabelAfter(self):
        return self._getString(21)

    def setLabelAfter(self, value):
        self._setString(21, value)
        return

    def getBonusName(self):
        return self._getString(22)

    def setBonusName(self, value):
        self._setString(22, value)
        return

    def getCountBefore(self):
        return self._getNumber(23)

    def setCountBefore(self, value):
        self._setNumber(23, value)
        return

    def getLabelAlignAfter(self):
        return self._getString(24)

    def setLabelAlignAfter(self, value):
        self._setString(24, value)
        return

    def _initialize(self):
        super(LootCompensationRendererModel, self)._initialize()
        self._addStringProperty(b'iconFrom', b'')
        self._addStringProperty(b'labelBeforeStr', b'')
        self._addStringProperty(b'iconBefore', b'')
        self._addStringProperty(b'iconAfter', b'')
        self._addStringProperty(b'labelBefore', b'')
        self._addStringProperty(b'labelAfter', b'')
        self._addStringProperty(b'bonusName', b'')
        self._addNumberProperty(b'countBefore', 1)
        self._addStringProperty(b'labelAlignAfter', b'center')
        return
