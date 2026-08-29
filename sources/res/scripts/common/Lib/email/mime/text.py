__all__ = [
 b'MIMEText']
from email.encoders import encode_7or8bit
from email.mime.nonmultipart import MIMENonMultipart

class MIMEText(MIMENonMultipart):

    def __init__(self, _text, _subtype=b'plain', _charset=b'us-ascii'):
        MIMENonMultipart.__init__(self, b'text', _subtype, **{b'charset': _charset})
        self.set_payload(_text, _charset)
        return
