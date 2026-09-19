from __future__ import absolute_import
import BigWorld

def getVOIPManager():
    if not globals().has_key(b'__handler'):
        from VOIP.VOIPManager import VOIPManager
        globals()[b'__handler'] = VOIPManager()
    return __handler
