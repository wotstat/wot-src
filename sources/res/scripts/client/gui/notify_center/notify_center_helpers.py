from debug_utils import LOG_ERROR
from gui.shared.view_helpers.UsersInfoHelper import UsersInfoHelper

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


def spa2Nickname(value):
    helper = UsersInfoHelper()
    contact = helper.getContact(value)
    name = (b'<font color="#DFDFDF">{}</font>').format(contact.getName())
    clanAbbrev = (b'<font color="#8C8C7E">[{}]</font>').format(contact.getClanAbbrev()) if contact.getClanAbbrev() else b''
    return (b'{}{}').format(name, clanAbbrev)
