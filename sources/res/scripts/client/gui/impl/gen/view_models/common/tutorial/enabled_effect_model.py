from gui.impl.gen.view_models.common.tutorial.effect_model import EffectModel

class EnabledEffectModel(EffectModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(EnabledEffectModel, self).__init__(properties=properties, commands=commands)
        return

    def getEnabled(self):
        return self._getBool(4)

    def setEnabled(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(EnabledEffectModel, self)._initialize()
        self._addBoolProperty(b'enabled', False)
        return
