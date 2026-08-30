import BigWorld

def getVOIPManager():
    if not globals().has_key(b'handler'):
        from VOIP.VOIPSingleton import VOIPSingleton
        globals()[b'handler'] = VOIPSingleton()
        BigWorld.VOIP.setHandler(handler)
    return handler


def isOSSupported():
    return BigWorld.VOIP.isOSSupported()
