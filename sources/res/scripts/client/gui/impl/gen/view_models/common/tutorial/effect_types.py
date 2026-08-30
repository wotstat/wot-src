from frameworks.wulf import ViewModel

class EffectTypes(ViewModel):
    __slots__ = ()
    HINT = b'hint'
    DISPLAY = b'display'
    ENABLED = b'enabled'
    OVERLAY = b'overlay'

    def __init__(self, properties=0, commands=0):
        super(EffectTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EffectTypes, self)._initialize()
        return
