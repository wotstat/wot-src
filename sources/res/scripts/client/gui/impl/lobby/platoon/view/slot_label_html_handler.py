import json
from HTMLParser import HTMLParser
from gui.impl.gen.view_models.views.lobby.platoon.slot_label_element_model import Types

def getStyle(attrs):
    result = {}
    if attrs.get(b'width'):
        result[b'width'] = (b'{}rem').format(attrs.get(b'width'))
    if attrs.get(b'height'):
        result[b'height'] = (b'{}rem').format(attrs.get(b'height'))
    if attrs.get(b'vspace'):
        result[b'marginTop'] = (b'{}rem').format(attrs.get(b'vspace'))
        result[b'marginBottom'] = (b'{}rem').format(attrs.get(b'vspace'))
    if attrs.get(b'hspace'):
        result[b'marginLeft'] = (b'{}rem').format(attrs.get(b'hspace'))
        result[b'marginRight'] = (b'{}rem').format(attrs.get(b'hspace'))
    if attrs.get(b'src'):
        result[b'background'] = (b'url({}) center / contain no-repeat').format(attrs.get(b'src'))
    if attrs.get(b'size'):
        result[b'fontSize'] = (b'{}rem').format(attrs.get(b'size'))
    if attrs.get(b'color'):
        result[b'color'] = attrs.get(b'color')
    return json.dumps(result)


class SlotLabelHtmlParser(HTMLParser, object):

    def __init__(self):
        super(SlotLabelHtmlParser, self).__init__()
        self.parsingResult = []
        return

    def handle_starttag(self, tag, attrs):
        self.parsingResult.append({b'tag': tag, b'attrs': (self.__attrsToDict(attrs))})
        return

    def handle_data(self, data):
        self.parsingResult.append({b'tag': b'', b'data': data})
        return

    def getElements(self):
        result = []
        for index, entry in enumerate(self.parsingResult):
            entryTag = entry.get(b'tag')
            if entryTag == b'img':
                result.append({b'type': (Types.IMAGE), b'style': (getStyle(entry.get(b'attrs')))})
            elif entryTag == b'br':
                result.append({b'type': (Types.TEXT), b'text': b'\n'})
            elif entryTag == b'':
                data = entry.get(b'data')
                if data == b' ':
                    continue
                data = {b'type': (Types.TEXT), b'text': data}
                if index > 0 and self.parsingResult[index - 1].get(b'tag') == b'font':
                    data[b'style'] = getStyle(self.parsingResult[index - 1].get(b'attrs'))
                result.append(data)

        return result

    @staticmethod
    def __attrsToDict(attrs):
        return {parameter: value for parameter, value in attrs}
