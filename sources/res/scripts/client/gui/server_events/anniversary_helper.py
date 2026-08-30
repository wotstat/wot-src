ANNIVERSARY_EVENT_PREFIX = b'anniversary_ga'

def getEventNameByQuest(quest):
    if quest.getID().startswith(ANNIVERSARY_EVENT_PREFIX):
        return ANNIVERSARY_EVENT_PREFIX
    else:
        return
