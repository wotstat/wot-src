import typing
from constants import GF_RES_PROTOCOL
from gui.shared.utils.functions import getAbsoluteUrl

def getGfImagePath(imgPath):
    if imgPath is None:
        return
    else:
        newPath = getAbsoluteUrl(imgPath)
        newPath = newPath.replace(b'\\', b'/')
        if not newPath.startswith(GF_RES_PROTOCOL.IMG):
            newPath = (b'').join([GF_RES_PROTOCOL.IMG, newPath])
        return newPath
