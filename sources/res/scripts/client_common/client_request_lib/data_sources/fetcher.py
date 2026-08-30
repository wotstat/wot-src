from __future__ import absolute_import
from soft_exception import SoftException

class FakeResponse(object):

    def __init__(self, r):
        self.responseCode = r.status_code
        self.body = r.raw.read()
        self._headers = r.headers
        return

    def headers(self):
        return self._headers

    def __repr__(self):
        return (b'[HTTP status: {}] {}').format(self.responseCode, self.body)


def fetchURL(url, callback, headers=None, timeout=30, method=b'GET', postData=b''):
    import requests
    headers = headers or {}
    data = postData
    if isinstance(headers, (list, tuple)):
        res = {}
        for header in headers:
            a, b = header.split(b':')
            res[a] = b

        headers = res
    if not isinstance(data, str) and data is not None:
        raise SoftException((b'Unsupported parameter {}').format(data))
    methods = {b'GET': (requests.get), 
       b'PUT': (requests.put), 
       b'POST': (requests.post), 
       b'PATCH': (requests.patch), 
       b'DELETE': (requests.delete)}
    if method in methods:
        response = methods[method](url, headers=headers, data=data, verify=False, stream=True)
    else:
        raise SoftException((b'Unsupported method {}').format(method))
    callback(FakeResponse(response))
    return
