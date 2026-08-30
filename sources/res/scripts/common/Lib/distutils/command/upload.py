import os, socket, platform
from urllib2 import urlopen, Request, HTTPError
from base64 import standard_b64encode
import urlparse, cStringIO as StringIO
from hashlib import md5
from distutils.errors import DistutilsError, DistutilsOptionError
from distutils.core import PyPIRCCommand
from distutils.spawn import spawn
from distutils import log

class upload(PyPIRCCommand):
    description = b'upload binary package to PyPI'
    user_options = PyPIRCCommand.user_options + [
     (b'sign', b's', b'sign files to upload using gpg'),
     (b'identity=', b'i', b'GPG identity used to sign files')]
    boolean_options = PyPIRCCommand.boolean_options + [b'sign']

    def initialize_options(self):
        PyPIRCCommand.initialize_options(self)
        self.username = b''
        self.password = b''
        self.show_response = 0
        self.sign = False
        self.identity = None
        return

    def finalize_options(self):
        PyPIRCCommand.finalize_options(self)
        if self.identity and not self.sign:
            raise DistutilsOptionError(b'Must use --sign for --identity to have meaning')
        config = self._read_pypirc()
        if config != {}:
            self.username = config[b'username']
            self.password = config[b'password']
            self.repository = config[b'repository']
            self.realm = config[b'realm']
        if not self.password and self.distribution.password:
            self.password = self.distribution.password
        return

    def run(self):
        if not self.distribution.dist_files:
            msg = b'Must create and upload files in one command (e.g. setup.py sdist upload)'
            raise DistutilsOptionError(msg)
        for command, pyversion, filename in self.distribution.dist_files:
            self.upload_file(command, pyversion, filename)

        return

    def upload_file(self, command, pyversion, filename):
        schema, netloc, url, params, query, fragments = urlparse.urlparse(self.repository)
        if params or query or fragments:
            raise AssertionError(b'Incompatible url %s' % self.repository)
        if schema not in (b'http', b'https'):
            raise AssertionError(b'unsupported schema ' + schema)
        if self.sign:
            gpg_args = [
             b'gpg', b'--detach-sign', b'-a', filename]
            if self.identity:
                gpg_args[2:2] = [
                 b'--local-user', self.identity]
            spawn(gpg_args, dry_run=self.dry_run)
        f = open(filename, b'rb')
        try:
            content = f.read()
        finally:
            f.close()

        meta = self.distribution.metadata
        data = {b':action': b'file_upload', 
           b'protcol_version': b'1', 
           b'name': (meta.get_name()), 
           b'version': (meta.get_version()), 
           b'content': (
                      os.path.basename(filename), content), 
           b'filetype': command, 
           b'pyversion': pyversion, 
           b'md5_digest': (md5(content).hexdigest()), 
           b'metadata_version': b'1.0', 
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
        comment = b''
        if command == b'bdist_rpm':
            dist, version, id = platform.dist()
            if dist:
                comment = b'built for %s %s' % (dist, version)
        elif command == b'bdist_dumb':
            comment = b'built for %s' % platform.platform(terse=1)
        data[b'comment'] = comment
        if self.sign:
            data[b'gpg_signature'] = (
             os.path.basename(filename) + b'.asc',
             open(filename + b'.asc').read())
        auth = b'Basic ' + standard_b64encode(self.username + b':' + self.password)
        boundary = b'--------------GHSKFJDLGDS7543FJKLFHRE75642756743254'
        sep_boundary = b'\r\n--' + boundary
        end_boundary = sep_boundary + b'--\r\n'
        body = StringIO.StringIO()
        for key, value in data.items():
            if not isinstance(value, list):
                value = [
                 value]
            for value in value:
                if isinstance(value, tuple):
                    fn = b';filename="%s"' % value[0]
                    value = value[1]
                else:
                    fn = b''
                body.write(sep_boundary)
                body.write(b'\r\nContent-Disposition: form-data; name="%s"' % key)
                body.write(fn)
                body.write(b'\r\n\r\n')
                body.write(value)

        body.write(end_boundary)
        body = body.getvalue()
        self.announce(b'Submitting %s to %s' % (filename, self.repository), log.INFO)
        headers = {b'Content-type': (b'multipart/form-data; boundary=%s' % boundary), 
           b'Content-length': (str(len(body))), 
           b'Authorization': auth}
        request = Request(self.repository, data=body, headers=headers)
        try:
            result = urlopen(request)
            status = result.getcode()
            reason = result.msg
            if self.show_response:
                msg = (b'\n').join((b'-' * 75, result.read(), b'-' * 75))
                self.announce(msg, log.INFO)
        except socket.error as e:
            self.announce(str(e), log.ERROR)
            raise
        except HTTPError as e:
            status = e.code
            reason = e.msg

        if status == 200:
            self.announce(b'Server response (%s): %s' % (status, reason), log.INFO)
        else:
            msg = b'Upload failed (%s): %s' % (status, reason)
            self.announce(msg, log.ERROR)
            raise DistutilsError(msg)
        return
