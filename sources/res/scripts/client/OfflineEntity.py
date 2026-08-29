import BigWorld

class OfflineEntity(BigWorld.Entity):
    inputHandler = None

    def __init__(self):
        return

    def prerequisites(self):
        return []

    def onEnterWorld(self, prereqs):
        return

    def onLeaveWorld(self):
        return

    def handleKeyEvent(self, event):
        return False
