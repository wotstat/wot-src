__revision__ = b'$Id$'
import sys, os, string
from distutils.core import Command
from distutils.debug import DEBUG
from distutils.file_util import write_file
from distutils.sysconfig import get_python_version
from distutils.errors import DistutilsOptionError, DistutilsPlatformError, DistutilsFileError, DistutilsExecError
from distutils import log

class bdist_rpm(Command):
    description = b'create an RPM distribution'
    user_options = [
     94, 
     95, 
     96, 
     97, 
     98, 
     99, 
     100, 
     101, 
     102, 
     103, 
     104, 
     105, 
     106, 
     107, 
     108, 
     109, 
     110, 
     111, 
     112, 
     113, 
     114, 
     115, 
     116, 
     117, 
     118, 
     119, 
     120, 
     121, 
     122, 
     123, 
     124, 
     125, 
     126, 
     127, 
     128, 
     129, 
     130, 
     131, 
     132, 
     133, 
     134]
    boolean_options = [
     50, 55, 59, 
     48, 83]
    negative_opt = {b'no-keep-temp': b'keep-temp', b'no-rpm-opt-flags': b'use-rpm-opt-flags', 
       b'rpm2-mode': b'rpm3-mode'}

    def initialize_options(self):
        self.bdist_base = None
        self.rpm_base = None
        self.dist_dir = None
        self.python = None
        self.fix_python = None
        self.spec_only = None
        self.binary_only = None
        self.source_only = None
        self.use_bzip2 = None
        self.distribution_name = None
        self.group = None
        self.release = None
        self.serial = None
        self.vendor = None
        self.packager = None
        self.doc_files = None
        self.changelog = None
        self.icon = None
        self.prep_script = None
        self.build_script = None
        self.install_script = None
        self.clean_script = None
        self.verify_script = None
        self.pre_install = None
        self.post_install = None
        self.pre_uninstall = None
        self.post_uninstall = None
        self.prep = None
        self.provides = None
        self.requires = None
        self.conflicts = None
        self.build_requires = None
        self.obsoletes = None
        self.keep_temp = 0
        self.use_rpm_opt_flags = 1
        self.rpm3_mode = 1
        self.no_autoreq = 0
        self.force_arch = None
        self.quiet = 0
        return

    def finalize_options(self):
        self.set_undefined_options(b'bdist', (b'bdist_base', b'bdist_base'))
        if self.rpm_base is None:
            if not self.rpm3_mode:
                raise DistutilsOptionError, b'you must specify --rpm-base in RPM 2 mode'
            self.rpm_base = os.path.join(self.bdist_base, b'rpm')
        if self.python is None:
            if self.fix_python:
                self.python = sys.executable
            else:
                self.python = b'python'
        elif self.fix_python:
            raise DistutilsOptionError, b'--python and --fix-python are mutually exclusive options'
        if os.name != b'posix':
            raise DistutilsPlatformError, b"don't know how to create RPM distributions on platform %s" % os.name
        if self.binary_only and self.source_only:
            raise DistutilsOptionError, b"cannot supply both '--source-only' and '--binary-only'"
        if not self.distribution.has_ext_modules():
            self.use_rpm_opt_flags = 0
        self.set_undefined_options(b'bdist', (b'dist_dir', b'dist_dir'))
        self.finalize_package_data()
        return

    def finalize_package_data(self):
        self.ensure_string(b'group', b'Development/Libraries')
        self.ensure_string(b'vendor', b'%s <%s>' % (self.distribution.get_contact(),
         self.distribution.get_contact_email()))
        self.ensure_string(b'packager')
        self.ensure_string_list(b'doc_files')
        if isinstance(self.doc_files, list):
            for readme in (b'README', b'README.txt'):
                if os.path.exists(readme) and readme not in self.doc_files:
                    self.doc_files.append(readme)

        self.ensure_string(b'release', b'1')
        self.ensure_string(b'serial')
        self.ensure_string(b'distribution_name')
        self.ensure_string(b'changelog')
        self.changelog = self._format_changelog(self.changelog)
        self.ensure_filename(b'icon')
        self.ensure_filename(b'prep_script')
        self.ensure_filename(b'build_script')
        self.ensure_filename(b'install_script')
        self.ensure_filename(b'clean_script')
        self.ensure_filename(b'verify_script')
        self.ensure_filename(b'pre_install')
        self.ensure_filename(b'post_install')
        self.ensure_filename(b'pre_uninstall')
        self.ensure_filename(b'post_uninstall')
        self.ensure_string_list(b'provides')
        self.ensure_string_list(b'requires')
        self.ensure_string_list(b'conflicts')
        self.ensure_string_list(b'build_requires')
        self.ensure_string_list(b'obsoletes')
        self.ensure_string(b'force_arch')
        return

    def run(self):
        if DEBUG:
            print b'before _get_package_data():'
            print b'vendor =', self.vendor
            print b'packager =', self.packager
            print b'doc_files =', self.doc_files
            print b'changelog =', self.changelog
        if self.spec_only:
            spec_dir = self.dist_dir
            self.mkpath(spec_dir)
        else:
            rpm_dir = {}
            for d in (b'SOURCES', b'SPECS', b'BUILD', b'RPMS', b'SRPMS'):
                rpm_dir[d] = os.path.join(self.rpm_base, d)
                self.mkpath(rpm_dir[d])

            spec_dir = rpm_dir[b'SPECS']
        spec_path = os.path.join(spec_dir, b'%s.spec' % self.distribution.get_name())
        self.execute(write_file, (
         spec_path,
         self._make_spec_file()), b"writing '%s'" % spec_path)
        if self.spec_only:
            return
        else:
            saved_dist_files = self.distribution.dist_files[:]
            sdist = self.reinitialize_command(b'sdist')
            if self.use_bzip2:
                sdist.formats = [
                 b'bztar']
            else:
                sdist.formats = [
                 b'gztar']
            self.run_command(b'sdist')
            self.distribution.dist_files = saved_dist_files
            source = sdist.get_archive_files()[0]
            source_dir = rpm_dir[b'SOURCES']
            self.copy_file(source, source_dir)
            if self.icon:
                if os.path.exists(self.icon):
                    self.copy_file(self.icon, source_dir)
                else:
                    raise DistutilsFileError, b"icon file '%s' does not exist" % self.icon
            log.info(b'building RPMs')
            rpm_cmd = [b'rpm']
            if os.path.exists(b'/usr/bin/rpmbuild') or os.path.exists(b'/bin/rpmbuild'):
                rpm_cmd = [
                 b'rpmbuild']
            if self.source_only:
                rpm_cmd.append(b'-bs')
            elif self.binary_only:
                rpm_cmd.append(b'-bb')
            else:
                rpm_cmd.append(b'-ba')
            if self.rpm3_mode:
                rpm_cmd.extend([b'--define',
                 b'_topdir %s' % os.path.abspath(self.rpm_base)])
            if not self.keep_temp:
                rpm_cmd.append(b'--clean')
            if self.quiet:
                rpm_cmd.append(b'--quiet')
            rpm_cmd.append(spec_path)
            nvr_string = b'%{name}-%{version}-%{release}'
            src_rpm = nvr_string + b'.src.rpm'
            non_src_rpm = b'%{arch}/' + nvr_string + b'.%{arch}.rpm'
            q_cmd = b"rpm -q --qf '%s %s\\n' --specfile '%s'" % (
             src_rpm, non_src_rpm, spec_path)
            out = os.popen(q_cmd)
            try:
                binary_rpms = []
                source_rpm = None
                while 1:
                    line = out.readline()
                    if not line:
                        break
                    l = string.split(string.strip(line))
                    binary_rpms.append(l[1])
                    if source_rpm is None:
                        source_rpm = l[0]

                status = out.close()
                if status:
                    raise DistutilsExecError(b'Failed to execute: %s' % repr(q_cmd))
            finally:
                out.close()

            self.spawn(rpm_cmd)
            if not self.dry_run:
                if self.distribution.has_ext_modules():
                    pyversion = get_python_version()
                else:
                    pyversion = b'any'
                if not self.binary_only:
                    srpm = os.path.join(rpm_dir[b'SRPMS'], source_rpm)
                    self.move_file(srpm, self.dist_dir)
                    filename = os.path.join(self.dist_dir, source_rpm)
                    self.distribution.dist_files.append((
                     b'bdist_rpm', pyversion, filename))
                if not self.source_only:
                    for rpm in binary_rpms:
                        rpm = os.path.join(rpm_dir[b'RPMS'], rpm)
                        if os.path.exists(rpm):
                            self.move_file(rpm, self.dist_dir)
                            filename = os.path.join(self.dist_dir, os.path.basename(rpm))
                            self.distribution.dist_files.append((
                             b'bdist_rpm', pyversion, filename))

            return

    def _dist_path(self, path):
        return os.path.join(self.dist_dir, os.path.basename(path))

    def _make_spec_file(self):
        spec_file = [
         b'%define name ' + self.distribution.get_name(),
         b'%define version ' + self.distribution.get_version().replace(b'-', b'_'),
         b'%define unmangled_version ' + self.distribution.get_version(),
         b'%define release ' + self.release.replace(b'-', b'_'),
         b'',
         b'Summary: ' + self.distribution.get_description()]
        spec_file.extend([
         b'Name: %{name}',
         b'Version: %{version}',
         b'Release: %{release}'])
        if self.use_bzip2:
            spec_file.append(b'Source0: %{name}-%{unmangled_version}.tar.bz2')
        else:
            spec_file.append(b'Source0: %{name}-%{unmangled_version}.tar.gz')
        spec_file.extend([
         b'License: ' + self.distribution.get_license(),
         b'Group: ' + self.group,
         b'BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot',
         b'Prefix: %{_prefix}'])
        if not self.force_arch:
            if not self.distribution.has_ext_modules():
                spec_file.append(b'BuildArch: noarch')
        else:
            spec_file.append(b'BuildArch: %s' % self.force_arch)
        for field in (b'Vendor', b'Packager', b'Provides', b'Requires', b'Conflicts', b'Obsoletes'):
            val = getattr(self, string.lower(field))
            if isinstance(val, list):
                spec_file.append(b'%s: %s' % (field, string.join(val)))
            elif val is not None:
                spec_file.append(b'%s: %s' % (field, val))

        if self.distribution.get_url() != b'UNKNOWN':
            spec_file.append(b'Url: ' + self.distribution.get_url())
        if self.distribution_name:
            spec_file.append(b'Distribution: ' + self.distribution_name)
        if self.build_requires:
            spec_file.append(b'BuildRequires: ' + string.join(self.build_requires))
        if self.icon:
            spec_file.append(b'Icon: ' + os.path.basename(self.icon))
        if self.no_autoreq:
            spec_file.append(b'AutoReq: 0')
        spec_file.extend([
         b'',
         b'%description',
         self.distribution.get_long_description()])
        def_setup_call = b'%s %s' % (self.python, os.path.basename(sys.argv[0]))
        def_build = b'%s build' % def_setup_call
        if self.use_rpm_opt_flags:
            def_build = b'env CFLAGS="$RPM_OPT_FLAGS" ' + def_build
        install_cmd = b'%s install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES' % def_setup_call
        script_options = [
         (b'prep', b'prep_script', b'%setup -n %{name}-%{unmangled_version}'),
         (
          b'build', b'build_script', def_build),
         (
          b'install', b'install_script', install_cmd),
         (b'clean', b'clean_script', b'rm -rf $RPM_BUILD_ROOT'),
         (b'verifyscript', b'verify_script', None),
         (b'pre', b'pre_install', None),
         (b'post', b'post_install', None),
         (b'preun', b'pre_uninstall', None),
         (b'postun', b'post_uninstall', None)]
        for rpm_opt, attr, default in script_options:
            val = getattr(self, attr)
            if val or default:
                spec_file.extend([
                 b'',
                 b'%' + rpm_opt])
                if val:
                    spec_file.extend(string.split(open(val, b'r').read(), b'\n'))
                else:
                    spec_file.append(default)

        spec_file.extend([
         b'',
         b'%files -f INSTALLED_FILES',
         b'%defattr(-,root,root)'])
        if self.doc_files:
            spec_file.append(b'%doc ' + string.join(self.doc_files))
        if self.changelog:
            spec_file.extend([
             b'',
             b'%changelog'])
            spec_file.extend(self.changelog)
        return spec_file

    def _format_changelog(self, changelog):
        if not changelog:
            return changelog
        new_changelog = []
        for line in string.split(string.strip(changelog), b'\n'):
            line = string.strip(line)
            if line[0] == b'*':
                new_changelog.extend([b'', line])
            elif line[0] == b'-':
                new_changelog.append(line)
            else:
                new_changelog.append(b'  ' + line)

        if not new_changelog[0]:
            del new_changelog[0]
        return new_changelog
