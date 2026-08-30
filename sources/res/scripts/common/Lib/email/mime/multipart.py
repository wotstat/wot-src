__all__ = [
 b'MIMEMultipart']
from email.mime.base import MIMEBase

class MIMEMultipart(MIMEBase):

    def __init__(self, _subtype=b'mixed', boundary=None, _subparts=None, **_params):
        MIMEBase.__init__(self, b'multipart', _subtype, **_params)
        self._payload = []
        if _subparts:
            for p in _subparts:
                self.attach(p)

        if boundary:
            self.set_boundary(boundary)
        return
