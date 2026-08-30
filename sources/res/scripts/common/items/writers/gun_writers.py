from __future__ import absolute_import
from items import _xml
from items.writers import shared_writers

def writeRecoilEffect(item, section, cache):
    if item is None:
        return
    else:
        if item.effectName != b'none':
            _xml.rewriteString(section, b'recoilEffect', item.effectName)
            section.deleteSection(b'backoffTime')
            section.deleteSection(b'returnTime')
        else:
            _xml.rewriteFloat(section, b'backoffTime', item.backoffTime)
            _xml.rewriteFloat(section, b'returnTime', item.returnTime)
            section.deleteSection(b'recoilEffect')
        _xml.rewriteFloat(section, b'amplitude', item.amplitude)
        shared_writers.writeLodDist(item.lodDist, section, b'lodDist', cache)
        return
