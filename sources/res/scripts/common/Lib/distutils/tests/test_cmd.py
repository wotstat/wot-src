import unittest, os
from test.test_support import captured_stdout, run_unittest
from distutils.cmd import Command
from distutils.dist import Distribution
from distutils.errors import DistutilsOptionError
from distutils import debug

class MyCmd(Command):

    def initialize_options(self):
        return


class CommandTestCase(unittest.TestCase):

    def setUp(self):
        dist = Distribution()
        self.cmd = MyCmd(dist)
        return

    def test_ensure_string_list(self):
        cmd = self.cmd
        cmd.not_string_list = [b'one', 2, b'three']
        cmd.yes_string_list = [b'one', b'two', b'three']
        cmd.not_string_list2 = object()
        cmd.yes_string_list2 = b'ok'
        cmd.ensure_string_list(b'yes_string_list')
        cmd.ensure_string_list(b'yes_string_list2')
        self.assertRaises(DistutilsOptionError, cmd.ensure_string_list, b'not_string_list')
        self.assertRaises(DistutilsOptionError, cmd.ensure_string_list, b'not_string_list2')
        cmd.option1 = b'ok,dok'
        cmd.ensure_string_list(b'option1')
        self.assertEqual(cmd.option1, [b'ok', b'dok'])
        cmd.option2 = [
         b'xxx', b'www']
        cmd.ensure_string_list(b'option2')
        cmd.option3 = [
         b'ok', 2]
        self.assertRaises(DistutilsOptionError, cmd.ensure_string_list, b'option3')
        return

    def test_make_file(self):
        cmd = self.cmd
        self.assertRaises(TypeError, cmd.make_file, infiles=1, outfile=b'', func=b'func', args=())

        def _execute(func, args, exec_msg, level):
            self.assertEqual(exec_msg, b'generating out from in')
            return

        cmd.force = True
        cmd.execute = _execute
        cmd.make_file(infiles=b'in', outfile=b'out', func=b'func', args=())
        return

    def test_dump_options(self):
        msgs = []

        def _announce(msg, level):
            msgs.append(msg)
            return

        cmd = self.cmd
        cmd.announce = _announce
        cmd.option1 = 1
        cmd.option2 = 1
        cmd.user_options = [(b'option1', b'', b''), (b'option2', b'', b'')]
        cmd.dump_options()
        wanted = [
         b"command options for 'MyCmd':", b'  option1 = 1',
         b'  option2 = 1']
        self.assertEqual(msgs, wanted)
        return

    def test_ensure_string(self):
        cmd = self.cmd
        cmd.option1 = b'ok'
        cmd.ensure_string(b'option1')
        cmd.option2 = None
        cmd.ensure_string(b'option2', b'xxx')
        self.assertTrue(hasattr(cmd, b'option2'))
        cmd.option3 = 1
        self.assertRaises(DistutilsOptionError, cmd.ensure_string, b'option3')
        return

    def test_ensure_filename(self):
        cmd = self.cmd
        cmd.option1 = __file__
        cmd.ensure_filename(b'option1')
        cmd.option2 = b'xxx'
        self.assertRaises(DistutilsOptionError, cmd.ensure_filename, b'option2')
        return

    def test_ensure_dirname(self):
        cmd = self.cmd
        cmd.option1 = os.path.dirname(__file__) or os.curdir
        cmd.ensure_dirname(b'option1')
        cmd.option2 = b'xxx'
        self.assertRaises(DistutilsOptionError, cmd.ensure_dirname, b'option2')
        return

    def test_debug_print(self):
        cmd = self.cmd
        with captured_stdout() as stdout:
            cmd.debug_print(b'xxx')
        stdout.seek(0)
        self.assertEqual(stdout.read(), b'')
        debug.DEBUG = True
        try:
            with captured_stdout() as stdout:
                cmd.debug_print(b'xxx')
            stdout.seek(0)
            self.assertEqual(stdout.read(), b'xxx\n')
        finally:
            debug.DEBUG = False

        return


def test_suite():
    return unittest.makeSuite(CommandTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
