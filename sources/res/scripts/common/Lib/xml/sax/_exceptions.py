import sys
if sys.platform[:4] == b'java':
    from java.lang import Exception
del sys

class SAXException(Exception):

    def __init__(self, msg, exception=None):
        self._msg = msg
        self._exception = exception
        Exception.__init__(self, msg)
        return

    def getMessage(self):
        return self._msg

    def getException(self):
        return self._exception

    def __str__(self):
        return self._msg

    def __getitem__(self, ix):
        raise AttributeError(b'__getitem__')
        return


class SAXParseException(SAXException):

    def __init__(self, msg, exception, locator):
        SAXException.__init__(self, msg, exception)
        self._locator = locator
        self._systemId = self._locator.getSystemId()
        self._colnum = self._locator.getColumnNumber()
        self._linenum = self._locator.getLineNumber()
        return

    def getColumnNumber(self):
        return self._colnum

    def getLineNumber(self):
        return self._linenum

    def getPublicId(self):
        return self._locator.getPublicId()

    def getSystemId(self):
        return self._systemId

    def __str__(self):
        sysid = self.getSystemId()
        if sysid is None:
            sysid = b'<unknown>'
        linenum = self.getLineNumber()
        if linenum is None:
            linenum = b'?'
        colnum = self.getColumnNumber()
        if colnum is None:
            colnum = b'?'
        return b'%s:%s:%s: %s' % (sysid, linenum, colnum, self._msg)


class SAXNotRecognizedException(SAXException):
    pass


class SAXNotSupportedException(SAXException):
    pass


class SAXReaderNotAvailable(SAXNotSupportedException):
    pass
