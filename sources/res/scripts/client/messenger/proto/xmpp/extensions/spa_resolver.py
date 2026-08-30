from messenger.proto.xmpp.extensions import PyExtension, PyQuery
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.shared_handlers import IQChildHandler
from messenger.proto.xmpp.gloox_constants import IQ_TYPE

class SpaResolverError(PyExtension):

    def __init__(self):
        super(SpaResolverError, self).__init__(_TAG.ERROR)
        return

    @classmethod
    def getDefaultData(cls):
        return b''

    def getTag(self):
        return b''

    def parseTag(self, pyGlooxTag):
        return pyGlooxTag.getCData()


class SpaResolverItem(PyExtension):

    def __init__(self, dbID=0, nickname=b''):
        super(SpaResolverItem, self).__init__(_TAG.ITEM)
        if dbID:
            self.setAttribute(b'id', dbID)
        if nickname:
            self.setAttribute(b'nickname', nickname)
        self.setChild(SpaResolverError())
        return

    @classmethod
    def getDefaultData(cls):
        return (0, b'', SpaResolverError.getDefaultData())

    def parseTag(self, pyGlooxTag):
        dbID = pyGlooxTag.findAttribute(b'id')
        if dbID:
            dbID = long(dbID)
        else:
            dbID = 0
        nickname = pyGlooxTag.findAttribute(b'nickname')
        error = self._getChildData(pyGlooxTag, 0, SpaResolverError.getDefaultData())
        return (
         dbID, nickname, error)


class SpaResolverQuery(PyExtension):

    def __init__(self, items=None):
        super(SpaResolverQuery, self).__init__(_TAG.QUERY)
        self.setXmlNs(_NS.WG_SPA_RESOLVER)
        items = items or tuple()
        for item in items:
            self.setChild(item)

        return

    @classmethod
    def getDefaultData(cls):
        return []


class SpaResolverByIDsQuery(PyQuery):

    def __init__(self, dbIDs):
        super(SpaResolverByIDsQuery, self).__init__(IQ_TYPE.GET, SpaResolverQuery(items=[SpaResolverItem(dbID, b'') for dbID in dbIDs]))
        return


class SpaResolverHandler(IQChildHandler):

    def __init__(self):
        super(SpaResolverHandler, self).__init__(SpaResolverQuery((SpaResolverItem(),)))
        return
