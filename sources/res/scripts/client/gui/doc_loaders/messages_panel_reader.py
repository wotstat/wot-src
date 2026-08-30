from __future__ import absolute_import
from helpers import html
import resource_helper
_EXPECTED_STYLES = {b'entityStyle': (b'fontSize', b'fontFace', b'fontColor')}

def _getDefaultSettings():
    return {b'direction': b'up', 
       b'lifeTime': 1000, 
       b'alphaSpeed': 1000, 
       b'maxLinesCount': 5, 
       b'poolSettings': (), 
       b'textBottomPadding': 0.0, 
       b'textRightPadding': 0.0, 
       b'useHtml': False, 
       b'showUniqueOnly': False, 
       b'messageGap': 0}


def _readSettings(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, b'settings')
    settings = _getDefaultSettings()
    for xmlCtx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(xmlCtx, subSection, b'setting')
        settings[item.name] = item.value

    return settings


def _readStyles(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, b'styles', safe=True)
    styles = {}
    if section is not None:
        for xmlCtx, subSection in resource_helper.getIterator(ctx, section):
            item = resource_helper.readItem(xmlCtx, subSection, b'style')
            expectedKeys = _EXPECTED_STYLES[item.name]
            for key in expectedKeys:
                pass

            styles[item.name] = item.value

    return styles


def _readMessages(ctx, root):
    ctx, section = resource_helper.getSubSection(ctx, root, b'messages')
    messages = {}
    for xmlCtx, subSection in resource_helper.getIterator(ctx, section):
        item = resource_helper.readItem(xmlCtx, subSection, b'message')
        text, aliases = item.value
        aliases = aliases.split(b',', 1)
        if len(aliases) == 1:
            aliases *= 2
        messages[item.name] = (html.translation(text), tuple(aliases))

    return messages


_cache = {}

def readXML(path):
    global _cache
    if path in _cache:
        return _cache[path]
    ctx, root = resource_helper.getRoot(path)
    settings = _readSettings(ctx, root)
    styles = _readStyles(ctx, root)
    messages = _readMessages(ctx, root)
    _cache[path] = (
     settings, styles, messages)
    return (
     settings, styles, messages)
