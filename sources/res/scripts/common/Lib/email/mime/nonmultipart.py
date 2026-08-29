__all__ = [
 b'MIMENonMultipart']
from email import errors
from email.mime.base import MIMEBase

class MIMENonMultipart(MIMEBase):

    def attach(self, payload):
        raise errors.MultipartConversionError(b'Cannot attach additional subparts to non-multipart/*')
        return
