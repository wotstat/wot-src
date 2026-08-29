import os, StringIO, sys, unittest, warnings, textwrap
from distutils.dist import Distribution, fix_help_options
from distutils.cmd import Command
import distutils.dist
from test.test_support import TESTFN, captured_stdout, run_unittest, unlink
from distutils.tests import support
from distutils import log

class test_dist(Command):
    user_options = [
     (b'sample-option=', b'S', b'help text')]

    def initialize_options(self):
        self.sample_option = None
        return


class TestDistribution(Distribution):

    def find_config_files(self):
        return self._config_files


class DistributionTestCase(support.TempdirManager, support.LoggingSilencer, support.EnvironGuard, unittest.TestCase):

    def setUp(self):
        super(DistributionTestCase, self).setUp()
        self.argv = (sys.argv, sys.argv[:])
        del sys.argv[1:]
        return

    def tearDown(self):
        sys.argv = self.argv[0]
        sys.argv[:] = self.argv[1]
        super(DistributionTestCase, self).tearDown()
        return

    def create_distribution(self, configfiles=()):
        d = TestDistribution()
        d._config_files = configfiles
        d.parse_config_files()
        d.parse_command_line()
        return d

    def test_debug_mode(self):
        with open(TESTFN, b'w') as f:
            f.write(b'[global]\n')
            f.write(b'command_packages = foo.bar, splat')
        self.addCleanup(unlink, TESTFN)
        files = [
         TESTFN]
        sys.argv.append(b'build')
        with captured_stdout() as stdout:
            self.create_distribution(files)
        stdout.seek(0)
        self.assertEqual(stdout.read(), b'')
        distutils.dist.DEBUG = True
        try:
            with captured_stdout() as stdout:
                self.create_distribution(files)
            stdout.seek(0)
            self.assertEqual(stdout.read(), b'')
        finally:
            distutils.dist.DEBUG = False

        return

    def test_command_packages_unspecified(self):
        sys.argv.append(b'build')
        d = self.create_distribution()
        self.assertEqual(d.get_command_packages(), [b'distutils.command'])
        return

    def test_command_packages_cmdline(self):
        from distutils.tests.test_dist import test_dist
        sys.argv.extend([b'--command-packages',
         b'foo.bar,distutils.tests',
         b'test_dist',
         b'-Ssometext'])
        d = self.create_distribution()
        self.assertEqual(d.get_command_packages(), [
         b'distutils.command', b'foo.bar', b'distutils.tests'])
        cmd = d.get_command_obj(b'test_dist')
        self.assertIsInstance(cmd, test_dist)
        self.assertEqual(cmd.sample_option, b'sometext')
        return

    def test_command_packages_configfile(self):
        sys.argv.append(b'build')
        self.addCleanup(os.unlink, TESTFN)
        f = open(TESTFN, b'w')
        try:
            print >> f, b'[global]'
            print >> f, b'command_packages = foo.bar, splat'
        finally:
            f.close()

        d = self.create_distribution([TESTFN])
        self.assertEqual(d.get_command_packages(), [
         b'distutils.command', b'foo.bar', b'splat'])
        sys.argv[1:] = [
         b'--command-packages', b'spork', b'build']
        d = self.create_distribution([TESTFN])
        self.assertEqual(d.get_command_packages(), [
         b'distutils.command', b'spork'])
        sys.argv[1:] = [
         b'--command-packages', b'', b'build']
        d = self.create_distribution([TESTFN])
        self.assertEqual(d.get_command_packages(), [b'distutils.command'])
        return

    def test_write_pkg_file(self):
        tmp_dir = self.mkdtemp()
        my_file = os.path.join(tmp_dir, b'f')
        klass = Distribution
        dist = klass(attrs={b'author': u'Mister Caf\xe9', b'name': b'my.package', 
           b'maintainer': u'Caf\xe9 Junior', 
           b'description': u'Caf\xe9 torr\xe9fi\xe9', 
           b'long_description': u'H\xe9h\xe9h\xe9'})
        dist.metadata.write_pkg_file(open(my_file, b'w'))
        dist = klass(attrs={b'author': b'Mister Cafe', b'name': b'my.package', 
           b'maintainer': b'Cafe Junior', 
           b'description': b'Cafe torrefie', 
           b'long_description': b'Hehehe'})
        my_file2 = os.path.join(tmp_dir, b'f2')
        dist.metadata.write_pkg_file(open(my_file2, b'w'))
        return

    def test_empty_options(self):
        warns = []

        def _warn(msg):
            warns.append(msg)
            return

        self.addCleanup(setattr, warnings, b'warn', warnings.warn)
        warnings.warn = _warn
        dist = Distribution(attrs={b'author': b'xxx', b'name': b'xxx', b'version': b'xxx', 
           b'url': b'xxxx', b'options': {}})
        self.assertEqual(len(warns), 0)
        self.assertNotIn(b'options', dir(dist))
        return

    def test_finalize_options(self):
        attrs = {b'keywords': b'one,two', b'platforms': b'one,two'}
        dist = Distribution(attrs=attrs)
        dist.finalize_options()
        self.assertEqual(dist.metadata.platforms, [b'one', b'two'])
        self.assertEqual(dist.metadata.keywords, [b'one', b'two'])
        return

    def test_get_command_packages(self):
        dist = Distribution()
        self.assertEqual(dist.command_packages, None)
        cmds = dist.get_command_packages()
        self.assertEqual(cmds, [b'distutils.command'])
        self.assertEqual(dist.command_packages, [
         b'distutils.command'])
        dist.command_packages = b'one,two'
        cmds = dist.get_command_packages()
        self.assertEqual(cmds, [b'distutils.command', b'one', b'two'])
        return

    def test_announce(self):
        dist = Distribution()
        args = (b'ok',)
        kwargs = {b'level': b'ok2'}
        self.assertRaises(ValueError, dist.announce, args, kwargs)
        return

    def test_find_config_files_disable(self):
        temp_home = self.mkdtemp()
        if os.name == b'posix':
            user_filename = os.path.join(temp_home, b'.pydistutils.cfg')
        else:
            user_filename = os.path.join(temp_home, b'pydistutils.cfg')
        with open(user_filename, b'w') as f:
            f.write(b'[distutils]\n')

        def _expander(path):
            return temp_home

        old_expander = os.path.expanduser
        os.path.expanduser = _expander
        try:
            d = distutils.dist.Distribution()
            all_files = d.find_config_files()
            d = distutils.dist.Distribution(attrs={b'script_args': [
                              b'--no-user-cfg']})
            files = d.find_config_files()
        finally:
            os.path.expanduser = old_expander

        self.assertEqual(len(all_files) - 1, len(files))
        return


