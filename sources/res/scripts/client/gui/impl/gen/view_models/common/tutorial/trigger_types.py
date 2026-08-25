from frameworks.wulf import ViewModel

class TriggerTypes(ViewModel):
    __slots__ = ()
    CLICK_TYPE = b'click'
    CLICK_OUTSIDE_TYPE = b'clickOutside'
    ESCAPE = b'escape'
    ENABLED = b'enabled'
    DISABLED = b'disabled'
    ENABLED_CHANGE = b'enabled_change'
    VISIBLE_CHANGE = b'visible_change'

    def __init__(self, properties=0, commands=0):
        super(TriggerTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(TriggerTypes, self)._initialize()
        return
