class SoftException(Exception):
    pass


class DisabledServiceSoftException(SoftException):

    def __init__(self, message=b'disabledService'):
        super(DisabledServiceSoftException, self).__init__(message)
        self.message = message
        return
