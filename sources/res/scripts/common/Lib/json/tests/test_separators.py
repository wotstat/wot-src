import textwrap
from json.tests import PyTest, CTest

class TestSeparators(object):

    def test_separators(self):
        h = [
         [
          b'blorpie'], [b'whoops'], [], b'd-shtaeou', b'd-nthiouh', b'i-vhbjkhnth', {b'nifty': 87}, {b'field': b'yes', b'morefield': False}]
        expect = textwrap.dedent(b'        [\n          [\n            "blorpie"\n          ] ,\n          [\n            "whoops"\n          ] ,\n          [] ,\n          "d-shtaeou" ,\n          "d-nthiouh" ,\n          "i-vhbjkhnth" ,\n          {\n            "nifty" : 87\n          } ,\n          {\n            "field" : "yes" ,\n            "morefield" : false\n          }\n        ]')
        d1 = self.dumps(h)
        d2 = self.dumps(h, indent=2, sort_keys=True, separators=(b' ,', b' : '))
        h1 = self.loads(d1)
        h2 = self.loads(d2)
        self.assertEqual(h1, h)
        self.assertEqual(h2, h)
        self.assertEqual(d2, expect)
        return


class TestPySeparators(TestSeparators, PyTest):
    pass


class TestCSeparators(TestSeparators, CTest):
    pass
