__revision__ = b'$Id$'
import os
from warnings import warn
import sys
from distutils.errors import DistutilsExecError
from distutils.spawn import spawn
from distutils.dir_util import mkpath
from distutils import log
try:
    from pwd import getpwnam
except ImportError:
    getpwnam = None

try:
    from grp import getgrnam
except ImportError:
    getgrnam = None

def _get_gid(name):
    if getgrnam is None or name is None:
        return
    try:
        result = getgrnam(name)
    except KeyError:
        result = None

    if result is not None:
        return result[2]
    else:
        return


def _get_uid(name):
    if getpwnam is None or name is None:
        return
    try:
        result = getpwnam(name)
    except KeyError:
        result = None

    if result is not None:
        return result[2]
    else:
        return


def make_tarball(base_name, base_dir, compress=b'gzip', verbose=0, dry_run=0, owner=None, group=None):
    tar_compression = {b'gzip': b'gz', b'bzip2': b'bz2', None: b'', b'compress': b''}
    compress_ext = {b'gzip': b'.gz', b'bzip2': b'.bz2', b'compress': b'.Z'}
    if compress is not None and compress not in compress_ext.keys():
        raise ValueError, b"bad value for 'compress': must be None, 'gzip', 'bzip2' or 'compress'"
    archive_name = base_name + b'.tar'
    if compress != b'compress':
        archive_name += compress_ext.get(compress, b'')
    mkpath(os.path.dirname(archive_name), dry_run=dry_run)
    import tarfile
    log.info(b'Creating tar archive')
    uid = _get_uid(owner)
    gid = _get_gid(group)

    def _set_uid_gid(tarinfo):
        if gid is not None:
            tarinfo.gid = gid
            tarinfo.gname = group
        if uid is not None:
            tarinfo.uid = uid
            tarinfo.uname = owner
        return tarinfo

    if not dry_run:
        tar = tarfile.open(archive_name, b'w|%s' % tar_compression[compress])
        try:
            tar.add(base_dir, filter=_set_uid_gid)
        finally:
            tar.close()

    if compress == b'compress':
        warn(b"'compress' will be deprecated.", PendingDeprecationWarning)
        compressed_name = archive_name + compress_ext[compress]
        if sys.platform == b'win32':
            cmd = [
             compress, archive_name, compressed_name]
        else:
            cmd = [
             compress, b'-f', archive_name]
        spawn(cmd, dry_run=dry_run)
        return compressed_name
    else:
        return archive_name


def make_zipfile(base_name, base_dir, verbose=0, dry_run=0):
    try:
        import zipfile
    except ImportError:
        zipfile = None

    zip_filename = base_name + b'.zip'
    mkpath(os.path.dirname(zip_filename), dry_run=dry_run)
    if zipfile is None:
        if verbose:
            zipoptions = b'-r'
        else:
            zipoptions = b'-rq'
        try:
            spawn([b'zip', zipoptions, zip_filename, base_dir], dry_run=dry_run)
        except DistutilsExecError:
            raise DistutilsExecError, b"unable to create zip file '%s': could neither import the 'zipfile' module nor find a standalone zip utility" % zip_filename

    else:
        log.info(b"creating '%s' and adding '%s' to it", zip_filename, base_dir)
        if not dry_run:
            zip = zipfile.ZipFile(zip_filename, b'w', compression=zipfile.ZIP_DEFLATED)
            if base_dir != os.curdir:
                path = os.path.normpath(os.path.join(base_dir, b''))
                zip.write(path, path)
                log.info(b"adding '%s'", path)
            for dirpath, dirnames, filenames in os.walk(base_dir):
                for name in dirnames:
                    path = os.path.normpath(os.path.join(dirpath, name, b''))
                    zip.write(path, path)
                    log.info(b"adding '%s'", path)

                for name in filenames:
                    path = os.path.normpath(os.path.join(dirpath, name))
                    if os.path.isfile(path):
                        zip.write(path, path)
                        log.info(b"adding '%s'" % path)

            zip.close()
    return zip_filename


ARCHIVE_FORMATS = {b'gztar': (
            make_tarball, [(b'compress', b'gzip')], b"gzip'ed tar-file"), 
   b'bztar': (
            make_tarball, [(b'compress', b'bzip2')], b"bzip2'ed tar-file"), 
   b'ztar': (
           make_tarball, [(b'compress', b'compress')], b'compressed tar file'), 
   b'tar': (
          make_tarball, [(b'compress', None)], b'uncompressed tar file'), 
   b'zip': (
          make_zipfile, [], b'ZIP file')}

def check_archive_formats(formats):
    for format in formats:
        if format not in ARCHIVE_FORMATS:
            return format

    return


def make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None):
    save_cwd = os.getcwd()
    if root_dir is not None:
        log.debug(b"changing into '%s'", root_dir)
        base_name = os.path.abspath(base_name)
        if not dry_run:
            os.chdir(root_dir)
    if base_dir is None:
        base_dir = os.curdir
    kwargs = {b'dry_run': dry_run}
    try:
        format_info = ARCHIVE_FORMATS[format]
    except KeyError:
        raise ValueError, b"unknown archive format '%s'" % format

    func = format_info[0]
    for arg, val in format_info[1]:
        kwargs[arg] = val

    if format != b'zip':
        kwargs[b'owner'] = owner
        kwargs[b'group'] = group
    try:
        filename = func(base_name, base_dir, **kwargs)
    finally:
        if root_dir is not None:
            log.debug(b"changing back to '%s'", save_cwd)
            os.chdir(save_cwd)

    return filename
