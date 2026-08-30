from debug_utils import LOG_ERROR

def parseSize(sizeStr):
    if sizeStr:
        try:
            size = tuple(map(int, sizeStr.split(b'x')))
            if len(size) != 2:
                return
        except ValueError:
            LOG_ERROR(b'Failed to parse size: %s' % sizeStr)
            size = None

    else:
        size = None
    return size
