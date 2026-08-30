import unittest, os, sys, idlelib
from idlelib import PathBrowser

class PathBrowserTest(unittest.TestCase):

    def test_DirBrowserTreeItem(self):
        d = PathBrowser.DirBrowserTreeItem(b'')
        d.GetSubList()
        self.assertEqual(b'', d.GetText())
        dir = os.path.split(os.path.abspath(idlelib.__file__))[0]
        self.assertEqual(d.ispackagedir(dir), True)
        self.assertEqual(d.ispackagedir(dir + b'/Icons'), False)
        return

    def test_PathBrowserTreeItem(self):
        p = PathBrowser.PathBrowserTreeItem()
        self.assertEqual(p.GetText(), b'sys.path')
        sub = p.GetSubList()
        self.assertEqual(len(sub), len(sys.path))
        return


if __name__ == b'__main__':
    unittest.main(verbosity=2, exit=False)
