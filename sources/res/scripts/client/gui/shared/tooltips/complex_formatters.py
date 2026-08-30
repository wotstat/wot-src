from __future__ import absolute_import
from gui import makeHtmlString
from gui.shared.utils.functions import stripColorTagDescrTags
from helpers import i18n
_TEXT_FORMAT = b"{0[0]}{1}{0[1]}\n<font size='1' > </font>\n"
_TOOLTIP_KIND = (b'header', b'body', b'note', b'attention')
_BLOCK_TAGS_MAP = {b'HEADER': {b'INFO': (
                       makeHtmlString(b'html_templates:lobby/tooltips_complex', b'header_info_start'),
                       makeHtmlString(b'html_templates:lobby/tooltips_complex', b'header_info_end')), 
               b'WARNING': (
                          makeHtmlString(b'html_templates:lobby/tooltips_complex', b'header_warning_start'),
                          makeHtmlString(b'html_templates:lobby/tooltips_complex', b'header_warning_end'))}, 
   b'BODY': {b'INFO': (
                     makeHtmlString(b'html_templates:lobby/tooltips_complex', b'body_info_start'),
                     makeHtmlString(b'html_templates:lobby/tooltips_complex', b'body_info_end')), 
             b'WARNING': (
                        makeHtmlString(b'html_templates:lobby/tooltips_complex', b'body_warning_start'),
                        makeHtmlString(b'html_templates:lobby/tooltips_complex', b'body_warning_end'))}, 
   b'NOTE': {b'INFO': (
                     makeHtmlString(b'html_templates:lobby/tooltips_complex', b'note_info_start'),
                     makeHtmlString(b'html_templates:lobby/tooltips_complex', b'note_info_end')), 
             b'WARNING': [
                        makeHtmlString(b'html_templates:lobby/tooltips_complex', b'note_warning_start'),
                        makeHtmlString(b'html_templates:lobby/tooltips_complex', b'note_warning_end')]}, 
   b'ATTENTION': {b'INFO': (
                          makeHtmlString(b'html_templates:lobby/tooltips_complex', b'attention_info_start'),
                          makeHtmlString(b'html_templates:lobby/tooltips_complex', b'attention_info_end')), 
                  b'WARNING': (
                             makeHtmlString(b'html_templates:lobby/tooltips_complex', b'attention_warning_start'),
                             makeHtmlString(b'html_templates:lobby/tooltips_complex', b'attention_warning_end'))}}

def _getTags(blockType, formatType):
    blockTag = _BLOCK_TAGS_MAP[blockType]
    if formatType in blockTag:
        return blockTag[formatType]
    return (b'', b'')


def _getFormattedText(text, blockType, formatType):
    if formatType is None:
        formatType = b'INFO'
    tags = _getTags(blockType, formatType)
    return _TEXT_FORMAT.format(tags, text)


def _doFormatToolTipFromKey(tooltipID, formatType):
    result = []
    for kind in _TOOLTIP_KIND:
        contentKey = (b'{}/{}').format(tooltipID, kind)
        content = i18n.makeString(contentKey)
        subkey = contentKey[1:].split(b':', 1)
        if content and subkey and content != subkey[1]:
            result.append(_getFormattedText(content, kind.upper(), formatType))

    return (b'').join(result)


def _doFormatToolTipFromText(tooltipID, formatType):
    result = b''
    for tooltipKind in _TOOLTIP_KIND:
        tooltipBlock = tooltipKind.upper()
        tags = {b'open': (b'{' + tooltipBlock + b'}'), 
           b'close': (b'{/' + tooltipBlock + b'}')}
        indicies = {b'start': (tooltipID.find(tags[b'open'])), 
           b'end': (tooltipID.find(tags[b'close']))}
        if indicies[b'start'] != -1 and indicies[b'end'] != -1:
            indicies[b'start'] += len(tags[b'open'])
            result += _getFormattedText(stripColorTagDescrTags(tooltipID[indicies[b'start']:indicies[b'end']]), tooltipBlock, formatType)

    return result


def doFormatData(data, formatType):
    result = []
    for kind in _TOOLTIP_KIND:
        if kind in data and data[kind] is not None:
            result.append(_getFormattedText(data[kind], kind.upper(), formatType))

    return (b'').join(result)


def doFormatToolTip(tooltipID, formatType):
    if not tooltipID:
        return b''
    if tooltipID.startswith(b'#'):
        return _doFormatToolTipFromKey(tooltipID, formatType)
    return _doFormatToolTipFromText(tooltipID, formatType)
