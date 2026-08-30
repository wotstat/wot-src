import os, sys, unittest, importlib, test.test_support
this_dir_path = os.path.abspath(os.path.dirname(__file__))

def is_package(path):
    for name in os.listdir(path):
        if name in (b'__init__.py', b'__init__.pyc', b'__init.pyo'):
            return True

    return False


def get_tests_modules(basepath=this_dir_path, gui=True, packages=None):
    py_ext = b'.py'
    for dirpath, dirnames, filenames in os.walk(basepath):
        for dirname in list(dirnames):
            if dirname[0] == b'.':
                dirnames.remove(dirname)

        if is_package(dirpath) and filenames:
            pkg_name = dirpath[len(basepath) + len(os.sep):].replace(b'/', b'.')
            if packages and pkg_name not in packages:
                continue
            filenames = filter((lambda x: x.startswith(b'test_') and x.endswith(py_ext)), filenames)
            for name in filenames:
                try:
                    yield importlib.import_module(b'.%s' % name[:-len(py_ext)], pkg_name)
                except test.test_support.ResourceDenied:
                    if gui:
                        raise

    return


def get_tests(text=True, gui=True, packages=None):
    attrs = []
    if text:
        attrs.append(b'tests_nogui')
    if gui:
        attrs.append(b'tests_gui')
    for module in get_tests_modules(gui=gui, packages=packages):
        for attr in attrs:
            for test in getattr(module, attr, ()):
                yield test

    return


if __name__ == b'__main__':
    test.test_support.run_unittest(*get_tests())
