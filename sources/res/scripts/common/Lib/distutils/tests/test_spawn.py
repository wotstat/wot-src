import os, stat, sys, time, unittest
from test.support import captured_stdout, run_unittest
from test import support as test_support
from distutils.spawn import _nt_quote_args
from distutils.spawn import spawn, find_executable
from distutils.errors import DistutilsExecError
from distutils.tests import support

class SpawnTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_nt_quote_args(self):
        for args, wanted in (
         ([b'with space', b'nospace'],
          [
           b'"with space"', b'nospace']),
         (
          [
           b'nochange', b'nospace'],
          [
           b'nochange', b'nospace'])):
            res = _nt_quote_args(args)
            self.assertEqual(res, wanted)

        return

    @unittest.skipUnless(os.name in (b'nt', b'posix'), b'Runs only under posix or nt')
    def test_spawn(self):
        tmpdir = self.mkdtemp()
        if os.name == b'posix':
            exe = os.path.join(tmpdir, b'foo.sh')
            self.write_file(exe, b'#!/bin/sh\nexit 1')
            os.chmod(exe, 511)
        else:
            exe = os.path.join(tmpdir, b'foo.bat')
            self.write_file(exe, b'exit 1')
        os.chmod(exe, 511)
        self.assertRaises(DistutilsExecError, spawn, [exe])
        if os.name == b'posix':
            exe = os.path.join(tmpdir, b'foo.sh')
            self.write_file(exe, b'#!/bin/sh\nexit 0')
            os.chmod(exe, 511)
        else:
            exe = os.path.join(tmpdir, b'foo.bat')
            self.write_file(exe, b'exit 0')
        os.chmod(exe, 511)
        spawn([exe])
        return

    def test_find_executable(self):
        with test_support.temp_dir() as tmp_dir:
            program_noeext = test_support.TESTFN
            program = program_noeext + b'.exe'
            filename = os.path.join(tmp_dir, program)
            with open(filename, b'wb'):
                pass
            os.chmod(filename, stat.S_IXUSR)
            rv = find_executable(program, path=tmp_dir)
            self.assertEqual(rv, filename)
            if sys.platform == b'win32':
                rv = find_executable(program_noeext, path=tmp_dir)
                self.assertEqual(rv, filename)
            with test_support.change_cwd(tmp_dir):
                rv = find_executable(program)
                self.assertEqual(rv, program)
            dont_exist_program = b'dontexist_' + program
            rv = find_executable(dont_exist_program, path=tmp_dir)
            self.assertIsNone(rv)
            with test_support.EnvironmentVarGuard() as env:
                from distutils import spawn
                with test_support.swap_attr(spawn.os, b'defpath', tmp_dir):
                    env.pop(b'PATH')
                    rv = find_executable(program)
                    self.assertEqual(rv, filename)
        return


def test_suite():
    return unittest.makeSuite(SpawnTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
