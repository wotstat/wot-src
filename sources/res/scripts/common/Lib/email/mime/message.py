__all__ = [
 b'MIMEMessage']
from email import message
from email.mime.nonmultipart import MIMENonMultipart

class MIMEMessage(MIMENonMultipart):

    def __init__(self, _msg, _subtype=b'rfc822'):
        MIMENonMultipart.__init__(self, b'message', _subtype)
        if not isinstance(_msg, message.Message):
            raise TypeError(b'Argument is not an instance of Message')
        message.Message.attach(self, _msg)
        self.set_default_type(b'message/rfc822')
        return
