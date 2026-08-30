import ResMgr
from gui.wgnc.errors import ParseError
from gui.wgnc.xml import actions_parsers, gui_parsers, shared_parsers, proxy_data_parsers

class _NotificationParser(shared_parsers.SectionParser):
    __slots__ = (b'_actionsParser', b'_guiParser', b'_proxyDataParser')

    def __init__(self, actionsParser, guiParser, proxyDataParser):
        super(_NotificationParser, self).__init__()
        self._actionsParser = actionsParser
        self._guiParser = guiParser
        self._proxyDataParser = proxyDataParser
        return

    def getTagName(self):
        return b'notification'

    def parse(self, section):
        if section.name != self.getTagName():
            raise ParseError((b'Root tag "{0}" is invalid').format(section.name))
        notifyID = section.readInt64(b'notification_id', 0)
        if not notifyID:
            raise ParseError(b'Attribute "notification_id" is not valid.')
        ttl = section.readFloat(b'valid_till', 0.0)
        sub = section[self._actionsParser.getTagName()]
        if sub:
            actionsHolder = self._actionsParser.parse(sub)
        else:
            actionsHolder = None
        sub = section[self._guiParser.getTagName()]
        if sub:
            itemsHolder = self._guiParser.parse(sub)
        else:
            itemsHolder = None
        sub = section[self._proxyDataParser.getTagName()]
        if sub:
            proxyDataItemsHolder = self._proxyDataParser.parse(sub)
        else:
            proxyDataItemsHolder = None
        return (notifyID, ttl, actionsHolder, itemsHolder, proxyDataItemsHolder)


_PARSER_BY_VER = {b'2.0': (
          _NotificationParser,
          (
           actions_parsers.ActionsParser_v2,
           gui_parsers.GUIItemsParser_v2,
           proxy_data_parsers.ProxyDataItemParser_v2))}

def _parse(section):
    ver = section.readString(b'ver', b'')
    if not ver:
        raise ParseError(b'Attribute "ver" is not valid.')
    if ver not in _PARSER_BY_VER:
        raise ParseError((b'That version {0} is not supported.').format(ver))
    clazz, (actionsClazz, guiClazz, proxyDataClazz) = _PARSER_BY_VER[ver]
    return clazz(actionsClazz(), guiClazz(), proxyDataClazz()).parse(section)


def fromString(xml):
    section = ResMgr.DataSection().createSectionFromString(xml)
    if not section:
        raise ParseError(b'Can not read notification')
    return _parse(section)


def fromSection(section):
    if not section:
        raise ParseError(b'Section is empty')
    return _parse(section)
