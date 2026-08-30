import SoundGroups

class SoundStatesSwitcher(object):

    def __init__(self, soundGroup, startState, stopState):
        super(SoundStatesSwitcher, self).__init__()
        self.soundGroup = soundGroup
        self.startState = startState
        self.stopState = stopState
        self.active = False
        return

    def enable(self):
        if self.active:
            return
        SoundGroups.g_instance.setState(self.soundGroup, self.startState)
        self.active = True
        return

    def disable(self):
        if not self.active:
            return
        self.active = False
        SoundGroups.g_instance.setState(self.soundGroup, self.stopState)
        return
