from frameworks.wulf import ViewModel

class EventBannerState(ViewModel):
    __slots__ = ()
    ANNOUNCE = b'announce'
    INTRO = b'intro'
    IN_PROGRESS = b'inProgress'
    INACTIVE = b'inactive'
    FINISHED = b'finished'

    def __init__(self, properties=0, commands=0):
        super(EventBannerState, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(EventBannerState, self)._initialize()
        return
