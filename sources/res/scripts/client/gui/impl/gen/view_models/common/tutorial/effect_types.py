from frameworks.wulf import ViewModel

class EffectTypes(ViewModel):
    __slots__ = ()
    HINT = b'hint'
    BOOTCAMP_HINT = b'bootcampHint'
    DISPLAY = b'display'
    TWEEN = b'tween'
    CLIP = b'clip'
    ENABLED = b'enabled'
    OVERLAY = b'overlay'
    DEFAULT_OVERLAY = b'defaultOverlay'
    LAYOUT = b'layout'

    def __init__(self, properties=0, commands=0):
        super(EffectTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EffectTypes, self)._initialize()
        return
