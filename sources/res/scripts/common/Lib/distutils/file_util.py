__revision__ = b'$Id$'
import os
from distutils.errors import DistutilsFileError
from distutils import log
_copy_action = {None: b'copying', b'hard': b'hard linking', 
   b'sym': b'symbolically linking'}

def _copy_file_contents(src, dst, buffer_size=16384):
    fsrc = None
    fdst = None
    try:
        try:
            fsrc = open(src, b'rb')
        except os.error as (errno, errstr):
            raise DistutilsFileError(b"could not open '%s': %s" % (src, errstr))

        if os.path.exists(dst):
            try:
                os.unlink(dst)
            except os.error as (errno, errstr):
                raise DistutilsFileError(b"could not delete '%s': %s" % (dst, errstr))

        try:
            fdst = open(dst, b'wb')
        except os.error as (errno, errstr):
            raise DistutilsFileError(b"could not create '%s': %s" % (dst, errstr))

        while 1:
            try:
                buf = fsrc.read(buffer_size)
            except os.error as (errno, errstr):
                raise DistutilsFileError(b"could not read from '%s': %s" % (src, errstr))

            if not buf:
                break
            try:
                fdst.write(buf)
            except os.error as (errno, errstr):
                raise DistutilsFileError(b"could not write to '%s': %s" % (dst, errstr))

    finally:
        if fdst:
            fdst.close()
        if fsrc:
            fsrc.close()

    return


def copy_file(src, dst, preserve_mode=1, preserve_times=1, update=0, link=None, verbose=1, dry_run=0):
    from distutils.dep_util import newer
    from stat import ST_ATIME, ST_MTIME, ST_MODE, S_IMODE
    if not os.path.isfile(src):
        raise DistutilsFileError(b"can't copy '%s': doesn't exist or not a regular file" % src)
    if os.path.isdir(dst):
        dir = dst
        dst = os.path.join(dst, os.path.basename(src))
    else:
        dir = os.path.dirname(dst)
    if update and not newer(src, dst):
        if verbose >= 1:
            log.debug(b'not copying %s (output up-to-date)', src)
        return (dst, 0)
    try:
        action = _copy_action[link]
    except KeyError:
        raise ValueError(b"invalid value '%s' for 'link' argument" % link)

    if verbose >= 1:
        if os.path.basename(dst) == os.path.basename(src):
            log.info(b'%s %s -> %s', action, src, dir)
        else:
            log.info(b'%s %s -> %s', action, src, dst)
    if dry_run:
        return (dst, 1)
    if link == b'hard':
        if not (os.path.exists(dst) and os.path.samefile(src, dst)):
            try:
                os.link(src, dst)
                return (dst, 1)
            except OSError:
                pass

    elif link == b'sym':
        if not (os.path.exists(dst) and os.path.samefile(src, dst)):
            os.symlink(src, dst)
            return (
             dst, 1)
    _copy_file_contents(src, dst)
    if preserve_mode or preserve_times:
        st = os.stat(src)
        if preserve_times:
            os.utime(dst, (st[ST_ATIME], st[ST_MTIME]))
        if preserve_mode:
            os.chmod(dst, S_IMODE(st[ST_MODE]))
    return (
     dst, 1)


def move_file(src, dst, verbose=1, dry_run=0):
    from os.path import exists, isfile, isdir, basename, dirname
    import errno
    if verbose >= 1:
        log.info(b'moving %s -> %s', src, dst)
    if dry_run:
        return dst
    if not isfile(src):
        raise DistutilsFileError(b"can't move '%s': not a regular file" % src)
    if isdir(dst):
        dst = os.path.join(dst, basename(src))
    elif exists(dst):
        raise DistutilsFileError(b"can't move '%s': destination '%s' already exists" % (
         src, dst))
    if not isdir(dirname(dst)):
        raise DistutilsFileError(b"can't move '%s': destination '%s' not a valid path" % (
         src, dst))
    copy_it = 0
    try:
        os.rename(src, dst)
    except os.error as (num, msg):
        if num == errno.EXDEV:
            copy_it = 1
        else:
            raise DistutilsFileError(b"couldn't move '%s' to '%s': %s" % (src, dst, msg))

    if copy_it:
        copy_file(src, dst, verbose=verbose)
        try:
            os.unlink(src)
        except os.error as (num, msg):
            try:
                os.unlink(dst)
            except os.error:
                pass

            raise DistutilsFileError((b"couldn't move '%s' to '%s' by copy/delete: " + b"delete '%s' failed: %s") % (
             src, dst, src, msg))

    return dst


def write_file(filename, contents):
    f = open(filename, b'w')
    try:
        for line in contents:
            f.write(line + b'\n')

    finally:
        f.close()

    return
