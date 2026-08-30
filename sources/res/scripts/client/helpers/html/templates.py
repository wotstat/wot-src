from types import DictType
from typing import TYPE_CHECKING
from collections import defaultdict
import ResMgr
from debug_utils import LOG_WARNING, LOG_ERROR, LOG_CURRENT_EXCEPTION
from helpers import html
if TYPE_CHECKING:
    from typing import Optional, Dict

class Template(object):

    def __init__(self, source, ctx=None):
        super(Template, self).__init__()
        self.source = source
        self.ctx = ctx
        return

    def __repr__(self):
        return (u'Template(source = {0:>s})').format(self.source)

    def format(self, ctx=None, **kwargs):
        sourceKey = kwargs.get(b'sourceKey', b'text')
        if sourceKey in self.source:
            text = unicode(self.source[sourceKey])
        else:
            LOG_ERROR(b'Invalid source key', sourceKey)
            return u''
        if ctx is None:
            ctx = {}
        if isinstance(self.ctx, DictType) and isinstance(ctx, DictType):
            ctx.update(self.ctx)
        if ctx:
            try:
                text = text % ctx
            except (ValueError, TypeError, KeyError, UnicodeDecodeError):
                LOG_WARNING(b'Can not format template (source = %r, ctx = %r)', text, ctx)
                LOG_CURRENT_EXCEPTION()

        return text


class DummyTemplate(Template):

    def __init__(self, source, ctx=None):
        super(DummyTemplate, self).__init__(source, ctx)
        if isinstance(self.source, bytes):
            self.source = unicode(self.source)
        return

    def __repr__(self):
        return (u'DummyTemplate(source = {0:>s})').format(self.source)

    def format(self, ctx=None, **kwargs):
        return self.source


class Collection(defaultdict):

    def __init__(self, domain, ns):
        super(Collection, self).__init__()
        self._domain = domain
        self._ns = ns
        return

    def __repr__(self):
        return (b'Collection(domain = {0:>s}, ns = {1:>s}, keys = {2!r:s})').format(self._domain, self._ns, self.keys())

    def __missing__(self, key):
        self[key] = value = DummyTemplate(key)
        return value

    def load(self, *args):
        raise NotImplementedError(b'Loader.load not implemented')
        return

    def unload(self):
        self.clear()
        return

    def _make(self, source):
        return Template(source)

    def format(self, key, ctx=None, **kwargs):
        return self[key].format(ctx=ctx, **kwargs)


class XMLCollection(Collection):

    def load(self, section=None, clear=False):
        if section is None:
            if clear:
                ResMgr.purge(self._domain)
            section = ResMgr.openSection(self._domain)
            if section is None:
                LOG_ERROR((b'{0:>s} can not open or read').format(self._domain))
                return
        if self._ns:
            subsection = section[self._ns]
            if subsection is None:
                return
        else:
            subsection = section
        for key, child in subsection.items():
            self[key] = self._make(child)

        return

    def _make(self, source):
        keys = source.keys()
        ctx = None
        srcDict = {}
        if keys:
            for key in keys:
                if key == b'context':
                    ctx = dict((item[0], item[1].asString) for item in source[b'context'].items())
                else:
                    srcDict[key] = html.translation(source.readWideString(key))

        else:
            srcDict[b'text'] = html.translation(source.asWideString)
        return Template(srcDict, ctx)
