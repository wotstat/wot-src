from constants import NC_MESSAGE_PRIORITY

class NotificationPriorityLevel(object):
    HIGH = b'high'
    MEDIUM = b'medium'
    LOW = b'low'
    RANGE = (
     HIGH, MEDIUM, LOW)
    NC_MAPPING = {(NC_MESSAGE_PRIORITY.HIGH): HIGH, 
       (NC_MESSAGE_PRIORITY.MEDIUM): MEDIUM, 
       (NC_MESSAGE_PRIORITY.LOW): LOW}

    @classmethod
    def convertFromNC(cls, priority):
        result = NotificationPriorityLevel.MEDIUM
        if priority in cls.NC_MAPPING:
            result = cls.NC_MAPPING[priority]
        return result


class NotificationGroup(object):
    INFO = b'info'
    INVITE = b'invite'
    OFFER = b'offer'
    ALL = (INFO, INVITE, OFFER)


class NotificationGuiSettings(object):
    __slots__ = (b'isNotify', b'priorityLevel', b'isAlert', b'auxData', b'showAt', b'__customEvent', b'groupID', b'messageType', b'messageSubtype', b'decorator', b'lifeTime', b'isSoundable')

    def __init__(self, isNotify=False, priorityLevel=NotificationPriorityLevel.MEDIUM, isAlert=False, auxData=None, showAt=0, groupID=NotificationGroup.INFO, messageType=None, messageSubtype=None, decorator=None, lifeTime=0, isSoundable=False):
        super(NotificationGuiSettings, self).__init__()
        self.isNotify = isNotify
        self.priorityLevel = priorityLevel
        self.isAlert = isAlert
        self.auxData = auxData or []
        self.showAt = showAt
        self.groupID = groupID
        self.messageType = messageType
        self.messageSubtype = messageSubtype
        self.decorator = decorator
        self.lifeTime = lifeTime
        self.__customEvent = None
        self.isSoundable = isSoundable
        return

    def setCustomEvent(self, eType, ctx=None):
        self.__customEvent = (eType, ctx)
        return

    def getCustomEvent(self):
        return self.__customEvent
