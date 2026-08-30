from debug_utils import LOG_WARNING
from gui.wgnc.settings import WGNC_POP_UP_PRIORITIES
from gui.wgnc.xml.format_by_tags import formatText
from gui.wgnc.xml.shared_parsers import ParsersCollection, SectionParser
from gui.wgnc import gui_items

class _ButtonsParser(SectionParser):

    def getTagName(self):
        return b'buttons'

    def parse(self, section):
        result = []
        for name, sub in section.items():
            if name != b'button':
                continue
            label = sub.asString
            if not label:
                LOG_WARNING(b'Button section is not valid, label is empty', sub.asBinary)
                continue
            actions = sub.readString(b'actions')
            if not actions:
                LOG_WARNING(b'Button section is not valid, actions is empty', sub.asBinary)
                continue
            result.append((label, actions))

        return result


class _GUIActionsParser(SectionParser):

    def getTagName(self):
        return b'handlers'

    def parse(self, section):
        result = []
        for name, sub in section.items():
            if name != b'handler':
                continue
            gui_event = sub.readString(b'gui_event')
            if not gui_event:
                LOG_WARNING(b'Handler section is not valid, gui_event is empty', sub.asBinary)
                continue
            actions = sub.readString(b'actions')
            if not actions:
                LOG_WARNING(b'Handler section is not valid, actions is empty', sub.asBinary)
                continue
            result.append((gui_event, actions))

        return result


class _PopUpParser(SectionParser):

    def getTagName(self):
        return b'popup'

    def parse(self, section):
        body = formatText(self._readString(b'body', section))
        priority = self._readString(b'priority', section)
        if priority not in WGNC_POP_UP_PRIORITIES:
            LOG_WARNING(b'Priority of pop up is not valid, uses default priority', priority)
            priority = b'medium'
        topic = formatText(section.readWideString(b'topic', u''))
        icon = section.readString(b'icon', b'')
        bg = section.readString(b'bg', b'')
        group = section.readString(b'group', b'info')
        isNotify = section.readBool(b'isNotify', True)
        sub = _ButtonsParser()
        if sub.getTagName() in section.keys():
            buttons = sub.parse(section[sub.getTagName()])
        else:
            buttons = None
        return gui_items.PopUpItem(body, topic, priority, buttons, icon, bg, group, isNotify)


class _WindowParser(SectionParser):
    __slots__ = (b'_itemClass',)

    def __init__(self, itemClass=gui_items.WindowItem):
        super(_WindowParser, self).__init__()
        self._itemClass = itemClass
        return

    def getTagName(self):
        return b'window'

    def parse(self, section):
        name = self._readString(b'name', section)
        body = formatText(self._readString(b'body', section))
        topic = section.readString(b'topic', b'')
        isModal = section.readBool(b'modal', False)
        isHidden = section.readBool(b'hidden', True)
        sub = _ButtonsParser()
        if sub.getTagName() in section.keys():
            buttons = sub.parse(section[sub.getTagName()])
        else:
            buttons = None
        return self._itemClass(name, body, topic, buttons, isModal, isHidden)


class _PollParser(_WindowParser):

    def __init__(self, itemClass=gui_items.PollItem):
        super(_PollParser, self).__init__(itemClass)
        return

    def getTagName(self):
        return b'poll'


class _BrowserParser(SectionParser):

    def getTagName(self):
        return b'browser'

    def parse(self, section):
        sub = _GUIActionsParser()
        if sub.getTagName() in section.keys():
            handlers = sub.parse(section[sub.getTagName()])
        else:
            handlers = None
        return gui_items.BrowserItem(name=self._readString(b'name', section), body=self._readString(b'href', section), handlers=handlers, hidden=section.readBool(b'hidden', True), topic=section.readWideString(b'topic', u''))


class _GUIItemsParser(ParsersCollection):

    def getTagName(self):
        return b'gui'

    def parse(self, section):
        items = []
        for item in super(_GUIItemsParser, self).parse(section):
            items.append(item)

        return gui_items.GUIHolder(items)


class GUIItemsParser_v2(_GUIItemsParser):

    def __init__(self):
        super(GUIItemsParser_v2, self).__init__((
         _PopUpParser(),
         _WindowParser(),
         _PollParser(),
         _BrowserParser()))
        return
