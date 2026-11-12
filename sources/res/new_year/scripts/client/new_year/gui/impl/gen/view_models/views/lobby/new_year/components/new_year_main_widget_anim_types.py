from frameworks.wulf import ViewModel

class NewYearMainWidgetAnimTypes(ViewModel):
    __slots__ = ()
    ANIM_TYPE_NONE = b'none'
    ANIM_TYPE_UP = b'up'
    ANIM_TYPE_DOWN = b'down'
    ANIM_TYPE_UP_LONG = b'upLong'
    ANIM_TYPE_DOWN_LONG = b'downLong'

    def __init__(self, properties=0, commands=0):
        super(NewYearMainWidgetAnimTypes, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(NewYearMainWidgetAnimTypes, self)._initialize()
        return
