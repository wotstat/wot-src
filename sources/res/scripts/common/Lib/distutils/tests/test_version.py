import unittest
from distutils.version import LooseVersion
from distutils.version import StrictVersion
from test.test_support import run_unittest

class VersionTestCase(unittest.TestCase):

    def test_prerelease(self):
        version = StrictVersion(b'1.2.3a1')
        self.assertEqual(version.version, (1, 2, 3))
        self.assertEqual(version.prerelease, (b'a', 1))
        self.assertEqual(str(version), b'1.2.3a1')
        version = StrictVersion(b'1.2.0')
        self.assertEqual(str(version), b'1.2')
        return

    def test_cmp_strict(self):
        versions = ((b'1.5.1', b'1.5.2b2', -1),
         (
          b'161', b'3.10a', ValueError),
         (b'8.02', b'8.02', 0),
         (
          b'3.4j', b'1996.07.12', ValueError),
         (
          b'3.2.pl0', b'3.1.1.6', ValueError),
         (
          b'2g6', b'11g', ValueError),
         (b'0.9', b'2.2', -1),
         (b'1.2.1', b'1.2', 1),
         (b'1.1', b'1.2.2', -1),
         (b'1.2', b'1.1', 1),
         (b'1.2.1', b'1.2.2', -1),
         (b'1.2.2', b'1.2', 1),
         (b'1.2', b'1.2.2', -1),
         (b'0.4.0', b'0.4', 0),
         (
          b'1.13++', b'5.5.kw', ValueError))
        for v1, v2, wanted in versions:
            try:
                res = StrictVersion(v1).__cmp__(StrictVersion(v2))
            except ValueError:
                if wanted is ValueError:
                    continue
                else:
                    raise AssertionError(b"cmp(%s, %s) shouldn't raise ValueError" % (
                     v1, v2))

            self.assertEqual(res, wanted, b'cmp(%s, %s) should be %s, got %s' % (
             v1, v2, wanted, res))

        return

    def test_cmp(self):
        versions = ((b'1.5.1', b'1.5.2b2', -1),
         (b'161', b'3.10a', 1),
         (b'8.02', b'8.02', 0),
         (b'3.4j', b'1996.07.12', -1),
         (b'3.2.pl0', b'3.1.1.6', 1),
         (b'2g6', b'11g', -1),
         (b'0.960923', b'2.2beta29', -1),
         (b'1.13++', b'5.5.kw', -1))
        for v1, v2, wanted in versions:
            res = LooseVersion(v1).__cmp__(LooseVersion(v2))
            self.assertEqual(res, wanted, b'cmp(%s, %s) should be %s, got %s' % (
             v1, v2, wanted, res))

        return


def test_suite():
    return unittest.makeSuite(VersionTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
