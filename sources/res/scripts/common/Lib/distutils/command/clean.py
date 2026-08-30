__revision__ = b'$Id$'
import os
from distutils.core import Command
from distutils.dir_util import remove_tree
from distutils import log

class clean(Command):
    description = b"clean up temporary files from 'build' command"
    user_options = [
     19, 
     21, 
     22, 
     23, 
     24, 
     25]
    boolean_options = [
     b'all']

    def initialize_options(self):
        self.build_base = None
        self.build_lib = None
        self.build_temp = None
        self.build_scripts = None
        self.bdist_base = None
        self.all = None
        return

    def finalize_options(self):
        self.set_undefined_options(b'build', (b'build_base', b'build_base'), (b'build_lib', b'build_lib'), (b'build_scripts', b'build_scripts'), (b'build_temp', b'build_temp'))
        self.set_undefined_options(b'bdist', (b'bdist_base', b'bdist_base'))
        return

    def run(self):
        if os.path.exists(self.build_temp):
            remove_tree(self.build_temp, dry_run=self.dry_run)
        else:
            log.debug(b"'%s' does not exist -- can't clean it", self.build_temp)
        if self.all:
            for directory in (self.build_lib,
             self.bdist_base,
             self.build_scripts):
                if os.path.exists(directory):
                    remove_tree(directory, dry_run=self.dry_run)
                else:
                    log.warn(b"'%s' does not exist -- can't clean it", directory)

        if not self.dry_run:
            try:
                os.rmdir(self.build_base)
                log.info(b"removing '%s'", self.build_base)
            except OSError:
                pass

        return
