__all__ = [
 b'encode_7or8bit',
 b'encode_base64',
 b'encode_noop',
 b'encode_quopri']
import base64
from quopri import encodestring as _encodestring

def _qencode(s):
    enc = _encodestring(s, quotetabs=True)
    return enc.replace(b' ', b'=20')


def _bencode(s):
    if not s:
        return s
    hasnewline = s[-1] == b'\n'
    value = base64.encodestring(s)
    if not hasnewline and value[-1] == b'\n':
        return value[:-1]
    return value


def encode_base64(msg):
    orig = msg.get_payload()
    encdata = _bencode(orig)
    msg.set_payload(encdata)
    msg[b'Content-Transfer-Encoding'] = b'base64'
    return


def encode_quopri(msg):
    orig = msg.get_payload()
    encdata = _qencode(orig)
    msg.set_payload(encdata)
    msg[b'Content-Transfer-Encoding'] = b'quoted-printable'
    return


def encode_7or8bit(msg):
    orig = msg.get_payload()
    if orig is None:
        msg[b'Content-Transfer-Encoding'] = b'7bit'
        return
    else:
        try:
            orig.encode(b'ascii')
        except UnicodeError:
            msg[b'Content-Transfer-Encoding'] = b'8bit'
        else:
            msg[b'Content-Transfer-Encoding'] = b'7bit'

        return


def encode_noop(msg):
    return
