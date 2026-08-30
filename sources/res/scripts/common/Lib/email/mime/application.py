__all__ = [
 b'MIMEApplication']
from email import encoders
from email.mime.nonmultipart import MIMENonMultipart

class MIMEApplication(MIMENonMultipart):

    def __init__(self, _data, _subtype=b'octet-stream', _encoder=encoders.encode_base64, **_params):
        if _subtype is None:
            raise TypeError(b'Invalid application MIME subtype')
        MIMENonMultipart.__init__(self, b'application', _subtype, **_params)
        self.set_payload(_data)
        _encoder(self)
        return
