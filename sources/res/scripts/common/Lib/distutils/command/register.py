__revision__ = b'$Id$'
import urllib2, getpass, urlparse
from warnings import warn
from distutils.core import PyPIRCCommand
from distutils import log

class register(PyPIRCCommand):
    description = b'register the distribution with the Python package index'
    user_options = PyPIRCCommand.user_options + [
     (b'list-classifiers', None, b'list the valid Trove classifiers'),
     (b'strict', None, b'Will stop the registering if the meta-data are not fully compliant')]
    boolean_options = PyPIRCCommand.boolean_options + [
     b'verify', b'list-classifiers', b'strict']
    sub_commands = [
     (
      b'check', (lambda self: True))]

    def initialize_options(self):
        PyPIRCCommand.initialize_options(self)
        self.list_classifiers = 0
        self.strict = 0
        return

    def finalize_options(self):
        PyPIRCCommand.finalize_options(self)
        check_options = {b'strict': (b'register', self.strict), b'restructuredtext': (b'register', 1)}
        self.distribution.command_options[b'check'] = check_options
        return

    def run(self):
        self.finalize_options()
        self._set_config()
        for cmd_name in self.get_sub_commands():
            self.run_command(cmd_name)

        if self.dry_run:
            self.verify_metadata()
        elif self.list_classifiers:
            self.classifiers()
        else:
            self.send_metadata()
        return

    def check_metadata(self):
        warn(b'distutils.command.register.check_metadata is deprecated,               use the check command instead', PendingDeprecationWarning)
        check = self.distribution.get_command_obj(b'check')
        check.ensure_finalized()
        check.strict = self.strict
        check.restructuredtext = 1
        check.run()
        return

    def _set_config(self):
        config = self._read_pypirc()
        if config != {}:
            self.username = config[b'username']
            self.password = config[b'password']
            self.repository = config[b'repository']
            self.realm = config[b'realm']
            self.has_config = True
        elif self.repository not in (b'pypi', self.DEFAULT_REPOSITORY):
            raise ValueError(b'%s not found in .pypirc' % self.repository)
        if self.repository == b'pypi':
            self.repository = self.DEFAULT_REPOSITORY
        self.has_config = False
        return

    def classifiers(self):
        response = urllib2.urlopen(self.repository + b'?:action=list_classifiers')
        log.info(response.read())
        return

    def verify_metadata(self):
        code, result = self.post_to_server(self.build_post_data(b'verify'))
        log.info(b'Server response (%s): %s' % (code, result))
        return

    def send_metadata(self):
        if self.has_config:
            choice = b'1'
            username = self.username
            password = self.password
        else:
            choice = b'x'
            username = password = b''
        choices = (b'1 2 3 4').split()
        while choice not in choices:
            self.announce(b'We need to know who you are, so please choose either:\n 1. use your existing login,\n 2. register as a new user,\n 3. have the server generate a new password for you (and email it to you), or\n 4. quit\nYour selection [default 1]: ', log.INFO)
            choice = raw_input()
            if not choice:
                choice = b'1'
            elif choice not in choices:
                print b'Please choose one of the four options!'

        if choice == b'1':
            while not username:
                username = raw_input(b'Username: ')

            while not password:
                password = getpass.getpass(b'Password: ')

            auth = urllib2.HTTPPasswordMgr()
            host = urlparse.urlparse(self.repository)[1]
            auth.add_password(self.realm, host, username, password)
            code, result = self.post_to_server(self.build_post_data(b'submit'), auth)
            self.announce(b'Server response (%s): %s' % (code, result), log.INFO)
            if code == 200:
                if self.has_config:
                    self.distribution.password = password
                else:
                    self.announce(b'I can store your PyPI login so future submissions will be faster.', log.INFO)
                    self.announce(b'(the login will be stored in %s)' % self._get_rc_file(), log.INFO)
                    choice = b'X'
                    while choice.lower() not in b'yn':
                        choice = raw_input(b'Save your login (y/N)?')
                        if not choice:
                            choice = b'n'

                    if choice.lower() == b'y':
                        self._store_pypirc(username, password)
        elif choice == b'2':
            data = {b':action': b'user'}
            data[b'name'] = data[b'password'] = data[b'email'] = b''
            data[b'confirm'] = None
            while not data[b'name']:
                data[b'name'] = raw_input(b'Username: ')

            while data[b'password'] != data[b'confirm']:
                while not data[b'password']:
                    data[b'password'] = getpass.getpass(b'Password: ')

                while not data[b'confirm']:
                    data[b'confirm'] = getpass.getpass(b' Confirm: ')

                if data[b'password'] != data[b'confirm']:
                    data[b'password'] = b''
                    data[b'confirm'] = None
                    print b"Password and confirm don't match!"

            while not data[b'email']:
                data[b'email'] = raw_input(b'   EMail: ')

            code, result = self.post_to_server(data)
            if code != 200:
                log.info(b'Server response (%s): %s' % (code, result))
            else:
                log.info(b'You will receive an email shortly.')
                log.info(b'Follow the instructions in it to complete registration.')
        elif choice == b'3':
            data = {b':action': b'password_reset'}
            data[b'email'] = b''
            while not data[b'email']:
                data[b'email'] = raw_input(b'Your email address: ')

            code, result = self.post_to_server(data)
            log.info(b'Server response (%s): %s' % (code, result))
        return

    def build_post_data(self, action):
        meta = self.distribution.metadata
        data = {b':action': action, 
           b'metadata_version': b'1.0', 
           b'name': (meta.get_name()), 
           b'version': (meta.get_version()), 
           b'summary': (meta.get_description()), 
           b'home_page': (meta.get_url()), 
           b'author': (meta.get_contact()), 
           b'author_email': (meta.get_contact_email()), 
           b'license': (meta.get_licence()), 
           b'description': (meta.get_long_description()), 
           b'keywords': (meta.get_keywords()), 
           b'platform': (meta.get_platforms()), 
           b'classifiers': (meta.get_classifiers()), 
           b'download_url': (meta.get_download_url()), 
           b'provides': (meta.get_provides()), 
           b'requires': (meta.get_requires()), 
           b'obsoletes': (meta.get_obsoletes())}
        if data[b'provides'] or data[b'requires'] or data[b'obsoletes']:
            data[b'metadata_version'] = b'1.1'
        return data

    def post_to_server(self, data, auth=None):
        if b'name' in data:
            self.announce(b'Registering %s to %s' % (data[b'name'],
             self.repository), log.INFO)
        boundary = b'--------------GHSKFJDLGDS7543FJKLFHRE75642756743254'
        sep_boundary = b'\n--' + boundary
        end_boundary = sep_boundary + b'--'
        chunks = []
        for key, value in data.items():
            if type(value) not in (type([]), type(())):
                value = [
                 value]
            for value in value:
                chunks.append(sep_boundary)
                chunks.append(b'\nContent-Disposition: form-data; name="%s"' % key)
                chunks.append(b'\n\n')
                chunks.append(value)
                if value and value[-1] == b'\r':
                    chunks.append(b'\n')

        chunks.append(end_boundary)
        chunks.append(b'\n')
        body = []
        for chunk in chunks:
            if isinstance(chunk, unicode):
                body.append(chunk.encode(b'utf-8'))
            else:
                body.append(chunk)

        body = (b'').join(body)
        headers = {b'Content-type': (b'multipart/form-data; boundary=%s; charset=utf-8' % boundary), 
           b'Content-length': (str(len(body)))}
        req = urllib2.Request(self.repository, body, headers)
        opener = urllib2.build_opener(urllib2.HTTPBasicAuthHandler(password_mgr=auth))
        data = b''
        try:
            result = opener.open(req)
        except urllib2.HTTPError as e:
            if self.show_response:
                data = e.fp.read()
            result = (
             e.code, e.msg)
        except urllib2.URLError as e:
            result = (
             500, str(e))
        else:
            if self.show_response:
                data = result.read()
            result = (200, b'OK')

        if self.show_response:
            dashes = b'-' * 75
            self.announce(b'%s%s%s' % (dashes, data, dashes))
        return result
