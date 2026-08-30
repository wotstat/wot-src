import BigWorld, Event

class ArenaInfoScoreSystemComponent(BigWorld.DynamicScriptComponent):

    def __init__(self, *args):
        self.onArenaScoreUpdated = Event.Event()
        return

    def set_totalScore(self, prev):
        self.onArenaScoreUpdated(self.totalScore)
        return
