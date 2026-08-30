import os, unittest
from test.test_support import captured_stdout
from distutils.ccompiler import gen_lib_options, CCompiler, get_default_compiler
from distutils.sysconfig import customize_compiler
from distutils import debug
from distutils.tests import support

class FakeCompiler(object):

    def library_dir_option(self, dir):
        return b'-L' + dir

    def runtime_library_dir_option(self, dir):
        return [
         b'-cool', b'-R' + dir]

    def find_library_file(self, dirs, lib, debug=0):
        return b'found'

    def library_option(self, lib):
        return b'-l' + lib


class CCompilerTestCase(support.EnvironGuard, unittest.TestCase):

    def test_set_executables(self):

        class MyCCompiler(CCompiler):
            executables = {b'compiler': b'', b'compiler_cxx': b'', b'linker': b''}

        compiler = MyCCompiler()
        compiler.set_executables(compiler=[b'env', b'OMPI_MPICC=clang', b'mpicc'])
        self.assertEqual(compiler.compiler, [b'env',
         b'OMPI_MPICC=clang',
         b'mpicc'])
        compiler.set_executables(compiler_cxx=b'env OMPI_MPICXX=clang++ mpicxx')
        self.assertEqual(compiler.compiler_cxx, [b'env',
         b'OMPI_MPICXX=clang++',
         b'mpicxx'])
        compiler.set_executables(linker=u'env OMPI_MPICXX=clang++ mpiCC')
        self.assertEqual(compiler.linker, [u'env',
         u'OMPI_MPICXX=clang++',
         u'mpiCC'])
        return

    def test_gen_lib_options(self):
        compiler = FakeCompiler()
        libdirs = [b'lib1', b'lib2']
        runlibdirs = [b'runlib1']
        libs = [os.path.join(b'dir', b'name'), b'name2']
        opts = gen_lib_options(compiler, libdirs, runlibdirs, libs)
        wanted = [7, 8, 9, 10, 11, 
         12]
        self.assertEqual(opts, wanted)
        return

    def test_debug_print(self):

        class MyCCompiler(CCompiler):
            executables = {}

        compiler = MyCCompiler()
        with captured_stdout() as stdout:
            compiler.debug_print(b'xxx')
        stdout.seek(0)
        self.assertEqual(stdout.read(), b'')
        debug.DEBUG = True
        try:
            with captured_stdout() as stdout:
                compiler.debug_print(b'xxx')
            stdout.seek(0)
            self.assertEqual(stdout.read(), b'xxx\n')
        finally:
            debug.DEBUG = False

        return

    @unittest.skipUnless(get_default_compiler() == b'unix', b'not testing if default compiler is not unix')
    def test_customize_compiler(self):
        os.environ[b'AR'] = b'my_ar'
        os.environ[b'ARFLAGS'] = b'-arflags'

        class compiler:
            compiler_type = b'unix'

            def set_executables(self, **kw):
                self.exes = kw
                return

        comp = compiler()
        customize_compiler(comp)
        self.assertEqual(comp.exes[b'archiver'], b'my_ar -arflags')
        return


def test_suite():
    return unittest.makeSuite(CCompilerTestCase)


if __name__ == b'__main__':
    unittest.main(defaultTest=b'test_suite')
