import os, sys, unittest
from test import test_support
from Tkinter import Tcl, TclError
test_support.requires(b'gui')

class TkLoadTest(unittest.TestCase):

    @unittest.skipIf(b'DISPLAY' not in os.environ, b'No $DISPLAY set.')
    def testLoadTk(self):
        tcl = Tcl()
        self.assertRaises(TclError, tcl.winfo_geometry)
        tcl.loadtk()
        self.assertEqual(b'1x1+0+0', tcl.winfo_geometry())
        tcl.destroy()
        return

    def testLoadTkFailure(self):
        old_display = None
        if sys.platform.startswith((b'win', b'darwin', b'cygwin')):
            return
        else:
            with test_support.EnvironmentVarGuard() as env:
                if b'DISPLAY' in os.environ:
                    del env[b'DISPLAY']
                    display = os.popen(b'echo $DISPLAY').read().strip()
                    if display:
                        return
                tcl = Tcl()
                self.assertRaises(TclError, tcl.winfo_geometry)
                self.assertRaises(TclError, tcl.loadtk)
            return


tests_gui = (
 TkLoadTest,)
if __name__ == b'__main__':
    test_support.run_unittest(*tests_gui)
