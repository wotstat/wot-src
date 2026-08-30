import sys
from json.tests import PyTest, CTest

class TestScanstring(object):

    def test_scanstring(self):
        scanstring = self.json.decoder.scanstring
        if sys.maxunicode == 65535:
            self.assertEqual(scanstring(u'"z\U0001d120x"', 1, None, True), (u'z\U0001d120x', 6))
        else:
            self.assertEqual(scanstring(u'"z\U0001d120x"', 1, None, True), (u'z\U0001d120x', 5))
        self.assertEqual(scanstring(b'"\\u007b"', 1, None, True), (u'{', 8))
        self.assertEqual(scanstring(b'"A JSON payload should be an object or array, not a string."', 1, None, True), (u'A JSON payload should be an object or array, not a string.', 60))
        self.assertEqual(scanstring(b'["Unclosed array"', 2, None, True), (u'Unclosed array', 17))
        self.assertEqual(scanstring(b'["extra comma",]', 2, None, True), (u'extra comma', 14))
        self.assertEqual(scanstring(b'["double extra comma",,]', 2, None, True), (u'double extra comma', 21))
        self.assertEqual(scanstring(b'["Comma after the close"],', 2, None, True), (u'Comma after the close', 24))
        self.assertEqual(scanstring(b'["Extra close"]]', 2, None, True), (u'Extra close', 14))
        self.assertEqual(scanstring(b'{"Extra comma": true,}', 2, None, True), (u'Extra comma', 14))
        self.assertEqual(scanstring(b'{"Extra value after close": true} "misplaced quoted value"', 2, None, True), (u'Extra value after close', 26))
        self.assertEqual(scanstring(b'{"Illegal expression": 1 + 2}', 2, None, True), (u'Illegal expression', 21))
        self.assertEqual(scanstring(b'{"Illegal invocation": alert()}', 2, None, True), (u'Illegal invocation', 21))
        self.assertEqual(scanstring(b'{"Numbers cannot have leading zeroes": 013}', 2, None, True), (u'Numbers cannot have leading zeroes', 37))
        self.assertEqual(scanstring(b'{"Numbers cannot be hex": 0x14}', 2, None, True), (u'Numbers cannot be hex', 24))
        self.assertEqual(scanstring(b'[[[[[[[[[[[[[[[[[[[["Too deep"]]]]]]]]]]]]]]]]]]]]', 21, None, True), (u'Too deep', 30))
        self.assertEqual(scanstring(b'{"Missing colon" null}', 2, None, True), (u'Missing colon', 16))
        self.assertEqual(scanstring(b'{"Double colon":: null}', 2, None, True), (u'Double colon', 15))
        self.assertEqual(scanstring(b'{"Comma instead of colon", null}', 2, None, True), (u'Comma instead of colon', 25))
        self.assertEqual(scanstring(b'["Colon instead of comma": false]', 2, None, True), (u'Colon instead of comma', 25))
        self.assertEqual(scanstring(b'["Bad value", truth]', 2, None, True), (u'Bad value', 12))
        return

    def test_surrogates(self):
        scanstring = self.json.decoder.scanstring

        def assertScan(given, expect):
            self.assertEqual(scanstring(given, 1, None, True), (
             expect, len(given)))
            if not isinstance(given, unicode):
                given = unicode(given)
                self.assertEqual(scanstring(given, 1, None, True), (
                 expect, len(given)))
            return

        surrogates = unichr(55348) + unichr(56608)
        assertScan(b'"z\\ud834\\u0079x"', u'z\ud834yx')
        assertScan(b'"z\\ud834\\udd20x"', u'z\U0001d120x')
        assertScan(b'"z\\ud834\\ud834\\udd20x"', u'z\ud834\U0001d120x')
        assertScan(b'"z\\ud834x"', u'z\ud834x')
        assertScan(u'"z\\ud834\udd20x12345"', u'z%sx12345' % surrogates)
        assertScan(b'"z\\udd20x"', u'z\udd20x')
        assertScan(u'"z\U0001d120x"', u'z\U0001d120x')
        assertScan(u'"z\ud834\\udd20x"', u'z%sx' % surrogates)
        assertScan(u'"z\ud834x"', u'z\ud834x')
        return

    def test_bad_escapes(self):
        scanstring = self.json.decoder.scanstring
        bad_escapes = [
         1, 
         2, 
         3, 
         4, 
         5, 
         6, 
         7, 
         8, 
         9, 
         10, 
         11, 
         12, 
         13, 
         14, 
         15, 
         16, 
         17, 
         18, 
         19, 
         20, 
         21, 
         22, 
         23]
        for s in bad_escapes:
            with self.assertRaises(ValueError):
                scanstring(s, 1, None, True)

        return

    def test_issue3623(self):
        self.assertRaises(ValueError, self.json.decoder.scanstring, b'xxx', 1, b'xxx')
        self.assertRaises(UnicodeDecodeError, self.json.encoder.encode_basestring_ascii, b'xx\xff')
        return

    def test_overflow(self):
        with self.assertRaises(OverflowError):
            self.json.decoder.scanstring(b'xxx', sys.maxsize + 1)
        return


class TestPyScanstring(TestScanstring, PyTest):
    pass


class TestCScanstring(TestScanstring, CTest):
    pass