class MetadataTestCase(support.TempdirManager, support.EnvironGuard, unittest.TestCase):

    def setUp(self):
        super(MetadataTestCase, self).setUp()
        self.argv = (sys.argv, sys.argv[:])
        return

    def tearDown(self):
        sys.argv = self.argv[0]
        sys.argv[:] = self.argv[1]
        super(MetadataTestCase, self).tearDown()
        return

    def test_classifier(self):
        attrs = {b'name': b'Boa', b'version': b'3.0', b'classifiers': [
                          b'Programming Language :: Python :: 3']}
        dist = Distribution(attrs)
        meta = self.format_metadata(dist)
        self.assertIn(b'Metadata-Version: 1.1', meta)
        return

    def test_download_url(self):
        attrs = {b'name': b'Boa', b'version': b'3.0', b'download_url': b'http://example.org/boa'}
        dist = Distribution(attrs)
        meta = self.format_metadata(dist)
        self.assertIn(b'Metadata-Version: 1.1', meta)
        return

    def test_long_description(self):
        long_desc = textwrap.dedent(b'        example::\n              We start here\n            and continue here\n          and end here.')
        attrs = {b'name': b'package', b'version': b'1.0', 
           b'long_description': long_desc}
        dist = Distribution(attrs)
        meta = self.format_metadata(dist)
        meta = meta.replace(b'\n' + b'        ', b'\n')
        self.assertIn(long_desc, meta)
        return

    def test_simple_metadata(self):
        attrs = {b'name': b'package', b'version': b'1.0'}
        dist = Distribution(attrs)
        meta = self.format_metadata(dist)
        self.assertIn(b'Metadata-Version: 1.0', meta)
        self.assertNotIn(b'provides:', meta.lower())
        self.assertNotIn(b'requires:', meta.lower())
        self.assertNotIn(b'obsoletes:', meta.lower())
        return

    def test_provides(self):
        attrs = {b'name': b'package', b'version': b'1.0', 
           b'provides': [
                       b'package', b'package.sub']}
        dist = Distribution(attrs)
        self.assertEqual(dist.metadata.get_provides(), [
         b'package', b'package.sub'])
        self.assertEqual(dist.get_provides(), [
         b'package', b'package.sub'])
        meta = self.format_metadata(dist)
        self.assertIn(b'Metadata-Version: 1.1', meta)
        self.assertNotIn(b'requires:', meta.lower())
        self.assertNotIn(b'obsoletes:', meta.lower())
        return

    def test_provides_illegal(self):
        self.assertRaises(ValueError, Distribution, {b'name': b'package', b'version': b'1.0', 
           b'provides': [
                       b'my.pkg (splat)']})
        return

    def test_requires(self):
        attrs = {b'name': b'package', b'version': b'1.0', 
           b'requires': [
                       b'other', b'another (==1.0)']}
        dist = Distribution(attrs)
        self.assertEqual(dist.metadata.get_requires(), [
         b'other', b'another (==1.0)'])
        self.assertEqual(dist.get_requires(), [
         b'other', b'another (==1.0)'])
        meta = self.format_metadata(dist)
        self.assertIn(b'Metadata-Version: 1.1', meta)
        self.assertNotIn(b'provides:', meta.lower())
        self.assertIn(b'Requires: other', meta)
        self.assertIn(b'Requires: another (==1.0)', meta)
        self.assertNotIn(b'obsoletes:', meta.lower())
        return

    def test_requires_illegal(self):
        self.assertRaises(ValueError, Distribution, {b'name': b'package', b'version': b'1.0', 
           b'requires': [
                       b'my.pkg (splat)']})
        return

    def test_obsoletes(self):
        attrs = {b'name': b'package', b'version': b'1.0', 
           b'obsoletes': [
                        b'other', b'another (<1.0)']}
        dist = Distribution(attrs)
        self.assertEqual(dist.metadata.get_obsoletes(), [
         b'other', b'another (<1.0)'])
        self.assertEqual(dist.get_obsoletes(), [
         b'other', b'another (<1.0)'])
        meta = self.format_metadata(dist)
        self.assertIn(b'Metadata-Version: 1.1', meta)
        self.assertNotIn(b'provides:', meta.lower())
        self.assertNotIn(b'requires:', meta.lower())
        self.assertIn(b'Obsoletes: other', meta)
        self.assertIn(b'Obsoletes: another (<1.0)', meta)
        return

    def test_obsoletes_illegal(self):
        self.assertRaises(ValueError, Distribution, {b'name': b'package', b'version': b'1.0', 
           b'obsoletes': [
                        b'my.pkg (splat)']})
        return

    def format_metadata(self, dist):
        sio = StringIO.StringIO()
        dist.metadata.write_pkg_file(sio)
        return sio.getvalue()

    def test_custom_pydistutils(self):
        if os.name == b'posix':
            user_filename = b'.pydistutils.cfg'
        else:
            user_filename = b'pydistutils.cfg'
        temp_dir = self.mkdtemp()
        user_filename = os.path.join(temp_dir, user_filename)
        f = open(user_filename, b'w')
        try:
            f.write(b'.')
        finally:
            f.close()

        try:
            dist = Distribution()
            if sys.platform in (b'linux', b'darwin'):
                os.environ[b'HOME'] = temp_dir
                files = dist.find_config_files()
                self.assertIn(user_filename, files)
            if sys.platform == b'win32':
                os.environ[b'HOME'] = temp_dir
                files = dist.find_config_files()
                self.assertIn(user_filename, files, b'%r not found in %r' % (user_filename, files))
        finally:
            os.remove(user_filename)

        return

    def test_fix_help_options(self):
        help_tuples = [
         (b'a', b'b', b'c', b'd'), (1, 2, 3, 4)]
        fancy_options = fix_help_options(help_tuples)
        self.assertEqual(fancy_options[0], (b'a', b'b', b'c'))
        self.assertEqual(fancy_options[1], (1, 2, 3))
        return

    def test_show_help(self):
        self.addCleanup(log.set_threshold, log._global_log.threshold)
        dist = Distribution()
        sys.argv = []
        dist.help = 1
        dist.script_name = b'setup.py'
        with captured_stdout() as s:
            dist.parse_command_line()
        output = [line for line in s.getvalue().split(b'\n') if line.strip() != b'']
        self.assertTrue(output)
        return

    def test_read_metadata(self):
        attrs = {b'name': b'package', b'version': b'1.0', 
           b'long_description': b'desc', 
           b'description': b'xxx', 
           b'download_url': b'http://example.com', 
           b'keywords': [
                       b'one', b'two'], 
           b'requires': [
                       b'foo']}
        dist = Distribution(attrs)
        metadata = dist.metadata
        PKG_INFO = StringIO.StringIO()
        metadata.write_pkg_file(PKG_INFO)
        PKG_INFO.seek(0)
        metadata.read_pkg_file(PKG_INFO)
        self.assertEqual(metadata.name, b'package')
        self.assertEqual(metadata.version, b'1.0')
        self.assertEqual(metadata.description, b'xxx')
        self.assertEqual(metadata.download_url, b'http://example.com')
        self.assertEqual(metadata.keywords, [b'one', b'two'])
        self.assertEqual(metadata.platforms, [b'UNKNOWN'])
        self.assertEqual(metadata.obsoletes, None)
        self.assertEqual(metadata.requires, [b'foo'])
        return


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(DistributionTestCase))
    suite.addTest(unittest.makeSuite(MetadataTestCase))
    return suite


if __name__ == b'__main__':
    run_unittest(test_suite())
