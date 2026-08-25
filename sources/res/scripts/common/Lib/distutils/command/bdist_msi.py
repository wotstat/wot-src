import sys, os
from sysconfig import get_python_version
from distutils.core import Command
from distutils.dir_util import remove_tree
from distutils.version import StrictVersion
from distutils.errors import DistutilsOptionError
from distutils import log
from distutils.util import get_platform
import msilib
from msilib import schema, sequence, text
from msilib import Directory, Feature, Dialog, add_data

class PyDialog(Dialog):

    def __init__(self, *args, **kw):
        Dialog.__init__(self, *args)
        ruler = self.h - 36
        self.line(b'BottomLine', 0, ruler, self.w, 0)
        return

    def title(self, title):
        self.text(b'Title', 15, 10, 320, 60, 196611, b'{\\VerdanaBold10}%s' % title)
        return

    def back(self, title, next, name=b'Back', active=1):
        if active:
            flags = 3
        else:
            flags = 1
        return self.pushbutton(name, 180, self.h - 27, 56, 17, flags, title, next)

    def cancel(self, title, next, name=b'Cancel', active=1):
        if active:
            flags = 3
        else:
            flags = 1
        return self.pushbutton(name, 304, self.h - 27, 56, 17, flags, title, next)

    def next(self, title, next, name=b'Next', active=1):
        if active:
            flags = 3
        else:
            flags = 1
        return self.pushbutton(name, 236, self.h - 27, 56, 17, flags, title, next)

    def xbutton(self, name, title, next, xpos):
        return self.pushbutton(name, int(self.w * xpos - 28), self.h - 27, 56, 17, 3, title, next)


