import os
from framework import framework_info
from dylib import dylib_info
from itertools import *
__all__ = [
 b'dyld_find', b'framework_find',
 b'framework_info', b'dylib_info']
DEFAULT_FRAMEWORK_FALLBACK = [
 os.path.expanduser(b'~/Library/Frameworks'),
 b'/Library/Frameworks',
 b'/Network/Library/Frameworks',
 b'/System/Library/Frameworks']
DEFAULT_LIBRARY_FALLBACK = [
 os.path.expanduser(b'~/lib'),
 b'/usr/local/lib',
 b'/lib',
 b'/usr/lib']

def ensure_utf8(s):
    if isinstance(s, unicode):
        return s.encode(b'utf8')
    return s


def dyld_env(env, var):
    if env is None:
        env = os.environ
    rval = env.get(var)
    if rval is None:
        return []
    else:
        return rval.split(b':')


def dyld_image_suffix(env=None):
    if env is None:
        env = os.environ
    return env.get(b'DYLD_IMAGE_SUFFIX')


def dyld_framework_path(env=None):
    return dyld_env(env, b'DYLD_FRAMEWORK_PATH')


def dyld_library_path(env=None):
    return dyld_env(env, b'DYLD_LIBRARY_PATH')


def dyld_fallback_framework_path(env=None):
    return dyld_env(env, b'DYLD_FALLBACK_FRAMEWORK_PATH')


def dyld_fallback_library_path(env=None):
    return dyld_env(env, b'DYLD_FALLBACK_LIBRARY_PATH')


def dyld_image_suffix_search(iterator, env=None):
    suffix = dyld_image_suffix(env)
    if suffix is None:
        return iterator
    else:

        def _inject(iterator=iterator, suffix=suffix):
            for path in iterator:
                if path.endswith(b'.dylib'):
                    yield path[:-len(b'.dylib')] + suffix + b'.dylib'
                else:
                    yield path + suffix
                yield path

            return

        return _inject()


def dyld_override_search(name, env=None):
    framework = framework_info(name)
    if framework is not None:
        for path in dyld_framework_path(env):
            yield os.path.join(path, framework[b'name'])

    for path in dyld_library_path(env):
        yield os.path.join(path, os.path.basename(name))

    return


def dyld_executable_path_search(name, executable_path=None):
    if name.startswith(b'@executable_path/') and executable_path is not None:
        yield os.path.join(executable_path, name[len(b'@executable_path/'):])
    return


def dyld_default_search(name, env=None):
    yield name
    framework = framework_info(name)
    if framework is not None:
        fallback_framework_path = dyld_fallback_framework_path(env)
        for path in fallback_framework_path:
            yield os.path.join(path, framework[b'name'])

    fallback_library_path = dyld_fallback_library_path(env)
    for path in fallback_library_path:
        yield os.path.join(path, os.path.basename(name))

    if framework is not None and not fallback_framework_path:
        for path in DEFAULT_FRAMEWORK_FALLBACK:
            yield os.path.join(path, framework[b'name'])

    if not fallback_library_path:
        for path in DEFAULT_LIBRARY_FALLBACK:
            yield os.path.join(path, os.path.basename(name))

    return


def dyld_find(name, executable_path=None, env=None):
    name = ensure_utf8(name)
    executable_path = ensure_utf8(executable_path)
    for path in dyld_image_suffix_search(chain(dyld_override_search(name, env), dyld_executable_path_search(name, executable_path), dyld_default_search(name, env)), env):
        if os.path.isfile(path):
            return path

    raise ValueError(b'dylib %s could not be found' % (name,))
    return


def framework_find(fn, executable_path=None, env=None):
    try:
        return dyld_find(fn, executable_path=executable_path, env=env)
    except ValueError as e:
        pass

    fmwk_index = fn.rfind(b'.framework')
    if fmwk_index == -1:
        fmwk_index = len(fn)
        fn += b'.framework'
    fn = os.path.join(fn, os.path.basename(fn[:fmwk_index]))
    try:
        return dyld_find(fn, executable_path=executable_path, env=env)
    except ValueError:
        raise e

    return


def test_dyld_find():
    env = {}
    return


if __name__ == b'__main__':
    test_dyld_find()
