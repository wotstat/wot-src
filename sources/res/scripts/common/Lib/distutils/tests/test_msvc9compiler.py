import sys, unittest, os
from distutils.errors import DistutilsPlatformError
from distutils.tests import support
from test.test_support import run_unittest
_MANIFEST_WITH_ONLY_MSVC_REFERENCE = b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assembly xmlns="urn:schemas-microsoft-com:asm.v1"\n          manifestVersion="1.0">\n  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">\n    <security>\n      <requestedPrivileges>\n        <requestedExecutionLevel level="asInvoker" uiAccess="false">\n        </requestedExecutionLevel>\n      </requestedPrivileges>\n    </security>\n  </trustInfo>\n  <dependency>\n    <dependentAssembly>\n      <assemblyIdentity type="win32" name="Microsoft.VC90.CRT"\n         version="9.0.21022.8" processorArchitecture="x86"\n         publicKeyToken="XXXX">\n      </assemblyIdentity>\n    </dependentAssembly>\n  </dependency>\n</assembly>\n'
_MANIFEST_WITH_MULTIPLE_REFERENCES = b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assembly xmlns="urn:schemas-microsoft-com:asm.v1"\n          manifestVersion="1.0">\n  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">\n    <security>\n      <requestedPrivileges>\n        <requestedExecutionLevel level="asInvoker" uiAccess="false">\n        </requestedExecutionLevel>\n      </requestedPrivileges>\n    </security>\n  </trustInfo>\n  <dependency>\n    <dependentAssembly>\n      <assemblyIdentity type="win32" name="Microsoft.VC90.CRT"\n         version="9.0.21022.8" processorArchitecture="x86"\n         publicKeyToken="XXXX">\n      </assemblyIdentity>\n    </dependentAssembly>\n  </dependency>\n  <dependency>\n    <dependentAssembly>\n      <assemblyIdentity type="win32" name="Microsoft.VC90.MFC"\n        version="9.0.21022.8" processorArchitecture="x86"\n        publicKeyToken="XXXX"></assemblyIdentity>\n    </dependentAssembly>\n  </dependency>\n</assembly>\n'
_CLEANED_MANIFEST = b'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<assembly xmlns="urn:schemas-microsoft-com:asm.v1"\n          manifestVersion="1.0">\n  <trustInfo xmlns="urn:schemas-microsoft-com:asm.v3">\n    <security>\n      <requestedPrivileges>\n        <requestedExecutionLevel level="asInvoker" uiAccess="false">\n        </requestedExecutionLevel>\n      </requestedPrivileges>\n    </security>\n  </trustInfo>\n  <dependency>\n\n  </dependency>\n  <dependency>\n    <dependentAssembly>\n      <assemblyIdentity type="win32" name="Microsoft.VC90.MFC"\n        version="9.0.21022.8" processorArchitecture="x86"\n        publicKeyToken="XXXX"></assemblyIdentity>\n    </dependentAssembly>\n  </dependency>\n</assembly>'
if sys.platform == b'win32':
    from distutils.msvccompiler import get_build_version
    if get_build_version() >= 8.0:
        SKIP_MESSAGE = None
    else:
        SKIP_MESSAGE = b'These tests are only for MSVC8.0 or above'
else:
    SKIP_MESSAGE = b'These tests are only for win32'

@unittest.skipUnless(SKIP_MESSAGE is None, SKIP_MESSAGE)
class msvc9compilerTestCase(support.TempdirManager, unittest.TestCase):

    def test_no_compiler(self):
        from distutils.msvc9compiler import query_vcvarsall

        def _find_vcvarsall(version):
            return

        from distutils import msvc9compiler
        old_find_vcvarsall = msvc9compiler.find_vcvarsall
        msvc9compiler.find_vcvarsall = _find_vcvarsall
        try:
            self.assertRaises(DistutilsPlatformError, query_vcvarsall, b'wont find this version')
        finally:
            msvc9compiler.find_vcvarsall = old_find_vcvarsall

        return

    def test_reg_class(self):
        from distutils.msvc9compiler import Reg
        self.assertRaises(KeyError, Reg.get_value, b'xxx', b'xxx')
        path = b'Control Panel\\Desktop'
        v = Reg.get_value(path, u'dragfullwindows')
        self.assertIn(v, (u'0', u'1', u'2'))
        import _winreg
        HKCU = _winreg.HKEY_CURRENT_USER
        keys = Reg.read_keys(HKCU, b'xxxx')
        self.assertEqual(keys, None)
        keys = Reg.read_keys(HKCU, b'Control Panel')
        self.assertIn(b'Desktop', keys)
        return

    def test_remove_visual_c_ref(self):
        from distutils.msvc9compiler import MSVCCompiler
        tempdir = self.mkdtemp()
        manifest = os.path.join(tempdir, b'manifest')
        f = open(manifest, b'w')
        try:
            f.write(_MANIFEST_WITH_MULTIPLE_REFERENCES)
        finally:
            f.close()

        compiler = MSVCCompiler()
        compiler._remove_visual_c_ref(manifest)
        f = open(manifest)
        try:
            content = (b'\n').join([line.rstrip() for line in f.readlines()])
        finally:
            f.close()

        self.assertEqual(content, _CLEANED_MANIFEST)
        return

    def test_remove_entire_manifest(self):
        from distutils.msvc9compiler import MSVCCompiler
        tempdir = self.mkdtemp()
        manifest = os.path.join(tempdir, b'manifest')
        f = open(manifest, b'w')
        try:
            f.write(_MANIFEST_WITH_ONLY_MSVC_REFERENCE)
        finally:
            f.close()

        compiler = MSVCCompiler()
        got = compiler._remove_visual_c_ref(manifest)
        self.assertIsNone(got)
        return


def test_suite():
    return unittest.makeSuite(msvc9compilerTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