class bdist_msi(Command):
    description = b'create a Microsoft Installer (.msi) binary distribution'
    user_options = [
     (
      b'bdist-dir=', None,
      b'temporary directory for creating the distribution'),
     (
      b'plat-name=', b'p',
      b'platform name to embed in generated filenames (default: %s)' % get_platform()),
     (
      b'keep-temp', b'k',
      b'keep the pseudo-installation tree around after ' + b'creating the distribution archive'),
     (
      b'target-version=', None,
      b'require a specific python version' + b' on the target system'),
     (
      b'no-target-compile', b'c',
      b'do not compile .py to .pyc on the target system'),
     (
      b'no-target-optimize', b'o',
      b'do not compile .py to .pyo (optimized) on the target system'),
     (
      b'dist-dir=', b'd',
      b'directory to put final built distributions in'),
     (
      b'skip-build', None,
      b'skip rebuilding everything (for testing/debugging)'),
     (
      b'install-script=', None,
      b'basename of installation script to be run after installation or before deinstallation'),
     (
      b'pre-install-script=', None,
      b'Fully qualified filename of a script to be run before any files are installed.  This script need not be in the distribution')]
    boolean_options = [
     b'keep-temp', b'no-target-compile', b'no-target-optimize',
     b'skip-build']
    all_versions = [
     28, 29, 30, 31, 32, 
     33, 34, 35, 36, 37, 
     38, 
     39, 40, 41, 42, 
     43, 44, 45, 46, 47]
    other_version = b'X'

    def initialize_options(self):
        self.bdist_dir = None
        self.plat_name = None
        self.keep_temp = 0
        self.no_target_compile = 0
        self.no_target_optimize = 0
        self.target_version = None
        self.dist_dir = None
        self.skip_build = None
        self.install_script = None
        self.pre_install_script = None
        self.versions = None
        return

    def finalize_options(self):
        self.set_undefined_options(b'bdist', (b'skip_build', b'skip_build'))
        if self.bdist_dir is None:
            bdist_base = self.get_finalized_command(b'bdist').bdist_base
            self.bdist_dir = os.path.join(bdist_base, b'msi')
        short_version = get_python_version()
        if not self.target_version and self.distribution.has_ext_modules():
            self.target_version = short_version
        if self.target_version:
            self.versions = [
             self.target_version]
            if not self.skip_build and self.distribution.has_ext_modules() and self.target_version != short_version:
                raise DistutilsOptionError, b"target version can only be %s, or the '--skip-build' option must be specified" % (
                 short_version,)
        else:
            self.versions = list(self.all_versions)
        self.set_undefined_options(b'bdist', (b'dist_dir', b'dist_dir'), (b'plat_name', b'plat_name'))
        if self.pre_install_script:
            raise DistutilsOptionError, b'the pre-install-script feature is not yet implemented'
        if self.install_script:
            for script in self.distribution.scripts:
                if self.install_script == os.path.basename(script):
                    break
            else:
                raise DistutilsOptionError, b"install_script '%s' not found in scripts" % self.install_script

        self.install_script_key = None
        return

    def run(self):
        if not self.skip_build:
            self.run_command(b'build')
        install = self.reinitialize_command(b'install', reinit_subcommands=1)
        install.prefix = self.bdist_dir
        install.skip_build = self.skip_build
        install.warn_dir = 0
        install_lib = self.reinitialize_command(b'install_lib')
        install_lib.compile = 0
        install_lib.optimize = 0
        if self.distribution.has_ext_modules():
            target_version = self.target_version
            if not target_version:
                target_version = sys.version[0:3]
            plat_specifier = b'.%s-%s' % (self.plat_name, target_version)
            build = self.get_finalized_command(b'build')
            build.build_lib = os.path.join(build.build_base, b'lib' + plat_specifier)
        log.info(b'installing to %s', self.bdist_dir)
        install.ensure_finalized()
        sys.path.insert(0, os.path.join(self.bdist_dir, b'PURELIB'))
        install.run()
        del sys.path[0]
        self.mkpath(self.dist_dir)
        fullname = self.distribution.get_fullname()
        installer_name = self.get_installer_filename(fullname)
        installer_name = os.path.abspath(installer_name)
        if os.path.exists(installer_name):
            os.unlink(installer_name)
        metadata = self.distribution.metadata
        author = metadata.author
        if not author:
            author = metadata.maintainer
        if not author:
            author = b'UNKNOWN'
        version = metadata.get_version()
        sversion = b'%d.%d.%d' % StrictVersion(version).version
        fullname = self.distribution.get_fullname()
        if self.target_version:
            product_name = b'Python %s %s' % (self.target_version, fullname)
        else:
            product_name = b'Python %s' % fullname
        self.db = msilib.init_database(installer_name, schema, product_name, msilib.gen_uuid(), sversion, author)
        msilib.add_tables(self.db, sequence)
        props = [(b'DistVersion', version)]
        email = metadata.author_email or metadata.maintainer_email
        if email:
            props.append((b'ARPCONTACT', email))
        if metadata.url:
            props.append((b'ARPURLINFOABOUT', metadata.url))
        if props:
            add_data(self.db, b'Property', props)
        self.add_find_python()
        self.add_files()
        self.add_scripts()
        self.add_ui()
        self.db.Commit()
        if hasattr(self.distribution, b'dist_files'):
            tup = (
             b'bdist_msi', self.target_version or b'any', fullname)
            self.distribution.dist_files.append(tup)
        if not self.keep_temp:
            remove_tree(self.bdist_dir, dry_run=self.dry_run)
        return

    def add_files(self):
        db = self.db
        cab = msilib.CAB(b'distfiles')
        rootdir = os.path.abspath(self.bdist_dir)
        root = Directory(db, cab, None, rootdir, b'TARGETDIR', b'SourceDir')
        f = Feature(db, b'Python', b'Python', b'Everything', 0, 1, directory=b'TARGETDIR')
        items = [
         (
          f, root, b'')]
        for version in self.versions + [self.other_version]:
            target = b'TARGETDIR' + version
            name = default = b'Python' + version
            desc = b'Everything'
            if version is self.other_version:
                title = b'Python from another location'
                level = 2
            else:
                title = b'Python %s from registry' % version
                level = 1
            f = Feature(db, name, title, desc, 1, level, directory=target)
            dir = Directory(db, cab, root, rootdir, target, default)
            items.append((f, dir, version))

        db.Commit()
        seen = {}
        for feature, dir, version in items:
            todo = [dir]
            while todo:
                dir = todo.pop()
                for file in os.listdir(dir.absolute):
                    afile = os.path.join(dir.absolute, file)
                    if os.path.isdir(afile):
                        short = b'%s|%s' % (dir.make_short(file), file)
                        default = file + version
                        newdir = Directory(db, cab, dir, file, default, short)
                        todo.append(newdir)
                    else:
                        if not dir.component:
                            dir.start_component(dir.logical, feature, 0)
                        if afile not in seen:
                            key = seen[afile] = dir.add_file(file)
                            if file == self.install_script:
                                if self.install_script_key:
                                    raise DistutilsOptionError(b'Multiple files with name %s' % file)
                                self.install_script_key = b'[#%s]' % key
                        else:
                            key = seen[afile]
                            add_data(self.db, b'DuplicateFile', [
                             (
                              key + version, dir.component, key, None, dir.logical)])

            db.Commit()

        cab.commit(db)
        return

    def add_find_python(self):
        start = 402
        for ver in self.versions:
            install_path = b'SOFTWARE\\Python\\PythonCore\\%s\\InstallPath' % ver
            machine_reg = b'python.machine.' + ver
            user_reg = b'python.user.' + ver
            machine_prop = b'PYTHON.MACHINE.' + ver
            user_prop = b'PYTHON.USER.' + ver
            machine_action = b'PythonFromMachine' + ver
            user_action = b'PythonFromUser' + ver
            exe_action = b'PythonExe' + ver
            target_dir_prop = b'TARGETDIR' + ver
            exe_prop = b'PYTHON' + ver
            if msilib.Win64:
                Type = 18
            else:
                Type = 2
            add_data(self.db, b'RegLocator', [
             (
              machine_reg, 2, install_path, None, Type),
             (
              user_reg, 1, install_path, None, Type)])
            add_data(self.db, b'AppSearch', [
             (
              machine_prop, machine_reg),
             (
              user_prop, user_reg)])
            add_data(self.db, b'CustomAction', [
             (
              machine_action, 307, target_dir_prop, b'[' + machine_prop + b']'),
             (
              user_action, 307, target_dir_prop, b'[' + user_prop + b']'),
             (
              exe_action, 307, exe_prop, b'[' + target_dir_prop + b']\\python.exe')])
            add_data(self.db, b'InstallExecuteSequence', [
             (
              machine_action, machine_prop, start),
             (
              user_action, user_prop, start + 1),
             (
              exe_action, None, start + 2)])
            add_data(self.db, b'InstallUISequence', [
             (
              machine_action, machine_prop, start),
             (
              user_action, user_prop, start + 1),
             (
              exe_action, None, start + 2)])
            add_data(self.db, b'Condition', [
             (
              b'Python' + ver, 0, b'NOT TARGETDIR' + ver)])
            start += 4

        return

    def add_scripts(self):
        if self.install_script:
            start = 6800
            for ver in self.versions + [self.other_version]:
                install_action = b'install_script.' + ver
                exe_prop = b'PYTHON' + ver
                add_data(self.db, b'CustomAction', [
                 (
                  install_action, 50, exe_prop, self.install_script_key)])
                add_data(self.db, b'InstallExecuteSequence', [
                 (
                  install_action, b'&Python%s=3' % ver, start)])
                start += 1

        if self.pre_install_script:
            scriptfn = os.path.join(self.bdist_dir, b'preinstall.bat')
            f = open(scriptfn, b'w')
            f.write(b'rem ="""\n%1 %0\nexit\n"""\n')
            f.write(open(self.pre_install_script).read())
            f.close()
            add_data(self.db, b'Binary', [
             (
              b'PreInstall', msilib.Binary(scriptfn))])
            add_data(self.db, b'CustomAction', [
             (b'PreInstall', 2, b'PreInstall', None)])
            add_data(self.db, b'InstallExecuteSequence', [
             (b'PreInstall', b'NOT Installed', 450)])
        return

    def add_ui(self):
        db = self.db
        x = y = 50
        w = 370
        h = 300
        title = b'[ProductName] Setup'
        modal = 3
        modeless = 1
        add_data(db, b'Property', [
         240, 
         241, 
         242, 
         243, 
         244, 
         245])
        add_data(db, b'TextStyle', [
         (b'DlgFont8', b'Tahoma', 9, None, 0),
         (b'DlgFontBold8', b'Tahoma', 8, None, 1),
         (b'VerdanaBold10', b'Verdana', 10, None, 1),
         (b'VerdanaRed9', b'Verdana', 9, 255, 0)])
        add_data(db, b'InstallUISequence', [
         250, 
         251, 
         252, 
         253, 
         254])
        add_data(db, b'ActionText', text.ActionText)
        add_data(db, b'UIText', text.UIText)
        fatal = PyDialog(db, b'FatalError', x, y, w, h, modal, title, b'Finish', b'Finish', b'Finish')
        fatal.title(b'[ProductName] Installer ended prematurely')
        fatal.back(b'< Back', b'Finish', active=0)
        fatal.cancel(b'Cancel', b'Back', active=0)
        fatal.text(b'Description1', 15, 70, 320, 80, 196611, b'[ProductName] setup ended prematurely because of an error.  Your system has not been modified.  To install this program at a later time, please run the installation again.')
        fatal.text(b'Description2', 15, 155, 320, 20, 196611, b'Click the Finish button to exit the Installer.')
        c = fatal.next(b'Finish', b'Cancel', name=b'Finish')
        c.event(b'EndDialog', b'Exit')
        user_exit = PyDialog(db, b'UserExit', x, y, w, h, modal, title, b'Finish', b'Finish', b'Finish')
        user_exit.title(b'[ProductName] Installer was interrupted')
        user_exit.back(b'< Back', b'Finish', active=0)
        user_exit.cancel(b'Cancel', b'Back', active=0)
        user_exit.text(b'Description1', 15, 70, 320, 80, 196611, b'[ProductName] setup was interrupted.  Your system has not been modified.  To install this program at a later time, please run the installation again.')
        user_exit.text(b'Description2', 15, 155, 320, 20, 196611, b'Click the Finish button to exit the Installer.')
        c = user_exit.next(b'Finish', b'Cancel', name=b'Finish')
        c.event(b'EndDialog', b'Exit')
        exit_dialog = PyDialog(db, b'ExitDialog', x, y, w, h, modal, title, b'Finish', b'Finish', b'Finish')
        exit_dialog.title(b'Completing the [ProductName] Installer')
        exit_dialog.back(b'< Back', b'Finish', active=0)
        exit_dialog.cancel(b'Cancel', b'Back', active=0)
        exit_dialog.text(b'Description', 15, 235, 320, 20, 196611, b'Click the Finish button to exit the Installer.')
        c = exit_dialog.next(b'Finish', b'Cancel', name=b'Finish')
        c.event(b'EndDialog', b'Return')
        inuse = PyDialog(db, b'FilesInUse', x, y, w, h, 19, title, b'Retry', b'Retry', b'Retry', bitmap=False)
        inuse.text(b'Title', 15, 6, 200, 15, 196611, b'{\\DlgFontBold8}Files in Use')
        inuse.text(b'Description', 20, 23, 280, 20, 196611, b'Some files that need to be updated are currently in use.')
        inuse.text(b'Text', 20, 55, 330, 50, 3, b'The following applications are using files that need to be updated by this setup. Close these applications and then click Retry to continue the installation or Cancel to exit it.')
        inuse.control(b'List', b'ListBox', 20, 107, 330, 130, 7, b'FileInUseProcess', None, None, None)
        c = inuse.back(b'Exit', b'Ignore', name=b'Exit')
        c.event(b'EndDialog', b'Exit')
        c = inuse.next(b'Ignore', b'Retry', name=b'Ignore')
        c.event(b'EndDialog', b'Ignore')
        c = inuse.cancel(b'Retry', b'Exit', name=b'Retry')
        c.event(b'EndDialog', b'Retry')
        error = Dialog(db, b'ErrorDlg', 50, 10, 330, 101, 65543, title, b'ErrorText', None, None)
        error.text(b'ErrorText', 50, 9, 280, 48, 3, b'')
        error.pushbutton(b'N', 120, 72, 81, 21, 3, b'No', None).event(b'EndDialog', b'ErrorNo')
        error.pushbutton(b'Y', 240, 72, 81, 21, 3, b'Yes', None).event(b'EndDialog', b'ErrorYes')
        error.pushbutton(b'A', 0, 72, 81, 21, 3, b'Abort', None).event(b'EndDialog', b'ErrorAbort')
        error.pushbutton(b'C', 42, 72, 81, 21, 3, b'Cancel', None).event(b'EndDialog', b'ErrorCancel')
        error.pushbutton(b'I', 81, 72, 81, 21, 3, b'Ignore', None).event(b'EndDialog', b'ErrorIgnore')
        error.pushbutton(b'O', 159, 72, 81, 21, 3, b'Ok', None).event(b'EndDialog', b'ErrorOk')
        error.pushbutton(b'R', 198, 72, 81, 21, 3, b'Retry', None).event(b'EndDialog', b'ErrorRetry')
        cancel = Dialog(db, b'CancelDlg', 50, 10, 260, 85, 3, title, b'No', b'No', b'No')
        cancel.text(b'Text', 48, 15, 194, 30, 3, b'Are you sure you want to cancel [ProductName] installation?')
        c = cancel.pushbutton(b'Yes', 72, 57, 56, 17, 3, b'Yes', b'No')
        c.event(b'EndDialog', b'Exit')
        c = cancel.pushbutton(b'No', 132, 57, 56, 17, 3, b'No', b'Yes')
        c.event(b'EndDialog', b'Return')
        costing = Dialog(db, b'WaitForCostingDlg', 50, 10, 260, 85, modal, title, b'Return', b'Return', b'Return')
        costing.text(b'Text', 48, 15, 194, 30, 3, b'Please wait while the installer finishes determining your disk space requirements.')
        c = costing.pushbutton(b'Return', 102, 57, 56, 17, 3, b'Return', None)
        c.event(b'EndDialog', b'Exit')
        prep = PyDialog(db, b'PrepareDlg', x, y, w, h, modeless, title, b'Cancel', b'Cancel', b'Cancel')
        prep.text(b'Description', 15, 70, 320, 40, 196611, b'Please wait while the Installer prepares to guide you through the installation.')
        prep.title(b'Welcome to the [ProductName] Installer')
        c = prep.text(b'ActionText', 15, 110, 320, 20, 196611, b'Pondering...')
        c.mapping(b'ActionText', b'Text')
        c = prep.text(b'ActionData', 15, 135, 320, 30, 196611, None)
        c.mapping(b'ActionData', b'Text')
        prep.back(b'Back', None, active=0)
        prep.next(b'Next', None, active=0)
        c = prep.cancel(b'Cancel', None)
        c.event(b'SpawnDialog', b'CancelDlg')
        seldlg = PyDialog(db, b'SelectFeaturesDlg', x, y, w, h, modal, title, b'Next', b'Next', b'Cancel')
        seldlg.title(b'Select Python Installations')
        seldlg.text(b'Hint', 15, 30, 300, 20, 3, b'Select the Python locations where %s should be installed.' % self.distribution.get_fullname())
        seldlg.back(b'< Back', None, active=0)
        c = seldlg.next(b'Next >', b'Cancel')
        order = 1
        c.event(b'[TARGETDIR]', b'[SourceDir]', ordering=order)
        for version in self.versions + [self.other_version]:
            order += 1
            c.event(b'[TARGETDIR]', b'[TARGETDIR%s]' % version, b'FEATURE_SELECTED AND &Python%s=3' % version, ordering=order)

        c.event(b'SpawnWaitDialog', b'WaitForCostingDlg', ordering=order + 1)
        c.event(b'EndDialog', b'Return', ordering=order + 2)
        c = seldlg.cancel(b'Cancel', b'Features')
        c.event(b'SpawnDialog', b'CancelDlg')
        c = seldlg.control(b'Features', b'SelectionTree', 15, 60, 300, 120, 3, b'FEATURE', None, b'PathEdit', None)
        c.event(b'[FEATURE_SELECTED]', b'1')
        ver = self.other_version
        install_other_cond = b'FEATURE_SELECTED AND &Python%s=3' % ver
        dont_install_other_cond = b'FEATURE_SELECTED AND &Python%s<>3' % ver
        c = seldlg.text(b'Other', 15, 200, 300, 15, 3, b'Provide an alternate Python location')
        c.condition(b'Enable', install_other_cond)
        c.condition(b'Show', install_other_cond)
        c.condition(b'Disable', dont_install_other_cond)
        c.condition(b'Hide', dont_install_other_cond)
        c = seldlg.control(b'PathEdit', b'PathEdit', 15, 215, 300, 16, 1, b'TARGETDIR' + ver, None, b'Next', None)
        c.condition(b'Enable', install_other_cond)
        c.condition(b'Show', install_other_cond)
        c.condition(b'Disable', dont_install_other_cond)
        c.condition(b'Hide', dont_install_other_cond)
        cost = PyDialog(db, b'DiskCostDlg', x, y, w, h, modal, title, b'OK', b'OK', b'OK', bitmap=False)
        cost.text(b'Title', 15, 6, 200, 15, 196611, b'{\\DlgFontBold8}Disk Space Requirements')
        cost.text(b'Description', 20, 20, 280, 20, 196611, b'The disk space required for the installation of the selected features.')
        cost.text(b'Text', 20, 53, 330, 60, 3, b'The highlighted volumes (if any) do not have enough disk space available for the currently selected features.  You can either remove some files from the highlighted volumes, or choose to install less features onto local drive(s), or select different destination drive(s).')
        cost.control(b'VolumeList', b'VolumeCostList', 20, 100, 330, 150, 393223, None, b'{120}{70}{70}{70}{70}', None, None)
        cost.xbutton(b'OK', b'Ok', None, 0.5).event(b'EndDialog', b'Return')
        whichusers = PyDialog(db, b'WhichUsersDlg', x, y, w, h, modal, title, b'AdminInstall', b'Next', b'Cancel')
        whichusers.title(b'Select whether to install [ProductName] for all users of this computer.')
        g = whichusers.radiogroup(b'AdminInstall', 15, 60, 260, 50, 3, b'WhichUsers', b'', b'Next')
        g.add(b'ALL', 0, 5, 150, 20, b'Install for all users')
        g.add(b'JUSTME', 0, 25, 150, 20, b'Install just for me')
        whichusers.back(b'Back', None, active=0)
        c = whichusers.next(b'Next >', b'Cancel')
        c.event(b'[ALLUSERS]', b'1', b'WhichUsers="ALL"', 1)
        c.event(b'EndDialog', b'Return', ordering=2)
        c = whichusers.cancel(b'Cancel', b'AdminInstall')
        c.event(b'SpawnDialog', b'CancelDlg')
        progress = PyDialog(db, b'ProgressDlg', x, y, w, h, modeless, title, b'Cancel', b'Cancel', b'Cancel', bitmap=False)
        progress.text(b'Title', 20, 15, 200, 15, 196611, b'{\\DlgFontBold8}[Progress1] [ProductName]')
        progress.text(b'Text', 35, 65, 300, 30, 3, b'Please wait while the Installer [Progress2] [ProductName]. This may take several minutes.')
        progress.text(b'StatusLabel', 35, 100, 35, 20, 3, b'Status:')
        c = progress.text(b'ActionText', 70, 100, w - 70, 20, 3, b'Pondering...')
        c.mapping(b'ActionText', b'Text')
        c = progress.control(b'ProgressBar', b'ProgressBar', 35, 120, 300, 10, 65537, None, b'Progress done', None, None)
        c.mapping(b'SetProgress', b'Progress')
        progress.back(b'< Back', b'Next', active=False)
        progress.next(b'Next >', b'Cancel', active=False)
        progress.cancel(b'Cancel', b'Back').event(b'SpawnDialog', b'CancelDlg')
        maint = PyDialog(db, b'MaintenanceTypeDlg', x, y, w, h, modal, title, b'Next', b'Next', b'Cancel')
        maint.title(b'Welcome to the [ProductName] Setup Wizard')
        maint.text(b'BodyText', 15, 63, 330, 42, 3, b'Select whether you want to repair or remove [ProductName].')
        g = maint.radiogroup(b'RepairRadioGroup', 15, 108, 330, 60, 3, b'MaintenanceForm_Action', b'', b'Next')
        g.add(b'Repair', 0, 18, 200, 17, b'&Repair [ProductName]')
        g.add(b'Remove', 0, 36, 200, 17, b'Re&move [ProductName]')
        maint.back(b'< Back', None, active=False)
        c = maint.next(b'Finish', b'Cancel')
        c.event(b'[REINSTALL]', b'ALL', b'MaintenanceForm_Action="Repair"', 5)
        c.event(b'[Progress1]', b'Repairing', b'MaintenanceForm_Action="Repair"', 6)
        c.event(b'[Progress2]', b'repairs', b'MaintenanceForm_Action="Repair"', 7)
        c.event(b'Reinstall', b'ALL', b'MaintenanceForm_Action="Repair"', 8)
        c.event(b'[REMOVE]', b'ALL', b'MaintenanceForm_Action="Remove"', 11)
        c.event(b'[Progress1]', b'Removing', b'MaintenanceForm_Action="Remove"', 12)
        c.event(b'[Progress2]', b'removes', b'MaintenanceForm_Action="Remove"', 13)
        c.event(b'Remove', b'ALL', b'MaintenanceForm_Action="Remove"', 14)
        c.event(b'EndDialog', b'Return', b'MaintenanceForm_Action<>"Change"', 20)
        maint.cancel(b'Cancel', b'RepairRadioGroup').event(b'SpawnDialog', b'CancelDlg')
        return

    def get_installer_filename(self, fullname):
        if self.target_version:
            base_name = b'%s.%s-py%s.msi' % (fullname, self.plat_name,
             self.target_version)
        else:
            base_name = b'%s.%s.msi' % (fullname, self.plat_name)
        installer_name = os.path.join(self.dist_dir, base_name)
        return installer_name
