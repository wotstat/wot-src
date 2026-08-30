from collections import namedtuple
from messenger.proto.xmpp.extensions import PyQuery, PyExtension
from messenger.proto.xmpp.extensions.disco import CreatedByElement
from messenger.proto.xmpp.extensions.shared_handlers import IQChildHandler
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG, XML_NAME_SPACE as _NS
from messenger.proto.xmpp.entities import XMPPMucChannelEntity
from messenger.proto.xmpp.extensions.spa_resolver import SpaResolverItem
from messenger.proto.xmpp.extensions.custom_items import SharedExtension
from messenger.proto.xmpp.gloox_constants import IQ_TYPE
XmppUserSearchInfo = namedtuple(b'XmppUserSearchInfo', b'dbId, nickname, clanInfo')

class _SimpleCriterionExtension(PyExtension):

    def __init__(self, name, value):
        super(_SimpleCriterionExtension, self).__init__(_TAG.CRITERION)
        self.setAttribute(b'name', name)
        self.setAttribute(b'value', value)
        return


class ChannelSearchQuery(PyQuery):

    def __init__(self, token, to=b'', count=50):
        super(ChannelSearchQuery, self).__init__(IQ_TYPE.GET, to=to)
        self._token = token
        self._results_count = count
        self._ext = self.__initExtension()
        return

    def __initExtension(self):
        filterExtension = PyExtension(_TAG.FILTER).setXmlNs(_NS.EXT_MUC_ROOMS).setAttribute(b'roomname-prefix', self._token).setAttribute(b'max-entries', self._results_count)
        filterExtension.setChild(_SimpleCriterionExtension(b'muc#roomconfig_membersonly', 0))
        return PyExtension(_TAG.QUERY).setXmlNs(_NS.DISCO_ITEMS).setChild(filterExtension)


class ChannelsListHandler(IQChildHandler):

    def __init__(self):
        super(ChannelsListHandler, self).__init__(PyExtension(_TAG.QUERY).setXmlNs(_NS.DISCO_ITEMS).setChild(ChannelItemExtension()))
        return


class ChannelItemExtension(PyExtension):

    def __init__(self):
        super(ChannelItemExtension, self).__init__(_TAG.ITEM)
        self.setChild(CreatedByElement())
        return

    def parseTag(self, pyGlooxTag):
        jid = pyGlooxTag.findAttribute(b'jid')
        name = pyGlooxTag.findAttribute(b'name')
        return XMPPMucChannelEntity(jid, name)


class UsersSearchQuery(PyQuery):

    def __init__(self, token, to=b''):
        super(UsersSearchQuery, self).__init__(IQ_TYPE.GET, to=to)
        self._nickname = token
        self._ext = self.__initExtension()
        return

    def __initExtension(self):
        filterExtension = PyExtension(_TAG.ITEM).setXmlNs(_NS.SPA_RESOLVER).setAttribute(b'nickname', self._nickname)
        return PyExtension(_TAG.QUERY).setXmlNs(_NS.SPA_RESOLVER).setChild(filterExtension)


class UserSearchHandler(IQChildHandler):

    def __init__(self):
        super(UserSearchHandler, self).__init__(PyExtension(_TAG.QUERY).setXmlNs(_NS.SPA_RESOLVER).setChild(UserSearchItemExtension()))
        return


class NicknamePrefixSearchQuery(PyQuery):

    def __init__(self, token, limit=50, to=b''):
        super(NicknamePrefixSearchQuery, self).__init__(IQ_TYPE.GET, to=to)
        self._prefix = token
        self._limit = limit
        self._ext = self.__initExtension()
        return

    def __initExtension(self):
        return PyExtension(_TAG.NICKNAME_PREFIX_SEARCH).setXmlNs(_NS.SPA_RESOLVER).setAttribute(b'prefix', self._prefix).setAttribute(b'limit', self._limit)


class NicknamePrefixSearchHandler(IQChildHandler):

    def __init__(self):
        super(NicknamePrefixSearchHandler, self).__init__(PyExtension(_TAG.NICKNAME_PREFIX_SEARCH).setXmlNs(_NS.SPA_RESOLVER).setChild(UserSearchItemExtension()))
        return


class UserSearchItemExtension(SpaResolverItem):

    def __init__(self):
        super(UserSearchItemExtension, self).__init__(_TAG.ITEM)
        self.setChild(SharedExtension())
        return

    @classmethod
    def getDefaultData(cls):
        return (SpaResolverItem.getDefaultData(), SharedExtension.getDefaultData())

    def parseTag(self, pyGlooxTag):
        dbId, nickname, _ = super(UserSearchItemExtension, self).parseTag(pyGlooxTag)
        info = self._getChildData(pyGlooxTag, 1, SharedExtension.getDefaultData())
        if b'clanInfo' in info:
            clanInfo = info[b'clanInfo']
        else:
            clanInfo = None
        return XmppUserSearchInfo(dbId, nickname, clanInfo)
