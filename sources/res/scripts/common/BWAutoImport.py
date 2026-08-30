from __future__ import absolute_import
import collections
from weakref import proxy as _proxy
from WeakMethod import WeakMethodProxy
import inspect

def _fix_base_handler_in_urllib2():
    import functools
    try:
        from urllib2 import BaseHandler
    except ImportError:
        from urllib.request import BaseHandler

    def add_parent(self_, parent):
        self_.parent = _proxy(parent)
        return

    functools.update_wrapper(add_parent, BaseHandler.add_parent)
    setattr(BaseHandler, b'add_parent', add_parent)
    return


def _fix_proxy_handler_in_urllib2():
    try:
        from urllib2 import ProxyHandler
    except ImportError:
        from urllib.request import ProxyHandler

    def wrapper_setattr(self_, key, value):
        if inspect.isfunction(value):
            self_.__dict__[key] = _proxy(value)
        else:
            self_.__dict__[key] = value
        return

    setattr(ProxyHandler, b'__setattr__', wrapper_setattr)
    return


def _fix_http_response_in_urllib2():
    import functools, socket
    try:
        from urllib import addinfourl
        from urllib2 import AbstractHTTPHandler, URLError
    except ImportError:
        from urllib.request import AbstractHTTPHandler
        from urllib.response import addinfourl
        from urllib.error import URLError

    def do_open(self, http_class, req, **http_conn_args):
        host = req.get_host()
        if not host:
            raise URLError(b'no host given')
        h = http_class(host, timeout=req.timeout, **http_conn_args)
        h.set_debuglevel(self._debuglevel)
        headers = dict(req.unredirected_hdrs)
        headers.update(dict((k, v) for k, v in req.headers.items() if k not in headers))
        headers[b'Connection'] = b'close'
        headers = dict((name.title(), val) for name, val in headers.items())
        if req._tunnel_host:
            tunnel_headers = {}
            proxy_auth_hdr = b'Proxy-Authorization'
            if proxy_auth_hdr in headers:
                tunnel_headers[proxy_auth_hdr] = headers[proxy_auth_hdr]
                del headers[proxy_auth_hdr]
            h.set_tunnel(req._tunnel_host, headers=tunnel_headers)
        try:
            h.request(req.get_method(), req.get_selector(), req.data, headers)
        except socket.error as err:
            h.close()
            raise URLError(err)
        else:
            try:
                r = h.getresponse(buffering=True)
            except TypeError:
                r = h.getresponse()

        r.recv = WeakMethodProxy(r.read)
        fp = socket._fileobject(r, close=True)
        resp = addinfourl(fp, r.msg, req.get_full_url())
        resp.code = r.status
        resp.msg = r.reason
        return resp

    functools.update_wrapper(do_open, AbstractHTTPHandler.do_open)
    setattr(AbstractHTTPHandler, b'do_open', do_open)
    return


def _fix_ordered_dict():
    from py2to3.moves.collections.abc import MutableMapping

    class _Link(object):
        __slots__ = (b'prev', b'next', b'key', b'__weakref__')

    class OrderedDict(dict, MutableMapping):

        def __init__(self, *args, **kwds):
            super(OrderedDict, self).__init__()
            if len(args) > 1:
                raise TypeError(b'expected at most 1 arguments, got %d' % len(args))
            try:
                self.__root
            except AttributeError:
                self.__hardroot = _Link()
                self.__root = root = _proxy(self.__hardroot)
                root.prev = root.next = root
                self.__map = {}

            self.update(*args, **kwds)
            return

        def __setitem__(self, key, value, dict_setitem=dict.__setitem__, proxy=_proxy, Link=_Link):
            if key not in self:
                self.__map[key] = link = Link()
                root = self.__root
                last = root.prev
                link.prev, link.next, link.key = last, root, key
                last.next = link
                root.prev = proxy(link)
            dict.__setitem__(self, key, value)
            return

        def __delitem__(self, key, dict_delitem=dict.__delitem__):
            dict_delitem(self, key)
            link = self.__map.pop(key)
            link_prev = link.prev
            link_next = link.next
            link_prev.next = link_next
            link_next.prev = link_prev
            return

        def __iter__(self):
            root = self.__root
            curr = root.next
            while curr is not root:
                yield curr.key
                curr = curr.next

            return

        def iteritems(self):
            for key in self:
                yield (
                 key, self[key])

            return

        def itervalues(self):
            for key in self:
                yield self[key]

            return

        def __reversed__(self):
            root = self.__root
            curr = root.prev
            while curr is not root:
                yield curr.key
                curr = curr.prev

            return

        def __reduce__(self):
            items = [[k, self[k]] for k in self]
            tmp = (self.__map, self.__root)
            del self.__map
            del self.__root
            inst_dict = vars(self).copy()
            self.__map, self.__root = tmp
            if inst_dict:
                return (self.__class__, (items,), inst_dict)
            return (
             self.__class__, (items,))

        def clear(self):
            root = self.__root
            root.prev = root.next = root
            self.__map.clear()
            dict.clear(self)
            return

        def popitem(self, last=True):
            if not self:
                raise KeyError(b'dictionary is empty')
            root = self.__root
            if last:
                link = root.prev
                link_prev = link.prev
                link_prev.next = root
                root.prev = link_prev
            else:
                link = root.next
                link_next = link.next
                root.next = link_next
                link_next.prev = root
            key = link.key
            del self.__map[key]
            value = dict.pop(self, key)
            return (key, value)

        def move_to_end(self, key, last=True):
            link = self.__map[key]
            link_prev = link.prev
            link_next = link.next
            link_prev.next = link_next
            link_next.prev = link_prev
            root = self.__root
            if last:
                last = root.prev
                link.prev = last
                link.next = root
                last.next = root.prev = link
            else:
                first = root.next
                link.prev = root
                link.next = first
                root.next = first.prev = link
            return

        iterkeys = __iter__
        setdefault = MutableMapping.setdefault
        update = MutableMapping.update
        pop = MutableMapping.pop
        keys = MutableMapping.keys
        values = MutableMapping.values
        items = MutableMapping.items
        __ne__ = MutableMapping.__ne__
        __hash__ = None

        def __repr__(self):
            if not self:
                return b'%s()' % (self.__class__.__name__,)
            return b'%s(%r)' % (self.__class__.__name__, list(self.items()))

        def copy(self):
            return self.__class__(self)

        @classmethod
        def fromkeys(cls, iterable, value=None):
            d = cls()
            for key in iterable:
                d[key] = value

            return d

        def __eq__(self, other):
            if isinstance(other, OrderedDict):
                return len(self) == len(other) and all(p == q for p, q in zip(self.items(), other.items()))
            return dict.__eq__(self, other)

    collections.OrderedDict = OrderedDict
    return


def _fixed_asdict(t):
    return dict(zip(t._fields, t))


def _fix_namedtuple():
    from collections import namedtuple as _orig_namedtuple
    import sys as _sys

    def _fixed_namedtuple(*args, **kwargs):
        res = _orig_namedtuple(*args, **kwargs)
        res._asdict = _fixed_asdict
        try:
            res.__module__ = _sys._getframe(1).f_globals.get(b'__name__', b'__main__')
        except (AttributeError, ValueError):
            pass

        return res

    collections.namedtuple = _fixed_namedtuple
    return


_fix_base_handler_in_urllib2()
_fix_proxy_handler_in_urllib2()
_fix_http_response_in_urllib2()
_fix_ordered_dict()
_fix_namedtuple()
