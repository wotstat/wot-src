import os
from ConfigParser import ConfigParser
from distutils.cmd import Command
DEFAULT_PYPIRC = b'[distutils]\nindex-servers =\n    pypi\n\n[pypi]\nusername:%s\npassword:%s\n'

class PyPIRCCommand(Command):
    DEFAULT_REPOSITORY = b'https://upload.pypi.org/legacy/'
    DEFAULT_REALM = b'pypi'
    repository = None
    realm = None
    user_options = [
     (
      b'repository=', b'r',
      b'url of repository [default: %s]' % DEFAULT_REPOSITORY),
     (b'show-response', None, b'display full response text from server')]
    boolean_options = [
     b'show-response']

    def _get_rc_file(self):
        return os.path.join(os.path.expanduser(b'~'), b'.pypirc')

    def _store_pypirc(self, username, password):
        rc = self._get_rc_file()
        f = os.fdopen(os.open(rc, os.O_CREAT | os.O_WRONLY, 384), b'w')
        try:
            f.write(DEFAULT_PYPIRC % (username, password))
        finally:
            f.close()

        return

    def _read_pypirc(self):
        rc = self._get_rc_file()
        if os.path.exists(rc):
            self.announce(b'Using PyPI login from %s' % rc)
            repository = self.repository or self.DEFAULT_REPOSITORY
            config = ConfigParser()
            config.read(rc)
            sections = config.sections()
            if b'distutils' in sections:
                index_servers = config.get(b'distutils', b'index-servers')
                _servers = [server.strip() for server in index_servers.split(b'\n') if server.strip() != b'']
                if _servers == []:
                    if b'pypi' in sections:
                        _servers = [
                         b'pypi']
                    else:
                        return {}
                for server in _servers:
                    current = {b'server': server}
                    current[b'username'] = config.get(server, b'username')
                    for key, default in (
                     (b'repository',
                      self.DEFAULT_REPOSITORY),
                     (
                      b'realm', self.DEFAULT_REALM),
                     (b'password', None)):
                        if config.has_option(server, key):
                            current[key] = config.get(server, key)
                        else:
                            current[key] = default

                    if current[b'server'] == repository or current[b'repository'] == repository:
                        return current

            elif b'server-login' in sections:
                server = b'server-login'
                if config.has_option(server, b'repository'):
                    repository = config.get(server, b'repository')
                else:
                    repository = self.DEFAULT_REPOSITORY
                return {b'username': (config.get(server, b'username')), b'password': (config.get(server, b'password')), 
                   b'repository': repository, 
                   b'server': server, 
                   b'realm': (self.DEFAULT_REALM)}
        return {}

    def initialize_options(self):
        self.repository = None
        self.realm = None
        self.show_response = 0
        return

    def finalize_options(self):
        if self.repository is None:
            self.repository = self.DEFAULT_REPOSITORY
        if self.realm is None:
            self.realm = self.DEFAULT_REALM
        return
