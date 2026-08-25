import resource_helper
from gui.wgnc import actions
from gui.wgnc.wgnc_helpers import parseSize
from gui.wgnc.errors import ParseError
from gui.wgnc.xml.shared_parsers import SectionParser, ParsersCollection

class _CallbackActionParser(SectionParser):

    def getTagName(self):
        return b'callback'

    def parse(self, section):
        return actions.Callback(self._readString(b'name', section), section.readBool(b'purge', True))


class _BrowseActionParser(SectionParser):

    def getTagName(self):
        return b'browse'

    def parse(self, section):
        name = self._readString(b'name', section)
        url = self._readString(b'href', section)
        target = section.readString(b'target', b'internal')
        if target == b'internal':
            size = parseSize(section.readString(b'size'))
            showRefresh = section.readBool(b'show_refresh')
            webClientHandler = section.readString(b'web_client_handler')
            isSolidBorder = section.readBool(b'is_solid_border')
            action = actions.OpenInternalBrowser(name, url, size, showRefresh, webClientHandler, isSolidBorder)
        elif target == b'external':
            action = actions.OpenExternalBrowser(name, url)
        elif target == b'promo':
            action = actions.OpenPromoBrowser(name, url)
        elif target == b'stronghold':
            action = actions.OpenStrongholdBrowser(name, url)
        elif target == b'ranked':
            action = actions.OpenRankedBrowser(name, url)
        else:
            raise ParseError((b'The target of action "{0}" is not valid: {1}.').format(self.getTagName(), target))
        return action


class _OpenWindowParser(SectionParser):

    def getTagName(self):
        return b'openwindow'

    def parse(self, section):
        return actions.OpenWindow(self._readString(b'name', section), self._readString(b'target', section))


class _CustomActionsParser(SectionParser):

    def getTagName(self):
        return b'custom_action'

    def parse(self, section):
        ctx, _ = resource_helper.getRoot(b'')
        return actions.CustomAction(action_name=self._readString(b'name', section), **self.__parse(ctx, section))

    def __parse(self, ctx, section):
        res = {}
        for c, ss in resource_helper.getIterator(ctx, section):
            val = resource_helper.readItem(c, ss, ss.name).value
            res[self.__getKeyName(ss)] = val if val else self.__parse(c, ss)

        if not res:
            res[self.__getKeyName(section)] = resource_helper.readItem(ctx, section, section.name).value
        if b'action_class' not in res.keys():
            res[b'action_class'] = resource_helper.readItem(ctx, section, section.name).value
        return res

    def __getKeyName(self, section):
        if section[b'name'] is not None:
            return section[b'name'].asString
        else:
            return section.name


class _ReplaceButtonsAction(SectionParser):

    def getTagName(self):
        return b'replace_buttons'

    def parse(self, section):
        text = section.asString
        if not text:
            raise ParseError((b'The content of action "{0}" is not defined.').format(self.getTagName()))
        return actions.ReplaceButtons(self._readString(b'name', section), section.asString)


class _ActionsParser(ParsersCollection):

    def getTagName(self):
        return b'actions'

    def parse(self, section):
        items = []
        for item in super(_ActionsParser, self).parse(section):
            items.append(item)

        return actions.ActionsHolder(items)


class ActionsParser_v2(_ActionsParser):

    def __init__(self):
        super(ActionsParser_v2, self).__init__((
         _CallbackActionParser(),
         _BrowseActionParser(),
         _OpenWindowParser(),
         _ReplaceButtonsAction(),
         _CustomActionsParser()))
        return
