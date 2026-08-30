__revision__ = b'$Id$'
from distutils.core import Command
from distutils.dist import PKG_INFO_ENCODING
from distutils.errors import DistutilsSetupError
try:
    from docutils.utils import Reporter
    from docutils.parsers.rst import Parser
    from docutils import frontend
    from docutils import nodes
    from StringIO import StringIO

    class SilentReporter(Reporter):

        def __init__(self, source, report_level, halt_level, stream=None, debug=0, encoding=b'ascii', error_handler=b'replace'):
            self.messages = []
            Reporter.__init__(self, source, report_level, halt_level, stream, debug, encoding, error_handler)
            return

        def system_message(self, level, message, *children, **kwargs):
            self.messages.append((level, message, children, kwargs))
            return nodes.system_message(message, level=level, type=self.levels[level], *children, **kwargs)


    HAS_DOCUTILS = True
except ImportError:
    HAS_DOCUTILS = False

class check(Command):
    description = b'perform some checks on the package'
    user_options = [(b'metadata', b'm', b'Verify meta-data'),
     (b'restructuredtext', b'r', b'Checks if long string meta-data syntax are reStructuredText-compliant'),
     (b'strict', b's', b'Will exit with an error if a check fails')]
    boolean_options = [
     b'metadata', b'restructuredtext', b'strict']

    def initialize_options(self):
        self.restructuredtext = 0
        self.metadata = 1
        self.strict = 0
        self._warnings = 0
        return

    def finalize_options(self):
        return

    def warn(self, msg):
        self._warnings += 1
        return Command.warn(self, msg)

    def run(self):
        if self.metadata:
            self.check_metadata()
        if self.restructuredtext:
            if HAS_DOCUTILS:
                self.check_restructuredtext()
            elif self.strict:
                raise DistutilsSetupError(b'The docutils package is needed.')
        if self.strict and self._warnings > 0:
            raise DistutilsSetupError(b'Please correct your package.')
        return

    def check_metadata(self):
        metadata = self.distribution.metadata
        missing = []
        for attr in (b'name', b'version', b'url'):
            if not (hasattr(metadata, attr) and getattr(metadata, attr)):
                missing.append(attr)

        if missing:
            self.warn(b'missing required meta-data: %s' % (b', ').join(missing))
        if metadata.author:
            if not metadata.author_email:
                self.warn(b"missing meta-data: if 'author' supplied, " + b"'author_email' must be supplied too")
        elif metadata.maintainer:
            if not metadata.maintainer_email:
                self.warn(b"missing meta-data: if 'maintainer' supplied, " + b"'maintainer_email' must be supplied too")
        else:
            self.warn(b'missing meta-data: either (author and author_email) ' + b'or (maintainer and maintainer_email) ' + b'must be supplied')
        return

    def check_restructuredtext(self):
        data = self.distribution.get_long_description()
        if not isinstance(data, unicode):
            data = data.decode(PKG_INFO_ENCODING)
        for warning in self._check_rst_data(data):
            line = warning[-1].get(b'line')
            if line is None:
                warning = warning[1]
            else:
                warning = b'%s (line %s)' % (warning[1], line)
            self.warn(warning)

        return

    def _check_rst_data(self, data):
        source_path = self.distribution.script_name or b'setup.py'
        parser = Parser()
        settings = frontend.OptionParser(components=(Parser,)).get_default_values()
        settings.tab_width = 4
        settings.pep_references = None
        settings.rfc_references = None
        reporter = SilentReporter(source_path, settings.report_level, settings.halt_level, stream=settings.warning_stream, debug=settings.debug, encoding=settings.error_encoding, error_handler=settings.error_encoding_error_handler)
        document = nodes.document(settings, reporter, source=source_path)
        document.note_source(source_path, -1)
        try:
            parser.parse(data, document)
        except AttributeError as e:
            reporter.messages.append((
             -1, b'Could not finish the parsing: %s.' % e, b'', {}))

        return reporter.messages
