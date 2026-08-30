import unittest, os, sys
from test.test_support import run_unittest
from distutils.command.build_clib import build_clib
from distutils.errors import DistutilsSetupError
from distutils.tests import support
from distutils.spawn import find_executable

class BuildCLibTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_check_library_dist(self):
        pkg_dir, dist = self.create_dist()
        cmd = build_clib(dist)
        self.assertRaises(DistutilsSetupError, cmd.check_library_list, b'foo')
        self.assertRaises(DistutilsSetupError, cmd.check_library_list, [
         b'foo1', b'foo2'])
        self.assertRaises(DistutilsSetupError, cmd.check_library_list, [
         (1, b'foo1'), (b'name', b'foo2')])
        self.assertRaises(DistutilsSetupError, cmd.check_library_list, [
         (b'name', b'foo1'),
         (b'another/name', b'foo2')])
        self.assertRaises(DistutilsSetupError, cmd.check_library_list, [
         (
          b'name', {}),
         (b'another', b'foo2')])
        libs = [
         (
          b'name', {}), (b'name', {b'ok': b'good'})]
        cmd.check_library_list(libs)
        return

    def test_get_source_files(self):
        pkg_dir, dist = self.create_dist()
        cmd = build_clib(dist)
        cmd.libraries = [
         (
          b'name', {})]
        self.assertRaises(DistutilsSetupError, cmd.get_source_files)
        cmd.libraries = [
         (
          b'name', {b'sources': 1})]
        self.assertRaises(DistutilsSetupError, cmd.get_source_files)
        cmd.libraries = [
         (
          b'name', {b'sources': [b'a', b'b']})]
        self.assertEqual(cmd.get_source_files(), [b'a', b'b'])
        cmd.libraries = [
         (
          b'name', {b'sources': (b'a', b'b')})]
        self.assertEqual(cmd.get_source_files(), [b'a', b'b'])
        cmd.libraries = [
         (
          b'name', {b'sources': (b'a', b'b')}),
         (
          b'name2', {b'sources': [b'c', b'd']})]
        self.assertEqual(cmd.get_source_files(), [b'a', b'b', b'c', b'd'])
        return

    def test_build_libraries(self):
        pkg_dir, dist = self.create_dist()
        cmd = build_clib(dist)

        class FakeCompiler:

            def compile(*args, **kw):
                return

            create_static_lib = compile

        cmd.compiler = FakeCompiler()
        lib = [
         (
          b'name', {b'sources': b'notvalid'})]
        self.assertRaises(DistutilsSetupError, cmd.build_libraries, lib)
        lib = [
         (
          b'name', {b'sources': (list())})]
        cmd.build_libraries(lib)
        lib = [
         (
          b'name', {b'sources': (tuple())})]
        cmd.build_libraries(lib)
        return

    def test_finalize_options(self):
        pkg_dir, dist = self.create_dist()
        cmd = build_clib(dist)
        cmd.include_dirs = b'one-dir'
        cmd.finalize_options()
        self.assertEqual(cmd.include_dirs, [b'one-dir'])
        cmd.include_dirs = None
        cmd.finalize_options()
        self.assertEqual(cmd.include_dirs, [])
        cmd.distribution.libraries = b'WONTWORK'
        self.assertRaises(DistutilsSetupError, cmd.finalize_options)
        return

    @unittest.skipIf(sys.platform == b'win32', b"can't test on Windows")
    def test_run(self):
        pkg_dir, dist = self.create_dist()
        cmd = build_clib(dist)
        foo_c = os.path.join(pkg_dir, b'foo.c')
        self.write_file(foo_c, b'int main(void) { return 1;}\n')
        cmd.libraries = [(b'foo', {b'sources': [foo_c]})]
        build_temp = os.path.join(pkg_dir, b'build')
        os.mkdir(build_temp)
        cmd.build_temp = build_temp
        cmd.build_clib = build_temp
        from distutils.ccompiler import new_compiler
        from distutils.sysconfig import customize_compiler
        compiler = new_compiler()
        customize_compiler(compiler)
        for ccmd in compiler.executables.values():
            if ccmd is None:
                continue
            if find_executable(ccmd[0]) is None:
                self.skipTest(b'The %r command is not found' % ccmd[0])

        cmd.run()
        self.assertIn(b'libfoo.a', os.listdir(build_temp))
        return


def test_suite():
    return unittest.makeSuite(BuildCLibTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
