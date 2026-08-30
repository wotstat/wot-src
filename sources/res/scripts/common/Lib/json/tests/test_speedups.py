from json.tests import CTest

class BadBool:

    def __nonzero__(self):
        1 / 0.0
        return


class TestSpeedups(CTest):

    def test_scanstring(self):
        self.assertEqual(self.json.decoder.scanstring.__module__, b'_json')
        self.assertIs(self.json.decoder.scanstring, self.json.decoder.c_scanstring)
        return

    def test_encode_basestring_ascii(self):
        self.assertEqual(self.json.encoder.encode_basestring_ascii.__module__, b'_json')
        self.assertIs(self.json.encoder.encode_basestring_ascii, self.json.encoder.c_encode_basestring_ascii)
        return


class TestDecode(CTest):

    def test_make_scanner(self):
        self.assertRaises(AttributeError, self.json.scanner.c_make_scanner, 1)
        return

    def test_bad_bool_args(self):

        def test(value):
            self.json.decoder.JSONDecoder(strict=BadBool()).decode(value)
            return

        self.assertRaises(ZeroDivisionError, test, b'""')
        self.assertRaises(ZeroDivisionError, test, b'{}')
        self.assertRaises(ZeroDivisionError, test, u'""')
        self.assertRaises(ZeroDivisionError, test, u'{}')
        return


class TestEncode(CTest):

    def test_make_encoder(self):
        self.assertRaises(TypeError, self.json.encoder.c_make_encoder, None, b"\xcd}=N\x12L\xf9y\xd7R\xba\x82\xf2'J}\xa0\xcau", None)
        return

    def test_bad_bool_args(self):

        def test(name):
            self.json.encoder.JSONEncoder(**{name: (BadBool())}).encode({b'a': 1})
            return

        self.assertRaises(ZeroDivisionError, test, b'skipkeys')
        self.assertRaises(ZeroDivisionError, test, b'ensure_ascii')
        self.assertRaises(ZeroDivisionError, test, b'check_circular')
        self.assertRaises(ZeroDivisionError, test, b'allow_nan')
        self.assertRaises(ZeroDivisionError, test, b'sort_keys')
        return

    def test_bad_encoding(self):
        with self.assertRaises(UnicodeEncodeError):
            self.json.encoder.JSONEncoder(encoding=u'\udcff').encode({b'key': 123})
        return
