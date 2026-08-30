import unittest
from test.test_support import captured_stderr
import warnings
showwarning = warnings.showwarning
running_in_idle = b'idle' in showwarning.__name__
from idlelib import run
from idlelib import PyShell as shell
idlemsg = b'\nWarning (from warnings module):\n  File "test_warning.py", line 99\n    Line of code\nUserWarning: Test\n'
shellmsg = idlemsg + b'>>> '

class RunWarnTest(unittest.TestCase):

    @unittest.skipIf(running_in_idle, b'Does not work when run within Idle.')
    def test_showwarnings(self):
        self.assertIs(warnings.showwarning, showwarning)
        run.capture_warnings(True)
        self.assertIs(warnings.showwarning, run.idle_showwarning_subproc)
        run.capture_warnings(False)
        self.assertIs(warnings.showwarning, showwarning)
        return

    def test_run_show(self):
        with captured_stderr() as f:
            run.idle_showwarning_subproc(b'Test', UserWarning, b'test_warning.py', 99, f, b'Line of code')
            self.assertEqual(idlemsg.splitlines(), f.getvalue().splitlines())
        return


class ShellWarnTest(unittest.TestCase):

    @unittest.skipIf(running_in_idle, b'Does not work when run within Idle.')
    def test_showwarnings(self):
        self.assertIs(warnings.showwarning, showwarning)
        shell.capture_warnings(True)
        self.assertIs(warnings.showwarning, shell.idle_showwarning)
        shell.capture_warnings(False)
        self.assertIs(warnings.showwarning, showwarning)
        return

    def test_idle_formatter(self):
        s = shell.idle_formatwarning(b'Test', UserWarning, b'test_warning.py', 99, b'Line of code')
        self.assertEqual(idlemsg, s)
        return

    def test_shell_show(self):
        with captured_stderr() as f:
            shell.idle_showwarning(b'Test', UserWarning, b'test_warning.py', 99, f, b'Line of code')
            self.assertEqual(shellmsg.splitlines(), f.getvalue().splitlines())
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=False)
