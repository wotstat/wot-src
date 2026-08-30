import os, unittest
from distutils.command.install_scripts import install_scripts
from distutils.core import Distribution
from distutils.tests import support
from test.test_support import run_unittest

class InstallScriptsTestCase(support.TempdirManager, support.LoggingSilencer, unittest.TestCase):

    def test_default_settings(self):
        dist = Distribution()
        dist.command_obj[b'build'] = support.DummyCommand(build_scripts=b'/foo/bar')
        dist.command_obj[b'install'] = support.DummyCommand(install_scripts=b'/splat/funk', force=1, skip_build=1)
        cmd = install_scripts(dist)
        self.assertFalse(cmd.force)
        self.assertFalse(cmd.skip_build)
        self.assertIsNone(cmd.build_dir)
        self.assertIsNone(cmd.install_dir)
        cmd.finalize_options()
        self.assertTrue(cmd.force)
        self.assertTrue(cmd.skip_build)
        self.assertEqual(cmd.build_dir, b'/foo/bar')
        self.assertEqual(cmd.install_dir, b'/splat/funk')
        return

    def test_installation(self):
        source = self.mkdtemp()
        expected = []

        def write_script(name, text):
            expected.append(name)
            f = open(os.path.join(source, name), b'w')
            try:
                f.write(text)
            finally:
                f.close()

            return

        write_script(b'script1.py', b'#! /usr/bin/env python2.3\n# bogus script w/ Python sh-bang\npass\n')
        write_script(b'script2.py', b'#!/usr/bin/python\n# bogus script w/ Python sh-bang\npass\n')
        write_script(b'shell.sh', b'#!/bin/sh\n# bogus shell script w/ sh-bang\nexit 0\n')
        target = self.mkdtemp()
        dist = Distribution()
        dist.command_obj[b'build'] = support.DummyCommand(build_scripts=source)
        dist.command_obj[b'install'] = support.DummyCommand(install_scripts=target, force=1, skip_build=1)
        cmd = install_scripts(dist)
        cmd.finalize_options()
        cmd.run()
        installed = os.listdir(target)
        for name in expected:
            self.assertIn(name, installed)

        return


def test_suite():
    return unittest.makeSuite(InstallScriptsTestCase)


if __name__ == b'__main__':
    run_unittest(test_suite())
