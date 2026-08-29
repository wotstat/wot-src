class _EventBoardSettings(object):

    def __init__(self):
        self.__minimized = {}
        return

    def isGroupMinimized(self, event):
        groupID = event.getEventID()
        if groupID in self.__minimized:
            return self.__minimized[groupID]
        return event.isFinished()

    def updateExpanded(self, event, value):
        groupID = event.getEventID()
        self.__minimized[groupID] = not value
        return


_settings = _EventBoardSettings()

def isGroupMinimized(event):
    return _settings.isGroupMinimized(event)


def expandGroup(event, isExpanded):
    _settings.updateExpanded(event, isExpanded)
    return
