import os, textwrap, unittest
from test.test_support import run_unittest
from distutils.command.check import check, HAS_DOCUTILS
from distutils.tests import support
from distutils.errors import DistutilsSetupError
try:
    import pygments
except ImportError:
    pygments = None

HERE = os.path.dirname(__file__)

class CheckTestCase(support.LoggingSilencer, support.TempdirManager, unittest.TestCase):

    def _run(self, metadata=None, cwd=None, **options):
        if metadata is None:
            metadata = {}
        if cwd is not None:
            old_dir = os.getcwd()
            os.chdir(cwd)
        pkg_info, dist = self.create_dist(**metadata)
        cmd = check(dist)
        cmd.initialize_options()
        for name, value in options.items():
            setattr(cmd, name, value)

        cmd.ensure_finalized()
        cmd.run()
        if cwd is not None:
            os.chdir(old_dir)
        return cmd

    def test_check_metadata(self):
        cmd = self._run()
        self.assertEqual(cmd._warnings, 2)
        metadata = {b'url': b'xxx', b'author': b'xxx', b'author_email': b'xxx', 
           b'name': b'xxx', 
           b'version': b'xxx'}
        cmd = self._run(metadata)
        self.assertEqual(cmd._warnings, 0)
        self.assertRaises(DistutilsSetupError, self._run, {}, **{b'strict': 1})
        cmd = self._run(metadata, strict=1)
        self.assertEqual(cmd._warnings, 0)
        metadata = {b'url': u'xxx', b'author': u'\xc9ric', b'author_email': u'xxx', 
           u'name': b'xxx', b'version': u'xxx', 
           b'description': u'Something about esszet \xdf', 
           b'long_description': u'More things about esszet \xdf'}
        cmd = self._run(metadata)
        self.assertEqual(cmd._warnings, 0)
        return

    @unittest.skipUnless(HAS_DOCUTILS, b"won't test without docutils")
    def test_check_document(self):
        pkg_info, dist = self.create_dist()
        cmd = check(dist)
        broken_rest = b'title\n===\n\ntest'
        msgs = cmd._check_rst_data(broken_rest)
        self.assertEqual(len(msgs), 1)
        rest = b'title\n=====\n\ntest'
        msgs = cmd._check_rst_data(rest)
        self.assertEqual(len(msgs), 0)
        return

    @unittest.skipUnless(HAS_DOCUTILS, b"won't test without docutils")
    def test_check_restructuredtext(self):
        broken_rest = b'title\n===\n\ntest'
        pkg_info, dist = self.create_dist(long_description=broken_rest)
        cmd = check(dist)
        cmd.check_restructuredtext()
        self.assertEqual(cmd._warnings, 1)
        metadata = {b'url': b'xxx', b'author': b'xxx', b'author_email': b'xxx', 
           b'name': b'xxx', 
           b'version': b'xxx', b'long_description': broken_rest}
        self.assertRaises(DistutilsSetupError, self._run, metadata, **{b'strict': 1, b'restructuredtext': 1})
        metadata[b'long_description'] = u'title\n=====\n\ntest \xdf'
        cmd = self._run(metadata, strict=1, restructuredtext=1)
        self.assertEqual(cmd._warnings, 0)
        metadata[b'long_description'] = b'title\n=====\n\n.. include:: includetest.rst'
        cmd = self._run(metadata, cwd=HERE, strict=1, restructuredtext=1)
        self.assertEqual(cmd._warnings, 0)
        return

    @unittest.skipUnless(HAS_DOCUTILS, b"won't test without docutils")
    def test_check_restructuredtext_with_syntax_highlight(self):
        example_rst_docs = []
        example_rst_docs.append(textwrap.dedent(b"            Here's some code:\n\n            .. code:: python\n\n                def foo():\n                    pass\n            "))
        example_rst_docs.append(textwrap.dedent(b"            Here's some code:\n\n            .. code-block:: python\n\n                def foo():\n                    pass\n            "))
        for rest_with_code in example_rst_docs:
            pkg_info, dist = self.create_dist(long_description=rest_with_code)
            cmd = check(dist)
            cmd.check_restructuredtext()
            msgs = cmd._check_rst_data(rest_with_code)
            if pygments is not None:
                self.assertEqual(len(msgs), 0)
            else:
                self.assertEqual(len(msgs), 1)
                self.assertEqual(str(msgs[0][1]), b'Cannot analyze code. Pygments package not found.')

        return

    def test_check_all(self):
        metadata = {b'url': b'xxx', b'author': b'xxx'}
        self.assertRaises(DistutilsSetupError, self._run, {}, **{b'strict': 1, b'restructuredtext': 1})
        return


def test_suite():
    return unittest.makeSuite(CheckTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
