from messenger.proto.xmpp.extensions import PyHandler

class IQHandler(PyHandler):

    def getFilterString(self):
        return (b'/iq/{0}').format(self._ext.getXPath())


class IQChildHandler(PyHandler):
    __slots__ = (b'_index',)

    def __init__(self, ext, index=0):
        super(IQChildHandler, self).__init__(ext)
        self._index = index
        return

    def getFilterString(self):
        return (b'/iq/{0}').format(self._ext.getXPath(self._index))

    def handleTag(self, pyGlooxTag):
        child = self._ext.getChild(self._index)
        if not child:
            return
        result = pyGlooxTag.filterXPath(self.getFilterString())
        for tag in result:
            data = child.parseTag(tag)
            if data:
                yield data

        return


class ProxyHandler(PyHandler):

    def getFilterString(self):
        return self._ext.getXPath()
