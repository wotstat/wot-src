import BigWorld

def getVOIPManager():
    if not globals().has_key(b'__handler'):
        from VOIPManager import VOIPManager
        globals()[b'__handler'] = VOIPManager()
        BigWorld.VOIP.setHandler(__handler)
    return __handler
