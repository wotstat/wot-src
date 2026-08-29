import os, sys, unittest
from ctypes.macholib.dyld import dyld_find

def find_lib(name):
    possible = [
     b'lib' + name + b'.dylib', name + b'.dylib', name + b'.framework/' + name]
    for dylib in possible:
        try:
            return os.path.realpath(dyld_find(dylib))
        except ValueError:
            pass

    raise ValueError(b'%s not found' % (name,))
    return


class MachOTest(unittest.TestCase):

    @unittest.skipUnless(sys.platform == b'darwin', b'OSX-specific test')
    def test_find(self):
        self.assertEqual(find_lib(b'pthread'), b'/usr/lib/libSystem.B.dylib')
        result = find_lib(b'z')
        self.assertRegexpMatches(result, b'.*/lib/libz\\..*.*\\.dylib')
        self.assertEqual(find_lib(b'IOKit'), b'/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit')
        return


if __name__ == b'__main__':
    unittest.main()
