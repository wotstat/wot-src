import unittest
from test.test_support import run_unittest
from email.test.test_email import TestEmailBase
from email.charset import Charset
from email.header import Header, decode_header
from email.message import Message
try:
    unicode(b'foo', b'euc-jp')
except LookupError:
    raise unittest.SkipTest

class TestEmailAsianCodecs(TestEmailBase):

    def test_japanese_codecs(self):
        eq = self.ndiffAssertEqual
        j = Charset(b'euc-jp')
        g = Charset(b'iso-8859-1')
        h = Header(b'Hello World!')
        jhello = b'\xa5\xcf\xa5\xed\xa1\xbc\xa5\xef\xa1\xbc\xa5\xeb\xa5\xc9\xa1\xaa'
        ghello = b'Gr\xfc\xdf Gott!'
        h.append(jhello, j)
        h.append(ghello, g)
        eq(h.encode(), b'Hello World! =?iso-2022-jp?b?GyRCJU8lbSE8JW8hPCVrJUkhKhsoQg==?=\n =?iso-8859-1?q?Gr=FC=DF?= =?iso-8859-1?q?_Gott!?=')
        eq(decode_header(h.encode()), [
         (b'Hello World!', None),
         (b'\x1b$B%O%m!<%o!<%k%I!*\x1b(B', b'iso-2022-jp'),
         (b'Gr\xfc\xdf Gott!', b'iso-8859-1')])
        long = b'test-ja \xa4\xd8\xc5\xea\xb9\xc6\xa4\xb5\xa4\xec\xa4\xbf\xa5\xe1\xa1\xbc\xa5\xeb\xa4\xcf\xbb\xca\xb2\xf1\xbc\xd4\xa4\xce\xbe\xb5\xc7\xa7\xa4\xf2\xc2\xd4\xa4\xc3\xa4\xc6\xa4\xa4\xa4\xde\xa4\xb9'
        h = Header(long, j, header_name=b'Subject')
        enc = h.encode()
        eq(enc, b'=?iso-2022-jp?b?dGVzdC1qYSAbJEIkWEVqOUYkNSRsJD8lYSE8JWskTztKGyhC?=\n =?iso-2022-jp?b?GyRCMnE8VCROPjVHJyRyQlQkQyRGJCQkXiQ5GyhC?=')
        eq(h.__unicode__().encode(b'euc-jp'), long)
        return

    def test_payload_encoding(self):
        jhello = b'\xa5\xcf\xa5\xed\xa1\xbc\xa5\xef\xa1\xbc\xa5\xeb\xa5\xc9\xa1\xaa'
        jcode = b'euc-jp'
        msg = Message()
        msg.set_payload(jhello, jcode)
        ustr = unicode(msg.get_payload(), msg.get_content_charset())
        self.assertEqual(jhello, ustr.encode(jcode))
        return


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestEmailAsianCodecs))
    return suite


def test_main():
    run_unittest(TestEmailAsianCodecs)
    return


if __name__ == b'__main__':
    unittest.main(defaultTest=b'suite')
