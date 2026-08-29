from gui.shared.event_bus import SharedEvent

class StoryModeViewReadyEvent(SharedEvent):
    VIEW_READY = b'StoryModeViewReadyEvent.VIEW_READY'

    def __init__(self, viewID):
        super(StoryModeViewReadyEvent, self).__init__(self.VIEW_READY)
        self.viewID = viewID
        return
