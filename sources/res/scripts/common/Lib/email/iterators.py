__all__ = [
 b'body_line_iterator',
 b'typed_subpart_iterator',
 b'walk']
import sys
from cStringIO import StringIO

def walk(self):
    yield self
    if self.is_multipart():
        for subpart in self.get_payload():
            for subsubpart in subpart.walk():
                yield subsubpart

    return


def body_line_iterator(msg, decode=False):
    for subpart in msg.walk():
        payload = subpart.get_payload(decode=decode)
        if isinstance(payload, basestring):
            for line in StringIO(payload):
                yield line

    return


def typed_subpart_iterator(msg, maintype=b'text', subtype=None):
    for subpart in msg.walk():
        if subpart.get_content_maintype() == maintype:
            if subtype is None or subpart.get_content_subtype() == subtype:
                yield subpart

    return


def _structure(msg, fp=None, level=0, include_default=False):
    if fp is None:
        fp = sys.stdout
    tab = b' ' * (level * 4)
    print >> fp, tab + msg.get_content_type(),
    if include_default:
        print >> fp, b'[%s]' % msg.get_default_type()
    else:
        print >> fp
    if msg.is_multipart():
        for subpart in msg.get_payload():
            _structure(subpart, fp, level + 1, include_default)

    return
