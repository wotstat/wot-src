__all__ = [
 b'Parser', b'HeaderParser']
import warnings
from cStringIO import StringIO
from email.feedparser import FeedParser
from email.message import Message

class Parser:

    def __init__(self, *args, **kws):
        if len(args) >= 1:
            if b'_class' in kws:
                raise TypeError(b"Multiple values for keyword arg '_class'")
            kws[b'_class'] = args[0]
        if len(args) == 2:
            if b'strict' in kws:
                raise TypeError(b"Multiple values for keyword arg 'strict'")
            kws[b'strict'] = args[1]
        if len(args) > 2:
            raise TypeError(b'Too many arguments')
        if b'_class' in kws:
            self._class = kws[b'_class']
            del kws[b'_class']
        else:
            self._class = Message
        if b'strict' in kws:
            warnings.warn(b"'strict' argument is deprecated (and ignored)", DeprecationWarning, 2)
            del kws[b'strict']
        if kws:
            raise TypeError(b'Unexpected keyword arguments')
        return

    def parse(self, fp, headersonly=False):
        feedparser = FeedParser(self._class)
        if headersonly:
            feedparser._set_headersonly()
        while True:
            data = fp.read(8192)
            if not data:
                break
            feedparser.feed(data)

        return feedparser.close()

    def parsestr(self, text, headersonly=False):
        return self.parse(StringIO(text), headersonly=headersonly)


class HeaderParser(Parser):

    def parse(self, fp, headersonly=True):
        return Parser.parse(self, fp, True)

    def parsestr(self, text, headersonly=True):
        return Parser.parsestr(self, text, True)
