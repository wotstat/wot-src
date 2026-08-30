class IHasID(object):

    def getID(self):
        raise NotImplementedError
        return

    def setID(self, entityID):
        raise NotImplementedError
        return

    def clear(self):
        return


class IHasTargetID(object):

    def getTargetID(self):
        raise NotImplementedError
        return

    def setTargetID(self, targetID):
        raise NotImplementedError
        return


class HasID(IHasID):

    def __init__(self, entityID=None, entityType=0, **kwargs):
        super(HasID, self).__init__(**kwargs)
        self._id = entityID
        self._type = entityType
        return

    def getID(self):
        return self._id

    def getType(self):
        return self._type

    def setID(self, entityID):
        self._id = entityID
        return


class HasTargetID(IHasTargetID):

    def __init__(self, targetID, **kwargs):
        super(HasTargetID, self).__init__(**kwargs)
        self._targetID = targetID
        return

    def getTargetID(self):
        return self._targetID

    def setTargetID(self, targetID):
        self._targetID = targetID
        return


class HasIDAndTarget(HasID, HasTargetID):

    def __init__(self, entityID=None, targetID=None, entityType=0):
        super(HasIDAndTarget, self).__init__(entityID=entityID, targetID=targetID, entityType=entityType)
        self._targetID = targetID
        return
