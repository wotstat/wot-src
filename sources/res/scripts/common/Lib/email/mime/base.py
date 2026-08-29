__all__ = [
 b'MIMEBase']
from email import message

class MIMEBase(message.Message):

    def __init__(self, _maintype, _subtype, **_params):
        message.Message.__init__(self)
        ctype = b'%s/%s' % (_maintype, _subtype)
        self.add_header(b'Content-Type', ctype, **_params)
        self[b'MIME-Version'] = b'1.0'
        return
