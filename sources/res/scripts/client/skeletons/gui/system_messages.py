class ISystemMessages(object):

    def init(self):
        raise NotImplementedError
        return

    def destroy(self):
        raise NotImplementedError
        return

    @property
    def proto(self):
        raise NotImplementedError
        return

    def pushMessage(self, text, type, priority=None, messageData=None, savedData=None):
        raise NotImplementedError
        return

    def pushI18nMessage(self, key, *args, **kwargs):
        raise NotImplementedError
        return
