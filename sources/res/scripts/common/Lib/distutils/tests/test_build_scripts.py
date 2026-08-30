import os, unittest
from distutils.command.build_scripts import build_scripts
from distutils.core import Distribution
import sysconfig
from distutils.tests import support
from test.test_support import run_unittest

class BuildScriptsTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_default_settings(self):
        cmd = self.get_build_scripts_cmd(b'/foo/bar', [])
        self.assertFalse(cmd.force)
        self.assertIsNone(cmd.build_dir)
        cmd.finalize_options()
        self.assertTrue(cmd.force)
        self.assertEqual(cmd.build_dir, b'/foo/bar')
        return

    def test_build(self):
        source = self.mkdtemp()
        target = self.mkdtemp()
        expected = self.write_sample_scripts(source)
        cmd = self.get_build_scripts_cmd(target, [os.path.join(source, fn) for fn in expected])
        cmd.finalize_options()
        cmd.run()
        built = os.listdir(target)
        for name in expected:
            self.assertIn(name, built)

        return

    def get_build_scripts_cmd(self, target, scripts):
        import sys
        dist = Distribution()
        dist.scripts = scripts
        dist.command_obj[b'build'] = support.DummyCommand(build_scripts=target, force=1, executable=sys.executable)
        return build_scripts(dist)

    def write_sample_scripts(self, dir):
        expected = []
        expected.append(b'script1.py')
        self.write_script(dir, b'script1.py', b'#! /usr/bin/env python2.3\n# bogus script w/ Python sh-bang\npass\n')
        expected.append(b'script2.py')
        self.write_script(dir, b'script2.py', b'#!/usr/bin/python\n# bogus script w/ Python sh-bang\npass\n')
        expected.append(b'shell.sh')
        self.write_script(dir, b'shell.sh', b'#!/bin/sh\n# bogus shell script w/ sh-bang\nexit 0\n')
        return expected

    def write_script(self, dir, name, text):
        f = open(os.path.join(dir, name), b'w')
        try:
            f.write(text)
        finally:
            f.close()

        return

    def test_version_int(self):
        source = self.mkdtemp()
        target = self.mkdtemp()
        expected = self.write_sample_scripts(source)
        cmd = self.get_build_scripts_cmd(target, [os.path.join(source, fn) for fn in expected])
        cmd.finalize_options()
        old = sysconfig.get_config_vars().get(b'VERSION')
        sysconfig._CONFIG_VARS[b'VERSION'] = 4
        try:
            cmd.run()
        finally:
            if old is not None:
                sysconfig._CONFIG_VARS[b'VERSION'] = old

        built = os.listdir(target)
        for name in expected:
            self.assertIn(name, built)

        return


def test_suite():
    return unittest.makeSuite(BuildScriptsTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
